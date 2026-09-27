"""
Construye la matriz de comercio bilateral que necesita el Bloque 2 de la
prueba discriminante del dominio B (H-ACOPLAMIENTO: b vs participación del
comercio nodo -> hub).

Fuente primaria: Correlates of War (COW) Trade Data Set v4.0 (Barbieri &
Keshk), comercio diádico 1870–2014 en millones de USD corrientes, archivo
`data/COW_Trade_4.0.zip` (SHA-256 anclado en `data/FUENTES.md`).

Definiciones del codebook (verificadas):
    flow1 = importaciones del país A (importer1) desde el país B (importer2)
    flow2 = importaciones del país B desde el país A
    -9    = dato faltante
Por espejo: exportaciones B -> A = flow1; exportaciones A -> B = flow2.

Reglas de entidad (no se sustituyen Estados): COW agrupa bajo un mismo código
entidades territorialmente distintas de las series de Maddison 2020 (fronteras
actuales). Esos años NO se asignan al país del corpus, pero sí cuentan en los
totales de exportación de sus socios (se re-etiquetan):
    * "United States of America" -> "United States" (mismo Estado).
    * "Czech Republic" (1993+) -> "Czechia"; "Czechoslovakia" no se mapea.
    * "Yugoslavia" (COW 345) -> "Serbia" solo en años < 1918 y >= 2006.
    * "Russia" (COW 365) 1917–1991 = URSS -> re-etiquetado, no es "Russia".
    * "Vietnam" (COW 816) < 1976 = Vietnam del Norte -> re-etiquetado.
    * "Pakistan" (COW 770) < 1972 incluye Pakistán Oriental -> re-etiquetado.

Salida compacta (lo que consume `bloque2_acoplamiento`): columnas
`origen, destino, anio, valor`, con
    * las exportaciones nodo -> hub de cada par del dominio B, dentro de la
      ventana [year_min, year_max] del par (así la "participación inicial"
      corresponde al inicio real de la serie);
    * una fila por (origen, año) con destino "RESTO_DEL_MUNDO" = exportaciones
      totales del origen menos las filas anteriores, de modo que la suma por
      (origen, año) es exactamente el total de exportaciones del origen.

Salidas:
    data/comercio_bilateral.csv
    reconstruction_real/logs/build_comercio_bilateral_cow_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/build_comercio_bilateral_cow.py
"""

import hashlib
import logging
import sys
import zipfile
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_TOP = ROOT / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

IN_ZIP = DATA_TOP / "COW_Trade_4.0.zip"
MIEMBRO = "COW_Trade_4.0/Dyadic_COW_4.0.csv"
IN_B = ROOT / "reconstruction_real" / "data" / "by_domain" / "dominio_B_real.csv"
OUT_CSV = DATA_TOP / "comercio_bilateral.csv"
LOG_FILE = LOG_DIR / "build_comercio_bilateral_cow_log.txt"

SHA256_ZIP = "c44c4b5ce62e68865368482c428306df4624d3a39edec29adc1aa2c0928f7cc7"
ANIO_MIN = 1900  # ninguna serie del dominio B empieza antes
RESTO = "RESTO_DEL_MUNDO"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("COMERCIO-COW")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def entidad(nombre, anio):
    """Nombre COW -> nombre del corpus, o etiqueta de entidad distinta."""
    if nombre == "United States of America":
        return "United States"
    if nombre == "Czech Republic":
        return "Czechia"
    if nombre == "Yugoslavia":
        return "Serbia" if (anio < 1918 or anio >= 2006) else "Yugoslavia (COW 345)"
    if nombre == "Russia" and 1917 <= anio <= 1991:
        return "USSR (COW 365)"
    if nombre == "Vietnam" and anio < 1976:
        return "North Vietnam (COW 816)"
    if nombre == "Pakistan" and anio < 1972:
        return "Pakistan incl. East Pakistan (COW 770)"
    return nombre


