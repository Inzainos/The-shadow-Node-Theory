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


def main():
    if len(sys.argv) < 2:
        print("Uso: evaluar_prospectiva.py <cierres.csv.gz> [fin_ventana]")
        print("  <cierres.csv.gz>: datos de la ventana (par, fecha, close)")
        return 1
    ruta_datos = Path(sys.argv[1])
    fin = sys.argv[2] if len(sys.argv) > 2 else FIN_DEFECTO

    cohorte = list(csv.DictReader(COHORTE.open()))
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
        nacimiento_idx = None
        for i, (f, _) in enumerate(puntos):
            if f >= c["fecha_nacimiento"]:
                nacimiento_idx = i
                break
        if nacimiento_idx is None:
            continue
        # solo candidatos vivos al corte (dd < 99% contra ATH congelado)
        hasta = [p for p in puntos if p[0] <= CORTE_COHORTE]
        if not hasta:
            continue
        precio_corte = hasta[-1][1]
        if 100 * (1 - precio_corte / c["ath_corte"]) >= 99:
            continue
        candidatos += 1
        despues = [p for p in puntos if CORTE_COHORTE < p[0] <= fin]
        if not despues:
            continue
        fin_precio = despues[-1][1]
        min_ventana = min(p[1] for p in despues)
        if not (min_ventana < 0.01 * c["ath_corte"]
                and fin_precio < 0.01 * c["ath_corte"]):
            continue
        colapsos_crudos += 1
        # receta ADENDA 1: madurez >= 120 por lado sobre toda la serie
        precios_todo = np.array([p[1] for p in puntos])
        pk = int(np.argmax(precios_todo))
        if pk < 120 or len(precios_todo) - pk < 120:
            continue
        b = fit_loglog(np.arange(1, pk + 2, dtype=float),
                       precios_todo[:pk + 1])
        fin_valle = pk + max(int(np.argmin(precios_todo[pk:])), 1)
        d = fit_loglog(np.arange(1, fin_valle - pk + 1, dtype=float),
                       precios_todo[pk:fin_valle + 1])
        if b is None or d is None:
            continue
        maduros.append((par, b, d))

    frac = 100 * colapsos_crudos / candidatos if candidatos else float("nan")
    print(f"VENTANA {CORTE_COHORTE} → {fin}")
    print(f"Candidatos (vivos dd<99% al corte): {candidatos}")
    print(f"P1a — colapsos crudos: {colapsos_crudos} → "
          f"{'✓ RESPALDADA' if colapsos_crudos >= 1 else '✗ FALSADA'} "
          f"(peso bajo, ADENDA 2)")
    print(f"FRACCIÓN — {frac:.1f}% (DESCRIPTIVA del régimen; sin "
          f"compuerta, ADENDA 4)")

    if maduros:
        ds = [m[2] for m in maduros]
        med = float(np.median(ds))
        print(f"P2 — mediana Δ = {med:+.3f} (n maduros = {len(maduros)}) | "
              f"banda [{P2_LO}, {P2_HI}] → "
              f"{'✓ RESPALDADA' if P2_LO <= med <= P2_HI else '✗ FUERA'}")
        if len(maduros) >= 5:
            rho, p = spearmanr([m[1] for m in maduros], ds)
            ic = np.tanh(np.arctanh(rho) + np.array([-1, 1]) * 1.96
                         / np.sqrt(len(maduros) - 3))
            dentro = abs(ic[0]) < P3_UMBRAL and abs(ic[1]) < P3_UMBRAL
            print(f"P3 (TOST) — ρ(b,Δ) = {rho:+.3f}, IC95 "
                  f"[{ic[0]:+.3f}, {ic[1]:+.3f}] (n={len(maduros)}) → "
                  f"{'✓ DEMOSTRADA' if dentro else 'INCONCLUSO a este n'}")
        else:
            print("P3 — n<5 maduros: no evaluable (criterio preregistrado)")
    else:
        print("Sin colapsos maduros medibles: P2/P3 no evaluables.")

    print("\nEl informe formal se escribe en audits/ con la fecha real "
          "de evaluación, favorable o desfavorable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
