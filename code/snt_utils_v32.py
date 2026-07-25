"""
Shadow Node Theory — Shared utilities, v32 (audit extension)
Fractal Core Research | Tlaxcala, Mexico | 2026

Extends ``code/snt_utils.py`` with the machinery the integral audit (v32)
needed and that the base module did not expose:

  * Durbin-Watson (``dw``) for *every* fit, not just domain B.
  * The AR(1) diagnostics that drive the audit's headline finding:
    ``rho_ar1``, ``n_eff`` (Bartlett) and a proper Newey-West (HAC) slope
    p-value ``p_ar1``.
  * Both R^2 conventions kept separate — ``r2_log`` (Pearson^2 on the
    log-log fit, the definition domain B used) and ``r2_raw``
    (1 - SSres/SStot on the raw ratio, what the other domains used).
  * ``p_exacto`` — the slope p-value *without* ``round(p, 6)``, so the 557
    corpus rows truncated to ``0.0`` stop blocking FDR / meta-analysis.
  * ``se_b`` / ``ci_lo`` / ``ci_hi`` for every fit.
  * ``comparar_modelos`` — the RC1 test (power vs exponential vs linear by
    AIC) that the README claimed but no committed script implemented.
  * ``ajustar_mle_clauset`` — the long-pending MLE + KS power-law fit.
  * ``spearman_cluster`` — cluster-level Spearman (generalises the rc12 fix).
  * ``corregir_corpus`` — post-hoc AR(1) correction over an already-fitted
    corpus that carries a ``dw`` column, *without* re-fitting.
  * ``fdr_bh`` — Benjamini-Hochberg over the 721-case corpus.
  * ``plegado_trigger`` — flags the ``t = |year - trigger| + 1e-6`` folding
    bug in the base fitter (points either side of the trigger collapse to
    the same t).

Retro-compatible: ``ajustar_ley_potencia`` returns every key the base
version returned, plus the new ones. Existing scripts keep working after
swapping the import.

References for the corrections:
  * Bartlett (1946) — effective sample size of an AR(1) mean.
  * Newey & West (1987) — heteroskedasticity/autocorrelation-consistent
    covariance.
  * Clauset, Shalizi & Newman (2009) — power-law MLE + KS.
  * Benjamini & Hochberg (1995) — false discovery rate.
"""

import warnings

import numpy as np
from scipy import stats

# Keep the base classification bands importable/usable from here.
try:
    from snt_utils import ajustar_ley_potencia as _ajustar_base  # noqa: F401
except Exception:  # pragma: no cover - base import is best-effort
    _ajustar_base = None


def _clasificar(b):
    """The base module's classification bands (kept in sync)."""
    if b > 2.0:
        return "Satelizacion extrema (b>2)"
    if b > 1.0:
        return "Satelizacion rapida sin friccion"
    if b > 0.3:
        return "Satelizacion activa"
    if b > 0.05:
        return "Satelizacion gradual"
    if b > -0.1:
        return "Estado estacionario / equilibrio"
    return "Convergencia / leapfrog"


def durbin_watson(resid):
    """Durbin-Watson statistic of an OLS residual vector."""
    e = np.asarray(resid, dtype=float)
    if e.size < 2:
        return float("nan")
    denom = np.sum(e ** 2)
    if denom == 0:
        return float("nan")
    return float(np.sum(np.diff(e) ** 2) / denom)


def n_efectivo(n, rho):
    """Bartlett effective sample size for an AR(1) process.

    ``n_eff = n * (1 - rho) / (1 + rho)``. This is derived for the *mean*
    of an AR(1) series, not a regression slope, so treat it as an
    order-of-magnitude deflator, never a final correction (use Newey-West
    / GLS for that). See ``p_ar1`` for the proper HAC slope test.
    """
    rho = max(min(float(rho), 0.999), -0.999)
    ne = float(n) * (1.0 - rho) / (1.0 + rho)
    return max(ne, 0.0)


def _newey_west_lag(n):
    """Standard automatic Bartlett bandwidth: floor(4*(n/100)^(2/9))."""
    if n <= 0:
        return 0
    return int(np.floor(4.0 * (n / 100.0) ** (2.0 / 9.0)))


