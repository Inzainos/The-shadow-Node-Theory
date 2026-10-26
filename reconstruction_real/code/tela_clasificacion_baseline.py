#!/usr/bin/env python3
"""
TELA — LÍNEA BASE, EXACTITUD BALANCEADA, PERMUTACIÓN Y LEAVE-ONE-DOMAIN-OUT
===========================================================================

Complemento de `tela_cimatica.py`. Esa prueba reporta la exactitud
leave-one-out (LOO) por centroide más cercano (50.7 % por dominio, 66.2 % por
tono φ en la tela integrada v2) pero NO la compara contra:

  1. la línea base mayoritaria (clasificador que siempre predice la clase más
     frecuente), que en un corpus donde B aporta 446 de 740 trayectorias es
     alta;
  2. la exactitud balanceada (recall medio por clase), que no premia ni
     castiga el desbalance;
  3. un nulo de permutación de etiquetas (¿la forma de la trayectoria está
     asociada a la etiqueta más de lo que daría el azar?);
  4. un esquema leave-one-DOMAIN-out, que es el que corresponde a la pregunta
     "¿la forma identifica el tono φ en un dominio que el clasificador no vio?"

Este script NO modifica `tela_cimatica.py`: importa sus funciones, reproduce
primero su exactitud con una implementación vectorizada (control de
consistencia) y solo entonces agrega las medidas anteriores.

Notas de lectura (declaradas aquí para que viajen con el código):
  - φ es CONSTANTE dentro de cada dominio en la tela v2 (se asigna por dominio).
    Por eso clasificar el tono equivale a clasificar el dominio con etiquetas
    agrupadas. El nulo "por dominios" permuta la asignación φ entre dominios
    (12 unidades), que es el nulo apropiado para esa pregunta; el nulo "por
    filas" permuta etiquetas caso a caso y sobreestima la significancia cuando
    las etiquetas son constantes por dominio.
  - La prueba "sin E3" retira el dominio cuya receta de selección fija el
    nacimiento de la trayectoria (ver TELA_V2_INTEGRADA_2026-10-21.md,
    Limitaciones).
  - La estandarización de rasgos usa todos los casos del conjunto evaluado
    (igual que `tela_cimatica.py`) salvo en leave-one-domain-out, donde se
    estima solo con los dominios de entrenamiento.

Uso:
    python reconstruction_real/code/tela_clasificacion_baseline.py [--n-perm N]

Salidas:
  data/tela_clasificacion_baseline.csv
  data/tela_clasificacion_lodo.csv
  logs/tela_clasificacion_baseline_log.txt

Semilla fija (SEED): el resultado es determinista.
"""

import argparse
import logging
import os
import sys

import numpy as np
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

import tela_cimatica as tc  # noqa: E402

DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
LOG_DIR = os.path.join(SCRIPT_DIR, "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

SEED = 20261025
N_PERM_DEFAULT = 5000

# Cifras publicadas en TELA_V2_INTEGRADA_2026-10-21.md (control de consistencia)
PUBLICADAS = {
    ("dominio", "todos"): 0.507,
    ("dominio", "solo_forma"): 0.419,
    ("tono", "todos"): 0.662,
    ("tono", "solo_forma"): 0.586,
}

log = logging.getLogger("tela_baseline")
log.setLevel(logging.INFO)
_fh = logging.FileHandler(
    os.path.join(LOG_DIR, "tela_clasificacion_baseline_log.txt"), mode="w")
_fh.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)-7s | %(message)s"))
log.addHandler(_fh)


# --------------------------------------------------------------------------
# Construcción de casos (idéntica a tela_cimatica.main)
# --------------------------------------------------------------------------
def construir_casos():
    df = tc.cargar_tela()
    trajs = tc.trayectorias(df)
    casos = {}
    for (dom, cid), r in trajs.items():
        ras = tc.rasgos(r["lm"])
        phi = df[(df["dominio"] == dom) & (df["id"] == cid)][
            "phi_friccion"].iloc[0]
        casos[(dom, cid)] = {
            "lm": r["lm"], "fuente": r["fuente"], "phi": phi,
            "rasgos": ras, "rasgos_forma": ras[1:],
        }
    return casos


def tabla(casos, usar_tau0):
    """Devuelve (claves ordenadas, X sin estandarizar, dominios, tonos)."""
    claves = sorted(casos)
    campo = "rasgos" if usar_tau0 else "rasgos_forma"
    X = np.array([casos[k][campo] for k in claves], dtype=float)
    dominios = np.array([k[0] for k in claves])
    tonos = np.array([casos[k]["phi"] for k in claves])
    return claves, X, dominios, tonos


