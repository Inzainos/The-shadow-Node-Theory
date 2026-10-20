"""Recalibracion de alta precision del valor puntual del Dominio B.

Adenda: reconstruction_real/preregistro/ADENDA_RECALIBRACION_DOMINIO_B_2026-10-03.md
(subida antes de correr este script).

Cierra —o tumba— la primera de las tres reservas con las que quedo el cierre del
valor puntual el 2026-10-03. `ar1_inf` midio 7.1% de falso positivo contra un
techo de banda de 7.5%, con un IC95 de Wilson [5.5%, 9.2%] que la rebasa. Con
N_SIM = 2,000 el error Monte Carlo (+-1.9 puntos) es del mismo orden que el ancho
de la banda (5 puntos), asi que la admisibilidad la decidia el ruido de la
simulacion y no el metodo.

Esto no es una hipotesis nueva: es la misma cantidad, el mismo estimador y la
misma regla, con menos error. La banda [0.025, 0.075] NO se toca.

    Tamano (b = 0):   N = 200,000  -> estrato estimable ~70,000
    Poder:            N =  20,000  en b = -0.30 y b = -0.60
    Semilla:          20261003, declarada en la adenda
    Estratificacion:  por el caso REAL de origen (la corregida en 68e7ec3)

Los doce metodos se importan de dominio_B_valor_puntual.py en vez de copiarse,
para que no puedan divergir. Ese script y sus salidas NO se tocan.

Salidas:
    reconstruction_real/data/dominio_B_recalibracion.csv
    reconstruction_real/logs/dominio_B_recalibracion_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/dominio_B_recalibracion.py
"""

import csv
import logging
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

import dominio_B_valor_puntual as D          # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "reconstruction_real" / "data" / "dominio_B_recalibracion.csv"
CAL_2K = ROOT / "reconstruction_real" / "data" / "dominio_B_calibracion.csv"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "dominio_B_recalibracion_log.txt"

SEMILLA = 20261003
N_TAMANO = 200_000
N_PODER = 20_000
B_PODER = D.B_PODER                  # (-0.30, -0.60), del pre-registro base
BOOT_SIM = D.BOOT_SIM                # 199, sin cambio
ALFA = D.ALFA
SIZE_MIN, SIZE_MAX = D.SIZE_MIN, D.SIZE_MAX     # [0.025, 0.075], sin cambio
PASO_LOG = 20_000

log = logging.getLogger("RECAL")


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


def wilson(exitos, n, z=1.959964):
    """IC de Wilson al 95% para una proporcion. (nan, nan) si n = 0."""
    if n <= 0:
        return float("nan"), float("nan")
    p = exitos / n
    centro = p + z * z / (2 * n)
    radio = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    den = 1 + z * z / n
    return (centro - radio) / den, (centro + radio) / den


def perfiles_reales(casos):
    """(n, rho, sigma, el caso real de origen es estimable) por caso."""
    perfiles = []
    for c in casos:
        b, _, e, _ = D.ols(c["x"], c["y"])
        n = len(c["x"])
        rho = D.rho_de_dw(D.durbin_watson(e))
        perfiles.append((n, rho, float(np.std(e, ddof=2)),
                         D.n_efectivo(n, rho) >= 3.0))
    return perfiles


def serie_sintetica(n, rho, sigma, b_true, rng):
    """log R = b*log t + AR(1), con el arranque estacionario del script base."""
    e = np.empty(n)
    e[0] = rng.normal(0.0, sigma)
    ruido = rng.normal(0.0, sigma * math.sqrt(1.0 - rho ** 2), n - 1)
    for k in range(1, n):
        e[k] = rho * e[k - 1] + ruido[k - 1]
    x = np.log(np.arange(1, n + 1, dtype=float))
    return x, b_true * x + e


