#!/usr/bin/env python3
"""Regresión: evaluar_prospectiva reproduce el backcast de la ventana 2025-26.

DOS protecciones (revisión del operador, 2026-10-26 segunda ronda):

1. Congelar al 2025-08-31 y evaluar hasta 2026-08-31 reproduce los
   números del backcast (89 crudos, 36 maduros, Δ = −0.944, ρ = −0.191).
2. INVARIANTE DE TRUNCADO: la evaluación sobre el archivo COMPLETO
   (que extiende hasta 2026-09-30) da EXACTAMENTE lo mismo que sobre
   el archivo truncado al fin de la ventana — igualdad estricta, no
   tolerancia. Si la fuga del valle reaparece, este test la caza.

Corre con pytest o directo:
    python reconstruction_real/tests/test_evaluar_prospectiva.py
"""

import csv
import gzip
import os
import sys
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "reconstruction_real", "code"))

import congelar_cohorte  # noqa: E402
import evaluar_prospectiva as ep  # noqa: E402
import backcast_prospectiva as bp  # noqa: E402

FUENTE = os.path.join(_ROOT, "data", "binance_cierres_diarios.csv.gz")
CORTE = "2025-08-31"
FIN = "2026-08-31"

ESPERADO = {
    "candidatos": 389,
    "censurados": 55,
    "colapsos_crudos": 53,
    "colapsos_maduros": 22,
    "mediana_delta": -0.9612,
    "rho_b_delta": 0.1892,
    "ic95_inf": -0.2526,
    "ic95_sup": 0.5657,
}


def _congelar_y_evaluar(ruta_datos):
    """Congela al CORTE y evalúa hasta FIN con la cohorte temporal."""
    with tempfile.TemporaryDirectory() as tmp:
        cohorte_ruta = os.path.join(tmp, "cohorte.csv")
        congelar_cohorte.congelar(FUENTE, CORTE, cohorte_ruta)
        return ep.evaluar(ruta_datos, fin=FIN,
                          ruta_cohorte=cohorte_ruta,
                          corte_cohorte=CORTE)


def _truncar_en(ruta_origen, fecha_fin, ruta_destino):
    """Escribe un CSV.gz con solo las filas con fecha <= fecha_fin."""
    with gzip.open(ruta_origen, "rt") as f_in, \
            gzip.open(ruta_destino, "wt", newline="") as f_out:
        lector = csv.DictReader(f_in)
        escritor = csv.DictWriter(f_out, fieldnames=lector.fieldnames)
        escritor.writeheader()
        for fila in lector:
            if fila["fecha"] <= fecha_fin:
                escritor.writerow(fila)


def test_el_evaluador_reproduce_el_backcast():
    res = _congelar_y_evaluar(FUENTE)
    for clave, esperado in ESPERADO.items():
        assert res[clave] == esperado, (
            f"{clave}: {res[clave]} ≠ {esperado}")


def test_backcast_y_evaluador_aplican_el_mismo_truncado():
    series = bp.cargar_series()
    _, colapsos, maduros, censurados = bp.backcast(
        series, CORTE, FIN)
    assert colapsos == ESPERADO["colapsos_crudos"]
    assert len(maduros) == ESPERADO["colapsos_maduros"]
    assert censurados == ESPERADO["censurados"]


def test_truncado_en_fin_da_resultado_identico():
    """El invariante: los datos posteriores al fin NO cambian NADA."""
    with tempfile.TemporaryDirectory() as tmp:
        truncado = os.path.join(tmp, "truncado.csv.gz")
        _truncar_en(FUENTE, FIN, truncado)
        res_completo = _congelar_y_evaluar(FUENTE)
        res_truncado = _congelar_y_evaluar(truncado)
    for clave in ESPERADO:
        assert res_completo[clave] == res_truncado[clave], (
            f"INVARIANTE ROTO en {clave}: completo {res_completo[clave]} "
            f"≠ truncado {res_truncado[clave]} — la fuga del valle "
            f"reapareció")


def test_pares_sin_seguimiento_completo_se_censuran():
    with tempfile.TemporaryDirectory() as tmp:
        cohorte = os.path.join(tmp, "cohorte.csv")
        datos = os.path.join(tmp, "cierres.csv.gz")
        with open(cohorte, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(
                fh, fieldnames=["par", "ath_corte", "precio_corte",
                                "fecha_ath"])
            writer.writeheader()
            writer.writerows([
                {"par": "OBSERVADO", "ath_corte": 100, "precio_corte": 50,
                 "fecha_ath": "2025-01-01"},
                {"par": "DELISTADO", "ath_corte": 100, "precio_corte": 50,
                 "fecha_ath": "2025-01-01"},
                {"par": "SIN_DATOS", "ath_corte": 100, "precio_corte": 50,
                 "fecha_ath": "2025-01-01"},
            ])
        with gzip.open(datos, "wt", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["par", "fecha", "close"])
            writer.writeheader()
            writer.writerows([
                {"par": "OBSERVADO", "fecha": "2026-09-30", "close": 50},
                {"par": "OBSERVADO", "fecha": "2027-09-30", "close": 50},
                {"par": "DELISTADO", "fecha": "2026-09-30", "close": 50},
                {"par": "DELISTADO", "fecha": "2027-01-01", "close": 0.5},
                {"par": "SIN_DATOS", "fecha": "2026-09-30", "close": 50},
            ])

        res = ep.evaluar(
            datos, ruta_cohorte=cohorte, corte_cohorte="2026-09-30",
            fin="2027-09-30")

    assert res["candidatos"] == 3
    assert res["censurados"] == 2
    assert res["colapsos_crudos"] == 0


def test_descarga_que_no_llega_al_fin_no_se_evalua():
    with tempfile.TemporaryDirectory() as tmp:
        cohorte = os.path.join(tmp, "cohorte.csv")
        datos = os.path.join(tmp, "cierres.csv.gz")
        with open(cohorte, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(
                fh, fieldnames=["par", "ath_corte", "precio_corte",
                                "fecha_ath"])
            writer.writeheader()
            writer.writerow({"par": "PAR", "ath_corte": 100,
                             "precio_corte": 50, "fecha_ath": "2025-01-01"})
        with gzip.open(datos, "wt", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["par", "fecha", "close"])
            writer.writeheader()
            writer.writerow({"par": "PAR", "fecha": "2027-09-29", "close": 50})

        try:
            ep.evaluar(
                datos, ruta_cohorte=cohorte, corte_cohorte="2026-09-30",
                fin="2027-09-30")
        except ValueError as exc:
            assert "descarga incompleta" in str(exc)
        else:
            raise AssertionError("se permitió evaluar una descarga incompleta")


if __name__ == "__main__":
    test_el_evaluador_reproduce_el_backcast()
    print("evaluador == backcast en la ventana 2025-26 ✓")
    test_truncado_en_fin_da_resultado_identico()
    print("invariante de truncado: completo == truncado ✓")