def estandarizar(X, ref=None):
    ref = X if ref is None else ref
    mu, sd = ref.mean(axis=0), ref.std(axis=0)
    sd = np.where(sd == 0, 1.0, sd)
    return (X - mu) / sd


# --------------------------------------------------------------------------
# LOO por centroide, vectorizado (equivalente a tela_cimatica.clasificacion_loo)
# --------------------------------------------------------------------------
def loo_centroide(Xz, etiquetas):
    """Predicción LOO por centroide más cercano.

    Devuelve (grupos, inv, pred, evaluable): `inv` indexa la etiqueta real en
    `grupos`; `pred` indexa la predicha; `evaluable` marca filas cuyo grupo
    tiene >= 2 miembros (mismo criterio que el original).
    """
    grupos, inv = np.unique(np.asarray(etiquetas), return_inverse=True)
    n, G = len(inv), len(grupos)
    onehot = np.zeros((n, G))
    onehot[np.arange(n), inv] = 1.0
    n_g = onehot.sum(axis=0)
    S = onehot.T @ Xz
    C = S / n_g[:, None]
    d2 = ((Xz[:, None, :] - C[None, :, :]) ** 2).sum(axis=2)
    n_own = n_g[inv]
    C_own = (S[inv] - Xz) / np.maximum(n_own - 1.0, 1.0)[:, None]
    d2[np.arange(n), inv] = ((Xz - C_own) ** 2).sum(axis=1)
    pred = d2.argmin(axis=1)
    return grupos, inv, pred, n_own >= 2


def metricas(inv, pred, evaluable, n_grupos):
    y, p = inv[evaluable], pred[evaluable]
    acc = float((y == p).mean())
    cuentas = np.bincount(y, minlength=n_grupos)
    base = float(cuentas.max() / cuentas.sum())
    recalls = [float((p[y == g] == g).mean())
               for g in range(n_grupos) if (y == g).any()]
    bal = float(np.mean(recalls))
    return {"n_eval": int(evaluable.sum()), "n_grupos": len(recalls),
            "exactitud": acc, "base_mayoritaria": base,
            "exactitud_balanceada": bal,
            "azar_balanceada": 1.0 / len(recalls)}


def nulo_permutacion(Xz, etiquetas, rng, n_perm, por_dominio=None):
    """Distribución nula de (exactitud balanceada, exactitud).

    por_dominio=None  -> permuta etiquetas fila a fila.
    por_dominio=array -> permuta la asignación etiqueta<-dominio entre
                         dominios (la etiqueta es constante por dominio).
    """
    etiquetas = np.asarray(etiquetas)
    bal = np.empty(n_perm)
    acc = np.empty(n_perm)
    if por_dominio is not None:
        doms, idx = np.unique(por_dominio, return_inverse=True)
        etiqueta_dom = np.array([etiquetas[por_dominio == d][0] for d in doms])
    for i in range(n_perm):
        if por_dominio is None:
            et = rng.permutation(etiquetas)
        else:
            et = rng.permutation(etiqueta_dom)[idx]
        g, inv, pred, ev = loo_centroide(Xz, et)
        m = metricas(inv, pred, ev, len(g))
        bal[i], acc[i] = m["exactitud_balanceada"], m["exactitud"]
    return bal, acc


def p_superior(obs, nulo):
    return float((1 + np.sum(nulo >= obs - 1e-12)) / (1 + len(nulo)))


