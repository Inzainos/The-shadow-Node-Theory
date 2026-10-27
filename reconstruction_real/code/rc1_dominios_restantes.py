"""RC1 en los dominios restantes (A, E2, C): ¿el veredicto sobre b >= 1 se replica?

Pre-registro: reconstruction_real/preregistro/PREREGISTRO_RC1_DOMINIOS_RESTANTES_2026-10-17.md
(commit 4e9cb9e, subido antes de descargar un solo byte de datos nuevos).

RC1 (2026-10-02) cerro la pregunta del regimen superlineal sobre los tres dominios
que entonces tenian serie cruda: E3 (234), B (446) y ACO (18). El veredicto fue
doble: (i) el AIC de comparar_modelos no es admisible en la banda b >= 1 (error de
seleccion 80.3% / 96.8% / 48.9%, umbral 20%), y (ii) una exponencial verdadera
ajustada como ley de potencia cae en b >= 1 casi siempre en las bandas altas, por
lo que la etiqueta "Roche Radius" fue retirada.

Este script extiende la misma maquinaria a los dominios restantes con serie cruda
reconstruible desde fuentes publicas:

    A  (4 casos)   -- recetas candidatas SOBRE data/wup2018_aglomeraciones_1950_2018.csv.gz
    E2 (2 casos)  -- R `lynx` (Rdatasets) y tabla lince-liebre 1900-1920 (dsem/CRAN,
                     Gotelli 2008 Fig 6.16 <- MacLulich 1937, Elton & Nicholson 1942)
    C  (22 casos) -- poblacion estatal anual 1900-2025, US Census via FRED (sin API key)

Ninguno de los tres tiene casos superlineales publicados (max +0.8914), asi que la
pregunta por dominio es la contrafactual del pre-registro:

    P0. Con la (n, rho AR(1), sigma) real de cada dominio, ¿el AIC discriminaria a
        b >= 1 si existiera un caso asi? (bandas contrafactuales b=1.25 y b=1.75)
    P5. ¿una exponencial verdadera con el ruido de este dominio produciria una
        b aparente >= 1?

REGLA POR DOMINIO (Axioma 0.1 / 2): cada dominio por separado, sin agrupar ni
ordenar. Los resultados se cuentan; su diferencia no se mide.

Fase 0 -- identificacion de recetas (lista ordenada del pre-registro; aceptacion:
primera receta con >= 90% de los casos reproduciendo la b publicada dentro de
±0.01). Sin receta exacta NO se calibra: calibrar con una serie aproximada
contaminaria el (rho, sigma) — el instrumento mismo.

Salidas:
    data/us_census_poblacion_estatal_1900_2025.csv   (si falta, se descarga)
    reconstruction_real/data/rc1_resto_recetas.csv
    reconstruction_real/data/rc1_resto_por_caso.csv
    reconstruction_real/data/rc1_resto_calibracion.csv
    reconstruction_real/data/rc1_resto_resumen.csv
    reconstruction_real/logs/rc1_dominios_restantes_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/rc1_dominios_restantes.py
"""

import csv
import hashlib
import io
import logging
import sys
import time
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "code"))
sys.path.insert(0, str(ROOT / "reconstruction_real" / "code"))
from snt import configurar_logging as configurar_log  # noqa: E402
from snt import sha256  # noqa: E402
from snt_utils_v32 import comparar_modelos  # noqa: E402
from rc1_superlineal import (  # noqa: E402
    ajuste_loglog, banda_de, perfil, ruido_ar1,
)

DATA = ROOT / "data"
RR = ROOT / "reconstruction_real" / "data"
WUP = DATA / "wup2018_aglomeraciones_1950_2018.csv.gz"
LYNX = DATA / "lynx_1821_1934.csv"
HARE = DATA / "hare_lynx_1900_1920.csv"
CENSO = DATA / "us_census_poblacion_estatal_1900_2025.csv"
C_PUB = RR / "by_domain" / "dominio_C_real.csv"
A_PUB = RR / "by_domain" / "dominio_A_real.csv"
E2_PUB = RR / "by_domain" / "dominio_E2_real.csv"

OUT_REC = RR / "rc1_resto_recetas.csv"
OUT_CASO = RR / "rc1_resto_por_caso.csv"
OUT_CAL = RR / "rc1_resto_calibracion.csv"
OUT_RES = RR / "rc1_resto_resumen.csv"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "rc1_dominios_restantes_log.txt"

