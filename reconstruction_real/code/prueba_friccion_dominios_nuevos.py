"""
Punto 2 del pre-registro 2026-09-27 — fricción con dominios nuevos, sin COVID.

Pre-registro: `reconstruction_real/preregistro/PREREGISTRO_2026-09-27.md`.

Pregunta: ¿la relación negativa entre fricción a priori y b se sostiene a
nivel de DOMINIO cuando se agregan dominios nuevos que no son COVID?

Dominios nuevos (fricción fijada en el pre-registro, antes de ver datos)
------------------------------------------------------------------------
* E4 mpox 2022 — nula (0). OWID monkeypox; receta de E3 identificada en el
  punto 3: casos acumulados, 60 días desde el primer día con >= 100 casos.
* D2 cuotas digitales — baja (1). StatCounter mundial mensual 2009-01..2024-12:
  browser, search engine, OS (todas las plataformas) y social media (todas),
  mobile vendor (móvil, única plataforma de esa categoría). Hub = mayor cuota
  media en los primeros 12 meses con datos; nodos = cuota media >= 1% en esos
  12 meses (sin "Other"/"Unknown"); R = cuota_hub/cuota_nodo, t = mes 1..n,
  >= 24 meses con cuota > 0. Se descartan los meses iniciales sin datos (todas
  las cuotas en 0) y se ordena por fecha.
* A2 ciudades — media (2). WUP 2018 (subconjunto 1950–2018 del punto 4): por
  país, hub = mayor aglomeración en 1950, nodos = las demás; R = pob_hub/pob_nodo.
* B-comercio — alta (3). b de `dominio_B_hub_comercio.csv` (PR #45).
Dominios del corpus: A (media 2), C (alta 3), E2 (alta 3), B (alta 3),
D (baja 1), E1 (nula 0), E3 (nula 0) — mapa de fricción del corpus.

Pruebas
-------
Principal: 7 dominios sin COVID (A, A2, B-comercio, C, D2, E2, E4); Spearman
entre fricción y la MEDIA de b por dominio; p por permutación exacta de las
etiquetas de fricción entre dominios (una cola, ρ < 0).
Secundarias: (a) mediana por dominio; (b) B publicado en lugar de B-comercio;
(c) + E1 y E3; (d) + D; (e) por caso, solo descriptivo.
Decisión: respaldada si ρ < 0 y p < 0.05; contraria si ρ > 0 con p de dos
colas < 0.05; no respaldada en otro caso.

Salidas
-------
    data/owid_mpox_casos_totales.csv.gz, data/statcounter_2009_2024.csv.gz
    reconstruction_real/data/friccion_dominios_nuevos_casos.csv
    reconstruction_real/data/friccion_dominios_nuevos_resumen.csv
    reconstruction_real/logs/prueba_friccion_dominios_nuevos_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/prueba_friccion_dominios_nuevos.py
"""

import hashlib
import itertools
import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_TOP = ROOT / "data"
DATA_RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

MPOX_FULL = DATA_TOP / "raw_covid" / "owid-monkeypox-data.csv"
MPOX_SUB = DATA_TOP / "owid_mpox_casos_totales.csv.gz"
SC_DIR = DATA_TOP / "raw_statcounter"
SC_SUB = DATA_TOP / "statcounter_2009_2024.csv.gz"
WUP_SUB = DATA_TOP / "wup2018_aglomeraciones_1950_2018.csv.gz"
IN_BCOM = DATA_RR / "dominio_B_hub_comercio.csv"
IN_CORPUS = DATA_RR / "snt_corpus_REAL_v5.csv"
OUT_CASOS = DATA_RR / "friccion_dominios_nuevos_casos.csv"
OUT_RES = DATA_RR / "friccion_dominios_nuevos_resumen.csv"
LOG_FILE = LOG_DIR / "prueba_friccion_dominios_nuevos_log.txt"

SHA = {
    "owid-monkeypox-data.csv":
        "2764761fd455f9fb295101129b10e37cf1f4e7acf1ae3c779b6f6d2b25b2c927",
    "browser.csv": "4811c5353a8bb06d25398bb9fd9d5c231e5299fa91dd18706d0613dd09dee9fe",
    "os_combined.csv":
        "eb3a5703b5213a36b2559c1057168866d3c1611757dd3ea14d2f46aa03430dfa",
    "search_engine.csv":
        "158017b6e1e53c798fac7c23372ea12f2b07f448ac76deb339fe9b07e80f3f6d",
    "social_media.csv":
        "1b45289f61eb1f030a5066cd2182cfbe798b48322847b08dc93253c705544c64",
    "vendor.csv": "d8983f44751d506dfd4da916cb9392470645f25009a24582b3225bc6b4904af5",
}
SC_CATS = ["browser", "search_engine", "os_combined", "social_media", "vendor"]
FRICCION = {"A": 2, "A2": 2, "B": 3, "B-comercio": 3, "C": 3, "D": 1, "D2": 1,
            "E1": 0, "E2": 3, "E3": 0, "E4": 0}
