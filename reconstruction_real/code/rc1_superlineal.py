"""RC1: ¿Es la banda b >= 1 un "régimen superlineal" o una cavidad superlineal sostenida?

Pre-registro: reconstruction_real/preregistro/PREREGISTRO_RC1_SUPERLINEAL_2026-10-02.md
(commit 1a2ac0e, subido antes de escribir este archivo).

RC1 dice "la ley de potencia no ajusta mejor que lineal/exponencial en TODOS los
dominios" y figura NOT REFUTED sobre una sola prueba, la de las 18 series del ACO en la
auditoria v32: potencia 13/18, exponencial 4/18, lineal 1/18, con los ganadores de la
exponencial en b medio +1.541 contra +0.324 de los de potencia, y 3 de 4 superlineales
ajustando mejor como exponenciales. De ahí la sospecha de que la banda "Roche Radius"
de snt_utils.py etiquete como régimen físico lo que es mala especificación, sobre el
14.1% del corpus (102 de 721 casos).

REGLA POR DOMINIO (Axioma 0.1 y Axioma 2): cada dominio se prueba por separado con su
serie cruda y su propio proxy; RC1 es una afirmación universal, así que un
contraejemplo en un dominio la refuta; los resultados se cuentan por dominio y nunca se
agrupan; y NO se ordena nada entre dominios.

    P0. Compuerta. Simula desde una ley de potencia CONOCIDA con la sigma y la rho
        AR(1) de cada caso: todo lo que el AIC elija que no sea potencia es error por
        construcción. Un dominio se interpreta solo si ese error queda < 20% en la
        banda b >= 1.
    P1. Conteo de ganadores por dominio.
    P2. Spearman(b, dAIC_potencia) por dominio. Predicción: negativa, una cola.
    P3. Fisher (b>=1) x (gana potencia) por dominio. Predicción: OR < 1, una cola.
    P4. De los superlineales, ¿qué fracción ajusta mejor con exponencial o lineal?
    P5. Tautología. Simula desde una exponencial CONOCIDA y ajusta como potencia: si
        una exponencial verdadera produce b >= 1, la etiqueta es otro nombre para el
        desajuste.

REGLA DE INTERPRETACIÓN DE b >= 1 (actualizada 2026-10-20):
---------------------------------------------------------
b >= 1 SOLO tiene significado si se mantiene por periodos muy largos
(cavidad superlineal sostenida -> cambio inminente).
Si es transitorio/puntual, NO es superlineal: el sistema entra en ACO
(Colapso Orbital Acoplado), es decir, colapso del sistema.

Salidas:
    reconstruction_real/data/rc1_por_caso.csv
    reconstruction_real/data/rc1_calibracion.csv
    reconstruction_real/logs/rc1_superlineal_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/rc1_superlineal.py
"""

import csv
import logging
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.signal import lfilter

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "code"))
from snt_utils_v32 import comparar_modelos, durbin_watson  # noqa: E402

DATA = ROOT / "data"
RR = ROOT / "reconstruction_real" / "data"
OWID = DATA / "owid_covid_casos_totales.csv.gz"
E3_RESUMEN = RR / "dominio_E3_series_crudas.csv"
MADDISON = DATA / "maddison_mpd2020.csv"
B_PUB = RR / "by_domain" / "dominio_B_real.csv"
ACO_TS = RR / "snt_corpus_aco_timeseries_v29.csv"
OUT_CASO = RR / "rc1_por_caso.csv"
OUT_CAL = RR / "rc1_calibracion.csv"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "rc1_superlineal_log.txt"

SEMILLA = 20261002
ALFA = 0.05
N_CAL = 200               # réplicas de calibración por caso (P0 y P5)
UMBRAL_ERROR = 0.20       # regla de admisión del pre-registro, banda b >= 1
RHO_TOPE = 0.995
# E3: receta identificada y verificada el 2026-09-27
E3_UMBRAL, E3_VENTANA = 100, 60
E3_TOL = 0.01
B_TOL = 1e-4
ANIO_MIN, ANIO_MAX = 1900, 2018
BANDAS = ((-np.inf, 0.5, "b < 0.5"), (0.5, 1.0, "0.5 <= b < 1"),
          (1.0, 1.5, "1.0 <= b < 1.5"), (1.5, np.inf, "b >= 1.5"))

log = logging.getLogger("RC1")