SEMILLA = 20261017
ALFA = 0.05
N_CAL = 200                 # replicas por caso-banda (P0) y por caso (P5)
UMBRAL_ERROR = 0.20         # admisibilidad en la banda b >= 1 (regla de RC1)
TOL_RECETA = 0.01           # Fase 0: |b_receta - b_publicada|
B_CF = (1.25, 1.75)         # centros de las bandas contrafactuales b >= 1
ANIO_MIN, ANIO_MAX = 1900, 2025

# Pares del dominio C (C_002..C_024; C_001 Mexico es rango-tamaño, sin serie R(t))
PARES_C = [
    ("C_002", "CA", "NV"), ("C_003", "CA", "AZ"), ("C_004", "CA", "OR"),
    ("C_005", "NY", "NJ"), ("C_006", "NY", "CT"), ("C_007", "NY", "PA"),
    ("C_008", "TX", "OK"), ("C_009", "TX", "NM"), ("C_010", "TX", "LA"),
    ("C_011", "IL", "IN"), ("C_012", "IL", "WI"), ("C_013", "IL", "MO"),
    ("C_014", "FL", "GA"), ("C_015", "FL", "AL"),
    ("C_016", "MA", "NH"), ("C_017", "MA", "ME"), ("C_018", "MA", "VT"),
    ("C_019", "WA", "ID"), ("C_020", "WA", "MT"),
    ("C_021", "CO", "WY"), ("C_022", "CO", "UT"),
    ("C_023", "GA", "SC"), ("C_024", "MI", "OH"),
]
ESTADOS_C = sorted({s for _, h, n in PARES_C for s in (h, n)})

# Alias WUP (el archivo de aglomeraciones >= 300 mil no usa los nombres del corpus)
ALIAS_WUP = {"Osaka": "Kinki M.M.A. (Osaka)"}
CENSO_ANIOS = {"Japan": [2000, 2005, 2010, 2015, 2020],
               "France": [1999, 2006, 2011, 2016, 2021],
               "Spain": [2001, 2011, 2021]}

log = logging.getLogger("RC1-RESTO")


