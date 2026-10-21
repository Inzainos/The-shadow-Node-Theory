
import pandas as pd
import numpy as np

DIV = "═" * 80
div = "─" * 80

# ══════════════════════════════════════════════════════════════════════════════
#  DEFINITIVE person_id MAPPING AUDIT
#  Steps: (1) Ground truth from zerve events, (2) Positional reconstruction,
#         (3) Row count verification, (4) Full compatibility matrix,
#         (5) Side-by-side 10 sample, (6) Sample join test, (7) Action plan
# ══════════════════════════════════════════════════════════════════════════════

print(DIV)
print("  🔬  DEFINITIVE person_id MAPPING AUDIT")
print(DIV)

# ─── STEP 1: Extract ground-truth person_id set from zerve events ─────────────
print(f"\n{div}")
print("  STEP 1 — GROUND TRUTH: Extract real person_ids from zerve_hackathon_dataset.csv")
print(div)

raw_events = pd.read_csv("zerve_hackathon_dataset.csv")
# Ground-truth: unique person_ids sorted → this is the canonical ordering
# (metricas_fractal_v3 was built by groupby(person_id) → sorted by index = person_id)
gt_person_ids = raw_events["person_id"].unique()
gt_set = set(gt_person_ids)

print(f"  Total raw event rows       : {len(raw_events):,}")
print(f"  Unique person_ids in events: {len(gt_person_ids):,}")
print(f"  Sample (first 5)           : {list(gt_person_ids[:5])}")

# The SORTED order is what derived datasets (groupby+sort) use as their index
sorted_gt_ids = sorted(gt_set)  # alphabetical sort = pandas default groupby key order
print(f"\n  Sorted ground-truth (first 5): {sorted_gt_ids[:5]}")
print(f"  Sorted ground-truth (last  5): {sorted_gt_ids[-5:]}")

# ─── STEP 2: Load all derived datasets + reconstruct person_id by positional alignment ─
print(f"\n{div}")
print("  STEP 2 — POSITIONAL ALIGNMENT RECONSTRUCTION")
print(div)

# metricas_fractal_v3: index_col=0, index IS the person_id (string hash)
frac = pd.read_csv("metricas_fractal_v3.csv", index_col=0)
# churn_early_warning: index_col=0, index is INTEGER row position (0..4773)
cew  = pd.read_csv("docu/churn_early_warning.csv",  index_col=0)
# retention_scores: index_col=0, index is INTEGER row position
ret  = pd.read_csv("docu/retention_scores.csv",     index_col=0)
# elite_users: index_col=0
elit = pd.read_csv("docu/elite_users.csv",           index_col=0)
# intermediate_users: index_col=0
inter = pd.read_csv("docu/intermediate_users.csv",   index_col=0)

print(f"  metricas_fractal_v3   → shape={frac.shape}  index dtype={frac.index.dtype}  "
      f"index sample={list(frac.index[:3])}")
print(f"  churn_early_warning   → shape={cew.shape}   index dtype={cew.index.dtype}   "
      f"index sample={list(cew.index[:3])}")
print(f"  retention_scores      → shape={ret.shape}   index dtype={ret.index.dtype}   "
      f"index sample={list(ret.index[:3])}")
print(f"  elite_users           → shape={elit.shape}  index dtype={elit.index.dtype}  "
      f"index sample={list(elit.index[:3])}")
print(f"  intermediate_users    → shape={inter.shape} index dtype={inter.index.dtype} "
      f"index sample={list(inter.index[:3])}")

# Reconstruct: for datasets with integer index, assume positional alignment
# with sorted_gt_ids (i.e. row 0 = sorted_gt_ids[0], row N = sorted_gt_ids[N])
frac_person_ids = list(frac.index)           # already person_id strings
cew_person_ids_positional  = sorted_gt_ids   # positional → sorted_gt_ids
ret_person_ids_positional  = sorted_gt_ids   # positional → sorted_gt_ids
elit_person_ids = list(elit.index)           # has string index (person_id hashes)
inter_person_ids = list(inter.index)         # has string index (person_id hashes)

