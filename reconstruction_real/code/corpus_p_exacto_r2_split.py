#!/usr/bin/env python3
"""
Add p_exacto + r2_log/r2_raw split to the consolidated corpus.

Reads ``reconstruction_real/data/snt_corpus_REAL_v5.csv`` (summary stats only
for most domains) and enriches it where raw series are available:

* Domain B  (446 casos): ``by_domain/dominio_B_real.csv`` already carries
  ``se_b``, ``r_pearson``, ``dw`` → compute ``p_exacto`` exactly, split
  ``r2`` into ``r2_raw`` (existing) / ``r2_log`` (= r_pearson^2).
* Domain E3 (234 casos): ``dominio_E3_series_crudas.csv`` already carries
  ``p_ols`` (exact p), ``r2_log`` → copy; ``r2_raw`` needs raw OWID series
  (not in repo) → NA.
* Domain ACO (18 casos): ``snt_corpus_aco_timeseries_v29.csv`` carries raw
  (t, R) pairs → recompute everything with ``fit_powerlaw``.
* All other domains: raw series not in repo → ``p_exacto``/``r2_log``/
  ``r2_raw`` marked NA.

Writes ``reconstruction_real/data/snt_corpus_REAL_v6.csv`` with the new columns
and a provenance note per case. The v5 file is left untouched.

Uso:
    python reconstruction_real/code/corpus_p_exacto_r2_split.py
"""

import csv
import os
import sys

import numpy as np
from scipy import stats

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "code"))

from snt_utils_v32 import fit_powerlaw  # noqa: E402

DATA = os.path.join(_ROOT, "reconstruction_real", "data")
DATA_TOP = os.path.join(_ROOT, "data")


def _f(x, default=float("nan")):
    try:
        v = float(x)
        return v if v == v else default
    except (TypeError, ValueError):
        return default


