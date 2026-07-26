#!/usr/bin/env python3
"""
Prueba discriminante del dominio B — acoplamiento vs convergencia
=================================================================
Fractal Core Research | 2026-07-25

PREGUNTA
--------
El exponente b del dominio B, ¿mide acoplamiento hub-satelite (SNT) o mide
convergencia/divergencia de PIB per capita (beta-convergencia, Barro &
Sala-i-Martin)? Las dos hipotesis hacen predicciones separables.

  H-ACOPLAMIENTO : b crece con la intensidad del vinculo estructural
                   correlato -> participacion de comercio bilateral
  H-CONVERGENCIA : b crece con la brecha inicial de PIB per capita
                   correlato -> log(pib_hub / pib_nodo) en el anio inicial

MOTIVO
------
En la construccion actual el "hub" se asigna por mayor PIB per capita dentro
de un bucket geografico. 77 de 91 paises aparecen como hub Y como satelite
(Mexico: hub en 1 par, satelite en 9). El rol de hub es una propiedad del PAR,
no del pais. Eso es incompatible con una lectura estructural de red.

Si gana H-CONVERGENCIA, el dominio B (446 de 721 casos = 62% del corpus) no es
evidencia de SNT.

ESTADO
------
Bloque 1 (H-CONVERGENCIA) corre en cuanto exista data/owid-maddison.csv.
Bloque 2 (H-ACOPLAMIENTO) requiere ademas una matriz de comercio bilateral.
Bloque 0 (diagnostico estructural) corre YA, sin datos externos.

USO
---
    python prueba_discriminante_dominio_B.py \
        --corpus by_domain/dominio_B_real.csv \
        --maddison data/owid-maddison.csv \
        --comercio data/comercio_bilateral.csv
"""
import argparse
import itertools
import logging
import os
import sys

import numpy as np
import pandas as pd
from scipy import stats

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[logging.FileHandler("prueba_discriminante_log.txt", mode="w",
                                  encoding="utf-8"),
              logging.StreamHandler(sys.stdout)])
log = logging.getLogger("DISCRIM")


def head(t):
    log.info("")
    log.info("=" * 78)
    log.info(t)
    log.info("=" * 78)


# =============================================================================
def bloque0_estructura(B):
    """Diagnostico estructural. No requiere datos externos."""
    head("BLOQUE 0 — diagnostico estructural del rol de hub")

    hubs, nodos = set(B["hub"]), set(B["nodo"])
    ambos = hubs & nodos
    log.info("paises en rol de hub          : %d", len(hubs))
    log.info("paises en rol de satelite     : %d", len(nodos))
    log.info("paises en AMBOS roles         : %d  (%.0f%% de los hubs)",
             len(ambos), 100 * len(ambos) / len(hubs))

    filas = []
    for c in sorted(ambos):
        filas.append({"pais": c,
                      "como_hub": int((B["hub"] == c).sum()),
                      "como_satelite": int((B["nodo"] == c).sum())})
    amb = pd.DataFrame(filas).sort_values("como_satelite", ascending=False)
    log.info("")
    log.info("Casos mas contradictorios (mucho satelite, poco hub):")
    log.info("\n%s", amb.head(10).to_string(index=False))

    log.info("")
    log.info("INTERPRETACION: si el rol de hub fuera estructural, un pais no")
    log.info("apareceria en ambos roles dentro del mismo sistema regional.")
    log.info("Que %d%% lo haga indica que el rol lo fija un operador de",
             round(100 * len(ambos) / len(hubs)))
    log.info("comparacion sobre PIB per capita, no la topologia de una red.")

    log.info("")
    log.info("--- b por region ---")
    reg = B.groupby("region")["b"].agg(
        ["count", "mean", "median", "std"]).round(4)
    log.info("\n%s", reg.sort_values("mean", ascending=False).to_string())
    k = stats.kruskal(*[g["b"].values for _, g in B.groupby("region")])
    log.info("Kruskal-Wallis entre regiones: H=%.3f  p=%.4g",
             k.statistic, k.pvalue)
    log.info("b<0 (convergencia): %d (%.1f%%)  |  b>0 (divergencia): %d",
             int((B["b"] < 0).sum()), 100 * (B["b"] < 0).mean(),
             int((B["b"] > 0).sum()))
    return amb


