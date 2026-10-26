#!/usr/bin/env python3
"""Regresión: evaluar_prospectiva reproduce el backcast de la ventana 2025-26.

Congela al 2025-08-31 con congelar_cohorte.congelar() y evalúa la ventana
hasta 2026-08-31 con evaluar_prospectiva.evaluar(); compara contra los
números del backcast con tolerancia. Protege el script de evaluación con
el mismo CI (validación del operador, 2026-10-26: el defecto era que el
ATH y el valle de Δ se buscaban en la serie COMPLETA, filtrando datos
posteriores al fin de la ventana).

Corre con pytest o directo:
    python reconstruction_real/tests/test_evaluar_prospectiva.py
"""

import os
import sys
import tempfile

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "reconstruction_real", "code"))

import congelar_cohorte  # noqa: E402
import evaluar_prospectiva as ep  # noqa: E402

FUENTE = os.path.join(_ROOT, "data", "binance_cierres_diarios.csv.gz")

# Congelar 2025-08-31 → evaluar hasta 2026-08-31 (la ventana del backcast)
CORTE = "2025-08-31"
FIN = "2026-08-31"

# Lo que el backcast (script corregido, truncado en fin) mide en esa ventana
ESPERADO = {
    "candidatos": 389,
    "colapsos_crudos": 89,
    "colapsos_maduros": 36,
    "mediana_delta": -0.944,
    "rho_b_delta": -0.191,
}
TOL = {"mediana_delta": 0.005, "rho_b_delta": 0.005}


def test_el_evaluador_reproduce_el_backcast():
    with tempfile.TemporaryDirectory() as tmp:
        cohorte_ruta = os.path.join(tmp, "cohorte.csv")
        congelar_cohorte.congelar(FUENTE, CORTE, cohorte_ruta)
        ep.COHORTE = __import__("pathlib").Path(cohorte_ruta)
        ep.CORTE_COHORTE = CORTE
        res = ep.evaluar(FUENTE, FIN)

    assert res["candidatos"] == ESPERADO["candidatos"], (
        f"candidatos {res['candidatos']} ≠ {ESPERADO['candidatos']}")
    assert res["colapsos_crudos"] == ESPERADO["colapsos_crudos"], (
        f"crudos {res['colapsos_crudos']} ≠ {ESPERADO['colapsos_crudos']}")
    assert res["colapsos_maduros"] == ESPERADO["colapsos_maduros"], (
        f"maduros {res['colapsos_maduros']} ≠ {ESPERADO['colapsos_maduros']}")
    assert abs(res["mediana_delta"] - ESPERADO["mediana_delta"]) \
        <= TOL["mediana_delta"], (
        f"mediana Δ {res['mediana_delta']:.4f} ≠ "
        f"{ESPERADO['mediana_delta']}±{TOL['mediana_delta']}")
    assert abs(res["rho_b_delta"] - ESPERADO["rho_b_delta"]) \
        <= TOL["rho_b_delta"], (
        f"ρ(b,Δ) {res['rho_b_delta']:.4f} ≠ "
        f"{ESPERADO['rho_b_delta']}±{TOL['rho_b_delta']}")


if __name__ == "__main__":
    test_el_evaluador_reproduce_el_backcast()
    print("evaluador == backcast en la ventana 2025-26 ✓")
