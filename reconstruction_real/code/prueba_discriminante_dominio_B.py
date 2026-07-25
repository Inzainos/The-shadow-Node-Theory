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
    a = ap.parse_args()

    log.info("Prueba discriminante dominio B — acoplamiento vs convergencia")
    log.info("corpus=%s  maddison=%s  comercio=%s",
             a.corpus, a.maddison, a.comercio)

    B = pd.read_csv(a.corpus)
    log.info("corpus dominio B: %d casos", len(B))

    bloque0_estructura(B)
    D1 = bloque1_convergencia(B, a.maddison)
    D2 = bloque2_acoplamiento(B, a.comercio, D1)
    bloque3_conjunto(D1, D2)

    head("FIN")
    log.info("Bloque 0 : siempre corre")
    log.info("Bloque 1 : %s",
             "corrido" if D1 is not None else "BLOQUEADO (falta Maddison)")
    log.info("Bloque 2 : %s",
             "corrido" if D2 is not None else "BLOQUEADO (falta comercio)")


if __name__ == "__main__":
    main()