def main():
    digest = sha256(IN_ZIP)
    log.info("Fuente: %s | SHA-256 %s", IN_ZIP.relative_to(ROOT), digest)
    if digest != SHA256_ZIP:
        log.error("SHA-256 no coincide con el anclado (%s)", SHA256_ZIP)
        sys.exit(1)

    with zipfile.ZipFile(IN_ZIP) as z, z.open(MIEMBRO) as fh:
        d = pd.read_csv(fh, usecols=["year", "importer1", "importer2",
                                     "flow1", "flow2"])
    log.info("Diádico COW: %d filas, años %d-%d", len(d),
             int(d.year.min()), int(d.year.max()))
    d = d[d.year >= ANIO_MIN]

    # Exportaciones direccionales por espejo de importaciones
    exp = pd.concat([
        d.rename(columns={"importer2": "origen", "importer1": "destino",
                          "flow1": "valor"})[["origen", "destino", "year",
                                              "valor"]],
        d.rename(columns={"importer1": "origen", "importer2": "destino",
                          "flow2": "valor"})[["origen", "destino", "year",
                                              "valor"]],
    ], ignore_index=True).rename(columns={"year": "anio"})
    faltantes = int((exp.valor < 0).sum())
    exp = exp[exp.valor >= 0]
    log.info("Flujos direccionales %d-%d: %d válidos | %d faltantes (-9) "
             "descartados (faltante, no cero) | %d ceros reales",
             ANIO_MIN, int(exp.anio.max()), len(exp), faltantes,
             int((exp.valor == 0).sum()))

    exp["origen"] = [entidad(n, a) for n, a in zip(exp.origen, exp.anio)]
    exp["destino"] = [entidad(n, a) for n, a in zip(exp.destino, exp.anio)]
    for etiqueta in ("Yugoslavia (COW 345)", "USSR (COW 365)",
                     "North Vietnam (COW 816)",
                     "Pakistan incl. East Pakistan (COW 770)"):
        anios = exp.loc[exp.origen == etiqueta, "anio"]
        if len(anios):
            log.info("Re-etiquetado (no se asigna al corpus): %-40s %d-%d",
                     etiqueta, int(anios.min()), int(anios.max()))

    total = exp.groupby(["origen", "anio"])["valor"].sum().rename("total")

    B = pd.read_csv(IN_B)
    faltan = sorted((set(B.hub) | set(B.nodo)) - set(exp.origen))
    log.info("Países del dominio B sin ninguna exportación en COW: %s",
             faltan or "ninguno")

    filas = []
    for _, r in B.iterrows():
        m = exp[(exp.origen == r["nodo"]) & (exp.destino == r["hub"])
                & (exp.anio >= r["year_min"]) & (exp.anio <= r["year_max"])]
        filas.append(m)
    pares = pd.concat(filas, ignore_index=True).drop_duplicates(
        ["origen", "destino", "anio"])
    log.info("Pares del dominio B con algún año de comercio nodo->hub: %d de %d",
             pares.groupby(["origen", "destino"]).ngroups, len(B))

    # Fila RESTO_DEL_MUNDO: total del origen menos lo ya listado
    listado = pares.groupby(["origen", "anio"])["valor"].sum().rename("listado")
    resto = total.to_frame().join(listado, how="left").fillna({"listado": 0.0})
    origenes = set(B.nodo)
    resto = resto.reset_index()
    resto = resto[resto.origen.isin(origenes)]
    resto["valor"] = resto["total"] - resto["listado"]
    resto["destino"] = RESTO
    out = pd.concat([pares[["origen", "destino", "anio", "valor"]],
                     resto[["origen", "destino", "anio", "valor"]]],
                    ignore_index=True).sort_values(["origen", "anio", "destino"])

    chk = out.groupby(["origen", "anio"])["valor"].sum()
    ref = total.loc[chk.index]
    log.info("Control: suma por (origen, año) = total de exportaciones "
             "(máx. |dif| = %.3g)", float((chk - ref).abs().max()))

    out.to_csv(OUT_CSV, index=False, float_format="%.6g")
    log.info("CSV -> %s | %d filas | SHA-256 %s", OUT_CSV.relative_to(ROOT),
             len(out), sha256(OUT_CSV))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