VENTANA_E = 60
UMBRAL_E = 100

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("FRICCION-NUEVOS")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def verificar(path):
    dig = sha256(path)
    esperado = SHA[path.name]
    log.info("Fuente %s | SHA-256 %s", path.relative_to(ROOT), dig)
    if dig != esperado:
        log.error("SHA-256 distinto del anclado (%s)", esperado)
        sys.exit(1)


def b_loglog(y):
    """Pendiente log-log con t = 1..n sobre las observaciones positivas."""
    y = np.asarray(y, float)
    y = y[(y > 0) & np.isfinite(y)]
    n = len(y)
    if n < 3:
        return np.nan, n
    lt = np.log(np.arange(1, n + 1))
    ly = np.log(y)
    ltc = lt - lt.mean()
    return float(np.sum(ltc * (ly - ly.mean())) / np.sum(ltc ** 2)), n


# ---------------------------------------------------------------- dominios
def dominio_E4():
    if MPOX_FULL.exists():
        verificar(MPOX_FULL)
        M = pd.read_csv(MPOX_FULL, usecols=["location", "iso_code", "date",
                                            "total_cases"])
        M.to_csv(MPOX_SUB, index=False, compression={"method": "gzip", "mtime": 0})
    log.info("mpox subconjunto: %s | SHA-256 %s", MPOX_SUB.relative_to(ROOT),
             sha256(MPOX_SUB))
    M = pd.read_csv(MPOX_SUB, parse_dates=["date"])
    M = M[~M.iso_code.astype(str).str.startswith("OWID_")]
    filas = []
    for pais, g in M.groupby("location"):
        g = g.sort_values("date")
        ac = g.total_cases.ffill().fillna(0).values
        idx = np.where(ac >= UMBRAL_E)[0]
        if len(idx) == 0 or idx[0] + VENTANA_E > len(ac):
            continue
        b, n = b_loglog(ac[idx[0]:idx[0] + VENTANA_E])
        filas.append(dict(dominio="E4", caso=f"{pais} mpox 2022", b=b, n=n))
    log.info("E4 mpox: %d países con >= %d casos y %d días de ventana",
             len(filas), UMBRAL_E, VENTANA_E)
    return filas


def dominio_D2():
    tablas = []
    for c in SC_CATS:
        p = SC_DIR / f"{c}.csv"
        if p.exists():
            verificar(p)
            t = pd.read_csv(p)
            t.insert(0, "categoria", c)
            tablas.append(t.melt(id_vars=["categoria", "Date"], var_name="entidad",
                                 value_name="cuota"))
    if tablas:
        pd.concat(tablas).to_csv(SC_SUB, index=False,
                                 compression={"method": "gzip", "mtime": 0})
    log.info("StatCounter subconjunto: %s | SHA-256 %s", SC_SUB.relative_to(ROOT),
             sha256(SC_SUB))
    S = pd.read_csv(SC_SUB)
    filas = []
    for cat, g in S.groupby("categoria"):
        W = g.pivot_table(index="Date", columns="entidad", values="cuota",
                          aggfunc="first").sort_index()
        W = W[W.sum(axis=1) > 0]
        W = W.drop(columns=[c for c in W.columns
                            if c.strip().lower() in ("other", "unknown")])
        ini = W.iloc[:12].mean()
        hub = ini.idxmax()
        nodos = [e for e, v in ini.items() if e != hub and v >= 1.0]
        log.info("D2 %-13s %s..%s | hub %s (%.1f%%) | nodos %s", cat, W.index[0],
                 W.index[-1], hub, ini[hub], ", ".join(nodos))
        for e in nodos:
            ok = (W[hub] > 0) & (W[e] > 0)
            if ok.sum() < 24:
                log.info("   %s: %d meses con cuota > 0 (< 24), excluido", e,
                         int(ok.sum()))
                continue
            b, n = b_loglog((W[hub] / W[e])[ok].values)
            filas.append(dict(dominio="D2", caso=f"{cat}: {hub}/{e}", b=b, n=n))
    log.info("D2 cuotas digitales: %d pares", len(filas))
    return filas


def dominio_A2():
    log.info("WUP subconjunto: %s | SHA-256 %s", WUP_SUB.relative_to(ROOT),
             sha256(WUP_SUB))
    L = pd.read_csv(WUP_SUB)
    filas = []
    for pais, g in L.groupby("pais"):
        W = g.pivot_table(index="anio", columns="ciudad", values="pob_miles",
                          aggfunc="first").sort_index()
        if W.shape[1] < 2:
            continue
        hub = W.loc[1950].idxmax()
        for c in W.columns:
            if c == hub:
                continue
            b, n = b_loglog((W[hub] / W[c]).values)
            filas.append(dict(dominio="A2", caso=f"{pais}: {hub}/{c}", b=b, n=n))
    log.info("A2 ciudades: %d pares en %d países", len(filas),
             len({f['caso'].split(':')[0] for f in filas}))
    return filas