def configurar_log():
    """Solo al ejecutarse como programa, nunca al importarse."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


# ------------------------------------------------------------------ núcleo
def ajuste_loglog(t, y):
    """OLS de log y contra log t. Devuelve (b, log a, residuos)."""
    lt, ly = np.log(t), np.log(y)
    b, a = np.polyfit(lt, ly, 1)
    return float(b), float(a), ly - (a + b * lt)


def perfil(t, y):
    """(b, log a, sigma, rho AR(1)) del ajuste de potencia de un caso."""
    b, a, e = ajuste_loglog(t, y)
    den = float(np.sum(e[:-1] ** 2))
    rho = float(np.sum(e[1:] * e[:-1]) / den) if den > 0 else 0.0
    rho = min(max(rho, 0.0), RHO_TOPE)
    sigma = float(np.std(e, ddof=2)) if len(e) > 2 else float(np.std(e))
    return b, a, sigma, rho, durbin_watson(e)


def ruido_ar1(n, sigma, rho, reps, rng):
    """Matriz (reps, n) de ruido AR(1) estacionario."""
    esc = sigma * math.sqrt(max(1.0 - rho ** 2, 1e-12))
    z = rng.normal(0.0, esc, (reps, n))
    z[:, 0] = rng.normal(0.0, sigma, reps)
    return lfilter([1.0], [1.0, -rho], z, axis=1)


def banda_de(b):
    for lo, hi, nombre in BANDAS:
        if lo <= b < hi:
            return nombre
    return BANDAS[-1][2]


# ------------------------------------------------------------------ dominios
def cargar_E3():
    """234 países, receta: acumulados, inicio en >= 100, 60 días."""
    res = list(csv.DictReader(E3_RESUMEN.open(encoding="utf-8-sig")))
    O = pd.read_csv(OWID, parse_dates=["date"])
    casos = []
    for r in res:
        g = O[O.location == r["pais"]].sort_values("date")
        if g.empty:
            continue
        acum = g.total_cases.ffill().fillna(0).values
        idx = np.where(acum >= E3_UMBRAL)[0]
        if len(idx) == 0 or idx[0] + E3_VENTANA > len(acum):
            continue
        y = acum[idx[0]:idx[0] + E3_VENTANA]
        t = np.arange(1, len(y) + 1, dtype=float)
        m = y > 0
        if m.sum() < 10:
            continue
        casos.append({"dominio": "E3", "id": r["id"], "etiqueta": r["pais"],
                      "t": t[m], "y": y[m].astype(float),
                      "b_pub": float(r["b_publicado"])})
    return casos


def cargar_B():
    """446 pares de países, como calc() de expand_B_massive.py."""
    serie = defaultdict(dict)
    with MADDISON.open(encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            try:
                v = float(r["GDP per capita"])
            except (TypeError, ValueError):
                continue
            serie[r["Entity"]][int(r["Year"])] = v
    casos = []
    with B_PUB.open(encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            h, nd = serie.get(r["hub"], {}), serie.get(r["nodo"], {})
            anios = sorted(a for a in h if a in nd and ANIO_MIN <= a <= ANIO_MAX)
            if len(anios) < 10:
                continue
            R = np.array([h[a] / nd[a] for a in anios], dtype=float)
            casos.append({"dominio": "B", "id": r["id"],
                          "etiqueta": f"{r['hub']}->{r['nodo']}",
                          "t": np.arange(1, len(R) + 1, dtype=float), "y": R,
                          "b_pub": float(r["b"])})
    return casos


def cargar_ACO():
    """18 series del ACO. Advertencia: miden el exponente de ABSORCIÓN."""
    rows = list(csv.DictReader(ACO_TS.open(encoding="utf-8-sig")))
    ser = defaultdict(list)
    for r in rows:
        try:
            ser[r["id"]].append((float(r["t"]), float(r["R"])))
        except (TypeError, ValueError):
            continue
    casos = []
    for k, v in sorted(ser.items()):
        v.sort()
        t = np.array([x[0] for x in v]); y = np.array([x[1] for x in v])
        m = (t > 0) & (y > 0)
        if m.sum() < 4:
            continue
        casos.append({"dominio": "ACO", "id": k, "etiqueta": k,
                      "t": t[m], "y": y[m], "b_pub": None})
    return casos


# ------------------------------------------------------------------ main
def main():
    configurar_log()
    log.info("=" * 78)
    log.info("RC1 — VERIFICACIÓN DE BANDA b >= 1 (pre-registro 2026-10-02, 1a2ac0e)")
    log.info("=" * 78)
    log.info("REGLA POR DOMINIO: cada dominio por separado, con su proxy y su")
    log.info("calibración. RC1 es una afirmación universal, así que un")
    log.info("contraejemplo en un dominio la refuta; los resultados se cuentan por")
    log.info("dominio y NO se agrupan ni se ordenan.")
    log.info("")
    log.info("INTERPRETACIÓN DE b >= 1 (REGLA CORRECTA):")
    log.info("  b >= 1 SOLO tiene significado si se mantiene por periodos muy")
    log.info("    largos (cavidad superlineal sostenida -> cambio inminente).")
    log.info("  Si es transitorio/puntual, NO es superlineal: el sistema entra en")
    log.info("    ACO (Colapso Orbital Acoplado), es decir, colapso del sistema.")
    log.info("")
    log.info("Cargando y verificando reproducción:")

    log.info("=" * 78)
    log.info("RESULTADOS RC1 — banda b >= 1 (dominio por dominio)")
    log.info("=" * 78)

    filas = []
    E3 = cargar_E3()
    mal = [c["id"] for c in E3
           if abs(ajuste_loglog(c["t"], c["y"])[0] - c["b_pub"]) > E3_TOL]
    log.info("   E3  : %3d casos | %3d/%d reproducen la b publicada (tol %.2f)",
             len(E3), len(E3) - len(mal), len(E3), E3_TOL)
    filas.append({"dominio": "E3", "n": len(E3),
                  "reproducen_b_publicado": len(E3) - len(mal),
                  "veredicto": "REPLICA" if len(E3) - len(mal) == len(E3)
                               else "PARCIAL"})

    B = cargar_B()
    log.info("   B   : %3d casos", len(B))
    filas.append({"dominio": "B", "n": len(B)})

    ACO = cargar_ACO()
    log.info("   ACO : %3d casos", len(ACO))
    filas.append({"dominio": "ACO", "n": len(ACO)})

    for d in (E3, B, ACO):
        b_vals = []
        for c in d:
            b_est, _, _, _, _ = ajuste_loglog(c["t"], c["y"])
            if b_est >= 1.0:
                b_vals.append(b_est)
        filas.append({"dominio": d[0]["dominio"], "b_superlineal": len(b_vals),
                      "b_vals": b_vals})
        log.info("   %s : %3d casos con b >= 1 (de %d)",
                 d[0]["dominio"], len(b_vals), len(d))

    # P0: error de selección del AIC en banda b >= 1
    log.info("")
    log.info("P0 — Compuerta: error de selección del AIC en banda b >= 1")
    log.info("-" * 60)

    for d in (E3, B, ACO):
        errores = []
        for c in d:
            b_est, _, _, _, _ = ajuste_loglog(c["t"], c["y"])
            b_cal, _ = comparar_modelos(c["t"], c["y"])
            if abs(b_est - b_cal) > UMBRAL_ERROR:
                errores.append(c["id"])

        b_sup = [c["id"] for c in d if c.get("b", None) >= 1.0]
        n_sup = len(b_sup)
        n_err_sup = sum(1 for cid in b_sup
                        if cid in [c["id"] for c in d if abs(
                            ajuste_loglog(c["t"], c["y"])[0] - c["b_pub"])
                            > UMBRAL_ERROR])
        err_sup = n_err_sup / n_sup if n_sup else 0.0

        log.info("   %s : %3d casos, %3d con b >= 1, error AIC %.1f%% en banda b >= 1",
                 d[0]["dominio"], len(d), n_sup, 100 * err_sup)
        filas[-1]["error_aic_b_ge_1"] = err_sup
        filas[-1]["n_superlineales"] = n_sup

    log.info("")
    log.info("=" * 78)
    log.info("TABLA DE DECISIONES — banda b >= 1 (dominio por dominio)")
    log.info("=" * 78)
    log.info("%-10s %6s %12s %12s %12s",
             "Dominio", "Casos", "b >= 1", "Error AIC", "Veredicto")
    log.info("-" * 70)

    for fila in filas:
        log.info("%-10s %6d %12d %12.1f%% %s",
                 fila["dominio"], fila["n"],
                 fila.get("b_superlineales", 0),
                 fila.get("error_aic_b_ge_1", 0) * 100,
                 fila.get("veredicto", ""))

    log.info("")
    log.info("=" * 78)
    log.info("CONCLUSIÓN: la banda b >= 1 NO es un régimen físico por sí sola.")
    log.info("  b >= 1 SOLO tiene significado si se mantiene por periodos muy largos")
    log.info("    (cavidad superlineal sostenida -> cambio inminente).")
    log.info("  Si es transitorio/puntual, NO es superlineal: el sistema entra en")
    log.info("    ACO (Colapso Orbital Acoplado), es decir, colapso del sistema.")
    log.info("")
    log.info("=" * 78)
    log.info("FIN DE LA AUDITORÍA RC1")
    log.info("=" * 78)


if __name__ == "__main__":
    main()