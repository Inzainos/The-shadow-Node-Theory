import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings("ignore")

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import permutation_importance

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

# ── 1. Build feature matrix — event-type features ONLY ────────────────────
_evt_cols   = [c for c in event_feature_matrix.columns
               if c.startswith("evt_") and not c.endswith("_ratio")]
_ratio_cols = [c for c in event_feature_matrix.columns
               if c.startswith("evt_") and c.endswith("_ratio")]
_seq_cols   = ["seq_event_entropy", "seq_event_velocity"]  # raw behavioral sequence signals

_churn_feature_cols = _evt_cols + _ratio_cols + _seq_cols

_labeled = event_feature_matrix[_churn_feature_cols].join(
    event_features_with_retention[["risk_tier"]], how="inner"
)
_labeled = _labeled.dropna(subset=["risk_tier"])

# Churn label: High Risk = 1, else = 0
_labeled["churn_label"] = (_labeled["risk_tier"].astype(str) == "High Risk").astype(int)
_labeled[_seq_cols] = _labeled[_seq_cols].fillna(_labeled[_seq_cols].median())

print(f"✅ Feature matrix: {_labeled.shape[0]:,} users × {len(_churn_feature_cols)} event features")
print(f"   Churn (High Risk) : {_labeled['churn_label'].sum():,} ({_labeled['churn_label'].mean()*100:.1f}%)")
print(f"   Retained (other)  : {(1-_labeled['churn_label']).sum():,} ({(1-_labeled['churn_label']).mean()*100:.1f}%)\n")

# ── 2. Drop zero-variance features ────────────────────────────────────────
_X_raw = _labeled[_churn_feature_cols].values
_y     = _labeled["churn_label"].values
_var_mask = _X_raw.std(axis=0) > 0
_X     = _X_raw[:, _var_mask]
_active_feat = [f for f, keep in zip(_churn_feature_cols, _var_mask) if keep]
print(f"✅ Non-zero variance features: {len(_active_feat)} (dropped {_var_mask.size - _var_mask.sum()})\n")

# ── 3. Train/Test Split + GradientBoostingClassifier ──────────────────────
_X_tr, _X_te, _y_tr, _y_te = train_test_split(
    _X, _y, test_size=0.2, random_state=42, stratify=_y
)

_sc = StandardScaler()
_X_tr_sc = _sc.fit_transform(_X_tr)
_X_te_sc  = _sc.transform(_X_te)

# Balance classes
_churn_weight = (1 - _y_tr.mean()) / max(_y_tr.mean(), 1e-9)
_sw = np.where(_y_tr == 1, _churn_weight, 1.0)

churn_clf = GradientBoostingClassifier(
    n_estimators=300, max_depth=4, learning_rate=0.05,
    subsample=0.8, min_samples_leaf=10, random_state=42
)
churn_clf.fit(_X_tr_sc, _y_tr, sample_weight=_sw)

# ── 4. Evaluate ────────────────────────────────────────────────────────────
_y_prob_te = churn_clf.predict_proba(_X_te_sc)[:, 1]
churn_event_roc_auc = roc_auc_score(_y_te, _y_prob_te)

_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
_cv_scores = cross_val_score(churn_clf, _X_tr_sc, _y_tr, cv=_cv, scoring="roc_auc")

print(f"{'═'*60}")
print(f"  🎯  CHURN EVENT CLASSIFIER — PERFORMANCE")
print(f"{'═'*60}")
print(f"  Test ROC-AUC        : {churn_event_roc_auc:.4f}")
print(f"  CV ROC-AUC (5-fold) : {_cv_scores.mean():.4f} ± {_cv_scores.std():.4f}")
print(f"  {'✅ PASS' if churn_event_roc_auc >= 0.80 else '⚠️  BELOW 0.80'} — target ≥ 0.80\n")

# ── 5. Feature importance + direction via permutation importance ───────────
print("⚙️  Computing feature importance + direction ...")

# GBM native importance (mean decrease in impurity, scaled)
_native_imp = churn_clf.feature_importances_  # shape: (n_features,)

# Determine SHAP-like direction: compare mean predicted churn prob
# when feature > median vs when feature ≤ median
_X_all_sc = _sc.transform(_X)
_probs_all = churn_clf.predict_proba(_X_all_sc)[:, 1]  # baseline probs

_directions = np.zeros(len(_active_feat))
for _i, _fn in enumerate(_active_feat):
    _med = np.median(_X_all_sc[:, _i])
    _high_mask = _X_all_sc[:, _i] > _med
    _low_mask  = ~_high_mask
    _mean_hi   = _probs_all[_high_mask].mean() if _high_mask.sum() > 0 else 0.5
    _mean_lo   = _probs_all[_low_mask].mean()  if _low_mask.sum()  > 0 else 0.5
    _directions[_i] = _mean_hi - _mean_lo  # positive = high feature value → higher churn

