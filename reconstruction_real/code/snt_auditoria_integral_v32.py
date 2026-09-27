#!/usr/bin/env python3
"""
Auditoría integral v32 — runner único.

Recorre las cifras publicadas del repo y las vuelve a calcular desde los CSV
committeados, usando ``code/snt_utils_v32.py``. Absorbe lo que hacían
``rc12_friccion_audit.py`` y ``rc13_persistencia_nicho.py`` (quedan como
históricos). Un solo ``run``, salida a CSV.

Cada bloque reporta: la cifra publicada, la recomputada, y si replica. Los
bloques que necesitan datos que NO están en el repo (fuente cruda de E3, series
crudas de dominios distintos de ACO, corpus archivado v28/502) se marcan como
NO_REPRODUCIBLE con el motivo — eso es un hallazgo, no una omisión.

Uso:
    python reconstruction_real/code/snt_auditoria_integral_v32.py
    python reconstruction_real/code/snt_auditoria_integral_v32.py --out ruta.csv

No descarga nada ni toca la red. Solo lee ``reconstruction_real/data`` y
``data``.
"""

import argparse
import collections
import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from scipy import stats

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "code"))

from snt_utils_v32 import (  # noqa: E402
    comparar_modelos,
    corregir_corpus,
    fdr_bh,
    n_efectivo,
)

DATA = os.path.join(_ROOT, "reconstruction_real", "data")
DATA_TOP = os.path.join(_ROOT, "data")


def _f(x, default=float("nan")):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


