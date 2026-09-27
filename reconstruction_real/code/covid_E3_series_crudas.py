"""
Punto 3 del pre-registro 2026-09-27 — series crudas de COVID-19 (E3, E1) y
corrección por autocorrelación serial.

Pre-registro: `reconstruction_real/preregistro/PREREGISTRO_2026-09-27.md`.

Fuente
------
OWID COVID-19, archivo completo `owid-covid-data.csv` (repositorio
owid/covid-19-data), SHA-256 anclado abajo. El archivo (98 MB) no se versiona:
si está en `data/raw_covid/owid-covid-data.csv` el script verifica su SHA y
regenera el subconjunto versionado `data/owid_covid_casos_totales.csv.gz`
(columnas iso_code, continent, location, date, total_cases). Sin el archivo
completo, el script trabaja con el subconjunto y verifica su SHA.

Identificación de la receta de E3 (criterio fijado en el pre-registro)
----------------------------------------------------------------------
Recetas en este orden: variable ∈ {casos acumulados, casos nuevos suavizados a
7 días}; inicio ∈ {primer caso, primer día con >= 10 acumulados, primer día con
>= 100 acumulados}; 60 días; t = 1..60; b = pendiente log-log. Se acepta la
PRIMERA que reproduzca el b publicado dentro de ±0.01 en >= 90% de los países.
(Los casos nuevos suavizados se calculan como media móvil de 7 días de la
diferencia de los acumulados, para no depender de otra columna.)

Corrección (misma que la auditoría v32 aplicó al dominio B)
-----------------------------------------------------------
`code/snt_utils_v32.fit_powerlaw`: Durbin-Watson, ρ = 1 − DW/2, n efectivo de
Bartlett n(1−ρ)/(1+ρ) (estimable si >= 3) y p de Newey-West con rezago
floor(4·(n/100)^(2/9)). Además, las dos cotas de `corregir_corpus` (inferior:
EE inflado y gl recortados; superior: solo gl recortados).

E1 (4 casos): se prueban las construcciones naturales (número de países
alcanzados por fecha, umbrales 1/10/100 casos, inicio al principio de los datos
o en el primer caso de la región). Si ninguna reproduce los valores publicados,
E1 se declara no reproducible, como prevé el pre-registro.

Salidas
-------
    data/owid_covid_casos_totales.csv.gz                   (subconjunto versionado)
    reconstruction_real/data/dominio_E3_series_crudas.csv  (1 fila por país)
    reconstruction_real/logs/covid_E3_series_crudas_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/covid_E3_series_crudas.py
"""

import hashlib
import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "code"))
from snt_utils_v32 import corregir_corpus, fit_powerlaw  # noqa: E402

DATA_TOP = ROOT / "data"
DATA_RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
FULL = DATA_TOP / "raw_covid" / "owid-covid-data.csv"
SUB = DATA_TOP / "owid_covid_casos_totales.csv.gz"
IN_E3 = DATA_RR / "by_domain" / "dominio_E3_real.csv"
IN_E1 = DATA_RR / "by_domain" / "dominio_E1_real.csv"
OUT = DATA_RR / "dominio_E3_series_crudas.csv"
LOG_FILE = LOG_DIR / "covid_E3_series_crudas_log.txt"

SHA_FULL = "8473d0f0fdf962e1ffbd5b85b18726fc96a49bab109e271186c339725a12b10c"
URL_FULL = ("https://raw.githubusercontent.com/owid/covid-19-data/master/"
            "public/data/owid-covid-data.csv")