# =============================================================================
def bloque1_convergencia(B, maddison_path):
    """H-CONVERGENCIA: b ~ brecha inicial de PIB per capita."""
    head("BLOQUE 1 — H-CONVERGENCIA (b vs brecha inicial)")

    if not os.path.exists(maddison_path):
        log.warning("BLOQUEADO: no existe %s", maddison_path)
        log.warning("Sin la fuente no se puede calcular la brecha inicial.")
        log.warning("Ver data/FUENTES.md — fijar edicion y SHA-256 antes de "
                    "correr,")
        log.warning("porque el Maddison Project revisa estimaciones entre "
                    "ediciones.")
        return None

    M = pd.read_csv(maddison_path)
    col_pais = next(
        (c for c in ("country", "entity", "Entity") if c in M.columns), None)
    col_anio = next((c for c in ("year", "Year") if c in M.columns), None)
    col_pib = next(
        (c for c in M.columns if "gdp" in c.lower() or "pib" in c.lower()),
        None)
    if not all([col_pais, col_anio, col_pib]):
        log.error("No identifico columnas en %s: %s",
                  maddison_path, list(M.columns))
        return None
    log.info("Maddison: pais=%s anio=%s pib=%s", col_pais, col_anio, col_pib)

    piv = M.pivot_table(index=col_anio, columns=col_pais, values=col_pib)

    filas = []
    for _, r in B.iterrows():
        y0 = int(r["year_min"])
        try:
            g_hub, g_nodo = piv.loc[y0, r["hub"]], piv.loc[y0, r["nodo"]]
        except KeyError:
            continue
        if not (np.isfinite(g_hub) and np.isfinite(g_nodo)
                and g_hub > 0 and g_nodo > 0):
            continue
        filas.append({"id": r["id"], "b": r["b"], "region": r["region"],
                      "brecha_log": float(np.log(g_hub / g_nodo)),
                      "pib_hub_0": float(g_hub), "n": r["n"]})
    D = pd.DataFrame(filas)
    log.info("pares con brecha inicial calculable: %d de %d", len(D), len(B))
    if len(D) < 30:
        log.warning("Muy pocos pares emparejados; revisar nombres de paises.")
        return D

    rho, p = stats.spearmanr(D["brecha_log"], D["b"])
    log.info("")
    log.info("Spearman  b vs brecha inicial log(PIB_hub/PIB_nodo):")
    log.info("   rho = %+.4f   p = %.4g   n = %d", rho, p, len(D))
    log.info("")
    log.info("PREDICCION H-CONVERGENCIA: rho NEGATIVO y significativo")
    log.info("   (brecha grande -> el rezagado alcanza -> el cociente "
             "hub/nodo cae -> b menor)")
    log.info("VEREDICTO H-CONVERGENCIA: %s",
             "RESPALDADA" if (rho < 0 and p < 0.05) else "NO respaldada")

    # dentro de region, para descartar que sea puro efecto de region
    log.info("")
    log.info("--- controlando por region (Spearman intra-region) ---")
    for reg, g in D.groupby("region"):
        if len(g) < 8:
            continue
        rr, pp = stats.spearmanr(g["brecha_log"], g["b"])
        log.info("   %-20s n=%3d  rho=%+.3f  p=%.4f", reg, len(g), rr, pp)

    D.to_csv("discrim_bloque1_convergencia.csv", index=False)
    return D


# =============================================================================
def _maddison_pivot(maddison_path):
    """Carga el Maddison y devuelve (pivot año x país, columnas usadas)."""
    M = pd.read_csv(maddison_path)
    col_pais = next(
        (c for c in ("country", "entity", "Entity") if c in M.columns), None)
    col_anio = next((c for c in ("year", "Year") if c in M.columns), None)
    col_pib = next(
        (c for c in M.columns if "gdp" in c.lower() or "pib" in c.lower()),
        None)
    piv = M.pivot_table(index=col_anio, columns=col_pais, values=col_pib)
    return piv


