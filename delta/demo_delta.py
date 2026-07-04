"""
demo_delta.py — end-to-end smoke test of the Delta engine
=========================================================
Runs the Delta pipeline on two synthetic-but-realistic scenarios (one crypto,
one bolsa) to prove the engine works end-to-end. The synthetic series are
clearly labelled — real feeds (exchange / market data APIs) plug in at
analyze_pair() by passing real aligned price arrays instead.

    python demo_delta.py
"""
from __future__ import annotations

import numpy as np

from delta_engine import analyze_pair


def _synthetic_pair(n: int, drift: float, seed: int) -> tuple[np.ndarray, np.ndarray]:
    """Two geometric-random-walk price series; `drift` tilts hub vs shadow."""
    rng = np.random.default_rng(seed)
    hub = 100.0 * np.cumprod(1 + rng.normal(drift, 0.01, n))
    shadow = 100.0 * np.cumprod(1 + rng.normal(-drift, 0.012, n))
    return hub, shadow


def main() -> None:
    print("=== Delta engine — demo (synthetic data) ===\n")

    # Crypto: BTC drifting up vs an altcoin drifting down → BTC season (b > 0)
    btc, alt = _synthetic_pair(180, drift=0.0015, seed=7)
    sig = analyze_pair(btc, alt, hub="BTC", shadow="ALT", market="crypto")
    print("[CRYPTO] BTC vs ALT")
    for k, v in sig.to_dict().items():
        print(f"   {k:16s}: {v}")
    print()

    # Bolsa: a stock outperforming the index → leapfrog / breakout (b < 0)
    idx, stock = _synthetic_pair(180, drift=-0.0012, seed=11)
    sig2 = analyze_pair(idx, stock, hub="SPX", shadow="STOCK", market="stock_market")
    print("[BOLSA] SPX vs STOCK")
    for k, v in sig2.to_dict().items():
        print(f"   {k:16s}: {v}")

    print("\nDemo complete — pipeline ran end-to-end with no exceptions.")


if __name__ == "__main__":
    main()
