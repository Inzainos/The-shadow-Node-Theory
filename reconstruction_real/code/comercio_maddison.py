"""
Utilidades compartidas para cruzar COW Trade v4.0 con Maddison 2020.

Las usan `reconstruccion_B_hub_comercio.py` (hub emergente fijo, PR #45) y
`prueba_hub_temporal.py` (hub variable en el tiempo, pre-registro 2026-09-27).
No configura logging: cada script pasa su propio `log`.

Reglas de entidad (mismo territorio o nada):
    * exportador COW -> país del corpus: `entidad_nodo` (URSS ≠ Rusia 1917–1991,
      Yugoslavia ≠ Serbia 1918–2005, Vietnam del Norte < 1976, Pakistán
      unificado < 1972);
    * destino COW -> entidad Maddison 2020: `socio_maddison` (URSS -> Former
      USSR, Yugoslavia 1918–1991 -> Former Yugoslavia, Checoslovaquia ->
      Czechoslovakia, RFA -> Germany como única aproximación).
"""

import hashlib
import sys
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_TOP = ROOT / "data"
IN_ZIP = DATA_TOP / "COW_Trade_4.0.zip"
MIEMBRO = "COW_Trade_4.0/Dyadic_COW_4.0.csv"
IN_MADDISON = DATA_TOP / "maddison_mpd2020.csv"
IN_MPD_XLSX = DATA_TOP / "mpd2020.xlsx"
SHA256_ZIP = "c44c4b5ce62e68865368482c428306df4624d3a39edec29adc1aa2c0928f7cc7"

# Miembros del CMEA (Consejo de Ayuda Mutua Económica) presentes como nodos
CMEA = {"Poland", "Hungary", "Romania", "Bulgaria", "Czechia", "Mongolia",
        "Cuba", "Vietnam"}

RENOMBRE_SOCIO = {
    "United States of America": "United States",
    "Czech Republic": "Czechia",
    "Ivory Coast": "Cote d'Ivoire",
    "Democratic Republic of the Congo": "Democratic Republic of Congo",
    "Macedonia": "North Macedonia",
    "Swaziland": "Eswatini",
}
SIN_ENTIDAD = {"Korea", "German Democratic Republic", "Republic of Vietnam",
               "Yemen Arab Republic", "Yemen People's Republic",
               "Austria-Hungary", "Baden", "Bavaria", "Wuerttemburg",
               "Zanzibar"}
APROX = {"German Federal Republic": "Germany"}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def entidad_nodo(nombre, anio):
    """Nombre COW del EXPORTADOR -> nombre del corpus (mismas reglas que
    build_comercio_bilateral_cow.entidad); None = otro territorio."""
    if nombre == "United States of America":
        return "United States"
    if nombre == "Czech Republic":
        return "Czechia"
    if nombre == "Yugoslavia":
        return "Serbia" if (anio < 1918 or anio >= 2006) else None
    if nombre == "Russia" and 1917 <= anio <= 1991:
        return None
    if nombre == "Vietnam" and anio < 1976:
        return None
    if nombre == "Pakistan" and anio < 1972:
        return None
    return nombre


def socio_maddison(nombre, anio, entidades):
    """Destino COW -> entidad Maddison 2020 con el mismo territorio (o None)."""
    if nombre in SIN_ENTIDAD:
        return None
    if nombre in APROX:
        return APROX[nombre]
    if nombre == "Russia":
        if 1917 <= anio <= 1991:
            return "Former USSR"
        return "Russia" if anio >= 1992 else None
    if nombre == "Yugoslavia":
        if 1918 <= anio <= 1991:
            return "Former Yugoslavia"
        return "Serbia" if (anio < 1918 or anio >= 2006) else None
    if nombre == "Vietnam" and anio < 1976:
        return None
    if nombre == "Pakistan" and anio < 1972:
        return None
    nombre = RENOMBRE_SOCIO.get(nombre, nombre)
    return nombre if nombre in entidades else None


