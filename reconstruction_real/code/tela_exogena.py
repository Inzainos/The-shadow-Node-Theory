#!/usr/bin/env python3
"""
CAPA EXÓGENA DE LA TELA — SNT v34
==================================

Reconstruye las series reales (t, R) de todos los dominios con fuente
cruda versionada y calcula la capa estadística: medias, medianas, modas
y probabilidades dirección→destino sobre datos REALES (no sombras).

Fuentes versionadas (sin descargas):
  data/maddison_mpd2020.csv                         B: PIB per cápita MPD2020
                                                   (el panel de la
                                                   recalibración auditada
                                                   2026-10-03 — NO el
                                                   extracto owid-maddison)
  data/owid_covid_casos_totales.csv.gz              E3: casos diarios OWID
  reconstruction_real/data/snt_corpus_dominio_G_timeseries.csv   G: 1 caso
  reconstruction_real/data/snt_corpus_aco_timeseries_v29.csv   ACO: 18

Recetas (de los scripts de reconstrucción ya auditados):
  E3:  R = casos del país; variable y umbral identificados como en
       covid_E3_series_crudas.py — la PRIMERA receta que reproduce el b
       publicado ±0.01 en ≥ 90% de los países; ventana de 60 días.
  B:   R = PIB_pc_hub / PIB_pc_nodo, ventana year_min..year_max,
       t = posición 1..n (expand_dominio_B.py).
  ACO: serie tal cual (v29); b verificado contra dominio_ACO_v29.csv.
  G:   serie tal cual (sin b publicado versionado — declarado).

Verificación: el b recalculado (OLS log-log) contra el b publicado
(±0.01). Un caso que no reproduce sale con verificado=False y se
reporta en el log — no se descarta silenciosamente.

Estadística emitida:
  Por dominio : media, mediana, moda (histograma 20 bins), std de
                b, pendiente temprana, log R final y Δ log R.
  Dirección   : Spearman(pendiente temprana, log R final) por dominio.
  Probabilidad: P(régimen b | tercil de dirección temprana) — terciles
                calibrados con los datos (regla 9: nada de umbrales
                inventados), regímenes = bandas declaradas de la SNT.

Honestidad declarada:
  - E3 es un corpus de "fase de crecimiento 2020": selección con sesgo
    hacia dirección positiva (por diseño del dominio, se reporta).
  - G tiene 1 caso: estadística descriptiva sin inferencia.

Salidas:
  data/tela_exogena_series.csv        (id, dominio, t, R, proxy, ...)
  data/tela_exogena_casos.csv         (rasgos por caso)
  data/tela_exogena_estadisticas.csv  (descriptiva por dominio)
  data/tela_exogena_probabilidad.csv  (P(régimen | dirección))
  logs/tela_exogena_log.txt
"""

import os
import logging

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_RR = os.path.join(SCRIPT_DIR, "..", "data")
BY_DOMAIN = os.path.join(DATA_RR, "by_domain")
DATA_TOP = os.path.join(SCRIPT_DIR, "..", "..", "data")
LOG_DIR = os.path.join(SCRIPT_DIR, "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(
            os.path.join(LOG_DIR, "tela_exogena_log.txt"), mode="w"
        ),
    ],
)
log = logging.getLogger("tela_exogena")

N_GRID = 32
TAU_GRID = np.linspace(0.0, 1.0, N_GRID)
VENTANA_E3 = 60
TOL = 0.01
UMBRAL_ACEPTA = 0.90
RECETAS_E3 = [("acumulados", 1), ("acumulados", 10), ("acumulados", 100),
              ("nuevos_suav7", 1), ("nuevos_suav7", 10),
              ("nuevos_suav7", 100)]

PROXY = {
    "E3": "casos COVID-19 del país (receta aceptada)",
    "B": "PIB per cápita hub/nodo (Maddison MPD2020)",
    "ACO": "razón de dominio por caso (serie ACO v29)",
    "G": "ΣC1-alquilnaftalenos/fenantreno (proxy químico Bennu)",
}


def b_ols(t, y):
    """b de la ley de potencia por OLS log-log; NaN si no estimable."""
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)
    ok = (t > 0) & (y > 0)
    if ok.sum() < 5:
        return np.nan
    lt, ly = np.log(t[ok]), np.log(y[ok])
    if lt.std() == 0:
        return np.nan
    return float(np.polyfit(lt, ly, 1)[0])