def _ols_slope(x, y):
    """Simple OLS of y on x. Returns (b, a, resid, sxx, xbar)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    xbar = x.mean()
    ybar = y.mean()
    xc = x - xbar
    sxx = float(np.sum(xc ** 2))
    b = float(np.sum(xc * (y - ybar)) / sxx) if sxx > 0 else 0.0
    a = float(ybar - b * xbar)
    resid = y - (a + b * x)
    return b, a, resid, sxx, xbar


def newey_west_slope(x, y, lag=None):
    """Newey-West (HAC) standard error and p-value for the OLS slope.

    Returns dict with ``b``, ``se_ols``, ``se_nw``, ``t_nw``, ``p_nw``,
    ``lag``. Falls back gracefully for tiny samples.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = x.size
    out = {
        "b": float("nan"), "se_ols": float("nan"), "se_nw": float("nan"),
        "t_nw": float("nan"), "p_nw": float("nan"), "lag": 0,
    }
    if n < 3:
        return out
    b, a, e, sxx, xbar = _ols_slope(x, y)
    out["b"] = b
    if sxx <= 0:
        return out
    dof = n - 2
    sigma2 = float(np.sum(e ** 2) / dof) if dof > 0 else float("nan")
    out["se_ols"] = float(np.sqrt(sigma2 / sxx)) if sigma2 == sigma2 else float("nan")

    if lag is None:
        lag = _newey_west_lag(n)
    lag = max(0, min(int(lag), n - 1))
    out["lag"] = lag

    xc = x - xbar
    u = xc * e  # score contributions for the slope
    # Bartlett-weighted long-run variance of the scores.
    s = float(np.sum(u ** 2))
    for k in range(1, lag + 1):
        w = 1.0 - k / (lag + 1.0)
        s += 2.0 * w * float(np.sum(u[k:] * u[:-k]))
    var_b = s / (sxx ** 2)
    if var_b <= 0:
        return out
    se_nw = float(np.sqrt(var_b))
    out["se_nw"] = se_nw
    t = b / se_nw
    out["t_nw"] = float(t)
    if dof > 0:
        out["p_nw"] = float(2.0 * stats.t.sf(abs(t), dof))
    return out


def fit_powerlaw(t, r):
    """Full log-log power-law fit with autocorrelation diagnostics.

    ``t``, ``r`` are the (already positive) time and ratio arrays. Returns a
    dict with the base keys plus: ``r2_raw``, ``r2_log``, ``se_b``,
    ``ci_lo``, ``ci_hi``, ``p_exacto``, ``dw``, ``rho_ar1``, ``n_eff``,
    ``p_ar1``, ``nw_lag``.
    """
    t = np.asarray(t, dtype=float)
    r = np.asarray(r, dtype=float)
    mask = (t > 0) & (r > 0) & np.isfinite(t) & np.isfinite(r)
    t = t[mask]
    r = r[mask]
    n = t.size
    res = {
        "a": None, "b": None, "r2": None, "r2_raw": None, "r2_log": None,
        "r_pearson": None, "p_value": None, "p_exacto": None,
        "se_b": None, "ci_lo": None, "ci_hi": None,
        "dw": None, "rho_ar1": None, "n_eff": None, "p_ar1": None,
        "nw_lag": None, "clasificacion": "", "n": int(n),
    }
    if n < 3:
        res["clasificacion"] = "Datos insuficientes"
        return res

    log_t = np.log(t)
    log_r = np.log(r)
    b, a_log, resid, sxx, _ = _ols_slope(log_t, log_r)
    a = float(np.exp(a_log))

    # Raw-scale and log-scale R^2, kept separate.
    r_pred = a * t ** b
    ss_res = float(np.sum((r - r_pred) ** 2))
    ss_tot = float(np.sum((r - r.mean()) ** 2))
    r2_raw = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    if np.std(log_t) == 0 or np.std(log_r) == 0:
        rp, pv = 0.0, 1.0
    else:
        rp, pv = stats.pearsonr(log_t, log_r)
    r2_log = float(rp) ** 2

    # OLS slope SE / CI / exact p.
    dof = n - 2
    sigma2 = float(np.sum(resid ** 2) / dof) if dof > 0 else float("nan")
    se_b = float(np.sqrt(sigma2 / sxx)) if (sxx > 0 and sigma2 == sigma2) else float("nan")
    if se_b == se_b and se_b > 0 and dof > 0:
        tcrit = stats.t.ppf(0.975, dof)
        ci_lo = b - tcrit * se_b
        ci_hi = b + tcrit * se_b
        p_exacto = float(2.0 * stats.t.sf(abs(b / se_b), dof))
    else:
        ci_lo = ci_hi = float("nan")
        p_exacto = float(pv)

    # Autocorrelation diagnostics.
    dw = durbin_watson(resid)
    rho = 1.0 - dw / 2.0 if dw == dw else 0.0
    n_eff = n_efectivo(n, rho)
    nw = newey_west_slope(log_t, log_r)

    res.update({
        "a": round(a, 6), "b": round(b, 4),
        "r2": round(r2_raw, 4),          # base key = raw-scale, unchanged
        "r2_raw": round(r2_raw, 4), "r2_log": round(r2_log, 4),
        "r_pearson": round(float(rp), 4),
        "p_value": round(float(pv), 6),  # base key kept (rounded)
        "p_exacto": p_exacto,            # full precision
        "se_b": None if se_b != se_b else round(se_b, 6),
        "ci_lo": None if ci_lo != ci_lo else round(ci_lo, 4),
        "ci_hi": None if ci_hi != ci_hi else round(ci_hi, 4),
        "dw": None if dw != dw else round(dw, 4),
        "rho_ar1": round(rho, 4),
        "n_eff": round(n_eff, 2),
        "p_ar1": nw["p_nw"],
        "nw_lag": nw["lag"],
        "clasificacion": _clasificar(b),
    })
    return res


