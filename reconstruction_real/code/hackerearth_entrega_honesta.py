#!/usr/bin/env python3
"""
Entrega honesta del proyecto HackerEarth/Zerve — los numeros reales.

Entrena el modelo de churn con etiqueta TEMPORAL (no circular): features de
eventos antes del corte T1 = 2025-11-08, etiqueta = inactividad de 30 dias
despues de T1. Luego puntua a TODOS los usuarios con sus features al final de
los datos (2025-12-08) y reconstruye la matriz de accion 2x2 con dos
dimensiones ahora genuinamente distintas: probabilidad de churn (modelo
temporal) y profundidad de engagement (descriptiva).

Esto sustituye las cifras del reporte "Fractal V3" (ROC-AUC 0.9994 / 1.0 /
precision 1.0), que son circulares por construccion (etiqueta = cohorte
definida por CSI_V3, con CSI_V3 en los features). Ver
`audits/REVISION_REPORTE_HACKEREARTH_2026-10-18.md` y
`code/hackerearth_verificacion.py`.

Salidas (en data/hackerearth_zerve/):
    entrega_scores_honestos.csv      — 4,774 usuarios: features al corte,
                                       probabilidad de churn 30d, cuadrante
    entrega_matriz_accion.csv        — conteos del 2x2
    entrega_resumen.csv              — numeros reales clave
    log en reconstruction_real/logs/

Uso:
    python reconstruction_real/code/hackerearth_entrega_honesta.py \
        [--raw /ruta/a/zerve_hackathon_dataset.csv]
"""

import argparse
import csv
import hashlib
import logging
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score

ROOT = Path(__file__).resolve().parent.parent.parent
ZV = ROOT / "data" / "hackerearth_zerve"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "hackerearth_entrega_honesta_log.txt"

SHA_RAW = "73c44fc9d47abd67ef0e9280f71bc2fec9b8483d3fc304a1f747593f9aa27390"
DEFAULT_RAW = Path("/mnt/c/Users/elanz/Downloads/zerve_hackathon_dataset.csv")

T1 = pd.Timestamp("2025-11-08", tz="UTC")     # corte de entrenamiento
T_FIN = pd.Timestamp("2025-12-09", tz="UTC")  # fin de los datos (score)
UMBRAL_PROB = 0.5
UMBRAL_ENG = 3                                # >= 3 eventos totales

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("HE-ENTREGA")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


FEATURES = ["n_eventos", "tipos_evento", "dias_activos", "eventos_creditos",
            "eventos_agente", "recencia_dias", "antiguedad_dias", "velocidad"]


def features_hasta(df, corte):
    """Features de engagement por usuario, SOLO con eventos < corte."""
    d = df[df.timestamp < corte]
    g = d.groupby("person_id")
    f = pd.DataFrame({
        "n_eventos": g.size(),
        "tipos_evento": g["event"].nunique(),
        "dias_activos": g["timestamp"].apply(
            lambda s: s.dt.normalize().nunique()),
        "eventos_creditos": g["event"].apply(
            lambda s: s.isin(["credits_used", "credits_exceeded"]).sum()),
        "eventos_agente": g["event"].apply(
            lambda s: s.str.startswith("agent_").sum()),
        "recencia_dias": (corte - g["timestamp"].max()).dt.total_seconds() / 86400,
        "antiguedad_dias": (g["timestamp"].max() - g["timestamp"].min())
                           .dt.total_seconds() / 86400,
    })
    f["velocidad"] = f["n_eventos"] / f["dias_activos"].clip(lower=1)
    return f


