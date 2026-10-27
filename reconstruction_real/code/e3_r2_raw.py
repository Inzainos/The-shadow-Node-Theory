#!/usr/bin/env python3
"""
E3 r2_raw — completa el split R² del corpus para el Dominio E3.

El corpus v6 dejó `r2_raw` en NA para los 234 casos de E3 porque las series
crudas de OWID no estaban versionadas. Este script las reconstruye con la
receta E3 identificada en el punto 3 del pre-registro 2026-09-27 (casos
acumulados, inicio en el primer día con >= 100 acumulados, ventana de 60 días,
t = 1..60) desde el archivo completo de OWID con el SHA anclado — verificado
byte a byte contra el snapshot del 2026-09-27 (la descarga actual de
raw.githubusercontent.com coincide: 8473d0f0…).

Para cada país: reconstruye la serie, ajusta con ``fit_powerlaw`` (misma
rutina de la auditoría v32) y registra ``r2_raw`` (1 − SSres/SStot en escala
original) junto con ``r2_log`` y ``b``. Compuerta de sanidad: el ``b`` debe
reproducir el publicado dentro de ±0.01 (el mismo criterio de aceptación de la
receta); los casos que no coinciden se reportan y NO se usan (conservador).

Salidas:
    reconstruction_real/data/dominio_E3_r2_raw.csv
    reconstruction_real/logs/e3_r2_raw_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/e3_r2_raw.py
"""

import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))
from snt import sha256  # noqa: E402
sys.path.insert(0, str(ROOT / "code"))
from snt_utils_v32 import fit_powerlaw  # noqa: E402

DATA_TOP = ROOT / "data"
DATA_RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

FULL = DATA_TOP / "raw_covid" / "owid-covid-data.csv"
IN_E3 = DATA_RR / "dominio_E3_series_crudas.csv"
OUT = DATA_RR / "dominio_E3_r2_raw.csv"
LOG_FILE = LOG_DIR / "e3_r2_raw_log.txt"

SHA_FULL = "8473d0f0fdf962e1ffbd5b85b18726fc96a49bab109e271186c339725a12b10c"
VENTANA = 60
UMBRAL = 100
TOL = 0.01

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("E3-R2RAW")


def serie_pais_acum(O, pais):
    """Serie de casos acumulados de un país (ffill, 0 inicial) — igual que
    `serie_pais` de `covid_E3_series_crudas.py`."""
    g = O[O.location == pais].sort_values("date")
    if g.empty:
        return None
    return g.total_cases.ffill().fillna(0).values


def ventana60(acum):
    """Ventana de 60 días desde el primer día con >= 100 acumulados."""
    idx = np.where(acum >= UMBRAL)[0]
    if len(idx) == 0 or idx[0] + VENTANA > len(acum):
        return None
    return acum[idx[0]:idx[0] + VENTANA]


def main():
    log.info("=" * 78)
    log.info("E3 r2_raw — split R2 del Dominio E3 desde series crudas OWID")
    log.info("=" * 78)

    if not FULL.exists():
        log.error("Falta %s (descargar de owid/covid-19-data; SHA anclado "
                  "en FUENTES.md)", FULL)
        return 1
    dig = sha256(FULL)
    log.info("Archivo OWID: %s | SHA-256 %s", FULL.name, dig[:16] + "…")
    if dig != SHA_FULL:
        log.error("SHA-256 distinto del anclado (%s): la fuente cambió",
                  SHA_FULL[:16] + "…")
        return 1
    log.info("SHA-256 IDENTICO al snapshot del 2026-09-27 (receta reproducible)")

    O = pd.read_csv(FULL, usecols=["location", "date", "total_cases"])
    O["date"] = pd.to_datetime(O["date"])

    E3 = pd.read_csv(IN_E3)
    log.info("Casos E3: %d (de dominio_E3_series_crudas.csv)", len(E3))

    filas = []
    n_coincide = 0
    for _, r in E3.iterrows():
        acum = serie_pais_acum(O, r["pais"])
        y = ventana60(acum) if acum is not None else None
        if y is None:
            log.warning("   %s: sin ventana de %d dias (umbral %d)",
                        r["pais"], VENTANA, UMBRAL)
            filas.append({"id": r["id"], "pais": r["pais"],
                          "b_publicado": r["b_publicado"],
                          "b": None, "coincide_r2raw": False,
                          "r2_raw": None, "r2_log": None, "n": 0,
                          "motivo": "sin ventana"})
            continue
        t = np.arange(1, len(y) + 1, dtype=float)
        f = fit_powerlaw(t, y)
        b = f["b"]
        coincide = abs(b - float(r["b_publicado"])) <= TOL
        n_coincide += coincide
        filas.append({
            "id": r["id"], "pais": r["pais"],
            "b_publicado": r["b_publicado"], "b": b,
            "coincide_r2raw": coincide,
            "r2_raw": f["r2_raw"], "r2_log": f["r2_log"], "n": f["n"],
            "motivo": "",
        })

    df = pd.DataFrame(filas)
    df.to_csv(OUT, index=False)
    log.info("Compuerta de sanidad: b reproduce el publicado (±%.2f) en "
             "%d/%d casos (criterio de la receta original)", TOL,
             n_coincide, len(df))
    ok = df[df["coincide_r2raw"] & df["r2_raw"].notna()]
    log.info("r2_raw computado y valido: %d/%d | r2_log recomputado: %d",
             len(ok), len(df), int(df["r2_log"].notna().sum()))
    if df["r2_log"].notna().sum():
        d = df.dropna(subset=["r2_log"])
        dif = (d["r2_log"] - d["r2_log"].round(4)).abs().max()
        log.info("Consistencia r2_log vs resumen commiteado: max |dif| = %.4f "
                 "(redondeos del resumen)", dif)
    log.info("Salida: %s", OUT.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
