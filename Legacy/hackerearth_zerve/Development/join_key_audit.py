
import pandas as pd
import numpy as np

# ══════════════════════════════════════════════════════════════════════════════
#  JOIN KEY AUDIT — Deep cross-dataset join compatibility matrix
#  Files: zerve_hackathon_dataset.csv, metricas_fractal_v3.csv,
#         docu/churn_early_warning.csv, docu/retention_scores.csv,
#         docu/elite_users.csv, docu/intermediate_users.csv
# ══════════════════════════════════════════════════════════════════════════════

DIV = "═" * 80
div = "─" * 80

# ─── 1. Load all 6 files ─────────────────────────────────────────────────────
print(DIV)
print("  📂  LOADING ALL 6 FILES")
print(DIV)

files = {
    "zerve_hackathon_dataset": ("zerve_hackathon_dataset.csv", {}),
    "metricas_fractal_v3":     ("metricas_fractal_v3.csv",     {"index_col": 0}),
    "churn_early_warning":     ("docu/churn_early_warning.csv",{"index_col": 0}),
    "retention_scores":        ("docu/retention_scores.csv",   {"index_col": 0}),
    "elite_users":             ("docu/elite_users.csv",        {"index_col": 0}),
    "intermediate_users":      ("docu/intermediate_users.csv", {"index_col": 0}),
}

dfs = {}
for name, (path, kwargs) in files.items():
    dfs[name] = pd.read_csv(path, **kwargs)
    print(f"  ✅  {name:<30} → {dfs[name].shape[0]:>7,} rows × {dfs[name].shape[1]:>3} cols")

# ─── 2. Column names & dtypes for ALL files ──────────────────────────────────
print(f"\n{DIV}")
print("  📋  COLUMN NAMES & DTYPES — ALL FILES")
print(DIV)

for name, df in dfs.items():
    print(f"\n  ┌── {name}  ({df.shape[0]:,} rows × {df.shape[1]} cols)")
    print(f"  │   Index: name='{df.index.name}' dtype={df.index.dtype}  "
          f"is_int={pd.api.types.is_integer_dtype(df.index)}")
    for col in df.columns:
        print(f"  │     • {col:<50} {str(df[col].dtype)}")
    print(f"  └{'─'*60}")

# ─── 3. Candidate join keys in each file ─────────────────────────────────────
print(f"\n{DIV}")
print("  🔑  CANDIDATE JOIN KEY IDENTIFICATION")
print(DIV)

# Define what key is available in each dataset and WHERE it lives
KEY_PROFILE = {}
for name, df in dfs.items():
    profile = {
        "has_person_id_col":  "person_id" in df.columns,
        "has_user_id_col":    "user_id"   in df.columns,
        "index_name":         df.index.name,
        "index_dtype":        str(df.index.dtype),
        "index_is_int":       pd.api.types.is_integer_dtype(df.index),
        "index_is_str":       df.index.dtype == object,
        "n_rows":             len(df),
        "index_unique":       df.index.nunique(),
        "index_sample":       list(df.index[:5]),
    }
    # Determine primary candidate key
    if profile["has_person_id_col"]:
        profile["primary_key"] = "person_id (column)"
        profile["key_values"]  = df["person_id"]
    elif profile["index_is_str"] and not profile["index_is_int"]:
        profile["primary_key"] = f"index (string/hash, name='{df.index.name}')"
        profile["key_values"]  = pd.Series(df.index)
    elif profile["index_is_int"]:
        profile["primary_key"] = "index (INTEGER — positional, NOT a join key)"
        profile["key_values"]  = pd.Series([], dtype=str)  # can't join on positional int
    else:
        profile["primary_key"] = "UNKNOWN"
        profile["key_values"]  = pd.Series([], dtype=str)
    KEY_PROFILE[name] = profile

for name, p in KEY_PROFILE.items():
    icon = "✅" if "person_id (column)" in p["primary_key"] or "string" in p["primary_key"] else "❌"
    print(f"\n  {icon}  {name}")
    print(f"       Primary key    : {p['primary_key']}")
    print(f"       Index dtype    : {p['index_dtype']}  is_int={p['index_is_int']}  is_str={p['index_is_str']}")
    print(f"       Unique keys    : {p['index_unique']:,} / {p['n_rows']:,} rows")
    print(f"       person_id col  : {'YES' if p['has_person_id_col'] else 'NO ❌'}")
    print(f"       user_id col    : {'YES' if p['has_user_id_col']   else 'NO'}")

# ─── 4. Dtype compatibility + 5. Index type detection ────────────────────────
print(f"\n{DIV}")
print("  🔬  DTYPE COMPATIBILITY & INDEX TYPE ANALYSIS")
print(DIV)

