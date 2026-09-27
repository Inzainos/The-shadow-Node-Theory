"""
Construye la entrada exacta del dominio B a partir de la fuente primaria.

El dominio B (446 pares de países, 62% del corpus) se construyó con el
Maddison Project Database 2020 (MPD2020, cobertura 1–2018), con los nombres
de país de Our World in Data. Esa edición nunca se fijó en el repo y la copia
vigente de OWID (`data/owid-maddison.csv`, descargada 2026-07-25) es una
edición posterior: con ella B solo se regenera aproximado (441 vs 446 casos).

Este script convierte `data/mpd2020.xlsx` (hoja "Full data") al formato que
leen los scripts del dominio B (`Entity, Code, Year, GDP per capita`):

  * verifica el SHA-256 del xlsx contra el valor anclado en `data/FUENTES.md`;
  * traduce los nombres de MPD a los de OWID por código ISO3, usando la tabla
    Code -> Entity de `data/owid-maddison.csv` (solo para nombres, no datos);
  * los países sin equivalente en esa tabla conservan el nombre de MPD, salvo
    "Sudan (Former)" -> "Sudan" (nombre con el que OWID publicaba la serie).

Con la salida, `expand_B_massive.py` reproduce el dominio B publicado byte a
byte (446/446 casos; SHA-256 idéntico al de `by_domain/dominio_B_real.csv`).

Salidas:
    data/maddison_mpd2020.csv
    reconstruction_real/logs/build_maddison_mpd2020_csv_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/build_maddison_mpd2020_csv.py
"""

import hashlib
import logging
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_TOP = ROOT / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

IN_XLSX = DATA_TOP / "mpd2020.xlsx"
IN_NOMBRES = DATA_TOP / "owid-maddison.csv"
OUT_CSV = DATA_TOP / "maddison_mpd2020.csv"
LOG_FILE = LOG_DIR / "build_maddison_mpd2020_csv_log.txt"

# SHA-256 del xlsx descargado de la GGDC (ver data/FUENTES.md)
SHA256_XLSX = "d20853c2e0930d6855fb6d8138da11f24fcf313d234e2db9773ea1f551adfec3"
# Nombres de MPD sin equivalente por ISO3 en la tabla de OWID
RENOMBRES = {"Sudan (Former)": "Sudan"}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("MADDISON-2020")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def main():
    digest = sha256(IN_XLSX)
    log.info("Fuente: %s | SHA-256 %s", IN_XLSX.relative_to(ROOT), digest)
    if digest != SHA256_XLSX:
        log.error("SHA-256 no coincide con el anclado (%s): la fuente cambió",
                  SHA256_XLSX)
        sys.exit(1)

    mpd = pd.read_excel(IN_XLSX, sheet_name="Full data")
    log.info("MPD2020 'Full data': %d filas, %d países, años %d-%d",
             len(mpd), mpd["countrycode"].nunique(),
             int(mpd["year"].min()), int(mpd["year"].max()))

    nombres = (pd.read_csv(IN_NOMBRES).dropna(subset=["Code"])
               .drop_duplicates("Code").set_index("Code")["Entity"])
    mpd["Entity"] = mpd["countrycode"].map(nombres)
    sin_mapa = mpd["Entity"].isna()
    mpd.loc[sin_mapa, "Entity"] = mpd.loc[sin_mapa, "country"].replace(RENOMBRES)
    for pais in sorted(mpd.loc[sin_mapa, "country"].unique()):
        log.info("Sin equivalente OWID por ISO3: %-20s -> %s",
                 pais, RENOMBRES.get(pais, pais))

    antes = len(mpd)
    mpd = mpd.dropna(subset=["gdppc"])
    log.info("Filas sin gdppc descartadas (faltante, no cero): %d",
             antes - len(mpd))

    out = (mpd.rename(columns={"countrycode": "Code", "year": "Year",
                               "gdppc": "GDP per capita"})
           [["Entity", "Code", "Year", "GDP per capita"]])
    out.to_csv(OUT_CSV, index=False)
    log.info("CSV -> %s | %d filas, %d entidades | SHA-256 %s",
             OUT_CSV.relative_to(ROOT), len(out), out["Entity"].nunique(),
             sha256(OUT_CSV))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
