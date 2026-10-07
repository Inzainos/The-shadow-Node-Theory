"""RC1: el regimen superlineal b >= 1, regimen fisico o mala especificacion.

Pre-registro: reconstruction_real/preregistro/PREREGISTRO_RC1_SUPERLINEAL_2026-10-02.md
(commit 1a2ac0e, subido antes de escribir este archivo).

RC1 dice "la ley de potencia no ajusta mejor que lineal/exponencial en TODOS los
dominios" y figura NOT REFUTED sobre una sola prueba, la de las 18 series del ACO en la
auditoria v32: potencia 13/18, exponencial 4/18, lineal 1/18, con los ganadores de la
exponencial en b medio +1.541 contra +0.324 de los de potencia, y 3 de 4 superlineales
ajustando mejor como exponenciales. De ahi la sospecha de que la banda "Roche Radius"
de snt_utils.py etiquete como regimen fisico lo que es mala especificacion, sobre el
14.1% del corpus (102 de 721 casos).

REGLA POR DOMINIO (Axioma 0.1 y Axioma 2): cada dominio se prueba por separado con su
serie cruda y su propio proxy; RC1 es una afirmacion universal, asi que un
contraejemplo en un dominio la refuta; los resultados se cuentan por dominio y nunca se
agrupan; y NO se ordena nada entre dominios.

    P0. Compuerta. Simula desde una ley de potencia CONOCIDA con la sigma y la rho
        AR(1) de cada caso: todo lo que el AIC elija que no sea potencia es error por
        construccion. Un dominio se interpreta solo si ese error queda < 20% en la
        banda b >= 1.
    P1. Conteo de ganadores por dominio.
    P2. Spearman(b, dAIC_potencia) por dominio. Prediccion: negativa, una cola.
    P3. Fisher (b>=1) x (gana potencia) por dominio. Prediccion: OR < 1, una cola.
    P4. De los superlineales, que fraccion ajusta mejor con exponencial o lineal.
    P5. Tautologia. Simula desde una exponencial CONOCIDA y ajusta como potencia: si
        una exponencial verdadera produce b >= 1, la etiqueta es otro nombre para el
        desajuste.

Salidas:
    reconstruction_real/data/rc1_por_caso.csv
    reconstruction_real/data/rc1_calibracion.csv
    reconstruction_real/logs/rc1_superlineal_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/rc1_superlineal.py
"""

import csv
import logging
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
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
N_CAL = 200               # replicas de calibracion por caso (P0 y P5)
UMBRAL_ERROR = 0.20       # regla de admision del pre-registro, banda b >= 1
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