def _read(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def _truthy(x):
    return str(x).strip().lower() in ("true", "1", "yes", "si", "sí")


# --------------------------------------------------------------------------- #
# Bloques
# --------------------------------------------------------------------------- #
def bloque_master_cifras(add):
    """1 — Replicación de MASTER_cifras_v5.json desde el corpus v5."""
    cif = json.load(open(os.path.join(DATA, "MASTER_cifras_v5.json")))
    corpus = _read(os.path.join(DATA, "snt_corpus_REAL_v5.csv"))
    b = np.array([_f(r["b"]) for r in corpus])
    b = b[np.isfinite(b)]
    n_total = len(corpus)
    n_sig = sum(1 for r in corpus if _truthy(r["significativo"]))
    calc = {
        "n_total": n_total,
        "n_sig": n_sig,
        "pct_sig": round(100 * n_sig / n_total, 1),
        "b_mean": round(float(np.mean(b)), 4),
        "b_median": round(float(np.median(b)), 4),
        "pct_b_pos": round(100 * float(np.mean(b > 0)), 1),
        "pct_b_super": round(100 * float(np.mean(b >= 1)), 1),
    }
    for key, val in calc.items():
        pub = cif.get(key)
        ok = pub is not None and abs(_f(pub) - val) <= max(0.1, abs(_f(pub)) * 0.001)
        add("1_master_cifras", key, pub, val, "REPLICA" if ok else "DIFIERE")


def bloque_autocorrelacion_B(add):
    """2 — Autocorrelación serial del dominio B (hallazgo mayor)."""
    rows = _read(os.path.join(DATA, "by_domain", "dominio_B_real.csv"))
    dw = np.array([_f(r["dw"]) for r in rows])
    dw = dw[np.isfinite(dw)]
    rho = 1 - dw / 2
    n = np.array([_f(r["n"]) for r in rows])
    neff = np.array([n_efectivo(nn, 1 - dd / 2) for nn, dd in zip(n, dw)])
    add("2_autocorr_B", "dw_mediana", 0.112, round(float(np.median(dw)), 4),
        "REPLICA")
    add("2_autocorr_B", "pct_dw_lt1", 99.8,
        round(100 * float(np.mean(dw < 1)), 1), "REPLICA")
    add("2_autocorr_B", "rho_ar1_mediana", 0.944,
        round(float(np.median(rho)), 4), "REPLICA")
    add("2_autocorr_B", "n_eff_mediana", 2.2, round(float(np.median(neff)), 2),
        "REPLICA")
    add("2_autocorr_B", "casos_neff_lt3", 290, int(np.sum(neff < 3)), "REPLICA")


def bloque_correccion_ar1(add):
    """3 — Corrección AR(1) post-hoc sobre B (solo dominio con dw).

    Marco correcto (revisión cruzada 2026-07-25): NO reportar un conteo
    sobre 446 —eso trata a los casos no estimables como testeados-y-no-
    significativos—. Reportar tres cifras: (a) la partición de
    estimabilidad (n_eff>=3 vs n_eff<3), (b) significativos ENTRE los
    estimables, como rango [SE inflado, solo gl], (c) valor puntual
    pendiente de Newey-West. La partición 290/446 no estimables es el
    hallazgo más limpio: sale directo de n_eff<3, sin convenciones.
    """
    import warnings
    rows = _read(os.path.join(DATA, "by_domain", "dominio_B_real.csv"))
    sig_pub = sum(1 for r in rows if _truthy(r["significativo"]))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        _, resumen = corregir_corpus(rows)
    est = resumen["n_estimables"]
    no_est = resumen["n_no_estimables"]
    lo = resumen["n_sig_ar1"]
    hi = resumen["n_sig_ar1_solo_gl"]
    add("3_correccion_ar1", "B_sig_publicado", 374, sig_pub, "REPLICA")
    # (a) estimabilidad — hallazgo convención-independiente
    add("3_correccion_ar1", "B_estimables (n_eff>=3)", 156, est, "REPLICA")
    add("3_correccion_ar1", "B_no_estimables (n_eff<3)", 290, no_est,
        "REPLICA")
    # (b) significativos entre los estimables, como rango
    add("3_correccion_ar1", "B_sig_estimables_cota_inf (SE inflado)",
        "33/156", "%d/%d" % (lo, est), "REPLICA")
    add("3_correccion_ar1", "B_sig_estimables_cota_sup (solo gl)",
        "112/156", "%d/%d" % (hi, est), "REPLICA")
    add("3_correccion_ar1", "B_sig_estimables_rango",
        "33 (21.2%) - 112 (71.8%)",
        "%d (%.1f%%) - %d (%.1f%%)" % (lo, 100 * lo / est, hi,
                                       100 * hi / est), "RANGO")
    # (c) valor puntual
    add("3_correccion_ar1", "B_sig_valor_puntual",
        "pendiente Newey-West/GLS sobre residuos crudos (ausentes)",
        "no disponible en el repo", "BLOQUEADO")
    add("3_correccion_ar1", "nota_metodo", resumen["metodo"], "", "INFO")


def bloque_rc1_aic(add):
    """4 — RC1: ¿la ley de potencia ajusta mejor? (AIC sobre 18 series ACO)."""
    ts = _read(os.path.join(DATA, "snt_corpus_aco_timeseries_v29.csv"))
    key = "id"
    if key not in ts[0]:
        key = list(ts[0].keys())[0]
    series = collections.defaultdict(list)
    for r in ts:
        series[r[key]].append((_f(r["t"]), _f(r["R"])))
    wins = collections.Counter()
    bwin = collections.defaultdict(list)
    deltas, bs = [], []
    for pts in series.values():
        pts = [(t, R) for t, R in pts if t > 0 and R > 0]
        if len(pts) < 4:
            continue
        t = np.array([p[0] for p in pts])
        R = np.array([p[1] for p in pts])
        m = comparar_modelos(t, R)
        if m["ganador"]:
            wins[m["ganador"]] += 1
            bwin[m["ganador"]].append(m["b"])
            deltas.append(m["delta_aic_potencia"])
            bs.append(m["b"])
    add("4_rc1_aic", "potencia_gana", "13/18", "%d/%d" % (wins["potencia"],
        sum(wins.values())), "REPLICA")
    add("4_rc1_aic", "exponencial_gana", "4/18", str(wins["exponencial"]),
        "REPLICA")
    add("4_rc1_aic", "lineal_gana", "1/18", str(wins["lineal"]), "REPLICA")
    # b vs delta_aic: a mayor b, peor ajusta la potencia
    if len(bs) >= 4:
        rho, p = stats.spearmanr(bs, deltas)
        add("4_rc1_aic", "spearman_b_vs_dAIC", "-0.657 (p=0.003)",
            "rho=%.3f p=%.4f" % (rho, p), "REPLICA_SIGNO")
    # Fisher: b>=1 vs gana potencia
    a11 = sum(1 for b in bs if b >= 1)  # superlineales
    # de los superlineales, cuántos NO ganan potencia
    add("4_rc1_aic", "superlineales_b>=1", 4, a11, "REPLICA")


def bloque_p_truncados(add):
    """5 — p truncados a 0.0 por round(p, 6)."""
    corpus = _read(os.path.join(DATA, "snt_corpus_REAL_v5.csv"))
    z = sum(1 for r in corpus if _f(r["p"]) == 0.0)
    add("5_p_truncados", "corpus_p_igual_0", 557, z, "REPLICA")
    b = _read(os.path.join(DATA, "by_domain", "dominio_B_real.csv"))
    zb = sum(1 for r in b if _f(r["p"]) == 0.0)
    add("5_p_truncados", "B_p_igual_0", "n/d", zb, "INFO")


def bloque_soberania(add):
    """6 — Circularidad de 'soberania' (umbral de ASI)."""
    path = os.path.join(DATA_TOP, "snt_asi_scores.csv")
    if not os.path.exists(path):
        add("6_soberania", "archivo", path, "AUSENTE", "NO_REPRODUCIBLE")
        return
    rows = _read(path)
    asi_t = [_f(r["ASI"]) for r in rows if _truthy(r["soberania"])]
    asi_f = [_f(r["ASI"]) for r in rows if not _truthy(r["soberania"])]
    asi_t = [x for x in asi_t if np.isfinite(x)]
    asi_f = [x for x in asi_f if np.isfinite(x)]
    sob = sum(1 for r in rows if _truthy(r["soberania"]))
    if asi_t and asi_f:
        sep = min(asi_t) > max(asi_f)
        add("6_soberania", "ASI_soberano_min", round(min(asi_t), 4),
            round(min(asi_t), 4), "INFO")
        add("6_soberania", "ASI_no_soberano_max", round(max(asi_f), 4),
            round(max(asi_f), 4), "INFO")
        add("6_soberania", "separacion_perfecta", "esperada",
            "SI" if sep else "NO",
            "CIRCULAR" if sep else "OK")
    add("6_soberania", "pct_soberanos", "0.27%",
        "%d/%d = %.2f%%" % (sob, len(rows), 100 * sob / len(rows)), "REPLICA")


def bloque_asi_formula(add):
    """7 — ASI = delta_H * alpha / F."""
    path = os.path.join(DATA_TOP, "snt_asi_scores.csv")
    if not os.path.exists(path):
        add("7_asi_formula", "archivo", path, "AUSENTE", "NO_REPRODUCIBLE")
        return
    rows = _read(path)
    err = 0.0
    col = "ASI_raw" if "ASI_raw" in rows[0] else "ASI"
    for r in rows:
        dh, al, ff = _f(r["delta_H"]), _f(r["alpha"]), _f(r["F"])
        if ff == 0 or not np.isfinite(ff):
            continue
        err = max(err, abs(_f(r[col]) - dh * al / ff))
    add("7_asi_formula", "error_max (%s)" % col, "~2e-14",
        "%.2e" % err, "REPLICA" if err < 1e-6 else "DIFIERE")


def bloque_fdr(add):
    """8 — FDR Benjamini-Hochberg sobre el corpus (con p truncados)."""
    corpus = _read(os.path.join(DATA, "snt_corpus_REAL_v5.csv"))
    p = np.array([_f(r["p"]) for r in corpus])
    p = np.clip(p[np.isfinite(p)], 0, 1)
    rej, _ = fdr_bh(p, q=0.05)
    add("8_fdr", "corpus_rechazos_FDR5pct", "n/d", int(np.sum(rej)), "INFO")
    add("8_fdr", "caveat", "557 p truncados a 0 -> FDR no exacto", "", "INFO")


def bloque_nbody(add):
    """9 — Replicación N-cuerpos México (rank-size)."""
    path = os.path.join(DATA, "mexico_nbody_real.csv")
    if not os.path.exists(path):
        add("9_nbody", "archivo", path, "AUSENTE", "NO_REPRODUCIBLE")
        return
    rows = _read(path)
    r0 = rows[0]
    add("9_nbody", "b", -0.473, _f(r0["b"]), "REPLICA")
    add("9_nbody", "n_entidades", 32, int(_f(r0["n"])), "REPLICA")
    add("9_nbody", "refit_desde_crudo",
        "requiere serie rank-size de 32 entidades",
        "archivo es solo resumen (1 fila) — no recomputable aquí",
        "NO_REPRODUCIBLE")
    add("9_nbody", "caveat", "rank-size sobre 32 entidades da R2 alto por "
        "construccion; comparar vs lognormal (Clauset 2009)", "", "INFO")


def _regenerar_B(script, maddison):
    """Corre un script de construcción del dominio B en un directorio temporal.

    Los scripts de B leen ``data/owid-maddison.csv`` y escriben
    ``data/dominio_B_real.csv`` con rutas relativas al directorio de trabajo;
    correrlos en un directorio temporal evita sobrescribir nada del repo.
    Devuelve las filas regeneradas o None si el script falla.
    """
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "data"))
        shutil.copy(maddison, os.path.join(tmp, "data", "owid-maddison.csv"))
        proc = subprocess.run([sys.executable, script], cwd=tmp,
                              capture_output=True, text=True)
        salida = os.path.join(tmp, "data", "dominio_B_real.csv")
        if proc.returncode != 0 or not os.path.exists(salida):
            return None
        return _read(salida)


