"""Deriva del exponente a lo largo de la vida de un caso, contra la friccion.

Pre-registro: reconstruction_real/preregistro/PREREGISTRO_DERIVA_FORMA_2026-10-02.md
(commit e9a152c, subido antes de escribir este archivo).

La SNT ajusta la satelizacion con una sola forma, R(t) = a*t^b, mientras su capa de
colapso ya admite cinco modos fijados por friccion x disparador x piso. De esa
asimetria sale la hipotesis del autor: la forma no es una etiqueta por caso sino una
trayectoria DENTRO del caso — y los ambientes digitales no la tienen, porque con
friccion ~ 0 no hay con que estirar una fase intermedia.

Prediccion diferencial que se prueba: la deriva del exponente existe en friccion alta
y esta AUSENTE en friccion ~ 0.

Tres brazos, porque dos estarian confundidos (el Dominio B mide un cociente y npm un
nivel; un precio de cripto es un cociente y cripto es friccion ~ 0):

    Dominio B   friccion 3    cociente PIBpc hub/nodo        446 casos
    Cripto      friccion ~0   cociente precio moneda/BTC     hasta 662
    npm         friccion ~0   nivel mensual de descargas      450

Se mide el exponente local b_k por ventana movil y se toma Spearman entre el indice de
ventana y b_k. El nulo se simula POR CASO con b constante y el ruido AR(1) del propio
caso, porque una deriva descendente tambien la produce la autocorrelacion: en el
Dominio B el OLS tiene 59.5% de falso positivo. Cada brazo se compara contra su propio
nulo.

Salidas:
    reconstruction_real/data/deriva_forma_por_caso.csv
    reconstruction_real/data/deriva_forma_resumen.csv
    reconstruction_real/logs/deriva_forma_friccion_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/deriva_forma_friccion.py
"""

import csv
import gzip
import json
import logging
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.signal import lfilter

ROOT = Path(__file__).resolve().parent.parent.parent
MADDISON = ROOT / "data" / "maddison_mpd2020.csv"
B_PUB = ROOT / "reconstruction_real" / "data" / "by_domain" / "dominio_B_real.csv"
CRIPTO = ROOT / "data" / "binance_cierres_diarios.csv.gz"
NPM_DESC = ROOT / "data" / "raw_npm" / "descargas.jsonl.gz"
NPM_MENS = ROOT / "data" / "npm_descargas_mensuales_deriva.csv.gz"
NPM_COH = ROOT / "reconstruction_real" / "data" / "npm_cohorte_aco.csv.gz"
OUT_CASO = ROOT / "reconstruction_real" / "data" / "deriva_forma_por_caso.csv"
OUT_RES = ROOT / "reconstruction_real" / "data" / "deriva_forma_resumen.csv"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "deriva_forma_friccion_log.txt"

SEMILLA = 20261002
ALFA = 0.05
N_NULO = 299              # replicas del nulo por caso
N_BOOT = 1999             # bootstrap de casos para el IC de la diferencia
N_PODER = 60              # casos por brazo para medir el poder (anadido)
DERIVAS_PODER = ((1.5, 0.5), (1.0, 0.5))   # derivas verdaderas simuladas
MIN_VENTANAS = 5
# S2: definicion operativa de "cae" contra "se mantiene". El pre-registro fijo el
# punto pero no el umbral ni el estadistico, asi que se declaran aqui.
S2_COLAPSO = 0.10         # retiene menos del 10% de su maximo -> cae
S2_PERSISTE = 0.90        # retiene 90% o mas -> se mantiene
N_NULO_S2 = 299           # replicas del nulo de retencion por caso
RHO_TOPE = 0.995
HUB_CRIPTO = "BTCUSDT"
MIN_DIAS_CRIPTO = 200
MIN_MESES_NPM = 24
TOL_B = 1e-4
ANIO_MIN, ANIO_MAX = 1900, 2018

log = logging.getLogger("DERIVA")


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
def pendiente(x, y):
    """Pendiente OLS de y contra x. Vectorizada en el eje 0 si y es 2D."""
    xc = x - x.mean()
    sxx = float(np.sum(xc ** 2))
    if sxx <= 0:
        return np.nan if y.ndim == 1 else np.full(y.shape[0], np.nan)
    if y.ndim == 1:
        return float(np.sum(xc * (y - y.mean())) / sxx)
    return (y - y.mean(axis=1, keepdims=True)) @ xc / sxx