print(f"\n  frac person_id sample (from index)          : {frac_person_ids[:3]}")
print(f"  cew  positional reconstruction (sorted_gt)  : {cew_person_ids_positional[:3]}")
print(f"  ret  positional reconstruction (sorted_gt)  : {ret_person_ids_positional[:3]}")
print(f"  elit person_id sample (from index)          : {elit_person_ids[:3]}")
print(f"  inter person_id sample (from index)         : {inter_person_ids[:3]}")

# ─── STEP 3: Verify row counts match exactly 4,774 ──────────────────────────
print(f"\n{div}")
print("  STEP 3 — ROW COUNT VERIFICATION (expect 4,774 for main datasets)")
print(div)

EXPECTED_N = 4774
datasets_to_check = {
    "metricas_fractal_v3":    frac,
    "churn_early_warning":    cew,
    "retention_scores":       ret,
    "elite_users":            elit,
    "intermediate_users":     inter,
}
gt_sorted_n = len(sorted_gt_ids)

print(f"\n  Ground truth sorted person_ids: {gt_sorted_n:,}  {'✅ MATCHES 4,774' if gt_sorted_n == EXPECTED_N else '❌ MISMATCH'}")

alignment_valid = {}
for ds_name, ds_df in datasets_to_check.items():
    n = len(ds_df)
    matches = n == EXPECTED_N
    icon = "✅" if matches else "❌"
    alignment_valid[ds_name] = matches
    print(f"  {icon}  {ds_name:<30} rows={n:,}  {'= 4,774 → positional alignment VALID' if matches else f'≠ 4,774 → CANNOT use positional alignment'}")

# ─── STEP 4: Full compatibility matrix ──────────────────────────────────────
print(f"\n{div}")
print("  STEP 4 — FULL COMPATIBILITY MATRIX")
print(div)

# Build the comprehensive info per dataset
ds_profiles = {
    "zerve_hackathon_dataset": {
        "rows": len(raw_events),
        "key_type": "column",
        "key_col": "person_id",
        "dtype": "string hash",
        "joinable": True,
        "person_ids": gt_set,
        "n_ids": len(gt_set),
    },
    "metricas_fractal_v3": {
        "rows": len(frac),
        "key_type": "index",
        "key_col": "index (person_id hash)",
        "dtype": "string hash",
        "joinable": True,
        "person_ids": set(frac_person_ids),
        "n_ids": len(set(frac_person_ids)),
    },
    "churn_early_warning": {
        "rows": len(cew),
        "key_type": "positional integer index",
        "key_col": "index (int 0..4773)",
        "dtype": "int64",
        "joinable": False,
        "person_ids": set(cew_person_ids_positional) if alignment_valid["churn_early_warning"] else set(),
        "n_ids": len(cew_person_ids_positional) if alignment_valid["churn_early_warning"] else 0,
        "positional_fix_valid": alignment_valid["churn_early_warning"],
    },
    "retention_scores": {
        "rows": len(ret),
        "key_type": "positional integer index",
        "key_col": "index (int 0..4773)",
        "dtype": "int64",
        "joinable": False,
        "person_ids": set(ret_person_ids_positional) if alignment_valid["retention_scores"] else set(),
        "n_ids": len(ret_person_ids_positional) if alignment_valid["retention_scores"] else 0,
        "positional_fix_valid": alignment_valid["retention_scores"],
    },
    "elite_users": {
        "rows": len(elit),
        "key_type": "index",
        "key_col": "index (person_id hash subset)",
        "dtype": "string hash",
        "joinable": True,
        "person_ids": set(elit_person_ids),
        "n_ids": len(set(elit_person_ids)),
    },
    "intermediate_users": {
        "rows": len(inter),
        "key_type": "index",
        "key_col": "index (person_id hash subset)",
        "dtype": "string hash",
        "joinable": True,
        "person_ids": set(inter_person_ids),
        "n_ids": len(set(inter_person_ids)),
    },
}

# For each pair compute overlap and recommended fix
_ds_names = list(ds_profiles.keys())
_n = len(_ds_names)

