import pandas as pd
import numpy as np

# ── FRACTAL V3 PROTOCOL ANALYSIS — HackerEarth ───────────────────────────────
# Uses pre-computed user_metrics_fractal from load_fractal_metrics block
# user_metrics_fractal already contains: total_eventos, herramientas_unicas,
# total_creditos, coder_agent_events, dias_activos, vida_util_dias,
# pct_coder_agent, VDR, resonancia, CSI_V3

print("=" * 72)
print("  🧬  HackerEarth — FRACTAL V3 PROTOCOL — FULL ANALYSIS")
print("=" * 72)

# ── 1. USER METRICS SUMMARY ──────────────────────────────────────────────────
print(f"\n📊 User Metrics Summary (N = {len(user_metrics_fractal):,} users)")
print(f"   Total Events (sum)      : {user_metrics_fractal['total_eventos'].sum():>12,.0f}")
print(f"   Unique Tools (avg)      : {user_metrics_fractal['herramientas_unicas'].mean():>12.2f}")
print(f"   Total Credits (sum)     : {user_metrics_fractal['total_creditos'].sum():>12.2f}")
print(f"   Coder Agent (avg %)     : {user_metrics_fractal['pct_coder_agent'].mean():>12.2f}%")
print(f"   Active Days (avg)       : {user_metrics_fractal['dias_activos'].mean():>12.2f}")
print(f"   Lifespan Days (avg)     : {user_metrics_fractal['vida_util_dias'].mean():>12.2f}")

# ── 2. VDR — Velocity of tool Diversification Rate ───────────────────────────
print("\n📐 VDR — Velocity of tool Diversification Rate")
print(f"   VDR mean                : {user_metrics_fractal['VDR'].mean():>12.4f}")
print(f"   VDR median              : {user_metrics_fractal['VDR'].median():>12.4f}")
print(f"   VDR p95                 : {user_metrics_fractal['VDR'].quantile(0.95):>12.4f}")
print(f"   VDR max                 : {user_metrics_fractal['VDR'].max():>12.4f}")
print(f"   Users with VDR > 0      : {(user_metrics_fractal['VDR'] > 0).sum():>12,}")

# ── 3. CSI_V3 COMPOSITE SCORE WITH RESONANCE BOOST ───────────────────────────
print("\n🔮 CSI_V3 Composite Score with Resonance Boost")
resonance_users = user_metrics_fractal['resonancia'].sum()
total_users = len(user_metrics_fractal)
print(f"   Resonance users (boost) : {resonance_users:>12,} ({resonance_users/total_users*100:.1f}%)")
print(f"   CSI_V3 mean             : {user_metrics_fractal['CSI_V3'].mean():>12.4f}")
print(f"   CSI_V3 median           : {user_metrics_fractal['CSI_V3'].median():>12.4f}")
print(f"   CSI_V3 p95              : {user_metrics_fractal['CSI_V3'].quantile(0.95):>12.4f}")
print(f"   CSI_V3 max              : {user_metrics_fractal['CSI_V3'].max():>12.4f}")

# ── 4. COHORT DISTRIBUTION ────────────────────────────────────────────────────
# Assign cohorts based on CSI_V3 thresholds from load_fractal_metrics
# Elite > p99.5, Intermediate > p93.1, Basic = rest
_p99_5 = user_metrics_fractal['CSI_V3'].quantile(0.995)
_p93_1 = user_metrics_fractal['CSI_V3'].quantile(0.931)

def _assign_cohort(score):
    if score > _p99_5:
        return "Elite"
    elif score > _p93_1:
        return "Intermediate"
    else:
        return "Basic"

_cohort_col = user_metrics_fractal['CSI_V3'].apply(_assign_cohort)
_cohort_dist = _cohort_col.value_counts()
print(f"\n🏅 Cohort Distribution (p99.5={_p99_5:.2f}, p93.1={_p93_1:.2f})")
for _c, _n in _cohort_dist.items():
    print(f"   {_c:<15}: {_n:>6,}  ({_n/total_users*100:.1f}%)")

# ── 5. TOP 10 ORCHESTRATORS ───────────────────────────────────────────────────
_top10 = user_metrics_fractal.sort_values('CSI_V3', ascending=False).head(10).copy()
_top10['cohort_label'] = _top10['CSI_V3'].apply(_assign_cohort)

print("\n")
print("═" * 90)
print("  🏆  TOP 10 ORCHESTRATORS — HackerEarth FRACTAL V3 RANKING")
print("═" * 90)
print(f"  {'Rank':<5} {'User ID (truncated)':<20} {'CSI_V3':>8} {'VDR':>9} {'Tools':>6} {'Credits':>10} {'Active Days':>12} {'Resonance':>10} {'Cohort':<14}")
print(f"  {'-'*87}")
for _rank, (_uid, _row) in enumerate(_top10.iterrows(), 1):
    _uid_short = str(_uid)[:18] + ".."
    _res_icon = "✅" if _row['resonancia'] else "—"
    _cohort_label = _row.get('cohort_label', _assign_cohort(_row['CSI_V3']))
    print(
        f"  {_rank:<5} {_uid_short:<20} {_row['CSI_V3']:>8.2f} {_row['VDR']:>9.3f} "
        f"{int(_row['herramientas_unicas']):>6} {_row['total_creditos']:>10.2f} "
        f"{int(_row['dias_activos']):>12} {_res_icon:>10}   {_cohort_label:<14}"
    )
print("═" * 90)

# ── 6. SAVE TO metricas_fractal_v3.csv (working directory) ───────────────────
_save_path = "metricas_fractal_v3.csv"
user_metrics_fractal.to_csv(_save_path)
print(f"\n✅ Saved {len(user_metrics_fractal):,} user records → {_save_path}")

# Verify file saved correctly
import os
_file_size = os.path.getsize(_save_path)
print(f"   File size: {_file_size:,} bytes ({_file_size/1024:.1f} KB)")

print("\n" + "═" * 72)
print("  ✅  HackerEarth FRACTAL V3 PROTOCOL COMPLETE")
print("═" * 72)
