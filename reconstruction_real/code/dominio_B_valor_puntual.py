"""El valor puntual del Dominio B: cuantos de los 156 estimables son significativos.

Pre-registro: reconstruction_real/preregistro/PREREGISTRO_DOMINIO_B_PUNTUAL_2026-10-02.md
(commit 05bc9ee, subido antes de correr este script).

El Dominio B son 446 pares de paises, el 62% del corpus, con R(t) =
PIBpc_hub/PIBpc_nodo y un OLS de log R contra log t. La auditoria v32 mostro que
sus residuos son casi de raiz unitaria: DW mediana 0.112, rho AR(1) mediana 0.944,
n efectiva mediana 2.2 contra 69 nominal. La particion de estimabilidad (156 si,
290 no) y las cotas de significativos entre los estimables (33 a 112) estan
cerradas. El valor puntual no lo estaba: Newey-West con rezago automatico da 120 de
156, por encima de la cota superior, porque subcorrige a rho ~ 0.94. La corrida del
2026-10-03 lo cierra en 33 de 156 (21.2%) con el unico metodo admisible de doce; ver
las tres reservas en la seccion 6.1 del informe.

El diseno no elige un metodo por autoridad, lo mide:

    P1. Calibracion. 2,000 casos sinteticos con b = 0 y la terna (n, rho, sigma)
        de un caso real al azar. Tasa de falso positivo de cada metodo. Un metodo
        es admisible si su tasa cae en [0.025, 0.075].
    P2. Poder. Lo mismo con b = -0.30 y b = -0.60.
    P3. Valor puntual. Los metodos admisibles, sobre los 446 casos reales.

Salidas:
    reconstruction_real/data/dominio_B_calibracion.csv
    reconstruction_real/data/dominio_B_valor_puntual.csv
    reconstruction_real/logs/dominio_B_valor_puntual_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/dominio_B_valor_puntual.py
"""

import csv
import logging
import math
import sys
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "code"))
from snt_utils_v32 import newey_west_slope  # noqa: E402

MADDISON = ROOT / "data" / "maddison_mpd2020.csv"
B_PUB = ROOT / "reconstruction_real" / "data" / "by_domain" / "dominio_B_real.csv"
OUT_CAL = ROOT / "reconstruction_real" / "data" / "dominio_B_calibracion.csv"
OUT_PTO = ROOT / "reconstruction_real" / "data" / "dominio_B_valor_puntual.csv"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "dominio_B_valor_puntual_log.txt"

SEMILLA = 20261002
ALFA = 0.05
N_SIM = 2000
BOOT_SIM = 199           # replicas de bootstrap dentro de la simulacion
BOOT_REAL = 999          # replicas de bootstrap sobre los datos reales
TOL_B = 1e-4             # tolerancia de reproduccion de la b publicada
SIZE_MIN, SIZE_MAX = 0.025, 0.075   # regla de admision del pre-registro
B_PODER = (-0.30, -0.60)
RHO_TOPE = 0.995
ANIO_MIN, ANIO_MAX = 1900, 2018

log = logging.getLogger("B-PUNTUAL")


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


# --------------------------------------------------------------- utilidades
def ols(x, y):
    """OLS simple. Devuelve (b, a, residuos, sxx)."""
    xc = x - x.mean()
    sxx = float(np.sum(xc ** 2))
    b = float(np.sum(xc * (y - y.mean())) / sxx)
    a = float(y.mean() - b * x.mean())
    return b, a, y - (a + b * x), sxx


def durbin_watson(e):
    s = float(np.sum(e ** 2))
    return float(np.sum(np.diff(e) ** 2) / s) if s > 0 else float("nan")


def rho_de_dw(dw):
    """rho AR(1) implicita, recortada como fija el pre-registro."""
    return float(min(max(1.0 - dw / 2.0, 0.0), RHO_TOPE))


def n_efectivo(n, rho):
    return n * (1.0 - rho) / (1.0 + rho)


def bloques(n):
    """Las tres longitudes de bloque del pre-registro."""
    return {
        "b3": max(2, int(round(n ** (1.0 / 3.0)))),
        "b8": max(2, int(round(math.sqrt(n)))),
        "b17": max(2, int(round(n / 4.0))),
    }


# --------------------------------------------------------------- los metodos
def p_ols(x, y):
    return float(stats.linregress(x, y).pvalue)


