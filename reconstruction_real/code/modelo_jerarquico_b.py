#!/usr/bin/env python3
"""MODELO JERÁRQUICO DE b — preregistro 2026-10-26 (pendiente 5.3).

Preregistro: reconstruction_real/preregistro/PREREGISTRO_MODELO_JERARQUICO_2026-10-26.md
(commit 4107679, antes de este script). Receta fijada ahí; sin libertades.

A: réplica caso-nivel del ancla fricción→b (codificación pre-especificada).
B: nulo por dominios — permutar tier→dominio (constante dentro de dominio),
   N=5000, semilla 20261026. p_perm una cola inferior.
C: MixedLM b ~ fric + (1|dominio).
D: réplica por dominios (n=10, descriptiva).
"""

import logging
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

warnings.simplefilter("ignore")

ROOT = Path(__file__).resolve().parent.parent.parent
RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR / "modelo_jerarquico_log.txt", mode="w"),
    ],
)
log = logging.getLogger("modelo_jerarquico")

SEMILLA = 20261026
N_PERM = 5000

# Codificación pre-especificada en el preregistro (mapeo tela)
FRICCION_DOMINIO = {
    "D": 1, "E1": 1, "E3": 1,          # nula
    "A": 2,                             # media
    "B": 3, "C": 3, "E2": 3,          # alta
    "F1": 4, "F2": 4, "F3": 4,        # fisica
}


def main():
    log.info("=" * 78)
    log.info("MODELO JERÁRQUICO DE b — preregistro 2026-10-26 "
             "(N_perm=%d, semilla %d)", N_PERM, SEMILLA)
    log.info("=" * 78)

    df = pd.read_csv(RR / "snt_corpus_REAL_v6.csv")
    df["fric"] = df["dominio"].map(FRICCION_DOMINIO)
    d = df.dropna(subset=["b", "fric"]).copy()
    log.info("Casos con b y fricción: %d de %d (excluidos %d sin b)",
             len(d), len(df), len(df) - len(d))
    dominios = sorted(d["dominio"].unique())
    tier_real = {dom: FRICCION_DOMINIO[dom] for dom in dominios}
    log.info("Dominios: %s", dominios)
    log.info("Tiers: %s", tier_real)

    # ── A: réplica caso-nivel ──
    rho_obs, p_obs = spearmanr(d["fric"], d["b"])
    log.info("")
    log.info("A — Réplica caso-nivel: Spearman(fric, b) = %+.4f "
             "(p=%.3e, n=%d)", rho_obs, p_obs, len(d))
    log.info("   (ancla del Axioma 5: ρ=−0.68, n=714 — la discrepancia "
             "se reporta, no se reconcilia)")

    # ── B: nulo por dominios ──
    rng = np.random.default_rng(SEMILLA)
    tiers = np.array([tier_real[dom] for dom in dominios])
    b_por_dom = {dom: d.loc[d["dominio"] == dom, "b"].to_numpy()
                 for dom in dominios}
    log.info("")
    log.info("B — Nulo por dominios: permutar tier→dominio (mantiene "
             "constancia intra-dominio), %d permutaciones", N_PERM)
    b_concat = np.concatenate([b_por_dom[dom] for dom in dominios])
    dom_idx = np.concatenate(
        [np.full(len(b_por_dom[dom]), i) for i, dom in enumerate(dominios)])
    rhos_perm = np.empty(N_PERM)
    for k in range(N_PERM):
        tiers_perm = rng.permutation(tiers)
        fric_perm = tiers_perm[dom_idx]
        rhos_perm[k] = spearmanr(fric_perm, b_concat)[0]
    p_perm = float((1 + np.sum(rhos_perm <= rho_obs)) / (N_PERM + 1))
    log.info("   nulo: mediana %+.4f [p5 %+.4f, p95 %+.4f]",
             np.median(rhos_perm), np.quantile(rhos_perm, 0.05),
             np.quantile(rhos_perm, 0.95))
    log.info("   p_perm = P(ρ* ≤ ρ_obs) = %.4f", p_perm)

    # ── C: MixedLM ──
    log.info("")
    log.info("C — Modelo mixto: b ~ fric + (1|dominio)")
    import statsmodels.formula.api as smf
    m = smf.mixedlm("b ~ fric", d, groups=d["dominio"]).fit()
    pend = float(m.fe_params.get("fric"))
    se = float(m.bse_fe.get("fric"))
    p_mlm = float(m.pvalues.get("fric"))
    var_dom = float(m.cov_re.iloc[0, 0]) if hasattr(m.cov_re, "iloc") else 0.0
    log.info("   pendiente fricción = %+.4f (SE %.4f, p=%.4g)",
             pend, se, p_mlm)
    log.info("   varianza del intercepto por dominio = %.4g", var_dom)

    # ── D: por dominio (réplica de la salvedad) ──
    medias = d.groupby("dominio")["b"].mean()
    tiers_d = np.array([tier_real[dom] for dom in dominios])
    bs_d = medias[dominios].to_numpy()
    rho_d, p_d = spearmanr(tiers_d, bs_d)
    log.info("")
    log.info("D — Por dominio (n=%d): Spearman = %+.4f (p=%.4f) "
             "[salvedad del Axioma 5: por dominio p=0.25]",
             len(dominios), rho_d, p_d)

    pd.DataFrame([{
        "n_casos": len(d),
        "rho_caso_nivel": round(float(rho_obs), 4),
        "p_caso_nivel": float(p_obs),
        "nulo_mediana": round(float(np.median(rhos_perm)), 4),
        "nulo_p5": round(float(np.quantile(rhos_perm, 0.05)), 4),
        "nulo_p95": round(float(np.quantile(rhos_perm, 0.95)), 4),
        "p_perm": round(p_perm, 4),
        "mlm_pendiente": round(pend, 4),
        "mlm_se": round(se, 4),
        "mlm_p": round(p_mlm, 6),
        "por_dominio_rho": round(float(rho_d), 4),
        "por_dominio_p": round(float(p_d), 4),
        "n_perm": N_PERM, "semilla": SEMILLA,
    }]).to_csv(RR / "modelo_jerarquico_resumen.csv", index=False)

    log.info("")
    if p_perm < 0.05 and p_mlm < 0.05:
        log.info("VEREDICTO 1: la asociación SOBREVIVE al control de "
                 "estructura (p_perm=%.4f, MLM p=%.4g) — se reporta con "
                 "SE honesto; entre-dominios por construcción.", p_perm,
                 p_mlm)
    elif p_perm >= 0.05:
        log.info("VEREDICTO 2: el ρ caso-nivel NO se distingue de una "
                 "asignación arbitraria de tiers entre dominios "
                 "(p_perm=%.4f) — mismo veredicto que el tono φ: el ancla "
                 "queda como descriptivo del agrupamiento, no como "
                 "medición de fricción. Pendiente MixedLM reportada con "
                 "su SE.", p_perm)
    else:
        log.info("VEREDICTO MIXTO: p_perm=%.4f, MLM p=%.4g — reportado "
                 "sin re-interpretar.", p_perm, p_mlm)
    log.info("EJECUCION COMPLETADA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