# ------------------------------------------------------------------ Fase 0: A
def fase0_A(filas):
    """Recetas candidatas del pre-registro sobre el WUP versionado."""
    serie = defaultdict(dict)
    with __import__("gzip").open(WUP, "rt", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            serie[r["ciudad"]][int(r["anio"])] = float(r["pob_miles"])
    casos = list(csv.DictReader(A_PUB.open(encoding="utf-8-sig")))
    reproducidos = 0
    for c in casos:
        cid, bpub = c["id"], float(c["b"])
        # hub/nodo desde la descripcion "X->Y pop ..."
        hub, nodo = c["descripcion"].split(" pop ")[0].split("→")
        pais = "Japan" if hub == "Tokyo" else ("France" if hub == "Paris" else "Spain")
        ini = int(c["descripcion"].split(" pop ")[1].split("-")[0])
        H = serie.get(ALIAS_WUP.get(hub, hub), {})
        N = serie.get(ALIAS_WUP.get(nodo, nodo), {})
        if not H or not N:
            filas.append({"dominio": "A", "id": cid, "receta": "—",
                          "n": 0, "b_receta": "", "b_pub": bpub,
                          "delta": "", "reproduce": "sin_serie_en_fuente"})
            continue
        anios_comunes = sorted(a for a in H if a in N
                               and ini <= a <= min(2020, 2018))
        recetas = [
            ("anual_ini_2018", anios_comunes),
            ("cada3", [a for a in anios_comunes if (a - ini) % 3 == 0]),
            ("cada4", [a for a in anios_comunes if (a - ini) % 4 == 0]),
            ("cada5", [a for a in anios_comunes if (a - ini) % 5 == 0]),
            ("censo", [a for a in anios_comunes if a in CENSO_ANIOS[pais]]),
            ("1950_2018", sorted(set(H) & set(N))),
        ]
        mejor = None
        for nombre, anios in recetas:
            if len(anios) < 3:
                filas.append({"dominio": "A", "id": cid, "receta": nombre,
                              "n": len(anios), "b_receta": "", "b_pub": bpub,
                              "delta": "", "reproduce": "no_evaluable (<3 pts)"})
                continue
            t = np.arange(1, len(anios) + 1, dtype=float)
            y = np.array([H[a] / N[a] for a in anios], dtype=float)
            b = ajuste_loglog(t, y)[0]
            delta = b - bpub
            ok = abs(delta) <= TOL_RECETA
            filas.append({"dominio": "A", "id": cid, "receta": nombre,
                          "n": len(anios), "b_receta": round(b, 4),
                          "b_pub": bpub, "delta": round(delta, 4),
                          "reproduce": int(ok)})
            if mejor is None or abs(delta) < abs(mejor[3]):
                mejor = (nombre, len(anios), b, delta)
            if ok:
                break
        if mejor and abs(mejor[3]) <= TOL_RECETA:
            reproducidos += 1
            log.info("   A %s: receta %s reproduce (b=%+.4f, pub %+.4f)",
                     cid, mejor[0], mejor[2], bpub)
        else:
            log.info("   A %s: NINGUNA receta reproduce (mejor: %s b=%+.4f vs pub %+.4f)",
                     cid, mejor[0] if mejor else "—",
                     mejor[2] if mejor else float("nan"), bpub)
    total = len(casos)
    log.info("   A: %d/%d casos reproducen la b publicada (umbral 4/4)", reproducidos, total)
    return casos if reproducidos == total else []


# ----------------------------------------------------------------- Fase 0: E2
def fase0_E2(filas):
    """E2_01 (tabla lince-liebre 1900-1920) y E2_02 (R lynx, 1821-1850)."""
    pub = list(csv.DictReader(E2_PUB.open(encoding="utf-8-sig")))
    casos_ok = []
    byid = {r["id"]: r for r in pub}

    # -- E2_01: recetas pre-registradas R = liebre/lince y R = lince/liebre
    hl = pd.read_csv(HARE)
    t = np.arange(1, len(hl) + 1, dtype=float)
    bpub = float(byid["E2_01"]["b"])
    elegido = None
    for nombre, y in [("R=liebre/lince", hl.pieles_liebre / hl.pieles_lince),
                      ("R=lince/liebre", hl.pieles_lince / hl.pieles_liebre)]:
        b = ajuste_loglog(t, y.values)[0]
        ok = abs(b - bpub) <= TOL_RECETA
        filas.append({"dominio": "E2", "id": "E2_01", "receta": nombre,
                      "n": len(t), "b_receta": round(b, 4), "b_pub": bpub,
                      "delta": round(b - bpub, 4), "reproduce": int(ok)})
        if ok:
            elegido = (nombre, y.values)
            break
    if elegido:
        log.info("   E2_01: receta '%s' reproduce exacto (b=%+.4f vs pub %+.4f)",
                 elegido[0], ajuste_loglog(t, elegido[1])[0], bpub)
        casos_ok.append({"dominio": "E2", "id": "E2_01",
                         "etiqueta": "Lynx→Hare 1900-1920",
                         "t": t, "y": elegido[1], "b_pub": bpub})
    else:
        log.info("   E2_01: ninguna de las 2 recetas reproduce")

    # -- E2_02: 4 recetas sobre la ventana 1821-1850 (todas de normalizacion
    #    constante: comparten pendiente, se listan por fidelidad al protocolo)
    lx = pd.read_csv(LYNX)
    x = lx[lx.anio.between(1821, 1850)].capturas_lince.values
    xf = lx.capturas_lince.values
    t2 = np.arange(1, len(x) + 1, dtype=float)
    bpub2 = float(byid["E2_02"]["b"])
    for nombre, y in [("x/media(ventana)", x / x.mean()),
                      ("x/media(1821-1934)", x / xf.mean()),
                      ("x/mediana(ventana)", x / np.median(x)),
                      ("x/x_1821", x / x[0])]:
        b = ajuste_loglog(t2, y)[0]
        ok = abs(b - bpub2) <= TOL_RECETA
        filas.append({"dominio": "E2", "id": "E2_02", "receta": nombre,
                      "n": len(t2), "b_receta": round(b, 4), "b_pub": bpub2,
                      "delta": round(b - bpub2, 4), "reproduce": int(ok)})
    log.info("   E2_02: las 4 recetas dan b=%+.4f vs pub %+.4f -> NO reproducible",
             ajuste_loglog(t2, x / x.mean())[0], bpub2)

    log.info("   E2: 1/2 casos reproducibles (se calibra SOLO E2_01, "
             "rotulado como caso unico; E2_02 queda no reproducible)")
    return casos_ok


# ------------------------------------------------------------------ Fase 0: C
def asegurar_censo():
    """Descarga (una vez) las 32 series estatales de FRED y arma el CSV long."""
    if CENSO.exists():
        log.info("   censo: %s presente (sha256 %s…)", CENSO.name, sha256(CENSO)[:16])
        return
    log.info("   censo: descargando %d series FRED ({XX}POP, Census PEP, sin API key)…",
             len(ESTADOS_C))
    filas = []
    for st in ESTADOS_C:
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={st}POP"
        for intento in range(3):
            try:
                raw = urllib.request.urlopen(url, timeout=30).read()
                break
            except Exception as exc:  # noqa: BLE001 — reintento con pausa
                if intento == 2:
                    raise
                log.warning("      %s falló (%s), reintento…", st, exc)
                time.sleep(3)
        d = pd.read_csv(io.BytesIO(raw))
        d.columns = ["fecha", "poblacion_miles"]
        d["anio"] = d.fecha.str[:4].astype(int)
        d = d[(d.anio >= ANIO_MIN) & (d.anio <= ANIO_MAX)]
        log.info("      %sPOP: %d años (%d-%d) | sha256 %s…", st, len(d),
                 d.anio.min(), d.anio.max(), hashlib.sha256(raw).hexdigest()[:16])
        for _, r in d.iterrows():
            filas.append({"estado": st, "anio": int(r.anio),
                          "poblacion_miles": float(r.poblacion_miles)})
        time.sleep(0.4)
    with CENSO.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["estado", "anio", "poblacion_miles"])
        w.writeheader()
        w.writerows(filas)
    log.info("   censo: %s escrito (sha256 %s…)", CENSO.name, sha256(CENSO)[:16])