def ventana_e3(acum, nuevos, var, umbral):
    idx = np.where(acum >= umbral)[0]
    if len(idx) == 0 or idx[0] + VENTANA_E3 > len(acum):
        return None
    y = acum if var == "acumulados" else nuevos
    return y[idx[0]:idx[0] + VENTANA_E3]


def reconstruir_e3():
    """Series E3 desde el subconjunto OWID versionado + receta auditada."""
    O = pd.read_csv(os.path.join(DATA_TOP, "owid_covid_casos_totales.csv.gz"),
                    parse_dates=["date"])
    E3 = pd.read_csv(os.path.join(BY_DOMAIN, "dominio_E3_real.csv"))
    E3["pais"] = E3["descripcion"].str.replace(
        " COVID-19 growth phase 2020", "", regex=False)
    faltan = sorted(set(E3["pais"]) - set(O["location"]))
    if faltan:
        log.warning("E3: %d países sin serie OWID: %s", len(faltan), faltan)
        E3 = E3[E3["pais"].isin(set(O["location"]))]

    series = {}
    for p in E3["pais"]:
        g = O[O["location"] == p].sort_values("date")
        acum = g["total_cases"].ffill().fillna(0.0).to_numpy(dtype=float)
        nuevos = pd.Series(np.diff(acum, prepend=0.0)).rolling(7).mean() \
            .to_numpy(dtype=float)
        series[p] = (acum, nuevos)

    aceptada = None
    for var, umbral in RECETAS_E3:
        bs = np.array([
            b_ols(np.arange(1, VENTANA_E3 + 1), w)
            if (w := ventana_e3(*series[p], var, umbral)) is not None
            else np.nan
            for p in E3["pais"]
        ])
        coinc = int((np.abs(bs - E3["b"].to_numpy()) <= TOL).sum())
        log.info("  receta E3 %-13s umbral %3d → coinciden %d/%d",
                 var, umbral, coinc, len(E3))
        if aceptada is None and coinc >= UMBRAL_ACEPTA * len(E3):
            aceptada = (var, umbral)
    if aceptada is None:
        log.error("E3: ninguna receta alcanza %.0f%% — sin series",
                  100 * UMBRAL_ACEPTA)
        return pd.DataFrame(), None
    log.info("E3 RECETA ACEPTADA: %s desde el primer día con ≥ %d "
             "acumulados, %d días", aceptada[0], aceptada[1], VENTANA_E3)

    filas = []
    for _, r in E3.iterrows():
        w = ventana_e3(*series[r["pais"]], *aceptada)
        if w is None:
            log.warning("E3 %s: sin ventana completa — excluido", r["id"])
            continue
        t = np.arange(1, len(w) + 1)
        ok = w > 0
        if (~ok).any():
            log.info("E3 %s: %d puntos con R≤0 excluidos del log",
                     r["id"], int((~ok).sum()))
        b_ver = b_ols(t, w)
        for ti, ri in zip(t[ok], w[ok]):
            filas.append({
                "id": r["id"], "dominio": "E3", "t": int(ti), "R": float(ri),
                "proxy": PROXY["E3"], "t_unidad": "dias",
                "b_publicado": float(r["b"]), "b_verificado": b_ver,
                "verificado": bool(abs(b_ver - float(r["b"])) <= TOL),
            })
    log.info("E3: %d casos reconstruidos, %d puntos",
             len({f["id"] for f in filas}), len(filas))
    return pd.DataFrame(filas), aceptada


