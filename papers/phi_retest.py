"""
Re-test H-φ on CURRENT data:
 (A) the 721-case corpus satellization exponents b>0 (the original claim),
 (B) NEW: the collapse exponents Δ (ACO absorption + crypto), not tested before.
H-φ predicts b clusters within ±0.10 of {φ/4, φ/3, φ/2, 2φ/3, 3φ/4, φ} above chance.
"""
import numpy as np, pandas as pd
from pathlib import Path

PHI = (1 + 5**0.5) / 2
TARGETS = np.array([PHI/4, PHI/3, PHI/2, 2*PHI/3, 3*PHI/4, PHI])
TOL = 0.10
ROOT = Path("/home/user/The-shadow-Node-Theory")
rng = np.random.default_rng(42)


def near_phi(vals):
    vals = np.asarray(vals, float)
    return np.array([np.any(np.abs(v - TARGETS) <= TOL) for v in vals])


def test(vals, label):
    vals = np.asarray(vals, float)
    vals = vals[np.isfinite(vals)]
    if len(vals) < 5:
        print(f"\n[{label}] n={len(vals)} — too few"); return
    obs = near_phi(vals).mean()
    lo, hi = vals.min(), vals.max()
    # Monte Carlo: uniform over observed range
    sims = []
    for _ in range(5000):
        s = rng.uniform(lo, hi, len(vals))
        sims.append(near_phi(s).mean())
    sims = np.array(sims)
    exp = sims.mean()
    p = (np.sum(sims >= obs) + 1) / (len(sims) + 1)
    print(f"\n[{label}] n={len(vals)}, range [{lo:.2f},{hi:.2f}]")
    print(f"  near φ-fraction (±0.10): observed {obs*100:.1f}%  "
          f"| expected by chance {exp*100:.1f}% (IC ~[{np.percentile(sims,2.5)*100:.1f},"
          f"{np.percentile(sims,97.5)*100:.1f}])")
    print(f"  p(obs >= chance) = {p:.3f}  -> "
          f"{'SIGNAL' if p < 0.05 else 'no signal (consistent with chance)'}")


print(f"φ = {PHI:.4f} | targets = {np.round(TARGETS,3)}")

# (A) corpus b>0
df = pd.read_csv(ROOT / "reconstruction_real/data/snt_corpus_REAL_v5.csv")
bpos = df.loc[df["b"] > 0, "b"].values
test(bpos, "A: corpus 721 — satellization b>0")

# also b>0 of friction-free domains only (E1,E3 = the H-φ's intended regime)
ff = df[df["dominio"].isin(["E1", "E3"]) & (df["b"] > 0)]["b"].values
test(ff, "A': friction-free bio (E1,E3) b>0 — H-φ's intended regime")

# (B) NEW collapse exponents Δ
aco = pd.read_csv(ROOT / "reconstruction_real/data/snt_corpus_aco_v29.csv")
test(aco["b"].values, "B: ACO absorption exponents Δ (18)")

orth = pd.read_csv(ROOT / "reconstruction_real/data/orthogonality_crypto_v25.csv")
test(np.abs(orth["delta_fall"].values), "B': |crypto fall exponents| (11)")
test(orth["b_rise"].values, "B'': crypto rise exponents b (11)")