def escenario(etiqueta, b_true, n_sim, perfiles, rng):
    """Cuenta rechazos por metodo, en total y en el estrato estimable."""
    rech_tot = {m: 0 for m in D.NOMBRES}
    rech_est = {m: 0 for m in D.NOMBRES}
    eval_tot = {m: 0 for m in D.NOMBRES}
    eval_est = {m: 0 for m in D.NOMBRES}
    n_est = 0
    for i in range(n_sim):
        n, rho, sigma, fuente_estimable = perfiles[
            rng.integers(0, len(perfiles))]
        x, y = serie_sintetica(n, rho, sigma, b_true, rng)
        ps = D.todos_los_p(x, y, BOOT_SIM, rng)
        n_est += fuente_estimable
        for m in D.NOMBRES:
            p = ps.get(m)
            if p is None:
                continue
            eval_tot[m] += 1
            rech_tot[m] += p < ALFA
            if fuente_estimable:
                eval_est[m] += 1
                rech_est[m] += p < ALFA
        if (i + 1) % PASO_LOG == 0:
            log.info("   %s — %d / %d simulaciones (%.0f%%)", etiqueta, i + 1,
                     n_sim, 100 * (i + 1) / n_sim)
    log.info("%s — estimables por el caso REAL de origen: %d/%d (%.1f%%)",
             etiqueta, n_est, n_sim, 100 * n_est / n_sim)
    return rech_tot, eval_tot, rech_est, eval_est, n_est


def tasas_de_2k():
    """Tasas del estrato estimable de la corrida pre-registrada de 2,000."""
    if not CAL_2K.exists():
        return {}
    with CAL_2K.open(newline="", encoding="utf-8") as fh:
        return {(r["escenario"], r["metodo"]): r for r in csv.DictReader(fh)}


