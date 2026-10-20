"""Secundaria del pre-registro: el mismo analisis sobre cantidades per capita.

Pre-registro: reconstruction_real/preregistro/PREREGISTRO_RANGO_TAMANO_2026-10-02.md
(commit 5b97328), seccion 1: "Secundaria: se repite todo con per capita donde
exista (Eurostat EUR_HAB, y Mexico con pib_pc), para medir cuanto del veredicto
depende de la cantidad elegida."

Esa es toda la razon de ser de este archivo. La corrida principal usa PIB
total, que es la cantidad de tipo Zipf y la unica disponible en los seis
niveles; el per capita abarca muchisimo menos rango dinamico, y el fracaso de
Mexico vino justamente de usarlo. Aqui se mide ese efecto en lugar de
suponerlo.

Brasil queda fuera: la tabla 5938 del IBGE no publica per capita, como ya
quedo anotado en el pre-registro. Quedan los tres niveles NUTS de la UE y
Mexico, de n = 32 a n = 1,342.

Mexico con pib_pc es, ademas, una prueba de consistencia: es exactamente la
serie de nbody_lognormal_clauset.py, asi que su dAIC debe reproducir el 65.04
ya publicado en audits/RESULTADOS_LOGNORMAL_2026-10-02.md.

    P1. Curva rango-tamano: potencia contra lognormal, por AIC, en cada nivel.
    P2. Poder contra n: tasa de falso "sobrevive" por nivel.
    P3. Veredicto de Clauset donde el poder alcanza (tasa < 20%).

Salidas:
    data/raw_rango_tamano/                              (no versionado)
    reconstruction_real/data/rango_tamano_percapita.csv
    reconstruction_real/logs/rango_tamano_percapita_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/rango_tamano_percapita.py
"""

import csv
import logging
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nbody_lognormal_clauset import (ajustar_potencia, bondad_ajuste,  # noqa: E402
                                     vuong)
from rango_tamano_internacional import (ALFA, ANIO, BOOT_GOF,  # noqa: E402
                                        EUROSTAT, LOG_DIR, MEXICO, OUT,
                                        P_DESCARTE, ROOT, SEMILLA,
                                        UMBRAL_PODER, bajar, configurar_log,
                                        es_region, poder, rango_tamano,
                                        veredicto)

SALIDA = ROOT / "reconstruction_real" / "data" / "rango_tamano_percapita.csv"
LOG_FILE = LOG_DIR / "rango_tamano_percapita_log.txt"

log = logging.getLogger("PER-CAPITA")


def cargar_niveles():
    """Devuelve [(etiqueta, valores, fuente, sha)] con cantidades per capita."""
    niveles = []

    d, h = bajar(EUROSTAT.format(unit="EUR_HAB"), f"eurostat_eur_hab_{ANIO}.json")
    indices = d["dimension"]["geo"]["category"]["index"]
    valores = d["value"]
    for largo, etiqueta in ((3, "UE NUTS1"), (4, "UE NUTS2"), (5, "UE NUTS3")):
        v = []
        for codigo, i in indices.items():
            if len(codigo) != largo or not es_region(codigo):
                continue
            x = valores.get(str(i))
            if x is not None and x > 0:
                v.append(float(x))
        niveles.append((etiqueta, np.array(v),
                        "Eurostat nama_10r_3gdp EUR_HAB", h))

    with MEXICO.open(encoding="utf-8-sig") as fh:
        filas = list(csv.DictReader(fh))
    v = np.array([float(r["pib_pc"]) for r in filas if float(r["pib_pc"]) > 0])
    niveles.append(("Mexico entidades", v, "matriz_mexico_32.csv pib_pc", "—"))

    niveles.sort(key=lambda t: len(t[1]))
    return niveles


def daic_principal():
    """dAIC de la corrida principal (PIB total), para ponerlos uno al lado del otro."""
    if not OUT.exists():
        return {}
    with OUT.open(encoding="utf-8") as fh:
        return {f["nivel"]: float(f["daic"]) for f in csv.DictReader(fh)}


