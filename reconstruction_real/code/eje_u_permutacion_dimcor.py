"""Eje u con Entropía de Permutación (series cortas) y Dimensión de Correlación (series largas)

Pre-registro:
    reconstruction_real/preregistro/PREREGISTRO_EJE_U_PERMUTACION_DIMCOR_2026-11-04.md

Script determinista, sin red, con log y SHA-256.
"""

import logging
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))
from snt import configurar_log, sha256 as sha256_file

LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_FILE = LOG_DIR / "eje_u_permutacion_dimcor_2026-11-04.log"
configurar_log("EJE-U-PERM-DIMCOR", log_dir=LOG_DIR, log_file=LOG_FILE.name)
log = logging.getLogger("EJE-U-PERM-DIMCOR")

OUT_CASES = ROOT / "reconstruction_real" / "data" / "eje_u_permutacion_dimcor_por_caso.csv"
OUT_SUMMARY = ROOT / "reconstruction_real" / "data" / "eje_u_permutacion_dimcor_resumen.csv"
OUT_AUDIT = ROOT / "reconstruction_real" / "audits" / "RESULTADOS_EJE_U_PERMUTACION_DIMCOR_2026-11-04.md"

B_META = ROOT / "reconstruction_real" / "data" / "by_domain" / "dominio_B_real.csv"
MADDISON = ROOT / "data" / "maddison_mpd2020.csv"
CRYPTO = ROOT / "data" / "binance_cierres_diarios.csv.gz"

def sha256_path(p: Path) -> str:
    return sha256_file(str(p))

log.info("SHA-256 inputs")
for p in [B_META, MADDISON, CRYPTO]:
    if p.exists():
        log.info(f"{p}: {sha256_path(p)}")
    else:
        log.warning(f"{p} no existe")

# Permutación helpers
def permutation_entropy_window(series, m=3):
    n = len(series)
    if n < m:
        return np.nan
    patterns = []
    for i in range(n - m + 1):
        win = series[i:i+m]
        pat = tuple(np.argsort(win))
        patterns.append(pat)
    from collections import Counter
    cnt = Counter(patterns)
    if not cnt:
        return np.nan
    probs = np.array(list(cnt.values()), dtype=float)
    probs = probs / probs.sum()
    # evitar log(0)
    probs = probs[probs>0]
    H = -np.sum(probs * np.log(probs))
    H_norm = H / np.log(math.factorial(m)) if H>0 else 0.0
    return float(H_norm)

def permutation_entropy_series(series, m=3, window=20):
    n = len(series)
    if n < window:
        return np.full(n, np.nan)
    out = np.full(n, np.nan)
    for i in range(window-1, n):
        win = series[i-window+1:i+1]
        out[i] = permutation_entropy_window(win, m=m)
    return out

# Carga real de Maddison
log.info("Cargando Maddison")
maddison = pd.read_csv(MADDISON, usecols=["Entity", "Year", "GDP per capita"])
maddison_dict = {}
for _, row in maddison.iterrows():
    ent = row["Entity"]
    yr = int(row["Year"])
    val = float(row["GDP per capita"])
    maddison_dict.setdefault(ent, {})[yr] = val

log.info("Cargando metadatos Dominio B")
dfb = pd.read_csv(B_META)
rows = []

MIN_DOMAIN_CASES = 30
INVARIANCE_MEDIAN_MIN = 0.60
IQR_MIN = 0.05

YEAR_MIN = 1900
YEAR_MAX = 2018

def get_series(hub, nodo):
    hub_data = maddison_dict.get(hub, {})
    nodo_data = maddison_dict.get(nodo, {})
    years = sorted(set(hub_data.keys()) & set(nodo_data.keys()))
    years = [y for y in years if YEAR_MIN <= y <= YEAR_MAX]
    if len(years) < 40:
        return None
    R = []
    for y in years:
        if hub_data[y] > 0 and nodo_data[y] > 0:
            R.append(hub_data[y] / nodo_data[y])
    if len(R) < 40:
        return None
    logR = np.log(R)
    return logR