def main():
    configurar_log()
    rng = np.random.default_rng(SEMILLA)
    log.info("=" * 78)
    log.info("DOMINIO B — RECALIBRACION DE ALTA PRECISION")
    log.info("Adenda: preregistro/ADENDA_RECALIBRACION_DOMINIO_B_2026-10-03.md")
    log.info("=" * 78)
    log.info("Semilla %d | tamano N=%d | poder N=%d | BOOT_SIM=%d",
             SEMILLA, N_TAMANO, N_PODER, BOOT_SIM)
    log.info("Banda de admision [%.3f, %.3f] — SIN CAMBIO respecto al "
             "pre-registro base.", SIZE_MIN, SIZE_MAX)
    log.info("El estrato lo fija el caso REAL de origen, no la realizacion "
             "simulada (correccion de 68e7ec3).")

    casos = D.cargar_series()
    log.info("Series reconstruidas: %d casos", len(casos))
    perfiles = perfiles_reales(casos)
    n_est_real = sum(1 for p in perfiles if p[3])
    log.info("Estimables en los datos reales: %d/%d (%.1f%%)",
             n_est_real, len(perfiles), 100 * n_est_real / len(perfiles))

    previo = tasas_de_2k()
    filas = []
    tasas_tamano = {}

    for etq, b_true, n_sim in (("tamano (b = 0)", 0.0, N_TAMANO),
                               ("poder (b = %.2f)" % B_PODER[0], B_PODER[0],
                                N_PODER),
                               ("poder (b = %.2f)" % B_PODER[1], B_PODER[1],
                                N_PODER)):
        log.info("")
        log.info("=" * 78)
        log.info("ESCENARIO %s — %d simulaciones", etq, n_sim)
        log.info("=" * 78)
        rt, et, re_, ee, n_est = escenario(etq, b_true, n_sim, perfiles, rng)
        log.info("%-11s %9s %9s %18s %11s", "metodo", "tasa est.", "n est.",
                 "IC95 Wilson", "tasa 2,000")
        for m in D.NOMBRES:
            lo, hi = wilson(re_[m], ee[m])
            t = re_[m] / ee[m] if ee[m] else float("nan")
            ant = previo.get((etq, m))
            t_ant = float(ant["tasa_estimables"]) if ant else float("nan")
            log.info("%-11s %8.2f%% %9d   [%6.2f%%, %6.2f%%] %10.1f%%",
                     m, 100 * t, ee[m], 100 * lo, 100 * hi, 100 * t_ant)
            if etq.startswith("tamano"):
                tasas_tamano[m] = (t, lo, hi, ee[m])
            filas.append({
                "escenario": etq, "b_verdadera": b_true, "metodo": m,
                "n_sim": n_sim,
                "tasa_total": round(rt[m] / et[m], 6) if et[m] else "",
                "n_evaluables_total": et[m],
                "tasa_estimables": round(t, 6) if ee[m] else "",
                "n_evaluables_estimables": ee[m],
                "ic95_lo": round(lo, 6), "ic95_hi": round(hi, 6),
                "tasa_estimables_2000": round(t_ant, 6) if ant else "",
                "n_estrato_simulado": n_est,
            })

    # ------------------------------------------------- regla de admision
    log.info("")
    log.info("=" * 78)
    log.info("REGLA DE ADMISION — tasa medida en el estrato estimable dentro "
             "de [%.3f, %.3f]", SIZE_MIN, SIZE_MAX)
    log.info("=" * 78)
    admisibles, contenidos = [], []
    for m in D.NOMBRES:
        t, lo, hi, n_e = tasas_tamano[m]
        dentro = SIZE_MIN <= t <= SIZE_MAX
        ic_dentro = dentro and lo >= SIZE_MIN and hi <= SIZE_MAX
        if dentro:
            admisibles.append(m)
        if ic_dentro:
            contenidos.append(m)
        log.info("%-11s tasa %7.3f%%  IC95 [%6.3f%%, %6.3f%%]  ->  %s%s",
                 m, 100 * t, 100 * lo, 100 * hi,
                 "ADMISIBLE" if dentro else "no admisible",
                 ", IC95 contenido en la banda" if ic_dentro else
                 (", IC95 rebasa la banda" if dentro else ""))

    for f in filas:
        f["admisible"] = int(f["metodo"] in admisibles)
        f["ic95_contenido"] = int(f["metodo"] in contenidos)

    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)

    # -------------------------------- confirmacion sobre los datos reales
    log.info("")
    log.info("=" * 78)
    log.info("CONFIRMACION SOBRE LOS 446 CASOS REALES (ar1_inf es "
             "determinista, no usa el RNG)")
    log.info("=" * 78)
    sig = 0
    for c in casos:
        p_inf, _, neff = D.p_cotas_ar1(c["x"], c["y"])
        if neff >= 3.0 and p_inf is not None and p_inf < ALFA:
            sig += 1
    log.info("ar1_inf significativos entre los estimables: %d de %d (%.1f%%)",
             sig, n_est_real, 100 * sig / n_est_real)

    # ------------------------------------------------------------ veredicto
    log.info("")
    log.info("=" * 78)
    log.info("VEREDICTO SEGUN LA REGLA FIJADA EN LA ADENDA")
    log.info("=" * 78)
    t, lo, hi, _ = tasas_tamano["ar1_inf"]
    log.info("ar1_inf: tasa %.3f%% | IC95 [%.3f%%, %.3f%%] | banda "
             "[%.1f%%, %.1f%%]", 100 * t, 100 * lo, 100 * hi,
             100 * SIZE_MIN, 100 * SIZE_MAX)
    if not admisibles:
        log.warning("NINGUN METODO ES ADMISIBLE. Por la regla de la adenda, el "
                    "valor puntual VUELVE A NO DECLARARSE y se cierra como "
                    "indecidible. El 33 regresa a ser la cifra conservadora a "
                    "citar.")
    else:
        poder = {}
        for f in filas:
            if (f["metodo"] in admisibles
                    and f["b_verdadera"] == B_PODER[0]
                    and f["tasa_estimables"] != ""):
                poder[f["metodo"]] = f["tasa_estimables"]
        mejor = (max(poder, key=lambda m: poder[m]) if poder else admisibles[0])
        log.info("Metodos admisibles: %s", ", ".join(admisibles))
        log.info("Mayor poder a b = %+.2f: %s (%.1f%%)", B_PODER[0], mejor,
                 100 * poder.get(mejor, float("nan")))
        if mejor in contenidos:
            log.info("RESERVA 1 CERRADA: el IC95 de %s esta contenido en la "
                     "banda. El valor puntual queda firme.", mejor)
        else:
            log.warning("RESERVA 1 NO CERRADA: el IC95 de %s sigue rebasando "
                        "la banda con el error ya en su minimo practico.",
                        mejor)
        log.info("Las reservas 2 (tautologia de la cota) y 3 (menor poder de "
                 "los doce) NO las cierra esta recalibracion, por diseno.")
    log.info("Recalibracion -> %s", OUT.relative_to(ROOT))
    log.info("LOG           -> %s", LOG_FILE.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