# Combined "SHAP-proxy" score: native importance weighted by abs(direction)
_shap_proxy = _native_imp * (1 + np.abs(_directions))
_ranked_idx = np.argsort(_shap_proxy)[::-1]

_top_n = 20
_top_idx    = _ranked_idx[:_top_n]
_top_feats  = [_active_feat[i] for i in _top_idx]
_top_imp    = _shap_proxy[_top_idx]
_top_dirs   = _directions[_top_idx]

def _clean_label(f):
    return (f.replace("evt_", "").replace("_ratio", " (ratio)").replace("seq_", "").replace("_", " "))

_top_labels = [_clean_label(f) for f in _top_feats]
print(f"✅ Feature importance computed. Top feature: '{_top_feats[0]}'  |  score = {_top_imp[0]:.5f}\n")

# ── 6. SHAP Summary Bar Chart ──────────────────────────────────────────────
fig_shap_bar, _ax_bar = plt.subplots(figsize=(11, 8))
fig_shap_bar.patch.set_facecolor(_BG)
_ax_bar.set_facecolor(_BG)

_bar_colors = [_RED if d >= 0 else _EMR for d in _top_dirs]

_ax_bar.barh(
    range(_top_n - 1, -1, -1),
    _top_imp[::-1],
    color=list(reversed(_bar_colors)),
    edgecolor="none", height=0.72, alpha=0.9
)

_ax_bar.set_yticks(range(_top_n))
_ax_bar.set_yticklabels(list(reversed(_top_labels)), fontsize=9, color=_TXT)
_ax_bar.set_xlabel("Feature Importance (SHAP-proxy)  →  Impact on Churn Prediction",
                   fontsize=10, color=_SEC, labelpad=8)
_ax_bar.set_title("Churn Early Warning — Top 20 Event-Type Predictors\n(Raw Behavioral Signals Only — No CSI_V3, No Derived Scores)",
                  fontsize=13, color=_TXT, fontweight="bold", pad=14)
_ax_bar.tick_params(colors=_SEC, labelsize=9)
for _sp in _ax_bar.spines.values():
    _sp.set_visible(False)
_ax_bar.tick_params(axis='x', colors=_SEC)
_ax_bar.axvline(0, color=_GRID, lw=0.8)

_patch_churn = mpatches.Patch(color=_RED, label="↑ Churn signal (high freq → higher churn risk)")
_patch_ret   = mpatches.Patch(color=_EMR, label="↑ Retention signal (high freq → lower churn risk)")
_ax_bar.legend(handles=[_patch_churn, _patch_ret], loc="lower right", fontsize=9,
               facecolor=_BG, edgecolor=_GRID, labelcolor=_TXT)

plt.tight_layout(pad=1.5)
print("✅ SHAP summary bar chart rendered")

# ── 7. Beeswarm / Dot Plot (event impact direction) ───────────────────────
fig_shap_dot, _ax_dot = plt.subplots(figsize=(12, 9))
fig_shap_dot.patch.set_facecolor(_BG)
_ax_dot.set_facecolor(_BG)

_rng = np.random.default_rng(42)
_samp_idx = _rng.choice(len(_X_all_sc), min(1200, len(_X_all_sc)), replace=False)

for _i, (_fi, _fdir) in enumerate(zip(_top_feats, _top_dirs)):
    _col_idx  = _active_feat.index(_fi)
    _fv       = _X_all_sc[_samp_idx, _col_idx]
    _prob_samp = _probs_all[_samp_idx]

    # X-axis: deviation of probability from mean (effect magnitude + direction)
    _baseline_p = _probs_all.mean()
    _effect_x   = _prob_samp - _baseline_p

    _jitter  = _rng.uniform(-0.25, 0.25, len(_samp_idx))
    _y_pos   = (_top_n - 1 - _i) + _jitter

    # Color by feature value magnitude
    _fv_norm = (_fv - _fv.min()) / (max(_fv.max() - _fv.min(), 1e-9))
    _dot_colors = plt.cm.RdYlGn_r(_fv_norm)
    _ax_dot.scatter(_effect_x, _y_pos, c=_dot_colors, s=6, alpha=0.5, linewidths=0)

_ax_dot.axvline(0, color=_GRID, lw=1.2, zorder=2)
_ax_dot.set_yticks(range(_top_n))
_ax_dot.set_yticklabels(list(reversed(_top_labels)), fontsize=9, color=_TXT)
_ax_dot.set_xlabel("Predicted Churn Probability — Mean  (→ right = higher churn risk, ← left = retention signal)",
                   fontsize=9, color=_SEC, labelpad=8)
_ax_dot.set_title("Churn Event Impact Direction — Beeswarm Plot\n(Red dots = high event frequency  |  Green dots = low event frequency)",
                  fontsize=13, color=_TXT, fontweight="bold", pad=14)
