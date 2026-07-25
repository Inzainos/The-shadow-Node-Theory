#!/usr/bin/env python3
"""Regresión: fija la corrección AR(1) del dominio B.

Blinda el punto exacto donde dos implementaciones independientes de la misma
corrección divergieron durante la revisión cruzada de la auditoría v32. Sin
este test, una tercera implementación puede volver a divergir sin que nadie se
entere hasta la siguiente revisión.

Las cifras que se fijan son las **convención-independientes**, no una guarda
defensiva de implementación (por eso NO se fija 145 ni 114 — dependían de cómo
se floorean los grados de libertad para casos no estimables):

  * Estimabilidad (sale directo de ``n_eff``, sin aproximaciones):
      - ``n_eff >= 3`` (estimable)      = 156 / 446
      - ``n_eff <  3`` (NO estimable)   = 290 / 446
  * Significativos ENTRE los estimables, como rango:
      - cota inferior (SE inflado + gl) =  33 / 156  (21.2%)  ← invariante a la
                                                              convención de gl
      - cota superior (solo gl, df>0)   = 112 / 156  (71.8%)

El valor puntual verdadero vive dentro de ``[33, 112]`` sobre los estimables y
solo se fija con Newey-West/GLS sobre residuos crudos (ausentes del repo).

Corre con pytest o directo:
    python reconstruction_real/tests/test_correccion_ar1.py
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

ESTIMABLES = 156        # n_eff >= 3
NO_ESTIMABLES = 290     # n_eff < 3
COTA_INFERIOR = 33      # SE inflado + gl, entre estimables (invariante a gl)
COTA_SUPERIOR = 112     # solo gl (df>0), entre estimables


def _corregir_B():
    with open(_B_CSV, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return corregir_corpus(rows)


def test_estimabilidad_dominio_B():
    """290/446 no estimables — el hallazgo convención-independiente."""
    _, resumen = _corregir_B()
    assert resumen["n_estimables"] == ESTIMABLES, (
        "estimables (n_eff>=3) cambió: %d != %d"
        % (resumen["n_estimables"], ESTIMABLES))
    assert resumen["n_no_estimables"] == NO_ESTIMABLES, (
        "no estimables (n_eff<3) cambió: %d != %d"
        % (resumen["n_no_estimables"], NO_ESTIMABLES))


def test_cota_inferior_invariante():
    """La cota inferior 33 no depende de la convención de gl."""
    _, resumen = _corregir_B()
    assert resumen["n_sig_ar1"] == COTA_INFERIOR, (
        "cota inferior AR(1) (SE inflado) cambió: %d != %d"
        % (resumen["n_sig_ar1"], COTA_INFERIOR))


def test_cota_superior_entre_estimables():
    """La cota superior se cuenta SOLO sobre los estimables (112, no 145)."""
    out, resumen = _corregir_B()
    # el resumen ya la restringe a estimables
    assert resumen["n_sig_ar1_solo_gl"] == COTA_SUPERIOR, (
        "cota superior (solo gl, entre estimables) cambió: %d != %d"
        % (resumen["n_sig_ar1_solo_gl"], COTA_SUPERIOR))
    # y ningún caso NO estimable debe contarse como significativo
    contaminados = sum(
        1 for r in out
        if r.get("estimable") is False and (r.get("sig_ar1") or
                                            r.get("sig_ar1_solo_gl")))
    assert contaminados == 0, (
        "%d casos no estimables contados como significativos" % contaminados)


def test_rango_ordenado_y_warning():
    _, resumen = _corregir_B()
    assert resumen["n_sig_ar1"] < resumen["n_sig_ar1_solo_gl"]
    with open(_B_CSV, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        corregir_corpus(rows)
    assert any("estimables" in str(w.message) for w in caught), (
        "corregir_corpus debe advertir sobre estimabilidad y rango")


if __name__ == "__main__":
    test_estimabilidad_dominio_B()
    test_cota_inferior_invariante()
    test_cota_superior_entre_estimables()
    test_rango_ordenado_y_warning()
    print("OK — dominio B: %d estimables / %d no estimables; "
          "significativos entre estimables [%d, %d]"
          % (ESTIMABLES, NO_ESTIMABLES, COTA_INFERIOR, COTA_SUPERIOR))