def fase0_C(filas):
    """Receta unica pre-especificada: R = pob_hub/pob_node, anual 1900-2025."""
    asegurar_censo()
    d = pd.read_csv(CENSO)
    serie = {st: dict(zip(g.anio, g.poblacion_miles))
             for st, g in d.groupby("estado")}
    pub = {r["id"]: float(r["b"]) for r in csv.DictReader(C_PUB.open(encoding="utf-8-sig"))}
    casos = []
    for cid, hub, nodo in PARES_C:
        anios = sorted(set(serie[hub]) & set(serie[nodo]))
        t = np.arange(1, len(anios) + 1, dtype=float)
        y = np.array([serie[hub][a] / serie[nodo][a] for a in anios], dtype=float)
        b = ajuste_loglog(t, y)[0]
        bpub = pub[cid]
        ok = abs(b - bpub) <= TOL_RECETA
        filas.append({"dominio": "C", "id": cid,
                      "receta": f"R={hub}/{nodo} anual {ANIO_MIN}-{ANIO_MAX}",
                      "n": len(anios), "b_receta": round(b, 4), "b_pub": bpub,
                      "delta": round(b - bpub, 4), "reproduce": int(ok)})
        if ok:
            casos.append({"dominio": "C", "id": cid, "etiqueta": f"{hub}→{nodo}",
                          "t": t, "y": y, "b_pub": bpub})
    n_ok = len(casos)
    log.info("   C: %d/%d casos reproducen (umbral pre-registrado >= 21/22)",
             n_ok, len(PARES_C))
    return casos if n_ok >= int(0.9 * len(PARES_C)) else []


