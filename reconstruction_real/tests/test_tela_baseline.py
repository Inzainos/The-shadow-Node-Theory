#!/usr/bin/env python3
"""Regresión: línea base, balanceada, permutación y LODO de la tela.

Protege `tela_clasificacion_baseline.py` en tres frentes:

  1. Corrección numérica: el LOO vectorizado coincide con una implementación
     ingenua de referencia (distancia a centroides recalculados sin la fila).
  2. Determinismo: con la misma semilla el nulo de permutación es idéntico.
  3. Coherencia de los CSV versionados con las cifras publicadas y con la
     identidad "la línea base mayoritaria supera a la exactitud cruda por
     dominio" que motivó esta auditoría.

Corre con pytest o directo:
    python reconstruction_real/tests/test_tela_baseline.py
"""

import os
import sys

import numpy as np
import pandas as pd

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "reconstruction_real", "code"))

import tela_clasificacion_baseline as tb  # noqa: E402

_DATA = os.path.join(_ROOT, "reconstruction_real", "data")


def _sintetico(seed=7, n_por_grupo=(12, 8, 3, 1)):
    rng = np.random.default_rng(seed)
    X, y = [], []
    for g, (n, mu) in enumerate(zip(n_por_grupo, (0.0, 2.0, -2.0, 5.0))):
        X.append(rng.normal(mu, 1.0, size=(n, 4)))
        y += [f"g{g}"] * n
    return np.vstack(X), np.array(y)


def _loo_ingenuo(Xz, y):
    """Referencia: recalcula cada centroide excluyendo la fila evaluada."""
    preds, evaluable = [], []
    for i in range(len(y)):
        mejor, mejor_d = None, np.inf
        for g in sorted(set(y)):
            idx = [j for j in range(len(y)) if y[j] == g and j != i]
            if not idx:
                continue
            d = np.linalg.norm(Xz[i] - Xz[idx].mean(axis=0))
            if d < mejor_d:
                mejor, mejor_d = g, d
        preds.append(mejor)
        evaluable.append(int((y == y[i]).sum()) >= 2)
    return np.array(preds), np.array(evaluable)


def test_loo_vectorizado_coincide_con_la_referencia_ingenua():
    X, y = _sintetico()
    Xz = tb.estandarizar(X)
    grupos, inv, pred, ev = tb.loo_centroide(Xz, y)
    ref_pred, ref_ev = _loo_ingenuo(Xz, y)
    assert (ev == ref_ev).all()
    assert (grupos[pred][ev] == ref_pred[ref_ev]).all()


def test_el_singleton_no_es_evaluable_pero_si_candidato():
    X, y = _sintetico()
    Xz = tb.estandarizar(X)
    grupos, inv, pred, ev = tb.loo_centroide(Xz, y)
    assert not ev[y == "g3"].any()
    assert ev[y == "g0"].all()


def test_metricas_base_mayoritaria_y_balanceada():
    inv = np.array([0, 0, 0, 0, 1, 1])
    pred = np.array([0, 0, 0, 0, 0, 0])      # siempre predice la clase 0
    ev = np.ones(6, dtype=bool)
    m = tb.metricas(inv, pred, ev, 2)
    assert abs(m["exactitud"] - 4 / 6) < 1e-12
    assert abs(m["base_mayoritaria"] - 4 / 6) < 1e-12
    assert abs(m["exactitud_balanceada"] - 0.5) < 1e-12   # (1 + 0) / 2
    assert abs(m["azar_balanceada"] - 0.5) < 1e-12


def test_nulo_de_permutacion_es_determinista_por_semilla():
    X, y = _sintetico()
    Xz = tb.estandarizar(X)
    a = tb.nulo_permutacion(Xz, y, np.random.default_rng(1), 25)
    b = tb.nulo_permutacion(Xz, y, np.random.default_rng(1), 25)
    c = tb.nulo_permutacion(Xz, y, np.random.default_rng(2), 25)
    assert np.array_equal(a[0], b[0]) and np.array_equal(a[1], b[1])
    assert not np.array_equal(a[0], c[0])


def test_p_de_permutacion_nunca_es_cero():
    assert tb.p_superior(1.0, np.zeros(100)) == 1 / 101
    assert tb.p_superior(0.0, np.zeros(100)) == 1.0


def test_lodo_no_evalua_tonos_ausentes_del_entrenamiento():
    rng = np.random.default_rng(3)
    X = rng.normal(size=(9, 3))
    dominios = np.array(["d1"] * 3 + ["d2"] * 3 + ["d3"] * 3)
    tonos = np.array(["a"] * 6 + ["b"] * 3)       # 'b' solo existe en d3
    df, _ = tb._lodo(X, dominios, tonos)
    d3 = df[df.dominio_retenido == "d3"].iloc[0]
    assert d3.n_eval == 0 and "ausente" in d3.nota
    assert df[df.dominio_retenido == "d1"].iloc[0].n_eval == 3


def test_csv_versionado_reproduce_las_cifras_publicadas():
    d = pd.read_csv(os.path.join(_DATA, "tela_clasificacion_baseline.csv"))
    t = d[d.conjunto == "todos_los_casos"].set_index(["tarea", "rasgos"])
    publicadas = {("dominio", "todos"): 0.507, ("dominio", "solo_forma"): 0.419,
                  ("tono", "todos"): 0.662, ("tono", "solo_forma"): 0.586}
    for clave, pub in publicadas.items():
        assert round(t.loc[clave, "exactitud"], 3) == pub, clave
        assert abs(t.loc[clave, "exactitud"]
                   - t.loc[clave, "exactitud_original"]) < 1e-12, clave


def test_csv_versionado_conserva_el_hallazgo_de_la_linea_base():
    d = pd.read_csv(os.path.join(_DATA, "tela_clasificacion_baseline.csv"))
    f = d[(d.conjunto == "todos_los_casos") & (d.tarea == "dominio")]
    assert (f.base_mayoritaria > f.exactitud).all()
    assert (f.exactitud_balanceada > 3 * f.azar_balanceada).all()
    tono = d[(d.conjunto == "todos_los_casos") & (d.tarea == "tono")]
    assert (tono.p_perm_dominios_bal > 0.05).all()


def test_csv_lodo_resumen_coherente():
    r = pd.read_csv(os.path.join(_DATA, "tela_clasificacion_lodo_resumen.csv"))
    assert set(r.rasgos) == {"todos", "solo_forma"}
    assert (r.n_eval == 718).all()
    assert ((r.exactitud >= 0) & (r.exactitud <= 1)).all()
    assert (r.p_perm_dominios_bal > 0.05).all()


if __name__ == "__main__":
    pruebas = [v for k, v in sorted(globals().items())
               if k.startswith("test_") and callable(v)]
    for t in pruebas:
        t()
        print("OK  ", t.__name__)
    print(f"{len(pruebas)} pruebas OK")
