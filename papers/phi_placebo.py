"""
Placebo control for the apparent φ signal.
The φ targets tile [0.4,1.6] densely; data concentrated there will hit them
regardless of φ. Correct test: keep the DATA fixed, replace the 6 φ-targets
with 6 RANDOM targets (same range, same ±0.10), 10000 times. If φ is special,
the data's φ-hit-rate should exceed most random target-sets.
"""
import numpy as np, pandas as pd
from pathlib import Path
PHI = (1+5**0.5)/2
TARGETS = np.array([PHI/4, PHI/3, PHI/2, 2*PHI/3, 3*PHI/4, PHI])
TOL = 0.10
ROOT = Path("/home/user/The-shadow-Node-Theory")
rng = np.random.default_rng(7)


def hit(vals, targets):
    return np.mean([np.any(np.abs(v-targets) <= TOL) for v in vals])


def placebo(vals, label):
    vals = np.asarray(vals, float); vals = vals[np.isfinite(vals)]
    lo, hi = vals.min(), vals.max()
    obs = hit(vals, TARGETS)
    # random 6-target sets drawn from the data's own range
    rand = np.array([hit(vals, rng.uniform(lo, hi, len(TARGETS)))
                     for _ in range(10000)])
    p = (np.sum(rand >= obs) + 1) / (len(rand) + 1)
    print(f"\n[{label}] n={len(vals)}, range [{lo:.2f},{hi:.2f}]")
    print(f"  φ-targets hit rate: {obs*100:.1f}%")
    print(f"  random 6-target sets: mean {rand.mean()*100:.1f}%  "
          f"median {np.median(rand)*100:.1f}%  "
          f"95th pct {np.percentile(rand,95)*100:.1f}%")
    print(f"  p(random >= φ) = {p:.3f}  -> "
          f"{'φ IS special' if p < 0.05 else 'φ NOT special (artifact of band coverage)'}")


df = pd.read_csv(ROOT/"reconstruction_real/data/snt_corpus_REAL_v5.csv")
placebo(df.loc[df.b > 0, "b"].values, "corpus 721 b>0")
placebo(df[df.dominio.isin(["E1", "E3"]) & (df.b > 0)]["b"].values,
        "friction-free bio (E1,E3) b>0")
