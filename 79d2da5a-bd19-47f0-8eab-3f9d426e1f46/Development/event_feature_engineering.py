import pandas as pd
import numpy as np
from scipy.stats import entropy as scipy_entropy

# ── 1. Load raw event data ────────────────────────────────────────────────
print("📂 Loading zerve_hackathon_dataset.csv ...")
_raw = pd.read_csv("zerve_hackathon_dataset.csv")
_raw["timestamp"] = pd.to_datetime(_raw["timestamp"], format="mixed", utc=True)
print(f"   Raw rows: {len(_raw):,}  |  Users: {_raw['person_id'].nunique():,}  |  Events: {_raw['event'].nunique()}")
print(f"   Unique event types: {sorted(_raw['event'].unique())}\n")

# ── 2. Pivot event-type counts per user ────────────────────────────────────
_event_counts = (
    _raw.groupby(["person_id", "event"])
    .size()
    .unstack(fill_value=0)
)
_event_counts.columns = [f"evt_{c}" for c in _event_counts.columns]

# Ratio features (proportion of each event type relative to total events)
_total_events = _event_counts.sum(axis=1)
_event_ratios = _event_counts.div(_total_events, axis=0)
_event_ratios.columns = [f"{c}_ratio" for c in _event_counts.columns]

print(f"✅ Pivoted {len(_event_counts.columns)} event-count cols + {len(_event_ratios.columns)} ratio cols")

# ── 3. Event sequence metrics ──────────────────────────────────────────────
_sorted = _raw.sort_values(["person_id", "timestamp"])

# First & last event type per user
_first_event = _sorted.groupby("person_id")["event"].first().rename("seq_first_event")
_last_event  = _sorted.groupby("person_id")["event"].last().rename("seq_last_event")

# Time Between First and Second event (T2ST proxy) — in seconds
def _t2st(group):
    _ts = group["timestamp"].values
    if len(_ts) < 2:
        return np.nan
    return (_ts[1] - _ts[0]) / np.timedelta64(1, "s")

_t2st_s = _sorted.groupby("person_id").apply(_t2st, include_groups=False).rename("seq_t2st_seconds")

# Event entropy — diversity of event distribution per user
def _event_entropy(group):
    _counts_arr = group["event"].value_counts().values.astype(float)
    _probs = _counts_arr / _counts_arr.sum()
    return float(scipy_entropy(_probs, base=2))

_entropy = _sorted.groupby("person_id").apply(_event_entropy, include_groups=False).rename("seq_event_entropy")

# Event velocity — events per active day
_velocity_stats = _sorted.groupby("person_id").agg(
    _total_ev=("event", "count"),
    _active_days=("timestamp", lambda x: x.dt.date.nunique()),
)
_velocity = (_velocity_stats["_total_ev"] / _velocity_stats["_active_days"].clip(lower=1)).rename("seq_event_velocity")

# Assemble sequence feature frame
_seq_features = pd.concat(
    [_first_event, _last_event, _t2st_s, _entropy, _velocity],
    axis=1,
)
print(f"✅ Sequence features: {list(_seq_features.columns)}")

# ── 4. Churn signal per event type ────────────────────────────────────────
# Map each user → risk_tier from retention_scored_df
_tier_map = retention_scored_df["risk_tier"].astype(str)

# Users with High Risk and Confident Retained labels
_hr_users = set(_tier_map[_tier_map == "High Risk"].index)
_cr_users = set(_tier_map[_tier_map == "Confident Retained"].index)

_event_types = _raw["event"].unique()
_churn_signal_rows = []

for _evt in _event_types:
    _users_with_evt = set(_raw[_raw["event"] == _evt]["person_id"].unique())
    _n = len(_users_with_evt)
    if _n == 0:
        continue
    _n_hr = len(_users_with_evt & _hr_users)
    _n_cr = len(_users_with_evt & _cr_users)
    _pct_hr = _n_hr / _n * 100
    _pct_cr = _n_cr / _n * 100
    _churn_signal_rows.append({
        "event_type": _evt,
        "n_users": _n,
        "pct_high_risk": _pct_hr,
        "pct_confident_retained": _pct_cr,
        "churn_signal_score": _pct_hr,        # higher = stronger churn signal
        "retention_signal_score": _pct_cr,    # higher = stronger retention signal
    })

event_churn_signals = pd.DataFrame(_churn_signal_rows).set_index("event_type").sort_values("churn_signal_score", ascending=False)

# ── 5. Merge everything → per-user event feature matrix ───────────────────
event_feature_matrix = (
    _event_counts
    .join(_event_ratios, how="left")
    .join(_seq_features, how="left")
)

# Merge with retention_scored_df
event_features_with_retention = event_feature_matrix.join(
    retention_scored_df[["dias_activos", "herramientas_unicas", "total_creditos",
                          "pct_coder_agent", "VDR", "CSI_V3", "cohort",
                          "retention_prob", "risk_tier"]],
    how="left",
)

print(f"\n✅ event_feature_matrix       : {event_feature_matrix.shape[0]:,} users × {event_feature_matrix.shape[1]} features")
print(f"✅ event_features_with_retention : {event_features_with_retention.shape[0]:,} users × {event_features_with_retention.shape[1]} features")
print(f"✅ event_churn_signals         : {len(event_churn_signals)} event types tracked\n")

# ── 6. Print top 10 churn-signal events ───────────────────────────────────
print("═" * 72)
print("  🔴  TOP 10 CHURN-SIGNAL EVENTS  (highest % of users → High Risk)")
print("═" * 72)
print(f"  {'Event Type':<35} {'N Users':>8}  {'% High Risk':>11}  {'% Conf. Retained':>17}")
print(f"  {'-'*68}")
for _evt_name, _row in event_churn_signals.head(10).iterrows():
    print(
        f"  {str(_evt_name):<35}  "
        f"{int(_row['n_users']):>7,}  "
        f"{_row['pct_high_risk']:>10.1f}%  "
        f"{_row['pct_confident_retained']:>16.1f}%"
    )
print()

# ── 7. Print top 10 retention-signal events ───────────────────────────────
_ret_ranked = event_churn_signals.sort_values("retention_signal_score", ascending=False)

print("═" * 72)
print("  ✅  TOP 10 RETENTION-SIGNAL EVENTS  (highest % → Confident Retained)")
print("═" * 72)
print(f"  {'Event Type':<35} {'N Users':>8}  {'% Conf. Retained':>17}  {'% High Risk':>11}")
print(f"  {'-'*68}")
for _evt_name, _row in _ret_ranked.head(10).iterrows():
    print(
        f"  {str(_evt_name):<35}  "
        f"{int(_row['n_users']):>7,}  "
        f"{_row['pct_confident_retained']:>16.1f}%  "
        f"{_row['pct_high_risk']:>10.1f}%"
    )
print()

print("━" * 72)
print(f"  event_feature_matrix shape       : {event_feature_matrix.shape}")
print(f"  event_features_with_retention shape : {event_features_with_retention.shape}")
print(f"  NaN in merged matrix (t2st only) : seq_t2st_seconds NaNs = "
      f"{event_features_with_retention['seq_t2st_seconds'].isna().sum():,} "
      f"(users with only 1 event)")
print("━" * 72)
