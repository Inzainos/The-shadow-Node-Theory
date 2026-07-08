"""
run_real_delta.py — Delta on real market data
==============================================
Fetches real historical daily closes (CoinGecko + Yahoo Finance, no keys) and
runs the Delta engine on:

  Crypto : BTC (hub) vs top-10 altcoins (shadows)
  Bolsa  : S&P 500 (^GSPC) vs US large caps, and IPC (^MXX) vs BMV emisoras

Emits a DeltaSignal per pair and writes an aggregate summary (signals only —
no raw prices are stored). Descriptive signal, NOT financial advice.

    python run_real_delta.py
"""
from __future__ import annotations

import json
from pathlib import Path

from data_adapters import (
    CRYPTO_HUB, CRYPTO_SHADOWS, US_HUB, US_SHADOWS, MX_HUB, MX_SHADOWS,
    align_pair, fetch_bolsa_universe, fetch_crypto_universe,
)
from delta_engine import analyze_pair

HERE = Path(__file__).parent.resolve()
MIN_POINTS = 20


def _signals_for_market(prices: dict, hub: str, shadows: list[str], market: str,
                        hub_label: str) -> list[dict]:
    out = []
    hub_series = prices.get(hub)
    if hub_series is None or len(hub_series) < MIN_POINTS:
        print(f"[skip] no usable hub series for {hub}")
        return out
    for sh in shadows:
        s = prices.get(sh)
        if s is None or len(s) < MIN_POINTS:
            print(f"[skip] {sh}: insufficient data")
            continue
        h_al, s_al = align_pair(hub_series, s)
        try:
            sig = analyze_pair(h_al, s_al, hub=hub_label, shadow=sh, market=market)
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] analyze failed for {sh}: {exc}")
            continue
        out.append(sig.to_dict())
        print(f"  {market:12s} {hub_label:5s}->{sh:12s} "
              f"b={sig.b:+.3f} {sig.regime:22s} dir={sig.direction:16s} "
              f"conf={sig.confidence}")
    return out


def main() -> None:
    summary: dict[str, list] = {}

    print("=== CRYPTO (BTC hub vs top-10 alts) — CoinGecko ===")
    crypto = fetch_crypto_universe(days=180)
    summary["crypto"] = _signals_for_market(crypto, CRYPTO_HUB, CRYPTO_SHADOWS,
                                            "crypto", "BTC")

    print("\n=== BOLSA US (S&P 500 vs large caps) — Yahoo ===")
    us = fetch_bolsa_universe(US_HUB, US_SHADOWS)
    summary["bolsa_us"] = _signals_for_market(us, US_HUB, US_SHADOWS,
                                             "stock_market", "SPX")

    print("\n=== BOLSA MX (IPC vs BMV) — Yahoo ===")
    mx = fetch_bolsa_universe(MX_HUB, MX_SHADOWS)
    summary["bolsa_mx"] = _signals_for_market(mx, MX_HUB, MX_SHADOWS,
                                             "stock_market", "IPC")

    out = HERE / "real_delta_signals.json"
    out.write_text(json.dumps(summary, indent=2))
    n = sum(len(v) for v in summary.values())
    print(f"\nDone: {n} real-data signals written to {out.name} "
          f"(crypto={len(summary['crypto'])}, "
          f"us={len(summary['bolsa_us'])}, mx={len(summary['bolsa_mx'])}).")


if __name__ == "__main__":
    main()
