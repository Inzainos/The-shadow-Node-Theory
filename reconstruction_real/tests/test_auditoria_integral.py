#!/usr/bin/env python3
"""Regresión: la auditoría integral v32 reproduce sus propias cifras.

Re-ejecuta `snt_auditoria_integral_v32.run` hacia un archivo temporal (no toca
el CSV versionado) y lo compara con `data/auditoria_integral_v32_resultados.csv`:

  * El ESTADO de cada cifra (REPLICA, OK, NO_REPRODUCIBLE, CIRCULAR, ...) debe
    ser idéntico. Si una cifra pasa de REPLICA a otro estado, algún cambio en
    datos o código rompió una reproducción y esto debe verse en CI.
  * Los valores numéricos recomputados deben coincidir dentro de una tolerancia
    relativa de 1e-9, que absorbe diferencias de última cifra entre versiones
    de numpy/BLAS (se observaron en otros scripts) sin ocultar cambios reales.

Corre con pytest o directo:
    python reconstruction_real/tests/test_auditoria_integral.py
"""

import os
import sys
import tempfile

import pandas as pd

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "code"))
sys.path.insert(0, os.path.join(_ROOT, "reconstruction_real", "code"))

import snt_auditoria_integral_v32 as aud  # noqa: E402

_VERSIONADO = os.path.join(
    _ROOT, "reconstruction_real", "data",
    "auditoria_integral_v32_resultados.csv")

CLAVE = ["bloque", "cifra"]


def _regenerar():
    with tempfile.TemporaryDirectory() as tmp:
        salida = os.path.join(tmp, "auditoria.csv")
        aud.run(salida)
        return pd.read_csv(salida, dtype=str, keep_default_na=False)


def _cercanos(a, b, rtol=1e-9):
    try:
        x, y = float(a), float(b)
    except ValueError:
        return a == b
    return abs(x - y) <= rtol * max(1.0, abs(x), abs(y))


def test_la_auditoria_conserva_los_estados_y_valores_versionados():
    nuevo = _regenerar().set_index(CLAVE)
    viejo = pd.read_csv(_VERSIONADO, dtype=str,
                        keep_default_na=False).set_index(CLAVE)

    assert set(nuevo.index) == set(viejo.index), (
        "cambió el conjunto de cifras auditadas: "
        f"{sorted(set(nuevo.index) ^ set(viejo.index))}")

    estados = [(k, viejo.loc[k, "estado"], nuevo.loc[k, "estado"])
               for k in viejo.index if viejo.loc[k, "estado"]
               != nuevo.loc[k, "estado"]]
    assert not estados, f"estados que cambiaron: {estados}"

    numericos = [(k, viejo.loc[k, "recomputado"], nuevo.loc[k, "recomputado"])
                 for k in viejo.index
                 if not _cercanos(viejo.loc[k, "recomputado"],
                                  nuevo.loc[k, "recomputado"])]
    assert not numericos, f"valores recomputados distintos: {numericos}"


def test_el_numero_de_cifras_replicadas_no_baja():
    viejo = pd.read_csv(_VERSIONADO, dtype=str, keep_default_na=False)
    replicadas = viejo.estado.str.startswith("REPLICA").sum()
    assert replicadas >= 30, f"solo {replicadas} cifras replicadas"


if __name__ == "__main__":
    pruebas = [v for k, v in sorted(globals().items())
               if k.startswith("test_") and callable(v)]
    for t in pruebas:
        t()
        print("OK  ", t.__name__)
    print(f"{len(pruebas)} pruebas OK")