VENTANA = 60
TOL = 0.01
UMBRAL_ACEPTA = 0.90
RECETAS = [("acumulados", 1), ("acumulados", 10), ("acumulados", 100),
           ("nuevos_suav7", 1), ("nuevos_suav7", 10), ("nuevos_suav7", 100)]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("COVID-E3")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def cargar():
    if FULL.exists():
        dig = sha256(FULL)
        log.info("Archivo completo: %s | SHA-256 %s", FULL.relative_to(ROOT), dig)
        if dig != SHA_FULL:
            log.error("SHA-256 distinto del anclado (%s): la fuente cambió", SHA_FULL)
            sys.exit(1)
        O = pd.read_csv(FULL, usecols=["iso_code", "continent", "location",
                                       "date", "total_cases"])
        O.to_csv(SUB, index=False, compression={"method": "gzip", "mtime": 0})
        log.info("Subconjunto regenerado: %s (%d filas)", SUB.relative_to(ROOT),
                 len(O))
    else:
        log.info("Sin archivo completo (%s); se usa el subconjunto versionado.",
                 URL_FULL)
    log.info("Subconjunto: %s | SHA-256 %s", SUB.relative_to(ROOT), sha256(SUB))
    O = pd.read_csv(SUB, parse_dates=["date"])
    return O


def serie_pais(O, pais):
    g = O[O.location == pais].sort_values("date")
    acum = g.total_cases.ffill().fillna(0).values
    nuevos = pd.Series(np.diff(acum, prepend=0.0)).rolling(7).mean().values
    return acum, nuevos


def b_ventana(y):
    y = np.asarray(y, float)
    t = np.arange(1, len(y) + 1)
    ok = y > 0
    if ok.sum() < 10:
        return np.nan
    return float(np.polyfit(np.log(t[ok]), np.log(y[ok]), 1)[0])


def ventana(acum, nuevos, var, umbral):
    idx = np.where(acum >= umbral)[0]
    if len(idx) == 0 or idx[0] + VENTANA > len(acum):
        return None
    y = acum if var == "acumulados" else nuevos
    return y[idx[0]:idx[0] + VENTANA]


