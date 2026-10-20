"""Diagnostico EXPLORATORIO: en la curva rango-tamano, que decide el veredicto,
el tamano de muestra o el rango dinamico.

NO ESTA PRE-REGISTRADO. Se escribe despues de ver los resultados de
rango_tamano_internacional.py y se reporta como analisis post hoc, nunca como
confirmacion. Su unico proposito es evitar que el informe se quede en "podria
ser n, podria ser el rango, no se puede saber" cuando los datos si permiten
separar las dos cosas.

El problema: de los seis niveles de la corrida principal, cinco favorecen a la
lognormal y uno a la ley de potencia, los 5,570 municipios de Brasil. Ese nivel
es a la vez el de mayor n (5,570) y el de mayor rango dinamico (4.66 ordenes de
magnitud), asi que ambos factores quedan confundidos. En la UE pasa lo
contrario y por eso n solo no explica nada: NUTS3 tiene n = 1,327 y da el mayor
margen a favor de la lognormal de toda la tabla (dAIC = +4,868), mas que NUTS2
con n = 293 (+815).

La forma de separarlos es quedarse dentro de Brasil municipios y mover un
factor a la vez:

    A. n variable, rango libre      — submuestra aleatoria simple. Al bajar n
                                      el rango tambien se encoge solo, porque
                                      los extremos se pierden. Es la linea
                                      base, donde ambos factores se mueven.
    B. n variable, rango FIJO       — igual que A pero forzando que el maximo y
                                      el minimo global siempre entren. El rango
                                      queda clavado en 4.66 ordenes y lo unico
                                      que cambia es n.
    C. n FIJO, rango variable       — n = 1,327 (el de UE NUTS3) con tres
                                      reglas de seleccion que dan rangos
                                      distintos: los 1,327 mas grandes, un
                                      bloque contiguo del medio, y el de rango
                                      maximo.

Si el veredicto sigue a n, B deberia voltearse a lognormal al bajar n. Si
sigue al rango, B deberia mantener la potencia en todos los n, y C deberia
voltearse en cuanto el rango se recorte.

Salidas:
    reconstruction_real/data/rango_tamano_diagnostico.csv
    reconstruction_real/logs/rango_tamano_diagnostico_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/rango_tamano_diagnostico.py
"""

import csv
import logging
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rango_tamano_internacional import (LOG_DIR, ROOT, SEMILLA,  # noqa: E402
                                        cargar_niveles, configurar_log,
                                        rango_tamano, veredicto)

SALIDA = ROOT / "reconstruction_real" / "data" / "rango_tamano_diagnostico.csv"
LOG_FILE = LOG_DIR / "rango_tamano_diagnostico_log.txt"

REPLICAS = 200
REJILLA_N = (27, 111, 293, 1327, 2785)

log = logging.getLogger("DIAGNOSTICO")


def ordenes(v):
    """Rango dinamico en ordenes de magnitud."""
    return float(np.log10(v.max() / v.min()))


def resumen(muestras):
    """dAIC mediano, rango mediano y fraccion de veredictos a favor de la potencia."""
    daics = np.array([rango_tamano(m)["daic"] for m in muestras])
    rangos = np.array([ordenes(m) for m in muestras])
    return {
        "daic_mediano": float(np.median(daics)),
        "daic_p05": float(np.percentile(daics, 5)),
        "daic_p95": float(np.percentile(daics, 95)),
        "ordenes_mediano": float(np.median(rangos)),
        "frac_potencia": float(np.mean(daics < -2)),
        "frac_lognormal": float(np.mean(daics > 2)),
    }


def submuestra(v, n, rng, forzar_extremos):
    """Submuestra de tamano n; con forzar_extremos el rango queda intacto."""
    if not forzar_extremos:
        return rng.choice(v, size=n, replace=False)
    orden = np.sort(v)
    medio = orden[1:-1]
    resto = rng.choice(medio, size=n - 2, replace=False)
    return np.concatenate([[orden[0], orden[-1]], resto])


