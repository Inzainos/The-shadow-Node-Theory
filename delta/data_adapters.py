"""
data_adapters.py — real market-data adapters for Delta
======================================================
Fetches real historical daily closes with no API key required:

  Crypto : CoinGecko  /coins/{id}/market_chart   (USD daily prices)
  Bolsa  : Yahoo Finance /v8/finance/chart/{sym}  (daily closes)

Both return {symbol -> np.ndarray of closes}. Pairs are analyzed *within* a
market so trading calendars align; series are aligned by trailing common length
before fitting (see align_pair).

No credentials are stored or required. Network only; nothing is written here.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

import numpy as np

_UA = {"User-Agent": "Mozilla/5.0 (Delta/0.1; SNT research)"}

# CoinGecko ids: BTC hub + top-10 non-stablecoin alts
CRYPTO_HUB = "bitcoin"
CRYPTO_SHADOWS = [
    "ethereum", "ripple", "binancecoin", "solana", "dogecoin",
    "cardano", "tron", "chainlink", "avalanche-2", "polkadot",
]

# Bolsa: index hub + shadow tickers (Yahoo symbols)
US_HUB = "^GSPC"
US_SHADOWS = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA"]
MX_HUB = "^MXX"
MX_SHADOWS = ["AMXB.MX", "WALMEX.MX", "GFNORTEO.MX", "FEMSAUBD.MX",
              "GMEXICOB.MX", "CEMEXCPO.MX"]


def _get(url: str, timeout: int = 30, retries: int = 4) -> bytes:
    """GET with retry/backoff on HTTP 429 (rate limit), honoring Retry-After."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=_UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt < retries - 1:
                wait = int(exc.headers.get("Retry-After", 0) or 0) or (10 * (attempt + 1))
                time.sleep(wait)
                continue
            raise
    raise RuntimeError("unreachable")


def fetch_crypto(coin_id: str, days: int = 180) -> np.ndarray:
    """Daily USD closes for a CoinGecko coin id over the last `days`."""
    url = (f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
           f"?vs_currency=usd&days={days}&interval=daily")
    data = json.loads(_get(url))
    prices = [p[1] for p in data.get("prices", []) if p and p[1] is not None]
    return np.asarray(prices, dtype=float)


def fetch_yahoo(symbol: str, rng: str = "6mo") -> np.ndarray:
    """Daily closes for a Yahoo Finance symbol (nulls dropped)."""
    sym = urllib.parse.quote(symbol)
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
           f"?interval=1d&range={rng}")
    data = json.loads(_get(url))
    result = data["chart"]["result"][0]
    closes = result["indicators"]["quote"][0]["close"]
    vals = [c for c in closes if c is not None]
    return np.asarray(vals, dtype=float)


def align_pair(hub: np.ndarray, shadow: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Trim two series to their common trailing length."""
    n = min(len(hub), len(shadow))
    if n == 0:
        return hub, shadow
    return hub[-n:], shadow[-n:]


def fetch_crypto_universe(days: int = 180, pause: float = 6.0) -> dict[str, np.ndarray]:
    """Fetch BTC hub + all alt shadows. Small pause between calls (rate limits)."""
    out: dict[str, np.ndarray] = {}
    for cid in [CRYPTO_HUB] + CRYPTO_SHADOWS:
        try:
            out[cid] = fetch_crypto(cid, days)
        except Exception as exc:  # noqa: BLE001 — one bad symbol shouldn't kill the run
            print(f"[warn] crypto fetch failed for {cid}: {exc}")
        time.sleep(pause)
    return out


def fetch_bolsa_universe(hub: str, shadows: list[str], rng: str = "6mo",
                         pause: float = 0.5) -> dict[str, np.ndarray]:
    """Fetch one index hub + its shadow tickers from Yahoo."""
    out: dict[str, np.ndarray] = {}
    for sym in [hub] + shadows:
        try:
            out[sym] = fetch_yahoo(sym, rng)
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] yahoo fetch failed for {sym}: {exc}")
        time.sleep(pause)
    return out