def p_cotas_ar1(x, y):
    """Cota inferior (SE inflado + gl) y superior (solo gl) de la auditoria v32."""
    b, _, e, sxx = ols(x, y)
    n = len(x)
    dw = durbin_watson(e)
    rho = rho_de_dw(dw)
    neff = n_efectivo(n, rho)
    se = math.sqrt(float(np.sum(e ** 2)) / (n - 2) / sxx)
    gl = neff - 2.0
    if gl <= 0 or se <= 0:
        return None, None, neff
    t = abs(b) / se
    infl = math.sqrt((1.0 + rho) / (1.0 - rho)) if rho < 1 else float("inf")
    p_inf = float(2.0 * stats.t.sf(t / infl, gl)) if np.isfinite(infl) else 1.0
    p_sup = float(2.0 * stats.t.sf(t, gl))
    return p_inf, p_sup, neff


def p_gls_prais_winsten(x, y, max_iter=50, tol=1e-6):
    """GLS factible AR(1) iterado, conservando la primera observacion."""
    n = len(x)
    if n < 4:
        return None
    b, a, e, _ = ols(x, y)
    rho = 0.0
    for _ in range(max_iter):
        den = float(np.sum(e[:-1] ** 2))
        if den <= 0:
            return None
        nuevo = float(np.sum(e[1:] * e[:-1]) / den)
        nuevo = min(max(nuevo, -RHO_TOPE), RHO_TOPE)
        if abs(nuevo - rho) < tol:
            rho = nuevo
            break
        rho = nuevo
        f = math.sqrt(1.0 - rho ** 2)
        yt = np.concatenate([[f * y[0]], y[1:] - rho * y[:-1]])
        xt = np.concatenate([[f * x[0]], x[1:] - rho * x[:-1]])
        ct = np.concatenate([[f], np.full(n - 1, 1.0 - rho)])
        M = np.column_stack([ct, xt])
        coef, *_ = np.linalg.lstsq(M, yt, rcond=None)
        a, b = float(coef[0]), float(coef[1])
        e = y - (a + b * x)

    f = math.sqrt(1.0 - rho ** 2)
    yt = np.concatenate([[f * y[0]], y[1:] - rho * y[:-1]])
    xt = np.concatenate([[f * x[0]], x[1:] - rho * x[:-1]])
    ct = np.concatenate([[f], np.full(n - 1, 1.0 - rho)])
    M = np.column_stack([ct, xt])
    coef, res, *_ = np.linalg.lstsq(M, yt, rcond=None)
    b = float(coef[1])
    ajuste = M @ coef
    rss = float(np.sum((yt - ajuste) ** 2))
    gl = n - 2
    if gl <= 0 or rss <= 0:
        return None
    XtX_inv = np.linalg.inv(M.T @ M)
    se = math.sqrt(rss / gl * XtX_inv[1, 1])
    if se <= 0:
        return None
    return float(2.0 * stats.t.sf(abs(b) / se, gl)), rho


def _indices_bloques(n, largo, replicas, rng):
    """Matriz (replicas, n) de indices de bloques moviles."""
    k = int(math.ceil(n / largo))
    altos = max(1, n - largo + 1)
    inicios = rng.integers(0, altos, size=(replicas, k))
    idx = inicios[:, :, None] + np.arange(largo)[None, None, :]
    return (idx.reshape(replicas, k * largo) % n)[:, :n]


def p_bootstrap_bloques(x, y, largo, replicas, rng, restringido):
    """Bootstrap por bloques moviles bajo la nula b = 0.

    restringido=True remuestrea los residuos del ajuste con b = 0 (lo que fija el
    pre-registro); False remuestrea los del ajuste completo (variante anadida,
    declarada como desviacion: no arrastra la senal al ruido y por eso no pierde
    poder cuando b != 0).
    """
    n = len(x)
    b_obs, a, e_full, sxx = ols(x, y)
    if sxx <= 0:
        return None
    base = (y - y.mean()) if restringido else e_full
    centro = y.mean() if restringido else a
    idx = _indices_bloques(n, largo, replicas, rng)
    ys = centro + base[idx]                      # (replicas, n)
    xc = x - x.mean()
    bs = (ys - ys.mean(axis=1, keepdims=True)) @ xc / sxx
    extremos = int(np.sum(np.abs(bs) >= abs(b_obs)))
    return (1.0 + extremos) / (replicas + 1.0)


METODOS_BOOT = [
    ("boot_r%s", True), ("boot_u%s", False),
]