# ------------------------------------------------------------------ nucleo
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
    """234 paises, receta: acumulados, inicio en >= 100, 60 dias."""
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
    """446 pares de paises, como calc() de expand_B_massive.py."""
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
    """18 series del ACO. Advertencia: miden el exponente de ABSORCION."""
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
    rng = np.random.default_rng(SEMILLA)
    log.info("=" * 78)
    log.info("RC1 — REGIMEN SUPERLINEAL b >= 1 (pre-registro 2026-10-02, 1a2ac0e)")
    log.info("=" * 78)
    log.info("REGLA POR DOMINIO: cada dominio por separado, con su proxy y su")
    log.info("calibracion. RC1 es universal, asi que un contraejemplo la refuta.")
    log.info("Los resultados se CUENTAN por dominio y NO se agrupan ni se ordenan.")
    log.info("")

    log.info("Cargando y verificando reproduccion:")
    casos = []
    E3 = cargar_E3()
    mal = [c["id"] for c in E3
           if abs(ajuste_loglog(c["t"], c["y"])[0] - c["b_pub"]) > E3_TOL]
    log.info("   E3  : %3d casos | %3d/%d reproducen la b publicada (tol %.2f)",
             len(E3), len(E3) - len(mal), len(E3), E3_TOL)
    if len(mal) > 0.1 * len(E3):
        log.error("ALTO: mas del 10%% de E3 no reproduce. No se corre nada.")
        return 1
    casos += E3
    B = cargar_B()
    malB = [c["id"] for c in B
            if abs(ajuste_loglog(c["t"], c["y"])[0] - c["b_pub"]) > B_TOL]
    log.info("   B   : %3d casos | %3d/%d reproducen la b publicada (tol %g)",
             len(B), len(B) - len(malB), len(B), B_TOL)
    if malB:
        log.error("ALTO: %d casos de B no reproducen. No se corre nada.", len(malB))
        return 1
    casos += B
    A = cargar_ACO()
    log.info("   ACO : %3d casos (control; miden el exponente de ABSORCION)", len(A))
    casos += A
    log.info("")
    log.info("No testeables por falta de serie cruda: E1 (4 casos, los 4 "
             "superlineales), F2 (1), F3 (1). Se reportan, no se imputan.")

    # ---------------------------------------------------------- ajustes reales
    filas = []
    for c in casos:
        t, y = c["t"], c["y"]
        cm = comparar_modelos(t, y)
        b, a, sigma, rho, dw = perfil(t, y)
        c.update(b=b, log_a=a, sigma=sigma, rho=rho, cm=cm)
        filas.append({
            "dominio": c["dominio"], "id": c["id"], "etiqueta": c["etiqueta"],
            "n": len(t), "b": round(b, 4), "banda_b": banda_de(b),
            "superlineal": int(b >= 1.0), "dw": round(dw, 4),
            "rho_ar1": round(rho, 4), "sigma": round(sigma, 4),
            "aic_potencia": cm["aic"].get("potencia"),
            "aic_exponencial": cm["aic"].get("exponencial"),
            "aic_lineal": cm["aic"].get("lineal"),
            "ganador": cm["ganador"],
            "delta_aic_potencia": cm["delta_aic_potencia"],
        })

    # ---------------------------------------------------------------- P0 y P5
    log.info("")
    log.info("=" * 78)
    log.info("P0. COMPUERTA — ERROR DE SELECCION DEL AIC BAJO AUTOCORRELACION")
    log.info("=" * 78)
    log.info("Se simula desde una ley de potencia CONOCIDA (la b del caso) con la")
    log.info("sigma y la rho AR(1) del propio caso. Todo lo que el AIC elija que no")
    log.info("sea 'potencia' es error por construccion. %d replicas por caso.", N_CAL)
    cal = []
    admisible = {}
    for dom in ("E3", "B", "ACO"):
        grupo = [c for c in casos if c["dominio"] == dom]
        if not grupo:
            continue
        log.info("")
        log.info("%s — %d casos", dom, len(grupo))
        log.info("   %-16s %7s %14s %16s", "banda de b", "casos",
                 "error P0", "b aparente P5 >= 1")
        por_banda = defaultdict(lambda: {"n": 0, "err": 0, "tot": 0,
                                         "sup": 0, "stot": 0})
        for c in grupo:
            t = c["t"]; n = len(t)
            bd = banda_de(c["b"])
            e = ruido_ar1(n, c["sigma"], c["rho"], N_CAL, rng)
            # P0: potencia verdadera
            base = c["log_a"] + c["b"] * np.log(t)
            # P5: exponencial verdadera, con los parametros ajustados al caso
            de, ce = np.polyfit(t, np.log(c["y"]), 1)
            base_exp = ce + de * t
            d = por_banda[bd]
            d["n"] += 1
            for r in range(N_CAL):
                y0 = np.exp(base + e[r])
                if np.all(np.isfinite(y0)) and np.all(y0 > 0):
                    g = comparar_modelos(t, y0)["ganador"]
                    if g:
                        d["tot"] += 1
                        d["err"] += g != "potencia"
                y1 = np.exp(base_exp + e[r])
                if np.all(np.isfinite(y1)) and np.all(y1 > 0):
                    bb = ajuste_loglog(t, y1)[0]
                    d["stot"] += 1
                    d["sup"] += bb >= 1.0
        for _, _, nombre in BANDAS:
            d = por_banda.get(nombre)
            if not d or d["n"] == 0:
                continue
            err = d["err"] / d["tot"] if d["tot"] else float("nan")
            sup = d["sup"] / d["stot"] if d["stot"] else float("nan")
            log.info("   %-16s %7d %13.1f%% %15.1f%%", nombre, d["n"],
                     100 * err, 100 * sup)
            cal.append({"dominio": dom, "banda_b": nombre, "casos": d["n"],
                        "replicas": d["tot"],
                        "error_seleccion_P0": round(err, 4),
                        "frac_b_aparente_mayor_1_P5": round(sup, 4)})
        sup_n = sum(d["n"] for nb, d in por_banda.items() if "b >=" in nb
                    or "1.0 <=" in nb)
        sup_err = sum(d["err"] for nb, d in por_banda.items() if "b >=" in nb
                      or "1.0 <=" in nb)
        sup_tot = sum(d["tot"] for nb, d in por_banda.items() if "b >=" in nb
                      or "1.0 <=" in nb)
        tasa = sup_err / sup_tot if sup_tot else float("nan")
        ok = np.isfinite(tasa) and tasa < UMBRAL_ERROR
        admisible[dom] = ok
        log.info("   -> banda b >= 1 agregada: %d casos, error %.1f%% -> %s",
                 sup_n, 100 * tasa,
                 "ADMISIBLE" if ok else "NO INTERPRETABLE (umbral 20%)")
        cal.append({"dominio": dom, "banda_b": "b >= 1 (agregada)",
                    "casos": sup_n, "replicas": sup_tot,
                    "error_seleccion_P0": round(tasa, 4),
                    "admisible": int(ok)})

    with OUT_CAL.open("w", encoding="utf-8", newline="") as fh:
        cols = sorted({k for r in cal for k in r})
        cols = ["dominio", "banda_b"] + [c for c in cols
                                         if c not in ("dominio", "banda_b")]
        w = csv.DictWriter(fh, fieldnames=cols, restval="")
        w.writeheader()
        w.writerows(cal)

    # ------------------------------------------------------------ P1 a P4
    log.info("")
    log.info("=" * 78)
    log.info("P1 a P4. POR DOMINIO (solo se interpretan los admisibles en P0)")
    log.info("=" * 78)
    res = []
    for dom in ("E3", "B", "ACO"):
        f = [x for x in filas if x["dominio"] == dom]
        if not f:
            continue
        g = Counter(x["ganador"] for x in f)
        b = np.array([x["b"] for x in f])
        d = np.array([x["delta_aic_potencia"] for x in f], dtype=float)
        sup = b >= 1.0
        pot = np.array([x["ganador"] == "potencia" for x in f])
        log.info("")
        log.info("%s %s", dom, "" if admisible.get(dom) else "— NO INTERPRETABLE")
        log.info("   P1 ganadores: potencia %d/%d | exponencial %d | lineal %d",
                 g["potencia"], len(f), g["exponencial"], g["lineal"])
        rho_s, p_s = stats.spearmanr(b, d)
        p1c = p_s / 2 if rho_s < 0 else 1 - p_s / 2
        log.info("   P2 Spearman(b, dAIC) = %+.3f | p una cola = %.4f -> %s",
                 rho_s, p1c,
                 "a mayor b PEOR ajusta la potencia" if rho_s < 0 and p1c < ALFA
                 else "sin evidencia en la direccion predicha")
        tab = [[int(np.sum(sup & pot)), int(np.sum(sup & ~pot))],
               [int(np.sum(~sup & pot)), int(np.sum(~sup & ~pot))]]
        orr, p_f = stats.fisher_exact(tab, alternative="less")
        log.info("   P3 Fisher [b>=1: pot %d, otra %d][b<1: pot %d, otra %d] "
                 "OR = %.3f | p una cola = %.4f", tab[0][0], tab[0][1],
                 tab[1][0], tab[1][1], orr, p_f)
        if sup.sum():
            fr = float(np.mean(~pot[sup]))
            log.info("   P4 de los %d superlineales, %d (%.1f%%) ajustan mejor con "
                     "exponencial o lineal", int(sup.sum()),
                     int(np.sum(~pot[sup])), 100 * fr)
        else:
            fr = float("nan")
            log.info("   P4 sin casos superlineales en este dominio")
        res.append({"dominio": dom, "casos": len(f),
                    "admisible_P0": int(bool(admisible.get(dom))),
                    "gana_potencia": g["potencia"],
                    "gana_exponencial": g["exponencial"],
                    "gana_lineal": g["lineal"],
                    "superlineales": int(sup.sum()),
                    "spearman_b_dAIC": round(float(rho_s), 4),
                    "p_una_cola_P2": round(float(p1c), 5),
                    "fisher_OR_P3": round(float(orr), 4),
                    "p_una_cola_P3": round(float(p_f), 5),
                    "frac_superlineales_no_potencia_P4":
                        "" if not sup.sum() else round(fr, 4)})

    cols = list(filas[0].keys())
    with OUT_CASO.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, restval="")
        w.writeheader()
        w.writerows(filas)
    with OUT_CAL.open("a", encoding="utf-8", newline="") as fh:
        fh.write("\n")
    with (RR / "rc1_resumen.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(res[0].keys()))
        w.writeheader()
        w.writerows(res)

    log.info("")
    log.info("=" * 78)
    log.info("RESUMEN, POR DOMINIO Y SIN AGRUPAR")
    log.info("=" * 78)
    for r in res:
        log.info("%-5s admisible=%s | potencia %d/%d | superlineales %d | "
                 "P4 no-potencia %s", r["dominio"],
                 "si" if r["admisible_P0"] else "NO", r["gana_potencia"],
                 r["casos"], r["superlineales"],
                 r["frac_superlineales_no_potencia_P4"])
    log.info("Por caso     -> %s", OUT_CASO.relative_to(ROOT))
    log.info("Calibracion  -> %s", OUT_CAL.relative_to(ROOT))
    log.info("Resumen      -> %s", (RR / "rc1_resumen.csv").relative_to(ROOT))
    log.info("LOG          -> %s", LOG_FILE.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
