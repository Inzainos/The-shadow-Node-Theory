#!/usr/bin/env python3
"""SENSIBILIDAD de los nulos AR(1) de ACO a la estimación de φ.

Responde `observaciones.md` punto 5: 16/18 series ACO tienen n < 8 puntos;
φ estimado con tan pocos datos es ruidoso y el p = 0.013 merece un análisis
de sensibilidad. Aquí se re-corre el nulo N1 perturbando φ por caso en
±0.05 y ±0.15 (clamped [0, 0.995]), con todo lo demás igual al preregistro
`a253b15` (M=2000, semilla 20261026).

Salida: rango de p_N1 a través de las perturbaciones.
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nulos_ar1_aco import (PHI_TOPE, M_REPLICAS, SEMILLA,  # noqa: E402
                           ajustar_ar1, cargar_aco, simular_caso)

RR = Path(__file__).resolve().parent.parent / "data"


def p_n1_con_perturbacion(delta_phi):
    rng = np.random.default_rng(SEMILLA)
    aco = cargar_aco()
    finales = {}
    for cid, x in sorted(aco.items()):
        mu, phi, sigma, n = ajustar_ar1(x)
        phi_p = min(max(phi + delta_phi, 0.0), PHI_TOPE)
        finales[cid] = simular_caso(mu, phi_p, sigma, x[0], n, M_REPLICAS,
                                    rng)
    s_obs = float(np.median([abs(x[-1]) for x in aco.values()]))
    mat = np.stack([finales[c] for c in sorted(finales)])
    s_nulo = np.median(mat, axis=0)
    return float((1 + np.sum(s_nulo <= s_obs)) / (M_REPLICAS + 1))


def main():
    print("SENSIBILIDAD p_N1 a φ (todo lo demás igual al preregistro):")
    filas = []
    for dphi in (-0.15, -0.05, 0.0, 0.05, 0.15):
        p = p_n1_con_perturbacion(dphi)
        print(f"  φ{dphi:+.2f}: p_N1 = {p:.4f} "
              f"{'(robusto, <0.05)' if p < 0.05 else '(FRÁGIL, ≥0.05)'}")
        filas.append({"delta_phi": dphi, "p_N1": round(p, 4)})
    df = pd.DataFrame(filas)
    df.to_csv(RR / "sensibilidad_nulos_ar1.csv", index=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