def ventanas(n):
    """(ancho, paso, lista de inicios) segun el pre-registro."""
    w = max(8, int(round(n / 4.0)))
    if w > n:
        return w, 1, []
    s = max(1, int(round(w / 4.0)))
    return w, s, list(range(0, n - w + 1, s))


def exponentes_locales(lx, ly):
    """b_k por ventana movil. Devuelve (b_k, ancho, n_ventanas)."""
    n = len(lx)
    w, s, inicios = ventanas(n)
    if len(inicios) < MIN_VENTANAS:
        return None, w, len(inicios)
    bs = np.array([pendiente(lx[i:i + w], ly[i:i + w]) for i in inicios])
    return bs, w, len(inicios)


def _rangos(a):
    """Rangos por fila (promedio simple de orden, sin tratar empates)."""
    orden = np.argsort(a, axis=-1, kind="stable")
    r = np.empty_like(orden, dtype=float)
    np.put_along_axis(r, orden, np.arange(a.shape[-1], dtype=float), axis=-1)
    return r


def spearman_contra_indice(bs):
    """Spearman entre el indice de ventana y b_k. Vectorizado en el eje 0.

    El indice ya es su propio rango, asi que el Spearman es el Pearson entre
    los rangos de b_k y 0..K-1, que se calcula en forma cerrada. Es la misma
    cifra que scipy.stats.spearmanr pero sin un llamado por replica: el nulo
    hace 299 replicas por caso sobre miles de casos.
    """
    r = _rangos(bs)
    k = bs.shape[-1]
    x = np.arange(k, dtype=float)
    xc = x - x.mean()
    rc = r - r.mean(axis=-1, keepdims=True)
    den = math.sqrt(float(np.sum(xc ** 2))) * np.sqrt(np.sum(rc ** 2, axis=-1))
    with np.errstate(invalid="ignore", divide="ignore"):
        out = np.where(den > 0, (rc @ xc) / den, 0.0)
    return out


def deriva(bs):
    """Spearman entre indice de ventana y b_k, para un caso."""
    if bs is None or len(bs) < MIN_VENTANAS or not np.all(np.isfinite(bs)):
        return np.nan
    if np.ptp(bs) == 0:
        return 0.0
    return float(spearman_contra_indice(bs))


def perfil_ruido(lx, ly):
    """(b global, rho AR(1) de los residuos, sigma) del caso."""
    b = pendiente(lx, ly)
    e = ly - (ly.mean() + b * (lx - lx.mean()))
    den = float(np.sum(e[:-1] ** 2))
    rho = float(np.sum(e[1:] * e[:-1]) / den) if den > 0 else 0.0
    rho = min(max(rho, 0.0), RHO_TOPE)
    return b, rho, float(np.std(e, ddof=2)) if len(e) > 2 else float(np.std(e))


def retencion(lx, ly):
    """Cuanto del maximo conserva el caso al final, en escala original.

    r = mediana de la ultima ventana / maximo de la serie. Se toma la mediana de
    la ventana y no el ultimo punto para que una sola observacion rara no decida
    la clasificacion.
    """
    w, _, _ = ventanas(len(lx))
    return float(np.exp(np.median(ly[-w:]) - np.max(ly)))


def bandas_retencion(rs):
    """Fracciones (colapso, intermedio, persiste) de un vector de retenciones."""
    rs = np.asarray(rs, dtype=float)
    if rs.size == 0:
        return None
    col = float(np.mean(rs < S2_COLAPSO))
    per = float(np.mean(rs >= S2_PERSISTE))
    return col, 1.0 - col - per, per


def retencion_nula(lx, b, rho, sigma, rng, reps=N_NULO_S2):
    """Retencion bajo b CONSTANTE con el ruido AR(1) del propio caso.

    Sin esta referencia el reparto observado no se puede leer: con b negativa una
    serie baja sola, asi que una fraccion alta de "colapso" puede ser la
    pendiente y no una caida abrupta.
    """
    n = len(lx)
    esc = sigma * math.sqrt(max(1.0 - rho ** 2, 1e-12))
    z = rng.normal(0.0, esc, (reps, n))
    z[:, 0] = rng.normal(0.0, sigma, reps)
    e = lfilter([1.0], [1.0, -rho], z, axis=1)
    ys = b * lx[None, :] + e
    w, _, _ = ventanas(n)
    return np.exp(np.median(ys[:, -w:], axis=1) - np.max(ys, axis=1))