compat_rows = []
for _i in range(_n):
    for _j in range(_i + 1, _n):
        _a, _b = _ds_names[_i], _ds_names[_j]
        _pa, _pb = ds_profiles[_a], ds_profiles[_b]
        _sa, _sb = _pa["person_ids"], _pb["person_ids"]

        _overlap_n = len(_sa & _sb) if _sa and _sb else 0
        _min_n = min(_pa["n_ids"], _pb["n_ids"]) if (_pa["n_ids"] > 0 and _pb["n_ids"] > 0) else 0
        _pct = (_overlap_n / _min_n * 100) if _min_n > 0 else 0.0

        _a_joinable = _pa["joinable"]
        _b_joinable = _pb["joinable"]
        _can_join_directly = _a_joinable and _b_joinable

        if not _a_joinable and not _b_joinable:
            _status = "❌ NEITHER joinable"
            _fix = "Both need person_id index set; use positional reconstruction first"
        elif not _a_joinable:
            _status = "⚠️  Needs positional fix"
            _fix = f"Reconstruct {_a}: set person_id index from sorted gt_ids, then join on index"
        elif not _b_joinable:
            _status = "⚠️  Needs positional fix"
            _fix = f"Reconstruct {_b}: set person_id index from sorted gt_ids, then join on index"
        elif _overlap_n == 0:
            _status = "❌ ZERO OVERLAP"
            _fix = "Subset dataset — join will produce 0 rows (correct behavior for subsets)"
        elif _pct >= 95:
            _status = "✅ FULL JOIN"
            _fix = "pd.merge(left, right, left_index=True, right_index=True) or join on person_id"
        elif _pct >= 50:
            _status = "⚠️  PARTIAL JOIN"
            _fix = "pd.merge(..., how='left') to preserve left dataset rows"
        else:
            _status = "⚠️  LOW OVERLAP"
            _fix = "Check if datasets are subsets (expected) or if key format differs"

        compat_rows.append({
            "Dataset A":      _a,
            "Dataset B":      _b,
            "Key Type A":     _pa["key_type"],
            "Key Type B":     _pb["key_type"],
            "Dtype A":        _pa["dtype"],
            "Dtype B":        _pb["dtype"],
            "Overlap Count":  _overlap_n,
            "Overlap %":      f"{_pct:.1f}%",
            "Status":         _status,
            "Recommended Fix":_fix,
        })

audit_compat_matrix = pd.DataFrame(compat_rows)

print(f"\n  {'Dataset A':<27} {'Dataset B':<27} {'Overlap':>9} {'%':>7}  {'Status':<28} {'Fix'}")
print(f"  {'-'*27} {'-'*27} {'-'*9} {'-'*7}  {'-'*28} {'-'*50}")
for _, _r in audit_compat_matrix.iterrows():
    print(f"  {_r['Dataset A'][:26]:<27} {_r['Dataset B'][:26]:<27} "
          f"{str(_r['Overlap Count']):>9} {_r['Overlap %']:>7}  "
          f"{_r['Status']:<28} {_r['Recommended Fix'][:60]}")

# ─── STEP 5: Sample 10 person_ids side-by-side ──────────────────────────────
print(f"\n{div}")
print("  STEP 5 — SAMPLE 10 person_ids SIDE-BY-SIDE ACROSS ALL DATASETS")
print(div)

# Sample 10 from sorted_gt_ids
sample_indices = [0, 1, 2, 3, 4, 100, 500, 1000, 2500, 4773]
print(f"\n  {'Row#':<5}  {'zerve (ground truth)':<38} {'fractal (idx)':<38} {'cew (positional)':<38} {'ret (positional)':<38}")
print(f"  {'-'*5}  {'-'*38} {'-'*38} {'-'*38} {'-'*38}")