def dominio_Bcom():
    X = pd.read_csv(IN_BCOM)
    X = X[X.estado == "ok"]
    log.info("B-comercio: %d pares (SHA-256 %s)", len(X), sha256(IN_BCOM))
    return [dict(dominio="B-comercio", caso=f"{h}/{n}", b=b, n=k)
            for h, n, b, k in zip(X.hub, X.nodo, X.b, X.n)]


def corpus():
    C = pd.read_csv(IN_CORPUS)
    C = C[C.dominio.isin(["A", "B", "C", "D", "E1", "E2", "E3"])]
    return [dict(dominio=d, caso=i, b=b, n=n)
            for d, i, b, n in zip(C.dominio, C.id, C.b, C.n)]


# ---------------------------------------------------------------- pruebas
def prueba_dominios(T, dominios, estadistico, etiqueta):
    sub = T[T.dominio.isin(dominios)]
    agg = sub.groupby("dominio")["b"].agg(estadistico)
    fr = np.array([FRICCION[d] for d in agg.index], float)
    bm = agg.values
    rho = stats.spearmanr(fr, bm)[0]
    perms = np.array([stats.spearmanr(np.array(p), bm)[0]
                      for p in itertools.permutations(fr)])
    p1 = float(np.mean(perms <= rho + 1e-12))
    p2 = float(np.mean(np.abs(perms) >= abs(rho) - 1e-12))
    log.info("[%s] %d dominios | ρ(fricción, %s de b) = %+.3f | permutación "
             "exacta (%d): p 1 cola = %.4f, p 2 colas = %.4f", etiqueta,
             len(agg), estadistico, rho, len(perms), p1, p2)
    for d, v in agg.items():
        log.info("    %-11s fricción %d | %s b = %+.4f | n = %d", d, FRICCION[d],
                 estadistico, v, int((sub.dominio == d).sum()))
    return dict(prueba=etiqueta, estadistico=estadistico, dominios=len(agg),
                rho=rho, p_una_cola=p1, p_dos_colas=p2)


def decision(r):
    if r["rho"] < 0 and r["p_una_cola"] < 0.05:
        return "RESPALDADA"
    if r["rho"] > 0 and r["p_dos_colas"] < 0.05:
        return "CONTRARIA"
    return "NO RESPALDADA"


def main():
    log.info("=" * 78)
    log.info("PUNTO 2 (pre-registro 2026-09-27) — FRICCIÓN CON DOMINIOS NUEVOS")
    log.info("=" * 78)
    filas = dominio_E4() + dominio_D2() + dominio_A2() + dominio_Bcom() + corpus()
    T = pd.DataFrame(filas).dropna(subset=["b"])
    T["friccion"] = T.dominio.map(FRICCION)
    log.info("-" * 78)
    principal = ["A", "A2", "B-comercio", "C", "D2", "E2", "E4"]
    res = [prueba_dominios(T, principal, "mean", "PRINCIPAL sin COVID")]
    res.append(prueba_dominios(T, principal, "median", "(a) mediana"))
    res.append(prueba_dominios(T, ["A", "A2", "B", "C", "D2", "E2", "E4"], "mean",
                               "(b) con B publicado"))
    res.append(prueba_dominios(T, principal + ["E1", "E3"], "mean",
                               "(c) + E1 y E3 (con COVID)"))
    res.append(prueba_dominios(T, principal + ["D"], "mean", "(d) + D"))
    sub = T[T.dominio.isin(principal)]
    r, p = stats.spearmanr(sub.friccion, sub.b)
    log.info("[(e) por caso, descriptivo] ρ = %+.3f (p nominal %.3g, n = %d; "
             "no inferencial)", r, p, len(sub))
    log.info("-" * 78)
    log.info("DECISIÓN PRE-REGISTRADA (principal): %s", decision(res[0]))
    for x in res[1:]:
        log.info("  %-28s %s", x["prueba"], decision(x))

    T["b"] = T.b.round(6)
    T.to_csv(OUT_CASOS, index=False)
    R = pd.DataFrame(res)
    R["decision"] = [decision(x) for x in res]
    R.round(6).to_csv(OUT_RES, index=False)
    log.info("CSV -> %s (%d filas) | SHA-256 %s", OUT_CASOS.relative_to(ROOT),
             len(T), sha256(OUT_CASOS))
    log.info("CSV -> %s | SHA-256 %s", OUT_RES.relative_to(ROOT), sha256(OUT_RES))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
