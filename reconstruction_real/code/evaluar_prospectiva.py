#!/usr/bin/env python3
"""EVALUAR PROSPECTIVA ACO-A — congelar → evaluar al cierre de la ventana.

El script que se corre en (o después de) el 2027-09-30 para evaluar la
prueba prospectiva sellada (preregistro df888d0 + ADENDA 1-4). Aplica
los criterios FIJOS a la cohorte congelada v2 contra los datos frescos
de la ventana; no recalibra nada.

Criterios vigentes (consolidados tras las ADENDA 2 y 4):
  P1a  ≥ 1 colapso crudo (firma h(τ) > 0; peso evidencial BAJO, ADENDA 2)
  FRACCIÓN  descriptiva del régimen — SIN compuerta (ADENDA 4: la banda
       P1b [10%, 60%] quedó RETIRADA; habría falsado en 3/4 ventanas
       históricas porque mide el ciclo del mercado, no h(τ))
  P2   mediana de Δ de los colapsos maduros dentro de [−3.270, −0.115]
  P3   ortogonalidad DEMOSTRADA solo si el IC95 de ρ(b, Δ) cabe entero
       en (−0.3, +0.3) — TOST (ADENDA 2); si cruza: INCONCLUSO a ese n

Receta de las magnitudes (ADENDA 1): madurez ≥ 120 días por lado;
b = nacimiento → ATH; Δ = ATH → siguiente valle.

Uso (datos de la ventana: archivo de cierres fresco, descargado con
descargar_binance_klines.py o provisto por el operador):
    python reconstruction_real/code/evaluar_prospectiva.py <cierres.csv.gz> [fin_ventana]

Por defecto: fin = 2027-09-30, cohorte = cohorte v2 (corte 2026-09-30).
"""

import csv
import gzip
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parent.parent.parent
COHORTE = (ROOT / "reconstruction_real" / "data"
           / "cohorte_congelada_cripto_2026-10-26_v2.csv")
CORTE_COHORTE = "2026-09-30"
FIN_DEFECTO = "2027-09-30"
P2_LO, P2_HI = -3.270, -0.115
P3_UMBRAL = 0.3