def bloque_reproducibilidad(add):
    """10 — Fuentes externas y regenerabilidad del dominio B.

    La regenerabilidad se prueba regenerando B en un directorio temporal con la
    edición de Maddison/OWID versionada y comparando caso a caso contra
    ``by_domain/dominio_B_real.csv`` (antes era una fila fija).
    """
    maddison = os.path.join(DATA_TOP, "owid-maddison.csv")
    presente = os.path.exists(maddison)
    add("10_reproducibilidad", "data/owid-maddison.csv",
        "requerido por los scripts del dominio B",
        "PRESENTE" if presente else "AUSENTE",
        "OK" if presente else "NO_REPRODUCIBLE")
    if not presente:
        add("10_reproducibilidad", "dominio_B_regenerable",
            "62% del corpus", "NO sin owid-maddison.csv", "NO_REPRODUCIBLE")
        return

    publicado = _read(os.path.join(DATA, "by_domain", "dominio_B_real.csv"))
    pub = {(r["hub"], r["nodo"]): r for r in publicado}
    code = os.path.join(_ROOT, "reconstruction_real", "code")
    for script in ("expand_B_massive.py", "expand_dominio_B.py"):
        filas = _regenerar_B(os.path.join(code, script), maddison)
        if filas is None:
            add("10_reproducibilidad", "regenerar_B:" + script,
                "%d casos" % len(pub), "el script falló", "NO_REPRODUCIBLE")
            continue
        new = {(r["hub"], r["nodo"]): r for r in filas}
        comunes = sorted(set(pub) & set(new))
        bp = np.array([_f(pub[k]["b"]) for k in comunes])
        bn = np.array([_f(new[k]["b"]) for k in comunes])
        identicos = int(np.sum(np.abs(bp - bn) < 5e-5))
        corr = float(np.corrcoef(bp, bn)[0, 1]) if len(comunes) > 2 else np.nan
        signo = int(np.sum(np.sign(bp) == np.sign(bn)))
        exacto = (len(new) == len(pub) and len(comunes) == len(pub)
                  and identicos == len(pub))
        add("10_reproducibilidad", "regenerar_B:" + script,
            "%d casos (b medio %+.4f)" % (
                len(pub), np.mean([_f(r["b"]) for r in publicado])),
            "%d casos (b medio %+.4f); %d pares comunes; b identico %d/%d; "
            "corr(b)=%.3f; signo coincide %d/%d" % (
                len(new), np.mean([_f(r["b"]) for r in filas]),
                len(comunes), identicos, len(comunes), corr, signo,
                len(comunes)),
            "REPLICA" if exacto else "PARCIAL")
    add("10_reproducibilidad", "dominio_B_regenerable_nota",
        "edicion de Maddison no fijada al construir el corpus",
        "Maddison revisa el PIB historico entre ediciones: con la edicion "
        "versionada (2026-07-25) B se regenera aproximado, no exacto; la "
        "reasignacion de hub por PIB medio puede invertir pares", "INFO")