def gbm():
    return GradientBoostingClassifier(
        n_estimators=300, learning_rate=0.05, max_depth=4,
        min_samples_leaf=10, subsample=0.8, max_features="sqrt",
        random_state=42,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=str(DEFAULT_RAW))
    args = ap.parse_args()

    log.info("=" * 78)
    log.info("ENTREGA HONESTA HACKEREARTH/ZERVE — numeros reales")
    log.info("=" * 78)

    if not os.path.exists(args.raw):
        log.error("Falta el dataset crudo: %s", args.raw)
        return 1
    dig = sha256(args.raw)
    if dig != SHA_RAW:
        log.error("SHA-256 distinto del anclado")
        return 1
    log.info("SHA-256 raw OK (%s…)", dig[:16])

    df = pd.read_csv(args.raw, usecols=["person_id", "event", "timestamp"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, format="mixed")
    log.info("Eventos: %s | usuarios: %s | rango %s -> %s",
             f"{len(df):,}", f"{df.person_id.nunique():,}",
             df.timestamp.min().date(), df.timestamp.max().date())

    # ---- 1. Entrenamiento con etiqueta temporal ----
    pre = features_hasta(df, T1)
    activos_post = set(df[df.timestamp >= T1].person_id.unique())
    pre["churned"] = (~pre.index.isin(activos_post)).astype(int)

    y = pre["churned"].values
    X = pre[FEATURES].values
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    aucs = cross_val_score(gbm(), X, y, cv=cv, scoring="roc_auc")
    log.info("Modelo temporal: AUC CV 5-fold = %.4f +/- %.4f | n=%s | "
             "tasa churn 30d = %.1f%%", aucs.mean(), aucs.std(), len(pre),
             100 * y.mean())

    modelo = gbm()
    modelo.fit(X, y)
    imp = dict(zip(FEATURES, modelo.feature_importances_))
    top = sorted(imp.items(), key=lambda kv: -kv[1])
    log.info("Importancias: %s",
             "; ".join(f"{k} {v:.0%}" for k, v in top[:5]))

    # ---- 2. Score de TODOS los usuarios al final de los datos ----
    actuales = features_hasta(df, T_FIN)
    log.info("Usuarios a puntuar: %s", f"{len(actuales):,}")
    prob = modelo.predict_proba(actuales[FEATURES].values)[:, 1]

    scores = actuales.reset_index()[["person_id"] + FEATURES].copy()
    scores["prob_churn_30d"] = prob
    scores["engagement"] = scores["n_eventos"]

    def cuadrante(fila):
        alto = fila["prob_churn_30d"] > UMBRAL_PROB
        eng = fila["engagement"] >= UMBRAL_ENG
        if alto and eng:
            return "Intervenir ya (riesgo alto, engagement alto)"
        if alto and not eng:
            return "Reactivar (riesgo alto, engagement bajo)"
        if not alto and eng:
            return "Cuidar (riesgo bajo, engagement alto)"
        return "Vigilar (riesgo bajo, engagement bajo)"

    scores["cuadrante"] = scores.apply(cuadrante, axis=1)

    # Calibracion declarativa: tasa predicha vs ventana de entrenamiento
    log.info("Probabilidad media predicha: %.3f (tasa real de la ventana de "
             "entrenamiento: %.3f)", prob.mean(), y.mean())

    # ---- 3. Salidas ----
    out_scores = ZV / "entrega_scores_honestos.csv"
    scores.to_csv(out_scores, index=False)
    log.info("Scores -> %s", out_scores.relative_to(ROOT))

    matriz = scores["cuadrante"].value_counts().rename_axis("cuadrante") \
        .reset_index(name="usuarios")
    matriz["pct"] = (100 * matriz["usuarios"] / len(scores)).round(1)
    out_matriz = ZV / "entrega_matriz_accion.csv"
    matriz.to_csv(out_matriz, index=False)
    log.info("Matriz -> %s", out_matriz.relative_to(ROOT))

    resumen = [
        ("metrica", "valor"),
        ("usuarios_totales", len(scores)),
        ("ventana_datos", f"{df.timestamp.min().date()} a "
                          f"{df.timestamp.max().date()}"),
        ("modelo_entrenamiento", f"features < {T1.date()}, outcome 30d"),
        ("auc_cv_5fold", f"{aucs.mean():.4f} +/- {aucs.std():.4f}"),
        ("n_entrenamiento", len(pre)),
        ("tasa_churn_ventana", f"{100 * y.mean():.1f}%"),
        ("prob_media_predicha", f"{prob.mean():.3f}"),
        ("top_features", "; ".join(f"{k} {v:.0%}" for k, v in top[:5])),
        ("umbral_prob", UMBRAL_PROB),
        ("umbral_engagement_eventos", UMBRAL_ENG),
    ]
    for fila in matriz.itertuples():
        resumen.append((f"cuadrante_{fila.cuadrante}", fila.usuarios))
    out_res = ZV / "entrega_resumen.csv"
    with open(out_res, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerows(resumen)
    log.info("Resumen -> %s", out_res.relative_to(ROOT))

    # ---- 4. Numeros reales (stdout, para el documento de entrega) ----
    log.info("")
    log.info("=" * 78)
    log.info("NUMEROS REALES (sustituyen a 0.9994 / 1.0 / precision 1.0)")
    log.info("=" * 78)
    log.info("  AUC honesto (CV 5-fold, etiqueta temporal): %.4f +/- %.4f",
             aucs.mean(), aucs.std())
    log.info("  Senal dominante: %s",
             "; ".join(f"{k} {v:.0%}" for k, v in top[:3]))
    log.info("  Matriz 2x2 honesta:")
    for fila in matriz.itertuples():
        log.info("    %-55s %6d  (%.1f%%)", fila.cuadrante, fila.usuarios,
                 fila.pct)
    log.info("  Horizonte declarado: 30 dias desde el fin de los datos "
             "(2025-12-08).")
    log.info("  Caveats: censura derecha; un corte; recencia domina la senal.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
