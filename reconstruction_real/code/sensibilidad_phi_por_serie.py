#!/usr/bin/env python3
"""SENSIBILIDAD POR SERIE: bootstrap del φ de CADA caso ACO.

Versión versionada del análisis que corrió inline (2026-10-26): la
sensibilidad común (sensibilidad_nulos_ar1.py) perturba todos los φ
con el mismo delta; esta versión perturba el φ de CADA serie con su
PROPIO error de estimación (bootstrap paramétrico del ajuste AR(1)).

Responde a: "La sensibilidad a φ con un solo φ común, en lugar de un
bootstrap por serie" (PENDIENTES_SNT.md).

Salida: data/sensibilidad_phi_por_serie.csv
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nulos_ar1_aco import PHI_TOPE, SEMILLA, ajustar_ar1, cargar_aco, simular_caso

RR = Path(__file__).resolve().parent.parent / "data"
M_BOOT = 2000


def se_phi(x):
    """SE del coeficiente AR(1) por mínimos cuadrados."""
    mu, phi, sigma, n = ajustar_ar1(x)
    xc = x - mu
    if n < 3:
        return 0.15
    X = xc[:-1].reshape(-1, 1)
    y = xc[1:]
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = max(len(y) - 1, 1)
    s2 = float(resid.T @ resid) / dof
    try:
        cov = s2 * np.linalg.inv(X.T @ X)
        return float(np.sqrt(cov[0, 0]))
    except Exception:
        return 0.15


def main():
    rng = np.random.default_rng(SEMILLA)
    aco = cargar_aco()
    casos = []
    for cid, x in sorted(aco.items()):
        mu, phi, sigma, n = ajustar_ar1(x)
        casos.append({"cid": cid, "x": x, "mu": mu, "phi": phi,
                      "sigma": sigma, "n": n, "se_phi": se_phi(x)})

    s_obs = float(np.median([abs(x[-1]) for x in aco.values()]))
    p_vals = []
    for _ in range(M_BOOT):
        fines = {}
        for c in casos:
            phi_p = min(max(c["phi"] + rng.normal(0, c["se_phi"]),
                            0.0), PHI_TOPE)
            fines[c["cid"]] = simular_caso(c["mu"], phi_p, c["sigma"],
                                            c["x"][0], c["n"], 1, rng)[0]
        mat = np.array([fines[c["cid"]] for c in casos])
        s_nulo = float(np.median(mat))
        p_vals.append(1.0 if s_nulo <= s_obs else 0.0)

    p_boot = float((1 + np.sum(p_vals)) / (M_BOOT + 1))
    ses = [c["se_phi"] for c in casos]
    print(f"Bootstrap por serie (M={M_BOOT}): p_N1 = {p_boot:.4f}")
    print(f"SE de φ por caso: mediana {np.median(ses):.3f} "
          f"[p25 {np.percentile(ses, 25):.3f}, p75 {np.percentile(ses, 75):.3f}]")

    pd.DataFrame([{
        "p_N1_bootstrap_por_serie": round(p_boot, 4),
        "M": M_BOOT, "semilla": SEMILLA,
        "se_phi_mediana": round(float(np.median(ses)), 3),
        "se_phi_p25": round(float(np.percentile(ses, 25)), 3),
        "se_phi_p75": round(float(np.percentile(ses, 75)), 3),
    }]).to_csv(RR / "sensibilidad_phi_por_serie.csv", index=False)
    print(f"→ {RR / 'sensibilidad_phi_por_serie.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