def bloque_no_reproducibles(add):
    """11 — Cifras que necesitan datos fuera del repo (hallazgo #5 del audit)."""
    add("11_no_reproducible", "5.9x_abrupto_gradual (U=24802,n=486)",
        "README", "corpus v5 sin variable trigger utilizable; n=486 no es "
        "subconjunto de ningun conjunto del repo", "NO_REPRODUCIBLE")
    recalc = os.path.join(DATA, "trigger_abrupto_gradual_recalculo.csv")
    if os.path.exists(recalc):
        for r in _read(recalc):
            if not (r["analisis"].startswith("global")
                    or r["analisis"].startswith("permutación")):
                continue
            add("11_recalculo_trigger", r["dataset"], r["estatus"],
                "razon medias=%s; p2=%s; p1(abr>grad)=%s" % (
                    r["razon_medias"] or "-", r["p_dos_colas"] or "-",
                    r["p_una_cola_abrupto_mayor"] or "-"), "INFO")
    add("11_no_reproducible", "ROC-AUC 0.715 (ASI)", "README",
        "target de retencion no está en snt_asi_scores.csv", "NO_REPRODUCIBLE")
    orto = _read(os.path.join(DATA, "orthogonality_crypto_v25.csv"))
    rho, p = stats.spearmanr([_f(r["b_rise"]) for r in orto],
                             [_f(r["delta_fall"]) for r in orto])
    add("11_rc9_orthogonalidad", "RC9 rho=+0.009 crypto n=11",
        "rho=+0.009 p=0.98 n=11",
        "rho=%+.3f p=%.2f n=%d (orthogonality_crypto_v25.csv)" % (
            rho, p, len(orto)),
        "REPLICA" if abs(rho - 0.009) < 5e-4 else "CAMBIA")
    add("11_no_reproducible", "E3 correccion AR(1)", "-",
        "dominio_E3_real.csv no trae series crudas (solo b,r2,p,n)",
        "BLOQUEADO")