def main():
    configurar_log(LOG_FILE)
    rng = np.random.default_rng(SEMILLA)

    log.info("=" * 78)
    log.info("DIAGNOSTICO EXPLORATORIO (POST HOC, NO PRE-REGISTRADO)")
    log.info("n contra rango dinamico en la curva rango-tamano")
    log.info("=" * 78)

    niveles = dict((e, v) for e, v, _, _ in cargar_niveles())
    v = niveles["Brasil municipios"]
    log.info("Datos: Brasil municipios, n = %d, rango = %.2f ordenes",
             len(v), ordenes(v))
    a = rango_tamano(v)
    log.info("Ajuste completo: b = %.4f | dAIC = %+.1f -> %s",
             a["b"], a["daic"], veredicto(a["daic"]))
    log.info("Referencia de la UE: NUTS3 tiene n = 1,327 con 3.11 ordenes y "
             "dAIC = +4,868.5 (gana la lognormal).")
    log.info("Convencion de signo: dAIC > 0 favorece la LOGNORMAL, "
             "dAIC < 0 la POTENCIA.")

    filas = []

    for etiqueta, forzar in (("A. rango libre", False),
                             ("B. rango fijo en 4.66", True)):
        log.info("")
        log.info("=" * 78)
        log.info("%s — %d replicas por tamano", etiqueta, REPLICAS)
        log.info("=" * 78)
        log.info("%6s %9s %12s %22s %11s", "n", "ordenes", "dAIC mediano",
                 "intervalo 5–95%", "gana pot.")
        for n in REJILLA_N:
            if n > len(v):
                continue
            muestras = [submuestra(v, n, rng, forzar) for _ in range(REPLICAS)]
            r = resumen(muestras)
            log.info("%6d %9.2f %12.1f %10.1f a %+9.1f %10.0f%%", n,
                     r["ordenes_mediano"], r["daic_mediano"], r["daic_p05"],
                     r["daic_p95"], 100 * r["frac_potencia"])
            filas.append(dict(experimento=etiqueta, n=n, replicas=REPLICAS,
                              **{k: round(x, 4) for k, x in r.items()}))

    log.info("")
    log.info("=" * 78)
    log.info("C. n FIJO en 1,327 (el de UE NUTS3), tres rangos distintos")
    log.info("=" * 78)
    orden = np.sort(v)
    n_fijo = 1327
    inicio = (len(v) - n_fijo) // 2
    reglas = (
        ("los 1,327 mas grandes", orden[-n_fijo:]),
        ("bloque contiguo del medio", orden[inicio:inicio + n_fijo]),
        ("rango maximo (con extremos)", submuestra(v, n_fijo, rng, True)),
    )
    log.info("%-30s %9s %12s  %s", "regla de seleccion", "ordenes", "dAIC",
             "veredicto")
    for nombre, m in reglas:
        aj = rango_tamano(m)
        log.info("%-30s %9.2f %12.1f  %s", nombre, ordenes(m), aj["daic"],
                 veredicto(aj["daic"]))
        filas.append({"experimento": "C. n fijo 1327", "n": n_fijo,
                      "replicas": 1, "regla": nombre,
                      "ordenes_mediano": round(ordenes(m), 4),
                      "daic_mediano": round(aj["daic"], 4),
                      "frac_potencia": int(aj["daic"] < -2),
                      "frac_lognormal": int(aj["daic"] > 2)})

    cols = sorted({k for f in filas for k in f})
    cols = ["experimento", "n"] + [c for c in cols
                                   if c not in ("experimento", "n")]
    with SALIDA.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, restval="")
        w.writeheader()
        w.writerows(filas)

    log.info("")
    log.info("Resultados -> %s", SALIDA.relative_to(ROOT))
    log.info("LOG        -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