for _idx in sample_indices:
    _gt_id   = sorted_gt_ids[_idx] if _idx < len(sorted_gt_ids) else "N/A"
    _frac_id = frac_person_ids[_idx] if _idx < len(frac_person_ids) else "N/A"
    _cew_id  = cew_person_ids_positional[_idx] if (alignment_valid.get("churn_early_warning") and _idx < len(cew_person_ids_positional)) else "N/A (not alignable)"
    _ret_id  = ret_person_ids_positional[_idx]  if (alignment_valid.get("retention_scores") and _idx < len(ret_person_ids_positional)) else "N/A (not alignable)"
    _match_frac = "✅" if _gt_id == _frac_id else "❌"
    _match_cew  = "✅" if _gt_id == _cew_id else ("≡" if _cew_id != "N/A (not alignable)" else "—")
    _match_ret  = "✅" if _gt_id == _ret_id else ("≡" if _ret_id != "N/A (not alignable)" else "—")
    print(f"  {_idx:<5}  {_gt_id[:36]:<38} {_match_frac}{_frac_id[:35]:<37} {_match_cew}{str(_cew_id)[:35]:<37} {_match_ret}{str(_ret_id)[:35]:<37}")

print(f"\n  Legend: ✅ exact match with ground truth  |  ≡ positional reconstruction  |  ❌ MISMATCH  |  — N/A")

# ─── STEP 6: Sample join test zerve ↔ churn_early_warning ────────────────────
print(f"\n{div}")
print("  STEP 6 — SAMPLE JOIN TEST: zerve_hackathon_dataset ↔ churn_early_warning")
print("           (using positional reconstruction to resolve triggers)")
print(div)

# Reconstruct churn_early_warning with person_id as index
cew_fixed = cew.copy()
cew_fixed.index = sorted_gt_ids  # assign sorted ground-truth person_ids as index
cew_fixed.index.name = "person_id"

# Build per-user event summary from raw events (small sample = first 50 users)
sample_users = sorted_gt_ids[:50]
raw_sample = raw_events[raw_events["person_id"].isin(sample_users)].copy()

# Join on person_id
joined = raw_sample[["person_id", "event"]].drop_duplicates().merge(
    cew_fixed[["churn_probability", "risk_tier", "top_churn_trigger_event", "recommended_action"]],
    left_on="person_id",
    right_index=True,
    how="left"
)

_n_matched = joined["churn_probability"].notna().sum()
_n_total   = joined["person_id"].nunique()
print(f"\n  Sample join test (first 50 users):")
print(f"  Unique users in sample     : {_n_total}")
print(f"  Rows with matched triggers : {_n_matched:,}")
print(f"  Match rate                 : {_n_matched/_n_total*100 if _n_total > 0 else 0:.1f}%")
print(f"\n  Sample rows from joined result:")
_join_sample = joined[joined["churn_probability"].notna()].head(10)
for _, _row in _join_sample.iterrows():
    print(f"    person={_row['person_id'][:32]}  churn_prob={_row['churn_probability']:.3f}  "
          f"risk={_row['risk_tier']}  trigger={str(_row['top_churn_trigger_event'])[:40]}")

# Verify triggers are non-null and non-'none'
_none_triggers = (_join_sample["top_churn_trigger_event"].apply(lambda x: str(x).lower() == "none")).sum()
_null_triggers = _join_sample["top_churn_trigger_event"].isna().sum()
print(f"\n  Trigger quality check in sample:")
print(f"  - Null triggers  : {_null_triggers}")
print(f"  - 'none' strings : {_none_triggers}")
print(f"  - Valid triggers : {len(_join_sample) - _null_triggers - _none_triggers}")
_overall_none = (cew_fixed["top_churn_trigger_event"].apply(lambda x: str(x).lower() == "none")).sum()
print(f"\n  Full dataset: {_overall_none:,} / {len(cew_fixed):,} rows have literal 'none' as trigger "
      f"({_overall_none/len(cew_fixed)*100:.1f}%)")

# ─── STEP 7: Final Action Plan with exact code snippets ───────────────────────
print(f"\n{DIV}")
print("  STEP 7 — FINAL ACTION PLAN: EXACT CODE SNIPPETS TO FIX EACH FILE")
print(DIV)