def reconstruir_b():
    """Series B desde el panel Maddison MPD2020 versionado (el mismo de la
    recalibración auditada 2026-10-03) + receta expand_B."""
    mad = pd.read_csv(os.path.join(DATA_TOP, "maddison_mpd2020.csv"))
    B = pd.read_csv(os.path.join(BY_DOMAIN, "dominio_B_real.csv"))
    filas = []
    for _, r in B.iterrows():
        h = mad[(mad["Entity"] == r["hub"]) &
                (mad["Year"] >= r["year_min"]) &
                (mad["Year"] <= r["year_max"])][["Year", "GDP per capita"]] \
            .dropna()
        n_ = mad[(mad["Entity"] == r["nodo"]) &
                 (mad["Year"] >= r["year_min"]) &
                 (mad["Year"] <= r["year_max"])][["Year", "GDP per capita"]] \
            .dropna()
        m = pd.merge(h, n_, on="Year", suffixes=("_hub", "_nodo")) \
            .sort_values("Year")
        if len(m) < 5:
            log.warning("B %s: solapamiento < 5 años — excluido", r["id"])
            continue
        R = m["GDP per capita_hub"].to_numpy(dtype=float) / \
            m["GDP per capita_nodo"].to_numpy(dtype=float)
        t = np.arange(1, len(m) + 1)
        ok = R > 0
        b_ver = b_ols(t[ok], R[ok])
        for ti, ri in zip(t[ok], R[ok]):
            filas.append({
                "id": r["id"], "dominio": "B", "t": int(ti), "R": float(ri),
                "proxy": PROXY["B"], "t_unidad": "años_posicion",
                "b_publicado": float(r["b"]), "b_verificado": b_ver,
                "verificado": bool(abs(b_ver - float(r["b"])) <= TOL),
            })
    log.info("B: %d casos reconstruidos, %d puntos",
             len({f["id"] for f in filas}), len(filas))
    return pd.DataFrame(filas)


def reconstruir_series_directas():
    """ACO (v29) y G: series ya versionadas, b verificado si hay tabla."""
    filas = []
    aco_pub = pd.read_csv(os.path.join(BY_DOMAIN, "dominio_ACO_v29.csv"))
    aco_pub["id_serie"] = aco_pub["id"].str.replace("ACO_", "", regex=False)
    pub = dict(zip(aco_pub["id_serie"], aco_pub["b"].astype(float)))

    for nombre, dominio in [
        ("snt_corpus_aco_timeseries_v29.csv", "ACO"),
        ("snt_corpus_dominio_G_timeseries.csv", "G"),
    ]:
        df = pd.read_csv(os.path.join(DATA_RR, nombre))
        b_pub = pub.get
        for cid, g in df.groupby("id", sort=False):
            g = g.sort_values("t")
            R = g["R"].to_numpy(dtype=float)
            t = g["t"].to_numpy(dtype=float)
            ok = (R > 0) & (t > 0)
            b_ver = b_ols(t[ok], R[ok])
            bp = pub.get(cid) if dominio == "ACO" else None
            for ti, ri in zip(t[ok], R[ok]):
                filas.append({
                    "id": cid, "dominio": dominio, "t": float(ti),
                    "R": float(ri), "proxy": PROXY[dominio],
                    "t_unidad": str(g["t_unidad"].iloc[0]),
                    "b_publicado": bp if bp is not None else np.nan,
                    "b_verificado": b_ver,
                    "verificado": (bool(abs(b_ver - bp) <= TOL)
                                   if bp is not None else ""),
                })
        log.info("%s: %d casos, %d puntos", dominio,
                 df["id"].nunique(), int(ok.sum()) if len(df) else 0)
    return pd.DataFrame(filas)


def rasgos_por_caso(df):
    """Pendiente temprana y destino por caso (retícula de fase común)."""
    casos = []
    for (dom, cid), g in df.groupby(["dominio", "id"], sort=False):
        g = g.sort_values("t")
        R = g["R"].to_numpy(dtype=float)
        t = g["t"].to_numpy(dtype=float)
        ok = R > 0
        if ok.sum() < 5:
            continue
        t_ok = t[ok]
        if t_ok.max() > t_ok.min():
            tau = (t_ok - t_ok.min()) / (t_ok.max() - t_ok.min())
        else:
            tau = np.zeros_like(t_ok)
        lm = np.interp(TAU_GRID, tau, np.log10(R[ok]))
        casos.append({
            "dominio": dom, "id": cid,
            "b_publicado": g["b_publicado"].iloc[0],
            "b_verificado": g["b_verificado"].iloc[0],
            "verificado": g["verificado"].iloc[0],
            "pend_ini": (lm[8] - lm[0]) / 0.25,
            "lm_final": lm[-1],
            "delta_lm": lm[-1] - lm[0],
            "n_puntos": int(ok.sum()),
        })
    return pd.DataFrame(casos)


def moda_hist(x, bins=20):
    x = pd.Series(x).dropna().to_numpy(dtype=float)
    if len(x) < 5:
        return np.nan
    hist, edges = np.histogram(x, bins=bins)
    i = int(hist.argmax())
    return float((edges[i] + edges[i + 1]) / 2)