def bloque1b_placebo(B, maddison_path, n_iter=500, seed=20260725):
    """NULO CORRECTO para el Bloque 1 — controla el artefacto de asignacion.

    PROBLEMA: expand_dominio_B.py asigna hub por PIB per capita PROMEDIO sobre
    toda la serie (`pib_avg[a] >= pib_avg[b]`). Esa regla usa informacion de
    TODO el periodo para decidir el rol, y la brecha inicial es esencialmente
    el intercepto del mismo ajuste que produce b. Resultado: pendiente y brecha
    quedan mecanicamente anticorrelacionadas ANTES de cualquier economia.

    Simulacion con paseos aleatorios independientes (cero acoplamiento, cero
    convergencia) bajo esta misma regla: rho ~ -0.26. Con hub asignado por PIB
    del PRIMER anio: rho ~ -0.01. El artefacto lo inyecta la regla, no los datos.

    Por eso el rho observado NO debe compararse contra cero, sino contra la
    distribucion nula generada re-emparejando paises al azar dentro de region
    con el mismo pipeline completo.
    """
    head("BLOQUE 1b — nulo por remuestreo (artefacto de asignacion de hub)")

    if not os.path.exists(maddison_path):
        log.warning("BLOQUEADO: no existe %s", maddison_path)
        return None

    rng = np.random.default_rng(seed)
    piv = _maddison_pivot(maddison_path)

    y0, y1 = int(B["year_min"].min()), int(B["year_max"].max())
    paises_por_region = {r: sorted(set(g["hub"]) | set(g["nodo"]))
                         for r, g in B.groupby("region")}
    n_por_region = B["region"].value_counts().to_dict()

    def ajusta_par(pa, pb):
        """Replica exacta de expand_dominio_B: hub por PIB promedio, t=1..n."""
        try:
            s = piv.loc[y0:y1, [pa, pb]].dropna()
        except KeyError:
            return None
        if len(s) < 8:
            return None
        hub, nodo = (pa, pb) if s[pa].mean() >= s[pb].mean() else (pb, pa)
        R = (s[hub] / s[nodo]).values
        t = np.arange(1, len(R) + 1)
        if np.any(R <= 0):
            return None
        b = float(np.polyfit(np.log(t), np.log(R), 1)[0])
        return b, float(np.log(R[0]))

    nulos = []
    for _ in range(n_iter):
        bs, gaps = [], []
        for reg, paises in paises_por_region.items():
            if len(paises) < 2:
                continue
            for _ in range(n_por_region.get(reg, 0)):
                pa, pb = rng.choice(paises, size=2, replace=False)
                r = ajusta_par(pa, pb)
                if r:
                    bs.append(r[0])
                    gaps.append(r[1])
        if len(bs) > 30:
            rho, _ = stats.spearmanr(gaps, bs)
            if np.isfinite(rho):
                nulos.append(rho)
    nulos = np.array(nulos)
    if len(nulos) == 0:
        log.error("No se genero distribucion nula.")
        return None

    log.info("Distribucion nula (%d iteraciones, re-emparejamiento aleatorio",
             len(nulos))
    log.info("dentro de region, mismo pipeline con hub por PIB promedio):")
    log.info("   media  = %+.4f", nulos.mean())
    log.info("   IC95%%  = [%+.4f, %+.4f]", *np.percentile(nulos, [2.5, 97.5]))
    log.info("")
    log.info("IMPORTANTE: si la media del nulo NO es ~0, la regla de asignacion")
    log.info("de hub esta inyectando correlacion espuria por si sola.")
    return nulos


