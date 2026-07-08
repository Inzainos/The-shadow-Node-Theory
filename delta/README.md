# Delta — Crypto & Market Prediction Model

**Status:** core implemented (v0.1) · **Owner:** Elán Zainos Corona / Fractal Core Research

Delta is an **independent** SNT-based signal engine for crypto and equity
markets, built on the Shadow Node Theory satellization law and its
institutional-friction finding. It reuses the SNT correlation logic (ported
self-contained here — no cross-repo dependency), with the **Omega** platform
(Ω(t)) as conceptual precursor.

## Idea

Map each market to an SNT hub/shadow pair and fit the dominance law
`R(t) = a·t^b`:

- **Crypto:** hub = BTC, shadow = altcoin. `b > 0` → BTC season; `b < 0` → alt
  season / leapfrog.
- **Bolsa:** hub = index (S&P 500 / IPC), shadow = a stock. `b > 0` → stock
  being satellized (lagging); `b < 0` → breakout / leapfrog.

The exponent `b` is then compared against the **friction-expected b** for that
market (crypto = LOW friction, expected ≈0.60; bolsa = MEDIUM, ≈0.30). A large
deviation is the tradable **anomaly** — this is the SNT friction thesis
(ρ = −0.68) applied to markets.

## Modules

| File | Role |
|---|---|
| `snt_market_core.py` | Satellization fit `R(t)=a·t^b`, regime classification, rolling-b |
| `market_mapping.py` | Map crypto/bolsa price series → hub/shadow dominance ratio; market friction |
| `delta_engine.py` | Full pipeline → `DeltaSignal` (b, regime, anomaly, leapfrog, direction, confidence) |
| `demo_delta.py` | End-to-end smoke test on synthetic series (crypto + bolsa) |

## Run

```bash
cd delta
python demo_delta.py     # synthetic smoke test
```

Real feeds plug in at `delta_engine.analyze_pair(hub_price, shadow_price, ...)`
by passing aligned real price arrays (exchange / market-data API) instead of the
synthetic demo series.

## Scope & caveats

- Descriptive/decision-support signal, **not financial advice** and not a
  guarantee — `b` describes the direction and speed of dominance, read alongside
  the friction null. Position sizing / risk management are out of scope here.
- Independent of the Omega codebase (own data, pipeline, lifecycle); the SNT
  engine logic is ported here rather than imported.

## Real data

`data_adapters.py` + `run_real_delta.py` fetch **real historical daily closes
with no API key**:

- Crypto → CoinGecko (`/coins/{id}/market_chart`), BTC hub vs top-10 alts.
- Bolsa → Yahoo Finance (`/v8/finance/chart`), S&P 500 (`^GSPC`) + US caps and
  IPC (`^MXX`) + BMV emisoras.

```bash
cd delta
python run_real_delta.py   # writes real_delta_signals.json (23 signals)
```

`real_delta_signals.json` holds the latest run (signals only — no raw prices).

## Roadmap

- [x] Real data adapters (CoinGecko crypto + Yahoo Finance bolsa, no keys).
- [ ] Multi-shadow (N-Body) view: one hub vs a basket of shadows.
- [ ] Backtest harness against historical series.
- [ ] ACO-A collapse layer (Δ) for drawdown/collapse regimes.

Base theory: Shadow Node Theory / ACO-A (see `../papers/`, `../reconstruction_real/`).
Tracked in Asana and Notion.
