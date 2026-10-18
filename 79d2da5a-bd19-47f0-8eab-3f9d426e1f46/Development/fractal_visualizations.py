import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# ── Zerve / Mycelial dark theme ───────────────────────────────────────────────
BG       = "#1D1D20"
TEXT_PRI = "#fbfbff"
TEXT_SEC = "#909094"
GRID_COL = "#2e2e34"

ACCENT_BLUE   = "#A1C9F4"
ACCENT_ORANGE = "#FFB482"
ACCENT_GREEN  = "#8DE5A1"
ACCENT_CORAL  = "#FF9F9B"
HIGHLIGHT     = "#ffd400"

plt.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor":   BG,
    "axes.edgecolor":   GRID_COL,
    "axes.labelcolor":  TEXT_PRI,
    "xtick.color":      TEXT_SEC,
    "ytick.color":      TEXT_SEC,
    "text.color":       TEXT_PRI,
    "grid.color":       GRID_COL,
    "grid.linewidth":   0.6,
    "font.family":      "monospace",
})

df = user_metrics_fractal.copy()

def style_ax(ax, title, xlabel, ylabel):
    ax.set_title(title, color=TEXT_PRI, fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel(xlabel, color=TEXT_SEC, fontsize=10)
    ax.set_ylabel(ylabel, color=TEXT_SEC, fontsize=10)
    ax.tick_params(colors=TEXT_SEC, labelsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRID_COL)
    ax.grid(axis="y", linestyle="--", alpha=0.4)


# ══════════════════════════════════════════════════════════════════════════════
# Chart 1 – CSI_V3 Score Distribution
# ══════════════════════════════════════════════════════════════════════════════
csi_v3_distribution_fig, ax1 = plt.subplots(figsize=(10, 5))
csi_v3_distribution_fig.patch.set_facecolor(BG)

csi_max = df["CSI_V3"].max()
bins = np.linspace(0, csi_max + 0.01, 50)
counts, edges, patches = ax1.hist(df["CSI_V3"], bins=bins, color=ACCENT_BLUE,
                                   edgecolor=BG, linewidth=0.5, alpha=0.88)

# Blue → orange gradient across bars
for patch, left in zip(patches, edges[:-1]):
    ratio = left / (csi_max + 0.01)
    r = int(0xA1 + (0xFF - 0xA1) * ratio)
    g = int(0xC9 + (0xB4 - 0xC9) * ratio)
    b = int(0xF4 + (0x82 - 0xF4) * ratio)
    patch.set_facecolor(f"#{r:02x}{g:02x}{b:02x}")

median_csi = df["CSI_V3"].median()
mean_csi   = df["CSI_V3"].mean()
ax1.axvline(median_csi, color=HIGHLIGHT,    linestyle="--", linewidth=1.4, label=f"Median {median_csi:.1f}")
ax1.axvline(mean_csi,   color=ACCENT_CORAL, linestyle=":",  linewidth=1.4, label=f"Mean   {mean_csi:.1f}")

style_ax(ax1, "🍄 CSI_V3 Score Distribution — Mycelial Resonance", "CSI_V3 Score", "User Count")
ax1.legend(facecolor=BG, edgecolor=GRID_COL, labelcolor=TEXT_PRI, fontsize=9)
plt.tight_layout()
plt.show()


# ══════════════════════════════════════════════════════════════════════════════
# Chart 2 – VDR vs Tool Diversity Scatter
# ══════════════════════════════════════════════════════════════════════════════
vdr_scatter_fig, ax2 = plt.subplots(figsize=(10, 6))
vdr_scatter_fig.patch.set_facecolor(BG)

ev_min, ev_max = df["total_eventos"].min(), df["total_eventos"].max()
events_norm = (df["total_eventos"] - ev_min) / (ev_max - ev_min + 1e-9)
sizes = 20 + events_norm * 200

sc = ax2.scatter(
    df["herramientas_unicas"], df["VDR"],
    c=df["CSI_V3"], cmap="plasma",
    s=sizes, alpha=0.55, linewidths=0,
)

cbar = vdr_scatter_fig.colorbar(sc, ax=ax2, pad=0.02)
cbar.set_label("CSI_V3 Score", color=TEXT_SEC, fontsize=9)
cbar.ax.yaxis.set_tick_params(color=TEXT_SEC)
plt.setp(cbar.ax.yaxis.get_ticklabels(), color=TEXT_SEC, fontsize=8)
cbar.outline.set_edgecolor(GRID_COL)

style_ax(ax2, "🌐 VDR vs Tool Diversity — Network Depth", "Unique Tools Used", "VDR (Viral Diffusion Rate)")
ax2.grid(True, linestyle="--", alpha=0.3)
ax2.text(0.98, 0.02, "Bubble size ∝ total events", transform=ax2.transAxes,
         color=TEXT_SEC, fontsize=8, ha="right", va="bottom")
plt.tight_layout()
plt.show()


# ══════════════════════════════════════════════════════════════════════════════
# Chart 3 – Top 20 Users by CSI_V3
# ══════════════════════════════════════════════════════════════════════════════
top20_csi_fig, ax3 = plt.subplots(figsize=(12, 6))
top20_csi_fig.patch.set_facecolor(BG)

top20 = df.nlargest(20, "CSI_V3").reset_index(drop=True)

# Use index-based labels (person_id may be too long for axis ticks)
user_labels = [f"#{i+1}" for i in range(len(top20))]
bar_colors  = [ACCENT_GREEN if r else ACCENT_BLUE for r in top20["resonancia"]]
bars = ax3.bar(range(20), top20["CSI_V3"], color=bar_colors, edgecolor=BG, linewidth=0.5, width=0.7)

for bar, val in zip(bars, top20["CSI_V3"]):
    ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f"{val:.0f}", ha="center", va="bottom", fontsize=7.5, color=TEXT_SEC)