def fit_loglog(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = min(len(x), len(y))
    x, y = x[:n], y[:n]
    ok = (x > 0) & (y > 0)
    x, y = x[ok], y[ok]
    if len(x) < 20:
        return None
    return float(np.polyfit(np.log(x), np.log(y), 1)[0])


def evaluar(ruta_datos, fin=FIN_DEFECTO,
            ruta_cohorte=None, corte_cohorte=None):
    """Evalúa la ventana sellada contra la cohorte congelada.
    Devuelve dict con: candidatos, colapsos_crudos, colapsos_maduros,
    fraccion_pct, mediana_delta, rho_b_delta, ic95_inf, ic95_sup.
    (None en los que no apliquen)."""
    ruta_cohorte = Path(ruta_cohorte) if ruta_cohorte else COHORTE
    corte_cohorte = corte_cohorte or CORTE_COHORTE
    cohorte = list(csv.DictReader(ruta_cohorte.open()))
    for c in cohorte:
        c["ath_corte"] = float(c["ath_corte"])
        c["precio_corte"] = float(c["precio_corte"])

    series = defaultdict(list)
    with gzip.open(ruta_datos, "rt") as f:
        for row in csv.DictReader(f):
            series[row["par"]].append((row["fecha"], float(row["close"])))
    for par in series:
        series[par].sort()

    colapsos_crudos = 0
    maduros = []
    candidatos = 0
    for c in cohorte:
        par = c["par"]
        puntos = series.get(par, [])
        if not puntos:
            continue
        hasta = [p for p in puntos if p[0] <= corte_cohorte]
        if not hasta:
            continue
        precio_corte = hasta[-1][1]
        if 100 * (1 - precio_corte / c["ath_corte"]) >= 99:
            continue
        candidatos += 1
        despues = [p for p in puntos if corte_cohorte < p[0] <= fin]
        if not despues:
            continue
        fin_precio = despues[-1][1]
        min_ventana = min(p[1] for p in despues)
        if not (min_ventana < 0.01 * c["ath_corte"]
                and fin_precio < 0.01 * c["ath_corte"]):
            continue
        colapsos_crudos += 1
        # FIX (validación del operador, 2026-10-26): b con el ATH
        # CONGELADO de la cohorte; ATH y valle de Δ DENTRO de la ventana.
        puntos_hasta_ath = [p for p in puntos if p[0] <= c["fecha_ath"]]
        if len(puntos_hasta_ath) < 121:
            continue
        precios_vent = np.array([p[1] for p in puntos if p[0] <= fin])
        idx_ath = None
        for i, p2 in enumerate(puntos):
            if p2[0] > c["fecha_ath"]:
                idx_ath = i - 1
                break
        if idx_ath is None or len(precios_vent) - idx_ath < 121:
            continue
        b = fit_loglog(np.arange(1, idx_ath + 2, dtype=float),
                       precios_vent[:idx_ath + 1])
        ventana_baja = precios_vent[idx_ath:]
        if len(ventana_baja) < 20:
            continue
        fin_valle = idx_ath + max(int(np.argmin(ventana_baja)), 1)
        d = fit_loglog(np.arange(1, fin_valle - idx_ath + 1, dtype=float),
                       precios_vent[idx_ath:fin_valle + 1])
        if b is None or d is None:
            continue
        maduros.append((par, b, d))

    res = {
        "candidatos": candidatos,
        "colapsos_crudos": colapsos_crudos,
        "colapsos_maduros": len(maduros),
        "fraccion_pct": round(100 * colapsos_crudos / candidatos,
                              2) if candidatos else None,
        "mediana_delta": None, "rho_b_delta": None,
        "ic95_inf": None, "ic95_sup": None,
    }
    if maduros:
        ds = [m[2] for m in maduros]
        res["mediana_delta"] = round(float(np.median(ds)), 4)
        if len(maduros) >= 5:
            rho, _ = spearmanr([m[1] for m in maduros], ds)
            ic = np.tanh(np.arctanh(rho) + np.array([-1, 1]) * 1.96
                         / np.sqrt(len(maduros) - 3))
            res["rho_b_delta"] = round(float(rho), 4)
            res["ic95_inf"] = round(float(ic[0]), 4)
            res["ic95_sup"] = round(float(ic[1]), 4)
    return res


def main():
    if len(sys.argv) < 2:
        print("Uso: evaluar_prospectiva.py <cierres.csv.gz> [fin_ventana]")
        print("  <cierres.csv.gz>: datos de la ventana (par, fecha, close)")
        return 1
    ruta_datos = Path(sys.argv[1])
    fin = sys.argv[2] if len(sys.argv) > 2 else FIN_DEFECTO
    res = evaluar(ruta_datos, fin)

    print(f"VENTANA {CORTE_COHORTE} → {fin}")
    print(f"Candidatos (vivos dd<99% al corte): {res['candidatos']}")
    print(f"P1a — colapsos crudos: {res['colapsos_crudos']} → "
          f"{'✓ RESPALDADA' if res['colapsos_crudos'] >= 1 else '✗ FALSADA'} "
          f"(peso bajo, ADENDA 2)")
    frac = res['fraccion_pct']
    print(f"FRACCIÓN — {frac:.1f}% (DESCRIPTIVA del régimen; sin "
          f"compuerta, ADENDA 4)")

    if res["mediana_delta"] is not None:
        med = res["mediana_delta"]
        n_mad = res["colapsos_maduros"]
        print(f"P2 — mediana Δ = {med:+.3f} (n maduros = {n_mad}) | "
              f"banda [{P2_LO}, {P2_HI}] → "
              f"{'✓ RESPALDADA' if P2_LO <= med <= P2_HI else '✗ FUERA'}")
        if res["rho_b_delta"] is not None:
            ic = (res["ic95_inf"], res["ic95_sup"])
            dentro = abs(ic[0]) < P3_UMBRAL and abs(ic[1]) < P3_UMBRAL
            estado = ('✓ DEMOSTRADA' if dentro
                      else 'INCONCLUSO a este n — esperado por diseño '
                           'con n≈36 (ADENDA 2)')
            print(f"P3 (TOST) — ρ(b,Δ) = {res['rho_b_delta']:+.3f}, IC95 "
                  f"[{ic[0]:+.3f}, {ic[1]:+.3f}] (n={n_mad}) → {estado}")
        else:
            print("P3 — n<5 maduros: no evaluable (criterio preregistrado)")
    else:
        print("Sin colapsos maduros medibles: P2/P3 no evaluables.")

    print("\nEl informe formal se escribe en audits/ con la fecha real "
          "de evaluación, favorable o desfavorable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
