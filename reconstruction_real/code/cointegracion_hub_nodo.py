#!/usr/bin/env python3
"""COINTEGRACIÓN HUB–NODO — preregistro 2026-10-26 (pendiente 5.2).

Preregistro: reconstruction_real/preregistro/PREREGISTRO_COINTEGRACION_2026-10-26.md
(commit e76545b, ANTES de este script). Receta fijada ahí; sin libertades.

B (era estable): ADF por componente (log PIBpc hub, log PIBpc nodo) +
Engle-Granger (statsmodels.coint, MacKinnon) + ADF sobre log R.
E3/ACO: componentes no versionados — solo ADF sobre log R (descriptivo).

Determinista: ADF/EG no usan RNG.
"""

import logging
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller, coint

warnings.simplefilter("ignore")  # ConvergenceWarning/LinAlgError de casos cortos

ROOT = Path(__file__).resolve().parent.parent.parent
RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR / "cointegracion_log.txt", mode="w"),
    ],
)
log = logging.getLogger("cointegracion")

UMBRAL = 0.05      # preregistro


def _adf_ok(x):
    """(p_valor, estimable). Casos cortos/constantes → (nan, False)."""
    x = np.asarray(x, dtype=float)
    if len(x) < 8 or not np.isfinite(x).all() or np.std(x) == 0:
        return np.nan, False
    try:
        return float(adfuller(x, regression="c", autolag="AIC")[1]), True
    except Exception:
        return np.nan, False


def casos_b():
    """Pares B era-estable con componentes: (id, log hub, log nodo, log R)."""
    mad = pd.read_csv(ROOT / "data" / "maddison_mpd2020.csv")
    B = pd.read_csv(RR / "by_domain" / "dominio_B_real.csv")
    for _, r in B.iterrows():
        h = mad[(mad["Entity"] == r["hub"]) &
                (mad["Year"] >= r["year_min"]) &
                (mad["Year"] <= r["year_max"])][["Year", "GDP per capita"]] \
            .dropna()
        n_ = mad[(mad["Entity"] == r["nodo"]) &
                 (mad["Year"] >= r["year_min"]) &
                 (mad["Year"] <= r["year_max"])][["Year", "GDP per capita"]] \
            .dropna()
        m = pd.merge(h, n_, on="Year", suffixes=("_hub", "_nodo")) \
            .sort_values("Year")
        if len(m) < 8:
            continue
        hub = np.log(m["GDP per capita_hub"].to_numpy(dtype=float))
        nodo = np.log(m["GDP per capita_nodo"].to_numpy(dtype=float))
        ratio = hub - nodo
        yield r["id"], hub, nodo, ratio


