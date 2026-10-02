"""
Corre los tres puntos pre-registrados sobre la cohorte npm.

Pre-registro: reconstruction_real/preregistro/PREREGISTRO_NPM_2026-10-02.md
(commit 3ff9fca, subido antes de descargar cualquier dato de analisis).
Cohorte: reconstruction_real/data/npm_cohorte_aco.csv.gz (npm_cohorte_aco.py).

    P1. Hazard h(tau) > 0 y su forma, en bandas de edad de 1 ano.
    P2. Ortogonalidad b_subida ⊥ Delta_caida, por equivalencia con IC en +-0.3.
    P3. Disparador abrupto contra anunciado, emparejado por pico y edad al pico.

Salidas:
    reconstruction_real/data/npm_hazard_bandas.csv
    reconstruction_real/logs/npm_pruebas_aco_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/npm_pruebas_aco.py
"""

import csv
import gzip
import logging
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
COHORTE = ROOT / "reconstruction_real" / "data" / "npm_cohorte_aco.csv.gz"
BANDAS = ROOT / "reconstruction_real" / "data" / "npm_hazard_bandas.csv"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "npm_pruebas_aco_log.txt"

MIN_EN_RIESGO = 30          # minimo para que una banda cuente en H1a
BANDA_MESES = 12
EQUIV = 0.3                 # banda de equivalencia de la ortogonalidad
ALFA = 0.05

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("NPM-PRUEBAS")


def cargar():
    with gzip.open(COHORTE, "rt", encoding="utf-8") as fh:
        filas = list(csv.DictReader(fh))
    for f in filas:
        for c in ("pico_mensual", "n_meses", "edad_al_pico_meses", "n_subida",
                  "n_caida", "minimo_posterior", "deprecado",
                  "friccion_a_priori", "n_avisos"):
            f[c] = int(float(f[c]))
        for c in ("b_subida", "r2_subida", "delta_caida", "r2_caida",
                  "cvss_ventana"):
            f[c] = float(f[c])
        f["edad_extincion_meses"] = (int(f["edad_extincion_meses"])
                                     if f["edad_extincion_meses"] else None)
    log.info("Cohorte: %d paquetes", len(filas))
    return filas


def ic_fisher(rho, n):
    """Intervalo del 95% de Spearman por la transformacion de Fisher."""
    if n < 4:
        return (float("nan"), float("nan"))
    z = math.atanh(max(min(rho, 0.999999), -0.999999))
    se = 1.06 / math.sqrt(n - 3)          # correccion de Bonett-Wright
    return math.tanh(z - 1.96 * se), math.tanh(z + 1.96 * se)


