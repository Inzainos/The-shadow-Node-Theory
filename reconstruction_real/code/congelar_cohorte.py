#!/usr/bin/env python3
"""CONGELAR COHORTE PROSPECTIVA — el proceso de congelación, versionado.

Genera `cohorte_congelada_cripto_2026-10-26_v2.csv` (o el nombre que se
indique) desde `data/binance_cierres_diarios.csv.gz` al corte indicado,
SIN lookahead: solo datos con fecha <= CORTE definen el estado congelado.
Con este script el congelamiento de la ADENDA 3 es auditable y
reproducible (observación del operador: la cohorte v2 salió de un
proceso inline no versionado).

Regla (preregistro prospectivo + ADENDA 3):
  - vivos al corte: última observación == CORTE
  - ATH congelado: máximo de cierre hasta el CORTE (sin lookahead)
  - candidatos: dd < 99% contra el ATH congelado

Uso:
    python reconstruction_real/code/congelar_cohorte.py
    python reconstruction_real/code/congelar_cohorte.py 2026-09-30 \
        reconstruction_real/data/cohorte_congelada_cripto_2026-10-26_v2.csv
"""

import csv
import gzip
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
FUENTE = ROOT / "data" / "binance_cierres_diarios.csv.gz"
SALIDA_DEF = (ROOT / "reconstruction_real" / "data"
              / "cohorte_congelada_cripto_2026-10-26_v2.csv")
CORTE_DEF = "2026-09-30"


def congelar(ruta_fuente, corte, ruta_salida):
    series = defaultdict(list)
    with gzip.open(ruta_fuente, "rt") as f:
        for row in csv.DictReader(f):
            series[row["par"]].append((row["fecha"],
                                       float(row["close"])))

    # "vivo al corte" = tiene una observación EN la fecha del corte
    # (para pares de trading diario es equivalente a que la última
    # observación sea el corte, pero funciona también con archivos que
    # extienden más allá del corte — validación del operador 2026-10-26:
    # la regla anterior solo servía con el archivo truncado exacto).
    congelados = []
    for par, puntos in series.items():
        puntos.sort()
        if not puntos or puntos[-1][0] < corte:
            continue          # murió antes del corte
        hasta = [p for p in puntos if p[0] <= corte]
        if not hasta or hasta[-1][0] != corte:
            continue          # sin cotización en la fecha del corte
        ath_fecha, ath_val = max(hasta, key=lambda p: p[1])
        precio_corte = hasta[-1][1]
        congelados.append({
            "par": par, "n_obs": len(puntos),
            "fecha_nacimiento": puntos[0][0],
            "ath_corte": ath_val, "fecha_ath": ath_fecha,
            "precio_corte": precio_corte,
            "dd_pct_vs_ath": round(100 * (1 - precio_corte / ath_val), 2),
        })

    congelados.sort(key=lambda r: -r["ath_corte"])
    with open(ruta_salida, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=congelados[0].keys())
        w.writeheader()
        w.writerows(congelados)

    candidatos = sum(1 for c in congelados if c["dd_pct_vs_ath"] < 99)
    print(f"CONGELADOS al corte {corte}: {len(congelados)} pares | "
          f"{candidatos} candidatos (dd < 99%) | → {ruta_salida}")
    return len(congelados), candidatos


def main():
    corte = sys.argv[1] if len(sys.argv) > 1 else CORTE_DEF
    salida = (Path(sys.argv[2]) if len(sys.argv) > 2 else SALIDA_DEF)
    congelar(FUENTE, corte, salida)
    return 0


if __name__ == "__main__":
    sys.exit(main())