def main():
    configurar_log(LOG_FILE)
    rng = np.random.default_rng(SEMILLA)
    previo = daic_principal()

    log.info("=" * 78)
    log.info("RANGO-TAMANO PER CAPITA — secundaria del pre-registro 2026-10-02")
    log.info("=" * 78)
    log.info("Brasil no entra: la tabla 5938 del IBGE no publica per capita.")
    log.info("Descargando:")
    niveles = cargar_niveles()

    log.info("")
    log.info("=" * 78)
    log.info("P1. CURVA RANGO-TAMANO CON CANTIDADES PER CAPITA")
    log.info("=" * 78)
    log.info("'ordenes' es el rango dinamico log10(max/min): es la magnitud que "
             "Clauset et al. (2009) senalan como decisiva.")
    log.info("%-20s %6s %8s %8s %10s %10s  %s", "nivel", "n", "b", "ordenes",
             "dAIC pc", "dAIC total", "veredicto per capita")

    filas, ajustes = [], {}
    for etiqueta, v, fuente, sha in niveles:
        a = rango_tamano(v)
        ajustes[etiqueta] = (a, v, fuente, sha)
        ordenes = float(np.log10(v.max() / v.min()))
        d = a["daic"]
        ver = veredicto(d)
        antes = previo.get(etiqueta)
        log.info("%-20s %6d %8.4f %8.2f %10.1f %10s  %s", etiqueta, a["n"],
                 a["b"], ordenes, d,
                 "—" if antes is None else f"{antes:.1f}", ver)
        filas.append({
            "nivel": etiqueta, "n": a["n"], "fuente": fuente, "sha256": sha,
            "ordenes_magnitud": round(ordenes, 3),
            "b": round(a["b"], 4), "mu": round(a["mu"], 4),
            "sigma": round(a["sigma"], 4),
            "r2_log_potencia": round(a["r2_log_potencia"], 4),
            "r2_raw_potencia": round(a["r2_raw_potencia"], 4),
            "r2_log_lognormal": round(a["r2_log_lognormal"], 4),
            "r2_raw_lognormal": round(a["r2_raw_lognormal"], 4),
            "daic": round(d, 2), "veredicto_p1": ver,
            "daic_pib_total": "" if antes is None else round(antes, 2),
        })

    mex = next((f for f in filas if f["nivel"] == "Mexico entidades"), None)
    if mex is not None:
        log.info("")
        log.info("Consistencia con nbody_lognormal_clauset.py (Mexico, pib_pc): "
                 "dAIC = %.2f; el publicado es 65.04.", mex["daic"])

    log.info("")
    log.info("=" * 78)
    log.info("P2. PODER CONTRA TAMANO DE MUESTRA, CON PER CAPITA")
    log.info("=" * 78)
    log.info("%-20s %6s %22s  %s", "nivel", "n", "falso 'sobrevive'", "poder")
    tasas = {}
    for etiqueta, v, _, _ in niveles:
        t = poder(v, rng)
        tasas[etiqueta] = t
        ok = t < UMBRAL_PODER
        log.info("%-20s %6d %21.1f%%  %s", etiqueta, len(v), 100 * t,
                 "SUFICIENTE" if ok else "insuficiente")
        fila = next(f for f in filas if f["nivel"] == etiqueta)
        fila["tasa_falso_sobrevive"] = round(t, 4)
        fila["poder_suficiente"] = int(ok)

    log.info("")
    log.info("=" * 78)
    log.info("P3. VEREDICTO DE CLAUSET DONDE EL PODER ALCANZA (< %.0f%%)",
             100 * UMBRAL_PODER)
    log.info("=" * 78)
    interpretables = [e for e, t in tasas.items() if t < UMBRAL_PODER]
    if not interpretables:
        log.warning("Ningun nivel per capita alcanza el umbral de poder: "
                    "P3 no se interpreta.")
    for etiqueta in [e for e, _, _, _ in niveles if e in interpretables]:
        _, v, _, _ = ajustes[etiqueta]
        aj = ajustar_potencia(v)
        p_gof = bondad_ajuste(v, aj, rng, replicas=BOOT_GOF)
        fila = next(f for f in filas if f["nivel"] == etiqueta)
        log.info("")
        log.info("%s (n = %d, falso 'sobrevive' %.1f%%)", etiqueta, len(v),
                 100 * tasas[etiqueta])
        log.info("   alpha = %.3f | x_min = %.4g | cola = %d (%.0f%%) | KS = %.4f",
                 aj["alpha"], aj["xmin"], aj["n_cola"],
                 100 * aj["n_cola"] / len(v), aj["ks"])
        ver_gof = ("LA LEY DE POTENCIA SE DESCARTA" if p_gof < P_DESCARTE
                   else "no se descarta")
        log.info("   bondad de ajuste: p = %.3f -> %s", p_gof, ver_gof)
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
    cols = ["nivel", "n"] + [c for c in cols if c not in ("nivel", "n")]
    with SALIDA.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, restval="")
        w.writeheader()
        w.writerows(filas)

    log.info("")
    log.info("=" * 78)
    log.info("RESUMEN")
    log.info("=" * 78)
    gana_ln = sum(1 for f in filas if f["daic"] > 2)
    gana_pot = sum(1 for f in filas if f["daic"] < -2)
    log.info("P1: con per capita la lognormal gana en %d de %d niveles y la "
             "potencia en %d", gana_ln, len(filas), gana_pot)
    log.info("P2: el poder va de %.0f%% de falsos (n = %d) a %.0f%% (n = %d)",
             100 * tasas[niveles[0][0]], len(niveles[0][1]),
             100 * tasas[niveles[-1][0]], len(niveles[-1][1]))
    log.info("P3: niveles interpretables: %s",
             ", ".join(interpretables) if interpretables else "ninguno")
    log.info("Resultados -> %s", SALIDA.relative_to(ROOT))
    log.info("LOG        -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