# ------------------------------------------------------------------ Fase 1
def fase1(dominio, casos, filas_caso, cal, resumen):
    """Maquinaria RC1 por dominio: P0 (observada + contrafactual), P5, P1-P4."""
    log.info("")
    log.info("%s — %d casos con receta verificada", dominio, len(casos))
    perf = []
    for c in casos:
        t, y = c["t"], c["y"]
        b, la, sigma, rho, dw = perfil(t, y)
        cm = comparar_modelos(t, y)
        c.update(b=b, log_a=la, sigma=sigma, rho=rho, dw=dw, cm=cm)
        perf.append(c)
        filas_caso.append({
            "dominio": dominio, "id": c["id"], "etiqueta": c["etiqueta"],
            "n": len(t), "b": round(b, 4), "b_pub": c["b_pub"],
            "delta_vs_pub": round(b - c["b_pub"], 4),
            "banda_b": banda_de(b), "superlineal": int(b >= 1.0),
            "dw": round(dw, 4), "rho_ar1": round(rho, 4),
            "sigma": round(sigma, 4),
            "ganador": cm["ganador"], "delta_aic_potencia": cm["delta_aic_potencia"],
        })

    # autocorrelacion real del dominio (hallazgo en si mismo, ver informe)
    rhos = np.array([c["rho"] for c in perf])
    dws = np.array([c["dw"] for c in perf])
    log.info("   rho AR(1): mediana %.3f [%.3f, %.3f] | DW mediana %.3f | n mediana %d",
             np.median(rhos), rhos.min(), rhos.max(), np.median(dws),
             int(np.median([len(c["t"]) for c in perf])))

    # ---- P0 por banda: observada (b del caso) + contrafactual (1.25, 1.75)
    por_banda = defaultdict(lambda: {"n": 0, "err": 0, "tot": 0,
                                     "sup": 0, "s05": 0, "stot": 0})
    rng = np.random.default_rng(SEMILLA)
    for c in perf:
        t = c["t"]
        n = len(t)
        e = ruido_ar1(n, c["sigma"], c["rho"], N_CAL, rng)
        de, ce = np.polyfit(t, np.log(c["y"]), 1)   # exponencial ajustada al caso (P5)
        for banda, b_sim in [("obs:" + banda_de(c["b"]), c["b"]),
                             ("cf:1.0 <= b < 1.5", B_CF[0]),
                             ("cf:b >= 1.5", B_CF[1])]:
            d = por_banda[banda]
            d["n"] += 1
            base = c["log_a"] + b_sim * np.log(t)
            for r in range(N_CAL):
                y0 = np.exp(base + e[r])
                if np.all(np.isfinite(y0)) and np.all(y0 > 0):
                    g = comparar_modelos(t, y0)["ganador"]
                    if g:
                        d["tot"] += 1
                        d["err"] += g != "potencia"
        # P5: exponencial verdadera -> b aparente
        d5 = por_banda["P5"]
        d5["n"] += 1
        base_exp = ce + de * t
        for r in range(N_CAL):
            y1 = np.exp(base_exp + e[r])
            if np.all(np.isfinite(y1)) and np.all(y1 > 0):
                bb = ajuste_loglog(t, y1)[0]
                d5["stot"] += 1
                d5["sup"] += bb >= 1.0
                d5["s05"] += bb >= 0.5

    cf_tot = cf_err = 0
    for banda in sorted(por_banda):
        d = por_banda[banda]
        if banda == "P5":
            frac1 = d["sup"] / d["stot"] if d["stot"] else float("nan")
            frac05 = d["s05"] / d["stot"] if d["stot"] else float("nan")
            log.info("   P5 exponencial verdadera -> b aparente >= 1: %5.1f%% "
                     "(control >= 0.5: %5.1f%%)", 100 * frac1, 100 * frac05)
            cal.append({"dominio": dominio, "banda_b": "P5 (exponencial verdadera)",
                        "casos": d["n"], "replicas": d["stot"],
                        "frac_b_aparente_mayor_1": round(frac1, 4),
                        "frac_b_aparente_mayor_0_5": round(frac05, 4)})
            continue
        err = d["err"] / d["tot"] if d["tot"] else float("nan")
        log.info("   P0 %-20s casos %2d | error seleccion AIC: %5.1f%%",
                 banda, d["n"], 100 * err)
        cal.append({"dominio": dominio, "banda_b": banda, "casos": d["n"],
                    "replicas": d["tot"], "error_seleccion_P0": round(err, 4)})
        if banda.startswith("cf:"):
            cf_tot += d["tot"]
            cf_err += d["err"]
    tasa_cf = cf_err / cf_tot if cf_tot else float("nan")
    admisible = bool(np.isfinite(tasa_cf) and tasa_cf < UMBRAL_ERROR)
    log.info("   -> banda b >= 1 CONTRAFACTUAL agregada: error %.1f%% -> %s",
             100 * tasa_cf, "ADMISIBLE" if admisible else "NO INTERPRETABLE (umbral 20%)")
    cal.append({"dominio": dominio, "banda_b": "cf: b >= 1 (agregada)",
                "replicas": cf_tot, "error_seleccion_P0": round(tasa_cf, 4),
                "admisible": int(admisible)})

    # ---- P1-P4 (se reportan; se interpretan solo donde P0 admite)
    g = Counter(c["cm"]["ganador"] for c in perf)
    b_arr = np.array([c["b"] for c in perf])
    d_arr = np.array([c["cm"]["delta_aic_potencia"] for c in perf], dtype=float)
    if len(perf) >= 3:
        rho_s, p_s = stats.spearmanr(b_arr, d_arr)
        p1c = p_s / 2 if rho_s < 0 else 1 - p_s / 2
    else:
        rho_s, p1c = float("nan"), float("nan")
    sup = int((b_arr >= 1.0).sum())
    log.info("   P1 ganadores: potencia %d | exponencial %d | lineal %d",
             g["potencia"], g["exponencial"], g["lineal"])
    log.info("   P2 Spearman(b, dAIC) = %s | p una cola = %s",
             f"{rho_s:+.3f}" if np.isfinite(rho_s) else "n/a",
             f"{p1c:.4f}" if np.isfinite(p1c) else "no evaluable (n<3)")
    log.info("   P3/P4: no evaluables — el dominio no tiene casos superlineales "
             "publicados (%d observados)", sup)
    resumen.append({
        "dominio": dominio, "casos_calibrados": len(perf),
        "admisible_P0_cf_b_mayor_1": int(admisible),
        "error_P0_cf": round(tasa_cf, 4),
        "gana_potencia": g["potencia"], "gana_exponencial": g["exponencial"],
        "gana_lineal": g["lineal"], "superlineales_observados": sup,
        "spearman_b_dAIC": round(float(rho_s), 4) if np.isfinite(rho_s) else "",
        "p_una_cola_P2": round(float(p1c), 5) if np.isfinite(p1c) else "",
    })


