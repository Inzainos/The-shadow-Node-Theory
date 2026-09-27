"""
Punto 4 del pre-registro 2026-09-27 — corpus de disparadores codificados a ciegas.

Pre-registro: `reconstruction_real/preregistro/PREREGISTRO_2026-09-27.md`.

Pregunta: ¿un disparador abrupto por decreto (traslado de capital, Zona
Económica Especial) produce una satelización más rápida que la dinámica basal
de ciudades con la misma razón inicial de tamaño?

Datos
-----
ONU, World Urbanization Prospects 2018, archivo anual de aglomeraciones con
>= 300 mil habitantes en 2018 (`WUP2018-F22-Cities_Over_300K_Annual.xls`,
dentro de `WUP2018-Excel-files.zip`, SHA-256 anclado abajo). Se usan solo los
años 1950–2018 (estimaciones; sin proyecciones). El zip (5 MB) no se versiona;
el script extrae y versiona el subconjunto `data/wup2018_aglomeraciones_1950_2018.csv.gz`.

Casos (codificados en el pre-registro antes de ver las series)
--------------------------------------------------------------
Traslados de capital y Zonas Económicas Especiales de 1980; año efectivo y año
de decisión (sensibilidad). Entran los que tienen ambas ciudades en el archivo
y >= 15 observaciones desde el año efectivo.

Diseño
------
R = pob_retador / pob_incumbente, t = 1..n desde el año efectivo hasta 2018,
b por MCO log-log (igual que el corpus). Controles: otras aglomeraciones del
mismo país (sin retadores codificados ni el incumbente), R = pob_control /
pob_incumbente, misma ventana, |Δg| <= 0.25 con g = media de log R en las 5
primeras observaciones, K = 5 más cercanos; si hay menos de 3 en el país se
completa hasta K con aglomeraciones de cualquier otro país, con R contra la
mayor aglomeración de su país en el año efectivo. d = b_caso - media(b_ctrl).

Pruebas: principal Wilcoxon de una cola (d > 0); secundarias: percentil de
b_caso en todo su grupo de candidatos dentro del caliper (prueba de signo
contra 0.5), solo capitales, año de decisión, razón b̄_casos / b̄_controles.
Decisión: respaldada si p < 0.05 y mediana de d > 0; contraria si p de dos
colas < 0.05 con d < 0; no respaldada en otro caso.

Salidas
-------
    data/wup2018_aglomeraciones_1950_2018.csv.gz
    reconstruction_real/data/disparadores_ciudades_casos.csv
    reconstruction_real/logs/prueba_disparadores_ciudades_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/prueba_disparadores_ciudades.py
"""

import hashlib
import logging
import sys
import unicodedata
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_TOP = ROOT / "data"
DATA_RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
ZIP = DATA_TOP / "raw_wup" / "WUP2018-Excel-files.zip"
MIEMBRO = "WUP2018-F22-Cities_Over_300K_Annual.xls"
SUB = DATA_TOP / "wup2018_aglomeraciones_1950_2018.csv.gz"
OUT = DATA_RR / "disparadores_ciudades_casos.csv"
LOG_FILE = LOG_DIR / "prueba_disparadores_ciudades_log.txt"
SHA_ZIP = "80eb71bbabb46cb2e1599b51b16133bf28b0a99a541d72de20a1248ec6170a75"
URL_ZIP = ("https://population.un.org/wup/assets/Download/Archive/"
           "WUP2018-Excel-files.zip")
ANIO_FIN = 2018
N_MIN = 15
N_BRECHA = 5
CALIPER = 0.25
K = 5
MIN_PAIS = 3