# --------------------------------------------------------------------------
# Evaluación de una variante
# --------------------------------------------------------------------------
def evaluar(casos, tarea, usar_tau0, conjunto, rng, n_perm):
    claves, X, dominios, tonos = tabla(casos, usar_tau0)
    Xz = estandarizar(X)
    etiquetas = dominios if tarea == "dominio" else tonos
    grupos, inv, pred, ev = loo_centroide(Xz, etiquetas)
    m = metricas(inv, pred, ev, len(grupos))

    fila = {"tarea": tarea, "rasgos": "todos" if usar_tau0 else "solo_forma",
            "conjunto": conjunto, "n_casos": len(claves), **m}

    # Control de consistencia contra la implementación original
    if conjunto == "todos_los_casos":
        _, acc_orig, _, _ = tc.clasificacion_loo(
            casos, usar_tau0=usar_tau0, por_phi=(tarea == "tono"))
        fila["exactitud_original"] = float(acc_orig)
        if abs(acc_orig - m["exactitud"]) > 1e-12:
            log.error("INCONSISTENCIA vectorizado=%.6f original=%.6f (%s/%s)",
                      m["exactitud"], acc_orig, tarea, fila["rasgos"])
        pub = PUBLICADAS.get((tarea, fila["rasgos"]))
        fila["publicada"] = pub
        if pub is not None and abs(round(m["exactitud"], 3) - pub) > 0.0006:
            log.warning("No coincide con la cifra publicada %.3f: obtenida "
                        "%.3f", pub, m["exactitud"])
    else:
        fila["exactitud_original"] = np.nan
        fila["publicada"] = np.nan

    bal_n, acc_n = nulo_permutacion(Xz, etiquetas, rng, n_perm)
    fila.update({
        "nulo_filas_bal_media": float(bal_n.mean()),
        "nulo_filas_bal_p95": float(np.percentile(bal_n, 95)),
        "nulo_filas_acc_media": float(acc_n.mean()),
        "p_perm_filas_bal": p_superior(m["exactitud_balanceada"], bal_n),
        "p_perm_filas_acc": p_superior(m["exactitud"], acc_n),
    })
    if tarea == "tono":
        bal_d, _ = nulo_permutacion(Xz, etiquetas, rng, n_perm,
                                    por_dominio=dominios)
        fila.update({
            "nulo_dominios_bal_media": float(bal_d.mean()),
            "nulo_dominios_bal_p95": float(np.percentile(bal_d, 95)),
            "p_perm_dominios_bal": p_superior(
                m["exactitud_balanceada"], bal_d),
        })
    fila["semilla"] = SEED
    fila["n_perm"] = n_perm
    return fila


# --------------------------------------------------------------------------
# Leave-one-domain-out (tono φ en un dominio no visto)
# --------------------------------------------------------------------------
def _lodo(X, dominios, tonos):
    """Leave-one-domain-out sobre arreglos. Devuelve (df por dominio, resumen).

    Para cada dominio retenido se estandariza y se calculan centroides por
    tono SOLO con los demás dominios. Solo se evalúan filas cuyo tono existe
    en el entrenamiento. Se reportan tres referencias: la clase mayoritaria
    del entrenamiento, el azar uniforme entre los tonos del entrenamiento
    (1/k) y, en el resumen, la exactitud balanceada.
    """
    filas = []
    y_all, p_all, b_all, k_all = [], [], [], []
    for d in sorted(set(dominios)):
        test = dominios == d
        train = ~test
        Xz_tr = estandarizar(X[train])
        Xz_te = estandarizar(X[test], ref=X[train])
        grupos_tr = np.unique(tonos[train])
        cent = np.stack([Xz_tr[tonos[train] == g].mean(axis=0)
                         for g in grupos_tr])
        base_tono = pd.Series(tonos[train]).value_counts().idxmax()
        y_te = tonos[test]
        eval_ = np.isin(y_te, grupos_tr)
        if not eval_.any():
            filas.append({
                "dominio_retenido": d, "n_casos": int(test.sum()),
                "tono_real": y_te[0], "n_eval": 0, "aciertos": 0,
                "exactitud": np.nan, "exactitud_base_mayoritaria": np.nan,
                "azar_uniforme": np.nan,
                "nota": "tono ausente en entrenamiento: no evaluable",
            })
            continue
        d2 = ((Xz_te[:, None, :] - cent[None, :, :]) ** 2).sum(axis=2)
        pred = grupos_tr[d2.argmin(axis=1)]
        n_ev = int(eval_.sum())
        ok = int((pred[eval_] == y_te[eval_]).sum())
        ok_b = int((y_te[eval_] == base_tono).sum())
        filas.append({
            "dominio_retenido": d, "n_casos": int(test.sum()),
            "tono_real": y_te[0], "n_eval": n_ev, "aciertos": ok,
            "exactitud": ok / n_ev, "exactitud_base_mayoritaria": ok_b / n_ev,
            "azar_uniforme": 1.0 / len(grupos_tr), "nota": "",
        })
        y_all.extend(y_te[eval_].tolist())
        p_all.extend(pred[eval_].tolist())
        b_all.extend([base_tono] * n_ev)
        k_all.extend([1.0 / len(grupos_tr)] * n_ev)
    y, p, b = map(np.array, (y_all, p_all, b_all))
    tonos_eval = np.unique(y)
    resumen = {
        "n_eval": int(len(y)),
        "exactitud": float((y == p).mean()),
        "base_mayoritaria_entrenamiento": float((y == b).mean()),
        "azar_uniforme_esperado": float(np.mean(k_all)),
        "exactitud_balanceada": float(np.mean(
            [(p[y == g] == g).mean() for g in tonos_eval])),
        "balanceada_base_mayoritaria": float(np.mean(
            [(b[y == g] == g).mean() for g in tonos_eval])),
        "azar_balanceada": 1.0 / len(tonos_eval),
    }
    return pd.DataFrame(filas), resumen