def cargar_pib(log):
    """Maddison 2020 en forma ancha (Year x Entity), sin PIB per cápita <= 0."""
    log.info("Maddison: %s | SHA-256 %s", IN_MADDISON.relative_to(ROOT),
             sha256(IN_MADDISON))
    M = pd.read_csv(IN_MADDISON).dropna(subset=["GDP per capita"])
    no_pos = M["GDP per capita"] <= 0
    if no_pos.any():
        log.info("PIB per cápita <= 0 descartado (no admite log): %d filas (%s)",
                 int(no_pos.sum()), ", ".join(sorted(set(M.loc[no_pos, "Entity"]))))
    M = M[~no_pos]
    pib = M.pivot_table(index="Year", columns="Entity",
                        values="GDP per capita", aggfunc="first")
    return M, pib


def cargar_poblacion(M, log):
    """Población MPD2020 (miles), Year x Entity, vía Code -> Entity del CSV."""
    X = pd.read_excel(IN_MPD_XLSX, sheet_name="Full data")
    code2ent = M.drop_duplicates("Code").set_index("Code")["Entity"]
    X["Entity"] = X.countrycode.map(code2ent)
    pobl = X.dropna(subset=["Entity", "pop"]).pivot_table(
        index="year", columns="Entity", values="pop", aggfunc="first")
    log.info("Población MPD2020: %s | SHA-256 %s | %d entidades",
             IN_MPD_XLSX.relative_to(ROOT), sha256(IN_MPD_XLSX), pobl.shape[1])
    return pobl


def leer_cow(entidades, anio_min, log):
    """Exportaciones direccionales válidas (espejo de importaciones) desde
    `anio_min`, con columnas o, s, anio, v, nodo, socio, aprox."""
    digest = sha256(IN_ZIP)
    log.info("COW: %s | SHA-256 %s", IN_ZIP.relative_to(ROOT), digest)
    if digest != SHA256_ZIP:
        log.error("SHA-256 no coincide con el anclado (%s)", SHA256_ZIP)
        sys.exit(1)
    with zipfile.ZipFile(IN_ZIP) as z, z.open(MIEMBRO) as fh:
        d = pd.read_csv(fh, usecols=["year", "importer1", "importer2",
                                     "flow1", "flow2"])
    d = d[d.year >= anio_min]
    exp = pd.concat([
        d.rename(columns={"importer2": "o", "importer1": "s", "flow1": "v"}),
        d.rename(columns={"importer1": "o", "importer2": "s", "flow2": "v"}),
    ], ignore_index=True)[["o", "s", "year", "v"]]
    exp = exp[exp.v >= 0].rename(columns={"year": "anio"})
    exp["nodo"] = [entidad_nodo(n, a) for n, a in zip(exp.o, exp.anio)]
    exp["socio"] = [socio_maddison(n, a, entidades)
                    for n, a in zip(exp.s, exp.anio)]
    exp["aprox"] = exp.s.isin(APROX)
    log.info("Flujos direccionales válidos %d-%d: %d | socio sin entidad "
             "Maddison del mismo territorio: %d filas (%.1f%% del valor)",
             anio_min, int(exp.anio.max()), len(exp),
             int(exp.socio.isna().sum()),
             100 * exp.loc[exp.socio.isna(), "v"].sum() / exp.v.sum())
    return exp


def partial_spearman(y, x, *zs):
    """ρ de Spearman parcial y~x | z1, z2... (rangos residualizados)."""
    ry, rx = stats.rankdata(y), stats.rankdata(x)
    A = np.column_stack([np.ones_like(ry)] + [stats.rankdata(z) for z in zs])
    ey = ry - A @ np.linalg.lstsq(A, ry, rcond=None)[0]
    ex = rx - A @ np.linalg.lstsq(A, rx, rcond=None)[0]
    if np.std(ey) == 0 or np.std(ex) == 0:
        return np.nan
    return float(np.corrcoef(ey, ex)[0, 1])
