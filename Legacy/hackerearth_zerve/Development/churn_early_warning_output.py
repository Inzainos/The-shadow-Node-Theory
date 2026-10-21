import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplo en t as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import os
import warnings
warnings.filterwarnings("ignore")

# ── Zerve Design System ────────────────────────────────────────────────────
_BG   = "#1D1D20"
_TXT  = "#fbfbff"
_SEC  = "#909094"
_GRID = "#2e2e33"
_BLUE = "#A1C9F4"
_ORN  = "#FFB482"
_GRN  = "#8DE5A1"
_CRL  = "#FF9F9B"
_LAV  = "#D0BBFF"
_YEL  = "#ffd400"
_RED  = "#f04438"
_EMR  = "#17b26a"

# ══════════════════════════════════════════════════════════════════════════
# 1. Identify top-15 churn-signal event types by SHAP-proxy score
# ══════════════════════════════════════════════════════════════════════════
# Get top 15 events from churn_event_lift_df sorted by shap_proxy_score
_top15_events = (
    churn_event_lift_df
    .nlargest(15, "shap_proxy_score")["event_type"]
    .tolist()
)
_top15_cols = [f"evt_{e}" for e in _top15_events]

# ── Merge event features with risk tier & churn prob ─────────────────────
_efr = event_features_with_retention.copy()

# Sample up to 200 users per risk tier for heatmap readability
_efr_reset = _efr.reset_index(drop=True)
_efr_reset["user_idx"] = _efr_reset.index

# Get churn probabilities from the classifier for all users
_evt_cols_all  = [c for c in event_feature_matrix.columns
                  if c.startswith("evt_") and not c.endswith("_ratio")]
_ratio_cols_all = [c for c in event_feature_matrix.columns
                   if c.startswith("evt_") and c.endswith("_ratio")]
_seq_cols_ew    = ["seq_event_entropy", "seq_event_velocity"]
_churn_feat_ew  = _evt_cols_all + _ratio_cols_all + _seq_cols_ew

_efm_aligned = event_feature_matrix[_churn_feat_ew].copy()
_efm_aligned[_seq_cols_ew] = _efm_aligned[_seq_cols_ew].fillna(_efm_aligned[_seq_cols_ew].median())
_var_mask_ew = _efm_aligned.std(axis=0) > 0
_X_ew_full   = _efm_aligned.loc[:, _var_mask_ew].values

# Use same scaler from classifier (rebuild with same data — avoid leakage issues)
from sklearn.preprocessing import StandardScaler
_sc_ew = StandardScaler()
_X_ew_sc = _sc_ew.fit_transform(_X_ew_full)
_churn_probs = churn_clf.predict_proba(_X_ew_sc)[:, 1]

_efr_reset["churn_prob"] = _churn_probs
_efr_reset["risk_tier"]  = _efr["risk_tier"].values

# ── Build heatmap: sample up to 60 users per tier (sorted by churn_prob desc)
_tier_order = ["High Risk", "Moderate Risk", "Low Risk", "Likely Retained"]
_heatmap_users = []
for _t in _tier_order:
    _tier_df = _efr_reset[_efr_reset["risk_tier"].astype(str) == _t].nlargest(60, "churn_prob")
    _heatmap_users.append(_tier_df)
_hmap_df = pd.concat(_heatmap_users, ignore_index=True)

# Build event frequency matrix for top-15 events
_hmap_evt = _hmap_df[[c for c in _top15_cols if c in _hmap_df.columns]].copy()

# Normalize each column 0-1 for visualization
_hmap_norm = _hmap_evt.copy()
for _c in _hmap_norm.columns:
    _col_max = _hmap_norm[_c].max()
    if _col_max > 0:
        _hmap_norm[_c] = _hmap_norm[_c] / _col_max

_hmap_labels = [c.replace("evt_", "").replace("_", " ") for c in _hmap_norm.columns]
_hmap_values = _hmap_norm.values  # shape: (n_users, 15)

# Build tier color band for y-axis
_tier_colors_map = {
    "High Risk":       _RED,
    "Moderate Risk":   _ORN,
    "Low Risk":        _YEL,
    "Likely Retained": _EMR,
}
_tier_labels_col = _hmap_df["risk_tier"].astype(str).values

# ── Plot 1: Risk Heatmap ──────────────────────────────────────────────────
_n_users = len(_hmap_values)
_n_events = len(_hmap_labels)

