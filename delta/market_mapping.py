"""
market_mapping.py — Map market data to SNT hub/shadow dominance (Delta)
=======================================================================
Delta applies SNT satellization to two markets:

  Crypto : hub = BTC (or the exchange's dominant asset), shadow = an altcoin.
           R(t) = price_BTC / price_alt (in a common quote, e.g. USD).
           b < 0 → altcoin gaining (alt season / leapfrog risk)
           b > 0 → BTC gaining dominance (BTC season)

  Bolsa  : hub = index (S&P 500 / IPC), shadow = an individual stock.
           R(t) = index_level / stock_price (rebased).
           b > 0 → stock lagging the index (being satellized)
           b < 0 → stock outperforming (leapfrog / breakout)

Market friction (SNT institutional-friction finding, ρ=−0.68):
  crypto      → LOW    (expected b ≈ 0.60)  — few brakes, fast dominance shifts
  stock_market→ MEDIUM (expected b ≈ 0.30)  — regulated, slower

The friction-expected b is the null hypothesis; a large deviation of the
*observed* b from it is the tradable anomaly (see delta_engine.anomaly_score).
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum

import numpy as np


class FrictionLevel(IntEnum):
    ZERO = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    MAXIMUM = 4


# Friction-expected exponent b per level (SNT v2.5.0; matches Omega friction.py)
B_EXPECTATIONS = {
    FrictionLevel.ZERO: 0.95,
    FrictionLevel.LOW: 0.60,
    FrictionLevel.MEDIUM: 0.30,
    FrictionLevel.HIGH: 0.09,
    FrictionLevel.MAXIMUM: 0.02,
}

# Market → friction level
MARKET_FRICTION = {
    "crypto": FrictionLevel.LOW,
    "stock_market": FrictionLevel.MEDIUM,
}


@dataclass
class DominanceSeries:
    """A hub/shadow dominance ratio series ready for satellization fitting."""
    t: np.ndarray            # 1..n time index (bars since window start)
    ratio: np.ndarray        # hub/shadow dominance ratio
    hub: str
    shadow: str
    market: str              # "crypto" | "stock_market"


def _rebase(x: np.ndarray) -> np.ndarray:
    """Rebase a price series to its first value (avoids scale artifacts)."""
    x = np.asarray(x, dtype=float)
    if x.size == 0 or x[0] == 0:
        return x
    return x / x[0]


def build_dominance(
    hub_price: np.ndarray,
    shadow_price: np.ndarray,
    hub: str,
    shadow: str,
    market: str,
) -> DominanceSeries:
    """
    Build the dominance-ratio series R(t) = hub/shadow from two aligned,
    same-quote price series (e.g. both in USD). Prices are rebased first so
    the ratio starts at 1.0 and b measures relative drift, not level.
    """
    hub_price = np.asarray(hub_price, dtype=float)
    shadow_price = np.asarray(shadow_price, dtype=float)
    if hub_price.shape != shadow_price.shape:
        raise ValueError("hub and shadow price series must be the same length")
    if market not in MARKET_FRICTION:
        raise ValueError(f"unknown market '{market}' (use crypto|stock_market)")

    ratio = _rebase(hub_price) / _rebase(shadow_price)
    t = np.arange(1, len(ratio) + 1, dtype=float)
    return DominanceSeries(t=t, ratio=ratio, hub=hub, shadow=shadow, market=market)


def expected_b(market: str) -> float:
    """Friction-expected exponent b for a market (the null to beat)."""
    return B_EXPECTATIONS[MARKET_FRICTION[market]]
