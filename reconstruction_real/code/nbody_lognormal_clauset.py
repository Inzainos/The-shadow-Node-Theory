"""
Comparacion ley de potencia contra lognormal del ajuste rango-tamano de N-cuerpos.

Pre-registro: reconstruction_real/preregistro/PREREGISTRO_LOGNORMAL_2026-10-02.md
(commit 9718808). Cierra el pendiente que el README arrastra desde la auditoria v32:
un ajuste rango-tamano sobre 32 entidades ordenadas da un R2 alto casi por
construccion, asi que no es evidencia de apego preferencial hasta compararlo contra
una lognormal (Clauset, Shalizi & Newman 2009).

    P1. Distribucion: metodo de Clauset (MLE de alpha con x_min por KS, bondad de
        ajuste por bootstrap parametrico, razon de verosimilitudes de Vuong contra
        lognormal y contra exponencial).
    P2. Curva rango-tamano: potencia contra cuantiles lognormales, comparadas por AIC.
    P3. Poder: con que frecuencia el procedimiento de P1 declara "no descartable"
        una muestra que por construccion ES lognormal.

Datos: data/matriz_mexico_32.csv (columna pib_pc, 32 entidades). Sin descargas.

Salidas:
    reconstruction_real/data/nbody_lognormal_resultados.csv
    reconstruction_real/logs/nbody_lognormal_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/nbody_lognormal_clauset.py
"""

import csv
import logging
import math
import sys
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
DATOS = ROOT / "data" / "matriz_mexico_32.csv"
OUT = ROOT / "reconstruction_real" / "data" / "nbody_lognormal_resultados.csv"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "nbody_lognormal_log.txt"

SEMILLA = 20261002
N_BOOTSTRAP = 2000
N_PODER = 1000
ALFA = 0.05
P_DESCARTE = 0.1          # regla de Clauset: p < 0.1 descarta la ley de potencia
MAX_CANDIDATOS = 200      # tope de candidatos a x_min (ver ajustar_potencia)

log = logging.getLogger("LOGNORMAL")