def capa_estadistica(casos):
    log.info("-" * 78)
    log.info("ESTADÍSTICA EXÓGENA (medias, medianas, modas)")
    filas = []
    for dom, g in casos.groupby("dominio"):
        fila = {"dominio": dom, "n_casos": len(g)}
        for col in ("b_verificado", "pend_ini", "lm_final", "delta_lm"):
            x = g[col]
            fila[f"{col}_media"] = float(x.mean())
            fila[f"{col}_mediana"] = float(x.median())
            fila[f"{col}_moda"] = moda_hist(x)
            fila[f"{col}_std"] = float(x.std())
        filas.append(fila)
        rho, p = spearmanr(g["pend_ini"], g["lm_final"])
        log.info("%s: n=%d | b media %.3f mediana %.3f moda %.3f | "
                 "Spearman(pend_ini→final) = %+.3f (p=%.2e)",
                 dom, len(g), fila["b_verificado_media"],
                 fila["b_verificado_mediana"], fila["b_verificado_moda"],
                 rho, p)
    est = pd.DataFrame(filas)
    ruta = os.path.join(DATA_RR, "tela_exogena_estadisticas.csv")
    est.to_csv(ruta, index=False)
    log.info("Estadística por dominio → %s", ruta)

    casos_validos = casos.dropna(subset=["b_verificado"]).copy()
    q1, q2 = casos_validos["pend_ini"].quantile([1 / 3, 2 / 3])
    casos_validos["direccion"] = pd.cut(
        casos_validos["pend_ini"], [-np.inf, q1, q2, np.inf],
        labels=["tercil_bajo", "tercil_medio", "tercil_alto"])
    casos_validos["regimen"] = pd.cut(
        casos_validos["b_verificado"], [-np.inf, 0.0, 0.5, 1.0, np.inf],
        labels=["b<0 convergencia", "0≤b<0.5 incipiente",
                "0.5≤b<1 gradual", "b≥1 superlineal/ACO"])

    log.info("Terciles de dirección calibrados con datos: Q1/3=%.3f, "
             "Q2/3=%.3f (décadas/fase)", q1, q2)
    ct = pd.crosstab(casos_validos["direccion"], casos_validos["regimen"])
    prob = ct.div(ct.sum(axis=1), axis=0)
    log.info("P(régimen | dirección temprana):")
    for dir_, fila in prob.iterrows():
        log.info("  %-14s | %s", dir_,
                 " | ".join(f"{c}: {v:.3f}" for c, v in fila.items()))
    ruta_p = os.path.join(DATA_RR, "tela_exogena_probabilidad.csv")
    prob.to_csv(ruta_p)
    log.info("Matriz de probabilidad → %s", ruta_p)
    ruta_c = os.path.join(DATA_RR, "tela_exogena_casos.csv")
    casos_validos.to_csv(ruta_c, index=False)
    log.info("Rasgos por caso → %s", ruta_c)
    return est, prob


def main():
    log.info("=" * 78)
    log.info("CAPA EXÓGENA DE LA TELA — SNT v34")
    log.info("=" * 78)

    e3, receta = reconstruir_e3()
    b = reconstruir_b()
    directas = reconstruir_series_directas()
    partes = [x for x in (e3, b, directas) if len(x)]
    if not partes:
        log.error("Sin series reconstruidas — aborta")
        return
    series = pd.concat(partes, ignore_index=True)

    for dom in sorted(series["dominio"].unique()):
        g = series[series["dominio"] == dom]
        ver = g["verificado"]
        ver_ok = ver[ver != ""].astype(bool)
        if ver_ok.any():
            log.info("%s: %d casos, %d puntos | b verificado: %d/%d "
                     "(%.1f%%)", dom, g["id"].nunique(), len(g),
                     int(ver_ok.sum()), len(ver_ok),
                     100 * ver_ok.mean())
        else:
            log.info("%s: %d casos, %d puntos | sin b publicado que "
                     "verificar (G: declarado)", dom, g["id"].nunique(),
                     len(g))

    ruta_s = os.path.join(DATA_RR, "tela_exogena_series.csv")
    series.to_csv(ruta_s, index=False)
    log.info("Series exógenas → %s (%d puntos, %d casos)", ruta_s,
             len(series), series["id"].nunique())

    casos = rasgos_por_caso(series)
    log.info("Casos con rasgos: %d (excluidos por <5 puntos: %d)",
             len(casos), series["id"].nunique() - len(casos))
    capa_estadistica(casos)

    log.info("EJECUCION COMPLETADA — capa exógena")


if __name__ == "__main__":
    main()
