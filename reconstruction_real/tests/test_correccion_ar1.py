#!/usr/bin/env python3
"""Regresión: fija las cotas de la corrección AR(1) del dominio B.

Blinda el punto exacto donde dos implementaciones independientes de la misma
corrección divergieron (145 vs 33) durante la revisión cruzada de la auditoría
v32. Sin este test, una tercera implementación puede volver a divergir sin que
nadie se entere hasta la siguiente revisión.

Cotas esperadas sobre ``by_domain/dominio_B_real.csv`` (446 casos):

  * ``sig_ar1``          = 33   — cota inferior: SE inflado + gl recortado
                                  (corrección coherente).
  * ``sig_ar1_solo_gl``  = 145  — cota superior: solo gl recortado
                                  (media corrección; se conserva como bracket).

El valor puntual verdadero vive dentro de ``[33, 145]`` y solo se fija con
Newey-West/GLS sobre residuos crudos (ausentes del repo).

Corre con pytest o directo:  ``python reconstruction_real/tests/test_correccion_ar1.py``
"""

import csv
import os
import sys
import warnings

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "code"))

from snt_utils_v32 import corregir_corpus  # noqa: E402

_B_CSV = os.path.join(
    _ROOT, "reconstruction_real", "data", "by_domain", "dominio_B_real.csv")

COTA_INFERIOR = 33   # SE inflado + gl recortado (coherente)
COTA_SUPERIOR = 145  # solo gl recortado (cota superior)


def _corregir_B():
    with open(_B_CSV, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        _, resumen = corregir_corpus(rows)
    return resumen


def test_correccion_ar1_dominio_B_cotas():
    resumen = _corregir_B()
    assert resumen["n_sig_ar1"] == COTA_INFERIOR, (
        "cota inferior AR(1) (SE inflado + gl) cambió: %d != %d"
        % (resumen["n_sig_ar1"], COTA_INFERIOR))
    assert resumen["n_sig_ar1_solo_gl"] == COTA_SUPERIOR, (
        "cota superior AR(1) (solo gl) cambió: %d != %d"
        % (resumen["n_sig_ar1_solo_gl"], COTA_SUPERIOR))


def test_correccion_ar1_es_rango_ordenado():
    resumen = _corregir_B()
    assert resumen["n_sig_ar1"] < resumen["n_sig_ar1_solo_gl"], (
        "la cota inferior debe ser estrictamente menor que la superior")


def test_correccion_ar1_emite_warning():
    with open(_B_CSV, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        corregir_corpus(rows)
    assert any("RANGO" in str(w.message) for w in caught), (
        "corregir_corpus debe advertir que el resultado es un rango, "
        "no un valor puntual")


if __name__ == "__main__":
    test_correccion_ar1_dominio_B_cotas()
    test_correccion_ar1_es_rango_ordenado()
    test_correccion_ar1_emite_warning()
    print("OK — cotas AR(1) dominio B: [%d, %d]"
          % (COTA_INFERIOR, COTA_SUPERIOR))
