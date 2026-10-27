#!/usr/bin/env python3
"""
Verificacion empirica del reporte HackerEarth "Fractal V3" (2026-10-18).

Dos partes:

PARTE 1 — Reproducir las cifras del reporte y demostrar su circularidad.
  * 1a. Modelo de retencion del proyecto (GBM, features incl. CSI_V3, label =
    cohort != Basic): la etiqueta es un corte de percentil de CSI_V3 y CSI_V3
    esta en la matriz de features -> AUC 1.0 por construccion.
  * 1b. La etiqueta de churn (risk_tier == "High Risk") es identica a la
    cohorte Basic (4,444 = 4,444): CSI_V3 SOLO, sin 284 features, debe
    reproducir el 0.9994 si el "modelo" es una re-derivacion de la definicion.

PARTE 2 — La prueba honesta: etiqueta temporal prospectiva.
  Datos crudos: eventos PostHog 2025-09-01 .. 2025-12-08 (98 dias).
  Corte T1 = 2025-11-08; ventana de outcome = 30 dias (hasta el fin de datos).
  Poblacion en riesgo: usuarios con >= 1 evento antes de T1.
  Features: SOLO eventos con timestamp < T1 (dias activos, tipos de evento
  distintos, eventos de creditos, eventos de agente, recencia, antiguedad,
  velocidad). Etiqueta: SIN eventos en [T1, fin) = churned.
  GBM igual familia que el del proyecto; AUC por CV 5-fold.
  Sensibilidad: excluyendo usuarios con antiguedad < 7 dias (se dieron de alta
  justo antes del corte).
  Caveats declarados: censura a la derecha (el dato termina 2025-12-08; un
  "churned" pudo volver despues), una sola ventana, un solo corte.

Uso:
    python reconstruction_real/code/hackerearth_verificacion.py \
        [--raw /ruta/a/zerve_hackathon_dataset.csv]

Sin --raw usa la ruta por defecto de Downloads (no versionada; SHA anclado en
data/FUENTES.md). Los archivos pequenos (metricas, scores) se leen de
data/hackerearth_zerve/ (versionados).
"""

import argparse
import csv
import logging
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))
from snt import sha256  # noqa: E402
ZV = ROOT / "data" / "hackerearth_zerve"
DATA_RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "hackerearth_verificacion_log.txt"
OUT = DATA_RR / "hackerearth_verificacion_resultados.csv"

SHA_RAW = "73c44fc9d47abd67ef0e9280f71bc2fec9b8483d3fc304a1f747593f9aa27390"
# Dataset propietario, no redistribuible (ver sources.md). Ruta por variable de
# entorno SNT_ZERVE_RAW o por --raw; por defecto, el directorio de trabajo.
DEFAULT_RAW = Path(os.environ.get("SNT_ZERVE_RAW",
                                  "zerve_hackathon_dataset.csv"))

# Corte temporal: 30 dias antes del fin de los datos (2025-12-08).
T1 = pd.Timestamp("2025-11-08", tz="UTC")
T_FIN = pd.Timestamp("2025-12-09", tz="UTC")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("HE-VERIF")

RESULTADOS = []


def reg(punto, cifra, valor, estado="INFO"):
    RESULTADOS.append({"punto": punto, "cifra": cifra, "valor": valor,
                       "estado": estado})
    log.info("%-28s %-46s %s", punto, cifra, valor)


def gbm():
    return GradientBoostingClassifier(
        n_estimators=300, learning_rate=0.05, max_depth=4,
        min_samples_leaf=10, subsample=0.8, max_features="sqrt",
        random_state=42,
    )


def parte1():
    """Reproduccion de las cifras del reporte + demostracion de circularidad."""
    log.info("=" * 78)
    log.info("PARTE 1 — Reproducir las cifras del reporte")
    log.info("=" * 78)
    sc = pd.read_csv(ZV / "docu_retention_scores.csv")

    # Verificacion de conteos del PDF
    reg("P1_conteos", "usuarios", len(sc))
    reg("P1_conteos", "cohortes (Basic/Inter/Elite)",
        "/".join(str(sc.cohort.value_counts()[c]) for c in
                 ("Basic", "Intermediate", "Elite")))
    reg("P1_conteos", "tiers (High/Likely/AtRisk/Confident)",
        "/".join(str(sc.risk_tier.value_counts()[t]) for t in
                 ("High Risk", "Likely Retained", "At Risk",
                  "Confident Retained")))

    # 1b-0: ¿High Risk es exactamente Basic?
    identicos = int((sc.cohort == "Basic").sum() ==
                    (sc.risk_tier == "High Risk").sum()) and \
        int(((sc.cohort == "Basic") == (sc.risk_tier == "High Risk")).sum())
    reg("P1_tautologia", "High Risk == Basic (usuarios identicos)",
        f"{identicos}/{len(sc)}", "CIRCULAR" if identicos == len(sc) else "OK")

    # 1a: modelo de retencion tal como lo define el proyecto
    feats = ["dias_activos", "herramientas_unicas", "total_creditos",
             "pct_coder_agent", "VDR", "CSI_V3", "resonance_factor",
             "engagement_density"]
    X = sc[feats].values
    y = (sc["cohort"] != "Basic").astype(int).values
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                          random_state=42, stratify=y)
    sc_ = StandardScaler().fit(Xtr)
    m = gbm()
    m.fit(sc_.transform(Xtr), ytr)
    auc = roc_auc_score(yte, m.predict_proba(sc_.transform(Xte))[:, 1])
    reg("P1_retencion", "AUC label=cohort!=Basic, features incl. CSI_V3",
        f"{auc:.4f}", "CIRCULAR" if auc >= 0.9999 else "INFO")
    reg("P1_retencion", "reporte PDF", "1.0000 (precision 1.0, recall 1.0)")

    # 1b: CSI_V3 solo, contra la etiqueta de churn del proyecto
    ych = (sc["risk_tier"] == "High Risk").astype(int).values
    x_csi = sc[["CSI_V3"]].values
    auc_csi = roc_auc_score(ych, -x_csi.ravel())
    reg("P1_churn", "AUC de SOLO CSI_V3 (invertido) vs label High Risk",
        f"{auc_csi:.4f}", "CIRCULAR" if auc_csi >= 0.99 else "INFO")
    reg("P1_churn", "reporte PDF (284 features)", "0.9994 (CV 0.9945)")

    # Importancia: ¿CSI_V3 domina la etiqueta que define?
    imp = dict(zip(feats, m.feature_importances_))
    top = sorted(imp.items(), key=lambda kv: -kv[1])[:3]
    reg("P1_retencion", "top-3 importancia del modelo reproducido",
        "; ".join(f"{k} {v:.0%}" for k, v in top))