# Collect the join key series for each dataset
key_series = {}
key_dtype_label = {}
for name, p in KEY_PROFILE.items():
    kv = p["key_values"].dropna().astype(str).str.strip()
    key_series[name] = set(kv)
    # Detect key format
    sample = list(kv[:10])
    all_numeric = all(v.isdigit() for v in sample if v)
    all_hash    = all(len(v) > 20 for v in sample if v)
    if p["index_is_int"] and not p["has_person_id_col"]:
        key_dtype_label[name] = "INTEGER positional idx (NOT joinable)"
    elif all_hash:
        key_dtype_label[name] = "string hash/UUID"
    elif all_numeric:
        key_dtype_label[name] = "numeric string"
    else:
        key_dtype_label[name] = "mixed/other string"

print(f"\n  {'Dataset':<30} {'Key Location':<35} {'Key Format':<30}")
print(f"  {'-'*30} {'-'*35} {'-'*30}")
for name, p in KEY_PROFILE.items():
    loc = p["primary_key"].split("(")[0].strip()
    fmt = key_dtype_label[name]
    print(f"  {name:<30} {loc:<35} {fmt:<30}")

# ─── 6. Sample 5 key values side-by-side ─────────────────────────────────────
print(f"\n{DIV}")
print("  🔍  SAMPLE 5 KEY VALUES — SIDE-BY-SIDE")
print(DIV)

dsnames = list(dfs.keys())
samples = {}
for name, p in KEY_PROFILE.items():
    kv = p["key_values"].dropna().astype(str).str.strip()
    samples[name] = list(kv[:5])

max_rows = max(len(v) for v in samples.values())
print(f"\n  {'#':<4}", end="")
for name in dsnames:
    print(f"  {name[:28]:<30}", end="")
print()
print(f"  {'-'*4}", end="")
for _ in dsnames:
    print(f"  {'-'*30}", end="")
print()

for i in range(max_rows):
    print(f"  {i+1:<4}", end="")
    for name in dsnames:
        val = samples[name][i] if i < len(samples[name]) else "—"
        print(f"  {str(val)[:28]:<30}", end="")
    print()

# ─── 4. Exact match overlap counts between each pair ─────────────────────────
print(f"\n{DIV}")
print("  📊  EXACT MATCH OVERLAP COUNTS — ALL PAIRS")
print(DIV)

names = list(dfs.keys())
n = len(names)

# Build matrix
overlap_matrix = {}
for i in range(n):
    for j in range(n):
        a, b = names[i], names[j]
        sa, sb = key_series[a], key_series[b]
        if len(sa) == 0 or len(sb) == 0:
            overlap_matrix[(a, b)] = -1  # -1 = not joinable
        else:
            overlap_matrix[(a, b)] = len(sa & sb)

# Print matrix header
col_w = 14
print(f"\n  {'':30}", end="")
for name in names:
    short = name[:col_w-1]
    print(f"  {short:>{col_w}}", end="")
print()
print(f"  {'':30}  " + ("─" * (col_w+2)) * n)

for a in names:
    print(f"  {a[:28]:<30}", end="")
    for b in names:
        v = overlap_matrix[(a, b)]
        if v == -1:
            cell = "N/A"
        elif a == b:
            cell = f"({len(key_series[a]):,})"
        else:
            cell = f"{v:,}"
        print(f"  {cell:>{col_w}}", end="")
    print()

# ─── 7. Zero-overlap flags + root cause ──────────────────────────────────────
print(f"\n{DIV}")
print("  🚨  ZERO-OVERLAP FLAGS & ROOT CAUSE ANALYSIS")
print(DIV)

zero_pairs = []
partial_pairs = []
perfect_pairs = []

for i in range(n):
    for j in range(i+1, n):
        a, b = names[i], names[j]
        v = overlap_matrix[(a, b)]
        sa, sb = key_series[a], key_series[b]
        total_a, total_b = len(sa), len(sb)
        if v == -1:
            # Not joinable because one or both have positional int index
            zero_pairs.append((a, b, -1, total_a, total_b,
                "One or both datasets use INTEGER positional index (not a real key). "
                "Cannot join — index values represent row positions, not user IDs."))
        elif v == 0:
            # Joinable key type but zero overlap — investigate
            # Check key format mismatch
            fmt_a = key_dtype_label[a]
            fmt_b = key_dtype_label[b]
            if fmt_a != fmt_b:
                reason = f"Key format mismatch: '{a}' has {fmt_a} vs '{b}' has {fmt_b}"
            else:
                # Same format, check sample values
                sa5 = list(sa)[:3]
                sb5 = list(sb)[:3]
                reason = f"No overlapping IDs despite compatible dtypes. Sample A={sa5[:2]}, B={sb5[:2]}"
            zero_pairs.append((a, b, 0, total_a, total_b, reason))
        else:
            pct = v / min(total_a, total_b) * 100 if min(total_a, total_b) > 0 else 0
            if pct >= 95:
                perfect_pairs.append((a, b, v, total_a, total_b, pct))
            else:
                partial_pairs.append((a, b, v, total_a, total_b, pct))