def nulo_por_caso(lx, b, rho, sigma, rng):
    """Distribucion de la deriva bajo b CONSTANTE con el ruido AR(1) del caso.

    Las N_NULO replicas se generan de golpe: el AR(1) con lfilter y las
    pendientes por ventana con la rama 2D de pendiente(). Hacerlo con bucles de
    Python costaria ~650 millones de iteraciones con las series de cripto, que
    llegan a 3,302 dias.
    """
    n = len(lx)
    w, _, inicios = ventanas(n)
    if len(inicios) < MIN_VENTANAS:
        return None
    esc = sigma * math.sqrt(max(1.0 - rho ** 2, 1e-12))
    z = rng.normal(0.0, esc, (N_NULO, n))
    z[:, 0] = rng.normal(0.0, sigma, N_NULO)      # arranque estacionario
    e = lfilter([1.0], [1.0, -rho], z, axis=1)
    ys = b * lx[None, :] + e
    bs = np.column_stack([pendiente(lx[i:i + w], ys[:, i:i + w])
                          for i in inicios])
    bs = np.where(np.isfinite(bs), bs, 0.0)
    return spearman_contra_indice(bs)


# ------------------------------------------------------------------ brazos
def cargar_dominio_B():
    """446 pares de paises, exactamente como calc() de expand_B_massive.py."""
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
            casos.append({"brazo": "Dominio B", "friccion": "alta (3)",
                          "cantidad": "cociente", "id": r["id"],
                          "etiqueta": f"{r['hub']}->{r['nodo']}",
                          "b_pub": float(r["b"]),
                          "lx": np.log(np.arange(1, len(R) + 1, dtype=float)),
                          "ly": np.log(R)})
    return casos