# ------------------------------------------------------------------ P1
def punto1(filas):
    log.info("=" * 78)
    log.info("P1. HAZARD h(tau) > 0 Y SU FORMA")
    log.info("=" * 78)

    # Edad observada: hasta la extincion, o hasta el final de la serie.
    sujetos = []
    for f in filas:
        if f["edad_extincion_meses"] is not None:
            sujetos.append((f["edad_extincion_meses"], True))
        else:
            sujetos.append((f["n_meses"] - 1, False))

    bandas, anos = [], 0
    while True:
        ini, fin = anos * BANDA_MESES, (anos + 1) * BANDA_MESES
        en_riesgo = sum(1 for edad, _ in sujetos if edad >= ini)
        if en_riesgo == 0:
            break
        fines = sum(1 for edad, ev in sujetos if ev and ini <= edad < fin)
        bandas.append({"banda_anos": anos, "edad_meses_ini": ini,
                       "en_riesgo": en_riesgo, "fines": fines,
                       "hazard": round(fines / en_riesgo, 6)})
        anos += 1

    log.info("%-6s %10s %7s %9s", "banda", "en_riesgo", "fines", "hazard")
    for b in bandas:
        log.info("%-6d %10d %7d %9.4f", b["banda_anos"], b["en_riesgo"],
                 b["fines"], b["hazard"])

    utiles = [b for b in bandas if b["en_riesgo"] >= MIN_EN_RIESGO]
    sin_fines = [b for b in utiles if b["fines"] == 0]
    log.info("")
    log.info("H1a positividad: %d/%d bandas con >= %d en riesgo tienen fines",
             len(utiles) - len(sin_fines), len(utiles), MIN_EN_RIESGO)
    for b in sin_fines:
        cota = 3 / b["en_riesgo"]
        log.info("   banda %d sin fines (n=%d, cota superior 3/n = %.4f)",
                 b["banda_anos"], b["en_riesgo"], cota)
    h1a = "RESPALDADA" if not sin_fines else "NO RESPALDADA"
    log.info("H1a -> %s", h1a)

    log.info("")
    if len(utiles) >= 3:
        x = [b["banda_anos"] for b in utiles]
        y = [b["hazard"] for b in utiles]
        rho, p2 = stats.spearmanr(x, y)
        p1c = p2 / 2 if rho > 0 else 1 - p2 / 2
        log.info("H1b forma: Spearman(edad, hazard) = %+.3f | p 1 cola = %.4f "
                 "| p 2 colas = %.4f | n = %d bandas", rho, p1c, p2, len(utiles))
        h1b = "RESPALDADA" if (rho > 0 and p1c < ALFA) else "NO RESPALDADA"
    else:
        rho, p1c, h1b = float("nan"), float("nan"), "NO EVALUABLE"
        log.info("H1b forma: solo %d bandas utiles, no evaluable", len(utiles))
    log.info("H1b -> %s", h1b)
    log.info("   (cripto: creciente, confundido con el calendario; "
             "bancos FDIC: bañera, no respaldada)")

    # Confusion edad/calendario, declarada en el pre-registro.
    cal = Counter(f["mes_extincion"][:4] for f in filas if f["mes_extincion"])
    log.info("")
    log.info("Ano calendario de las %d extinciones: %s",
             sum(cal.values()), ", ".join(f"{a}:{n}" for a, n in sorted(cal.items())))

    with BANDAS.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(bandas[0].keys()))
        w.writeheader()
        w.writerows(bandas)
    log.info("Bandas -> %s", BANDAS.relative_to(ROOT))
    return {"h1a": h1a, "h1b": h1b, "rho_forma": rho, "p_forma": p1c,
            "bandas_utiles": len(utiles), "extinciones": sum(cal.values())}


# ------------------------------------------------------------------ P2
def punto2(filas):
    log.info("")
    log.info("=" * 78)
    log.info("P2. ORTOGONALIDAD b_subida ⊥ Delta_caida")
    log.info("=" * 78)

    b = np.array([f["b_subida"] for f in filas])
    d = np.array([f["delta_caida"] for f in filas])
    n = len(b)
    rho, p = stats.spearmanr(b, d)
    lo, hi = ic_fisher(rho, n)
    r_p, p_p = stats.pearsonr(b, d)

    log.info("n = %d pares", n)
    log.info("b_subida:    mediana %+.3f | rango [%+.3f, %+.3f]",
             float(np.median(b)), float(b.min()), float(b.max()))
    log.info("Delta_caida: mediana %+.3f | rango [%+.3f, %+.3f]",
             float(np.median(d)), float(d.min()), float(d.max()))
    log.info("Spearman rho = %+.3f (p = %.4f) | IC 95%% [%+.3f, %+.3f]",
             rho, p, lo, hi)
    log.info("Pearson  r   = %+.3f (p = %.4f)", r_p, p_p)

    if lo >= -EQUIV and hi <= EQUIV:
        dec = "RESPALDADA (equivalencia: el IC cae dentro de ±0.3)"
    elif abs(rho) >= EQUIV and p < ALFA:
        dec = "REFUTADA (|rho| >= 0.3 con p < 0.05)"
    else:
        dec = "INDETERMINADA (el IC se sale de ±0.3 sin alcanzar refutacion)"
    log.info("H2 -> %s", dec)

    # Secundaria: parcial controlando el tamano (log10 del pico).
    t = np.log10([max(f["pico_mensual"], 1) for f in filas])
    rb = stats.rankdata(b)
    rd = stats.rankdata(d)
    rt = stats.rankdata(t)
    rbt = np.corrcoef(rb, rt)[0, 1]
    rdt = np.corrcoef(rd, rt)[0, 1]
    rbd = np.corrcoef(rb, rd)[0, 1]
    den = math.sqrt((1 - rbt ** 2) * (1 - rdt ** 2))
    parcial = (rbd - rbt * rdt) / den if den > 0 else float("nan")
    log.info("Secundaria: Spearman parcial controlando log10(pico) = %+.3f",
             parcial)
    log.info("   (cripto, 242 pares: rho = -0.119, IC [-0.241, +0.007], "
             "RESPALDADA)")
    return {"n": n, "rho": rho, "ic": (lo, hi), "decision": dec,
            "parcial": parcial}