if zero_pairs:
    print(f"\n  ❌  ZERO / NOT-JOINABLE PAIRS:")
    for a, b, v, ta, tb, reason in zero_pairs:
        label = "NOT-JOINABLE (positional int)" if v == -1 else "ZERO OVERLAP"
        print(f"\n    ● {a}  ↔  {b}")
        print(f"      Status  : {label}")
        print(f"      Keys A  : {ta:,}   Keys B  : {tb:,}   Overlap: {'N/A' if v==-1 else v}")
        print(f"      Reason  : {reason}")

if partial_pairs:
    print(f"\n  ⚠️   PARTIAL OVERLAP PAIRS:")
    for a, b, v, ta, tb, pct in partial_pairs:
        print(f"\n    ● {a}  ↔  {b}")
        print(f"      Overlap : {v:,} / min({ta:,}, {tb:,}) = {pct:.1f}%")

if perfect_pairs:
    print(f"\n  ✅  HIGH/FULL OVERLAP PAIRS (≥95%):")
    for a, b, v, ta, tb, pct in perfect_pairs:
        print(f"    ● {a}  ↔  {b}   → {v:,} matching IDs  ({pct:.1f}%)")

# ─── FINAL JOIN COMPATIBILITY MATRIX (summary) ───────────────────────────────
print(f"\n{DIV}")
print("  📋  JOIN COMPATIBILITY MATRIX — FINAL SUMMARY")
print(DIV)

matrix_rows = []
for i in range(n):
    for j in range(i+1, n):
        a, b = names[i], names[j]
        v = overlap_matrix[(a, b)]
        sa, sb = key_series[a], key_series[b]
        ta, tb = len(sa), len(sb)

        if v == -1:
            status     = "❌ NOT JOINABLE"
            overlap    = "N/A"
            pct_str    = "—"
            root_cause = "Integer positional index ≠ person_id"
        elif v == 0:
            status     = "❌ ZERO OVERLAP"
            overlap    = "0"
            pct_str    = "0.0%"
            fmt_a = key_dtype_label[a]
            fmt_b = key_dtype_label[b]
            root_cause = f"Format mismatch or disjoint ID spaces ({fmt_a} vs {fmt_b})"
        else:
            pct = v / min(ta, tb) * 100 if min(ta, tb) > 0 else 0
            overlap    = f"{v:,}"
            pct_str    = f"{pct:.1f}%"
            if pct >= 95:
                status = "✅ FULL JOIN"
            elif pct >= 50:
                status = "⚠️  PARTIAL JOIN"
            else:
                status = "⚠️  LOW OVERLAP"
            root_cause = "—"

        matrix_rows.append({
            "Dataset A":       a,
            "Dataset B":       b,
            "Key A":           KEY_PROFILE[a]["primary_key"].split("(")[0].strip(),
            "Key B":           KEY_PROFILE[b]["primary_key"].split("(")[0].strip(),
            "Dtype A":         key_dtype_label[a],
            "Dtype B":         key_dtype_label[b],
            "Dtype Match":     "✅" if key_dtype_label[a] == key_dtype_label[b] else "❌",
            "Overlap Count":   overlap,
            "Overlap %":       pct_str,
            "Status":          status,
            "Root Cause":      root_cause,
        })

join_compat_matrix = pd.DataFrame(matrix_rows)
print(join_compat_matrix.to_string(index=False))

print(f"\n{DIV}")
print(f"  ✅  JOIN KEY AUDIT COMPLETE")
total_pairs = len(matrix_rows)
not_joinable = sum(1 for r in matrix_rows if "NOT JOINABLE" in r["Status"])
zero_ov      = sum(1 for r in matrix_rows if "ZERO" in r["Status"])
full_join    = sum(1 for r in matrix_rows if "FULL" in r["Status"])
partial_join = sum(1 for r in matrix_rows if "PARTIAL" in r["Status"] or "LOW" in r["Status"])
print(f"  Total pairs     : {total_pairs}")
print(f"  ✅  Full joins  : {full_join}")
print(f"  ⚠️   Partial     : {partial_join}")
print(f"  ❌  Not joinable: {not_joinable}")
print(f"  ❌  Zero overlap: {zero_ov}")
print(DIV)
