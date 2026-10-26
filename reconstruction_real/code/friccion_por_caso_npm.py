#!/usr/bin/env python3
"""FRICCIÓN POR CASO vs b — preregistro 2026-10-26 (pendiente 5.5).

Preregistro: reconstruction_real/preregistro/PREREGISTRO_FRICCION_POR_CASO_NPM_2026-10-26.md
(commit df888d0, antes de este script). Receta fijada ahí; sin libertades.

La única fricción POR CASO del corpus (npm 0..3 a priori) dentro de UN
dominio. Test principal: Spearman(friccion_a_priori, b_subida), n=450.
Predicción direccional pre-registrada: ρ < 0. Determinista (sin RNG).
"""

import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR / "friccion_por_caso_log.txt", mode="w"),
    ],
)
log = logging.getLogger("friccion_por_caso")


def main():
    log.info("=" * 78)
    log.info("FRICCIÓN POR CASO vs b (npm) — preregistro 2026-10-26")
    log.info("=" * 78)

    df = pd.read_csv(RR / "npm_cohorte_aco.csv.gz")
    df["friccion_a_priori"] = df["friccion_a_priori"].astype(int)
    df["b_subida"] = df["b_subida"].astype(float)
    n = len(df)
    log.info("Cohorte npm: %d paquetes (fricción 0..3 a priori)", n)

    # ── Test principal ──
    rho, p2 = stats.spearmanr(df["friccion_a_priori"], df["b_subida"])
    p1 = p2 / 2 if rho < 0 else 1 - p2 / 2
    log.info("")
    log.info("Spearman(friccion_a_priori, b_subida) = %+.4f | "
             "p 2 colas = %.4g | p 1 cola (dirección ρ<0) = %.4g | n = %d",
             rho, p2, p1, n)

    # ── Por nivel ──
    log.info("")
    log.info("Mediana de b_subida por nivel de fricción:")
    grupos = {}
    for k in sorted(df["friccion_a_priori"].unique()):
        g = df.loc[df["friccion_a_priori"] == k, "b_subida"].to_numpy()
        grupos[k] = g
        log.info("  fricción %d (n=%3d): mediana %+.4f [p25 %+.4f, p75 %+.4f]",
                 k, len(g), np.median(g), np.percentile(g, 25),
                 np.percentile(g, 75))
    muestras = [grupos[k] for k in sorted(grupos) if len(grupos[k]) >= 30]
    if len(muestras) >= 3:
        H, pk = stats.kruskal(*muestras)
        log.info("Kruskal-Wallis entre niveles con n>=30: H = %.3f, p = %.4g",
                 H, pk)

    # ── Control por disparador ──
    log.info("")
    log.info("Control por clase de disparador:")
    for clase in ("abrupto", "anunciado", "sin_clasificar"):
        sub = df[df["disparador"] == clase]
        if len(sub) < 30:
            log.info("  %s: n=%d — insuficiente (<30)", clase, len(sub))
            continue
        r_c, p_c = stats.spearmanr(sub["friccion_a_priori"],
                                   sub["b_subida"])
        log.info("  %s (n=%3d): ρ = %+.4f (p 2 colas %.4g)",
                 clase, len(sub), r_c, p_c)

    resumen = pd.DataFrame([{
        "n": n,
        "rho": round(float(rho), 4),
        "p_2colas": float(p2),
        "p_1cola_direccion": round(float(p1), 4),
        "kw_H": round(float(H), 3) if len(muestras) >= 3 else None,
        "kw_p": float(pk) if len(muestras) >= 3 else None,
    }])
    resumen.to_csv(RR / "friccion_por_caso_resumen.csv", index=False)

    log.info("")
    if rho < 0 and p1 < 0.05:
        log.info("VEREDICTO 1: dirección del Axioma 5 RESPALDADA por caso "
                 "dentro de npm (ρ=%+.3f, p 1 cola %.4g) — primera "
                 "evidencia estructuralmente limpia de fricción → b.",
                 rho, p1)
    else:
        log.info("VEREDICTO 2: NO respaldada por esta vía (ρ=%+.3f, "
                 "p 1 cola %.4g) — se reporta la cifra, no se interpreta.",
                 rho, p1)
    log.info("EJECUCION COMPLETADA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