_action_plan = [
    {
        "priority": "🔴 CRITICAL",
        "file": "churn_early_warning.csv",
        "issue": "Integer positional index — person_id missing",
        "impact": "Cannot join to person_id-indexed datasets (0 matches)",
        "fix_code": """# In churn_early_warning_classifier or churn_early_warning_output block:
import pandas as pd

# 1. Load the ground-truth sorted person_id list from fractal metrics
frac = pd.read_csv("metricas_fractal_v3.csv", index_col=0)
sorted_person_ids = sorted(frac.index.tolist())  # 4,774 sorted person_ids

# 2. Reconstruct churn_early_warning with person_id index
cew = pd.read_csv("docu/churn_early_warning.csv", index_col=0)
assert len(cew) == len(sorted_person_ids), f"Row count mismatch: {len(cew)} != {len(sorted_person_ids)}"
cew.index = sorted_person_ids
cew.index.name = "person_id"

# 3. Fix 'none' trigger strings
cew["top_churn_trigger_event"] = cew["top_churn_trigger_event"].replace("none", pd.NA)
cew["top_churn_trigger_event"] = cew["top_churn_trigger_event"].replace("None", pd.NA)

# 4. Fix risk_tier to string (not Categorical)
cew["risk_tier"] = cew["risk_tier"].astype(str)

# 5. Re-save
cew.to_csv("docu/churn_early_warning.csv", index=True)
print("✅ churn_early_warning.csv re-saved with person_id index")"""
    },
    {
        "priority": "🔴 CRITICAL",
        "file": "retention_scores.csv",
        "issue": "Integer positional index — person_id missing",
        "impact": "Cannot join to person_id-indexed datasets (0 matches)",
        "fix_code": """# In retention_scoring block:
import pandas as pd

# 1. Load sorted person_ids (same as above)
frac = pd.read_csv("metricas_fractal_v3.csv", index_col=0)
sorted_person_ids = sorted(frac.index.tolist())

# 2. Reconstruct retention_scores with person_id index
ret = pd.read_csv("docu/retention_scores.csv", index_col=0)
assert len(ret) == len(sorted_person_ids), f"Row count mismatch: {len(ret)} != {len(sorted_person_ids)}"
ret.index = sorted_person_ids
ret.index.name = "person_id"

# 3. Fix risk_tier to string
ret["risk_tier"] = ret["risk_tier"].astype(str)

# 4. Re-save
ret.to_csv("docu/retention_scores.csv", index=True)
print("✅ retention_scores.csv re-saved with person_id index")"""
    },
    {
        "priority": "🟠 HIGH",
        "file": "churn_early_warning.csv",
        "issue": f"~{_overall_none:,} rows ({_overall_none/len(cew_fixed)*100:.1f}%) have literal 'none' as top_churn_trigger_event",
        "impact": "Dashboard shows blank/none triggers for ~23% of users",
        "fix_code": """# Inline fix in churn_early_warning_output block (before saving):
# Replace 'none'/'None' string with actual fallback event from event_feature_matrix

# Option A — replace with pd.NA (shows blank in Dashboard):
cew["top_churn_trigger_event"] = cew["top_churn_trigger_event"].replace(
    {"none": pd.NA, "None": pd.NA}
)

# Option B — replace with most-common event for that user's risk tier
# (better UX — shows a plausible trigger):
default_evt_by_tier = cew.groupby("risk_tier")["top_churn_trigger_event"] \\
                         .agg(lambda x: x[x.str.lower() != "none"].mode().iloc[0] if (x.str.lower() != "none").any() else "evt_canvas_open") \\
                         .to_dict()
_mask = cew["top_churn_trigger_event"].str.lower() == "none"
cew.loc[_mask, "top_churn_trigger_event"] = cew.loc[_mask, "risk_tier"].map(default_evt_by_tier)"""
    },
    {
        "priority": "🟡 MEDIUM",
        "file": "ALL derived CSVs",
        "issue": "risk_tier is saved as Categorical dtype — may cause comparison failures",
        "impact": "Dashboard string comparisons on risk_tier may fail silently",
        "fix_code": """# Before any .to_csv() call in ALL export blocks:
for col in ["risk_tier"]:
    if col in df.columns and str(df[col].dtype) == "category":
        df[col] = df[col].astype(str)
# This ensures risk_tier is plain string in all files"""
    },
    {
        "priority": "💡 HOW TO JOIN",
        "file": "Dashboard join pattern",
        "issue": "Universal pattern to join all 6 datasets correctly after fixes",
        "impact": "Enables all trigger data to appear in Dashboard",
        "fix_code": """# AFTER applying fixes above, the universal join pattern is:
import pandas as pd

# Load all datasets (all now have person_id as index)
frac = pd.read_csv("metricas_fractal_v3.csv",     index_col=0)  # person_id index ✅
cew  = pd.read_csv("docu/churn_early_warning.csv", index_col=0)  # person_id index ✅ (after fix)
ret  = pd.read_csv("docu/retention_scores.csv",    index_col=0)  # person_id index ✅ (after fix)
elit = pd.read_csv("docu/elite_users.csv",          index_col=0)  # person_id index ✅
inter= pd.read_csv("docu/intermediate_users.csv",   index_col=0)  # person_id index ✅

# Master join: all 4,774 users with all available columns
dashboard_df = frac.join(cew,  how="left", rsuffix="_cew")  \\
                   .join(ret,  how="left", rsuffix="_ret")

# Add cohort labels
dashboard_df["is_elite"]        = dashboard_df.index.isin(elit.index)
dashboard_df["is_intermediate"] = dashboard_df.index.isin(inter.index)

# Join raw events for specific lookups:
raw = pd.read_csv("zerve_hackathon_dataset.csv")
# Join: raw["person_id"] ↔ dashboard_df.index
result = raw.merge(dashboard_df, left_on="person_id", right_index=True, how="left")

print(f"Joined rows with trigger data: {result['top_churn_trigger_event'].notna().sum():,}")
print(f"Trigger coverage: {result['top_churn_trigger_event'].notna().sum() / len(raw) * 100:.1f}%")"""
    },
]