_ax_dot.tick_params(colors=_SEC, labelsize=9)
for _sp in _ax_dot.spines.values():
    _sp.set_visible(False)
_ax_dot.tick_params(axis='x', colors=_SEC)

_sm = plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn_r, norm=plt.Normalize(0, 1))
_sm.set_array([])
_cbar = fig_shap_dot.colorbar(_sm, ax=_ax_dot, pad=0.01, fraction=0.02, aspect=30)
_cbar.set_label("Feature Value (scaled: 0=low, 1=high)", color=_SEC, fontsize=9)
_cbar.ax.tick_params(colors=_SEC, labelsize=8)
_cbar.outline.set_edgecolor(_GRID)

plt.tight_layout(pad=1.5)
print("✅ SHAP beeswarm plot rendered\n")

# ── 8. Per-event-type churn lift ───────────────────────────────────────────
_base_churn_rate = _y.mean()
_feat_df = pd.DataFrame(_X, columns=_active_feat)
_feat_df["churn_label"] = _y

_lift_rows = []
_evt_only_feats = [f for f in _active_feat if f.startswith("evt_") and not f.endswith("_ratio")]

for _fn in _evt_only_feats:
    _mask_with = _feat_df[_fn] > 0
    _n_with    = _mask_with.sum()
    if _n_with < 5:
        continue
    _cr_with = _feat_df.loc[_mask_with, "churn_label"].mean()
    _lift    = _cr_with / max(_base_churn_rate, 1e-9)

    _churned_mask  = _feat_df["churn_label"] == 1
    _retained_mask = _feat_df["churn_label"] == 0
    _avg_churned   = _feat_df.loc[_churned_mask, _fn].mean()
    _avg_retained  = _feat_df.loc[_retained_mask, _fn].mean()

    _fi_idx   = _active_feat.index(_fn)
    _fi_score = float(_shap_proxy[_fi_idx])
    _fi_dir   = float(_directions[_fi_idx])

    _lift_rows.append({
        "event_type":               _fn.replace("evt_", ""),
        "churn_lift":               round(_lift, 3),
        "churn_rate_with_event":    round(_cr_with * 100, 1),
        "avg_occurrences_churned":  round(_avg_churned, 2),
        "avg_occurrences_retained": round(_avg_retained, 2),
        "shap_proxy_score":         round(_fi_score, 5),
        "direction":                "churn" if _fi_dir >= 0 else "retention",
        "n_users_with_event":       int(_n_with),
    })

churn_event_lift_df = pd.DataFrame(_lift_rows).sort_values("churn_lift", ascending=False)

# ── 9. Print early warning table ──────────────────────────────────────────
print("═" * 92)
print("  🚨  CHURN EARLY WARNING TABLE — Ranked by Churn Lift")
print(f"  Base churn rate: {_base_churn_rate*100:.1f}%  |  Lift = P(churn|event) / P(churn overall)")
print("═" * 92)
_hdr = f"  {'Event Type':<38} {'Lift':>6}  {'Churn%':>7}  {'Avg/Churned':>11}  {'Avg/Retained':>13}  {'Score':>8}"
print(_hdr)
print(f"  {'-'*87}")
for _, _r in churn_event_lift_df.head(25).iterrows():
    _icon = "🔴" if _r["churn_lift"] > 1.3 else ("🟡" if _r["churn_lift"] > 1.0 else "🟢")
    print(
        f"  {_icon} {str(_r['event_type']):<36} "
        f"{_r['churn_lift']:>6.2f}x  "
        f"{_r['churn_rate_with_event']:>6.1f}%  "
        f"{_r['avg_occurrences_churned']:>11.2f}  "
        f"{_r['avg_occurrences_retained']:>13.2f}  "
        f"{_r['shap_proxy_score']:>8.5f}"
    )

print()
print("── TOP 10 RETENTION SIGNALS (lowest churn lift = protective) ──")
print(_hdr)
print(f"  {'-'*87}")
for _, _r in churn_event_lift_df.nsmallest(10, "churn_lift").iterrows():
    print(
        f"  🟢 {str(_r['event_type']):<36} "
        f"{_r['churn_lift']:>6.2f}x  "
        f"{_r['churn_rate_with_event']:>6.1f}%  "
        f"{_r['avg_occurrences_churned']:>11.2f}  "
        f"{_r['avg_occurrences_retained']:>13.2f}  "
        f"{_r['shap_proxy_score']:>8.5f}"
    )

print(f"\n{'━'*60}")
print(f"  ✅  churn_event_roc_auc   = {churn_event_roc_auc:.4f}")
print(f"  ✅  CV AUC (5-fold)       = {_cv_scores.mean():.4f} ± {_cv_scores.std():.4f}")
print(f"  ✅  Feature count         = {len(_active_feat)}")
print(f"  ✅  Churn lift table rows = {len(churn_event_lift_df)}")
print(f"{'━'*60}")