def parte2(raw_path):
    """Prueba prospectiva honesta: features pre-T1, outcome post-T1."""
    log.info("")
    log.info("=" * 78)
    log.info("PARTE 2 — Etiqueta temporal prospectiva (corte %s)", T1.date())
    log.info("=" * 78)

    dig = sha256(raw_path)
    reg("P2_datos", "SHA-256 raw", "OK" if dig == SHA_RAW else "DIFIERE",
        "OK" if dig == SHA_RAW else "DIFIERE")
    if dig != SHA_RAW:
        log.error("SHA distinto del anclado (%s)", SHA_RAW[:16])
        return

    df = pd.read_csv(raw_path, usecols=["person_id", "event", "timestamp"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True,
                                     format="mixed")
    reg("P2_datos", "eventos / usuarios",
        f"{len(df):,} / {df.person_id.nunique():,}")
    reg("P2_datos", "rango",
        f"{df.timestamp.min().date()} -> {df.timestamp.max().date()}")

    pre = df[df.timestamp < T1]
    post = df[df.timestamp >= T1]

    # Poblacion en riesgo: >= 1 evento antes de T1
    g = pre.groupby("person_id")
    feats = pd.DataFrame({
        "n_eventos": g.size(),
        "tipos_evento": g["event"].nunique(),
        "dias_activos": g["timestamp"].apply(
            lambda s: s.dt.normalize().nunique()),
        "eventos_creditos": g["event"].apply(
            lambda s: s.isin(["credits_used", "credits_exceeded"]).sum()),
        "eventos_agente": g["event"].apply(
            lambda s: s.str.startswith("agent_").sum()),
        "recencia_dias": (T1 - g["timestamp"].max()).dt.total_seconds() / 86400,
        "antiguedad_dias": (g["timestamp"].max() - g["timestamp"].min())
                           .dt.total_seconds() / 86400,
    })
    # velocidad: eventos por dia activo
    feats["velocidad"] = feats["n_eventos"] / feats["dias_activos"].clip(lower=1)

    activos_post = set(post.person_id.unique())
    feats["churned"] = (~feats.index.isin(activos_post)).astype(int)

    for etiqueta, d in (("principal (todos)", feats),
                        ("sensibilidad (antiguedad >= 7d)",
                         feats[feats.antiguedad_dias >= 7])):
        y = d["churned"].values
        if len(np.unique(y)) < 2:
            reg("P2_temporal", etiqueta, "una sola clase", "NO EVALUABLE")
            continue
        X = d.drop(columns=["churned"]).values
        base = y.mean()
        reg("P2_temporal", f"{etiqueta}: n / tasa churn 30d",
            f"{len(d):,} / {base:.1%}")
        m = gbm()
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        aucs = cross_val_score(m, X, y, cv=cv, scoring="roc_auc")
        reg("P2_temporal", f"{etiqueta}: GBM AUC CV 5-fold",
            f"{aucs.mean():.4f} +/- {aucs.std():.4f}")
        # Base simple: solo recencia
        auc_rec = roc_auc_score(y, d["recencia_dias"].values)
        reg("P2_temporal", f"{etiqueta}: AUC de SOLO recencia (dias sin actividad)",
            f"{auc_rec:.4f}")
        # Importancias
        Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                              random_state=42, stratify=y)
        m.fit(Xtr, ytr)
        imp = dict(zip(d.drop(columns=["churned"]).columns,
                       m.feature_importances_))
        top = sorted(imp.items(), key=lambda kv: -kv[1])[:3]
        reg("P2_temporal", f"{etiqueta}: top-3 importancia",
            "; ".join(f"{k} {v:.0%}" for k, v in top))

    reg("P2_caveats", "censura derecha",
        "el dato termina 2025-12-08; 'churned' pudo volver despues")
    reg("P2_caveats", "una sola ventana de 30d y un solo corte",
        "no es validacion temporal multiple")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=str(DEFAULT_RAW))
    args = ap.parse_args()

    log.info("=" * 78)
    log.info("VERIFICACION HACKEREARTH FRACTAL V3 — reporte del 2026-10-18")
    log.info("=" * 78)

    parte1()
    if os.path.exists(args.raw):
        parte2(args.raw)
    else:
        log.warning("Sin dataset crudo (%s): solo Parte 1", args.raw)

    DATA_RR.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["punto", "cifra", "valor",
                                           "estado"])
        w.writeheader()
        w.writerows(RESULTADOS)
    log.info("Salida: %s", OUT.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