risk_heatmap_fig, (_ax_tier, _ax_heat) = plt.subplots(
    1, 2, figsize=(16, max(8, _n_users * 0.06)),
    gridspec_kw={"width_ratios": [0.03, 1]},
    facecolor=_BG
)
risk_heatmap_fig.patch.set_facecolor(_BG)

# Left band: risk tier color
_tier_band = np.array([
    list(mcolors.to_rgb(_tier_colors_map.get(_tl, _SEC)))
    for _tl in _tier_labels_col
])  # (n_users, 3)
_ax_tier.imshow(_tier_band.reshape(_n_users, 1, 3), aspect="auto")
_ax_tier.set_xticks([])
_ax_tier.set_yticks([])
_ax_tier.set_title("Tier", fontsize=7, color=_SEC, pad=4)
for _sp in _ax_tier.spines.values():
    _sp.set_visible(False)

# Main heatmap
_im = _ax_heat.imshow(
    _hmap_values, aspect="auto", cmap="YlOrRd",
    vmin=0, vmax=1, interpolation="nearest"
)
_ax_heat.set_facecolor(_BG)
_ax_heat.set_xticks(range(_n_events))
_ax_heat.set_xticklabels(_hmap_labels, rotation=45, ha="right", fontsize=7, color=_TXT)
_ax_heat.set_yticks([])
_ax_heat.set_ylabel("Users (sorted by churn risk within tier)", fontsize=9, color=_SEC, labelpad=6)
_ax_heat.set_title(
    "Churn Signal Risk Heatmap — Users × Top 15 Churn-Signal Events\n"
    "(Color = normalized event frequency  |  Left strip = risk tier)",
    fontsize=12, color=_TXT, fontweight="bold", pad=10
)
for _sp in _ax_heat.spines.values():
    _sp.set_edgecolor(_GRID)

# Colorbar
_cbar = risk_heatmap_fig.colorbar(_im, ax=_ax_heat, fraction=0.015, pad=0.01)
_cbar.set_label("Normalized Event Frequency", color=_SEC, fontsize=9)
_cbar.ax.tick_params(colors=_SEC, labelsize=8)
_cbar.outline.set_edgecolor(_GRID)

# Tier legend
_tier_patches = [
    mpatches.Patch(color=_c, label=_t)
    for _t, _c in _tier_colors_map.items()
]
_ax_heat.legend(handles=_tier_patches, loc="upper right", fontsize=8,
                facecolor=_BG, edgecolor=_GRID, labelcolor=_TXT, ncol=2)

plt.tight_layout(pad=1.5)
print("✅ Chart 1: Risk Heatmap rendered")

# ══════════════════════════════════════════════════════════════════════════
# 2. Survival-style chart: event sequence position vs avg churn probability
# ══════════════════════════════════════════════════════════════════════════
# Proxy: use seq_event_velocity as "event sequence position" (total events / days active)
# Bin users by their total event count (seq_event_velocity × dias_activos proxy)
_surv_df = _efr_reset.copy()
_surv_df["total_evt_count"] = _efr["total_eventos"].values if "total_eventos" in _efr.columns else (
    _efr[_evt_cols_all].sum(axis=1).values
)

# Build binned event positions (1-20 bins by total event count)
_surv_df["evt_bin"] = pd.qcut(
    _surv_df["total_evt_count"].clip(lower=1),
    q=20, labels=False, duplicates="drop"
)
_surv_curve = (
    _surv_df.groupby("evt_bin", observed=True)["churn_prob"]
    .agg(["mean", "std", "count"])
    .reset_index()
)
_surv_curve.columns = ["evt_bin", "avg_churn_prob", "std_churn_prob", "n"]

# Map bin index to approximate event count midpoint
_bin_edges = pd.qcut(
    _surv_df["total_evt_count"].clip(lower=1),
    q=20, retbins=True, duplicates="drop"
)[1]
_bin_mids = [(_bin_edges[i] + _bin_edges[i+1]) / 2 for i in range(len(_bin_edges)-1)]
_n_bins = len(_surv_curve)
_x_vals = [_bin_mids[int(b)] for b in _surv_curve["evt_bin"]]
_y_vals = _surv_curve["avg_churn_prob"].values
_y_std  = _surv_curve["std_churn_prob"].values

survival_churn_risk_fig, _ax_surv = plt.subplots(figsize=(13, 6), facecolor=_BG)
survival_churn_risk_fig.patch.set_facecolor(_BG)
_ax_surv.set_facecolor(_BG)

