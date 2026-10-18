
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    roc_auc_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)
from sklearn.utils.class_weight import compute_sample_weight

# ── Zerve Design System ────────────────────────────────────────────────────
BG_COLOR    = "#1D1D20"
TEXT_PRI    = "#fbfbff"
TEXT_SEC    = "#909094"
GRID_COL    = "#2e2e33"
C_BLUE      = "#A1C9F4"
C_ORANGE    = "#FFB482"
C_GREEN     = "#8DE5A1"
C_CORAL     = "#FF9F9B"
C_LAVENDER  = "#D0BBFF"
C_HIGHLIGHT = "#ffd400"
C_SUCCESS   = "#17b26a"
C_WARN      = "#f04438"

# ── 1. Feature Engineering ─────────────────────────────────────────────────
retention_df = cohort_df.copy()

# Features: dias_activos, herramientas_unicas, total_creditos,
#           pct_coder_agent, VDR, resonancia (as int), CSI_V3
feature_cols = [
    "dias_activos",       # active_days
    "herramientas_unicas",# tool_diversity
    "total_creditos",     # credits_used
    "pct_coder_agent",    # coder_agent_pct
    "VDR",                # value delivery rate
    "CSI_V3",             # composite score
]

# resonancia = resonance_factor → bool to int
retention_df["resonance_factor"] = retention_df["resonancia"].astype(int)
feature_cols.append("resonance_factor")

# Derived feature: engagement density = active days / lifetime
retention_df["engagement_density"] = (
    retention_df["dias_activos"] / (retention_df["vida_util_dias"].clip(lower=1))
)
feature_cols.append("engagement_density")

# ── 2. Retention Label: Elite + Intermediate = 1 (retained), Basic = 0 ────
retention_df["retained"] = (retention_df["cohort"] != "Basic").astype(int)

label_counts = retention_df["retained"].value_counts()
print("═" * 60)
print("  RETENTION LABEL DISTRIBUTION")
print("═" * 60)
print(f"  Retained  (1) — Elite + Intermediate : {label_counts.get(1, 0):>5,}")
print(f"  Churned   (0) — Basic                : {label_counts.get(0, 0):>5,}")
print(f"  Class imbalance ratio                : 1 : {label_counts.get(0,1)/label_counts.get(1,1):.1f}")
print()

X = retention_df[feature_cols].values
y = retention_df["retained"].values

# ── 3. Train/Test Split (80/20, stratified) ────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Scale features (GBM doesn't strictly require it, but helps with regularization)
scaler_ret = StandardScaler()
X_train_sc = scaler_ret.fit_transform(X_train)
X_test_sc  = scaler_ret.transform(X_test)

print(f"  Train set: {X_train.shape[0]:,} samples | Test set: {X_test.shape[0]:,} samples")
print()

# ── 4. Class Imbalance Handling via sample weights ─────────────────────────
sample_weights_train = compute_sample_weight("balanced", y_train)

# ── 5. Gradient Boosting Classifier ───────────────────────────────────────
retention_model = GradientBoostingClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    min_samples_leaf=10,
    subsample=0.8,
    max_features="sqrt",
    random_state=42,
    validation_fraction=0.1,
    n_iter_no_change=20,
    tol=1e-4,
)
retention_model.fit(X_train_sc, y_train, sample_weight=sample_weights_train)

# ── 6. Cross-Validation (Stratified 5-fold) ────────────────────────────────
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_auc_scores = cross_val_score(
    GradientBoostingClassifier(
        n_estimators=200, learning_rate=0.05, max_depth=4,
        min_samples_leaf=10, subsample=0.8, random_state=42
    ),
    X_train_sc, y_train,
    cv=cv, scoring="roc_auc",
    fit_params={"sample_weight": sample_weights_train},
)
print(f"  Cross-Validation ROC-AUC (5-fold): {cv_auc_scores.mean():.4f} ± {cv_auc_scores.std():.4f}")
print(f"  CV scores per fold: {[round(s, 4) for s in cv_auc_scores]}")
print()

# ── 7. Evaluate on Test Set ────────────────────────────────────────────────
y_pred_prob = retention_model.predict_proba(X_test_sc)[:, 1]
y_pred      = retention_model.predict(X_test_sc)

roc_auc   = roc_auc_score(y_test, y_pred_prob)
precision = precision_score(y_test, y_pred, zero_division=0)
recall    = recall_score(y_test, y_pred, zero_division=0)
f1        = f1_score(y_test, y_pred, zero_division=0)
cm        = confusion_matrix(y_test, y_pred)

