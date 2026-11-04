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
CRYPTO_DIR = ROOT / "data" / "cripto"
CRYPTO_META = CRYPTO_DIR / "casos_cripto.csv"

def sha256_path(p: Path) -> str:
    return sha256_file(str(p))

log.info("SHA-256 inputs")
for p in [B_META, MADDISON, CRYPTO_META]:
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

def correlation_sum(distances, r):
    if len(distances) == 0:
        return np.nan
    return np.mean(distances < r)

def correlation_dimension_series(series, window=200, m_emb=2, tau=1, r_frac=0.1):
    n = len(series)
    if n < window:
        return np.full(n, np.nan)
    out = np.full(n, np.nan)
    # normalizar serie a media 0 y std 1 para estabilidad
    s = series - np.mean(series)
    s = s / (np.std(s) + 1e-12)
    for i in range(window-1, n):
        win = s[i-window+1:i+1]
        L = len(win)
        if L < m_emb * tau + 1:
            out[i] = np.nan
            continue
        # reconstrucción
        N = L - (m_emb-1)*tau
        if N < 10:
            out[i] = np.nan
            continue
        # matriz de embedding
        X = np.array([win[j:j+m_emb*tau:tau] for j in range(N)])
        # distancias pareadas aproximadas con muestreo
        # para velocidad, muestrear 400 puntos
        sample_n = min(400, N)
        idx = np.linspace(0, N-1, sample_n, dtype=int)
        Xs = X[idx]
        # distancias euclidianas
        from scipy.spatial.distance import pdist
        dists = pdist(Xs, metric='euclidean')
        # rango de r
        r_max = np.max(dists) * r_frac
        if r_max <= 0:
            out[i] = np.nan
            continue
        r1 = r_max * 0.5
        r2 = r_max * 1.5
        c1 = correlation_sum(dists, r1)
        c2 = correlation_sum(dists, r2)
        if c1 <= 0 or c2 <= 0 or c1 == c2:
            out[i] = np.nan
            continue
        d2 = np.log(c2 / c1) / np.log(r2 / r1)
        out[i] = float(d2)
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

# Crypto DimCor
OUT_CRYPTO_CASES = ROOT / "reconstruction_real" / "data" / "eje_u_dimcor_crypto_por_caso.csv"
OUT_CRYPTO_SUMMARY = ROOT / "reconstruction_real" / "data" / "eje_u_dimcor_crypto_resumen.csv"

log.info("Cargando casos cripto")
dfc_meta = pd.read_csv(CRYPTO_META)
crypto_rows = []
for _, r in dfc_meta.iterrows():
    case_id = r['id']
    coin_file = CRYPTO_DIR / r['coin_file']
    try:
        dfc = pd.read_csv(coin_file, usecols=["Date","Close"])
    except Exception as e:
        log.warning(f"{case_id} carga fallida: {e}")
        crypto_rows.append({
            "dominio": "Crypto",
            "id": case_id,
            "n_observaciones": 0,
            "elegible": False,
            "motivo": "carga_fallida",
            "d2_mean": np.nan,
            "iqr_u": np.nan,
            "n_posiciones_validas": 0
        })
        continue
    # limpiar
    dfc["Date"] = pd.to_datetime(dfc["Date"], errors="coerce")
    dfc = dfc.dropna(subset=["Close","Date"])
    dfc = dfc.sort_values("Date")
    prices = dfc["Close"].values.astype(float)
    # eliminar ceros
    prices = prices[prices>0]
    logp = np.log(prices)
    if len(logp) < 250:
        crypto_rows.append({
            "dominio": "Crypto",
            "id": case_id,
            "n_observaciones": len(logp),
            "elegible": False,
            "motivo": "serie_corta",
            "d2_mean": np.nan,
            "iqr_u": np.nan,
            "n_posiciones_validas": 0
        })
        continue
    d2_series = correlation_dimension_series(logp, window=200, m_emb=2, tau=1, r_frac=0.2)
    valid = ~np.isnan(d2_series)
    n_valid = int(valid.sum())
    d2_mean = float(np.nanmean(d2_series)) if n_valid>0 else np.nan
    iqr_u = float(np.nanpercentile(d2_series[valid],75)-np.nanpercentile(d2_series[valid],25)) if n_valid>0 else np.nan
    crypto_rows.append({
        "dominio": "Crypto",
        "id": case_id,
        "n_observaciones": len(logp),
        "elegible": True,
        "motivo": "",
        "d2_mean": d2_mean,
        "iqr_u": iqr_u,
        "n_posiciones_validas": n_valid
    })

df_crypto = pd.DataFrame(crypto_rows)
df_crypto.to_csv(OUT_CRYPTO_CASES, index=False)
log.info(f"Cripto casos escritos a {OUT_CRYPTO_CASES}")

crypto_summary = {
    "dominio": "Crypto",
    "n_casos": len(df_crypto),
    "n_elegibles": int(df_crypto["elegible"].sum()),
    "mediana_d2": df_crypto["d2_mean"].median(),
    "mediana_iqr": df_crypto["iqr_u"].median()
}
pd.DataFrame([crypto_summary]).to_csv(OUT_CRYPTO_SUMMARY, index=False)
log.info(f"Cripto resumen escrito a {OUT_CRYPTO_SUMMARY}")

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
Esta corrida reconstruye `R(t) = PIBpc_hub / PIBpc_nodo` desde Maddison MPD2020 para Dominio B y estima Dimensión de Correlación para Cripto con ventana 200.

## Resumen Dominio B (real)
- Casos: {summary['n_casos']}
- Mediana Spearman θ1/θ2: {summary['mediana_spearman']:.3f}
- Mediana IQR: {summary['mediana_iqr']:.3f}
- Invarianza pasa: {summary['invarianza_pasa']}
- Variación pasa: {summary['variacion_pasa']}

## Resumen Cripto D2
- Casos: {crypto_summary['n_casos']}
- Elegibles: {crypto_summary['n_elegibles']}
- Mediana D2: {crypto_summary['mediana_d2']:.3f}
- Mediana IQR D2: {crypto_summary['mediana_iqr']:.3f}

## Próximos pasos
- Calcular métricas por ventana deslizante para compuertas de invarianza A–D completas y decisión pre-especificada.
- Refinar estimador D2 con muestreo adaptativo y rango r optimizado.
"""

OUT_AUDIT.write_text(audit_md, encoding="utf-8")
log.info(f"Auditoría escrita a {OUT_AUDIT}")
log.info("Ejecución completada — infraestructura lista")