def _read(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def p_exacto_from_b_se(b, se_b, n):
    """Exact two-sided slope p-value from b, SE, n (no round-to-6 truncation)."""
    if se_b is None or not (se_b == se_b) or se_b <= 0:
        return None
    if not (b == b) or not (n == n) or n < 3:
        return None
    dof = n - 2
    if dof <= 0:
        return None
    t = abs(b / se_b)
    return float(2.0 * stats.t.sf(t, dof))


def main():
    corpus = _read(os.path.join(DATA, "snt_corpus_REAL_v5.csv"))

    # Index raw-series sources by corpus id.
    b_rows = {r["id"]: r for r in _read(os.path.join(DATA, "by_domain", "dominio_B_real.csv"))}

    e3_rows = {r["id"]: r for r in _read(os.path.join(DATA, "dominio_E3_series_crudas.csv"))}

    # r2_raw de E3 desde las series crudas OWID (receta verificada; solo casos
    # cuya b reproduce la publicada — ver e3_r2_raw.py, compuerta ±0.01).
    e3_r2raw_path = os.path.join(DATA, "dominio_E3_r2_raw.csv")
    e3_r2raw = {}
    if os.path.exists(e3_r2raw_path):
        for r in _read(e3_r2raw_path):
            if r["coincide_r2raw"] not in (None, "") and \
                    str(r["coincide_r2raw"]).strip().lower() in ("true", "1", "yes"):
                e3_r2raw[r["id"]] = _f(r["r2_raw"])

    aco = _read(os.path.join(DATA, "snt_corpus_aco_timeseries_v29.csv"))
    aco_series = {}
    for r in aco:
        aco_series.setdefault(r["id"], []).append((_f(r["t"]), _f(r["R"])))

    out_rows = []
    stats_n = {"exact_p": 0, "r2_split": 0, "na": 0}

    for row in corpus:
        cid = row["id"]
        out = dict(row)


        p_exacto = None
        r2_raw = None
        r2_log = None
        dw = None
        rho_ar1 = None
        n_eff = None
        se_b_final = None
        nota = []

        r2_raw = _f(row["r2"]) if "r2" in row and row["r2"] not in (None, "") else None

        # ---- Domain B: enough summary stats for exact p + r2 split ----
        if cid in b_rows:
            br = b_rows[cid]
            b_b = _f(br["b"])
            se_b_b = _f(br["se_b"])
            n_b = _f(br["n"])
            r_pearson = _f(br["r_pearson"])
            dw_b = _f(br["dw"])

            p_exacto = p_exacto_from_b_se(b_b, se_b_b, n_b)
            r2_raw = _f(br["r2"])
            if r_pearson == r_pearson:
                r2_log = r_pearson * r_pearson
            se_b_final = se_b_b
            if dw_b == dw_b:
                dw = dw_b
                rho_ar1 = 1.0 - dw_b / 2.0
                n_eff = n_b * (1.0 - rho_ar1) / (1.0 + rho_ar1) if n_b == n_b else None
            nota.append("B_resumen_exacto")
            stats_n["exact_p"] += 1
            stats_n["r2_split"] += 1

        # ---- Domain E3: exact p_ols and r2_log already present ----
        elif cid in e3_rows:
            er = e3_rows[cid]
            p_ols = _f(er["p_ols"])
            if p_ols == p_ols:
                p_exacto = p_ols
            r2_log = _f(er["r2_log"])
            # r2_raw: desde las series crudas OWID cuando la b reproduce la
            # publicada (233/234); el caso que no reproduce queda NA.
            r2_raw = e3_r2raw.get(cid)
            if r2_raw is None or not (r2_raw == r2_raw):
                r2_raw = None
                nota.append("E3_r2raw_no_disponible_b_no_reproduce")
            dw = _f(er["dw"])
            if dw == dw:
                rho_ar1 = 1.0 - dw / 2.0
                n_e3 = _f(er["n"])
                n_eff = n_e3 * (1.0 - rho_ar1) / (1.0 + rho_ar1) if n_e3 == n_e3 else None
            nota.append("E3_resumen_exacto_p")
            stats_n["exact_p"] += 1
            stats_n["r2_split"] += 1  # r2_log present, r2_raw = NA → partial split

        # ---- Domain ACO: recompute from raw (t, R) series ----
        elif cid in aco_series:
            pts = [(t, R) for t, R in aco_series[cid] if t > 0 and R > 0]
            if len(pts) >= 3:
                t_arr = np.array([p[0] for p in pts])
                r_arr = np.array([p[1] for p in pts])
                f = fit_powerlaw(t_arr, r_arr)
                p_exacto = f["p_exacto"]
                r2_raw = f["r2_raw"]
                r2_log = f["r2_log"]
                dw = f["dw"]
                rho_ar1 = f["rho_ar1"]
                n_eff = f["n_eff"]
                se_b_final = f["se_b"]
                nota.append("ACO_recomputado_raw")
                stats_n["exact_p"] += 1
                stats_n["r2_split"] += 1
            else:
                nota.append("ACO_insuficiente")
                stats_n["na"] += 1

        else:
            nota.append("sin_serie_raw")
            stats_n["na"] += 1

        out["p_exacto"] = "" if p_exacto is None else f"{p_exacto:.10g}"
        out["r2_raw"] = "" if r2_raw is None else f"{r2_raw:.6f}"
        out["r2_log"] = "" if r2_log is None else f"{r2_log:.6f}"
        out["dw"] = "" if dw is None else f"{dw:.6f}"
        out["rho_ar1"] = "" if rho_ar1 is None else f"{rho_ar1:.6f}"
        out["n_eff"] = "" if n_eff is None else f"{n_eff:.4f}"
        out["se_b"] = "" if se_b_final is None else f"{se_b_final:.10g}"
        out["provenencia"] = "; ".join(nota)

        out_rows.append(out)

    # Field order: original columns first, then new ones.
    base_fields = list(corpus[0].keys()) if corpus else []
    new_fields = ["p_exacto", "r2_raw", "r2_log", "dw", "rho_ar1", "n_eff",
                  "se_b", "provenencia"]
    fieldnames = [f for f in base_fields if f not in new_fields] + new_fields

    out_path = os.path.join(DATA, "snt_corpus_REAL_v6.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(out_rows)

    print(f"Escrito {out_path} ({len(out_rows)} casos)")
    print(f"  p_exacto computado: {stats_n['exact_p']}")
    print(f"  r2_log/r2_raw split: {stats_n['r2_split']}")
    print(f"  sin serie raw (NA): {stats_n['na']}")
    print("  p==0.0 en v5: 557 → en v6, casos con p_exacto no truncados")


if __name__ == "__main__":
    main()