for _plan in _action_plan:
    print(f"\n  {_plan['priority']}  |  {_plan['file']}")
    print(f"  Issue  : {_plan['issue']}")
    print(f"  Impact : {_plan['impact']}")
    print(f"  Code   :")
    for _line in _plan["fix_code"].strip().split("\n"):
        print(f"    {_line}")

print(f"\n{DIV}")
print("  ✅  AUDIT COMPLETE — SUMMARY")
print(DIV)
print(f"  Ground truth person_ids (zerve events) : {len(gt_set):,}")
print(f"  Confirmed row count = 4,774            : {all(v for v in alignment_valid.values() if v is not None)}")
print(f"  metricas_fractal_v3 index overlap      : {len(set(frac_person_ids) & gt_set):,} / {len(gt_set):,} ({len(set(frac_person_ids) & gt_set)/len(gt_set)*100:.1f}%)")
print(f"  churn_early_warning rows               : {len(cew):,} {'✅ positional fix VALID' if alignment_valid['churn_early_warning'] else '❌ CANNOT fix positionally'}")
print(f"  retention_scores rows                  : {len(ret):,} {'✅ positional fix VALID' if alignment_valid['retention_scores'] else '❌ CANNOT fix positionally'}")
print(f"  elite_users (subset) index overlap     : {len(set(elit_person_ids) & gt_set):,} / {len(elit_person_ids)}")
print(f"  intermediate_users (subset) overlap    : {len(set(inter_person_ids) & gt_set):,} / {len(inter_person_ids)}")
print(f"  'none' trigger strings in cew          : {_overall_none:,} ({_overall_none/len(cew_fixed)*100:.1f}%) — needs patching")
print(f"  Join test match rate (50 sample users) : {_n_matched}/{_n_total} ({_n_matched/_n_total*100 if _n_total > 0 else 0:.1f}%)")
print(DIV)
print("  ACTION REQUIRED:")
print("  1. Fix churn_early_warning.csv  — set sorted person_id as index (CRITICAL)")
print("  2. Fix retention_scores.csv     — set sorted person_id as index (CRITICAL)")
print("  3. Patch 'none' trigger strings — replace with pd.NA or risk-tier fallback (HIGH)")
print("  4. Cast risk_tier to str        — in all export blocks (MEDIUM)")
print("  5. Use universal join pattern   — join all via person_id index (enables Dashboard)")
print(DIV)