def bloque1c_split(B, maddison_path):
    """Rompe el acoplamiento mecanico: brecha en la 1a mitad, b en la 2a mitad.

    Con datos disjuntos, la brecha ya no es el intercepto del ajuste que produce
    b. Si la relacion sobrevive aqui, es economica; si desaparece, era artefacto.
    Este es el test limpio.
    """
    head("BLOQUE 1c — muestra partida (brecha 1a mitad / b 2a mitad)")

    if not os.path.exists(maddison_path):
        log.warning("BLOQUEADO: no existe %s", maddison_path)
        return None

    piv = _maddison_pivot(maddison_path)

    filas = []
    for _, r in B.iterrows():
        try:
            s = piv.loc[int(r["year_min"]):int(r["year_max"]),
                        [r["hub"], r["nodo"]]].dropna()
        except KeyError:
            continue
        if len(s) < 16:
            continue
        mitad = len(s) // 2
        R = (s[r["hub"]] / s[r["nodo"]]).values
        if np.any(R <= 0):
            continue
        brecha_1a = float(np.log(R[:mitad].mean()))          # solo 1a mitad
        R2 = R[mitad:]
        t2 = np.arange(1, len(R2) + 1)                        # solo 2a mitad
        b_2a = float(np.polyfit(np.log(t2), np.log(R2), 1)[0])
        filas.append({"id": r["id"], "region": r["region"],
                      "brecha_1a_mitad": brecha_1a, "b_2a_mitad": b_2a,
                      "b_completo": r["b"]})
    D = pd.DataFrame(filas)
    log.info("pares con muestra partida: %d de %d", len(D), len(B))
    if len(D) < 30:
        log.warning("n insuficiente.")
        return D

    rho, p = stats.spearmanr(D["brecha_1a_mitad"], D["b_2a_mitad"])
    log.info("")
    log.info("Spearman  b(2a mitad) vs brecha(1a mitad)  [DATOS DISJUNTOS]:")
    log.info("   rho = %+.4f   p = %.4g   n = %d", rho, p, len(D))
    log.info("")
    log.info("Comparar contra el rho del Bloque 1 (datos acoplados).")
    log.info("Si cae mucho, buena parte del Bloque 1 era acoplamiento mecanico.")
    D.to_csv("discrim_bloque1c_split.csv", index=False)
    return D


# =============================================================================
def bloque1d_nulo_calibrado(B, maddison_path, n_iter=300, seed=20260725):
    """NULO CORRECTO para el artefacto de asignacion — series sinteticas
    calibradas al Maddison real.

    POR QUE NO SIRVE EL BLOQUE 1b: re-emparejar paises dentro de region NO
    destruye el mecanismo que se quiere aislar. El acoplamiento pendiente-brecha
    aplica a CUALQUIER par de series; re-emparejar lo conserva intacto. El 1b no
    es un nulo, es mas cercano a un bootstrap: mide artefacto + estructura comun
    de las series reales (shocks globales, tendencias compartidas). Por eso sale
    mas extremo que lo observado.

    EL NULO QUE SI CORRESPONDE: series sinteticas sin ninguna economia, con la
    MISMA estructura de regiones y el MISMO n, y con los parametros de deriva,
    volatilidad y dispersion de niveles CALIBRADOS al Maddison real.

    Sin calibrar, la ubicacion del nulo depende de parametros inventados.
    """
    head("BLOQUE 1d — nulo sintetico calibrado (el correcto para el artefacto)")

    if not os.path.exists(maddison_path):
        log.warning("BLOQUEADO: no existe %s", maddison_path)
        return None

    rng = np.random.default_rng(seed)
    piv = _maddison_pivot(maddison_path)

    paises = sorted(set(B["hub"]) | set(B["nodo"]))
    y0, y1 = int(B["year_min"].min()), int(B["year_max"].max())
    sub = piv.loc[y0:y1, [p for p in paises if p in piv.columns]]

    # calibracion sobre los datos reales
    lg = np.log(sub)
    dif = lg.diff().values
    dif = dif[np.isfinite(dif)]
    drift, sigma = float(np.mean(dif)), float(np.std(dif))
    niv = lg.iloc[0].dropna().values
    niv_mu, niv_sd = float(np.mean(niv)), float(np.std(niv))
    n_anios = len(sub)
    log.info("Calibracion sobre Maddison real:")
    log.info("   deriva anual (media dlog) = %+.5f", drift)
    log.info("   volatilidad (sd dlog)     = %.5f", sigma)
    log.info("   nivel inicial log: media=%.3f  sd=%.3f", niv_mu, niv_sd)
    log.info("   anios por serie           = %d", n_anios)

    n_por_region = B["region"].value_counts().to_dict()

    def n_paises(k):
        n = 2
        while n * (n - 1) // 2 < k:
            n += 1
        return n

    def una_corrida(split):
        bs, gs = [], []
        for reg, k in n_por_region.items():
            S = [np.exp(np.cumsum(rng.normal(drift, sigma, n_anios))
                        + rng.normal(niv_mu, niv_sd))
                 for _ in range(n_paises(k))]
            for idx, (i, j) in enumerate(
                    itertools.combinations(range(len(S)), 2)):
                if idx >= k:
                    break
                A, Bs = S[i], S[j]
                hub, nodo = (A, Bs) if A.mean() >= Bs.mean() else (Bs, A)
                R = hub / nodo
                if split:
                    m = len(R) // 2
                    gs.append(float(np.log(R[:m].mean())))
                    R2 = R[m:]
                    t2 = np.arange(1, len(R2) + 1)
                    bs.append(float(np.polyfit(np.log(t2), np.log(R2), 1)[0]))
                else:
                    t = np.arange(1, len(R) + 1)
                    gs.append(float(np.log(R[0])))
                    bs.append(float(np.polyfit(np.log(t), np.log(R), 1)[0]))
        return stats.spearmanr(gs, bs)[0], len(bs)

    salida = {}
    for split, etiqueta in ((False, "Bloque 1 (serie completa)"),
                            (True, "Bloque 1c (muestra partida)")):
        r = np.array([una_corrida(split)[0] for _ in range(n_iter)])
        r = r[np.isfinite(r)]
        lo, hi = np.percentile(r, [2.5, 97.5])
        _, n_nulo = una_corrida(split)
        log.info("")
        log.info("--- %s ---  n del nulo = %d", etiqueta, n_nulo)
        log.info("   nulo calibrado: media = %+.4f   IC95 = [%+.4f, %+.4f]",
                 r.mean(), lo, hi)
        salida[etiqueta] = {"media": float(r.mean()),
                            "ic95": (float(lo), float(hi)), "dist": r}
    log.info("")
    log.info("COMPARAR el rho observado contra ESTE nulo, no contra cero y no")
    log.info("contra el del Bloque 1b. Si cae fuera del IC95, hay senal por")
    log.info("encima del artefacto de asignacion de hub.")
    return salida