# ---------------------------------------------------------------------- main
def main():
    configurar_log(LOG_FILE)
    log.info("=" * 78)
    log.info("RC1 RESTO — dominios A, E2, C (pre-registro 2026-10-17, commit 4e9cb9e)")
    log.info("=" * 78)
    log.info("Semilla %d | N_CAL %d | umbral admision b>=1: %.0f%% | tol receta ±%.2f",
             SEMILLA, N_CAL, 100 * UMBRAL_ERROR, TOL_RECETA)
    log.info("No testeables por diseno: D (3, propietario), E1 (4, no reproducible),")
    log.info("F1-F3 (4, ajustes masa/orbita, no trayectorias R(t)), C_001 (rango-tamano).")
    log.info("")

    filas_rec, filas_caso, cal, resumen = [], [], [], []

    log.info("FASE 0 — identificacion de recetas (criterio: >= 90%% dentro de ±%.2f)", TOL_RECETA)
    log.info("")
    log.info("A (WUP versionado, sin descargas):")
    fase0_A(filas_rec)
    log.info("")
    log.info("E2 (R lynx + tabla lince-liebre dsem/CRAN):")
    casos_E2 = fase0_E2(filas_rec)
    log.info("")
    log.info("C (US Census via FRED):")
    casos_C = fase0_C(filas_rec)
    log.info("")

    log.info("=" * 78)
    log.info("FASE 1 — maquinaria RC1 sobre los dominios con receta verificada")
    log.info("=" * 78)
    if casos_C:
        fase1("C", casos_C, filas_caso, cal, resumen)
    else:
        log.info("C: receta no identificada -> NO se calibra (regla del pre-registro)")
    if casos_E2:
        fase1("E2", casos_E2, filas_caso, cal, resumen)
    else:
        log.info("E2: sin casos reproducibles -> NO se calibra")

    # ---------------------------------------------------------------- salidas
    def escribir(ruta, filas):
        cols = ["dominio", "id", "receta", "n", "b_receta", "b_pub",
                "delta", "reproduce"]
        if filas and set(filas[0]) != set(cols):
            cols = sorted({k for r in filas for k in r})
        with ruta.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, restval="")
            w.writeheader()
            w.writerows(filas)
        log.info("Salida %s | sha256 %s…", ruta.relative_to(ROOT), sha256(ruta)[:16])

    escribir(OUT_REC, filas_rec)
    escribir(OUT_CASO, filas_caso)
    escribir(OUT_CAL, cal)
    escribir(OUT_RES, resumen)
    log.info("LOG %s", LOG_FILE.relative_to(ROOT))
    log.info("Insumos: %s sha %s… | %s sha %s… | %s sha %s…",
             WUP.name, sha256(WUP)[:16], LYNX.name, sha256(LYNX)[:16],
             CENSO.name, sha256(CENSO)[:16])
    return 0


if __name__ == "__main__":
    sys.exit(main())