# ------------------------------------------------------------------ P3
def punto3(filas):
    log.info("")
    log.info("=" * 78)
    log.info("P3. MODOS DE COLAPSO: DISPARADOR ABRUPTO CONTRA ANUNCIADO")
    log.info("=" * 78)

    clases = Counter(f["disparador"] for f in filas)
    log.info("Clases: %d abruptos, %d anunciados, %d sin clasificar",
             clases["abrupto"], clases["anunciado"], clases["sin_clasificar"])

    abr = [f for f in filas if f["disparador"] == "abrupto"]
    anu = [f for f in filas if f["disparador"] == "anunciado"]

    if len(abr) < 3:
        log.warning("")
        log.warning("H3 -> NO EVALUABLE. La regla pre-registrada de disparador "
                    "abrupto (aviso OSV con CVSS >= 7.0 en la ventana "
                    "[pico-3, pico+6] meses) selecciona %d caso(s) en esta "
                    "cohorte; el emparejamiento 1:1 y la prueba de Wilcoxon "
                    "necesitan un n que no existe.", len(abr))
        log.warning("No se sustituye la regla ni se amplia la ventana: seria "
                    "elegir el criterio despues de ver los datos.")
        res = {"decision": "NO EVALUABLE", "n_abruptos": len(abr),
               "n_anunciados": len(anu)}
    else:
        res = {"decision": "PENDIENTE", "n_abruptos": len(abr),
               "n_anunciados": len(anu)}

    # Secundaria (b): descriptivo del ajuste de potencia por clase.
    log.info("")
    log.info("Secundaria (descriptivo): Delta y R2 de la caida por clase")
    log.info("%-16s %6s %12s %12s", "clase", "n", "Delta mediana", "R2 mediano")
    for nombre, grupo in (("abrupto", abr), ("anunciado", anu),
                          ("sin_clasificar",
                           [f for f in filas
                            if f["disparador"] == "sin_clasificar"])):
        if grupo:
            log.info("%-16s %6d %12.3f %12.3f", nombre, len(grupo),
                     float(np.median([f["delta_caida"] for f in grupo])),
                     float(np.median([f["r2_caida"] for f in grupo])))

    # Secundaria (c): candidatos a "Detenido en Piso".
    piso = [f for f in filas
            if f["minimo_posterior"] >= 0.01 * f["pico_mensual"]]
    log.info("")
    log.info("Secundaria: %d/%d paquetes (%.1f%%) tienen el minimo posterior "
             "por encima del 1%% del pico (candidatos a Detenido en Piso)",
             len(piso), len(filas), 100 * len(piso) / len(filas))
    res["piso"] = len(piso)
    return res


# ------------------------------------------------------------------ main
def main():
    log.info("=" * 78)
    log.info("PRUEBAS PRE-REGISTRADAS npm — pre-registro 2026-10-02 (3ff9fca)")
    log.info("=" * 78)
    filas = cargar()

    comp = Counter(f["friccion_a_priori"] for f in filas)
    log.info("Composicion por friccion a priori (solo descriptivo): "
             "nula %d, baja %d, media %d, alta %d",
             comp[0], comp[1], comp[2], comp[3])

    r1 = punto1(filas)
    r2 = punto2(filas)
    r3 = punto3(filas)

    log.info("")
    log.info("=" * 78)
    log.info("RESUMEN")
    log.info("=" * 78)
    log.info("P1 H1a positividad h(tau) > 0      -> %s", r1["h1a"])
    log.info("P1 H1b el hazard crece con la edad -> %s", r1["h1b"])
    log.info("P2 ortogonalidad b ⊥ Delta         -> %s", r2["decision"])
    log.info("P3 abrupto contra anunciado        -> %s", r3["decision"])
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