# =============================================================================
def bloque2_acoplamiento(B, comercio_path, D1=None):
    """H-ACOPLAMIENTO: b ~ participacion de comercio bilateral.

    Espera un CSV largo con columnas: origen, destino, anio, valor.
    Se construye share = exportaciones(nodo->hub) / exportaciones totales(nodo).
    """
    head("BLOQUE 2 — H-ACOPLAMIENTO (b vs comercio bilateral)")

    if not os.path.exists(comercio_path):
        log.warning("BLOQUEADO: no existe %s", comercio_path)
        log.warning("Candidatos: IMF DOTS (1948-), CEPII BACI, UN Comtrade "
                    "(1962-).")
        log.warning("Requisito: bilateral y direccional. El hub debe EMERGER "
                    "de la red")
        log.warning("(centralidad), no asignarse por PIB per capita.")
        return None

    T = pd.read_csv(comercio_path)
    req = {"origen", "destino", "anio", "valor"}
    if not req.issubset(T.columns):
        log.error("Se esperan columnas %s; hay %s", req, list(T.columns))
        return None

    tot = T.groupby(["origen", "anio"])["valor"].sum().rename("total")
    T = T.join(tot, on=["origen", "anio"])
    T["share"] = T["valor"] / T["total"]

    filas = []
    for _, r in B.iterrows():
        m = T[(T["origen"] == r["nodo"]) & (T["destino"] == r["hub"])]
        if m.empty:
            continue
        filas.append({"id": r["id"], "b": r["b"], "region": r["region"],
                      "share_media": float(m["share"].mean()),
                      "share_inicial": float(
                          m.sort_values("anio")["share"].iloc[0])})
    D = pd.DataFrame(filas)
    log.info("pares con comercio bilateral disponible: %d de %d", len(D), len(B))
    if len(D) < 30:
        log.warning("Muy pocos pares emparejados.")
        return D

    for col in ("share_media", "share_inicial"):
        rho, p = stats.spearmanr(D[col], D["b"])
        log.info("Spearman b vs %-14s: rho = %+.4f   p = %.4g", col, rho, p)
    log.info("")
    log.info("PREDICCION H-ACOPLAMIENTO: rho POSITIVO y significativo")
    rho, p = stats.spearmanr(D["share_media"], D["b"])
    log.info("VEREDICTO H-ACOPLAMIENTO: %s",
             "RESPALDADA" if (rho > 0 and p < 0.05) else "NO respaldada")

    D.to_csv("discrim_bloque2_acoplamiento.csv", index=False)
    return D