def todos_los_p(x, y, replicas, rng):
    """Devuelve {metodo: p} para los nueve metodos del pre-registro y los tres anadidos."""
    n = len(x)
    out = {"ols": p_ols(x, y)}
    p_inf, p_sup, neff = p_cotas_ar1(x, y)
    out["ar1_inf"] = p_inf
    out["ar1_sup"] = p_sup
    out["_n_eff"] = neff
    nw = newey_west_slope(x, y)
    out["nw_auto"] = nw["p_nw"] if np.isfinite(nw["p_nw"]) else None
    nw4 = newey_west_slope(x, y, lag=max(1, int(round(n / 4.0))))
    out["nw_n4"] = nw4["p_nw"] if np.isfinite(nw4["p_nw"]) else None
    g = p_gls_prais_winsten(x, y)
    out["gls_pw"] = g[0] if g else None
    out["_rho_gls"] = g[1] if g else None
    for clave, largo in bloques(n).items():
        for plantilla, restr in METODOS_BOOT:
            out[plantilla % clave] = p_bootstrap_bloques(
                x, y, largo, replicas, rng, restr)
    return out


NOMBRES = (["ols", "ar1_inf", "ar1_sup", "nw_auto", "nw_n4", "gls_pw"]
           + [p % c for c in ("b3", "b8", "b17") for p, _ in METODOS_BOOT])
PREREGISTRADOS = {"ols", "ar1_inf", "ar1_sup", "nw_auto", "nw_n4", "gls_pw",
                  "boot_rb3", "boot_rb8", "boot_rb17"}