def _configurar_log():
    """Solo al ejecutarse como programa.

    Si se hiciera al importar, el modulo se aduenaria del logger raiz y
    cualquier script que reutilice estas funciones escribiria su registro en
    el archivo de este (basicConfig no hace nada si ya hay manejadores).
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


# ------------------------------------------------------- metodo de Clauset
def alpha_mle(x, xmin):
    """MLE del exponente de una ley de potencia continua (Clauset ec. 3.1)."""
    x = x[x >= xmin]
    if len(x) < 2:
        return float("nan"), 0
    return 1 + len(x) / np.sum(np.log(x / xmin)), len(x)


def ks_potencia(x, xmin, alpha):
    """Estadistico KS entre la cola empirica y la ley de potencia ajustada."""
    cola = np.sort(x[x >= xmin])
    n = len(cola)
    if n < 2:
        return float("nan")
    emp = np.arange(1, n + 1) / n
    teo = 1 - (cola / xmin) ** (1 - alpha)
    return float(np.max(np.abs(emp - teo)))


def ajustar_potencia(x, max_candidatos=MAX_CANDIDATOS):
    """Elige x_min minimizando KS (Clauset sec. 3.3).

    El barrido completo cuesta O(n^2): con n = 5,570 son 31 millones de
    operaciones por ajuste, y el bootstrap lo llama decenas de miles de veces.
    Por eso, cuando hay mas de max_candidatos valores distintos, se recorre un
    subconjunto espaciado logaritmicamente de ellos, que es lo que hacen las
    implementaciones habituales del metodo. Por debajo de ese tope el barrido
    es exhaustivo y el resultado identico al de la version original.
    """
    cand = np.unique(x)[:-2]          # deja al menos 3 puntos en la cola
    if len(cand) > max_candidatos:
        idx = np.unique(np.geomspace(1, len(cand), max_candidatos).astype(int) - 1)
        cand = cand[idx]

    orden = np.sort(x)
    n_total = len(orden)
    # suma de logaritmos por sufijo, para el MLE de alpha sin recorrer la cola
    suf_log = np.concatenate([np.cumsum(np.log(orden)[::-1])[::-1], [0.0]])

    mejor = (float("inf"), None, None, 0)
    for xmin in cand:
        i = int(np.searchsorted(orden, xmin, side="left"))
        n_cola = n_total - i
        if n_cola < 3:
            continue
        s = suf_log[i] - n_cola * math.log(xmin)
        if s <= 0:
            continue
        a = 1 + n_cola / s
        cola = orden[i:]
        emp = np.arange(1, n_cola + 1) / n_cola
        teo = 1 - (cola / xmin) ** (1 - a)
        d = float(np.max(np.abs(emp - teo)))
        if np.isfinite(d) and d < mejor[0]:
            mejor = (d, float(xmin), a, n_cola)
    return {"ks": mejor[0], "xmin": mejor[1], "alpha": mejor[2], "n_cola": mejor[3]}


def muestrear_potencia(n, xmin, alpha, rng):
    """Muestra de una ley de potencia continua por transformada inversa."""
    return xmin * (1 - rng.random(n)) ** (-1 / (alpha - 1))


def bondad_ajuste(x, ajuste, rng, replicas=N_BOOTSTRAP):
    """p por bootstrap parametrico (Clauset sec. 4.1).

    Cada replica mezcla la cola simulada con los datos observados por debajo de
    x_min, y se reajusta entera con el mismo procedimiento.
    """
    xmin, alpha, ks_obs = ajuste["xmin"], ajuste["alpha"], ajuste["ks"]
    abajo = x[x < xmin]
    n_cola = ajuste["n_cola"]
    p_cola = n_cola / len(x)
    peores = 0
    for _ in range(replicas):
        n_sint = int(rng.random(len(x)).__lt__(p_cola).sum())
        cola = muestrear_potencia(n_sint, xmin, alpha, rng)
        resto = (rng.choice(abajo, len(x) - n_sint, replace=True)
                 if len(abajo) else np.empty(0))
        sint = np.concatenate([cola, resto])
        aj = ajustar_potencia(sint)
        if np.isfinite(aj["ks"]) and aj["ks"] >= ks_obs:
            peores += 1
    return peores / replicas


def vuong(x, xmin, alpha, alternativa):
    """Razon de verosimilitudes de Vuong sobre la cola x >= xmin.

    Devuelve (R normalizado, p de dos colas). R > 0 favorece la ley de potencia.
    """
    cola = x[x >= xmin]
    n = len(cola)
    if n < 3:
        return float("nan"), float("nan")
    # log-verosimilitud por punto de la ley de potencia continua
    l1 = np.log((alpha - 1) / xmin) - alpha * np.log(cola / xmin)

    if alternativa == "lognormal":
        # MLE de la lognormal truncada en xmin, por optimizacion directa
        def neg(p):
            mu, sg = p
            if sg <= 0:
                return 1e12
            z = (np.log(xmin) - mu) / (sg * math.sqrt(2))
            cola_sup = 0.5 * math.erfc(z)      # P(X >= xmin)
            if cola_sup <= 0:
                return 1e12
            ll = (-np.log(cola * sg * math.sqrt(2 * math.pi))
                  - (np.log(cola) - mu) ** 2 / (2 * sg ** 2)
                  - math.log(cola_sup))
            return -float(np.sum(ll))
        from scipy.optimize import minimize
        p0 = [float(np.mean(np.log(cola))), float(np.std(np.log(cola)) or 1.0)]
        r = minimize(neg, p0, method="Nelder-Mead")
        mu, sg = r.x
        z = (np.log(xmin) - mu) / (sg * math.sqrt(2))
        cola_sup = 0.5 * math.erfc(z)
        l2 = (-np.log(cola * sg * math.sqrt(2 * math.pi))
              - (np.log(cola) - mu) ** 2 / (2 * sg ** 2) - math.log(cola_sup))
    elif alternativa == "exponencial":
        lam = 1 / float(np.mean(cola - xmin))
        l2 = np.log(lam) - lam * (cola - xmin)
    else:
        raise ValueError(alternativa)

    dif = l1 - l2
    R = float(np.sum(dif))
    sigma = float(np.std(dif, ddof=0))
    if sigma == 0:
        return R, 1.0
    z = R / (math.sqrt(n) * sigma)
    return R, float(math.erfc(abs(z) / math.sqrt(2)))


# ------------------------------------------------------------------ P1
def punto1(x, rng, filas):
    log.info("=" * 78)
    log.info("P1. DISTRIBUCION — METODO DE CLAUSET")
    log.info("=" * 78)
    aj = ajustar_potencia(x)
    log.info("Ley de potencia: alpha = %.3f | x_min = %.1f | n en la cola = %d "
             "| KS = %.4f", aj["alpha"], aj["xmin"], aj["n_cola"], aj["ks"])
    log.info("   (la cola son %d de %d entidades, %.0f%%)",
             aj["n_cola"], len(x), 100 * aj["n_cola"] / len(x))

    p = bondad_ajuste(x, aj, rng)
    log.info("Bondad de ajuste (bootstrap parametrico, %d replicas): p = %.3f",
             N_BOOTSTRAP, p)
    if p < P_DESCARTE:
        ver_gof = "LA LEY DE POTENCIA SE DESCARTA (p < 0.1)"
    else:
        ver_gof = ("No se puede descartar la ley de potencia (p >= 0.1). "
                   "Ojo: esto NO la confirma")
    log.info("   -> %s", ver_gof)
    filas.append({"punto": "P1", "prueba": "bondad_ajuste_potencia",
                  "estadistico": round(aj["ks"], 4), "p": round(p, 4),
                  "veredicto": ver_gof})

    log.info("")
    for alt in ("lognormal", "exponencial"):
        R, pv = vuong(x, aj["xmin"], aj["alpha"], alt)
        if not np.isfinite(pv):
            ver = "no evaluable"
        elif pv >= ALFA:
            ver = "INDISTINGUIBLE con estos datos"
        elif R > 0:
            ver = "favorece la LEY DE POTENCIA"
        else:
            ver = f"favorece la {alt.upper()}"
        log.info("Vuong, potencia contra %-12s: R = %+.3f | p = %.3f -> %s",
                 alt, R, pv, ver)
        filas.append({"punto": "P1", "prueba": f"vuong_vs_{alt}",
                      "estadistico": round(R, 4), "p": round(pv, 4),
                      "veredicto": ver})
    return aj


# ------------------------------------------------------------------ P2
def punto2(x, filas):
    log.info("")
    log.info("=" * 78)
    log.info("P2. CURVA RANGO-TAMANO — POTENCIA CONTRA CUANTILES LOGNORMALES")
    log.info("=" * 78)
    v = np.sort(x)[::-1]
    n = len(v)
    rango = np.arange(1, n + 1)

    b, a, r, _, _ = stats.linregress(np.log(rango), np.log(v))
    pred_pot = np.exp(a) * rango ** b

    mu, sg = float(np.mean(np.log(v))), float(np.std(np.log(v), ddof=1))
    q = 1 - (rango - 0.5) / n
    pred_ln = np.exp(mu + sg * stats.norm.ppf(q))

    log.info("Potencia:  b = %+.4f | a = %.1f", b, math.exp(a))
    log.info("Lognormal: mu = %.4f | sigma = %.4f", mu, sg)
    log.info("")
    log.info("%-12s %12s %12s %10s", "modelo", "R2 log", "R2 crudo", "AIC")

    res = {}
    for nombre, pred, k in (("potencia", pred_pot, 2), ("lognormal", pred_ln, 2)):
        r2_log = 1 - (np.sum((np.log(v) - np.log(pred)) ** 2)
                      / np.sum((np.log(v) - np.mean(np.log(v))) ** 2))
        r2_raw = 1 - (np.sum((v - pred) ** 2) / np.sum((v - np.mean(v)) ** 2))
        rss = float(np.sum((np.log(v) - np.log(pred)) ** 2))
        aic = n * math.log(rss / n) + 2 * k
        res[nombre] = aic
        log.info("%-12s %12.4f %12.4f %10.2f", nombre, r2_log, r2_raw, aic)
        filas.append({"punto": "P2", "prueba": f"r2_{nombre}",
                      "estadistico": round(r2_raw, 4), "p": "",
                      "veredicto": f"R2 log {r2_log:.4f} | AIC {aic:.2f}"})

    mejor = min(res, key=res.get)
    d = abs(res["potencia"] - res["lognormal"])
    if d < 2:
        ver = f"INDISTINGUIBLES (dAIC = {d:.2f} < 2)"
    elif d <= 10:
        ver = f"evidencia moderada a favor de la {mejor.upper()} (dAIC = {d:.2f})"
    else:
        ver = f"evidencia fuerte a favor de la {mejor.upper()} (dAIC = {d:.2f})"
    log.info("")
    log.info("-> %s", ver)
    filas.append({"punto": "P2", "prueba": "aic_potencia_vs_lognormal",
                  "estadistico": round(d, 4), "p": "", "veredicto": ver})


# ------------------------------------------------------------------ P3
def punto3(x, rng, filas):
    log.info("")
    log.info("=" * 78)
    log.info("P3. PODER DEL DISENO")
    log.info("=" * 78)
    mu, sg = float(np.mean(np.log(x))), float(np.std(np.log(x), ddof=1))
    log.info("Se simulan %d muestras de n = %d desde una LOGNORMAL "
             "(mu = %.3f, sigma = %.3f), que por construccion NO son leyes de "
             "potencia, y se les corre el procedimiento de P1.",
             N_PODER, len(x), mu, sg)

    sobreviven = 0
    for _ in range(N_PODER):
        sint = np.exp(rng.normal(mu, sg, len(x)))
        aj = ajustar_potencia(sint)
        if not np.isfinite(aj["ks"]):
            continue
        # Bootstrap corto por replica: el completo seria 1000 x 2000 ajustes.
        p = bondad_ajuste(sint, aj, rng, replicas=100)
        if p >= P_DESCARTE:
            sobreviven += 1
    tasa = sobreviven / N_PODER
    log.info("")
    log.info("La ley de potencia resulta 'no descartable' en %d de %d muestras "
             "lognormales: **%.1f%%**", sobreviven, N_PODER, 100 * tasa)
    if tasa > 0.5:
        ver = (f"SIN PODER: el procedimiento no descarta la ley de potencia ni "
               f"cuando los datos son lognormales por construccion ({tasa:.0%})")
    elif tasa > 0.2:
        ver = f"PODER BAJO: tasa de falso 'sobrevive' = {tasa:.0%}"
    else:
        ver = f"Poder aceptable: tasa de falso 'sobrevive' = {tasa:.0%}"
    log.info("-> %s", ver)
    filas.append({"punto": "P3", "prueba": "tasa_falso_sobrevive",
                  "estadistico": round(tasa, 4), "p": "", "veredicto": ver})
    return tasa


# ------------------------------------------------------------------ main
def main():
    _configurar_log()
    rng = np.random.default_rng(SEMILLA)
    log.info("=" * 78)
    log.info("COMPARACION LOGNORMAL — pre-registro 2026-10-02 (commit 9718808)")
    log.info("=" * 78)

    with DATOS.open(encoding="utf-8-sig") as fh:
        filas_csv = list(csv.DictReader(fh))
    x = np.array(sorted(float(r["pib_pc"]) for r in filas_csv))
    log.info("Datos: %s | n = %d entidades", DATOS.relative_to(ROOT), len(x))
    log.info("Rango: %.1f .. %.1f (factor %.2f | %.2f ordenes de magnitud)",
             x.min(), x.max(), x.max() / x.min(), math.log10(x.max() / x.min()))
    log.info("Clauset et al. (2009) piden varios ordenes de magnitud y n grande; "
             "esto queda muy por debajo. Anotado en el pre-registro, seccion 0.2.")
    log.info("")

    filas = []
    punto1(x, rng, filas)
    punto2(x, filas)
    tasa = punto3(x, rng, filas)

    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["punto", "prueba", "estadistico",
                                           "p", "veredicto"])
        w.writeheader()
        w.writerows(filas)

    log.info("")
    log.info("=" * 78)
    log.info("RESUMEN")
    log.info("=" * 78)
    for f in filas:
        if f["prueba"].startswith(("bondad", "vuong", "aic", "tasa")):
            log.info("%-30s %s", f["prueba"], f["veredicto"])
    log.info("")
    log.info("Lectura: con una tasa de falso 'sobrevive' del %.0f%%, cualquier "
             "'no se descarta la ley de potencia' en P1 debe leerse como falta "
             "de datos, no como respaldo.", 100 * tasa)
    log.info("Resultados -> %s", OUT.relative_to(ROOT))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