# =============================================================================
def bloque3_conjunto(D1, D2):
    """Modelo con ambos regresores: cuanto explica cada hipotesis."""
    head("BLOQUE 3 — modelo conjunto")
    if D1 is None or D2 is None:
        log.warning("BLOQUEADO: requiere los bloques 1 y 2 completos.")
        return
    D = D1.merge(D2[["id", "share_media"]], on="id")
    log.info("pares con ambos regresores: %d", len(D))
    if len(D) < 40:
        log.warning("n insuficiente para el modelo conjunto.")
        return

    X = np.column_stack([np.ones(len(D)), D["brecha_log"], D["share_media"]])
    y = D["b"].values
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    sse = float(resid @ resid)
    sst = float(((y - y.mean()) ** 2).sum())
    log.info("b = %+.4f  %+.4f*brecha_log  %+.4f*share_media", *beta)
    log.info("R2 = %.4f", 1 - sse / sst)

    for nombre, idx in (("solo brecha", [0, 1]), ("solo share", [0, 2])):
        Xr = X[:, idx]
        br, *_ = np.linalg.lstsq(Xr, y, rcond=None)
        rr = y - Xr @ br
        log.info("  %-12s: R2 = %.4f", nombre, 1 - float(rr @ rr) / sst)
    log.info("")
    log.info("Comparar los R2 parciales indica cuanto del exponente b es")
    log.info("atribuible a cada mecanismo. Si 'solo brecha' ~ el modelo "
             "completo,")
    log.info("el dominio B esta midiendo convergencia, no acoplamiento.")


# =============================================================================
def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", default="by_domain/dominio_B_real.csv")
    ap.add_argument("--maddison", default="data/owid-maddison.csv")
    ap.add_argument("--comercio", default="data/comercio_bilateral.csv")
    ap.add_argument("--n-placebo", type=int, default=500,
                    help="iteraciones del nulo por remuestreo (bloque 1b)")
    a = ap.parse_args()

    log.info("Prueba discriminante dominio B — acoplamiento vs convergencia")
    log.info("corpus=%s  maddison=%s  comercio=%s",
             a.corpus, a.maddison, a.comercio)

    B = pd.read_csv(a.corpus)
    log.info("corpus dominio B: %d casos", len(B))

    bloque0_estructura(B)
    D1 = bloque1_convergencia(B, a.maddison)
    NUL = bloque1b_placebo(B, a.maddison, n_iter=a.n_placebo)
    D1c = bloque1c_split(B, a.maddison)
    CAL = bloque1d_nulo_calibrado(B, a.maddison, n_iter=a.n_placebo)
    D2 = bloque2_acoplamiento(B, a.comercio, D1)
    bloque3_conjunto(D1, D2)

    head("FIN")
    log.info("Bloque 0  (estructura)   : siempre corre")
    log.info("Bloque 1  (convergencia) : %s",
             "corrido" if D1 is not None else "BLOQUEADO (falta Maddison)")
    log.info("Bloque 1b (nulo placebo) : %s",
             "corrido" if NUL is not None else "BLOQUEADO (falta Maddison)")
    log.info("Bloque 1c (split)        : %s",
             "corrido" if D1c is not None else "BLOQUEADO (falta Maddison)")
    log.info("Bloque 1d (nulo calibr.) : %s",
             "corrido" if CAL is not None else "BLOQUEADO (falta Maddison)")
    log.info("Bloque 2  (acoplamiento) : %s",
             "corrido" if D2 is not None else "BLOQUEADO (falta comercio)")
    log.info("")
    log.info("El rho observado se compara contra el nulo del 1d (calibrado), NO")
    log.info("contra cero y NO contra el 1b. El 1b conserva el mecanismo que se")
    log.info("quiere aislar, asi que no es un nulo valido para esta pregunta.")


if __name__ == "__main__":
    main()