def main():
    log.info("=" * 78)
    log.info("COINTEGRACIÓN HUB–NODO — preregistro 2026-10-26 (umbral %.2f)",
             UMBRAL)
    log.info("=" * 78)

    # ── B: ADF componentes + Engle-Granger + ADF del ratio ──
    filas = []
    for cid, hub, nodo, ratio in casos_b():
        p_h, ok_h = _adf_ok(hub)
        p_n, ok_n = _adf_ok(nodo)
        p_r, ok_r = _adf_ok(ratio)
        p_coint = np.nan
        if ok_h and ok_n:
            try:
                p_coint = float(coint(hub, nodo, trend="c",
                                      autolag="AIC")[1])
            except Exception:
                p_coint = np.nan
        amb_i1 = bool(ok_h and ok_n and p_h > UMBRAL and p_n > UMBRAL)
        filas.append({
            "id": cid, "n": len(hub),
            "p_adf_hub": round(p_h, 4) if ok_h else None,
            "p_adf_nodo": round(p_n, 4) if ok_n else None,
            "p_coint": round(p_coint, 4) if np.isfinite(p_coint) else None,
            "p_adf_ratio": round(p_r, 4) if ok_r else None,
            "ambos_I1": amb_i1,
            "cointegrado": bool(np.isfinite(p_coint)
                                and p_coint < UMBRAL) if amb_i1 else None,
        })
    df = pd.DataFrame(filas)
    df.to_csv(RR / "cointegracion_b_por_caso.csv", index=False)

    i1 = df[df["ambos_I1"]]
    n_i1 = len(i1)
    n_coint = int(i1["cointegrado"].sum()) if n_i1 else 0
    pct_coint = 100 * n_coint / n_i1 if n_i1 else float("nan")
    estac = int((df["p_adf_ratio"] < UMBRAL).sum())
    log.info("B: %d casos | ambos I(1): %d (%.0f%%) | cointegrados de los "
             "I(1): %d/%d (%.1f%%) | ratio estacionario: %d/%d (%.0f%%)",
             len(df), n_i1, 100 * n_i1 / len(df), n_coint, n_i1, pct_coint,
             estac, len(df), 100 * estac / len(df))

    # ── E3/ACO: ADF sobre log R (componentes no versionados) ──
    filas_ra = []
    aco = pd.read_csv(RR / "snt_corpus_aco_timeseries_v29.csv")
    aco = aco[(aco["t"] > 0) & (aco["R"] > 0)]
    for cid, g in aco.groupby("id"):
        p_r, ok = _adf_ok(np.log10(g["R"].to_numpy(dtype=float)))
        filas_ra.append({"dominio": "ACO", "id": cid, "n": len(g),
                         "p_adf_logR": round(p_r, 4) if ok else None})
    tela = pd.read_csv(RR / "tela_de_incertidumbre.csv")
    e3 = tela[tela["dominio"] == "E3"].sort_values(["id", "t"])
    for cid, g in e3.groupby("id"):
        p_r, ok = _adf_ok(np.log10(g["m"].to_numpy(dtype=float)))
        filas_ra.append({"dominio": "E3", "id": cid, "n": len(g),
                         "p_adf_logR": round(p_r, 4) if ok else None})
    dfra = pd.DataFrame(filas_ra)
    dfra.to_csv(RR / "cointegracion_ratio_adf.csv", index=False)
    for dom in ("E3", "ACO"):
        sub = dfra[dfra["dominio"] == dom]
        est = int((sub["p_adf_logR"] < UMBRAL).sum())
        ok = int(sub["p_adf_logR"].notna().sum())
        log.info("%s (descriptivo, sin componentes): ratio estacionario %d/%d"
                 " estimables", dom, est, ok)

    resumen = pd.DataFrame([{
        "B_casos": len(df),
        "B_ambos_I1": n_i1,
        "B_I1_cointegrados": n_coint,
        "pct_cointegrados_I1": round(pct_coint, 1) if n_i1 else None,
        "B_ratio_estacionario": estac,
        "E3_ratio_estacionario": int((dfra.query("dominio=='E3'")
                                      ["p_adf_logR"] < UMBRAL).sum()),
        "ACO_ratio_estacionario": int((dfra.query("dominio=='ACO'")
                                       ["p_adf_logR"] < UMBRAL).sum()),
        "umbral": UMBRAL,
    }])
    resumen.to_csv(RR / "cointegracion_resumen.csv", index=False)

    log.info("")
    if n_i1 == 0:
        log.info("SIN CASOS ambos-I(1): los componentes de B no son "
                 "mayoritariamente I(1); la preocupación de spuria no "
                 "aplica por esta vía. Veredicto descriptivo.")
    elif pct_coint >= 50:
        log.info("VEREDICTO 1 (pre-especificado): ≥50%% de los pares B "
                 "I(1) están cointegrados — los ajustes de R(t) sobre ellos "
                 "no son espurios como relaciones; b queda descriptivo del "
                 "ratio hacia su equilibrio.")
    else:
        log.info("VEREDICTO 2 (pre-especificado): <50%% de los pares B I(1) "
                 "están cointegrados (%.1f%%) — el ajuste de potencia sobre "
                 "R(t) es en general espurio como estimación de equilibrio; "
                 "b es descriptivo de la deriva del ratio. Consistente con "
                 "el hallazgo de convergencia del test de comercio.",
                 pct_coint)
    log.info("EJECUCION COMPLETADA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