def cargar_cripto():
    """Cocientes moneda/BTC en dias comunes, BTC como hub."""
    cierres = defaultdict(dict)
    with gzip.open(CRIPTO, "rt", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            try:
                v = float(r["close"])
            except (TypeError, ValueError):
                continue
            if v > 0:
                cierres[r["par"]][r["fecha"]] = v
    hub = cierres.get(HUB_CRIPTO, {})
    casos = []
    for par, serie in sorted(cierres.items()):
        if par == HUB_CRIPTO:
            continue
        fechas = sorted(f for f in serie if f in hub)
        if len(fechas) < MIN_DIAS_CRIPTO:
            continue
        R = np.array([serie[f] / hub[f] for f in fechas], dtype=float)
        casos.append({"brazo": "Cripto", "friccion": "~0",
                      "cantidad": "cociente", "id": par, "etiqueta": par,
                      "b_pub": None,
                      "lx": np.log(np.arange(1, len(R) + 1, dtype=float)),
                      "ly": np.log(R), "pico": fechas[int(np.argmax(R))]})
    return casos


def series_mensuales_npm(coh):
    """Serie mensual por paquete de la cohorte, en el orden de la fuente.

    Prefiere el derivado versionado ``data/npm_descargas_mensuales_deriva.csv.gz``
    (183 KB, SHA-256 en ``data/FUENTES.md``), que es la agregacion mensual exacta
    que usa este brazo. Si no esta, recae en el crudo no versionado
    ``data/raw_npm/descargas.jsonl.gz`` (15 MB) y produce lo mismo.

    El orden de salida replica el del archivo crudo, no el alfabetico: el nulo
    por caso consume el RNG caso por caso, asi que reordenar cambiaria las
    replicas sin cambiar el metodo.
    """
    if NPM_MENS.exists():
        orden, meses = [], defaultdict(lambda: defaultdict(float))
        with gzip.open(NPM_MENS, "rt", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                nombre = r["nombre"]
                if nombre not in coh:
                    continue
                if nombre not in meses:
                    orden.append(nombre)
                meses[nombre][r["mes"]] += float(r["descargas"])
        return [(nombre, meses[nombre]) for nombre in orden]

    log.warning("Sin %s; se recae en el crudo no versionado %s",
                NPM_MENS.name, NPM_DESC.name)
    salida = []
    with gzip.open(NPM_DESC, "rt", encoding="utf-8") as fh:
        for linea in fh:
            d = json.loads(linea)
            if d["nombre"] not in coh:
                continue
            meses = defaultdict(float)
            for dia, v in d["dias"].items():
                meses[dia[:7]] += float(v)
            salida.append((d["nombre"], meses))
    return salida


def cargar_npm():
    """Descargas mensuales de los 450 de la cohorte, desde el nacimiento."""
    with gzip.open(NPM_COH, "rt", encoding="utf-8") as fh:
        coh = {r["nombre"]: r for r in csv.DictReader(fh)}
    casos = []
    for nombre, meses in series_mensuales_npm(coh):
        claves = sorted(meses)
        if len(claves) < MIN_MESES_NPM:
            continue
        R = np.array([meses[k] for k in claves], dtype=float)
        if np.any(R <= 0):                 # el logaritmo no existe
            pos = R > 0
            R = R[pos]
            if len(R) < MIN_MESES_NPM:
                continue
        fila = coh[nombre]
        casos.append({"brazo": "npm", "friccion": "~0",
                      "cantidad": "nivel", "id": nombre,
                      "etiqueta": nombre, "b_pub": None,
                      "lx": np.log(np.arange(1, len(R) + 1, dtype=float)),
                      "ly": np.log(R),
                      "extinto": int(fila["mes_extincion"] not in ("", None)),
                      "delta_caida": fila["delta_caida"]})
    return casos


# ------------------------------------------------------------------ main
def main():
    configurar_log()
    rng = np.random.default_rng(SEMILLA)
    log.info("=" * 78)
    log.info("DERIVA DEL EXPONENTE CONTRA FRICCION — pre-registro 2026-10-02 (e9a152c)")
    log.info("=" * 78)

    log.info("Cargando brazos:")
    brazos = []
    B = cargar_dominio_B()
    desvios = [c["id"] for c in B
               if abs(pendiente(c["lx"], c["ly"]) - c["b_pub"]) > TOL_B]
    if desvios:
        log.error("ALTO: %d casos del Dominio B no reproducen su b publicada "
                  "(tolerancia %g). No se corre ninguna prueba.", len(desvios), TOL_B)
        return 1
    log.info("   Dominio B : %d casos | %d/%d reproducen la b publicada",
             len(B), len(B), len(B))
    brazos.extend(B)
    C = cargar_cripto()
    log.info("   Cripto    : %d casos (hub %s, minimo %d dias comunes)",
             len(C), HUB_CRIPTO, MIN_DIAS_CRIPTO)
    brazos.extend(C)
    N = cargar_npm()
    log.info("   npm       : %d casos (minimo %d meses)", len(N), MIN_MESES_NPM)
    brazos.extend(N)

    log.info("")
    log.info("Ventaneo: w = max(8, n/4), paso = w/4, minimo %d ventanas. "
             "Nulo: %d replicas por caso con b CONSTANTE y el ruido AR(1) del caso.",
             MIN_VENTANAS, N_NULO)

    filas = []
    excluidos = defaultdict(int)
    for c in brazos:
        lx, ly = c["lx"], c["ly"]
        bs, w, nv = exponentes_locales(lx, ly)
        if bs is None:
            excluidos[c["brazo"]] += 1
            continue
        rho_obs = deriva(bs)
        b_glob, rho_ar1, sigma = perfil_ruido(lx, ly)
        nulo = nulo_por_caso(lx, b_glob, rho_ar1, sigma, rng)
        p_desc = (1.0 + np.sum(nulo <= rho_obs)) / (N_NULO + 1.0)
        p_asc = (1.0 + np.sum(nulo >= rho_obs)) / (N_NULO + 1.0)
        filas.append({
            "brazo": c["brazo"], "friccion": c["friccion"],
            "cantidad": c["cantidad"], "id": c["id"], "etiqueta": c["etiqueta"],
            "n": len(lx), "ancho_ventana": w, "n_ventanas": nv,
            "b_global": round(b_glob, 4), "rho_ar1": round(rho_ar1, 4),
            "b_primera_ventana": round(float(bs[0]), 4),
            "b_ultima_ventana": round(float(bs[-1]), 4),
            "cruza_1_a_la_baja": int(bs[0] >= 1.0 > bs[-1]),
            "spearman_deriva": round(rho_obs, 4),
            "p_descendente": round(float(p_desc), 4),
            "p_ascendente": round(float(p_asc), 4),
            "desc_sig": int(p_desc < ALFA), "asc_sig": int(p_asc < ALFA),
            "extinto": c.get("extinto", ""),
            "pico": c.get("pico", ""),
        })

    with OUT_CASO.open("w", encoding="utf-8", newline="") as fh:
        w_ = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w_.writeheader()
        w_.writerows(filas)

    # ------------------------------------------------------------ P1 por brazo
    log.info("")
    log.info("=" * 78)
    log.info("P1. DERIVA POR BRAZO, CONTRA SU PROPIO NULO")
    log.info("=" * 78)
    log.info("%-12s %-10s %-10s %7s %14s %14s %12s", "brazo", "friccion",
             "cantidad", "casos", "desc. sig.", "asc. sig.", "deriva med.")
    res, fracs = [], {}
    for brazo in ("Dominio B", "Cripto", "npm"):
        f = [x for x in filas if x["brazo"] == brazo]
        if not f:
            continue
        nd = sum(x["desc_sig"] for x in f)
        na = sum(x["asc_sig"] for x in f)
        med = float(np.median([x["spearman_deriva"] for x in f]))
        fracs[brazo] = np.array([x["desc_sig"] for x in f], dtype=float)
        log.info("%-12s %-10s %-10s %7d %8d (%4.1f%%) %8d (%4.1f%%) %12.3f",
                 brazo, f[0]["friccion"], f[0]["cantidad"], len(f),
                 nd, 100 * nd / len(f), na, 100 * na / len(f), med)
        res.append({"punto": "P1_deriva_por_brazo", "brazo": brazo,
                    "friccion": f[0]["friccion"], "cantidad": f[0]["cantidad"],
                    "casos": len(f), "desc_sig": nd,
                    "frac_desc": round(nd / len(f), 4), "asc_sig": na,
                    "frac_asc": round(na / len(f), 4),
                    "deriva_mediana": round(med, 4),
                    "excluidos_por_ventanas": excluidos[brazo]})
    for b, n in excluidos.items():
        log.info("   excluidos por menos de %d ventanas — %s: %d",
                 MIN_VENTANAS, b, n)

    # --------------------------------------------- estadistico principal
    log.info("")
    log.info("=" * 78)
    log.info("PRINCIPAL. DIFERENCIA DOMINIO B (friccion alta) MENOS CRIPTO (friccion ~0)")
    log.info("=" * 78)
    log.info("Los dos son cocientes, asi que la diferencia aisla la friccion.")
    if "Dominio B" in fracs and "Cripto" in fracs:
        a, b_ = fracs["Dominio B"], fracs["Cripto"]
        dif = float(a.mean() - b_.mean())
        boot = np.array([rng.choice(a, len(a), replace=True).mean()
                         - rng.choice(b_, len(b_), replace=True).mean()
                         for _ in range(N_BOOT)])
        lo, hi = np.percentile(boot, [2.5, 97.5])
        log.info("   Dominio B %.1f%% - Cripto %.1f%% = %+.1f puntos "
                 "| IC 95%% [%+.1f, %+.1f]",
                 100 * a.mean(), 100 * b_.mean(), 100 * dif, 100 * lo, 100 * hi)
        ver = ("H1 RESPALDADA" if lo > 0 else
               "CONTRARIO A LA PREDICCION" if hi < 0 else
               "SIN DIFERENCIA DETECTABLE")
        log.info("   -> %s", ver)
        res.append({"punto": "PRINCIPAL_dif_B_menos_cripto", "brazo": "B-Cripto",
                    "frac_desc": round(dif, 4), "ic_lo": round(float(lo), 4),
                    "ic_hi": round(float(hi), 4), "veredicto": ver})

    # ------------------------------------------------------------ S1 cruce de 1
    log.info("")
    log.info("=" * 78)
    log.info("S1. EL CRUCE DEL 1 — 'potencia -> lineal' predice el cruce, no una bajada")
    log.info("=" * 78)
    log.info("%-12s %18s %18s %16s", "brazo", "b 1a ventana (med)",
             "b ult. ventana (med)", "cruzan 1 a baja")
    for brazo in ("Dominio B", "Cripto", "npm"):
        f = [x for x in filas if x["brazo"] == brazo]
        if not f:
            continue
        p = float(np.median([x["b_primera_ventana"] for x in f]))
        u = float(np.median([x["b_ultima_ventana"] for x in f]))
        cr = sum(x["cruza_1_a_la_baja"] for x in f)
        log.info("%-12s %18.3f %18.3f %10d (%4.1f%%)", brazo, p, u, cr,
                 100 * cr / len(f))
        res.append({"punto": "S1_cruce_1", "brazo": brazo,
                    "b_primera_mediana": round(p, 4),
                    "b_ultima_mediana": round(u, 4), "cruzan_1": cr,
                    "frac_cruzan": round(cr / len(f), 4)})

    # ------------------------------------------- S2 bimodalidad en friccion 0
    log.info("")
    log.info("=" * 78)
    log.info("S2. BIMODALIDAD EN FRICCION 0 — 'o muy abruptos o se mantienen'")
    log.info("=" * 78)
    log.info("El pre-registro fijo el punto pero NO la definicion operativa de "
             "'cae' ni un estadistico de bimodalidad. Se declaran aqui: retencion "
             "r = mediana de la ultima ventana / maximo de la serie; cae si "
             "r < %.2f, se mantiene si r >= %.2f. La hipotesis del autor predice "
             "masa en los dos extremos y hueco en medio.", S2_COLAPSO, S2_PERSISTE)
    log.info("Cada brazo digital se compara contra SU PROPIO nulo (b constante con "
             "su rho y su sigma, %d replicas por caso), nunca contra otro brazo: "
             "con b negativa una serie baja sola, asi que sin el nulo no se puede "
             "saber si el hueco es real o aritmetica de la pendiente.", N_NULO_S2)
    log.info("RNG propio (semilla %d) para no alterar las replicas de los puntos "
             "ya corridos.", SEMILLA + 2)
    rng_s2 = np.random.default_rng(SEMILLA + 2)
    log.info("%-8s %6s %10s %12s %10s %12s %10s %12s", "brazo", "casos",
             "cae obs", "cae nulo", "medio obs", "medio nulo", "mantiene",
             "mant. nulo")
    for brazo in ("Cripto", "npm"):
        pool = [c for c in brazos if c["brazo"] == brazo]
        if not pool:
            continue
        r_obs, nul_col, nul_med, nul_per = [], [], [], []
        for c in pool:
            lx, ly = c["lx"], c["ly"]
            r_obs.append(retencion(lx, ly))
            bg, rho_c, sg = perfil_ruido(lx, ly)
            bn = bandas_retencion(retencion_nula(lx, bg, rho_c, sg, rng_s2))
            if bn is None:
                continue
            nul_col.append(bn[0])
            nul_med.append(bn[1])
            nul_per.append(bn[2])
        obs = bandas_retencion(r_obs)
        if obs is None or not nul_col:
            continue
        esp = (float(np.mean(nul_col)), float(np.mean(nul_med)),
               float(np.mean(nul_per)))
        log.info("%-8s %6d %9.1f%% %11.1f%% %9.1f%% %11.1f%% %9.1f%% %11.1f%%",
                 brazo, len(pool), 100 * obs[0], 100 * esp[0], 100 * obs[1],
                 100 * esp[1], 100 * obs[2], 100 * esp[2])
        res.append({"punto": "S2_bimodalidad_digital", "brazo": brazo,
                    "casos": len(pool),
                    "frac_cae": round(obs[0], 4),
                    "frac_cae_nulo": round(esp[0], 4),
                    "frac_medio": round(obs[1], 4),
                    "frac_medio_nulo": round(esp[1], 4),
                    "frac_mantiene": round(obs[2], 4),
                    "frac_mantiene_nulo": round(esp[2], 4)})
        # empinamiento de la caida cuando cae
        caen = [x for x, r in zip(pool, r_obs) if r < S2_COLAPSO]
        if caen:
            ids = {x["id"] for x in caen}
            g = [x for x in filas if x["brazo"] == brazo and x["id"] in ids]
            if g:
                bgm = float(np.median([x["b_global"] for x in g]))
                bum = float(np.median([x["b_ultima_ventana"] for x in g]))
                log.info("   empinamiento de los que caen (n=%d): b global "
                         "mediana %+.3f | b de la ultima ventana %+.3f",
                         len(g), bgm, bum)
                res.append({"punto": "S2_empinamiento_caida", "brazo": brazo,
                            "casos": len(g), "b_global_mediana": round(bgm, 4),
                            "b_ultima_mediana": round(bum, 4)})
        hueco = obs[1] - esp[1]
        log.info("   hueco en medio: %+.1f puntos contra el nulo -> %s",
                 100 * hueco,
                 "mas vacio que el nulo (compatible con bimodalidad)"
                 if hueco < 0 else
                 "NO mas vacio que el nulo (sin evidencia de bimodalidad)")

    # --------------------------------------------- S3 control de supervivencia
    log.info("")
    log.info("=" * 78)
    log.info("S3. CONTROL DE SUPERVIVENCIA EN npm — extinguidos contra persistentes")
    log.info("=" * 78)
    nf = [x for x in filas if x["brazo"] == "npm" and x["extinto"] != ""]
    for etq, sel in (("extinguidos", 1), ("persistentes", 0)):
        g = [x for x in nf if x["extinto"] == sel]
        if not g:
            continue
        nd = sum(x["desc_sig"] for x in g)
        log.info("   %-14s n=%3d | desc. sig. %3d (%4.1f%%) | deriva mediana %+.3f",
                 etq, len(g), nd, 100 * nd / len(g),
                 float(np.median([x["spearman_deriva"] for x in g])))
        res.append({"punto": "S3_supervivencia_npm", "brazo": etq,
                    "casos": len(g), "desc_sig": nd,
                    "frac_desc": round(nd / len(g), 4)})

    # -------------------------------------------------- S4 relacion con RC1
    log.info("")
    log.info("=" * 78)
    log.info("S4. RELACION CON RC1 — los casos con b >= 1, 'atrapados temprano'?")
    log.info("=" * 78)
    log.info("b >= 1 se usa aqui como CORTE NUMERICO, no como regimen: RC1 "
             "(2026-10-02) midio que una exponencial verdadera ajustada como ley "
             "de potencia cae ahi casi siempre, asi que el umbral no separa "
             "satelizacion rapida de un desajuste de forma. Ver "
             "audits/RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md.")
    log.info("La comparacion es DENTRO de cada brazo; entre brazos no se compara.")
    log.info("Bajo la hipotesis del autor, un caso con b >= 1 esta atrapado "
             "temprano en su trayectoria, asi que deberia tener b de la primera "
             "ventana aun mayor que su b global y deriva descendente.")
    log.info("%-12s %-14s %6s %16s %14s %16s", "brazo", "grupo", "casos",
             "b 1a ventana (med)", "b global (med)", "desc. sig.")
    for brazo in ("Dominio B", "Cripto", "npm"):
        f = [x for x in filas if x["brazo"] == brazo]
        if not f:
            continue
        for etq, sel in (("b >= 1", True), ("b < 1", False)):
            g = [x for x in f if (x["b_global"] >= 1.0) == sel]
            if not g:
                log.info("%-12s %-14s %6d %16s %14s %16s", brazo, etq, 0,
                         "-", "-", "-")
                res.append({"punto": "S4_rc1_superlineales", "brazo": brazo,
                            "grupo": etq, "casos": 0})
                continue
            p1 = float(np.median([x["b_primera_ventana"] for x in g]))
            pg = float(np.median([x["b_global"] for x in g]))
            nd = sum(x["desc_sig"] for x in g)
            log.info("%-12s %-14s %6d %16.3f %14.3f %10d (%4.1f%%)", brazo, etq,
                     len(g), p1, pg, nd, 100 * nd / len(g))
            res.append({"punto": "S4_rc1_superlineales", "brazo": brazo,
                        "grupo": etq, "casos": len(g),
                        "b_primera_mediana": round(p1, 4),
                        "b_global_mediana": round(pg, 4),
                        "desc_sig": nd, "frac_desc": round(nd / len(g), 4)})

    # ------------------------------------------------- PODER (anadido)
    log.info("")
    log.info("=" * 78)
    log.info("PODER DEL DISENO POR BRAZO — ANADIDO, NO PRE-REGISTRADO")
    log.info("=" * 78)
    log.info("El pre-registro fijo el nulo pero no el poder. La validacion del codigo "
             "mostro que con ruido AR(1) fuerte el poder cae mucho, asi que una "
             "fraccion baja podria ser falta de poder y no ausencia de deriva. Sin "
             "esta tabla el resultado negativo no se puede interpretar — es la "
             "leccion del caso de Clauset.")
    log.info("%-12s %-18s %9s %12s", "brazo", "deriva verdadera", "casos",
             "detectada")
    for brazo in ("Dominio B", "Cripto", "npm"):
        pool = [c for c in brazos if c["brazo"] == brazo]
        if not pool:
            continue
        muestra = [pool[i] for i in rng.choice(len(pool),
                                               min(N_PODER, len(pool)),
                                               replace=False)]
        for b0, b1 in DERIVAS_PODER:
            det = ev = 0
            for c in muestra:
                lx = c["lx"]
                n = len(lx)
                _, rho_ar1, sigma = perfil_ruido(lx, c["ly"])
                bt = np.linspace(b0, b1, n)
                base = np.cumsum(bt * np.gradient(lx))
                esc = sigma * math.sqrt(max(1.0 - rho_ar1 ** 2, 1e-12))
                z = rng.normal(0.0, esc, n)
                z[0] = rng.normal(0.0, sigma)
                e = lfilter([1.0], [1.0, -rho_ar1], z)
                ly = base + e
                bs, _, nv = exponentes_locales(lx, ly)
                if bs is None:
                    continue
                r = deriva(bs)
                bg2, rr2, sg2 = perfil_ruido(lx, ly)
                nul = nulo_por_caso(lx, bg2, rr2, sg2, rng)
                if nul is None:
                    continue
                ev += 1
                det += (1.0 + np.sum(nul <= r)) / (N_NULO + 1.0) < ALFA
            if ev:
                log.info("%-12s %-18s %9d %11.1f%%", brazo,
                         f"{b0:+.1f} -> {b1:+.1f}", ev, 100 * det / ev)
                res.append({"punto": "PODER_anadido", "brazo": brazo,
                            "deriva_simulada": f"{b0}->{b1}", "casos": ev,
                            "frac_desc": round(det / ev, 4)})

    # ------------------------------------- limitacion 1: agrupar cripto
    log.info("")
    log.info("=" * 78)
    log.info("LIMITACION 1. CRIPTO AGRUPADA POR TRIMESTRE DE PICO")
    log.info("=" * 78)
    log.info("Los casos de cripto no son independientes: el mercado se mueve en bloque.")
    grupos = defaultdict(list)
    for x in filas:
        if x["brazo"] == "Cripto" and x["pico"]:
            a_, m_ = x["pico"][:4], int(x["pico"][5:7])
            grupos[f"{a_}T{(m_ - 1) // 3 + 1}"].append(x["desc_sig"])
    if grupos:
        por_g = np.array([np.mean(v) for v in grupos.values()])
        log.info("   %d trimestres | fraccion descendente media entre trimestres "
                 "%.1f%% (contra %.1f%% por caso)", len(grupos),
                 100 * por_g.mean(), 100 * fracs["Cripto"].mean())
        res.append({"punto": "LIM1_cripto_agrupada", "brazo": "Cripto",
                    "casos": len(grupos),
                    "frac_desc": round(float(por_g.mean()), 4)})

    cols = sorted({k for r in res for k in r})
    cols = ["punto", "brazo"] + [c for c in cols if c not in ("punto", "brazo")]
    with OUT_RES.open("w", encoding="utf-8", newline="") as fh:
        w_ = csv.DictWriter(fh, fieldnames=cols, restval="")
        w_.writeheader()
        w_.writerows(res)

    log.info("")
    log.info("=" * 78)
    log.info("RESUMEN")
    log.info("=" * 78)
    for brazo in ("Dominio B", "Cripto", "npm"):
        if brazo in fracs:
            log.info("%-12s friccion %-9s deriva descendente en %.1f%% de los casos",
                     brazo,
                     next(x["friccion"] for x in filas if x["brazo"] == brazo),
                     100 * fracs[brazo].mean())
    log.info("Por caso -> %s", OUT_CASO.relative_to(ROOT))
    log.info("Resumen  -> %s", OUT_RES.relative_to(ROOT))
    log.info("LOG      -> %s", LOG_FILE.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