def main():
    log.info("=" * 78)
    log.info("PUNTO 3 (pre-registro 2026-09-27) — SERIES CRUDAS COVID (E3, E1)")
    log.info("=" * 78)
    O = cargar()
    E3 = pd.read_csv(IN_E3)
    E3["pais"] = E3.descripcion.str.replace(" COVID-19 growth phase 2020", "",
                                            regex=False)
    faltan = sorted(set(E3.pais) - set(O.location))
    log.info("E3 publicado: %d países | sin serie en OWID: %s", len(E3),
             faltan or "ninguno")
    series = {p: serie_pais(O, p) for p in E3.pais}

    log.info("-" * 78)
    log.info("IDENTIFICACIÓN DE LA RECETA (acepta la primera con >= %.0f%% dentro "
             "de ±%.2f)", 100 * UMBRAL_ACEPTA, TOL)
    aceptada = None
    for var, umbral in RECETAS:
        bs = np.array([b_ventana(w) if (w := ventana(*series[p], var, umbral))
                       is not None else np.nan for p in E3.pais])
        ok = ~np.isnan(bs)
        coinc = int((np.abs(bs - E3.b.values) <= TOL).sum())
        r = np.corrcoef(bs[ok], E3.b.values[ok])[0, 1] if ok.sum() > 2 else np.nan
        log.info("  %-13s inicio >= %3d | calculables %3d | coinciden %3d/%d "
                 "(%.1f%%) | r = %.4f", var, umbral, int(ok.sum()), coinc, len(E3),
                 100 * coinc / len(E3), r)
        if aceptada is None and coinc >= UMBRAL_ACEPTA * len(E3):
            aceptada = (var, umbral)
    if aceptada is None:
        log.info("Ninguna receta alcanza el criterio: E3 NO reproducible.")
        return
    log.info("RECETA ACEPTADA: %s, inicio en el primer día con >= %d casos "
             "acumulados, %d días", aceptada[0], aceptada[1], VENTANA)

    filas = []
    for _, r in E3.iterrows():
        w = ventana(*series[r.pais], *aceptada)
        f = fit_powerlaw(np.arange(1, len(w) + 1), w)
        filas.append(dict(id=r.id, pais=r.pais, b_publicado=r.b, b=f["b"],
                          coincide=abs(f["b"] - r.b) <= TOL, n=f["n"],
                          r2_log=f["r2_log"], se_b=f["se_b"],
                          p_ols=f["p_exacto"], dw=f["dw"], rho_ar1=f["rho_ar1"],
                          n_eff=f["n_eff"], p_newey_west=f["p_ar1"],
                          nw_lag=f["nw_lag"]))
    R = pd.DataFrame(filas)
    corr, _ = corregir_corpus(R.to_dict("records"))
    C = pd.DataFrame(corr)
    R["estimable"] = C.estimable.values
    R["sig_ar1_cota_inf"] = C.sig_ar1.values
    R["sig_ar1_cota_sup"] = C.sig_ar1_solo_gl.values
    no = R[~R.coincide]
    log.info("Reproducción: %d/%d dentro de ±%.2f | fuera: %s", int(R.coincide.sum()),
             len(R), TOL, "; ".join(f"{p} (pub {bp:+.4f}, crudo {b:+.4f})"
                                    for p, bp, b in zip(no.pais, no.b_publicado,
                                                        no.b)) or "ninguno")

    log.info("-" * 78)
    log.info("CORRECCIÓN POR AUTOCORRELACIÓN (n = %d por serie)", VENTANA)
    log.info("  p OLS < 0.05 (nominal)              : %d/%d", int((R.p_ols < 0.05).sum()),
             len(R))
    log.info("  Durbin-Watson mediana               : %.4f (rango %.4f-%.4f)",
             R.dw.median(), R.dw.min(), R.dw.max())
    log.info("  DW < 1                              : %d/%d", int((R.dw < 1).sum()), len(R))
    log.info("  ρ AR(1) mediana                     : %.4f", R.rho_ar1.median())
    log.info("  n efectivo mediano                  : %.2f (nominal %d)",
             R.n_eff.median(), VENTANA)
    log.info("  estimables (n_eff >= 3)             : %d/%d", int(R.estimable.sum()),
             len(R))
    log.info("  Newey-West p < 0.05                 : %d/%d", int((R.p_newey_west < 0.05)
                                                                   .sum()), len(R))
    est = R[R.estimable]
    log.info("  entre estimables, cota inferior AR(1): %d/%d | cota superior: %d/%d",
             int(est.sig_ar1_cota_inf.sum()), len(est),
             int(est.sig_ar1_cota_sup.sum()), len(est))
    log.info("  b recalculado: media %+.4f, mediana %+.4f (publicado: media %+.4f)",
             R.b.mean(), R.b.median(), R.b_publicado.mean())

    log.info("-" * 78)
    log.info("E1 — construcciones probadas (países alcanzados por fecha)")
    E1 = pd.read_csv(IN_E1)
    Oc = O[~O.iso_code.str.startswith("OWID_")]
    regiones = {"E1_001": (None, 120), "E1_002": (["Asia", "Oceania"], 80),
                "E1_003": (["Europe"], 80),
                "E1_004": (["North America", "South America"], 80)}
    alguna = False
    for umbral in (1, 10, 100):
        for inicio in ("datos", "primer_caso"):
            bs = []
            for cid, (conts, n) in regiones.items():
                x = Oc if conts is None else Oc[Oc.continent.isin(conts)]
                primero = x[x.total_cases >= umbral].groupby("location").date.min()
                t0 = O.date.min() if inicio == "datos" else primero.min()
                dias = pd.date_range(t0, periods=n)
                cnt = np.array([(primero <= d).sum() for d in dias], float)
                bs.append(b_ventana(cnt))
            coinc = int(sum(abs(b - p) <= TOL for b, p in zip(bs, E1.b)))
            alguna |= coinc == len(E1)
            log.info("  umbral %3d, inicio %-11s: b = %s | publicado %s | "
                     "coinciden %d/4", umbral, inicio,
                     ", ".join(f"{b:+.3f}" for b in bs),
                     ", ".join(f"{b:+.3f}" for b in E1.b), coinc)
    log.info("E1: %s", "reproducible" if alguna else
             "NO reproducible con las construcciones naturales (se declara así, "
             "como prevé el pre-registro)")

    for c in ["b", "r2_log", "se_b", "dw", "rho_ar1", "n_eff"]:
        R[c] = R[c].astype(float).round(6)
    R.to_csv(OUT, index=False)
    log.info("-" * 78)
    log.info("CSV -> %s (%d filas) | SHA-256 %s", OUT.relative_to(ROOT), len(R),
             sha256(OUT))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