# Codificación del pre-registro (país WUP, retador, incumbente, año efectivo,
# año de decisión, clase).
CASOS = [
    ("Brazil", "Brasília", "Rio de Janeiro", 1960, 1956, "capital"),
    ("Pakistan", "Islamabad", "Karachi", 1967, 1959, "capital"),
    ("Nigeria", "Abuja", "Lagos", 1991, 1976, "capital"),
    ("Kazakhstan", "Astana", "Almaty", 1997, 1994, "capital"),
    ("United Republic of Tanzania", "Dodoma", "Dar es Salaam", 1996, 1973,
     "capital"),
    ("Côte d'Ivoire", "Yamoussoukro", "Abidjan", 1983, 1983, "capital"),
    ("Germany", "Berlin", "Bonn", 1999, 1991, "capital"),
    ("Malawi", "Lilongwe", "Zomba", 1975, 1965, "capital"),
    ("China", "Shenzhen", "Guangzhou, Guangdong", 1980, 1979, "zee"),
    ("China", "Zhuhai", "Guangzhou, Guangdong", 1980, 1979, "zee"),
    ("China", "Shantou", "Guangzhou, Guangdong", 1980, 1979, "zee"),
    ("China", "Xiamen", "Fuzhou, Fujian", 1980, 1979, "zee"),
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("DISPARADORES")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def norm(s):
    return unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore") \
        .decode().lower().strip()


def cargar():
    if ZIP.exists():
        dig = sha256(ZIP)
        log.info("WUP 2018: %s | SHA-256 %s", ZIP.relative_to(ROOT), dig)
        if dig != SHA_ZIP:
            log.error("SHA-256 distinto del anclado (%s)", SHA_ZIP)
            sys.exit(1)
        with zipfile.ZipFile(ZIP) as z, z.open(MIEMBRO) as fh:
            x = pd.read_excel(fh, header=16)
        anios = [c for c in x.columns if isinstance(c, (int, float))
                 and 1950 <= c <= ANIO_FIN]
        L = x.melt(id_vars=["Country or area", "City Code", "Urban Agglomeration"],
                   value_vars=anios, var_name="anio", value_name="pob_miles")
        L = L.rename(columns={"Country or area": "pais", "City Code": "codigo",
                              "Urban Agglomeration": "ciudad"})
        L["anio"] = L.anio.astype(int)
        L.to_csv(SUB, index=False, compression={"method": "gzip", "mtime": 0})
        log.info("Subconjunto 1950-%d regenerado: %s (%d filas)", ANIO_FIN,
                 SUB.relative_to(ROOT), len(L))
    else:
        log.info("Sin el zip (%s); se usa el subconjunto versionado.", URL_ZIP)
    log.info("Subconjunto: %s | SHA-256 %s", SUB.relative_to(ROOT), sha256(SUB))
    L = pd.read_csv(SUB)
    return L


def ajuste(num, den):
    """b y g de log(num/den) contra log t, t = 1..n."""
    ok = (num > 0) & (den > 0) & ~np.isnan(num) & ~np.isnan(den)
    n = int(ok.sum())
    if n < N_MIN:
        return None
    lR = np.log(num[ok] / den[ok])
    lt = np.log(np.arange(1, n + 1))
    ltc = lt - lt.mean()
    b = float(np.sum(ltc * (lR - lR.mean())) / np.sum(ltc ** 2))
    return b, float(np.mean(lR[:N_BRECHA])), n


def evaluar(W, casos_ok, usar_decision=False):
    """Calcula b de cada caso, sus controles y d."""
    retadores = {(c[0], c[1]) for c in CASOS}
    filas = []
    for pais, ret, inc, y_ef, y_dec, clase in casos_ok:
        y0 = y_dec if usar_decision else y_ef
        anios = np.arange(y0, ANIO_FIN + 1)
        P = W.loc[anios]
        f = ajuste(P[(pais, ret)].values, P[(pais, inc)].values)
        if f is None:
            continue
        b, g, n = f
        cand = []
        for (p, c) in W.columns:
            if p != pais or c in (ret, inc) or (p, c) in retadores:
                continue
            fc = ajuste(P[(p, c)].values, P[(pais, inc)].values)
            if fc and abs(fc[1] - g) <= CALIPER:
                cand.append((abs(fc[1] - g), p, c, fc[0]))
        cand.sort()
        pool = list(cand)
        ctl = cand[:K]
        externos = 0
        if len(ctl) < MIN_PAIS:
            ext = []
            for p in {p for (p, _) in W.columns if p != pais}:
                cols = [c for (pp, c) in W.columns if pp == p]
                pob0 = W.loc[y0, [(p, c) for c in cols]]
                inc_p = pob0.idxmax()[1] if pob0.notna().any() else None
                if inc_p is None:
                    continue
                for c in cols:
                    if c == inc_p or (p, c) in retadores:
                        continue
                    fc = ajuste(P[(p, c)].values, P[(p, inc_p)].values)
                    if fc and abs(fc[1] - g) <= CALIPER:
                        ext.append((abs(fc[1] - g), p, c, fc[0]))
            ext.sort()
            pool += ext
            falta = K - len(ctl)
            externos = min(falta, len(ext))
            ctl = ctl + ext[:falta]
        bc = [c[3] for c in ctl]
        bpool = np.array([c[3] for c in pool])
        pct = float((bpool < b).mean()) if len(bpool) else np.nan
        filas.append(dict(
            pais=pais, retador=ret, incumbente=inc, clase=clase, anio=y0,
            base_anio="decisión" if usar_decision else "efectivo",
            n=n, g=g, b=b, n_controles=len(ctl), controles_externos=externos,
            controles="; ".join(f"{c[2]} ({c[1]})" for c in ctl),
            b_controles=float(np.mean(bc)) if bc else np.nan,
            d=b - float(np.mean(bc)) if bc else np.nan,
            n_pool=len(bpool), percentil_en_pool=pct))
    return pd.DataFrame(filas)


def pruebas(R, etiqueta):
    x = R.dropna(subset=["d"])
    out = dict(n=len(x))
    if len(x) == 0:
        log.info("[%s] sin casos con controles", etiqueta)
        return out
    out.update(d_mediana=float(x.d.median()), d_pos=int((x.d > 0).sum()))
    if len(x) >= 2:
        out["p1"] = float(stats.wilcoxon(x.d, alternative="greater").pvalue)
        out["p2"] = float(stats.wilcoxon(x.d).pvalue)
    pc = x.percentil_en_pool.dropna()
    sig = stats.binomtest(int((pc > 0.5).sum()), len(pc), 0.5,
                          alternative="greater").pvalue if len(pc) else np.nan
    bm, cm = x.b.mean(), x.b_controles.mean()
    log.info("[%s] casos %d | d mediana %+.4f, d>0 en %d/%d | Wilcoxon 1 cola "
             "p = %s (2 colas p = %s) | percentil medio %.2f, >0.5 en %d/%d, "
             "signo p = %.4g | b̄ casos %+.4f, b̄ controles %+.4f, razón %s",
             etiqueta, len(x), out["d_mediana"], out["d_pos"], len(x),
             f"{out['p1']:.4g}" if "p1" in out else "-",
             f"{out['p2']:.4g}" if "p2" in out else "-", pc.mean(),
             int((pc > 0.5).sum()), len(pc), sig, bm, cm,
             f"{bm / cm:.2f}" if cm else "indefinida")
    return out


def decision(o):
    if "p1" not in o:
        return "sin datos suficientes"
    if o["p1"] < 0.05 and o["d_mediana"] > 0:
        return "RESPALDADA"
    if o["p2"] < 0.05 and o["d_mediana"] < 0:
        return "CONTRARIA"
    return "NO RESPALDADA"


def main():
    log.info("=" * 78)
    log.info("PUNTO 4 (pre-registro 2026-09-27) — DISPARADORES CODIFICADOS A CIEGAS")
    log.info("=" * 78)
    L = cargar()
    W = L.pivot_table(index="anio", columns=["pais", "ciudad"],
                      values="pob_miles", aggfunc="first")
    log.info("Aglomeraciones: %d en %d países, años %d-%d", W.shape[1],
             len({p for p, _ in W.columns}), W.index.min(), W.index.max())

    casos_ok = []
    for caso in CASOS:
        pais, ret, inc, y_ef = caso[:4]
        tiene = [(pais, c) in W.columns for c in (ret, inc)]
        n_obs = ANIO_FIN - y_ef + 1
        if all(tiene) and n_obs >= N_MIN:
            casos_ok.append(caso)
            log.info("  INCLUIDO  %-28s %s / %s (%d, %s)", pais, ret, inc, y_ef,
                     caso[5])
        else:
            falta = [c for c, t in zip((ret, inc), tiene) if not t]
            log.info("  EXCLUIDO  %-28s %s / %s — no está en el archivo: %s",
                     pais, ret, inc, ", ".join(falta) or f"n = {n_obs} < {N_MIN}")

    log.info("-" * 78)
    R = evaluar(W, casos_ok)
    for _, r in R.iterrows():
        log.info("  %-14s/%-22s %d | b = %+.4f | g = %+.3f | controles %d "
                 "(externos %d): b̄ = %+.4f | d = %+.4f | percentil %.2f (pool %d)",
                 r.retador, r.incumbente, r.anio, r.b, r.g, r.n_controles,
                 r.controles_externos, r.b_controles, r.d, r.percentil_en_pool,
                 r.n_pool)
    log.info("-" * 78)
    princ = pruebas(R, "todos, año efectivo")
    pruebas(R[R.clase == "capital"], "solo capitales")
    pruebas(R[R.clase == "zee"], "solo ZEE (descriptivo)")
    Rd = evaluar(W, casos_ok, usar_decision=True)
    dec = pruebas(Rd, "todos, año de decisión")
    log.info("-" * 78)
    log.info("DECISIÓN PRE-REGISTRADA (año efectivo): %s", decision(princ))
    log.info("  sensibilidad año de decisión: %s", decision(dec))

    T = pd.concat([R, Rd], ignore_index=True)
    for c in ["g", "b", "b_controles", "d", "percentil_en_pool"]:
        T[c] = T[c].astype(float).round(6)
    T.to_csv(OUT, index=False)
    log.info("CSV -> %s (%d filas) | SHA-256 %s", OUT.relative_to(ROOT), len(T),
             sha256(OUT))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