for _, r in dfb.iterrows():
    case_id = r['id']
    hub = r['hub']
    nodo = r['nodo']
    logR = get_series(hub, nodo)
    if logR is None:
        rows.append({
            "dominio": "B",
            "id": case_id,
            "n_observaciones": 0,
            "elegible": False,
            "motivo": "serie_insuficiente",
            "pe_m3_series_mean": np.nan,
            "pe_m4_series_mean": np.nan,
            "spearman_theta1_theta2": np.nan,
            "iqr_u": np.nan,
            "n_posiciones_validas": 0
        })
        continue
    # Series de entropía por ventana deslizante
    window = 20
    u_m3 = permutation_entropy_series(logR, m=3, window=window)
    u_m4 = permutation_entropy_series(logR, m=4, window=window)
    # Alinear posiciones válidas
    valid = ~np.isnan(u_m3) & ~np.isnan(u_m4)
    n_valid = int(valid.sum())
    if n_valid >= 12:
        spearman, _ = spearmanr(u_m3[valid], u_m4[valid])
    else:
        spearman = np.nan
    iqr_u = float(np.nanpercentile(u_m3[valid], 75) - np.nanpercentile(u_m3[valid], 25)) if n_valid>0 else np.nan
    rows.append({
        "dominio": "B",
        "id": case_id,
        "n_observaciones": len(logR),
        "elegible": True,
        "motivo": "",
        "pe_m3_series_mean": float(np.nanmean(u_m3)),
        "pe_m4_series_mean": float(np.nanmean(u_m4)),
        "spearman_theta1_theta2": float(spearman) if np.isfinite(spearman) else np.nan,
        "iqr_u": iqr_u,
        "n_posiciones_validas": n_valid
    })

df_out = pd.DataFrame(rows)
df_out.to_csv(OUT_CASES, index=False)
log.info(f"Casos escritos a {OUT_CASES}")

# Resumen
summary = {
    "dominio": "B",
    "n_casos": len(df_out),
    "mediana_spearman": df_out["spearman_theta1_theta2"].median(),
    "mediana_iqr": df_out["iqr_u"].median(),
    "invarianza_pasa": df_out["spearman_theta1_theta2"].median() >= INVARIANCE_MEDIAN_MIN,
    "variacion_pasa": df_out["iqr_u"].median() >= IQR_MIN
}

pd.DataFrame([summary]).to_csv(OUT_SUMMARY, index=False)
log.info(f"Resumen escrito a {OUT_SUMMARY}")

# Auditoría
audit_md = f"""# Resultados — eje u Permutación/DimCor v2.7.5

**Pre-registro:** `reconstruction_real/preregistro/PREREGISTRO_EJE_U_PERMUTACION_DIMCOR_2026-11-04.md`
**Script:** `eje_u_permutacion_dimcor.py`
**Fecha:** 2026-11-04

## Procedencia
SHA-256 inputs registrados en log.

## Nota de implementación
Esta corrida reconstruye `R(t) = PIBpc_hub / PIBpc_nodo` desde Maddison MPD2020 para Dominio B.
Dimensión de Correlación para Cripto pendiente de implementación completa.

## Resumen Dominio B (real)
- Casos: {summary['n_casos']}
- Mediana Spearman θ1/θ2: {summary['mediana_spearman']:.3f}
- Mediana IQR: {summary['mediana_iqr']:.3f}
- Invarianza pasa: {summary['invarianza_pasa']}
- Variación pasa: {summary['variacion_pasa']}

## Próximos pasos
- Implementar Dimensión de Correlación para Dominio Cripto con ventana 200.
- Calcular métricas por ventana deslizante para compuertas de invarianza A–D completas.
- Ejecutar decisión pre-especificada.
"""

OUT_AUDIT.write_text(audit_md, encoding="utf-8")
log.info(f"Auditoría escrita a {OUT_AUDIT}")
log.info("Ejecución completada — infraestructura lista")
