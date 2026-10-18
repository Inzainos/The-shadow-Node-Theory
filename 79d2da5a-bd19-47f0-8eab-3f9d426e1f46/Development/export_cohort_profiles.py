
import pandas as pd
import numpy as np
import os

# ── 1. Filter cohorts ──────────────────────────────────────────────────────
elite_df        = cohort_df[cohort_df["cohort"] == "Elite"].copy()
intermediate_df = cohort_df[cohort_df["cohort"] == "Intermediate"].copy()

# ── 2. Ensure output directory exists ─────────────────────────────────────
os.makedirs("docu", exist_ok=True)

# ── 3. Export to CSV ───────────────────────────────────────────────────────
elite_df.to_csv("docu/elite_users.csv", index=True, index_label="user_index")
intermediate_df.to_csv("docu/intermediate_users.csv", index=True, index_label="user_index")

print(f"✅  Exported {len(elite_df):,} Elite users        → docu/elite_users.csv")
print(f"✅  Exported {len(intermediate_df):,} Intermediate users → docu/intermediate_users.csv")
print()

# ── 4. Helper: event-pattern summary for a cohort ─────────────────────────
def cohort_event_summary(df, name):
    """
    Compute top event-pattern and most-used-tools fingerprint for a cohort.
    Since we work from aggregated user-level metrics (no raw event log per row),
    we characterise 'event patterns' by bucketing users into behavioural archetypes
    derived from the available numeric metrics.
    """
    numeric_cols = [
        "total_eventos", "dias_activos", "vida_util_dias",
        "herramientas_unicas", "total_creditos",
        "coder_agent_events", "pct_coder_agent", "VDR", "CSI_V3",
    ]

    print("=" * 70)
    print(f"  COHORT: {name}  (n = {len(df):,})")
    print("=" * 70)

    # ── 4a. Descriptive stats ──────────────────────────────────────────────
    stats = df[numeric_cols].describe().T[["mean", "50%", "std", "min", "max"]]
    stats.columns = ["Mean", "Median", "Std", "Min", "Max"]
    print("\n📊  Key Metric Distributions:")
    print(stats.round(3).to_string())

    # ── 4b. Top event-intensity quartile (event patterns) ─────────────────
    df_copy = df.copy()
    df_copy["_event_quartile"] = pd.qcut(
        df_copy["total_eventos"], q=4,
        labels=["Low", "Mid-Low", "Mid-High", "High"],
        duplicates="drop"
    )
    event_dist = df_copy["_event_quartile"].value_counts().sort_index()
    print("\n🔁  Top Event-Intensity Patterns (by total_eventos quartile):")
    for bucket, cnt in event_dist.items():
        bar = "█" * int(cnt / max(event_dist) * 20)
        print(f"   {str(bucket):<10}  {cnt:>4,} users  {bar}")

    # ── 4c. Coder-Agent engagement tiers ──────────────────────────────────
    df_copy["_coder_tier"] = pd.cut(
        df_copy["pct_coder_agent"],
        bins=[-0.01, 0, 10, 50, 100],
        labels=["None (0%)", "Low (1–10%)", "Medium (10–50%)", "Heavy (>50%)"],
    )
    coder_dist = df_copy["_coder_tier"].value_counts().sort_index()
    print("\n🤖  Coder Agent Usage Tiers:")
    for tier, cnt in coder_dist.items():
        pct = cnt / len(df_copy) * 100
        print(f"   {str(tier):<20}  {cnt:>4,} users  ({pct:.1f}%)")

    # ── 4d. Most-used tools (herramientas_unicas) distribution ────────────
    tool_counts = df_copy["herramientas_unicas"].value_counts().sort_index()
    # Keep top-10 tool counts
    top_tools = tool_counts.head(10)
    print("\n🛠️   Most-Used Tool Counts (herramientas_unicas — top 10 values):")
    for n_tools, cnt in top_tools.items():
        pct = cnt / len(df_copy) * 100
        bar = "█" * int(pct / max(top_tools / len(df_copy) * 100) * 20)
        print(f"   {n_tools:>2} tool(s):  {cnt:>4,} users  ({pct:.1f}%)  {bar}")

    # ── 4e. Resonance & lifecycle ──────────────────────────────────────────
    resonance_pct = df_copy["resonancia"].mean() * 100
    avg_lifetime  = df_copy["vida_util_dias"].mean()
    avg_active    = df_copy["dias_activos"].mean()
    print(f"\n📌  Engagement Highlights:")
    print(f"   Resonance rate    : {resonance_pct:.1f}%")
    print(f"   Avg lifetime (days): {avg_lifetime:.1f}")
    print(f"   Avg active days   : {avg_active:.1f}")
    print()


# ── 5. Print summaries ─────────────────────────────────────────────────────
cohort_event_summary(elite_df,        "Elite")
cohort_event_summary(intermediate_df, "Intermediate")

print("─" * 70)
print("📁  Files written to docu/ directory.")