print("═" * 60)
print("  MODEL PERFORMANCE — TEST SET")
print("═" * 60)
print(f"  ROC-AUC   : {roc_auc:.4f}")
print(f"  Precision : {precision:.4f}")
print(f"  Recall    : {recall:.4f}")
print(f"  F1 Score  : {f1:.4f}")
print()
print("  Confusion Matrix (rows=actual, cols=predicted):")
print(f"           Pred 0   Pred 1")
print(f"  Actual 0  {cm[0,0]:>5}    {cm[0,1]:>5}")
print(f"  Actual 1  {cm[1,0]:>5}    {cm[1,1]:>5}")
print()
print("  Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Churned (Basic)", "Retained"]))
print("═" * 60)

# Store as variables for downstream use
retention_roc_auc    = roc_auc
retention_precision  = precision
retention_recall     = recall
retention_f1         = f1
retention_cv_auc     = cv_auc_scores.mean()

# ── 8. Feature Importance Chart ───────────────────────────────────────────
feature_names_display = [
    "Active Days",
    "Tool Diversity",
    "Credits Used",
    "Coder Agent %",
    "VDR",
    "CSI V3",
    "Resonance Factor",
    "Engagement Density",
]

importances = retention_model.feature_importances_
sorted_idx  = np.argsort(importances)
sorted_imp  = importances[sorted_idx]
sorted_feat = [feature_names_display[i] for i in sorted_idx]

# Color bars by importance magnitude
max_imp  = sorted_imp.max()
bar_clrs = []
for imp in sorted_imp:
    ratio = imp / max_imp
    if ratio >= 0.6:
        bar_clrs.append(C_HIGHLIGHT)
    elif ratio >= 0.3:
        bar_clrs.append(C_BLUE)
    else:
        bar_clrs.append(C_LAVENDER)

fig_feat_imp, ax_fi = plt.subplots(figsize=(10, 6))
fig_feat_imp.patch.set_facecolor(BG_COLOR)
ax_fi.set_facecolor(BG_COLOR)

bars_fi = ax_fi.barh(sorted_feat, sorted_imp, color=bar_clrs, height=0.65, edgecolor="none")

# Value labels on bars
for bar_fi, imp_val in zip(bars_fi, sorted_imp):
    ax_fi.text(
        imp_val + max_imp * 0.01,
        bar_fi.get_y() + bar_fi.get_height() / 2,
        f"{imp_val:.3f}",
        va="center", ha="left",
        color=TEXT_PRI, fontsize=9, fontweight="bold"
    )

ax_fi.set_xlabel("Feature Importance (Gain)", color=TEXT_SEC, fontsize=10)
ax_fi.set_title(
    "Feature Importance — Retention Prediction Model\n"
    "Which behaviors drive Elite/Intermediate retention?",
    color=TEXT_PRI, fontsize=13, fontweight="bold", pad=14
)
ax_fi.tick_params(colors=TEXT_PRI, labelsize=9)
ax_fi.spines["top"].set_visible(False)
ax_fi.spines["right"].set_visible(False)
ax_fi.spines["bottom"].set_color(GRID_COL)
ax_fi.spines["left"].set_color(GRID_COL)
ax_fi.xaxis.label.set_color(TEXT_SEC)

# Legend
legend_patches = [
    mpatches.Patch(color=C_HIGHLIGHT, label="High importance (≥60%)"),
    mpatches.Patch(color=C_BLUE,      label="Medium importance (30–60%)"),
    mpatches.Patch(color=C_LAVENDER,  label="Low importance (<30%)"),
]
ax_fi.legend(
    handles=legend_patches,
    loc="lower right",
    framealpha=0.15,
    labelcolor=TEXT_PRI,
    fontsize=8,
    facecolor=BG_COLOR,
    edgecolor=GRID_COL,
)

plt.tight_layout()

# ── 9. Performance Summary Table (clean print) ────────────────────────────
print()
print("═" * 60)
print("  RETENTION MODEL — PERFORMANCE SUMMARY")
print("═" * 60)
print(f"  {'Metric':<28} {'Value':>10}")
print(f"  {'-'*38}")
print(f"  {'ROC-AUC (test)':<28} {roc_auc:>10.4f}")
print(f"  {'ROC-AUC (CV mean)':<28} {cv_auc_scores.mean():>10.4f}")
print(f"  {'ROC-AUC (CV std)':<28} {cv_auc_scores.std():>10.4f}")
print(f"  {'Precision':<28} {precision:>10.4f}")
print(f"  {'Recall':<28} {recall:>10.4f}")
print(f"  {'F1 Score':<28} {f1:>10.4f}")
print(f"  {'Train Samples':<28} {X_train.shape[0]:>10,}")
print(f"  {'Test Samples':<28} {X_test.shape[0]:>10,}")
print(f"  {'Features':<28} {len(feature_cols):>10}")
print(f"  {'Estimators (trees)':<28} {retention_model.n_estimators_:>10}")
print("═" * 60)
status_icon = "✅" if roc_auc > 0.85 else "⚠️"
print(f"\n  {status_icon}  ROC-AUC {'EXCEEDS' if roc_auc > 0.85 else 'BELOW'} target threshold (0.85)")
print()
