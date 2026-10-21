
import pandas as pd
import numpy as np
import os

# ══════════════════════════════════════════════════════════════════════════════
#  TRIGGER INTEGRITY AUDIT — Full cross-dataset inspection
#  Checks: column presence, nulls, unique values, join keys, index alignment
#  Files: zerve_hackathon_dataset.csv, metricas_fractal_v3.csv,
#         docu/churn_early_warning.csv, docu/retention_scores.csv,
#         docu/elite_users.csv, docu/intermediate_users.csv
# ══════════════════════════════════════════════════════════════════════════════

DIVIDER = "═" * 78
DIVIDER2 = "─" * 78

# ── Trigger / key columns to specifically inspect ────────────────────────────
TRIGGER_COLS = [
    "top_churn_trigger_event", "top_churn_trigger",
    "recommended_action", "risk_tier", "churn_probability",
    "trigger_event", "trigger", "event", "event_type",
    "retention_signal_score", "churn_signal_score",
    "shap_proxy_score", "churn_lift", "direction",
    "person_id", "user_id", "CSI_V3", "cohort", "retention_prob",
]

print(DIVIDER)
print("  🔍  TRIGGER INTEGRITY AUDIT — FULL CROSS-DATASET INSPECTION")
print(DIVIDER)

# ── Helper: profile a dataframe ───────────────────────────────────────────────
def audit_df(df, name, trigger_cols=TRIGGER_COLS):
    print(f"\n{'━'*78}")
    print(f"  📁  DATASET: {name}")
    print(f"{'━'*78}")
    print(f"  Shape           : {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"  Index type      : {type(df.index).__name__}  |  dtype: {df.index.dtype}")
    print(f"  Index sample    : {list(df.index[:5])}")
    print(f"  Index nulls     : {df.index.isna().sum()}")
    print(f"  Index unique    : {df.index.nunique():,}  (of {len(df.index):,} rows)")
    print(f"  Duplicate index : {df.index.duplicated().sum()}")
    
    print(f"\n  ALL COLUMNS ({df.shape[1]}):")
    for col in df.columns:
        dtype = df[col].dtype
        null_count = df[col].isna().sum()
        null_pct = null_count / len(df) * 100 if len(df) > 0 else 0
        unique = df[col].nunique()
        print(f"    • {col:<45} dtype={str(dtype):<12} nulls={null_count:>5} ({null_pct:4.1f}%)  unique={unique:>6,}")
    
    # Trigger column presence & values
    print(f"\n  🎯  TRIGGER COLUMN AUDIT:")
    found_triggers = []
    missing_triggers = []
    for tc in trigger_cols:
        if tc in df.columns:
            found_triggers.append(tc)
        elif tc == df.index.name:
            print(f"    ✅  '{tc}' — FOUND AS INDEX  (unique={df.index.nunique():,})")
        else:
            missing_triggers.append(tc)
    
    for tc in found_triggers:
        null_c = df[tc].isna().sum()
        unique_c = df[tc].nunique()
        sample_vals = df[tc].dropna().value_counts().head(8)
        print(f"\n    ✅  FOUND: '{tc}'")
        print(f"       dtype={df[tc].dtype}  |  nulls={null_c}  |  unique={unique_c}")
        print(f"       Top values:")
        for v, cnt in sample_vals.items():
            print(f"         {str(v):<50} → {cnt:>6,} rows ({cnt/len(df)*100:.1f}%)")
        if null_c > 0:
            print(f"       ⚠️  {null_c:,} NULL values ({null_c/len(df)*100:.1f}%)")
        if unique_c == 1:
            print(f"       ⚠️  SINGLE VALUE — column has zero variance (all same value)")
        if unique_c == 0:
            print(f"       ❌  ZERO unique values — all null or empty")
    
    if missing_triggers:
        print(f"\n    ❌  MISSING trigger columns in {name}:")
        for tc in missing_triggers:
            print(f"       • {tc}")
    
    return {"name": name, "shape": df.shape, "found": found_triggers, "missing": missing_triggers}

# ══════════════════════════════════════════════════════════════════════════════
#  1. Load and audit all 6 datasets
# ══════════════════════════════════════════════════════════════════════════════

datasets = {}

# 1a. zerve_hackathon_dataset.csv (raw events)
print(f"\n[1/6] Loading zerve_hackathon_dataset.csv ...")
raw_df = pd.read_csv("zerve_hackathon_dataset.csv")
datasets["zerve_hackathon_dataset"] = raw_df
r1 = audit_df(raw_df, "zerve_hackathon_dataset.csv")

# 1b. metricas_fractal_v3.csv
print(f"\n[2/6] Loading metricas_fractal_v3.csv ...")
frac_df = pd.read_csv("metricas_fractal_v3.csv", index_col=0)
datasets["metricas_fractal_v3"] = frac_df
r2 = audit_df(frac_df, "metricas_fractal_v3.csv")

# 1c. docu/churn_early_warning.csv
print(f"\n[3/6] Loading docu/churn_early_warning.csv ...")
cew_df = pd.read_csv("docu/churn_early_warning.csv", index_col=0)
datasets["churn_early_warning"] = cew_df
r3 = audit_df(cew_df, "docu/churn_early_warning.csv")

# 1d. docu/retention_scores.csv
print(f"\n[4/6] Loading docu/retention_scores.csv ...")
ret_df = pd.read_csv("docu/retention_scores.csv", index_col=0)
datasets["retention_scores"] = ret_df
r4 = audit_df(ret_df, "docu/retention_scores.csv")

# 1e. docu/elite_users.csv
print(f"\n[5/6] Loading docu/elite_users.csv ...")
elite_df_raw = pd.read_csv("docu/elite_users.csv", index_col=0)
datasets["elite_users"] = elite_df_raw
r5 = audit_df(elite_df_raw, "docu/elite_users.csv")

# 1f. docu/intermediate_users.csv
print(f"\n[6/6] Loading docu/intermediate_users.csv ...")
inter_df_raw = pd.read_csv("docu/intermediate_users.csv", index_col=0)
datasets["intermediate_users"] = inter_df_raw
r6 = audit_df(inter_df_raw, "docu/intermediate_users.csv")

# ══════════════════════════════════════════════════════════════════════════════
#  2. Cross-dataset join compatibility analysis
# ══════════════════════════════════════════════════════════════════════════════

print(f"\n{DIVIDER}")
print("  🔗  CROSS-DATASET JOIN COMPATIBILITY ANALYSIS")
print(DIVIDER)

# Key: which index/column in each dataset maps to person_id?
# raw event data → person_id column
# metricas_fractal_v3 → index (person_id)
# churn_early_warning → index (row number from _surv_df which is a reset_index)
# retention_scores → index 
# elite/intermediate → index

raw_users = set(raw_df["person_id"].unique())
frac_users = set(frac_df.index.unique())

print(f"\n  Raw event users (person_id col)   : {len(raw_users):,}")
print(f"  metricas_fractal_v3 index users   : {len(frac_users):,}")
print(f"  Intersection                      : {len(raw_users & frac_users):,}")
print(f"  In raw NOT in fractal             : {len(raw_users - frac_users):,}")
print(f"  In fractal NOT in raw             : {len(frac_users - raw_users):,}")

# Check churn_early_warning index
print(f"\n  churn_early_warning.csv index     : {cew_df.index.dtype}")
print(f"  Sample index values               : {list(cew_df.index[:5])}")
print(f"  Is integer index (row nums)?      : {pd.api.types.is_integer_dtype(cew_df.index)}")
if pd.api.types.is_integer_dtype(cew_df.index):
    print(f"  ⚠️  INDEX IS INTEGER (row position), NOT person_id!")
    print(f"  → churn_early_warning rows are positional indices 0..{cew_df.index.max()}")
    print(f"  → Cannot join directly to person_id-indexed datasets without position alignment")

# Check retention_scores index
print(f"\n  retention_scores.csv index        : {ret_df.index.dtype}")
print(f"  Sample index values               : {list(ret_df.index[:5])}")
ret_users = set(ret_df.index.unique()) if not pd.api.types.is_integer_dtype(ret_df.index) else set()
if not pd.api.types.is_integer_dtype(ret_df.index):
    print(f"  Retention score users             : {len(ret_users):,}")
    print(f"  Intersection with raw             : {len(raw_users & ret_users):,}")
    print(f"  In retention NOT in raw           : {len(ret_users - raw_users):,}")
else:
    print(f"  ⚠️  INTEGER INDEX — cannot join to person_id-indexed data without alignment")

# Check elite / intermediate
elite_users_set = set(elite_df_raw.index.unique())
inter_users_set = set(inter_df_raw.index.unique())
print(f"\n  elite_users.csv index             : {elite_df_raw.index.dtype}")
print(f"  elite_users count                 : {len(elite_users_set):,}")
print(f"  intermediate_users.csv index      : {inter_df_raw.index.dtype}")
print(f"  intermediate_users count          : {len(inter_users_set):,}")

if not pd.api.types.is_integer_dtype(elite_df_raw.index):
    print(f"  Elite ∩ fractal                   : {len(elite_users_set & frac_users):,}")
    print(f"  Intermediate ∩ fractal            : {len(inter_users_set & frac_users):,}")

# ══════════════════════════════════════════════════════════════════════════════
#  3. Trigger column deep-dive across all datasets
# ══════════════════════════════════════════════════════════════════════════════

print(f"\n{DIVIDER}")
print("  🎯  TRIGGER COLUMN DEEP-DIVE — UNIQUE VALUES & NULL ANALYSIS")
print(DIVIDER)

key_trigger_map = {
    "churn_early_warning": ["top_churn_trigger_event", "recommended_action", "risk_tier", "churn_probability"],
    "retention_scores": [],
    "metricas_fractal_v3": [],
    "elite_users": [],
    "intermediate_users": [],
    "zerve_hackathon_dataset": ["event"],
}

for ds_name, ds_df in datasets.items():
    print(f"\n  [{ds_name}]")
    triggers_to_show = key_trigger_map.get(ds_name, [])
    
    # Check specifically for trigger-related columns
    trigger_like = [c for c in ds_df.columns
                    if any(kw in c.lower() for kw in ["trigger", "action", "risk", "churn", "retention", "signal", "event"])]
    
    for col in sorted(set(triggers_to_show + trigger_like)):
        if col not in ds_df.columns:
            print(f"    ❌  '{col}' — NOT PRESENT")
            continue
        null_c = ds_df[col].isna().sum()
        null_pct = null_c / len(ds_df) * 100
        unique_c = ds_df[col].nunique()
        top_vals = ds_df[col].dropna().value_counts().head(5)
        
        status = "✅" if null_c == 0 and unique_c > 1 else "⚠️ "
        if null_c == len(ds_df) or unique_c == 0:
            status = "❌"
        
        print(f"    {status}  '{col}'  nulls={null_c}/{len(ds_df)} ({null_pct:.0f}%)  unique={unique_c}")
        for val, cnt in top_vals.items():
            print(f"         └─ {str(val):<50} = {cnt:>5,}")
        
        # Special check: "none" placeholder
        if "none" in [str(v).lower() for v in top_vals.index]:
            none_count = ds_df[col].apply(lambda x: str(x).lower() == "none").sum()
            print(f"         ⚠️  '{col}' contains {none_count:,} literal 'none' strings ({none_count/len(ds_df)*100:.1f}%)")

# ══════════════════════════════════════════════════════════════════════════════
#  4. Root Cause Summary
# ══════════════════════════════════════════════════════════════════════════════

print(f"\n{DIVIDER}")
print("  🔴  ROOT CAUSE SUMMARY — WHY TRIGGERS DON'T APPEAR IN DASHBOARD TABS")
print(DIVIDER)

# Enumerate specific issues found
issues = []

# Issue 1: churn_early_warning.csv index type
if pd.api.types.is_integer_dtype(cew_df.index):
    issues.append((
        "CRITICAL",
        "churn_early_warning.csv has INTEGER positional index (0..4773), NOT person_id hashes",
        "Dashboard joins on person_id will silently fail — no row will match unless dashboard also uses positional indexing",
        "Fix: re-save with person_id as index: cew_df.to_csv(..., index=True) after setting person_id as index"
    ))

# Issue 2: 'none' placeholder in top_churn_trigger_event
if "top_churn_trigger_event" in cew_df.columns:
    none_count = cew_df["top_churn_trigger_event"].apply(lambda x: str(x).lower() == "none").sum()
    none_pct = none_count / len(cew_df) * 100
    if none_count > 0:
        issues.append((
            "HIGH",
            f"top_churn_trigger_event has {none_count:,} ({none_pct:.1f}%) rows with literal string 'none'",
            "Dashboard likely filters for non-null/non-empty trigger events; 'none' is not null so filter passes but value is meaningless",
            "Fix: replace 'none' with pd.NA or assign most-likely event from event_feature_matrix for those users"
        ))

# Issue 3: risk_tier is a Categorical type
if "risk_tier" in cew_df.columns:
    if str(cew_df["risk_tier"].dtype) == "category":
        issues.append((
            "MEDIUM",
            "risk_tier column in churn_early_warning.csv is Categorical dtype",
            "CSV serialization may strip category metadata. Downstream code comparing risk_tier strings may fail if dtype differs",
            "Fix: cast to str before saving: df['risk_tier'] = df['risk_tier'].astype(str)"
        ))

# Issue 4: missing retention_triggers column (dashboard might look for it)
trigger_cols_in_cew = [c for c in cew_df.columns if "trigger" in c.lower()]
if not trigger_cols_in_cew:
    issues.append((
        "CRITICAL",
        "churn_early_warning.csv has NO column with 'trigger' in the name",
        "Dashboard tabs looking for a 'trigger' column won't find any data",
        "Fix: ensure 'top_churn_trigger_event' is exported correctly"
    ))

# Issue 5: Check if retention_scores has trigger columns at all
ret_trigger_cols = [c for c in ret_df.columns if any(kw in c.lower() for kw in ["trigger", "churn", "action", "risk"])]
if not ret_trigger_cols:
    issues.append((
        "HIGH",
        f"docu/retention_scores.csv has NO trigger/churn/action/risk columns (has {list(ret_df.columns[:8])}...)",
        "If dashboard tab reads from retention_scores.csv looking for triggers, it finds nothing",
        "Fix: add trigger columns to retention_scores export, or ensure dashboard reads from churn_early_warning.csv"
    ))

# Issue 6: Index mismatch between datasets
if pd.api.types.is_integer_dtype(cew_df.index) and not pd.api.types.is_integer_dtype(frac_df.index):
    issues.append((
        "CRITICAL",
        "INDEX TYPE MISMATCH between churn_early_warning (int) and metricas_fractal_v3/retention (person_id hash strings)",
        "Any merge/join between these datasets on index will produce 0 matches",
        "Fix: use consistent person_id string hash as index across all exported CSVs"
    ))

# Print all issues
for severity, problem, impact, fix in issues:
    icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🟢"}.get(severity, "⚪")
    print(f"\n  {icon}  [{severity}]  {problem}")
    print(f"     Impact: {impact}")
    print(f"     Fix   : {fix}")

if not issues:
    print("\n  ✅  No critical issues detected in trigger column structure!")
    print("  → Dashboard absence of triggers may be a rendering/filtering issue, not a data issue")

print(f"\n{DIVIDER}")
print(f"  📋  INTEGRITY AUDIT COMPLETE")
print(f"  Datasets audited  : {len(datasets)}")
print(f"  Issues found      : {len(issues)} ({sum(1 for s,*_ in issues if s=='CRITICAL')} CRITICAL, "
      f"{sum(1 for s,*_ in issues if s=='HIGH')} HIGH, "
      f"{sum(1 for s,*_ in issues if s=='MEDIUM')} MEDIUM)")
print(f"  Total trigger cols found in churn_early_warning: {trigger_cols_in_cew}")
print(DIVIDER)