# Gradient color by risk level
_colors_surv = [_EMR if y < 0.5 else (_ORN if y < 0.8 else _RED) for y in _y_vals]

_ax_surv.fill_between(_x_vals, _y_vals - _y_std, _y_vals + _y_std,
                      alpha=0.15, color=_ORN, zorder=1, label="±1 std")
_ax_surv.plot(_x_vals, _y_vals, color=_ORN, lw=2.5, zorder=3, label="Avg Churn Probability")

# Mark the peak spike
_peak_idx = int(np.argmax(_y_vals))
_ax_surv.scatter([_x_vals[_peak_idx]], [_y_vals[_peak_idx]],
                 color=_RED, s=120, zorder=5, label=f"Peak risk @ ~{int(_x_vals[_peak_idx])} events")
_ax_surv.axvline(_x_vals[_peak_idx], color=_RED, lw=1.2, linestyle="--", alpha=0.5, zorder=2)

# Scatter all points
_ax_surv.scatter(_x_vals, _y_vals, c=_colors_surv, s=45, zorder=4, alpha=0.9)

_ax_surv.set_xlabel("Event Sequence Position (Total Events — binned into 20 quantile groups)",
                     fontsize=10, color=_SEC, labelpad=8)
_ax_surv.set_ylabel("Avg Churn Probability", fontsize=10, color=_SEC, labelpad=8)
_ax_surv.set_title(
    "Survival-Style Chart — Where in the Event Journey Does Churn Risk Spike?\n"
    "(Each point = cohort of users at that event-volume stage)",
    fontsize=12, color=_TXT, fontweight="bold", pad=12
)
_ax_surv.tick_params(colors=_SEC, labelsize=9)
for _sp in _ax_surv.spines.values():
    _sp.set_edgecolor(_GRID)
_ax_surv.set_ylim(0, 1.05)
_ax_surv.axhline(0.5, color=_GRID, lw=0.8, linestyle=":", alpha=0.6)
_ax_surv.axhline(0.8, color=_CRL, lw=0.8, linestyle=":", alpha=0.5)

_ax_surv.legend(loc="upper right", fontsize=9, facecolor=_BG, edgecolor=_GRID, labelcolor=_TXT)
plt.tight_layout(pad=1.5)
print(f"✅ Chart 2: Survival-style chart rendered | peak churn spike @ ~{int(_x_vals[_peak_idx])} events")

# ══════════════════════════════════════════════════════════════════════════
# 3. 2×2 Action Matrix
# ══════════════════════════════════════════════════════════════════════════
# High churn risk: churn_prob >= 0.5
# High engagement events: total_evt_count >= median
_med_evt = _surv_df["total_evt_count"].median()
_churn_thresh = 0.5

_surv_df["high_churn"] = _surv_df["churn_prob"] >= _churn_thresh
_surv_df["high_engage"] = _surv_df["total_evt_count"] >= _med_evt

_quad_counts = {
    "Intervene Now":  int((( _surv_df["high_churn"]) & ( _surv_df["high_engage"])).sum()),
    "Re-engage":      int((( _surv_df["high_churn"]) & (~_surv_df["high_engage"])).sum()),
    "Nurture":        int(((~_surv_df["high_churn"]) & ( _surv_df["high_engage"])).sum()),
    "Monitor":        int(((~_surv_df["high_churn"]) & (~_surv_df["high_engage"])).sum()),
}

print(f"\n  2×2 Action Matrix:")
for _k, _v in _quad_counts.items():
    print(f"    {_k:<20} : {_v:,} users")

action_matrix_fig, _ax_mat = plt.subplots(figsize=(10, 8), facecolor=_BG)
action_matrix_fig.patch.set_facecolor(_BG)
_ax_mat.set_facecolor(_BG)

# Draw 4 quadrants
_quad_defs = [
    # (x, y, label, color, description, row, col)
    (0, 1, "Intervene Now",  _RED,  "High churn risk\n+ High engagement\n→ Act immediately",  "High Risk", "High Engage"),
    (1, 1, "Re-engage",      _ORN,  "High churn risk\n+ Low engagement\n→ Win-back campaign", "High Risk", "Low Engage"),
    (0, 0, "Nurture",        _EMR,  "Low churn risk\n+ High engagement\n→ Deepen relationship","Low Risk",  "High Engage"),
    (1, 0, "Monitor",        _BLUE, "Low churn risk\n+ Low engagement\n→ Watch & wait",        "Low Risk",  "Low Engage"),
]

