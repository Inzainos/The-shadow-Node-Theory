#!/usr/bin/env python3
"""Regresión RC1: el script preregistrado reproduce las cifras citadas.

Re-ejecuta `rc1_superlineal.main()` con las salidas redirigidas a un
directorio temporal (no toca los CSV versionados) y verifica dos cosas:

1. La compuerta P0 en la banda `b >= 1` (agregada): E3 80,3 % · B 96,8 % ·
   ACO 48,9 % — las cifras que cita el README. `claims.yaml` ya las compara
   contra el CSV versionado; este test las liga al SCRIPT que las genera
   (pendiente 1.2 de PENDIENTES_SNT.md).
2. Los CSV regenerados coinciden con los versionados (rtol 1e-9, el mismo
   patrón del test de la auditoría integral).

La restauración (2026-10-26): el commit 1ac2c02 reescribió el script y lo
dejó roto y amputado (421→317 líneas; sin P0-P5 ni escritores). Este test
existe para que eso no vuelva a pasar inadvertido: si alguien toca el
script o `snt_utils_v32.comparar_modelos`, la compuerta se recalcula y
debe dar lo mismo. Determinista: SEMILLA=20261002 (medido: reproducción
exacta, dif 0.00e+00).

Corre con pytest o directo:
    python reconstruction_real/tests/test_rc1_regresion.py
"""

import os
import sys
import tempfile
from pathlib import Path

import pandas as pd

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "reconstruction_real", "code"))

import rc1_superlineal as rc1  # noqa: E402

_VERSIONADO = os.path.join(_ROOT, "reconstruction_real", "data")

# Las tres cifras de la compuerta que el README sostiene (banda b >= 1).
# Tolerancia 5e-4: el CSV guarda fracciones a 4 decimales (0.8026) y el
# README las cita al decimal de porcentaje (80,3).
COMPUERTA = {"E3": 0.8026, "B": 0.9675, "ACO": 0.4888}
BANDA = "b >= 1 (agregada)"


def _cercanos(a, b, rtol=1e-9):
    return abs(float(a) - float(b)) <= rtol * max(1.0, abs(float(a)),
                                                  abs(float(b)))


def test_rc1_reproduce_compuerta_y_csvs_versionados():
    with tempfile.TemporaryDirectory() as tmp:
        rc1.OUT_CASO = Path(tmp) / "rc1_por_caso.csv"
        rc1.OUT_CAL = Path(tmp) / "rc1_calibracion.csv"
        rc1.OUT_RESUMEN = Path(tmp) / "rc1_resumen.csv"
        rc1.main()

        cal = pd.read_csv(rc1.OUT_CAL)

        # 1) Compuerta P0 por dominio, banda b >= 1
        for dominio, esperado in COMPUERTA.items():
            fila = cal[(cal["dominio"] == dominio)
                       & (cal["banda_b"] == BANDA)]
            assert not fila.empty, (
                f"falta la banda {BANDA!r} de {dominio} en rc1_calibracion")
            valor = fila["error_seleccion_P0"].iloc[0]
            assert abs(valor - esperado) <= 5e-4, (
                f"compuerta P0 de {dominio}: {valor:.4f} ≠ "
                f"{esperado:.4f} (README: {100 * esperado:.1f} %)")

        # 2) CSVs regenerados == versionados (forma, columnas, valores)
        for nombre, temporal in (("rc1_por_caso.csv", rc1.OUT_CASO),
                                 ("rc1_calibracion.csv", rc1.OUT_CAL)):
            nuevo = pd.read_csv(temporal)
            viejo = pd.read_csv(os.path.join(_VERSIONADO, nombre))
            assert nuevo.shape == viejo.shape, (
                f"{nombre}: forma {nuevo.shape} ≠ {viejo.shape}")
            assert list(nuevo.columns) == list(viejo.columns), (
                f"{nombre}: cambiaron las columnas")
            for col in nuevo.columns:
                if pd.api.types.is_numeric_dtype(nuevo[col]):
                    dif = (nuevo[col] - viejo[col]).abs().max()
                    assert dif <= 1e-9 * max(1.0, float(viejo[col].abs()
                                                         .max())), (
                        f"{nombre}.{col}: dif máx {dif:.2e} > rtol 1e-9")
                else:
                    iguales = (nuevo[col].astype(str)
                               == viejo[col].astype(str)).all()
                    assert iguales, f"{nombre}.{col}: categóricos difieren"


if __name__ == "__main__":
    test_rc1_reproduce_compuerta_y_csvs_versionados()
    print("RC1: compuerta y CSVs reproducidos ✓")
