#!/usr/bin/env python3
"""NULOS AR(1) PARA LA CONVERGENCIA ACO-A — preregistro 2026-10-26.

Preregistro: reconstruction_real/preregistro/PREREGISTRO_NULOS_AR1_ACO_2026-10-26.md
(commit a253b15, ANTES de este script). Receta fijada ahí; este archivo la
ejecuta sin libertades.

N1: AR(1) ajustado por caso (μ = media de log10 R; φ = lag-1 de (x−μ),
clamped [0, 0.995]; σ_ε = std ddof=1 de los residuos AR(1)), x*_0 anclado
al observado, M=2000 réplicas/caso, semilla global 20261026.
Estadístico: S = mediana de |log10 R_T| sobre los 18 casos.
p_N1 = P(S* ≤ S_obs) (una cola inferior).

Contraste B (descriptivo, sin test entre dominios): mismo estadístico en
las series B del paquete de la tela (no terminan en evento; terminan en
2018 por decisión de ventana).

Salidas:
    reconstruction_real/data/nulos_ar1_aco.csv   (por caso)
    reconstruction_real/data/nulos_ar1_resumen.csv
    reconstruction_real/logs/nulos_ar1_log.txt
"""

import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))
from snt import configurar_logging  # noqa: E402
RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

configurar_logging(LOG_DIR / "nulos_ar1_log.txt")
log = logging.getLogger("nulos_ar1")

SEMILLA = 20261026          # preregistro
M_REPLICAS = 2000           # preregistro
PHI_TOPE = 0.995            # preregistro


def cargar_aco():
    """Series ACO crudas: t > 0, R > 0, orden por t."""
    df = pd.read_csv(RR / "snt_corpus_aco_timeseries_v29.csv")
    df = df[(df["t"] > 0) & (df["R"] > 0)].sort_values(["id", "t"])
    series = {}
    for cid, g in df.groupby("id", sort=True):
        series[cid] = np.log10(g["R"].to_numpy(dtype=float))
    return series


def ajustar_ar1(x):
    """(mu, phi, sigma_eps, n) según la receta del preregistro."""
    n = len(x)
    mu = float(np.mean(x))
    xc = x - mu
    if n < 3:
        return mu, 0.0, float(np.std(x, ddof=1)) if n > 1 else 0.0, n
    phi = float(np.sum(xc[1:] * xc[:-1]) / np.sum(xc[:-1] ** 2))
    phi = min(max(phi, 0.0), PHI_TOPE)
    resid = xc[1:] - phi * xc[:-1]
    sigma = float(np.std(resid, ddof=1)) if len(resid) > 1 else 0.0
    return mu, phi, sigma, n


def simular_caso(mu, phi, sigma, x0, n, m_reps, rng):
    """M trayectorias AR(1) ancladas a x0. Devuelve |x_T| por réplica."""
    if n < 2:
        return np.full(m_reps, abs(x0))
    x = np.full(m_reps, x0, dtype=float)
    for _ in range(n - 1):
        x = mu + phi * (x - mu) + sigma * rng.standard_normal(m_reps)
    return np.abs(x)