ax3.set_xticks(range(20))
ax3.set_xticklabels(user_labels, fontsize=9)
style_ax(ax3, "🏆 Top 20 Users by CSI_V3 — Fungal Champions", "User Rank", "CSI_V3 Score")

legend_els = [Patch(facecolor=ACCENT_GREEN, label="Resonance ✓"),
              Patch(facecolor=ACCENT_BLUE,  label="Resonance ✗")]
ax3.legend(handles=legend_els, facecolor=BG, edgecolor=GRID_COL, labelcolor=TEXT_PRI, fontsize=9)
plt.tight_layout()
plt.show()


# ══════════════════════════════════════════════════════════════════════════════
# Chart 4 – Credit Usage Distribution by Cohort
# ══════════════════════════════════════════════════════════════════════════════
credit_cohort_fig, ax4 = plt.subplots(figsize=(10, 6))
credit_cohort_fig.patch.set_facecolor(BG)

# Dynamic cohort bins — handle edge case where max < 365
_vida_max = int(df["vida_util_dias"].max())
_cutpoints = sorted(set([0, 7, 30, 90, min(365, _vida_max), _vida_max + 1]))
# Ensure strictly monotonic and at least 2 unique boundaries
_cutpoints = sorted(set(_cutpoints))

_label_map = {(0, 7): "≤7d", (7, 30): "8–30d", (30, 90): "31–90d",
              (90, 365): "91–365d", (365, _vida_max + 1): ">365d"}
cohort_labels_used = [_label_map.get((a, b), f"{a}–{b}d")
                      for a, b in zip(_cutpoints[:-1], _cutpoints[1:])]

df["_cohort"] = pd.cut(df["vida_util_dias"], bins=_cutpoints,
                        labels=cohort_labels_used, right=True, include_lowest=True)

cohort_credits = (
    df.groupby("_cohort", observed=True)["total_creditos"]
    .agg(["median", "mean", "std"])
    .reset_index()
)

_n = len(cohort_credits)
x_pos = np.arange(_n)
bar_width = 0.35

ax4.bar(x_pos - bar_width / 2, cohort_credits["median"],
        width=bar_width, color=ACCENT_ORANGE, label="Median", edgecolor=BG)
ax4.bar(x_pos + bar_width / 2, cohort_credits["mean"],
        width=bar_width, color=ACCENT_BLUE, label="Mean", edgecolor=BG)

ax4.errorbar(x_pos + bar_width / 2, cohort_credits["mean"],
             yerr=cohort_credits["std"].fillna(0),
             fmt="none", ecolor=TEXT_SEC, elinewidth=1.2, capsize=4)

ax4.set_xticks(x_pos)
ax4.set_xticklabels(cohort_credits["_cohort"].astype(str), fontsize=10)
style_ax(ax4, "💎 Credit Usage by User Lifetime Cohort", "Lifetime Cohort", "Credits Consumed")
ax4.legend(facecolor=BG, edgecolor=GRID_COL, labelcolor=TEXT_PRI, fontsize=9)
plt.tight_layout()
plt.show()

print("✅ All 4 charts rendered successfully.")
print(f"   • CSI_V3 range:  {df['CSI_V3'].min():.2f} – {df['CSI_V3'].max():.2f}  (median {median_csi:.2f}, mean {mean_csi:.2f})")
print(f"   • VDR range:     {df['VDR'].min():.2f} – {df['VDR'].max():.2f}")
print(f"   • vida_util_dias max: {_vida_max}d  |  cohort bins: {_cutpoints}")
print(f"   • Top-20 resonance users: {top20['resonancia'].sum()} / 20")
print(f"   • Cohort credit medians:  {dict(zip(cohort_credits['_cohort'].astype(str), cohort_credits['median']))}")
