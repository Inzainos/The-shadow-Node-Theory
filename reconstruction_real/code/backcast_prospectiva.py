#!/usr/bin/env python3
"""BACKCAST de la prospectiva ACO-A — versión ejecutable del informe.

Reproduce los números de `audits/BACKCAST_PROSPECTIVA_2026-10-26.md`
(auditado por el operador en `observaciones.md`, punto 1: el backcast
corrió inline y no dejó script; este archivo lo corrige).

Receta: la ADENDA (`ADENDA_PROSPECTIVA_RECETA_2026-10-26.md`) — la
histórica exacta de `orthogonality_test.py`:
  - madurez >= 120 días de serie antes del ATH y >= 120 después
  - b: nacimiento → ATH (días desde nacimiento, fit log-log >= 20 pts)
  - Δ: ATH → siguiente valle (argmin post-ATH)

Congelamiento SIN LOOKAHEAD al CORTE (default 2025-08-31), ventana de
evaluación CORTE → FIN (default 2026-08-31), sobre el archivo versionado
`data/binance_cierres_diarios.csv.gz`.

Uso:
    python reconstruction_real/code/backcast_prospectiva.py            # defaults
    python reconstruction_real/code/backcast_prospectiva.py 2024-08-31 2025-08-31
"""

import csv
import gzip
import sys
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = __import__("pathlib").Path(__file__).resolve().parent.parent.parent
FUENTE = ROOT / "data" / "binance_cierres_diarios.csv.gz"

# Banda P2 pre-registrada (preregistro df888d0)
P2_LO, P2_HI = -3.270, -0.115
P3_UMBRAL = 0.3


def cargar_series():
    series = defaultdict(list)
    with gzip.open(FUENTE, "rt") as f:
        for row in csv.DictReader(f):
            series[row["par"]].append((row["fecha"], float(row["close"])))
    for par in series:
        series[par].sort()
    return series


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


def backcast(series, corte, fin):
    fecha_max = max((p[0] for puntos in series.values() for p in puntos),
                    default="")
    if fecha_max < fin:
        raise ValueError(
            f"descarga incompleta: última fecha {fecha_max or 'ausente'} "
            f"< fin de ventana {fin}")
    congelados = []
    for par, puntos in series.items():
        hasta = [p for p in puntos if p[0] <= corte]
        if not hasta or hasta[-1][0] != corte:
            continue
        precios = np.array([p[1] for p in hasta])
        pk = int(np.argmax(precios))
        ath = float(precios[pk])
        if 100 * (1 - float(precios[-1]) / ath) >= 99:
            continue
        congelados.append({"par": par, "ath": ath, "pk": pk,
                           "n_serie": len(puntos)})

    colapsos_crudos = 0
    censurados = 0
    colapsos = []
    for c in congelados:
        puntos = series[c["par"]]
        despues = [p for p in puntos if corte < p[0] <= fin]
        if not despues or despues[-1][0] != fin:
            censurados += 1
            continue
        fin_precio = despues[-1][1]
        min_ventana = min(p[1] for p in despues)
        if not (min_ventana < 0.01 * c["ath"] and fin_precio < 0.01 * c["ath"]):
            continue
        colapsos_crudos += 1
        # receta de la adenda: madurez >= 120 por lado — con la serie
        # TRUNCADA EN FIN (revisión del operador: n_serie completa
        # incluía datos posteriores a la ventana y relajaba el criterio)
        precios_vent = np.array([p[1] for p in puntos if p[0] <= fin])
        if c["pk"] < 120 or len(precios_vent) - c["pk"] < 120:
            continue
        precios = np.array([p[1] for p in puntos if p[0] <= corte])
        b = fit_loglog(np.arange(1, c["pk"] + 2, dtype=float),
                       precios[:c["pk"] + 1])
        # FIX (validación del operador, 2026-10-26): el ATH y el valle
        # de Δ se buscan DENTRO de la ventana (precios_vent, ya truncado
        # en fin — con la serie completa el valle se filtra en datos
        # posteriores al fin y el resultado depende de cuándo se
        # descargó el archivo).
        pk_todo = int(np.argmax(precios_vent))
        fin_valle = pk_todo + max(int(np.argmin(precios_vent[pk_todo:])), 1)
        d = fit_loglog(np.arange(1, fin_valle - pk_todo + 1, dtype=float),
                       precios_vent[pk_todo:fin_valle + 1])
        if b is None or d is None:
            continue
        colapsos.append((c["par"], b, d))
    return congelados, colapsos_crudos, colapsos, censurados


def main():
    corte = sys.argv[1] if len(sys.argv) > 1 else "2025-08-31"
    fin = sys.argv[2] if len(sys.argv) > 2 else "2026-08-31"
    print(f"BACKCAST {corte} → {fin} (receta de la ADENDA, congelamiento "
          f"sin lookahead)")
    series = cargar_series()
    congelados, crudos, colapsos, censurados = backcast(series, corte, fin)
    print(f"Cohorte congelada (vivos, dd<99%): {len(congelados)} pares")
    print(f"Censurados (sin cierre hasta el fin; no cuentan como colapso): "
          f"{censurados}")
    print(f"P1a — colapsos observados: {crudos} (con madurez y medibles: "
          f"{len(colapsos)}) → {'✓' if crudos >= 1 else '✗'}")
    resumen = {"corte": corte, "fin": fin, "candidatos": len(congelados),
               "censurados": censurados,
               "colapsos_crudos": crudos, "colapsos_maduros": len(colapsos)}
    if colapsos:
        ds = [c[2] for c in colapsos]
        resumen["mediana_delta"] = round(float(np.median(ds)), 4)
        if len(colapsos) >= 5:
            rho, p = spearmanr([c[1] for c in colapsos], ds)
            ic = np.tanh(np.arctanh(rho) + np.array([-1, 1]) * 1.96
                         / np.sqrt(len(colapsos) - 3))
            resumen["rho_b_delta"] = round(float(rho), 4)
            resumen["ic95_inf"] = round(float(ic[0]), 4)
            resumen["ic95_sup"] = round(float(ic[1]), 4)
    out = ROOT / "reconstruction_real" / "data" \
        / "backcast_prospectiva_resumen.csv"
    pd.DataFrame([resumen]).to_csv(out, index=False)
    print(f"Resumen → {out}")
    if colapsos:
        ds = [c[2] for c in colapsos]
        med = float(np.median(ds))
        print(f"P2 — mediana Δ = {med:+.3f} | banda [{P2_LO}, {P2_HI}] → "
              f"{'✓' if P2_LO <= med <= P2_HI else '✗'} (n medibles="
              f"{len(colapsos)})")
        if len(colapsos) >= 5:
            rho, p = spearmanr([c[1] for c in colapsos], ds)
            ic = np.tanh(np.arctanh(rho) + np.array([-1, 1]) * 1.96
                         / np.sqrt(len(colapsos) - 3))
            equivalencia = ic[0] > -P3_UMBRAL and ic[1] < P3_UMBRAL
            veredicto = ("equivalencia demostrada" if equivalencia else
                         "INCONCLUSO: el IC rebasa ±0.3")
            print(f"P3 — ρ(b,Δ) = {rho:+.3f} (p={p:.3f}, n={len(colapsos)}) "
                  f"IC95 [{ic[0]:+.3f}, {ic[1]:+.3f}] → {veredicto}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
