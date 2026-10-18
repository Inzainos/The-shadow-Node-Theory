
import pandas as pd
import numpy as np

# --- Cohort Thresholds ---
# Elite: top 0.5%  → percentile >= 99.5
# Intermediate: next 6.4% → percentile in [93.1, 99.5)
# Basic: rest → percentile < 93.1

p99_5 = user_metrics_fractal["CSI_V3"].quantile(0.995)
p93_1 = user_metrics_fractal["CSI_V3"].quantile(0.931)

print(f"CSI_V3 Cohort Thresholds (HackerEarth — Fractal V3):")
print(f"  Elite (top 0.5%)       : CSI_V3 >= {p99_5:.4f}")
print(f"  Intermediate (next 6.4%): {p93_1:.4f} <= CSI_V3 < {p99_5:.4f}")
print(f"  Basic (rest)           : CSI_V3 < {p93_1:.4f}")
print()

def assign_cohort(score):
    if score >= p99_5:
        return "Elite"
    elif score >= p93_1:
        return "Intermediate"
    else:
        return "Basic"

cohort_df = user_metrics_fractal.copy()
cohort_df["cohort"] = cohort_df["CSI_V3"].apply(assign_cohort)

# Cohort sizes
cohort_counts = cohort_df["cohort"].value_counts()
cohort_pct    = (cohort_counts / len(cohort_df) * 100).round(2)
print("Cohort Sizes:")
for cohort in ["Elite", "Intermediate", "Basic"]:
    n   = cohort_counts.get(cohort, 0)
    pct = cohort_pct.get(cohort, 0.0)
    print(f"  {cohort:<14}: {n:>5,}  ({pct:.2f}%)")
print()

# --- Behavioral Metrics per Cohort ---
metrics = {
    "Avg Active Days"   : "dias_activos",
    "Avg Tool Diversity": "herramientas_unicas",
    "Avg Credits Used"  : "total_creditos",
    "Avg Coder Agent %": "pct_coder_agent",
    "Avg VDR"           : "VDR",
}

summary_rows = []
for cohort in ["Elite", "Intermediate", "Basic"]:
    grp = cohort_df[cohort_df["cohort"] == cohort]
    row = {"Cohort": cohort, "N": len(grp), "% of Users": f"{len(grp)/len(cohort_df)*100:.2f}%"}
    for label, col in metrics.items():
        row[label] = round(grp[col].mean(), 4)
    summary_rows.append(row)

summary = pd.DataFrame(summary_rows).set_index("Cohort")

# Pretty print
pd.set_option("display.float_format", "{:.4f}".format)
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)

print("=" * 90)
print("  HackerEarth — CSI_V3 Cohort Behavioral Summary")
print("=" * 90)
print(summary.to_string())
print("=" * 90)

# Expose for downstream use
cohort_summary = summary