for _x, _y, _name, _clr, _desc, _rlab, _clab in _quad_defs:
    _rect = plt.Rectangle((_x, _y), 1, 1, facecolor=_clr, alpha=0.18, edgecolor=_clr, lw=2)
    _ax_mat.add_patch(_rect)
    _count = _quad_counts[_name]
    _ax_mat.text(_x + 0.5, _y + 0.72, _name, ha="center", va="center",
                 fontsize=16, fontweight="bold", color=_clr)
    _ax_mat.text(_x + 0.5, _y + 0.50, f"{_count:,} users", ha="center", va="center",
                 fontsize=13, color=_TXT, fontweight="bold")
    _ax_mat.text(_x + 0.5, _y + 0.25, _desc, ha="center", va="center",
                 fontsize=9, color=_SEC, linespacing=1.5)

# Axes labels
_ax_mat.set_xlim(0, 2)
_ax_mat.set_ylim(0, 2)
_ax_mat.set_xticks([0.5, 1.5])
_ax_mat.set_xticklabels(["High Engagement", "Low Engagement"], fontsize=12, color=_TXT)
_ax_mat.set_yticks([0.5, 1.5])
_ax_mat.set_yticklabels(["Low Churn Risk", "High Churn Risk"], fontsize=12, color=_TXT)
_ax_mat.set_title(
    "2×2 Churn Action Matrix — Intervention Strategy by Risk & Engagement\n"
    f"(Engagement threshold: ≥{int(_med_evt)} total events  |  Churn threshold: ≥{_churn_thresh:.0%} probability)",
    fontsize=12, color=_TXT, fontweight="bold", pad=14
)
_ax_mat.tick_params(colors=_SEC)
for _sp in _ax_mat.spines.values():
    _sp.set_edgecolor(_GRID)
_ax_mat.axvline(1, color=_GRID, lw=1.5)
_ax_mat.axhline(1, color=_GRID, lw=1.5)

plt.tight_layout(pad=1.5)
print("✅ Chart 3: 2×2 Action Matrix rendered")

# ══════════════════════════════════════════════════════════════════════════
# 4. Build & export churn_early_warning.csv
# ══════════════════════════════════════════════════════════════════════════
# Determine top churn trigger event per user (highest normalized event count among top-15)
_hmap_top15_avail = [c for c in _top15_cols if c in _efr_reset.columns]
_top_trigger = (
    _efr_reset[_hmap_top15_avail]
    .apply(lambda row: row.idxmax() if row.max() > 0 else "none", axis=1)
    .str.replace("evt_", "", regex=False)
)

# Assign recommended action
def _assign_action(row):
    if row["churn_prob"] >= _churn_thresh and row["total_evt_count"] >= _med_evt:
        return "Intervene Now"
    elif row["churn_prob"] >= _churn_thresh and row["total_evt_count"] < _med_evt:
        return "Re-engage"
    elif row["churn_prob"] < _churn_thresh and row["total_evt_count"] >= _med_evt:
        return "Nurture"
    else:
        return "Monitor"

_surv_df["top_churn_trigger"] = _top_trigger.values
_surv_df["recommended_action"] = _surv_df.apply(_assign_action, axis=1)

churn_early_warning_df = _surv_df[[
    "churn_prob", "risk_tier", "top_churn_trigger", "recommended_action"
]].copy()
churn_early_warning_df.columns = [
    "churn_probability", "risk_tier", "top_churn_trigger_event", "recommended_action"
]
churn_early_warning_df["churn_probability"] = churn_early_warning_df["churn_probability"].round(4)

# Save to docu/
os.makedirs("docu", exist_ok=True)
_csv_path = "docu/churn_early_warning.csv"
churn_early_warning_df.to_csv(_csv_path, index=True)

print(f"\n✅ CSV exported: {_csv_path}  ({len(churn_early_warning_df):,} rows)")
print(f"\n  Action distribution:")
print(churn_early_warning_df["recommended_action"].value_counts().to_string())
print(f"\n  Risk tier distribution:")
print(churn_early_warning_df["risk_tier"].value_counts().to_string())
print(f"\n  Top 10 churn trigger events:")
print(churn_early_warning_df["top_churn_trigger_event"].value_counts().head(10).to_string())
print(f"\n{'━'*60}")
print(f"  ✅  3 charts rendered successfully")
print(f"  ✅  CSV: docu/churn_early_warning.csv ({len(churn_early_warning_df):,} users)")
print(f"  ✅  Action matrix counts: {_quad_counts}")
print(f"{'━'*60}")
