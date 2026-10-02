"""
Replica internacional del hallazgo de rango-tamano del Modulo de N-cuerpos.

Pre-registro: reconstruction_real/preregistro/PREREGISTRO_RANGO_TAMANO_2026-10-02.md
(commit 5b97328, subido antes de descargar ningun dato de Brasil ni de la UE).

Mexico dejo claro que la lognormal le gana a la ley de potencia en la curva
rango-tamano (dAIC = 65), pero con n = 32 no pudo decidir si eso es general: la
prueba de Clauset tenia una tasa de falso "sobrevive" del 96.4%. Aqui se repite
en seis niveles territoriales, de 27 a 5,570 unidades.

    P1. Curva rango-tamano: potencia contra lognormal, por AIC, en cada nivel.
    P2. Poder contra n: tasa de falso "sobrevive" por nivel.
    P3. Veredicto de Clauset donde el poder alcanza (tasa < 20%).

Salidas:
    data/raw_rango_tamano/                              (no versionado)
    reconstruction_real/data/rango_tamano_internacional.csv
    reconstruction_real/data/rango_tamano_poder.csv
    reconstruction_real/logs/rango_tamano_internacional_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/rango_tamano_internacional.py
"""

import csv
import gzip
import hashlib
import json
import logging
import math
import sys
import urllib.request
from pathlib import Path

import numpy as np
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nbody_lognormal_clauset import (ajustar_potencia, bondad_ajuste,  # noqa: E402
                                     vuong)

ROOT = Path(__file__).resolve().parent.parent.parent
RAW = ROOT / "data" / "raw_rango_tamano"
RAW.mkdir(parents=True, exist_ok=True)
MEXICO = ROOT / "data" / "matriz_mexico_32.csv"
OUT = ROOT / "reconstruction_real" / "data" / "rango_tamano_internacional.csv"
OUT_PODER = ROOT / "reconstruction_real" / "data" / "rango_tamano_poder.csv"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "rango_tamano_internacional_log.txt"

SEMILLA = 20261002
N_PODER = 500
BOOT_PODER = 100
BOOT_GOF = 2000
UMBRAL_PODER = 0.20       # un nivel se interpreta si su tasa de falso < 20%
P_DESCARTE = 0.1
ALFA = 0.05
ANIO = "2021"

IBGE = "https://apisidra.ibge.gov.br/values/t/5938/{niv}/all/v/37/p/" + ANIO
EUROSTAT = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/"
            "data/nama_10r_3gdp?format=JSON&time=" + ANIO + "&unit={unit}")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
      "Accept-Encoding": "gzip"}

log = logging.getLogger("RANGO-TAMANO")


