"""
Operationalizing institutional friction (roadmap item #1).
Controlled within-domain test: 2008 financial cohort (same domain, same
month units). Friction = documented degree of regulatory pre-arrangement of
the resolution channel, ordinal 1..6 (6 = most institutional friction).
Test: does friction predict the collapse exponent Delta and the absorption time?
"""
import numpy as np
from scipy.stats import spearmanr, pearsonr

# case: (friction_rank, resolution_channel, Delta, time_to_90_hours)
# friction_rank: 6 = most pre-arranged/regulated ... 1 = disorderly, no resolution
cohort = {
    "Washington Mutual": (6, "FDIC receivership (P&A)",        0.009,    21),
    "Bear Stearns":      (5, "Fed-brokered (Maiden Lane)",     0.043,   626),
    "Chrysler":          (4, "Govt-managed (TARP / §363)",     0.138, 16071),
    "Wachovia":          (3, "FDIC-assisted open-bank",        0.153,  4140),
    "Merrill Lynch":     (2, "Pressured private merger",       0.217,  7122),
    "Lehman Brothers":   (1, "Disorderly Chapter 11 (none)",   0.246, 30681),
}

names = list(cohort)
F   = np.array([cohort[n][0] for n in names], float)
D   = np.array([cohort[n][2] for n in names], float)
Th  = np.array([cohort[n][3] for n in names], float)

print("Operationalized friction vs collapse — 2008 financial cohort (n=6)")
print("=" * 70)
print(f"{'case':<20}{'friction':>9}{'channel':>30}{'Delta':>8}")
for n in sorted(names, key=lambda k: -cohort[k][0]):
    fr, ch, d, t = cohort[n]
    print(f"{n:<20}{fr:>9}{ch:>30}{d:>8.3f}")

rho_d, p_d = spearmanr(F, D)
rho_t, p_t = spearmanr(F, np.log(Th))
print("\nFriction (1..6) vs collapse exponent Delta:")
print(f"  Spearman rho = {rho_d:+.3f}  (p = {p_d:.4f}, n=6)")
print("  -> higher friction predicts SMALLER Delta (faster, front-loaded absorption)")
print("\nFriction (1..6) vs log time-to-90% absorption:")
print(f"  Spearman rho = {rho_t:+.3f}  (p = {p_t:.4f}, n=6)")

# also Pearson on log-time as robustness
rho_tp, p_tp = pearsonr(F, np.log(Th))
print(f"  Pearson(F, log time) = {rho_tp:+.3f} (p={p_tp:.4f})")

print("\nInterpretation:")
print("  Within a single domain/units, the documented degree of regulatory")
print("  pre-arrangement is a measurable ordinal that tracks the collapse")
print("  exponent. This operationalizes 'friction governs the shape of Delta'")
print("  as a testable, falsifiable claim (RC-Delta2 / RC-Delta4).")

# Cross-domain friction TIERS (descriptive — confounded, for the mode map)
print("\n" + "=" * 70)
print("Cross-domain friction tiers vs collapse mode (descriptive)")
print("=" * 70)
tiers = [
    ("Astro (flare/TDE)",      "physical-high (viscosity/cooling)", "Regulated"),
    ("Finance 2008",           "institutional-high",                "Regulated"),
    ("History (Rome/USSR)",    "institutional",                     "Regulated"),
    ("Crypto EOS (gradual)",   "~0",                                "Cracquelure"),
    ("Crypto FTX (abrupt)",    "~0 (+ floor)",                      "Floor-Arrested"),
    ("Crypto LUNA (abrupt)",   "~0 (no floor)",                     "Catastrophic Cliff"),
    ("Biology Delta->Omicron", "bounded magnitude",                 "Logistic Sweep"),
]
for dom, fr, mode in tiers:
    print(f"  {dom:<24} friction={fr:<32} -> {mode}")