def ajustar_ley_potencia(años, sombra, dominante, trigger_año):
    """Retro-compatible drop-in for ``snt_utils.ajustar_ley_potencia``.

    Same signature, same return keys as the base version, plus every key
    ``fit_powerlaw`` adds. Also folds points through the trigger exactly
    like the base fitter (so behaviour matches) and flags it via
    ``plegado`` when a collision happens.
    """
    tiempos, ratios, years_used = [], [], []
    for i, año in enumerate(años):
        if sombra[i] > 0 and dominante[i] > 0:
            t = abs(año - trigger_año) + 1e-6
            tiempos.append(t)
            ratios.append(dominante[i] / sombra[i])
            years_used.append(año)

    res = fit_powerlaw(np.array(tiempos), np.array(ratios))
    res["plegado"] = plegado_trigger(years_used, trigger_año)
    return res, np.array(tiempos), np.array(ratios)


def comparar_modelos(t, r):
    """RC1 test: does a power law fit better than exponential or linear?

    Fits all three by OLS (power on log-log, exponential on log-linear,
    linear on raw) and ranks them by AIC computed on the *raw* residuals so
    the scales are comparable. Returns dict with per-model AIC, the winner
    and ``delta_aic_potencia`` (AIC_best_other - AIC_power; positive means
    power wins).
    """
    t = np.asarray(t, dtype=float)
    r = np.asarray(r, dtype=float)
    mask = (t > 0) & (r > 0) & np.isfinite(t) & np.isfinite(r)
    t = t[mask]
    r = r[mask]
    n = t.size
    out = {"n": int(n), "aic": {}, "ganador": None, "delta_aic_potencia": None}
    if n < 4:
        return out

    def aic_from_pred(pred, k):
        rss = float(np.sum((r - pred) ** 2))
        if rss <= 0:
            rss = 1e-300
        return n * np.log(rss / n) + 2 * k

    # Power: log r = log a + b log t
    bp, ap_log, _, _, _ = _ols_slope(np.log(t), np.log(r))
    pred_pow = np.exp(ap_log) * t ** bp
    # Exponential: log r = c + d t
    de, ce, _, _, _ = _ols_slope(t, np.log(r))
    pred_exp = np.exp(ce) * np.exp(de * t)
    # Linear: r = m t + q
    ml, ql, _, _, _ = _ols_slope(t, r)
    pred_lin = ml * t + ql

    aic = {
        "potencia": aic_from_pred(pred_pow, 3),
        "exponencial": aic_from_pred(pred_exp, 3),
        "lineal": aic_from_pred(pred_lin, 3),
    }
    ganador = min(aic, key=aic.get)
    otros = min(v for k, v in aic.items() if k != "potencia")
    out["aic"] = {k: round(v, 3) for k, v in aic.items()}
    out["ganador"] = ganador
    out["delta_aic_potencia"] = round(otros - aic["potencia"], 3)
    out["b"] = round(bp, 4)
    return out


