"""Eje u con Entropía de Permutación (series cortas) y Dimensión de Correlación (series largas)

Pre-registro:
    reconstruction_real/preregistro/PREREGISTRO_EJE_U_PERMUTACION_DIMCOR_2026-11-04.md

Script determinista, sin red, con log y SHA-256.
"""

import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))
from snt import configurar_log, sha256 as sha256_file
from eje_u_metrics import (
    correlation_dimension_pair_series,
    effective_pattern_count,
    permutation_entropy_series,
)

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
CRYPTO_META = CRYPTO_DIR / "casos_binance.csv"
BINANCE = ROOT / "data" / "binance_cierres_diarios.csv.gz"

def sha256_path(p: Path) -> str:
    return sha256_file(str(p))

log.info("SHA-256 inputs")
for p in [B_META, MADDISON, CRYPTO_META]:
    if p.exists():
        log.info(f"{p}: {sha256_path(p)}")
    else:
        log.warning(f"{p} no existe")

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
    pe_m3 = permutation_entropy_series(logR, m=3, window=window)
    pe_m4 = permutation_entropy_series(logR, m=4, window=window)
    u_m3 = effective_pattern_count(pe_m3, m=3)
    u_m4 = effective_pattern_count(pe_m4, m=4)
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
        "pe_m3_series_mean": float(np.nanmean(pe_m3)),
        "pe_m4_series_mean": float(np.nanmean(pe_m4)),
        "u_pe_m3_series_mean": float(np.nanmean(u_m3)),
        "u_pe_m4_series_mean": float(np.nanmean(u_m4)),
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

log.info("Cargando casos cripto Binance")
dfc_meta = pd.read_csv(CRYPTO_META)
# cargar binance completo una vez
log.info("Cargando datos Binance")
binance = pd.read_csv(BINANCE, usecols=['par','fecha','close'])
binance['fecha'] = pd.to_datetime(binance['fecha'], errors='coerce')
binance = binance.dropna(subset=['fecha'])
# índice por par
binance_dict = {par: grp.sort_values('fecha')[['fecha','close']].reset_index(drop=True) for par, grp in binance.groupby('par')}

crypto_rows = []
for _, r in dfc_meta.iterrows():
    case_id = r['id']
    coin_pair = r['coin_pair']
    # R(t) = close_coin / close_BTCUSDT
    try:
        df_coin = binance_dict.get(coin_pair)
        df_btc = binance_dict.get('BTCUSDT')
        if df_coin is None or df_btc is None:
            raise ValueError("par no encontrado")
    except Exception as e:
        log.warning(f"{case_id} carga fallida: {e}")
        crypto_rows.append({
            "dominio": "Crypto",
            "id": case_id,
            "n_observaciones": 0,
            "elegible": False,
            "motivo": "carga_fallida",
            "d2_mean": np.nan,
            "d2_mean_emb3": np.nan,
            "spearman_emb2_emb3": np.nan,
            "iqr_u": np.nan,
            "n_posiciones_validas": 0
        })
        continue
    # merge por fecha
    merged = pd.merge(df_coin, df_btc, on='fecha', suffixes=('_coin','_btc'))
    merged = merged.dropna(subset=['close_coin','close_btc'])
    if len(merged) < 250:
        crypto_rows.append({
            "dominio": "Crypto",
            "id": case_id,
            "n_observaciones": len(merged),
            "elegible": False,
            "motivo": "serie_corta",
            "d2_mean": np.nan,
            "d2_mean_emb3": np.nan,
            "spearman_emb2_emb3": np.nan,
            "iqr_u": np.nan,
            "n_posiciones_validas": 0
        })
        continue
    R = merged['close_coin'].values / merged['close_btc'].values
    R = R[R>0]
    logR = np.log(R)
    # D2 con embedding 2 y 3 para invarianza
    d2_series = correlation_dimension_pair_series(
        logR, window=200, embeddings=(2, 3), tau=1
    )
    d2_series_2 = d2_series[2]
    d2_series_3 = d2_series[3]
    valid = ~np.isnan(d2_series_2) & ~np.isnan(d2_series_3)
    n_valid = int(valid.sum())
    if n_valid >= 12:
        spearman, _ = spearmanr(d2_series_2[valid], d2_series_3[valid])
    else:
        spearman = np.nan
    d2_mean_2 = float(np.nanmean(d2_series_2[valid])) if n_valid>0 else np.nan
    d2_mean_3 = float(np.nanmean(d2_series_3[valid])) if n_valid>0 else np.nan
    # u^D2_t = exp(D2_t)
    u2 = np.exp(d2_series_2)
    u3 = np.exp(d2_series_3)
    iqr_u = float(np.nanpercentile(u2[valid],75)-np.nanpercentile(u2[valid],25)) if n_valid>0 else np.nan
    crypto_rows.append({
        "dominio": "Crypto",
        "id": case_id,
        "n_observaciones": len(logR),
        "elegible": True,
        "motivo": "",
        "d2_mean": d2_mean_2,
        "d2_mean_emb3": d2_mean_3,
        "spearman_emb2_emb3": float(spearman) if np.isfinite(spearman) else np.nan,
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
    "mediana_iqr": df_crypto["iqr_u"].median(),
    "mediana_spearman_emb": df_crypto["spearman_emb2_emb3"].median()
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
- Mediana D2 emb2: {crypto_summary['mediana_d2']:.3f}
- Mediana IQR u^D2: {crypto_summary['mediana_iqr']:.3f}
- Mediana Spearman emb2/emb3: {crypto_summary['mediana_spearman_emb']:.3f}

## Implementación conforme al pre-registro
- `u^PE` se calcula como número efectivo de patrones (`exp(PE × log(m!))`):
  m=3 para la métrica primaria y m=4 para la comparación de invarianza.
- D2 se estima por regresión lineal de `log C(r)` sobre `log r` en 11 radios
  equiespaciados entre `0.05σ` y `0.3σ`; ambos embeddings usan los mismos
  radios por ventana, con `σ` de la serie en esa ventana.

## Próximos pasos
- Calcular métricas por ventana deslizante para compuertas de invarianza A–D completas y decisión pre-especificada.
"""

OUT_AUDIT.write_text(audit_md, encoding="utf-8")
log.info(f"Auditoría escrita a {OUT_AUDIT}")
log.info("Ejecución completada — infraestructura lista")
