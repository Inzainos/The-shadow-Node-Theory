#!/usr/bin/env python3
"""CALIBRACIÓN DE POTENCIA del test de cointegración en B (5.2).

Responde `observaciones.md` punto 6: "93% I(1)" y "12.3% cointegrado" son
FALLAS EN RECHAZAR con poca potencia en series anuales cortas. Aquí se
simula bajo COINTEGRACIÓN CONOCIDA con las longitudes de B (n = 34, 69,
119) y se mide qué porcentaje de las veces Engle-Granger la detecta
(potencia). También el tamaño bajo NO-cointegración (debe ser ~5%).

Si la potencia es baja, "solo 12.3% cointegrado" NO implica que el 87.7%
no esté cointegrado — solo que el test no lo puede ver a ese n.
"""

import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import coint

warnings.simplefilter("ignore")

SEMILLA = 20261026
M = 3000         # simulaciones por configuración (M=500 daba SE~1.3pp; subido a 3000 tras observación del operador 2026-10-26)
NIVELES = [34, 69, 119]   # n mínimo, mediano y máximo de B

# Persistencia del término de error comparable a B (rho AR(1) del
# residual de la relación): escenarios 0.5 y 0.8
RHO_ERR = [0.5, 0.8]


def simular_cointegrado(n, rho, rng):
    """x random walk; y = x + e, e AR(1) con rho — cointegración(1,1)."""
    e = np.zeros(n)
    innov = rng.standard_normal(n) * 0.02
    for t in range(1, n):
        e[t] = rho * e[t - 1] + innov[t]
    x = np.cumsum(rng.standard_normal(n) * 0.02) + np.log(8000)
    y = x + e
    return x, y


def simular_no_cointegrado(n, rng):
    """Dos random walks independientes."""
    x = np.cumsum(rng.standard_normal(n) * 0.02) + np.log(8000)
    y = np.cumsum(rng.standard_normal(n) * 0.02) + np.log(5000)
    return x, y


def main():
    rng = np.random.default_rng(SEMILLA)
    filas = []
    print("CALIBRACIÓN DE POTENCIA — Engle-Granger en B (nivel 0.05)")
    print(f"Simulaciones: {M} por configuración · semilla {SEMILLA}")
    for n in NIVELES:
        for rho in RHO_ERR:
            aciertos = 0
            for _ in range(M):
                x, y = simular_cointegrado(n, rho, rng)
                try:
                    p = coint(y, x, trend="c", autolag="AIC")[1]
                    aciertos += int(p < 0.05)
                except Exception:
                    pass
            pot = 100 * aciertos / M
            print(f"  n={n:3d} rho_err={rho:.1f}: POTENCIA = {pot:5.1f}%")
            filas.append({"n": n, "rho_err": rho, "potencia_pct": round(pot, 1)})
    # Tamaño por n y por trend (diagnóstico del sobre-rechazo, observación
    # del operador: ¿por qué EG sobre-rechaza? mide si es trend='c' a n corto)
    for n in NIVELES:
        for trend in ("c", "n"):
            falsos = 0
            for _ in range(M):
                x, y = simular_no_cointegrado(n, rng)
                try:
                    p = coint(y, x, trend=trend, autolag="AIC")[1]
                    falsos += int(p < 0.05)
                except Exception:
                    pass
            tam = 100 * falsos / M
            print(f"  n={n:3d} NO cointegrado trend={trend!r} "
                  f"(tamaño, nominal 5%): {tam:.1f}%")
            filas.append({"n": n, "rho_err": None, "trend": trend,
                          "tamaño_pct": round(tam, 1)})

    pd.DataFrame(filas).to_csv(
        Path(__file__).resolve().parent.parent / "data"
        / "potencia_cointegracion.csv", index=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