def configurar_log(ruta=LOG_FILE):
    """Solo al ejecutarse como programa, nunca al importarse.

    Este modulo se importa desde rango_tamano_percapita.py. Si configurara el
    registro al importarse, abriria LOG_FILE en modo "w" y borraria el log de
    la corrida principal: es exactamente la falla que ya ocurrio el 2026-10-02
    con nbody_lognormal_clauset.py.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        handlers=[
            logging.FileHandler(ruta, mode="w", encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def bajar(url, nombre):
    """Descarga con cache en disco y SHA-256 anotado."""
    destino = RAW / nombre
    if not destino.exists():
        with urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=300) as r:
            crudo = r.read()
            if r.headers.get("Content-Encoding") == "gzip" or crudo[:2] == b"\x1f\x8b":
                crudo = gzip.decompress(crudo)
        destino.write_bytes(crudo)
    crudo = destino.read_bytes()
    h = hashlib.sha256(crudo).hexdigest()
    log.info("   %s | %s bytes | SHA-256 %s", nombre, f"{len(crudo):,}", h[:16])
    return json.loads(crudo), h


def es_region(codigo):
    """Falso para los codigos "extra-regio" de Eurostat.

    No estaban previstos en las exclusiones del pre-registro, que solo
    descartaba agregados y codigos de otra longitud. Pero Eurostat publica,
    por pais y por nivel, un codigo residual (BEZ/BEZZ/BEZZZ, FRZ/FRZZ/FRZZZ,
    ...) etiquetado "Extra-Regio": la actividad economica que no puede
    asignarse a ninguna region (embajadas, plataformas marinas, buques). Son
    16 en cada nivel NUTS, tienen la longitud correcta y por eso pasaban el
    filtro, pero NO son unidades territoriales: en la corrida descartada del
    2026-10-02 15:25 ocupaban toda la cola baja (desde 22.62 MIO_EUR) e
    inflaban el rango dinamico de la UE a 4.5 ordenes de magnitud, que es
    justo la cantidad decisiva del metodo de Clauset.
    """
    return set(codigo[2:]) != {"Z"}


def cargar_niveles():
    """Devuelve [(etiqueta, valores, fuente, sha)] segun el pre-registro."""
    niveles = []

    for niv, etiqueta in (("n3", "Brasil estados"), ("n6", "Brasil municipios")):
        d, h = bajar(IBGE.format(niv=niv), f"ibge_{niv}_{ANIO}.json")
        v = []
        for fila in d[1:]:                       # la fila 0 es la cabecera
            try:
                x = float(fila["V"])
            except (TypeError, ValueError):
                continue                          # valor ausente
            if x > 0:
                v.append(x)
        niveles.append((etiqueta, np.array(v), "IBGE SIDRA t/5938 v/37", h))

    d, h = bajar(EUROSTAT.format(unit="MIO_EUR"), f"eurostat_mio_eur_{ANIO}.json")
    geo = d["dimension"]["geo"]["category"]
    indices = geo["index"]
    valores = d["value"]
    for largo, etiqueta in ((3, "UE NUTS1"), (4, "UE NUTS2"), (5, "UE NUTS3")):
        v = []
        for codigo, i in indices.items():
            if len(codigo) != largo or not es_region(codigo):
                continue
            x = valores.get(str(i))
            if x is not None and x > 0:
                v.append(float(x))
        niveles.append((etiqueta, np.array(v), "Eurostat nama_10r_3gdp MIO_EUR", h))

    with MEXICO.open(encoding="utf-8-sig") as fh:
        filas = list(csv.DictReader(fh))
    v = np.array([float(r["pct_pib"]) for r in filas if float(r["pct_pib"]) > 0])
    niveles.append(("Mexico entidades", v, "matriz_mexico_32.csv pct_pib", "—"))

    niveles.sort(key=lambda t: len(t[1]))
    return niveles


# ------------------------------------------------------------------ P1
def veredicto(d):
    """Lectura de un dAIC con la convencion fijada en el pre-registro."""
    if abs(d) < 2:
        return "indistinguibles"
    fuerza = " (fuerte)" if abs(d) > 10 else " (moderada)"
    return ("LOGNORMAL" if d > 0 else "POTENCIA") + fuerza


def rango_tamano(v):
    """Ajusta potencia y cuantiles lognormales a la curva rango-tamano."""
    v = np.sort(v)[::-1]
    n = len(v)
    rango = np.arange(1, n + 1)

    b, a, _, _, _ = stats.linregress(np.log(rango), np.log(v))
    pred_pot = np.exp(a) * rango ** b
    mu, sg = float(np.mean(np.log(v))), float(np.std(np.log(v), ddof=1))
    pred_ln = np.exp(mu + sg * stats.norm.ppf(1 - (rango - 0.5) / n))

    out = {"b": b, "mu": mu, "sigma": sg, "n": n}
    for nombre, pred in (("potencia", pred_pot), ("lognormal", pred_ln)):
        rss = float(np.sum((np.log(v) - np.log(pred)) ** 2))
        out[f"r2_log_{nombre}"] = 1 - rss / float(
            np.sum((np.log(v) - np.mean(np.log(v))) ** 2))
        out[f"r2_raw_{nombre}"] = 1 - float(np.sum((v - pred) ** 2)) / float(
            np.sum((v - np.mean(v)) ** 2))
        out[f"aic_{nombre}"] = n * math.log(rss / n) + 4
    out["daic"] = out["aic_potencia"] - out["aic_lognormal"]
    return out


# ------------------------------------------------------------------ P2
def poder(v, rng):
    """Tasa de falso 'sobrevive' sobre muestras lognormales del mismo n."""
    mu, sg = float(np.mean(np.log(v))), float(np.std(np.log(v), ddof=1))
    sobreviven = 0
    for _ in range(N_PODER):
        sint = np.exp(rng.normal(mu, sg, len(v)))
        aj = ajustar_potencia(sint)
        if not np.isfinite(aj["ks"]):
            continue
        if bondad_ajuste(sint, aj, rng, replicas=BOOT_PODER) >= P_DESCARTE:
            sobreviven += 1
    return sobreviven / N_PODER


# ------------------------------------------------------------------ main
def main():
    configurar_log()
    rng = np.random.default_rng(SEMILLA)
    log.info("=" * 78)
    log.info("RANGO-TAMANO INTERNACIONAL — pre-registro 2026-10-02 (5b97328)")
    log.info("=" * 78)
    log.info("Descargando:")
    niveles = cargar_niveles()

    filas, filas_poder = [], []
    log.info("")
    log.info("=" * 78)
    log.info("P1. CURVA RANGO-TAMANO: POTENCIA CONTRA LOGNORMAL")
    log.info("=" * 78)
    log.info("%-20s %6s %8s %9s %9s %10s  %s", "nivel", "n", "b",
             "R2c pot", "R2c logn", "dAIC", "veredicto")

    ajustes = {}
    for etiqueta, v, fuente, sha in niveles:
        a = rango_tamano(v)
        ajustes[etiqueta] = (a, v, fuente, sha)
        d = a["daic"]
        ver = veredicto(d)
        log.info("%-20s %6d %8.4f %9.4f %9.4f %10.1f  %s", etiqueta, a["n"],
                 a["b"], a["r2_raw_potencia"], a["r2_raw_lognormal"], d, ver)
        filas.append({
            "nivel": etiqueta, "n": a["n"], "fuente": fuente, "sha256": sha,
            "b": round(a["b"], 4), "mu": round(a["mu"], 4),
            "sigma": round(a["sigma"], 4),
            "r2_log_potencia": round(a["r2_log_potencia"], 4),
            "r2_raw_potencia": round(a["r2_raw_potencia"], 4),
            "r2_log_lognormal": round(a["r2_log_lognormal"], 4),
            "r2_raw_lognormal": round(a["r2_raw_lognormal"], 4),
            "daic": round(d, 2), "veredicto_p1": ver,
        })

    log.info("")
    log.info("=" * 78)
    log.info("P2. PODER CONTRA TAMANO DE MUESTRA")
    log.info("=" * 78)
    log.info("Tasa de falso 'sobrevive': fraccion de %d muestras LOGNORMALES en "
             "las que la ley de potencia resulta no descartable.", N_PODER)
    log.info("%-20s %6s %22s  %s", "nivel", "n", "falso 'sobrevive'", "poder")
    tasas = {}
    for etiqueta, v, _, _ in niveles:
        t = poder(v, rng)
        tasas[etiqueta] = t
        ok = t < UMBRAL_PODER
        log.info("%-20s %6d %21.1f%%  %s", etiqueta, len(v), 100 * t,
                 "SUFICIENTE" if ok else "insuficiente")
        filas_poder.append({"nivel": etiqueta, "n": len(v),
                            "tasa_falso_sobrevive": round(t, 4),
                            "poder_suficiente": int(ok)})

    log.info("")
    log.info("=" * 78)
    log.info("P3. VEREDICTO DE CLAUSET DONDE EL PODER ALCANZA (< %.0f%%)",
             100 * UMBRAL_PODER)
    log.info("=" * 78)
    interpretables = [e for e, t in tasas.items() if t < UMBRAL_PODER]
    if not interpretables:
        log.warning("Ningun nivel alcanza el umbral de poder: P3 no se interpreta.")
    for etiqueta in [e for e, _, _, _ in niveles if e in interpretables]:
        a, v, _, _ = ajustes[etiqueta]
        aj = ajustar_potencia(v)
        p_gof = bondad_ajuste(v, aj, rng, replicas=BOOT_GOF)
        log.info("")
        log.info("%s (n = %d, falso 'sobrevive' %.1f%%)", etiqueta, len(v),
                 100 * tasas[etiqueta])
        log.info("   alpha = %.3f | x_min = %.4g | cola = %d (%.0f%%) | KS = %.4f",
                 aj["alpha"], aj["xmin"], aj["n_cola"],
                 100 * aj["n_cola"] / len(v), aj["ks"])
        ver_gof = ("LA LEY DE POTENCIA SE DESCARTA" if p_gof < P_DESCARTE
                   else "no se descarta")
        log.info("   bondad de ajuste: p = %.3f -> %s", p_gof, ver_gof)
        fila = next(f for f in filas if f["nivel"] == etiqueta)
        fila["clauset_alpha"] = round(aj["alpha"], 3)
        fila["clauset_p_gof"] = round(p_gof, 4)
        fila["clauset_veredicto"] = ver_gof
        for alt in ("lognormal", "exponencial"):
            R, pv = vuong(v, aj["xmin"], aj["alpha"], alt)
            if not np.isfinite(pv) or pv >= ALFA:
                ver = "indistinguible"
            elif R > 0:
                ver = "favorece la POTENCIA"
            else:
                ver = f"favorece la {alt.upper()}"
            log.info("   Vuong contra %-12s: R = %+.2f | p = %.4f -> %s",
                     alt, R, pv, ver)
            fila[f"vuong_{alt}_R"] = round(R, 3)
            fila[f"vuong_{alt}_p"] = round(pv, 4)
            fila[f"vuong_{alt}_veredicto"] = ver

    cols = sorted({k for f in filas for k in f})
    cols = (["nivel", "n"] + [c for c in cols if c not in ("nivel", "n")])
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(filas)
    with OUT_PODER.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas_poder[0].keys()))
        w.writeheader()
        w.writerows(filas_poder)

    log.info("")
    log.info("=" * 78)
    log.info("RESUMEN")
    log.info("=" * 78)
    gana_ln = sum(1 for f in filas if f["daic"] > 2)
    log.info("P1: la lognormal gana en %d de %d niveles", gana_ln, len(filas))
    log.info("P2: el poder pasa de %.0f%% de falsos a %.0f%% entre n = %d y n = %d",
             100 * tasas[niveles[0][0]], 100 * tasas[niveles[-1][0]],
             len(niveles[0][1]), len(niveles[-1][1]))
    log.info("P3: niveles interpretables: %s",
             ", ".join(interpretables) if interpretables else "ninguno")
    log.info("Resultados -> %s", OUT.relative_to(ROOT))
    log.info("Poder      -> %s", OUT_PODER.relative_to(ROOT))
    log.info("LOG        -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
