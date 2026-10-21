#!/usr/bin/env python3
"""
Follow-up npm — dos preguntas posteriores al test pre-registrado 2026-10-02.

POST-HOC, declarado: ninguna de las dos era hipotesis del pre-registro NPM
(`PREREGISTRO_NPM_2026-10-02.md`). La codificacion de friccion a priori se
incluyo alli "solo para describir la composicion de la cohorte y para que un
analisis futuro pueda retomarla" — este es ese analisis futuro.

P-A. ¿El hazard DECRECIENTE de npm (rho = -0.716, p = 0.013) es un artefacto
     de mezcla de cohortes? Estratifica el hazard por cohorte de nacimiento
     (nacimiento <= 2017 / 2018-2020 / >= 2021) y recalcula la forma dentro de
     cada estrato. Si la forma decreciente aparece dentro de cada cohorte, es
     robusta; si se aplana o invierte, era mezcla (las edades altas solo las
     alcanzan las cohortes viejas, supervivientes).

P-B. ¿La friccion a priori predice la forma de la caida (Delta)? Direccion
     anticipada en el propio pre-registro (mapa de modos): friccion alta ->
     caida suave; fricción ~0 + abrupto -> precipicio. Test: Spearman
     (friccion, delta_caida) + Kruskal-Wallis por grupo, con control por clase
     de disparador (la codificacion del disparador si fue pre-registrada como
     hipotesis P3).

Datos: `reconstruction_real/data/npm_cohorte_aco.csv.gz` (committeada, 450
paquetes con nacimiento, delta_caida, friccion_a_priori, disparador).

Uso:
    python reconstruction_real/code/npm_followup_cohorte_friccion.py
"""

import csv
import gzip
import logging
import sys
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
COHORTE = ROOT / "reconstruction_real" / "data" / "npm_cohorte_aco.csv.gz"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "npm_followup_cohorte_friccion_log.txt"

BANDA_MESES = 12
MIN_EN_RIESGO = 30

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("NPM-FOLLOWUP")

COHORTES_NAC = [("<=2017", lambda a: a <= 2017),
                ("2018-2020", lambda a: 2018 <= a <= 2020),
                (">=2021", lambda a: a >= 2021)]


def cargar():
    with gzip.open(COHORTE, "rt", encoding="utf-8") as fh:
        filas = list(csv.DictReader(fh))
    for f in filas:
        f["n_meses"] = int(f["n_meses"])
        f["edad_extincion_meses"] = (int(f["edad_extincion_meses"])
                                     if f["edad_extincion_meses"] else None)
        f["friccion_a_priori"] = int(f["friccion_a_priori"])
        f["delta_caida"] = float(f["delta_caida"])
        f["anio_nac"] = int(f["nacimiento"][:4])
    return filas


def hazard_bandas(sujetos):
    """Mismo calculo que punto1() de npm_pruebas_aco.py."""
    bandas, anos = [], 0
    while True:
        ini, fin = anos * BANDA_MESES, (anos + 1) * BANDA_MESES
        en_riesgo = sum(1 for edad, _ in sujetos if edad >= ini)
        if en_riesgo == 0:
            break
        fines = sum(1 for edad, ev in sujetos if ev and ini <= edad < fin)
        bandas.append({"banda_anos": anos, "en_riesgo": en_riesgo,
                       "fines": fines,
                       "hazard": fines / en_riesgo if en_riesgo else 0.0})
        anos += 1
    return bandas