# --------------------------------------------------------------- datos reales
def cargar_series():
    """Reconstruye las 446 series exactamente como calc() de expand_B_massive.py."""
    serie = {}
    with MADDISON.open(encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            try:
                v = float(r["GDP per capita"])
            except (TypeError, ValueError):
                continue
            serie.setdefault(r["Entity"], {})[int(r["Year"])] = v

    with B_PUB.open(encoding="utf-8-sig") as fh:
        pub = list(csv.DictReader(fh))

    casos = []
    for r in pub:
        h, nd = serie.get(r["hub"], {}), serie.get(r["nodo"], {})
        anios = sorted(a for a in h if a in nd and ANIO_MIN <= a <= ANIO_MAX)
        if len(anios) < 10:
            continue
        R = np.array([h[a] / nd[a] for a in anios], dtype=float)
        t = np.arange(1, len(R) + 1, dtype=float)
        casos.append({"id": r["id"], "hub": r["hub"], "nodo": r["nodo"],
                      "b_pub": float(r["b"]), "x": np.log(t), "y": np.log(R)})
    return casos


def main():
    configurar_log()
    rng = np.random.default_rng(SEMILLA)
    log.info("=" * 78)
    log.info("DOMINIO B — VALOR PUNTUAL (pre-registro 2026-10-02, 05bc9ee)")
    log.info("=" * 78)

    # ---------------------------------------------------------- reproduccion
    casos = cargar_series()
    log.info("Series reconstruidas desde %s: %d casos",
             MADDISON.relative_to(ROOT), len(casos))
    desvios = []
    perfiles = []
    for c in casos:
        b, _, e, _ = ols(c["x"], c["y"])
        if abs(b - c["b_pub"]) > TOL_B:
            desvios.append((c["id"], b, c["b_pub"]))
        n = len(c["x"])
        dw = durbin_watson(e)
        rho = rho_de_dw(dw)
        c.update(b=b, n=n, dw=dw, rho=rho, n_eff=n_efectivo(n, rho))
        # El cuarto elemento es si el caso REAL de origen es estimable. Ver la
        # nota de estratificacion en nulo_por_caso... mas abajo: clasificar por
        # la realizacion simulada en vez de por el origen metia casos de rho
        # alta en el estrato, porque rho se subestima en series cortas.
        perfiles.append((n, rho, float(np.std(e, ddof=2)),
                         c["n_eff"] >= 3.0))
    if desvios:
        for i, bb, bp in desvios[:5]:
            log.error("   %s: b reconstruida %.6f contra publicada %.6f", i, bb, bp)
        log.error("ALTO: %d casos no reproducen la b publicada (tolerancia %g). "
                  "No se corre ninguna prueba.", len(desvios), TOL_B)
        return 1
    log.info("Reproduccion: %d/%d casos con |b - b_publicada| <= %g. CORRECTO.",
             len(casos), len(casos), TOL_B)
    est_real = [c for c in casos if c["n_eff"] >= 3.0]
    log.info("DW mediana %.4f | rho mediana %.4f | n_eff mediana %.2f | "
             "estimables %d/%d",
             float(np.median([c["dw"] for c in casos])),
             float(np.median([c["rho"] for c in casos])),
             float(np.median([c["n_eff"] for c in casos])),
             len(est_real), len(casos))

    # ------------------------------------------------------- P1 y P2 simulados
    log.info("")
    log.info("=" * 78)
    log.info("P1 y P2. CALIBRACION — %d casos sinteticos por escenario", N_SIM)
    log.info("=" * 78)
    log.info("Las series sinteticas toman (n, rho, sigma) de un caso real al azar.")
    log.info("Con b = 0 todo rechazo es un falso positivo por construccion.")

    escenarios = [("tamano (b = 0)", 0.0)] + [
        ("poder (b = %+.2f)" % b, b) for b in B_PODER]
    filas_cal = []
    tasas_nulas = {}
    for etiqueta, b_true in escenarios:
        rechazos = {m: 0 for m in NOMBRES}
        rech_est = {m: 0 for m in NOMBRES}
        validos = {m: 0 for m in NOMBRES}
        val_est = {m: 0 for m in NOMBRES}
        n_est = 0
        n_est_realizacion = 0
        for _ in range(N_SIM):
            n, rho, sigma, fuente_estimable = perfiles[
                rng.integers(0, len(perfiles))]
            e = np.empty(n)
            e[0] = rng.normal(0.0, sigma)
            ruido = rng.normal(0.0, sigma * math.sqrt(1.0 - rho ** 2), n - 1)
            for k in range(1, n):
                e[k] = rho * e[k - 1] + ruido[k - 1]
            x = np.log(np.arange(1, n + 1, dtype=float))
            y = b_true * x + e
            ps = todos_los_p(x, y, BOOT_SIM, rng)
            # El estrato lo fija el caso REAL de origen, no la realizacion
            # simulada. Clasificar por la realizacion (como hizo la primera
            # corrida) mandaba 87% de las simulaciones al estrato estimable
            # cuando en los datos reales es 35%: con b = 0 los residuos son el
            # propio ruido AR(1) y rho se subestima en series cortas, asi que
            # n_eff sale inflada y entran casos de rho alta que el estrato real
            # no contiene. Eso sesgaba la tasa que decide la admisibilidad.
            estimable = bool(fuente_estimable)
            n_est += estimable
            n_est_realizacion += (ps["_n_eff"] is not None
                                  and ps["_n_eff"] >= 3.0)
            for m in NOMBRES:
                p = ps[m]
                if p is None or not np.isfinite(p):
                    continue
                validos[m] += 1
                rechazos[m] += p < ALFA
                if estimable:
                    val_est[m] += 1
                    rech_est[m] += p < ALFA
        log.info("")
        log.info("%s — estimables por el caso REAL de origen: %d/%d "
                 "(por la realizacion simulada habrian sido %d/%d; ver la nota "
                 "de estratificacion)", etiqueta, n_est, N_SIM,
                 n_est_realizacion, N_SIM)
        log.info("%-10s %10s %12s %10s %12s  %s", "metodo", "tasa total",
                 "(evaluables)", "tasa est.", "(evaluables)", "pre-registrado")
        for m in NOMBRES:
            tt = rechazos[m] / validos[m] if validos[m] else float("nan")
            te = rech_est[m] / val_est[m] if val_est[m] else float("nan")
            log.info("%-10s %9.1f%% %12d %9.1f%% %12d  %s", m, 100 * tt,
                     validos[m], 100 * te, val_est[m],
                     "si" if m in PREREGISTRADOS else "anadido")
            filas_cal.append({"escenario": etiqueta, "b_verdadera": b_true,
                              "metodo": m,
                              "preregistrado": int(m in PREREGISTRADOS),
                              "tasa_total": round(tt, 4),
                              "n_evaluables_total": validos[m],
                              "tasa_estimables": round(te, 4),
                              "n_evaluables_estimables": val_est[m]})
            if b_true == 0.0:
                tasas_nulas[m] = te

    # ------------------------------------------------------------ admisibilidad
    log.info("")
    log.info("=" * 78)
    log.info("REGLA DE ADMISION: tasa de falso positivo en el estrato estimable "
             "dentro de [%.3f, %.3f]", SIZE_MIN, SIZE_MAX)
    log.info("=" * 78)
    admisibles = [m for m in NOMBRES
                  if np.isfinite(tasas_nulas.get(m, float("nan")))
                  and SIZE_MIN <= tasas_nulas[m] <= SIZE_MAX]
    for m in NOMBRES:
        t = tasas_nulas.get(m, float("nan"))
        log.info("%-10s tamano %6.1f%%  ->  %s", m, 100 * t,
                 "ADMISIBLE" if m in admisibles else "no admisible")
    for f in filas_cal:
        f["admisible"] = int(f["metodo"] in admisibles)

    with OUT_CAL.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas_cal[0].keys()))
        w.writeheader()
        w.writerows(filas_cal)

    if not admisibles:
        log.warning("")
        log.warning("NINGUN METODO ES ADMISIBLE. Por regla pre-registrada, el "
                    "valor puntual NO se declara.")

    # ------------------------------------------------------------ P3 datos reales
    log.info("")
    log.info("=" * 78)
    log.info("P3. VALOR PUNTUAL SOBRE LOS %d CASOS REALES", len(casos))
    log.info("=" * 78)
    filas_pto = []
    for c in casos:
        ps = todos_los_p(c["x"], c["y"], BOOT_REAL, rng)
        fila = {"id": c["id"], "hub": c["hub"], "nodo": c["nodo"],
                "n": c["n"], "b": round(c["b"], 4), "dw": round(c["dw"], 4),
                "rho_ar1": round(c["rho"], 4), "n_eff": round(c["n_eff"], 2),
                "estimable": int(c["n_eff"] >= 3.0),
                "rho_gls": (round(ps["_rho_gls"], 4)
                            if ps["_rho_gls"] is not None else "")}
        for m in NOMBRES:
            fila["p_" + m] = ("" if ps[m] is None or not np.isfinite(ps[m])
                              else round(ps[m], 6))
        filas_pto.append(fila)
    with OUT_PTO.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas_pto[0].keys()))
        w.writeheader()
        w.writerows(filas_pto)

    n_est_real = sum(f["estimable"] for f in filas_pto)
    log.info("%-10s %16s %14s %12s  %s", "metodo", "sig/estimables",
             "sig/446", "en [33,112]", "estado")
    for m in NOMBRES:
        sig_e = sum(1 for f in filas_pto if f["estimable"] and f["p_" + m] != ""
                    and f["p_" + m] < ALFA)
        sig_t = sum(1 for f in filas_pto if f["p_" + m] != ""
                    and f["p_" + m] < ALFA)
        log.info("%-10s %10d/%-5d %14d %12s  %s", m, sig_e, n_est_real, sig_t,
                 "si" if 33 <= sig_e <= 112 else "NO",
                 "ADMISIBLE" if m in admisibles else "no admisible")

    log.info("")
    log.info("=" * 78)
    log.info("RESUMEN")
    log.info("=" * 78)
    if admisibles:
        poder = {}
        for f in filas_cal:
            if f["metodo"] in admisibles and f["b_verdadera"] == B_PODER[0]:
                poder[f["metodo"]] = f["tasa_estimables"]
        mejor = max(poder, key=lambda m: poder[m]) if poder else admisibles[0]
        sig_e = sum(1 for f in filas_pto if f["estimable"]
                    and f["p_" + mejor] != "" and f["p_" + mejor] < ALFA)
        log.info("Metodos admisibles: %s", ", ".join(admisibles))
        log.info("Mayor poder a b = %+.2f: %s (%.1f%%)", B_PODER[0], mejor,
                 100 * poder.get(mejor, float("nan")))
        log.info("VALOR PUNTUAL: %d de %d estimables (%.1f%%), metodo %s",
                 sig_e, n_est_real, 100 * sig_e / n_est_real, mejor)
        log.info("Cotas AR(1) publicadas: 33 (21.2%%) - 112 (71.8%%). "
                 "La cifra cae %s de las cotas.",
                 "DENTRO" if 33 <= sig_e <= 112 else "FUERA")
    else:
        log.info("El valor puntual NO se declara: con rho ~ 0.94 y n ~ 69 ningun "
                 "metodo evaluado alcanza el tamano nominal. Por regla "
                 "pre-registrada queda cerrado como indecidible.")
    log.info("Calibracion -> %s", OUT_CAL.relative_to(ROOT))
    log.info("Por caso    -> %s", OUT_PTO.relative_to(ROOT))
    log.info("LOG         -> %s", LOG_FILE.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