def lodo_tono(casos, usar_tau0, rng, n_perm):
    claves, X, dominios, tonos = tabla(casos, usar_tau0)
    df, resumen = _lodo(X, dominios, tonos)
    df["rasgos"] = "todos" if usar_tau0 else "solo_forma"
    resumen["rasgos"] = df["rasgos"].iloc[0]

    # Nulo por dominios: permuta la asignación tono<-dominio (12 unidades)
    doms, idx = np.unique(dominios, return_inverse=True)
    tono_dom = np.array([tonos[dominios == d][0] for d in doms])
    nulo_bal, nulo_acc = np.empty(n_perm), np.empty(n_perm)
    for i in range(n_perm):
        _, r = _lodo(X, dominios, rng.permutation(tono_dom)[idx])
        nulo_bal[i], nulo_acc[i] = r["exactitud_balanceada"], r["exactitud"]
    resumen.update({
        "nulo_dominios_bal_media": float(nulo_bal.mean()),
        "nulo_dominios_bal_p95": float(np.percentile(nulo_bal, 95)),
        "p_perm_dominios_bal": p_superior(resumen["exactitud_balanceada"],
                                          nulo_bal),
        "p_perm_dominios_acc": p_superior(resumen["exactitud"], nulo_acc),
        "semilla": SEED, "n_perm": n_perm,
    })
    return df, resumen


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--n-perm", type=int, default=N_PERM_DEFAULT,
                    help="permutaciones por prueba (default %(default)s)")
    args = ap.parse_args()

    log.info("=" * 78)
    log.info("TELA — LÍNEA BASE / BALANCEADA / PERMUTACIÓN / LODO "
             "(semilla %d, %d permutaciones)", SEED, args.n_perm)
    log.info("=" * 78)

    casos = construir_casos()
    sin_e3 = {k: v for k, v in casos.items() if k[0] != "E3"}
    rng = np.random.default_rng(SEED)

    filas = []
    for conjunto, cs in (("todos_los_casos", casos), ("sin_E3", sin_e3)):
        for tarea in ("dominio", "tono"):
            for usar_tau0 in (True, False):
                f = evaluar(cs, tarea, usar_tau0, conjunto, rng, args.n_perm)
                filas.append(f)
                log.info(
                    "%-15s %-7s %-10s n=%d | exactitud %.1f%% | base "
                    "mayoritaria %.1f%% | balanceada %.1f%% (azar %.1f%%) | "
                    "nulo filas bal %.1f%% p=%.4f%s",
                    conjunto, tarea, f["rasgos"], f["n_eval"],
                    100 * f["exactitud"], 100 * f["base_mayoritaria"],
                    100 * f["exactitud_balanceada"],
                    100 * f["azar_balanceada"],
                    100 * f["nulo_filas_bal_media"],
                    f["p_perm_filas_bal"],
                    (" | nulo dominios p=%.4f" % f["p_perm_dominios_bal"])
                    if "p_perm_dominios_bal" in f else "")

    df = pd.DataFrame(filas)
    ruta = os.path.join(DATA_DIR, "tela_clasificacion_baseline.csv")
    df.to_csv(ruta, index=False, float_format="%.6f")
    log.info("Resultados → %s", ruta)

    partes, resumenes = [], []
    for usar_tau0 in (True, False):
        d, r = lodo_tono(casos, usar_tau0, rng, args.n_perm)
        partes.append(d)
        resumenes.append(r)
        log.info("LODO tono (%s): n=%d | exactitud %.1f%% | base "
                 "mayoritaria %.1f%% | azar uniforme %.1f%% | balanceada "
                 "%.1f%% (azar %.1f%%) | nulo dominios bal %.1f%% p=%.4f",
                 r["rasgos"], r["n_eval"], 100 * r["exactitud"],
                 100 * r["base_mayoritaria_entrenamiento"],
                 100 * r["azar_uniforme_esperado"],
                 100 * r["exactitud_balanceada"], 100 * r["azar_balanceada"],
                 100 * r["nulo_dominios_bal_media"], r["p_perm_dominios_bal"])
    df_l = pd.concat(partes, ignore_index=True)
    ruta_l = os.path.join(DATA_DIR, "tela_clasificacion_lodo.csv")
    df_l.to_csv(ruta_l, index=False, float_format="%.6f")
    pd.DataFrame(resumenes).to_csv(
        os.path.join(DATA_DIR, "tela_clasificacion_lodo_resumen.csv"),
        index=False, float_format="%.6f")
    log.info("LODO por dominio → %s", ruta_l)
    log.info("EJECUCION COMPLETADA")


if __name__ == "__main__":
    main()