def punto_a(filas):
    log.info("=" * 78)
    log.info("P-A. ¿Hazard decreciente = artefacto de mezcla de cohortes?")
    log.info("=" * 78)

    def sujetos_de(fs):
        out = []
        for f in fs:
            if f["edad_extincion_meses"] is not None:
                out.append((f["edad_extincion_meses"], True))
            else:
                out.append((f["n_meses"] - 1, False))
        return out

    # Referencia: agregado (debe reproducir el rho = -0.716 publicado)
    bandas = hazard_bandas(sujetos_de(filas))
    utiles = [b for b in bandas if b["en_riesgo"] >= MIN_EN_RIESGO]
    rho, p = stats.spearmanr([b["banda_anos"] for b in utiles],
                             [b["hazard"] for b in utiles])
    log.info("Agregado (referencia): rho(edad, hazard) = %+.3f (p = %.4f, "
             "%d bandas >= %d en riesgo) — publicado: -0.716, p = 0.013",
             rho, p, len(utiles), MIN_EN_RIESGO)

    # Estratificado por cohorte de nacimiento
    log.info("")
    for etiqueta, cond in COHORTES_NAC:
        fs = [f for f in filas if cond(f["anio_nac"])]
        sujetos = sujetos_de(fs)
        bandas_c = hazard_bandas(sujetos)
        utiles_c = [b for b in bandas_c if b["en_riesgo"] >= MIN_EN_RIESGO]
        if len(utiles_c) < 3:
            log.info("Cohorte %s: n=%d paquetes, %d bandas utiles — no evaluable",
                     etiqueta, len(fs), len(utiles_c))
            continue
        rho_c, p_c = stats.spearmanr([b["banda_anos"] for b in utiles_c],
                                     [b["hazard"] for b in utiles_c])
        detalle = ", ".join("a%d:%.3f(n=%d)" % (b["banda_anos"], b["hazard"],
                                                b["en_riesgo"])
                            for b in utiles_c)
        log.info("Cohorte %s: n=%d | rho(edad, hazard) = %+.3f (p 2 colas = "
                 "%.4f, %d bandas) | %s", etiqueta, len(fs), rho_c, p_c,
                 len(utiles_c), detalle)

    log.info("")
    log.info("Lectura: si el rho es negativo DENTRO de cada cohorte, la forma")
    log.info("decreciente no es mezcla; si se aplana/invierte, las edades")
    log.info("altas solo las alcanzan las cohortes viejas (supervivientes).")


def punto_b(filas):
    log.info("")
    log.info("=" * 78)
    log.info("P-B. Friccion a priori (0..3) vs delta_caida — n=450")
    log.info("=" * 78)
    log.info("POST-HOC declarado: en el pre-registro NPM la friccion era")
    log.info("'solo descriptiva'; la codificacion fue fijada antes de ver las")
    log.info("series (fundacion=3, corporativa=2, otra org=1, individual=0).")

    F = np.array([f["friccion_a_priori"] for f in filas], float)
    D = np.array([f["delta_caida"] for f in filas], float)
    rho, p = stats.spearmanr(F, D)
    log.info("")
    log.info("Spearman(friccion, delta_caida) = %+.3f | p 2 colas = %.4f | n = %d",
             rho, p, len(filas))

    grupos = {}
    for f in filas:
        grupos.setdefault(f["friccion_a_priori"], []).append(f["delta_caida"])
    log.info("Mediana de delta_caida por nivel de friccion:")
    for k in sorted(grupos):
        g = np.array(grupos[k])
        log.info("  friccion %d (n=%3d): mediana %+.3f [p25 %+.3f, p75 %+.3f]",
                 k, len(g), np.median(g), np.percentile(g, 25),
                 np.percentile(g, 75))
    if len(grupos) >= 3:
        muestras = [np.array(grupos[k]) for k in sorted(grupos) if len(grupos[k]) >= 5]
        if len(muestras) >= 3:
            H, pk = stats.kruskal(*muestras)
            log.info("Kruskal-Wallis entre niveles con n>=5: H = %.3f, p = %.4f",
                     H, pk)

    # Control por clase de disparador (codificacion pre-registrada, P3)
    log.info("")
    log.info("Control por clase de disparador:")
    for clase in ("abrupto", "anunciado", "sin_clasificar"):
        fs = [f for f in filas if f["disparador"] == clase]
        if len(fs) < 20:
            log.info("  %s: n=%d — insuficiente", clase, len(fs))
            continue
        Fc = np.array([f["friccion_a_priori"] for f in fs], float)
        Dc = np.array([f["delta_caida"] for f in fs], float)
        if len(set(Fc)) < 2:
            log.info("  %s: n=%d — friccion constante", clase, len(fs))
            continue
        rho_c, p_c = stats.spearmanr(Fc, Dc)
        log.info("  %s (n=%3d): rho = %+.3f (p = %.4f)", clase, len(fs),
                 rho_c, p_c)

    log.info("")
    log.info("Lectura: la direccion anticipada en el propio pre-registro era")
    log.info("friccion alta -> caida suave. El resultado es el que es; por ser")
    log.info("post-hoc no actualiza ningun criterio RC por si solo.")


def main():
    filas = cargar()
    log.info("Cohorte npm: %d paquetes (npm_cohorte_aco.csv.gz)", len(filas))
    punto_a(filas)
    punto_b(filas)
    return 0


if __name__ == "__main__":
    sys.exit(main())
