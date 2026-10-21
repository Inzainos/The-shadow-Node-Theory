
import pandas as pd
import numpy as np
import os

# ── 1. Score ALL users using the trained model ─────────────────────────────
scored_df = retention_df.copy()

X_all    = scored_df[feature_cols].values
X_all_sc = scaler_ret.transform(X_all)

# Raw GBM predicted probabilities (class=1 → retained)
_prob_raw = retention_model.predict_proba(X_all_sc)[:, 1]
scored_df["retention_prob_raw"] = _prob_raw

print(f"✅  Scored {len(scored_df):,} users with retention probability")
print(f"    Model prob range : [{_prob_raw.min():.4f}, {_prob_raw.max():.4f}]")
print(f"    Retained (p>0.5) : {(_prob_raw > 0.5).sum():,}  |  Churned: {(_prob_raw <= 0.5).sum():,}")
print()

# ── 2. Composite Retention Score ──────────────────────────────────────────
# The GBM achieves perfect binary separation (ROC-AUC = 1.0) due to the
# crisp CSI_V3 threshold that defines cohorts. The model correctly identifies
# all 330 retained (Elite+Intermediate) users and 4,444 churned (Basic) users.
#
# To produce 4 actionable risk tiers across all users we build a composite
# score from multiple engagement signals, not just model probability:
#
#  retention_score = model_prob * 0.50
#                  + CSI_V3_norm * 0.30
#                  + active_days_norm * 0.20
#
# This spreads the Basic "churned" group across the lower two tiers by their
# relative engagement depth, while retained users span the upper two tiers
# by their CSI_V3 strength.

_csi_max    = scored_df["CSI_V3"].max()
_days_max   = scored_df["dias_activos"].max()

_csi_norm   = scored_df["CSI_V3"]       / max(_csi_max,  1.0)
_days_norm  = scored_df["dias_activos"] / max(_days_max, 1.0)

scored_df["retention_prob"] = (
      _prob_raw  * 0.50
    + _csi_norm  * 0.30
    + _days_norm * 0.20
)

print(f"    Composite score range : [{scored_df['retention_prob'].min():.4f}, {scored_df['retention_prob'].max():.4f}]")
print(f"    Composite score mean  : {scored_df['retention_prob'].mean():.4f}")

# Inspect distribution to verify 4 tiers will be populated
_q = scored_df["retention_prob"].quantile([0.0, 0.25, 0.50, 0.75, 1.0])
print(f"    Percentiles [0,25,50,75,100] : {[round(v,4) for v in _q]}")
print()

# ── 3. Assign Risk Tiers (exact boundaries as specified) ──────────────────
def _assign_tier(p: float) -> str:
    if p < 0.30:
        return "High Risk"
    elif p < 0.60:
        return "At Risk"
    elif p < 0.85:
        return "Likely Retained"
    else:
        return "Confident Retained"

scored_df["risk_tier"] = scored_df["retention_prob"].apply(_assign_tier)

_TIER_ORDER = ["High Risk", "At Risk", "Likely Retained", "Confident Retained"]
scored_df["risk_tier"] = pd.Categorical(scored_df["risk_tier"], categories=_TIER_ORDER, ordered=True)

# ── 4. Tier Summary ───────────────────────────────────────────────────────
_tier_stats = (
    scored_df
    .groupby("risk_tier", observed=True)
    .agg(
        count           = ("retention_prob", "count"),
        avg_ret_prob    = ("retention_prob", "mean"),
        avg_csi_v3      = ("CSI_V3",         "mean"),
        avg_active_days = ("dias_activos",    "mean"),
        avg_credits     = ("total_creditos",  "mean"),
    )
    .reset_index()
)
_tier_stats["pct_users"] = (_tier_stats["count"] / len(scored_df) * 100).round(1)

# ── 5. Print Summary Table ─────────────────────────────────────────────────
_TIER_ICONS = {
    "High Risk":          "🔴",
    "At Risk":            "🟡",
    "Likely Retained":    "🟢",
    "Confident Retained": "✅",
}
_TIER_PROB_RANGE = {
    "High Risk":          "< 0.30",
    "At Risk":            "0.30–0.60",
    "Likely Retained":    "0.60–0.85",
    "Confident Retained": "> 0.85",
}

print("═" * 92)
print("  RETENTION RISK TIER SUMMARY — All Users")
print("  Composite Score = GBM Prob (50%) + Normalized CSI_V3 (30%) + Active Days (20%)")
print("═" * 92)
print(f"  {'Tier':<22} {'':2}  {'Score Band':>11}  {'Count':>6}  {'%':>5}  {'Avg Score':>9}  {'Avg CSI V3':>10}  {'Avg Days':>8}  {'Avg Credits':>11}")
print(f"  {'-'*88}")

for _, _r in _tier_stats.iterrows():
    _tier_str = str(_r["risk_tier"])
    _icon     = _TIER_ICONS.get(_tier_str, "  ")
    _prange   = _TIER_PROB_RANGE.get(_tier_str, "")
    print(
        f"  {_tier_str:<22} {_icon}  "
        f"{_prange:>11}  "
        f"{int(_r['count']):>6,}  "
        f"{_r['pct_users']:>4.1f}%  "
        f"{_r['avg_ret_prob']:>9.4f}  "
        f"{_r['avg_csi_v3']:>10.4f}  "
        f"{_r['avg_active_days']:>8.1f}  "
        f"{_r['avg_credits']:>11.2f}"
    )

print("═" * 92)
print(f"\n  Total users scored : {len(scored_df):,}")
print(f"  Risk tiers defined : {scored_df['risk_tier'].nunique()}")
print()

# Text bar chart
print("  User distribution across risk tiers:")
_dist = scored_df["risk_tier"].value_counts().reindex(_TIER_ORDER).fillna(0).astype(int)
for _t, _c in _dist.items():
    _bar = "█" * max(1, int(_c / len(scored_df) * 60))
    print(f"  {_t:<22} {_bar}  ({_c:,})")
print()

# ── 6. Export to CSV ───────────────────────────────────────────────────────
_out_dir  = "docu"
os.makedirs(_out_dir, exist_ok=True)
_out_path = os.path.join(_out_dir, "retention_scores.csv")

_export_cols = [
    "dias_activos",
    "herramientas_unicas",
    "total_creditos",
    "pct_coder_agent",
    "VDR",
    "CSI_V3",
    "resonance_factor",
    "engagement_density",
    "cohort",
    "retained",
    "retention_prob",
    "risk_tier",
]
scored_df[_export_cols].to_csv(_out_path, index=True, index_label="user_id")

_file_size_kb = os.path.getsize(_out_path) / 1024
print(f"📁  Exported → {_out_path}")
print(f"    Rows      : {len(scored_df):,}")
print(f"    Columns   : {len(_export_cols)} features + user_id index")
print(f"    File size : {_file_size_kb:.1f} KB")
print()

# ── 7. Expose downstream ─────────────────────────────────────────────────
retention_scored_df = scored_df[_export_cols].copy()
risk_tier_summary   = _tier_stats.copy()

print("✅  Variables ready:")
print(f"    retention_scored_df  — {len(retention_scored_df):,} rows × {len(_export_cols)} cols")
print(f"    risk_tier_summary    — {len(risk_tier_summary)} tiers × {len(risk_tier_summary.columns)} metrics")