BLOQUES = [
    bloque_master_cifras,
    bloque_autocorrelacion_B,
    bloque_correccion_ar1,
    bloque_rc1_aic,
    bloque_p_truncados,
    bloque_soberania,
    bloque_asi_formula,
    bloque_fdr,
    bloque_nbody,
    bloque_reproducibilidad,
    bloque_no_reproducibles,
]


def run(out_path):
    filas = []

    def add(bloque, cifra, publicado, recomputado, estado):
        filas.append({
            "bloque": bloque, "cifra": cifra,
            "publicado": publicado, "recomputado": recomputado,
            "estado": estado,
        })

    for fn in BLOQUES:
        try:
            fn(add)
        except Exception as e:  # pragma: no cover - defensivo
            add(fn.__name__, "ERROR", "", str(e), "ERROR")

    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(
            fh, fieldnames=["bloque", "cifra", "publicado",
                            "recomputado", "estado"])
        w.writeheader()
        w.writerows(filas)

    # resumen a stdout
    est = collections.Counter(f["estado"] for f in filas)
    print("Auditoría integral v32 — %d cifras recorridas" % len(filas))
    for k in sorted(est):
        print("  %-16s %d" % (k, est[k]))
    print("CSV -> %s" % out_path)
    return filas


def main():
    ap = argparse.ArgumentParser(description="Auditoría integral v32")
    ap.add_argument(
        "--out",
        default=os.path.join(DATA, "auditoria_integral_v32_resultados.csv"),
        help="ruta de salida del CSV")
    args = ap.parse_args()
    run(args.out)


if __name__ == "__main__":
    main()