def main():
    log.info("=" * 78)
    log.info("NULOS AR(1) PARA LA CONVERGENCIA ACO-A — preregistro 2026-10-26")
    log.info("Semilla %d · %d réplicas/caso · φ clamp [0, %.3f]",
             SEMILLA, M_REPLICAS, PHI_TOPE)
    log.info("=" * 78)

    rng = np.random.default_rng(SEMILLA)
    aco = cargar_aco()
    log.info("ACO: %d casos (serie cruda, t>0, R>0)", len(aco))

    filas = []
    finales_nulo = {}      # cid -> |x*_T| por réplica
    for cid, x in sorted(aco.items()):
        mu, phi, sigma, n = ajustar_ar1(x)
        d_ini, d_fin = abs(x[0]), abs(x[-1])
        fins = simular_caso(mu, phi, sigma, x[0], n, M_REPLICAS, rng)
        finales_nulo[cid] = fins
        filas.append({
            "id": cid, "n": n,
            "mu": round(mu, 4), "phi": round(phi, 4),
            "sigma_eps": round(sigma, 4),
            "d_ini": round(d_ini, 4), "d_fin": round(d_fin, 4),
            "nulo_p05": round(float(np.quantile(fins, 0.05)), 4),
            "nulo_p50": round(float(np.quantile(fins, 0.50)), 4),
            "nulo_p95": round(float(np.quantile(fins, 0.95)), 4),
            "fin_dentro_nulo_p50": bool(d_fin <= np.quantile(fins, 0.50)),
        })
        log.info("  %-27s n=%d φ=%.3f μ=%+.3f σ=%.3f | %+.3f → %+.3f "
                 "(nulo p50 |x_T|=%.3f)", cid, n, phi, mu, sigma,
                 -filas[-1]["d_ini"], -filas[-1]["d_fin"],
                 filas[-1]["nulo_p50"])

    df = pd.DataFrame(filas)
    df.to_csv(RR / "nulos_ar1_aco.csv", index=False)

    # ── Estadístico global S: mediana de |x_T| sobre los 18 casos ──
    s_obs = float(np.median([abs(x[-1]) for x in aco.values()]))
    s_ini = float(np.median([abs(x[0]) for x in aco.values()]))
    mat = np.stack([finales_nulo[cid] for cid in sorted(finales_nulo)])
    s_nulo = np.median(mat, axis=0)          # (M,) mediana por réplica
    p_n1 = float((1 + np.sum(s_nulo <= s_obs)) / (M_REPLICAS + 1))

    log.info("")
    log.info("S_obs (mediana |log10 R_T|, 18 casos) = %.4f "
             "(inicio mediana %.4f)", s_obs, s_ini)
    log.info("N1: mediana del nulo %.4f [p5 %.4f, p95 %.4f] · "
             "p_N1 = P(S* ≤ S_obs) = %.4f",
             float(np.median(s_nulo)), float(np.quantile(s_nulo, 0.05)),
             float(np.quantile(s_nulo, 0.95)), p_n1)

    # ── Contraste B: ventanas que NO terminan en evento ──
    tela = pd.read_csv(RR / "tela_de_incertidumbre.csv")
    tb = tela[tela["dominio"] == "B"].sort_values(["id", "t"])
    s_b = None
    d_ini_b = None
    if len(tb):
        por_caso = tb.groupby("id")["m"].agg(["first", "last"])
        s_b = float(np.median(np.abs(np.log10(por_caso["last"]))))
        d_ini_b = float(np.median(np.abs(np.log10(por_caso["first"]))))
        log.info("Contraste B (n=%d, terminan en 2018 por ventana): "
                 "mediana |log10 R_T| = %.4f (inicio %.4f)",
                 len(por_caso), s_b, d_ini_b)

    resumen = pd.DataFrame([{
        "n_casos_aco": len(aco),
        "mediana_d_ini": round(s_ini, 4),
        "S_obs": round(s_obs, 4),
        "nulo_p50": round(float(np.median(s_nulo)), 4),
        "nulo_p05": round(float(np.quantile(s_nulo, 0.05)), 4),
        "nulo_p95": round(float(np.quantile(s_nulo, 0.95)), 4),
        "p_N1": round(p_n1, 4),
        "B_n": len(tb.groupby("id")) if len(tb) else 0,
        "B_mediana_d_ini": round(d_ini_b, 4) if d_ini_b is not None else None,
        "B_S": round(s_b, 4) if s_b is not None else None,
        "replicas": M_REPLICAS, "semilla": SEMILLA,
    }])
    resumen.to_csv(RR / "nulos_ar1_resumen.csv", index=False)

    log.info("")
    if p_n1 > 0.05:
        log.info("VEREDICTO PRE-ESPECIFICADO 1: la convergencia observada "
                 "está DENTRO de lo que la dinámica AR(1) de las propias "
                 "series produce — explicada por regresión a la media hacia "
                 "μ ≈ 0. No aporta evidencia adicional de 'firma' más allá "
                 "de la dinámica ya medida.")
    else:
        log.info("VEREDICTO PRE-ESPECIFICADO 2: la convergencia observada es "
                 "MÁS cerrada que la dinámica propia (p_N1=%.4f) — se "
                 "reporta como desviación del nulo; NO se interpreta como "
                 "'firma del colapso' por sí sola.", p_n1)
    log.info("EJECUCION COMPLETADA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