def ajustar_mle_clauset(x, xmin=None):
    """MLE power-law exponent + KS distance (Clauset et al. 2009).

    Continuous approximation. If ``xmin`` is None it sweeps candidate
    xmin values and picks the one minimising the KS distance.
    """
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x) & (x > 0)]
    if x.size < 3:
        return {"alpha": None, "xmin": None, "ks": None, "n_tail": 0}

    def fit_for(xm):
        tail = x[x >= xm]
        if tail.size < 2:
            return None
        alpha = 1.0 + tail.size / np.sum(np.log(tail / xm))
        srt = np.sort(tail)
        cdf_emp = np.arange(1, srt.size + 1) / srt.size
        cdf_mod = 1.0 - (srt / xm) ** (-(alpha - 1.0))
        ks = float(np.max(np.abs(cdf_emp - cdf_mod)))
        return {"alpha": float(alpha), "xmin": float(xm),
                "ks": ks, "n_tail": int(tail.size)}

    if xmin is not None:
        r = fit_for(xmin)
        return r or {"alpha": None, "xmin": xmin, "ks": None, "n_tail": 0}

    best = None
    for xm in np.unique(x):
        r = fit_for(xm)
        if r and (best is None or r["ks"] < best["ks"]):
            best = r
    return best or {"alpha": None, "xmin": None, "ks": None, "n_tail": 0}


