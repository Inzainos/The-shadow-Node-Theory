"""
snt_market_core.py — SNT satellization core for market data (Delta)
====================================================================
Self-contained port of the Shadow Node Theory satellization engine,
specialized for financial time series. Delta is independent of the Omega
codebase; this module carries the correlation logic it needs so the project
has no cross-repo dependency.

Core law:  R(t) = a · t^b     (dominance ratio hub/shadow over time)

Regime by exponent b (SNT v2.5.0 thresholds):
  b > 2.0   → EXTREME satellization
  b > 1.0   → ROCHE_RADIUS (fast, near-capture)
  b > 0.3   → SATELLIZATION_ACTIVE
  b > 0.05  → SATELLIZATION_GRADUAL
  b > -0.1  → EQUILIBRIUM
  b ≤ -0.1  → CONVERGENCE / leapfrog

Estimation: OLS on log-log space (np.polyfit), Pearson on log-log.
Faithful to code/snt_utils.py in the SNT theory repo and to the Omega
satellization engine (sentinel_omega/core/snt_engine/satellization.py).
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

import numpy as np
from scipy.stats import pearsonr


class DominanceRegime(Enum):
    CONVERGENCE = "convergence"
    EQUILIBRIUM = "equilibrium"
    SATELLIZATION_GRADUAL = "satellization_gradual"
    SATELLIZATION_ACTIVE = "satellization_active"
    ROCHE_RADIUS = "roche_radius"
    EXTREME = "extreme"


@dataclass
class SatellizationResult:
    a: float
    b: float
    r_squared: float
    r_pearson: float
    p_value: float
    regime: DominanceRegime
    n_observations: int


def classify_regime(b: float) -> DominanceRegime:
    """Map an exponent b to its SNT dominance regime (v2.5.0 thresholds)."""
    if b > 2.0:
        return DominanceRegime.EXTREME
    if b > 1.0:
        return DominanceRegime.ROCHE_RADIUS
    if b > 0.3:
        return DominanceRegime.SATELLIZATION_ACTIVE
    if b > 0.05:
        return DominanceRegime.SATELLIZATION_GRADUAL
    if b > -0.1:
        return DominanceRegime.EQUILIBRIUM
    return DominanceRegime.CONVERGENCE


def fit_satellization(t: np.ndarray, ratio: np.ndarray) -> SatellizationResult:
    """
    Fit R(t) = a · t^b on a precomputed dominance ratio series via log-log OLS.

    t     : monotonically increasing time index (>0), e.g. bars since window start.
    ratio : hub/shadow dominance ratio (>0) aligned with t.

    Raises ValueError if fewer than 3 valid points remain after filtering.
    """
    t = np.asarray(t, dtype=float)
    ratio = np.asarray(ratio, dtype=float)

    mask = (t > 0) & np.isfinite(ratio) & (ratio > 0)
    t_clean = t[mask]
    r_clean = ratio[mask]

    n = int(len(t_clean))
    if n < 3:
        raise ValueError(f"Insufficient data points for fit: {n} (need >= 3)")

    log_t = np.log(t_clean)
    log_r = np.log(r_clean)
    slope, intercept = np.polyfit(log_t, log_r, 1)
    b = float(slope)
    a = float(np.exp(intercept))

    r_pred = a * t_clean ** b
    ss_res = float(np.sum((r_clean - r_pred) ** 2))
    ss_tot = float(np.sum((r_clean - r_clean.mean()) ** 2))
    r_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    # A perfectly flat ratio (log_r constant) leaves the correlation undefined;
    # report it as no linear trend rather than emitting a nan / warning.
    if np.std(log_r) == 0 or np.std(log_t) == 0:
        r_pearson, p_value = 0.0, 1.0
    else:
        r_pearson, p_value = pearsonr(log_t, log_r)

    return SatellizationResult(
        a=round(a, 6),
        b=round(b, 4),
        r_squared=round(r_squared, 4),
        r_pearson=round(float(r_pearson), 4),
        p_value=round(float(p_value), 6),
        regime=classify_regime(b),
        n_observations=n,
    )


def rolling_b(
    ratio: np.ndarray,
    window: int = 30,
) -> list[Optional[float]]:
    """
    Rolling estimate of b over a sliding window on a dominance-ratio series.
    Returns a list aligned to `ratio` (None until the first full window).
    Used to detect regime shifts / leapfrogs as b moves through time.
    """
    ratio = np.asarray(ratio, dtype=float)
    out: list[Optional[float]] = [None] * len(ratio)
    for i in range(window, len(ratio) + 1):
        seg = ratio[i - window:i]
        t = np.arange(1, window + 1, dtype=float)
        try:
            out[i - 1] = fit_satellization(t, seg).b
        except ValueError:
            out[i - 1] = None
    return out
