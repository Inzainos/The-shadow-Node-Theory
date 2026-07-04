"""
delta_engine.py — Delta prediction engine (crypto & bolsa)
==========================================================
Independent SNT-based signal engine. Given aligned hub/shadow price series for
a market pair, it:

  1. builds the dominance ratio R(t) = hub/shadow (market_mapping),
  2. fits R(t) = a·t^b (snt_market_core),
  3. compares observed b against the friction-expected b for that market,
  4. tracks the rolling b to flag regime shifts / leapfrogs,
  5. emits a directional signal with a confidence proportional to fit quality
     and to how far b sits from the friction null.

This is a descriptive/decision-support signal, NOT financial advice and NOT a
guarantee — b describes the *direction and speed* of dominance, interpreted
alongside the SNT friction thesis (ρ=−0.68). Position sizing / risk management
are out of scope here.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Optional

import numpy as np

from market_mapping import DominanceSeries, build_dominance, expected_b
from snt_market_core import (
    DominanceRegime,
    SatellizationResult,
    fit_satellization,
    rolling_b,
)


@dataclass
class DeltaSignal:
    market: str
    hub: str
    shadow: str
    b: float
    regime: str
    r_squared: float
    p_value: float
    expected_b: float
    anomaly_score: float          # |b - expected_b| / expected_b
    leapfrog: bool                # rolling b crossed from + to strongly -
    direction: str                # "hub_dominates" | "shadow_leapfrog" | "balanced"
    confidence: float             # 0..1
    n_observations: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _anomaly_score(observed_b: float, exp_b: float) -> float:
    return abs(observed_b - exp_b) / max(exp_b, 0.01)


def _detect_leapfrog(bhist: list[Optional[float]]) -> bool:
    """A leapfrog: b was clearly positive earlier and turned clearly negative."""
    vals = [x for x in bhist if x is not None]
    if len(vals) < 4:
        return False
    early = np.nanmean(vals[: len(vals) // 2])
    late = np.nanmean(vals[len(vals) // 2:])
    return bool(early > 0.1 and late < -0.1)


def _direction(b: float, leapfrog: bool) -> str:
    if leapfrog or b <= -0.1:
        return "shadow_leapfrog"
    if b > 0.05:
        return "hub_dominates"
    return "balanced"


def _confidence(fit: SatellizationResult, anomaly: float) -> float:
    """Confidence grows with fit quality (R², significance) and anomaly size."""
    sig = 1.0 if fit.p_value < 0.05 else 0.5
    anomaly_term = min(anomaly, 1.0)
    conf = 0.5 * max(fit.r_squared, 0.0) + 0.3 * anomaly_term + 0.2 * sig
    return round(min(max(conf, 0.0), 1.0), 3)


def analyze_pair(
    hub_price: np.ndarray,
    shadow_price: np.ndarray,
    hub: str,
    shadow: str,
    market: str,
    rolling_window: int = 30,
) -> DeltaSignal:
    """Run the full Delta pipeline on one hub/shadow pair and emit a signal."""
    dom: DominanceSeries = build_dominance(hub_price, shadow_price, hub, shadow, market)
    fit = fit_satellization(dom.t, dom.ratio)
    exp_b = expected_b(market)
    anomaly = _anomaly_score(fit.b, exp_b)

    bhist = rolling_b(dom.ratio, window=min(rolling_window, max(3, len(dom.ratio) // 2)))
    leapfrog = _detect_leapfrog(bhist)

    return DeltaSignal(
        market=market,
        hub=hub,
        shadow=shadow,
        b=fit.b,
        regime=fit.regime.value if isinstance(fit.regime, DominanceRegime) else str(fit.regime),
        r_squared=fit.r_squared,
        p_value=fit.p_value,
        expected_b=round(exp_b, 4),
        anomaly_score=round(anomaly, 4),
        leapfrog=leapfrog,
        direction=_direction(fit.b, leapfrog),
        confidence=_confidence(fit, anomaly),
        n_observations=fit.n_observations,
    )