def spearman_cluster(x, y, groups):
    """Cluster-aware Spearman: correlate group means, not raw rows.

    Guards against the pseudo-replication that inflates the by-row
    p-value (714 non-independent cases treated as independent).
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    groups = np.asarray(groups)
    gx, gy = [], []
    for g in np.unique(groups):
        m = groups == g
        if np.sum(m) == 0:
            continue
        gx.append(np.nanmean(x[m]))
        gy.append(np.nanmean(y[m]))
    if len(gx) < 3:
        return {"rho": float("nan"), "p": float("nan"), "n_clusters": len(gx)}
    rho, p = stats.spearmanr(gx, gy)
    return {"rho": float(rho), "p": float(p), "n_clusters": len(gx)}


def corregir_corpus(rows, dw_key="dw", n_key="n", se_key="se_b", b_key="b"):
    """Post-hoc AR(1) correction over an already-fitted corpus.

    Operates on a list of dict rows that already carry ``dw`` — it does
    *not* re-fit. For each row it derives ``rho = 1 - dw/2``, the Bartlett
    ``n_eff``, the standard-error inflation factor
    ``infl = sqrt((1 + rho) / (1 - rho))``, and evaluates the corrected
    slope significance on ``df = n_eff - 2`` **with a ``df > 0`` gate**: a
    case with ``n_eff < 3`` cannot support a two-parameter fit, so it is
    marked ``estimable = False`` and never counted as significant. Flooring
    df at 1 (an earlier attempt) fabricates a 1-dof test where there is no
    data for one — rejected on cross-review, 2026-07-25.

    Report significance **among the estimable cases**, not over the full
    ``n`` — the two are different claims (see the v32 audit §1). The
    ``estimable`` split is the cleaner, convention-independent finding:
    it falls straight out of ``n_eff < 3`` and does not depend on the
    Bartlett approximation at all.

    Two variants remain, both gated by ``df > 0``:

    * ``sig_ar1`` — **coherent lower bound**: inflate the SE *and* cut the
      dof (``t' = (b/se) / infl``). If observations are correlated the slope
      variance grows, so the SE must inflate *in addition to* losing dof.
      Invariant to the df convention (33 either way).
    * ``sig_ar1_solo_gl`` — **upper bound**: cut the dof only, leave ``t``
      untouched. The incoherent half-correction the original audit reported;
      kept as the upper bracket.

    The Bartlett ``infl`` factor is derived for the *mean* of an AR(1), not
    a regression slope, so the true Newey-West/GLS value sits inside the
    bracket and needs the raw residuals (absent from the repo). A
    ``UserWarning`` says so.

    Rows without a usable ``dw`` pass through with ``corregible=False``.
    Returns (rows_out, resumen). Each output row gains ``rho_ar1``,
    ``n_eff``, ``se_infl``, ``estimable``, ``p_ar1``, ``sig_ar1``,
    ``sig_ar1_solo_gl`` and ``corregible``.
    """
    out = []
    n_corr = n_total = 0
    n_estimables = 0
    n_sig_ar1 = n_sig_solo_gl = 0
    for row in rows:
        r = dict(row)
        n_total += 1
        try:
            dw = float(row[dw_key])
            n = float(row[n_key])
        except (KeyError, TypeError, ValueError):
            dw = float("nan")
            n = float("nan")
        se = None
        try:
            se = float(row[se_key])
        except (KeyError, TypeError, ValueError):
            se = None
        b = None
        try:
            b = float(row[b_key])
        except (KeyError, TypeError, ValueError):
            b = None

        if not (dw == dw) or not (n == n) or n < 3:
            r.update({"rho_ar1": None, "n_eff": None, "se_infl": None,
                      "estimable": None, "p_ar1": None, "sig_ar1": None,
                      "sig_ar1_solo_gl": None, "corregible": False})
            out.append(r)
            continue

        rho = max(min(1.0 - dw / 2.0, 0.999), -0.999)
        n_eff = n_efectivo(n, rho)
        infl = float(np.sqrt((1.0 + rho) / (1.0 - rho)))
        n_corr += 1
        # Estimability: a two-parameter fit needs n_eff >= 3 (df = n_eff-2 > 0).
        estimable = n_eff >= 3.0
        if estimable:
            n_estimables += 1
        p_ar1 = None
        sig = sig_gl = None
        if se is not None and se > 0 and b is not None:
            dof = n_eff - 2.0
            if estimable and dof > 0:
                t0 = abs(b / se)
                p_ar1 = float(2.0 * stats.t.sf(t0 / infl, dof))  # coherent
                p_gl = float(2.0 * stats.t.sf(t0, dof))          # dof-only
                sig = bool(p_ar1 < 0.05)
                sig_gl = bool(p_gl < 0.05)
            else:
                # n_eff < 3: not estimable, never counted as significant.
                sig = False
                sig_gl = False
            if sig:
                n_sig_ar1 += 1
            if sig_gl:
                n_sig_solo_gl += 1
        r.update({
            "rho_ar1": round(rho, 4),
            "n_eff": round(n_eff, 2),
            "se_infl": round(infl, 3),
            "estimable": estimable,
            "p_ar1": p_ar1,
            "sig_ar1": sig,
            "sig_ar1_solo_gl": sig_gl,
            "corregible": True,
        })
        out.append(r)

    if n_corr:
        warnings.warn(
            "corregir_corpus: de %d casos, %d NO son estimables (n_eff<3) y se "
            "reportan como no estimables, no como no significativos. Entre los "
            "%d estimables, los significativos AR(1) son un RANGO [%d (SE "
            "inflado), %d (solo gl)], no un punto; el valor final requiere "
            "Newey-West/GLS sobre residuos crudos."
            % (n_corr, n_corr - n_estimables, n_estimables,
               n_sig_ar1, n_sig_solo_gl),
            UserWarning, stacklevel=2)

    resumen = {
        "n_total": n_total,
        "n_corregibles": n_corr,
        "n_estimables": n_estimables,               # n_eff >= 3
        "n_no_estimables": n_corr - n_estimables,   # n_eff < 3
        "n_sig_ar1": n_sig_ar1,               # cota inf. entre estimables
        "n_sig_ar1_solo_gl": n_sig_solo_gl,   # cota sup. entre estimables
        "metodo": "AR(1) analitico. Reportar significancia ENTRE los "
                  "estimables (n_eff>=3); los no estimables (n_eff<3) son no "
                  "estimables, no no-significativos. Rango [SE inflado, solo "
                  "gl]; valor puntual pendiente de Newey-West/GLS.",
    }
    return out, resumen


def fdr_bh(pvals, q=0.05):
    """Benjamini-Hochberg FDR. Returns (rejected_mask, p_adjusted)."""
    p = np.asarray(pvals, dtype=float)
    n = p.size
    if n == 0:
        return np.array([], dtype=bool), np.array([])
    order = np.argsort(p)
    ranked = p[order]
    adj = ranked * n / (np.arange(1, n + 1))
    # enforce monotonicity from the top
    adj = np.minimum.accumulate(adj[::-1])[::-1]
    adj = np.clip(adj, 0, 1)
    p_adj = np.empty(n)
    p_adj[order] = adj
    return p_adj <= q, p_adj


def plegado_trigger(años, trigger_año, tol=1e-9):
    """Detect the ``t = |year - trigger|`` folding collision.

    In the base fitter, a point before the trigger and one after it at the
    same distance map to the *same* t, and a point exactly on the trigger
    gets ``t = 1e-6`` whose ``log`` (-13.8) dominates the OLS. Returns a
    dict describing whether either pathology is present.
    """
    años = np.asarray(list(años), dtype=float)
    if años.size == 0:
        return {"colision": False, "punto_en_trigger": False, "n_colisiones": 0}
    t = np.abs(años - trigger_año)
    en_trigger = bool(np.any(t < tol))
    # count folded pairs (same distance, opposite sides)
    colisiones = 0
    vistos = {}
    for val, yr in zip(t, años):
        key = round(float(val), 9)
        if key in vistos and (yr - trigger_año) * (vistos[key] - trigger_año) < 0:
            colisiones += 1
        else:
            vistos[key] = yr
    return {
        "colision": colisiones > 0,
        "punto_en_trigger": en_trigger,
        "n_colisiones": colisiones,
    }
