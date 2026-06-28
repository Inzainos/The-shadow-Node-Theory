# Shadow Node Theory — Theoretical Framework v30

**Elán Zainos Corona** · Fractal Core Research, Tlaxcala, Mexico
ORCID: 0009-0009-9125-253X · June 2026

SSRN 6418778 · Zenodo 10.5281/zenodo.19446521 · github.com/Inzainos/The-shadow-Node-Theory

*English translation of `marco_teorico_v30.md`. Full content, including the
complete restored body (Annex A).*

---

## Note on this version (v30)

v30 consolidates v29 (corpus of 721 real cases, June 2026) and **integrates as a
central layer** the most recent theoretical development: the **Coupled Orbital
Collapse Architecture (ACO-A)**, reformulated as a **universal, transversal
layer** of the framework, not a separate module. Changes relative to v29:

- **New Part IV — Coupled Orbital Collapse layer.** Collapse goes from being a
  module of 18 socioeconomic cases to an **orthogonal axis (Δ)** coupled to all
  of SNT, with evidence across **five domains** (finance, history, crypto,
  biology, astronomy) using real data.
- **Law of Collapse Inevitability** in falsifiable form: `h(τ) > 0`.
- **Taxonomy of collapse modes** governed by *friction × trigger ×
  (floor/ceiling)*, and the **Principle of Least Friction** as the unifier.
- **Four roadmap results** already executed with real data (friction
  operationalized, orthogonality b⊥Δ, unbounded biology, hazard).
- **φ hypothesis updated:** closed after **4 rounds** (the 4th with a placebo
  control); still refuted and now methodologically stronger.

> Obsolescence note (inherited from v29): the v28 framework and any documents
> citing 502 cases must be considered an **obsolete version** in their
> statistical figures. The 502-case corpus contained ~188 synthetic `b` values
> (`np.random.normal()`) and impossible R² (down to −7.332). Those values were
> never published as final. v29/v30 documents the complete reconstruction with
> real primary data.

---

## Executive summary of the change

|                          | v28 (obsolete) | v29           | v30 (current)                    |
|--------------------------|----------------|---------------|----------------------------------|
| Cases (b axis)           | 502            | 721           | 721                              |
| Data                     | synthetic      | REAL          | REAL                             |
| Significant              | 31%            | 89%           | 89%                              |
| Corrupt R²               | ~99            | 0             | 0                                |
| Spearman ρ (friction→b)  | −0.74 (inflated)| −0.68 (n=714)| −0.68 (n=714), p=2.5×10⁻⁹⁷       |
| Central test             | not verifiable | p=2.4×10⁻⁷⁴   | p=2.4×10⁻⁷⁴                      |
| Collapse layer (Δ)       | separate module| separate module| **orthogonal axis, 5 domains**  |
| Hazard h(τ)              | —              | —             | **estimated (crypto, n=41)**     |
| H-φ                      | untested       | refuted (3)   | **refuted (4 rounds + placebo)** |
| Traceable to source      | NO             | YES           | YES (public GitHub)              |

---

# PART I — Theoretical foundations

## 1.0 Central claim

The universe operates as a network of networks at macro, meso and micro scales,
governed by the same organizing algorithm. Complex systems at all scales share
the scale-free network topology, suggesting a common underlying physical
principle. Shadow Node Theory demonstrates this principle with verifiable
quantitative data.

**Certainty levels:**

| Level | Content | Status |
|-------|---------|--------|
| 1 | Shared topology across multiple scales (Barabási, IllustrisTNG, SDSS) | DEMONSTRATED |
| 2 | SNT: satellization as a power law; friction predicts b (p=2.4×10⁻⁷⁴); 100% real, reproducible corpus | VERIFIED (721 cases) |
| 2★ | **Collapse as a transversal layer (Δ axis): regular modes across 5 domains** | **VERIFIED / STRONG HYPOTHESIS (Part IV)** |
| 3 | Inter-brain synchronization as a collective field (BrainNet, Waseda, Dartmouth) | ACTIVE HYPOTHESIS |
| 3 | Microtubules as information decoders (Penrose-Hameroff, Orch-OR) | ACTIVE HYPOTHESIS |
| 4 | Dark matter as a universal connective substrate | OPEN FRONTIER |

## 1.1 Formal definition

For two coupled entities with a dominant hub and a peripheral node, the dominance
ratio at time t is:

    R(t) = metric_hub(t) / metric_node(t)

SNT posits that, in the absence of institutional friction, this ratio follows a
power law:

    R(t) = a · t^b   ⟺   log R(t) = log a + b · log t

where **b** is the satellization exponent.

**Interpretation of the exponent b:**

- b < 0 → convergence (the node gains relative ground)
- b ≈ 0 → dynamic equilibrium
- 0 < b < 1 → sublinear satellization (gradual)
- b ≥ 1 → superlinear satellization (accelerated)

**Roche Radius (b = 1.0):** critical threshold. A node with b ≥ 1 is in
accelerated absorption — analogous to the astronomical Roche radius (the distance
within which tidal forces overcome the satellite's cohesion).

**Note (v29):** the exponent b is a **descriptive metric** of the speed and
direction of satellization, not a claim that the power law is the only generative
model in all domains. In systems with high institutional friction (national
economies), exponential and linear models compete with the power law at the
100-year scale. The power law emerges as the best description where friction is
low (epidemics, biological invasions).

---

# PART II — Corpus v30 (721 real cases)

## 2.0 Reconstruction methodology

For each case: (1) obtain primary time series from documented sources; (2)
compute R(t) = metric_hub(t)/metric_node(t); (3) OLS fit in log-log; (4) record
b, real R² ∈ [0,1], p-value, 95% CI, Durbin-Watson; (5) verify no R² is negative
or greater than 1. The entire corpus is reproducible from `reconstruction_real/`.

## 2.1 Corpus by domain

| Domain | Friction | Cases | Sig. | b̄ | R̄² | Source |
|--------|----------|-------|------|------|------|--------|
| A  | medium | 4   | 0%   | +0.082 | 0.18 | UN Demographic Yearbook |
| B  | high   | 446 | 84%  | +0.092 | 0.35 | Maddison 2020 |
| C  | high   | 24  | 100% | +0.091 | 0.53 | INEGI + US Census |
| D  | low    | 3   | 100% | −1.364 | 0.87 | HackerEarth 2026 |
| E1 | none   | 4   | 100% | +2.891 | 0.81 | OWID COVID (spatial) |
| E2 | high   | 2   | 50%  | +0.145 | 0.12 | MacLulich/Elton |
| E3 | none   | 234 | 100% | +0.912 | 0.85 | JHU COVID-19 |
| F1 | medium | 2   | 100% | −1.807 | 0.40 | Open Exoplanet Catalogue |
| F2 | medium | 1   | 100% | +1.273 | 0.48 | Open Exoplanet Catalogue |
| F3 | low    | 1   | 100% | +1.264 | 0.90 | Open Exoplanet Catalogue |
| **TOTAL** | | **721** | **89%** | **+0.366** | **0.58** | |

Integrity: R²<0: 0 cases · R²>1: 0 cases · invalid p: 0 cases · every b
reproducible from public scripts.

## 2.2 Institutional friction index

Ordinal scale 0–3, assigned a priori (before computing the b values):

- **3 — High:** national economies (B), subnational hierarchies (C),
  predator-prey systems (E2, mutual interdependence).
- **2 — Medium:** historical cities (A), planetary/stellar systems (F1, F2;
  orbital resonance / radiative limits).
- **1 — Low:** digital ecosystems (D), multiplanetary hierarchies (F3).
- **0 — None:** biological invasion (E1), epidemic growth (E3).

---

# PART III — Main findings (satellization axis)

**Finding 1 — Friction predicts satellization.** Spearman correlation between the
friction index and b per case (social/biological domains, n=714):
**ρ = −0.68, p = 2.5×10⁻⁹⁷.** The higher the institutional friction, the lower
the exponent.

**Finding 2 — Regime separation.** Friction-free biology (E1+E3): b̄ = +0.95.
Friction-laden economics (A+B+C): b̄ = +0.09. **Mann-Whitney U = 103,538,
p = 2.4×10⁻⁷⁴.** Systems with no institutional brake satellize ~10× faster.

**Finding 3 — Mechanistic equivalence.** Political sovereignty (B: b̄=+0.09) and
mutual ecological interdependence (E2: b̄=+0.14) are statistically
indistinguishable: two distinct mechanisms act as equivalent brakes.

**Finding 4 — Modeling regimes.** The power law is the best description where
friction is low (E3: 6/8 cases; E1: consistent b>1). Under high friction (B):
power law best in only ~8%, exponential ~49%, linear ~35%. The power-law regime
emerges where the theory predicts free satellization.

**Finding 5 — Atomic Sovereignty Index (ASI).** Validation on HackerEarth 2026
(n=4,771 real users): ROC-AUC train=0.719, test=0.697 (no overfitting); 5-Event
Wall: churn 93% (1 type) → 74% (≥5 types); absorption zone (<0.10) 88% churn;
parity (0.10–1.0) 73%; sovereign (≥1.0) 34%.

---

# PART IV — Coupled Orbital Collapse layer (ACO-A)

*Collapse as a universal orthogonal axis. Evidence across 5 domains with real data.*

## 4.0 Thesis

The Orbital Collapse Architecture ceases to be a separate module (18
socioeconomic cases) and is reformulated as a **universal, transversal layer** of
SNT: collapse is an **orthogonal axis** that can activate in any system, in any
domain, at any point of its trajectory. **A single principle (least friction)**
generates **distinct collapse modes** depending on boundary conditions.

## 4.1 State space: two orthogonal axes (b ⊥ Δ)

Each system = a pair of **independent** coordinates:

- **Axis 1 — Satellization:** `R(t) = a·t^b`, `R = m_hub / m_node`. **b** = how
  dominance evolves *while the coupled relationship runs*.
- **Axis 2 — Collapse:** `A(τ) = c·τ^Δ`, `A = m_absorber / m_hub^peak`,
  `τ = time since functional extinction`. **Δ** = the speed/shape of absorption
  *once the hub collapses*.

**Why orthogonal (not a 5th phase):** collapse does not wait for the
satellization cycle to end. A hub in full Dependence or Accumulation can collapse
abruptly. Different clock (τ ≠ t), different ratio, different exponent.

**Falsifiable orthogonality prediction:** among cases with both b *and* Δ
measured, `corr(b, Δ) ≈ 0`. The orthogonality is **b ⊥ Δ**.

**First test (crypto, n=11).** Since the satellization corpus and the collapse
cases are disjoint, a paired within-domain dataset is used: cryptocurrencies,
where the same coin has a rise (b_rise) and a fall (Δ_fall). Result:
**Spearman ρ(b_rise, Δ_fall) = +0.009 (p = 0.98)** — no relation, **consistent
with orthogonality** (RC-Δ1 not refuted). Reproducible in
`reconstruction_real/code/orthogonality_test.py`. *Caveats:* a single domain;
b_rise is a price-ascent exponent (a satellization analogue, not the canonical
hub/node b); cross-domain orthogonality remains untested.

## 4.2 Hazard layer h(τ): inevitability, in falsifiable form

If every system with dynamics tends toward collapse (§4.3), most observed systems
**have not collapsed yet** → right-censored data → **survival analysis / hazard
function h(τ)** framework.

> "No system is eternal" = **h(τ) > 0 for every system** (collapse probability
> never zero). Refutable if a system with hazard = 0 is found.

| Layer | Variable | Measures |
|-------|----------|----------|
| Satellization | b | dominance while running |
| Collapse risk | h(τ) | inevitability + time to extinction |
| Absorption | Δ | speed/shape of capture after extinction |

`F` (friction) modulates all three.

**First hazard estimate (crypto, n=41).** Survival over a cohort of
cryptocurrencies (Yahoo); functional extinction = price < 1% of all-time high
(≥99% drawdown, not recovered). 15 extinctions; **deaths across the whole age
range (0.27 → 8.6 years), no death-free era**; Kaplan-Meier declines steadily to
~0.60; hazard positive and rising with age → **consistent with h(τ)>0**.
Reproducible in `reconstruction_real/code/hazard_crypto.py`. *Caveats:* (1)
survivorship bias (only listed coins = survivors → true hazard is *higher*); (2)
age/calendar confound (most born 2017-18; the ~age-8 spike partly reflects the
2022-25 bear market); (3) strict per-bin positivity is limited by n.

## 4.3 Law of Collapse Inevitability

> Every system with dynamics tends toward a **collapse point**. "Collapse" is NOT
> death: it is a **point of critical reorganization** (a bifurcation).

On collapse, the system either **decays** (terminal absorption, measured by Δ) or
**leapfrogs** (renewal, re-entering the cycle — the Ouroboros). Collapse is the
moment where the choice between the two is made; the path depends on the node's
reserves (criterion RC4, dual threshold RQ/RL). Leapfrog witnesses: Querétaro
(b=−0.155), Nuevo León (b=−0.058). The "mean time to collapse" is **descriptive,
not predictive** for an individual case.

## 4.4 Taxonomy of collapse modes (three factors)

The mode is governed by **friction × trigger × (is there a floor/ceiling on the
magnitude?)**:

| Mode | Condition | Shape | Witness (real data) |
|------|-----------|-------|---------------------|
| **Regulated Orbital Decay** | high friction (physical or institutional) | smooth power law **or** exponential (non-accelerating) | 2008 (R²=0.85–0.99), Rome/USSR, astro, epidemic |
| **Cracquelure Decay** | friction≈0 + gradual | erratic fragmentation (crack network) | EOS (R²=0.10–0.70) |
| **Floor-Arrested** | friction≈0 + abrupt + **with floor** | power law to a residual floor | FTX (PL R²=0.875) |
| **Catastrophic Cliff** | friction≈0 + abrupt + **no floor** | accelerating super-exponential | LUNA (5.6 OOM / 11 d) |
| **Logistic Sweep** | **bounded** magnitude (frequency) | S-curve | Delta→Omicron (k=0.22/d) |

Physical anchors: *Catastrophic Cliff* → fold catastrophe (Thom). *Cracquelure
Decay* → desiccation cracking (craquelure): loss of cohesion that fragments via a
network of cracks.

**Key refinement (§4.6.2):** *Regulated Orbital Decay* is smooth /
non-accelerating and can be **power law** (scale-free: finance, astro) **or
exponential** (constant rate: epidemics). What separates it from the
*Catastrophic Cliff* is not the exact shape but that **the rate does NOT
accelerate** — only the cliff is super-exponential.

## 4.5 Principle of Least Friction (unifier)

> Every collapse follows the **trajectory that minimizes integrated friction**.
> The fractal cracks of cracquelure are the visible solution to that
> optimization: the path along which the system loses cohesion spending as little
> as possible.

Variational family: Fermat, least action, minimum dissipation, the lightning
bolt, the river. Here the minimized quantity is **friction**. **The principle =
gradient flow over a stability landscape** (§4.7).

| Friction field | Least-friction path | Mode |
|---|---|---|
| High and homogeneous | no easy crack → drains smoothly | Regulated |
| ≈0 and heterogeneous | many erratic channels → crack network | Cracquelure |
| ≈0 with a single channel | everything empties at once | Catastrophic Cliff |

**Falsifiable version:** the realized collapse has lower integrated friction than
counterfactual trajectories. (WaMu via the pre-arranged FDIC channel = least
friction → 21 h; Lehman without that channel → slow fragmentation, 30,681 h.)

## 4.6 Empirical evidence — 5 domains, real data

| Domain | Case | Friction | Floor/ceiling | Mode | Fit | Source |
|--------|------|----------|---------------|------|-----|--------|
| Astro | Solar flare M6.9 | physical | — | Regulated | PL exp −0.84, R²=0.975 | NOAA GOES |
| Astro | TDE AT2019qiz | physical (viscosity) | — | Regulated | PL exp −1.07, R²=0.843 (theor. −5/3) | NASA IRSA/ZTF |
| Finance | 2008 cohort (6 cases) | inst. high | — | Regulated | PL R²=0.85–0.99 | SEC/FDIC/Fed/SIGTARP |
| History | Rome, USSR, Aztec, Carthage | inst. | — | Regulated | PL R²=0.77–0.99 | Maddison 2023 |
| Crypto | EOS (gradual) | ≈0 | — | Cracquelure | erratic R²=0.10–0.70 | Drive + Yahoo |
| Crypto | FTX / FTT (abrupt) | ≈0 | floor ~$1 | Floor-Arrested | PL R²=0.875 | Yahoo Finance |
| Crypto | LUNA / Terra (abrupt) | ≈0 | no floor | Catastrophic Cliff | super-exp, accelerates | Yahoo Finance |
| Biology | Delta→Omicron (South Africa) | (bounded) | ceiling 100% | Logistic Sweep | k=0.218/d, R²=0.79 | CoV-Spectrum/LAPIS |

**Financial detail (time to 90% absorption, in hours — ordered by resolution
friction):** WaMu (FDIC) 21 h · Bear Stearns (Fed) 626 h · Wachovia 4,140 h ·
Merrill 7,122 h · Chrysler 16,071 h · Lehman (disorderly bankruptcy) 30,681 h.
Range ~1,460×. WaMu ≈ 21 h validates against the real fact (FDIC takeover in
~48 h).

**Connection to the central SNT finding:** institutional friction predicts b
(ρ=−0.68, p=2.5×10⁻⁹⁷, n=714). Friction **also governs the shape of Δ** (the
collapse mode). Friction is the lever for both axes.

### 4.6.1 Friction operationalized (roadmap #1)

Controlled test within the 2008 financial cohort (same domain and units).
Friction = the documented degree of **regulatory pre-arrangement of the
resolution channel**, ordinal 1–6 (6 = FDIC receivership/P&A; 5 = Fed-brokered;
4 = government/TARP §363; 3 = FDIC-assisted open-bank; 2 = pressured private
merger; 1 = disorderly bankruptcy). The scale is built from the *institutional
mechanism*, not from Δ.

| Test (n=6) | Result |
|---|---|
| Friction vs Δ (collapse exponent) | **Spearman ρ = −1.000, p < 0.001** |
| Friction vs log(time to 90%) | ρ = −0.829, p = 0.042 |

More friction → smaller Δ (frontal, orderly absorption). This operationalizes
"friction governs the shape of Δ" as a **measured and falsifiable** claim
(RC-Δ2/RC-Δ4). Reproducible in `reconstruction_real/code/friction_operational.py`.
*Caveats:* n=6; the friction ordinal is a documented judgment (the scale should
be pre-registered before expanding the case set).

### 4.6.2 Biology with unbounded magnitude (roadmap #3)

Variant *frequency* is bounded [0,1] → logistic by construction. To leave the
logistic regime we measure the collapse of an **epidemic wave in absolute counts**
(unbounded): the Omicron wave in South Africa (JHU CSSE), peak 14 Dec 2021
(~23,437 cases/day), falling to 11% of peak in 49 d.

| Fall fit | R² |
|---|---|
| Power law | 0.863 |
| **Exponential** (e-fold ≈ 22 d) | **0.958** |

The fall is **smooth (exponential), NOT a cliff** (returns do not accelerate).
Even without a ceiling, biological collapse stays **regulated**: the
epidemiological feedback (immunity, susceptible depletion, R_eff<1) is
**intrinsic friction**. Reproducible in
`reconstruction_real/code/bio_unbounded_collapse.py`.

### 4.6.3 Orthogonality b⊥Δ (roadmap #2)

See §4.1: crypto n=11, **ρ(b_rise, Δ_fall) = +0.009 (p = 0.98)** → consistent with
b⊥Δ. The cross-domain test with a paired dataset is still missing.

### 4.6.4 Hazard h(τ) (roadmap #4)

See §4.2: crypto n=41, 15 extinctions, **h(τ)>0 across the whole age range**.

## 4.7 The visual language: stability landscapes ("valley plots")

The system is a ball in a valley (basin of attraction) of a potential landscape;
friction controls how it rolls; collapse is the ball leaving its valley. **The
modes are distinct geometries of the same landscape**
(`figures/fig_paisajes_colapso.{svg,png}`):

- **Regulated:** a valley that tilts/flattens slowly → the ball rolls smoothly.
- **Catastrophic Cliff:** fold catastrophe — the valley wall vanishes and the
  ball falls to the bottom (zero, no floor).
- **Floor-Arrested:** same, but an intermediate valley (floor) traps the ball.
- **Cracquelure:** rugged/fractal landscape, many shallow channels.
- **Logistic Sweep:** double well (Delta-valley → Omicron-valley).
- **Leapfrog:** the ball escapes upward, to a better valley (renewal).

`figures/fig_catastrofe_cuspide.{svg,png}` shows the fold catastrophe: as friction
(the control parameter) drops, the stable valley and its barrier annihilate and
the system falls off the cliff. Anchors: catastrophe theory (Thom), Waddington's
epigenetic landscape, the ecological resilience "ball-in-cup" (Holling), climate
tipping points (Lenton).

## 4.8 Connection to existing SNT

- **F (friction)** already lives in ASI = δH·α/F → Δ connects via F without
  pretending it is the same number as b.
- **Leapfrog / RC4** → the collapse bifurcation.
- **Satellization cycle** → collapse is orthogonal to its phases.
- In astronomy **F is literal**: Chandrasekhar's dynamical friction and disk
  viscosity govern absorption (TDE, mergers).

## 4.9 Caveats / methodological honesty

- Crypto side = n=2 clean (EOS + LUNA) + FTX; small n.
- It is **correlational**: domains differ in more than friction (scale, what
  "mass" is, microstructure). Frame as a hypothesis.
- LUNA and the solar flare are not absorption ACO with a single absorber → they
  enter as evidence of *collapse shape/mode*.
- TDE exp −1.07 vs −5/3 theoretical: shallower due to the g band + imperfect host
  subtraction; the point is that it is a power law (regulated), not the exponent.
- "Time to 90%" depends on the threshold; the **ordering** abrupt < gradual is
  robust.
- Frequencies (Omicron) are bounded → logistic by construction.

---

# PART V — φ hypothesis (closed)

**STATUS: REFUTED after 4 rounds of independent validation.**

H-φ posited that the exponent b would cluster near fractions of the golden ratio
(φ = 1.618...), the set {φ/4, φ/3, φ/2, 2φ/3, 3φ/4, φ} ±0.10.

- **Round 1 (crypto):** 0/4 datasets with a φ signal.
- **Round 2 (primary biological literature):** 0/6 datasets with a signal.
- **Round 3 (real corpus, n=188, b>0):** 26.6% near φ vs 27.5% expected by chance
  (Monte Carlo N=5,000), **p = 0.642 — identical to chance.**
- **Round 4 (re-test on the 721 corpus + placebo control):** re-running on the
  expanded corpus surfaced an **apparent signal** that forced a more rigorous
  analysis:

| Subset | % near φ | uniform null | placebo (random targets) |
|---|---|---|---|
| Corpus b>0 (n=534) | 42.3% | p<0.001 (signal) | **p=0.170 — NOT special** |
| Friction-free bio E1+E3 (n=238) | 60.1% | p<0.001 | p<0.001 (survives) |

Two traps identified: (1) **band coverage** — the 6 φ-bands (±0.10) densely tile
[0.3–1.3], exactly where b concentrates; the uniform null overestimates chance,
and a placebo (6 *random* targets in the same range) shows that for the full
corpus φ is **not special** (p=0.170); (2) **pseudoreplication** — the bio
"signal" survives the placebo, but E3 are 234 countries measuring the SAME
pandemic (COVID), not independent data; COVID's characteristic b ≈ 0.846 falls
0.037 from φ/2 = 0.809: a single coincidence replicated 234×, not an attractor.

**Conclusion: H-φ remains refuted.** The expanded corpus does NOT rescue it.
*Methodological lesson:* the φ test requires a **placebo control** (random
targets) and **handling of non-independence**, not just a uniform null. H-φ is
classified as a **second-order speculative hypothesis**; it is not included in
the main paper's claims and does not affect the validity of the general SNT
framework, the exponent b, or the ASI. Sub-hypothesis H-3 (denominator 3 dominant
in b/φ): **discarded**. Reproducible: `papers/phi_retest.py` +
`papers/phi_placebo.py`.

---

# PART VI — Complete theoretical body (modules I–XVI + appendices)

The full framework — epistemological foundations, 5-level node taxonomy,
mechanism (Matthew effect / Pareto), 4-phase satellization cycle, historical
cases, leapfrog, operationalized ASI, biological and astronomical extensions,
active hypotheses (inter-brain synchronization, Orch-OR, oceanic nodules, Bitcoin
as a collective index), the dark-matter frontier, and the Sentinel Omega and
mathematical-tools appendices — is restored in full in **Annex A** at the end of
this document (recovered from the complete v27 framework, with corpus figures
corrected to v30). Parts I–V above are the current, authoritative layer; Annex A
is the complete conceptual body.

# PART VII — Publication status

- **SSRN (abstract 6418778):** **v30 REVISION SUBMITTED** (28 Jun 2026,
  `papers/snt_ssrn_v30_EN`); supersedes v2.3.1/502; under SSRN review.
- **Zenodo (DOI 10.5281/zenodo.19446521):** PUBLISHED — **updated to v30**
  (721-case real corpus).
- **PLOS Complex Systems (PCSY-D-26-00059):** MAJOR REVISION — deadline 10 Aug
  2026. Figures updated to v30 (721 cases). Editor: Haroldo V. Ribeiro;
  EIC: Hocine Cherifi.
- **Journal of Complex Networks (COMNET-2026-214):** REJECTED without review
  (Yamir Moreno). Action: re-submit to Scientific Reports / Physica A.
- **MIT GCFP 13th Annual Conference:** IN PREPARATION — deadline 17 Jul 2026.
  Thesis: institutional friction regularizes the *shape* of collapse.
- **Unreleased papers (require v30 update):** J. Theoretical Biology, Astrophysical
  Journal, Investigación Económica.

---

# Roadmap (updated status)

1. **Operationalize friction** along a path, by domain. *FIRST RESULT (§4.6.1):
   resolution friction vs Δ, ρ=−1.000, n=6.* Still to extend to more
   cases/domains with a pre-registered scale.
2. **Orthogonality test** `corr(b,Δ)≈0`. *FIRST RESULT (§4.1/§4.6.3): crypto
   n=11, ρ=+0.009.* Cross-domain test still missing.
3. **More cases per mode** (n=3+ crypto; several TDEs). *Unbounded biology: FIRST
   RESULT (§4.6.2) — Omicron in absolute counts decays smoothly exponential
   (R²=0.96), not a cliff.* Still to find a biological collapse WITHOUT intrinsic
   friction (abrupt external shock).
4. **Formalize h(τ).** *FIRST RESULT (§4.2/§4.6.4): crypto n=41, h(τ)>0 across the
   whole age range.* Still to get a larger cohort without survivorship bias and
   to disentangle age vs calendar.
5. **Define the "floor" rigorously** and decide whether it folds into friction or
   is an independent third axis.
6. **Independent validation / pre-registration** before claiming causality (today
   everything is correlational and descriptive).

---

# References

- Bolt, J. & van Zanden, J.L. (2020). *Maddison Project Database 2020.* Maddison
  Project Working Paper 15. University of Groningen.
- INEGI (2022). *GDP per capita by federal entity.* National Accounts System of
  Mexico.
- US Census Bureau (2023). *Historical state population estimates.*
- Dong, E., Du, H. & Gardner, L. (2020). An interactive web-based dashboard to
  track COVID-19 in real time. *The Lancet Infectious Diseases*, 20(5), 533–534.
  [Johns Hopkins CSSE]
- MacLulich, D.A. (1937). Fluctuations in the numbers of the varying hare.
  *University of Toronto Studies*, Biol. Ser. 43.
- Elton, C. & Nicholson, M. (1942). The ten-year cycle in numbers of the lynx in
  Canada. *Journal of Animal Ecology*, 11(2), 215–244.
- Open Exoplanet Catalogue (2024).
- Thom, R. (1972). *Stabilité structurelle et morphogénèse.* [fold catastrophe]
- Waddington, C.H. (1957). *The Strategy of the Genes.* [epigenetic landscape]
- Holling, C.S. (1973). Resilience and stability of ecological systems. *Annual
  Review of Ecology and Systematics*, 4, 1–23.
- Lenton, T.M. et al. (2008). Tipping elements in the Earth's climate system.
  *PNAS*, 105(6), 1786–1793.
- NOAA SWPC GOES X-ray flux; NASA IRSA / ZTF (TDE AT2019qiz); CoV-Spectrum / LAPIS.

---

# Repository and data

GitHub: github.com/Inzainos/The-shadow-Node-Theory · Corpus v5 (721 cases):
`reconstruction_real/data/snt_corpus_REAL_v5.csv`. Collapse layer:
`papers/SNT_Colapso_Acoplado.md`; scripts in `reconstruction_real/code/`
(`friction_operational.py`, `orthogonality_test.py`, `bio_unbounded_collapse.py`,
`hazard_crypto.py`, `collapse_multidomain.py`, `make_collapse_landscapes.py`);
φ hypothesis: `hypotheses/snt_phi_hypothesis.md` + `papers/phi_retest.py` +
`papers/phi_placebo.py`.

SSRN: https://ssrn.com/abstract=6418778 · Zenodo:
https://doi.org/10.5281/zenodo.19446521

---

*Fractal Core Research — Tlaxcala, Mexico · Theoretical Framework v30 · June 2026*
*"Technical truth over numerical impression."*

---

# ANNEX A — Complete theoretical body (v27 framework restored)

> **Version notice.** This annex restores the complete body of the theoretical
> framework (the v27/v28 version, ~230 KB), which the v29 update notes had
> truncated to a summary. The conceptual content is preserved intact and
> verbatim. **Any empirical corpus figure appearing within this annex is
> historical and is superseded by PART II (Corpus v30) and PART III (Findings)
> at the start of the document.** The statistical block of the "502-case corpus"
> (Module XI) was replaced by a correction pointing to the real v30 corpus.

---

UNIFIED THEORETICAL FRAMEWORK

Complex Systems, Scale-Free Networks and the
Universal Algorithm of Suppression and Emergence

Elán Zainos Corona · Fractal Core Research · Version 0.1 — March 2026

Complex systems at all scales share the same scale-free network topology,
suggesting a common organizing principle. Shadow Node Theory demonstrates this
principle at the social scale with verifiable data. The central hypothesis is
that there is an underlying physical substrate that explains both scale
invariance and the correlations between apparently disconnected phenomena.

## Introduction: Ancient Knowledge as an Empirical Base

There is an epistemological bias in modern science: the assumption that
knowledge is strictly cumulative and linear, that everything prior is inferior
to the present. This framework questions that assumption in a specific domain.

Ancient civilizations lacked the formal mathematical language we possess today.
Yet they had something modern science does not: systematic observation of
patterns over centuries without the noise of accelerated technological change.
Entire generations devoted exclusively to observing astronomical, biological,
climatic and social cycles.

**Evidence of ancient technical precision**

The Antikythera mechanism (150 BC): a geared device able to predict eclipses and
planetary positions with a precision not technologically replicated until the
14th century.

Astronomical alignments at Stonehenge, Chichén Itzá, Giza and Angkor Wat:
fractions-of-a-degree precision with specific solar and stellar events. Requires
applied mathematics and multigenerational observation.

The Maya calendar: a system of nested cycles describing patterns at multiple
temporal scales. Formalized systems thinking.

The golden ratio in classical architecture: appears as a structural principle,
not decorative. Empirical engineering that minimizes material and maximizes
stability.

The epistemological hypothesis of this framework is that sacred geometry and
ancient postulates are compressed databases of long-term empirical observation.
Modern mathematics is rediscovering with formal tools what was observed over
millennia. The researcher's task is not to dismiss those observations but to
translate them into contemporary verifiable language.

**The origin of this research: founding anecdote**

The starting point of this research was not a formal hypothesis but a personal
observation that generated a question. After reading about Wheeler's delayed-
choice experiment (1978), where measurement in the present affects how we
interpret a particle's past behavior, a home experiment was performed with an
unopened tube of pills.

First tube: 1 of 1 pills of the expected color. Second tube, opened three days
later with the same expectation: 8 of 10 pills of the expected color. Additional
observation: the presence of skeptical people seemed to correlate with results
less aligned with the expectation.

This experiment does not prove retrocausality. It does not replicate Wheeler's
experiment. What it did do was generate the question that oriented all subsequent
research: if the observer influences the observed system, and if that principle
replicates across scales, there is an organizing pattern that transcends the
specific physical substrate.

## Central Claim

The universe operates as a network of networks at macro, meso and micro scales,
governed by the same organizing algorithm. Complex systems at all scales share
the scale-free network topology, suggesting a common underlying physical
principle. Shadow Node Theory demonstrates this principle at the social scale
with verifiable quantitative data.

This claim has three components with differing degrees of certainty:

| LEVEL | CONTENT | STATUS |
| :-- | :-- | :-- |
| LEVEL 1 | Shared topology across multiple scales (Barabási, IllustrisTNG, SDSS, Physarum polycephalum) | Demonstrated |
| LEVEL 2 | Shadow Node Theory: urban suppression algorithm with quantitative data | Verifiable with data |
| LEVEL 3 | Inter-brain synchronization as a collective field (BrainNet, Waseda, Dartmouth) | Active hypothesis |
| LEVEL 3 | Microtubules as information decoders (Penrose-Hameroff, Orch-OR) | Active hypothesis |
| LEVEL 4 | Dark matter as a universal connective substrate | Open frontier |

## Level 1: The Demonstrated — Scale Invariance

The most solid finding of this framework is that systems radically different in
substrate and scale converge toward the same mathematical topology. This is not
metaphor. It is verifiable shared geometry.

### 1.1 Scale-Free Networks (Barabási-Albert, 2002)

Albert-László Barabási proved mathematically that networks growing via
preferential attachment — where the most connected nodes receive new connections
with higher probability — inevitably converge toward a power-law distribution:

P(k) ~ k^(-gamma)

where k is the node degree and gamma is the distribution exponent. This law
appears in: the Internet (distribution of links among websites); neural networks
(connectivity between neurons); academic citation networks (publication impact);
city networks (population distribution, Zipf's Law); cosmic filaments
(distribution of matter in the universe).

The underlying mechanism is identical in every case: two simple local rules
produce the same global pattern. No centralized control is required. No
intelligent design is required. The pattern emerges.

### 1.2 The Physarum Polycephalum Experiment (Nakagaki, 2010)

Toshiyuki Nakagaki and his team placed food at the exact points where the Tokyo
metro stations are located. They released slime mold, an organism without a
nervous system or centralized brain. In 26 hours, the organism had built a
network practically identical to the Tokyo metro system, simultaneously
optimizing distance, redundancy and efficiency.

The mold follows only two local rules: reinforce the paths that work; abandon the
paths that do not. From those two rules an optimal global network emerges. This
is called distributed emergent computation and is the same mechanism operating in
neural networks, urban systems and cosmic filaments.

The mechanism is not mystical. It is the same optimization algorithm running on
different substrates. Scale invariance is not geometric coincidence. It is
inevitable mathematical convergence under distributed optimization without
centralized control.

### 1.3 AT2025ulz and the Superkilonova: The Cosmic Ouroboros

On 18 August 2025, the LIGO detectors in Louisiana and Washington and Virgo in
Italy recorded gravitational waves (signal S250818k) from a source 1.3 billion
light-years away. The Zwicky Transient Facility identified within minutes a
rapidly fading object at that location. The event was named AT2025ulz. What
followed over the subsequent weeks of multispectral observation — X-ray, optical,
infrared, radio, gravitational waves — produced something the astronomical
community had never seen.

The team led by Mansi Kasliwal of Caltech, with collaborators from Carnegie
Mellon, Columbia and Ludwig Maximilian University, proposed in December 2025 in
The Astrophysical Journal Letters that AT2025ulz may be the first observed example
of a superkilonova: an event that had been theorized but never detected.

**The superkilonova mechanism.** The complete sequence, per the model proposed by
Brian Metzger of Columbia University: a massive star of at least 20 solar masses
with extremely rapid rotation collapses; its core does not form a single neutron
star as usually happens. Extreme rotational forces fragment the collapsing core
into an accretion disk. That disk fragments under its own gravity into multiple
clumps that collapse individually, forming two subsolar-mass neutron stars, at
least one below the Sun's mass. Within seconds of birth, the two neutron stars
spiral toward each other, emitting gravitational waves that deform the fabric of
spacetime. The neutron stars collide, generating a kilonova: an explosion that
forges the universe's heaviest elements — gold, platinum, uranium, the iron in
human blood. The kilonova's light glows red because heavy elements block the blue
wavelengths. The kilonova is partly obscured by the original supernova that
preceded it hours earlier, creating a hybrid event that confused observers for
days. Gravitational-wave data confirm at least one of the merging objects had
subsolar mass, with 99% probability — consistent with the "forbidden" neutron
stars theory predicted but nobody had observed.

**The Ouroboros: death as a mechanism of creation.** AT2025ulz is the most direct
physical representation of the principle that names this conceptual pattern. The
Ouroboros, the serpent biting its own tail, is humanity's oldest figure for the
cycle where end and origin are the same point. In this cosmic event the causal
chain is literal: a star dies in supernova; from its death two dead stars are
born; those two dead stars merge; from that merger are born the materials that
build life — carbon, iron, gold, uranium. Death does not precede life as a
separate stage. Death is the mechanism of creation. This is not metaphor: it is
r-process nucleosynthesis, verified spectroscopically by dozens of telescopes in
August and September 2025.

**Connection with the framework.** AT2025ulz's sequence is the same pattern this
framework identifies at other scales: maximum tension accumulation in the system
(stellar core with no energy outlet); collapse of the rigid structure (supernova:
first death); fracture into dynamic subsystems (two subsolar neutron stars);
tension between subsystems generating waves in the spacetime substrate; fusion of
subsystems (neutron-star collision: second death); emergence of new order at a
higher scale (heavy elements, seeding the universe). This is the same pattern SNT
identifies in urban systems, that Barabási identifies in scale-free networks, and
that Physarum polycephalum executes when building optimal transport networks.

Status: Candidate for first observed superkilonova. Published in The
Astrophysical Journal Letters, December 2025. Kasliwal et al., Caltech / Carnegie
Mellon / Columbia. Definitive confirmation requires additional detections of
subsolar neutron-star mergers. Research remains active.

Note on GRB 250702B: in earlier versions of this framework, GRB 250702B and
AT2025ulz were mentioned as the same event. They are distinct. GRB 250702B
(2 July 2025) is the longest gamma-ray burst ever observed, lasting about 7 hours,
still without a definitive progenitor classification. AT2025ulz (18 August 2025)
is the superkilonova candidate. Both are evidence of the same cosmic-scale
pattern but are separate phenomena.

## Level 2: The Verifiable — Shadow Node Theory

Shadow Node Theory is the empirically strongest contribution of this research. It
holds that urban stagnation is not random but follows complex-systems laws.
Specifically: when two power nodes orbit in critical proximity, the node with
greater accumulated advantage cannibalizes the historical node via a
mathematically predictable algorithm.

### 2.0 Node Taxonomy: SNT v2.0

The binary model (dominant node / shadow node) is a valid simplification to
isolate and measure divergence between two points. In reality, systems operate as
N-body networks where multiple nodes interact simultaneously across coupled
hierarchical levels. This section formalizes the full node taxonomy, articulated
in five functional levels defined by their thermodynamic function of processing
and retaining resources within the network.

**Level 0 — Central Macro-Hub (Absolute Dominant).** Entity with maximum
preferential-attachment inertia. Primary function: unidirectional absorption of
flows (capital, population, institutional decision, talent). Examples: Mexico City
within the national system, New York within the North Atlantic system, the Elite
user in the HackerEarth ecosystem. Natural limit: endogenous saturation (K_max) —
when the hub accumulates beyond its optimal carrying capacity, internal friction
(congestion, cost of living, bureaucracy) forces overflow toward Level 2 nodes,
the only passive redistribution path. Behavior under threat: not passive — when it
detects anomalous energy accumulation in a peripheral node it deploys an immune
response (regulatory capture, legislative changes, patent monopoly, or acquisition
of the emerging node's assets before it reaches independent critical mass).

**Level 1 — Secondary Attractors (Regional Hubs).** Nodes with gravitational mass
self-sufficient to generate their own preferential-attachment fields over their
immediate peripheries. They operate in a dual functional state: they satellize
their regional peripheries while being simultaneously drained by the Level 0 hub
on a different plane. Two subtypes: Independent (compete with Level 0 on distinct
dimensional planes, autonomous growth — Monterrey via export manufacturing,
Guadalajara via technology) and Dependent (satellize their periphery but require
Level 0 for their own systemic viability). Empirical example: Puebla in the
CDMX-Puebla-Tlaxcala system — Puebla satellizes Tlaxcala (FDI ratio 25.5×,
migration r = 0.9646) while being satellized by CDMX on larger-scale variables.

**Level 2 — Transition Nodes (Logistic Bypass).** Structures optimized to
intercept flows when the Level 0 hub exceeds its carrying capacity. They do not
generate primary economic activity of their own but capitalize on Level 0's
logistic overflow. They show power-law growth with positive acceleration
(b > 0.45) during expansion. Defining trait: their growth is parasitic on Level
0's success, not autonomous. Example: Querétaro as receptor of CDMX's industrial
overflow; the northern border-strip cities as receptors of manufacturing overflow
when CDMX saturates.

**Level 3 — Deep Shadow Nodes (Extraction Capillaries).** Base stratum. They
operate under severe historical-gradient satellization with unidirectional flows:
they provide raw energy (primary human capital via migration, natural resources,
agricultural output) to the upper levels without retaining value in proportion to
their contribution. Two existence conditions: simple satellization (one immediate
dominant attractor, e.g. Tlaxcala relative to Puebla) and compound satellization
(multiple simultaneous extraction vectors from different levels). In compound
satellization the total loss flow is the sum of the extraction gradients of all
upper nodes acting on Level 3:

Total_flow = w(Level3→Level1) + w(Level3→Level0)

This is the critical refinement of the original binary model. Tlaxcala loses
resources not only to Puebla but directly to CDMX via long-range labor migration,
FDI that bypasses Puebla, and federal political decisions. The binary model
systematically underestimates the total satellization of Level 3 nodes. They are
the primary candidates for leapfrog — they have the strongest incentive for the
dimensional jump and, if they achieve gravitational independence, can transit
directly to Exogenous status without passing through intermediate levels.

**Exogenous Level — Dimensional Anomalies.** Nodes sustained by direct injections
from networks external to the national system: tourism currency, FDI of a
geographic origin distinct from the central hub, international remittances, or
positioning in global value chains that bypass the domestic Level 0. The system's
internal satellization algorithm does not primarily govern them. Examples:
Quintana Roo (gravitational field sustained by international tourism currency),
direct-export free zones, university cities with direct federal funding. Exogeneity
is dimensional, not absolute: a node may be economically independent of Level 0
while politically dependent, or vice versa.

**Implications for the binary model.** The five-level taxonomy does not invalidate
the binary model: it contextualizes it. When the main paper compares Toledo and
Madrid, or Bruges and Antwerp, the binary model is valid because both nodes
operated at the same hierarchical level within the same political system.
Comparing pairs at the same level is the validity condition for the power-law fit.
When comparing nodes of different levels (Tlaxcala vs CDMX directly, without Puebla
as intermediary), the binary model underestimates the divergence speed because it
ignores the intermediate levels' extraction vectors. Real complex systems do not
have a single predator; they have a trophic chain. The five-level taxonomy is the
step from the simple differential equation to the coupled system of equations.

### 2.0.1 Empirical Verification: Mexico N-Body Matrix

The five-level taxonomy is verified empirically with INEGI 2022-2023 data for
Mexico's 32 federal entities. Distribution by level (using 2022 GDP per capita and
share of national GDP): **Level 0** — Mexico City: 1 entity, GDP pc 285.2k MXN,
14.8% of national GDP. **Level 1** — 9 entities (Nuevo León, Coahuila, Baja
California, Chihuahua, Sonora, Tamaulipas, Jalisco, Guanajuato, Puebla), mean GDP
pc 158.9k MXN, 41.0%. **Level 2** — 8 entities (Querétaro, Aguascalientes, Colima,
Estado de México, Sinaloa, Durango, San Luis Potosí, Yucatán), mean 126.5k MXN,
20.2%. **Level 3** — 11 entities (Morelos, Zacatecas, Tabasco, Nayarit, Hidalgo,
Michoacán, Veracruz, Tlaxcala, Guerrero, Oaxaca, Chiapas), mean 80.7k MXN, 16.8%.
**Exogenous** — 3 entities (Campeche via oil; Baja California Sur and Quintana Roo
via international tourism), mean 183.8k MXN, 4.3%.

The distribution follows a power law: fitting f(rank) = a · rank^b on INEGI 2022
data gives a = 396.8, b = −0.473, R² = 0.838, Pearson r = −0.933, p < 0.001 —
confirming the national system operates under the preferential-attachment dynamics
the theory predicts.

The central result is not the classification but the quantification of the binary
model's error. SNT v1.0 modeled Tlaxcala's satellization as a bilateral relation
with Puebla: gradient w_ij = GDP_pc_Puebla − GDP_pc_Tlaxcala = 26.2k MXN. The
N-body taxonomy reveals Tlaxcala simultaneously suffers a long-range extraction
vector toward CDMX: w_ij(Tlaxcala→CDMX) = 285.2 − 68.4 = 216.8k MXN. The total
compound gradient is 26.2 + 216.8 = 243.0k MXN. The binary model underestimated
Tlaxcala's total satellization by a factor of 9.3×; most extraction (89.2%) goes
directly to Level 0, skipping the Level 1 intermediary. Implication for leapfrog
strategy: competing only against Puebla attacks 10.8% of the problem.

GDP concentration confirms Pareto: 30.6% of entities (Level 0 + Level 1, 10 of 32)
hold 55.8% of national GDP; the 34.4% in Level 3 generate only 16.8% despite being
the most numerous group — a discontinuous distribution between levels, exactly the
Fractal Gap documented in the HackerEarth case. Source: INEGI PIBE 2023. Zenodo
DOI: 10.5281/zenodo.19027089.

### 2.0.2 Triple Systemic Resolution Model (SNT v2.0)

The binary model captures one dominant–shadow relation within a single system. But
reality operates at three distinct resolution scales with their own dynamics,
actors and incompatible competition rules. Mixing them in one model produces
erroneous predictions.

**Resolution I: Atomic System (Individual Node).** The base scale of processing
and survival. The Atomic Node is the sovereign individual entity (the analyst,
entrepreneur, student) operating under linear, autopoietic dynamics, independent
of the collective mycelium's biological extraction. Competition here is not against
a central hub but against the chaos of one's own environment. Success is measured
not by volume but by uncertainty reduction: how much entropy the node processes
with the least residual-energy expenditure. The node competing in HackerEarth 2026
operates as an Atomic Node, not a Shadow Node — it can operate from Tlaxcala and
reach the global 0.05 percentile because the dimension where it competes is
orthogonal to the national fungal network.

**Resolution II: Meso System — Intra-national Fungal Network.** A closed ecosystem
bounded by geopolitical border, corporate jurisdiction or institutional structure.
This is where SNT v1.0 applies directly in binary form: a Central Hub (Level 0)
administers the network by continuously extracting residual energy from peripheral
Shadow Nodes (Level 3). The dynamic is controlled parasitism, not destruction: the
hub needs shadow nodes to survive to keep providing flow. Applicability:
localized zero-sum systems, deliberately induced structural latency, absorption of
high-density Atomic Nodes from periphery to center, maintenance of minimum viable
substrate. Non-applicability: symmetric linear competition (a Shadow Node cannot
beat the hub with the hub's own rules), perfect thermodynamic equilibrium (Meso
homeostasis is controlled disequilibrium favoring the center), and the mass
leapfrog of an entire Shadow Node (asymptotic rupture is exclusive to the Atomic
Node; a whole territory only evolves if the density of independent Atomic Nodes
within it reaches critical mass).

**Resolution III: Macro System — Collision of Superorganisms.** The clash between
two or more complete fungal networks: country vs country, bloc vs bloc, tech
ecosystem vs tech ecosystem. No central hub controls both; they are sovereign
entities competing to colonize the same substrate of resources, markets or talent.
Absorption operates via two mechanisms: Silent Absorption (a network extends its
Directed Acyclic Graph over the rival's peripheral nodes via a 10–15% economic
advantage, human-capital flight and asymmetric treaties, without visible
structural collapse) and Kinetic Rupture (when the exogenous perturbation Ω(t)
exceeds the containment threshold: the dominant organism destroys the rival's
communication links and forces jurisdiction transfer of whole clusters; the
Ukraine case is the most recent example). The Atomic Node inside a hub-collision
zone faces the worst case: Ω(t) → ∞ consuming all available residual energy;
its protocol is immediate leapfrog to dimensional independence — strategic latency
is unviable in a collision zone.

### 2.0.3 Complete Node Taxonomy — Definitive Nomenclature

**Central Hub — Level 0:** primary gravitational attractor of the Meso system;
administers the fungal network by continuous residual-energy extraction. Does not
compete, extracts. Natural limit K_max; immune response under threat scales
non-linearly as a threatening node nears critical mass. **Orchestrator Node —
Level 2 (Mycelium / DAG):** orchestration infrastructure as a Directed Acyclic
Graph; executes distributed parallelism; capitalizes logistic overflow when the
hub exceeds K_max (e.g. Querétaro). **Shadow Node — Level 3:** base stratum under
recursive suppression via three vectors — legal (regulatory firewall), logistic
(infrastructure bypass that raises operation latency), and gravitational
(human-capital flight). Primary leapfrog candidate if it reaches critical mass of
independent Atomic Nodes. **Atomic Node — Micro Level:** sovereign individual under
autopoietic, linear dynamics; evolution depends on two concurrent vectors kept in
balance — the Specialization Vector (Δ_H_tech, high-level tools to process the
external environment) and the Everyday Structural Vector (Δ_H_env, low-level tools
to stabilize daily life). High technical specialization with a chaotic environment
yields a lower ASI than moderate specialization with full systemic coherence.
**Exogenous Level — Dimensional Anomalies:** nodes sustained by direct external
injections; exogeneity is dimensional, not absolute.

### 2.0.4 Dimensional-Jump (Leapfrog) Mechanics — Conditions and Failures

Leapfrog is the escape mechanism from satellization — not spontaneous but the
result of specific parametric alignment. **Validity conditions to execute the
jump:** (1) ASI > 1 (uncertainty reduction exceeds internal free energy); (2)
favorable systemic-latency gap — the hub operates in 168-hour cycles and the
Atomic Node can execute in a fraction of that; (3) an identified orthogonal
dimension where the hub's accumulated advantage does not apply; (4) the
Distribution Channel is not hub-controlled, or a bypass exists. **Conditions for
strategic latency (waiting):** absence of exact serialized variables to activate
the new dimension (tools not ready); extraction vector saturation greater than
available residual energy (jumping there drains totally); or an emerging
disruptive innovation that will lower activation cost next cycle. The critical
condition: waiting must generate net accumulation — internal retention rate ρ must
exceed the hub's extraction rate w_ij. If ρ < w_ij during the wait, latency is
sterile and accelerates definitive satellization.

**Taxonomy of jump failures.** Failure 1 — Premature Execution (t < t_min): the
node jumps before accumulating the technological maturity to identify the
orthogonal plane; the linear attempt is absorbed by the hub's preferential
attachment (analogy: Tlaxcala trying to compete in textiles with Puebla in the
19th century without its own rail). Failure 2 — Event Horizon (t > t_horizon):
the node passes the point of no return; continuous extraction has drained residual
energy below the activation threshold (E_a); the jump is thermodynamically
unviable; the node becomes an irreversible satellite absent an exogenous shock of
scale comparable to the original trigger. Failure 3 — Global Macro-Perturbation
(Ω(t)): an exogenous shock hits during the critical transit window; the node had
reallocated residual energy to build capabilities in the new dimension, losing
efficiency in its base dimension; if the shock magnitude exceeds available
activation energy, the jump is aborted and the node recaptured. This is the only
failure that does not imply a strategic error by the shadow node. Failure 4 —
Sterile Latency: the node delays the jump without optimizing during the wait;
continuous extraction exceeds net accumulation (ρ < w_ij); residual energy falls
below the activation threshold before the opportunity window arrives. Unlike
Failure 2, this is avoidable.

**Successive windows: failure is not terminal.** A failed jump does not imply
definitive satellization if residual energy has not hit zero. The global system
cyclically generates new orthogonal dimensions via technological innovation; each
new dimension lowers activation cost (E_a) because the required infrastructure is
smaller. The 2026 jump to AI-agent orchestration requires less physical
infrastructure than the 1850 jump to rail hub or the 1990 jump to aerospace
manufacturing. A node with positive residual energy can attempt leapfrog N times.

### 2.0.5 SNT v2.0 Variables — Formal Nomenclature

**E_res (Residual Energy):** capital, knowledge and processing capacity available
before systemic extraction. **w_ij (Extraction Vector):** rate of resource
transfer from node i to node j per unit time; empirically computable as a GDP-per-
capita differential (INEGI) or a tool adoption-rate differential (HackerEarth).
**E_a (Activation Energy):** minimum cost to execute the dimensional jump; decreases
with each new technological paradigm. **M_tech (Technological Multiplier):**
multiplicative advantage of disruptive innovation over base technology; a deferred
jump integrating M_tech > 1 can exceed a premature jump in momentum. **χ
(Relational Interface):** coefficient of high-density informal ties that lower
activation cost and mitigate the hub's immune detection; w_ij_effective = w_ij ·
(1 − χ). No moral connotation: a quantifiable network anomaly present in all
complex systems (asymmetric social capital in political economy; mycorrhizal
symbiosis in biology). **Ω(t) (Exogenous Macro-Perturbation):** global stochastic
factor that does not discriminate internal topology; impact is asymmetric (the
high-K_max hub absorbs it better than a low-energy shadow node); includes
pandemics, international financial collapses, systemic-scale geopolitical
conflicts. **Ck (Atomic Coherence Factor):** exclusive to the Micro resolution;
measures the balance between the Specialization Vector and the Everyday Structural
Vector; Ck = 1 at perfect balance, Ck = 0 when one absolutely dominates. **ASI
(Atomic Sovereignty Index):** composite measure of the Atomic Node's autonomy,
inspired by Friston's Free Energy Principle: ASI = (Δ_H · α) / F, where Δ_H is
processed information (uncertainty reduction), α is the autonomy coefficient
(proportion of node-generated vs hub-imposed actions), and F is internal free
energy (unresolved chaos). ASI > 1 indicates operative cognitive sovereignty.

The triple-resolution taxonomy does not invalidate SNT v1.0: the four historical
cases of the main paper (Bruges-Antwerp, Toledo-Madrid, Portugal-NW Europe,
Tlaxcala-Puebla) are all Meso-system instances — the scale where the binary model
is valid. The extension to Micro and Macro completes the framework without
contradicting the existing empirical corpus.

## Module I: Micro Resolution — The Atomic Node

The Atomic Node is the system's fundamental processing unit — an individual entity
under linear, autopoietic dynamics. "Atomic" does not mean it exists in a vacuum:
every individual operates within an immediate social nucleus (family, partner,
close network) that constitutes its own micro-system with its own extraction or
amplification hierarchy. The model treats that social nucleus as the Atomic
Node's Meso system.

**I.1 Resource structure.** Two categories with radically different dynamics.
*Quantitative resources (extractable):* money, property, time, physical
infrastructure, access to material tools — extractable by the micro-system's hub
via economic dependence, time demands or asset appropriation; loss is direct and
visible. *Qualitative resources (inherent):* knowledge, skills, accumulated
experience, judgment, capacity to process entropy, intrapersonal maturity —
inherent to the node, not directly extractable by any external hub, but not
permanent: they degrade at an internal rate that depends on practice. Qualitative
degradation is the second-order mechanism of satellization: the hub doesn't
extract the knowledge directly but drains the quantitative resources (time and
money) the node needs to practice and keep that knowledge alive. *Hierarchy:*
quantitative resources without qualitative backing dissipate; qualitative
resources without quantitative ones degrade slowly but survive and can recover.
The qualitative is the hard core; the quantitative is the fuel. A node that loses
all quantitative resources but keeps its qualitative ones intact has not reached
the event horizon — it can still recover and jump.

**I.2 Satellization mechanisms.** The individual is satellized when its social
nucleus acts as an extractor hub rather than an amplifier. The extractor hub
transfers quantitative resources asymmetrically without demanding or supporting
qualitative development — it creates dependence and actively slows the node's
qualitative growth (its benefit comes from the node's dependence, not its
autonomy). The amplifier supports both dimensions in parallel with equity. The
observable result is growth speed: the amplifier-backed node accelerates; the
shadow node inside an extractor hub decelerates even with resource access.

**I.3 The two dimensions of the jump.** A successful leapfrog requires two
dimensions developed in parallel, with a hierarchy. *Intrapersonal dimension
(base):* maturity, cognitive humility, recognition of one's own limits, emotional
stability under pressure — must develop first; without it the node can win a
contest or contract but cannot sustain the new position (immaturity produces a
nosedive after the jump). *Professional/business dimension (visible jump):*
technical skills, market positioning, access to economic opportunities. When both
are developed simultaneously the jump is stable; with only the professional
dimension it is temporary. The indicator of a definitive jump is independence from
external opportunity: the node that developed both stops waiting for the window
and starts generating its own opportunities.

**I.4 The opportunity window.** Opens when there is balance between quantitative
and qualitative resources — enough knowledge to exploit the opportunity and enough
material resources to execute it. Balance does not mean abundance in both; it
means neither brakes the other. Triggers can be external (an offer, market shift,
contest, crisis) or internal (reaching a level of skill or maturity). *Repetition
cycle:* if the jump happens without the necessary intrapersonal maturity, the
system forces the node to repeat the experience (internally — it cannot sustain
the position; externally — the environment reconfigures conditions until the node
faces the same challenge again). The real event horizon is not time alone but
crossing the minimum threshold in either dimension.

**I.5 The satellized node's escape route.** A shadow node inside an extractor hub
has an escape route that does not depend on the hub changing. If it has kept
qualitative development — even partial — it can activate networks external to its
social nucleus to compensate for the scarcity of quantitative resources. This is
the χ coefficient (Relational Interface) at the Micro level: the ability to
identify actors outside the extractor hub who can provide the quantitative
resources the hub does not give equitably. This confirms the model's fundamental
hierarchy: the qualitative resource is the strategic asset that opens every escape
route.

**I.6 Micro-module variables.** **RQ (Quantitative Resources):** financial
capital, available time, access to material tools; directly measurable;
extractable. **RL (Qualitative Resources):** knowledge, skills, intrapersonal
maturity, judgment; inherent, not directly extractable but degradable by lack of
practice (degradation rate proportional to RQ scarcity over prolonged periods).
**Ck (Coherence Factor):** balance between technical specialization and everyday-
environment coherence. **DI (Intrapersonal Dimension):** maturity, cognitive
humility, stability under pressure — necessary to sustain the jump. **DP
(Professional Dimension):** technical positioning and market access — sufficient
to execute but not to sustain without DI. **χ_micro:** ability to activate
networks external to the extractor hub to offset RQ deficit; proportional to
available RL. The Atomic Node fails not for lack of quantitative resources alone,
but when qualitative degradation crosses the minimum threshold needed to identify
the orthogonal dimension of the jump.

## Module II: Meso Resolution — The Intra-national System

The Meso system is a closed ecosystem bounded by geopolitical border, corporate
jurisdiction or institutional structure, operating under controlled parasitism:
the Central Hub does not seek to destroy Shadow Nodes but to keep them in
sustainable extraction guaranteeing continuous flow to the center.

**II.1 Hub ↔ Orchestrator Node.** The Orchestrator is not a satellized shadow
node but a deliberate receptor of the hub's overflow. When the hub exceeds K_max
(environmental contingency, transport/communication deficiency, logistic
saturation), it transfers capital, talent and communication infrastructure to the
Orchestrator to absorb that pressure. The relation is functional symbiosis, not
pure extraction — the only Meso relation where flow is bidirectional with mutual
benefit. Querétaro absorbing CDMX's industrial overflow is the clearest empirical
case.

**II.2 Hub stability — Law of Internal Irreversibility.** The Central Hub is
practically immovable from inside the Meso system. Even if an Orchestrator
surpasses it on some indicators, it will hardly usurp it, because that would
require a complete network reorganization — redesigning the dependencies of all
orbiting nodes, not just beating the hub on one metric. Displacing the hub
requires an event that incapacitates the system at the infrastructure,
communications or decision level. Triggers can be exogenous (catastrophes,
systemic conflicts) or endogenous: the Zwin Canal silting that incapacitated
Bruges was internal infrastructure degradation; Philip II's decree moving the
court from Toledo to Madrid was an internal political decision. Exogenous triggers
produce abrupt reorganization (high b); endogenous ones produce gradual
reorganization (low b); both produce the same end — a new hub — via mathematically
distinct trajectories.

**II.3 Node reclassification — hierarchy by function.** The Meso hierarchy is
fixed not by identity but by productive function. A displaced former hub does not
vanish — it reintegrates at the level matching its current production (Bruges as
cultural tourism, Toledo as museum-city, still generating flow). Reclassification
is bidirectional: a Shadow Node can ascend within the Meso system without the
dimensional leapfrog, via continuous production growth under the system's rules —
slower and more resource-costly than the orthogonal jump because it competes under
the hub's rules.

**II.4 The hub's immune response.** The hub does not trigger its immune response
to any growth of a lower node. The trigger is not the node's size but the
*direction* of its growth: if it grows to serve the system better (more
production, more resources to the hub), no threat — the hub incentivizes it. If it
grows to reorganize the system or compete for network control, the immune response
activates (regulatory capture, legislation, hostile acquisition). Continuous,
sustained, gradual growth — not bursty — is precisely what passes undetected,
allowing a Shadow Node to accumulate critical mass before the hub reacts. This is
the most viable internal-ascent strategy.

**II.5 Growth under extraction — the paradox resolved.** The Shadow Node needs
resources to grow but the hub continuously extracts some. The resolution is not to
compete for the extracted resources but to invest strategically in the node's own
deficiencies to generate more production with what remains after extraction. The
investment must hit the node's specific bottlenecks and be simultaneously
quantitative and qualitative (housing infrastructure in a quiet zone = quantitative
growth; the value proposition of tranquility = the qualitative component;
developing industry requires the telecom infrastructure to support it). A node
that correctly identifies and attacks its structural deficiency can grow even
under continuous extraction.

**II.6 Horizontal competition.** Real only when same-level Shadow Nodes compete
for the same market or resource. Two shadow nodes with distinct growth sources
(one agrarian, one textile) do not compete and can grow simultaneously. Strategic
implication: a node that finds a growth source distinct from its neighbors
eliminates horizontal competition automatically — the least-friction path for
internal ascent.

**II.7 Hub expansion mechanisms.** Three modalities of differing speed, cost and
stability. *Silent Absorption by economic attraction:* slowest but most stable —
border nodes between two systems gradually orient their economy toward the
neighboring hub (trade, labor flow, consumption) until real economic dependence no
longer matches their original hub; absorption happens functionally before the
political map changes; no immune resistance because the node stays within formal
jurisdiction. *Peaceful Expansion by agreement:* the hub offers advantageous
enough conditions for voluntary integration — low political cost, minimal
resistance. *Legal or violent expropriation:* fastest but most resource-costly and
least stable — generates active resistance requiring continuous pressure. There is
a logical progression: silent absorption first, then agreement, expropriation only
as last resort (Toledo-Madrid = political decree; Bruges-Antwerp = infrastructure
degradation; contemporary border absorptions illustrate different points).

**II.8 Meso-module variables.** **K_max:** the hub's logistic limit above which it
overflows toward Orchestrators (measurable as the inflection point where marginal
absorption cost exceeds marginal extraction benefit). **w_ij_meso:** extraction
rate from Shadow Node to hub (GDP-pc differential, net labor migration, FDI).
**I_hub:** non-linear immune-response rate, activated by the *direction* of
threatening growth. **χ_meso:** informal ties reducing extraction friction or
granting hub-resource access outside formal channels. **DF:** the node's specific
structural deficiency; the growth-maximizing investment under extraction is the
one attacking DF directly with quantitative + qualitative resources together. In
the Meso system the hub is not the enemy of growth — it is the ceiling of *linear*
growth; surpassing the ceiling needs a dimension where the system's rules do not
apply.

## Module III: Macro Resolution — The Collision of Superorganisms

The Macro system is competition between complete fungal networks: nations,
economic blocs, technological ecosystems. Unlike the Meso system, the actors are
sovereign — no entity above arbitrates with real executive power. International
regulators (UN, WTO, IMF) exist but cannot compel high-gravitational-mass
superorganisms. Rule compliance is strategic, not moral.

**III.1 Gravitational mass.** A superorganism's relative position is set by a
composite of four variables: total GDP, population density, technological level,
territorial area. This determines the possible competition type: horizontal
(comparable masses, neither can easily absorb the other) or vertical (unequal
masses, the larger has structural advantage from the start). A low-mass
superorganism cannot compete vertically in the same dimensions — its only viable
option is leapfrog to a dimension where the rival's accumulated mass does not
apply. High-mass superorganisms can more easily ignore sanctions (the cost is
absorbable by their internal network); low-mass ones comply not from conviction
but because the cost of defiance exceeds their resistance capacity. Those who
perceive international rules were designed to preserve the incumbents' advantage
have a rational incentive to ignore them — the system's rules are part of the
macro-scale satellization mechanism.

**III.2 The real brake on expansion — the internal network.** What truly brakes a
dominant superorganism's expansion is not international regulators but its own
internal node network. Sanctions hit first the internal nodes dependent on foreign
trade, imported technology or external financing; if they weaken, the internal
network weakens and the hub loses its base. A superorganism's real strength is not
just total GDP but the robustness of its internal network — how resilient its
nodes are to external pressure. It can sustain prolonged sanctions only if its
internal network is self-sufficient enough to absorb them without collapse.

**III.3 Leapfrog at Macro scale.** Between two comparable-mass superorganisms in
horizontal competition, the one that leapfrogs first ends with long-term
advantage — not the largest or most populous, but the one that identifies and
occupies a new dimension before preferential attachment consolidates. Estonia
(digital tech hub), Ireland (European fiscal/tech hub) and South Korea (precision
manufacturing + digital culture) are empirical instances of relatively small-mass
superorganisms that jumped to dimensions where larger ones had no accumulated
advantage. The operative sequence has two mandatory steps: first reduce the
critical bottlenecks to minimum viable (not fully solve them — that would consume
all resources before the jump); second invest concentratedly in specific points
where the superorganism already has a latent unexploited advantage.

**III.4 The dominant superorganism's strategy.** Detecting a rival jumping to a
new dimension creates a resource dilemma: it cannot abandon what made it dominant
(it would lose its base) nor ignore the new dimension (the rival would consolidate
preferential attachment there). The viable strategy is the simultaneous double
move: anchor and protect historical advantages while simultaneously attacking its
own deficiencies in the new dimension — an expansion, not a full pivot. Miscalibrating
the proportion loses on both fronts.

**III.5 The border node — bilateral strategy.** Border nodes between two
superorganisms are the most vulnerable in the Macro system but have an opportunity
interior nodes lack: simultaneous access to two systems with different needs. The
viable strategy is bilateral diversification: offer distinct, non-interchangeable
products/services to each neighbor, creating differentiated dependence in both.
Neither can easily absorb it without losing exclusive access to what the node
offers. The limit is kinetic rupture: if the two superorganisms enter direct
conflict, neutrality is the only viable defense (Switzerland = sustained
neutrality; Ukraine = neutrality's collapse when kinetic rupture reaches the
node's territory, where gravitational mass decides).

**III.6 The Atomic Node in the Macro system.** The Atomic Node can develop
economic, cognitive and dimensional independence — operate in global markets from
any location — but never fully escapes the Macro system because its legal
existence, tax regime and institutional protection are anchored to the
superorganism where it resides. It can change fiscal residence or migrate to a
more favorable superorganism (itself a Macro-level leapfrog) but is always inside
some superorganism. This is the upper limit of individual autonomy in the triple-
resolution model.

**III.7 Inter-scale interaction principles.** *Cascade Transmission:* Macro-scale
events (pandemics, wars, large disasters, global financial crises) hit all three
systems but not simultaneously — they cascade downward (Macro → Meso → Micro), at
a speed depending on how integrated each level is. An Atomic Node with high
dimensional independence feels the impact later and weaker — which is why
individuals with greater cognitive autonomy and lower physical-infrastructure
dependence best survive global exogenous shocks. *Scalar Velocity:* a system's
cycle time is inversely proportional to its hierarchical level. The Atomic Node
completes a full cycle (identify deficiency, invest, jump) in hours or weeks (the
HackerEarth 2026 case: a full cycle in 13.5 hours); a Shadow Node takes years or
decades; a superorganism takes generations. The Atomic Node thus has more
iteration opportunities than any higher-level entity — speed is the Micro level's
structural advantage.

**III.8 Macro-module variables.** **MG (Gravitational Mass):** composite of total
GDP, population density, tech level, area. **RI (Internal Robustness):** node-
network resilience to external pressure — the real brake on aggressive expansion.
**DB (Bilateral Differentiation):** degree to which a border node offers distinct,
non-substitutable goods to each neighbor — high DB = more autonomy. **TC (Cycle
Time):** TC_micro < TC_meso < TC_macro, differing by orders of magnitude (hours vs
years vs generations). **Ω_cascade:** how a Macro exogenous event transmits to
Meso and Micro with delay and damping proportional to each node's dimensional
independence. The Atomic Node's autonomy has a ceiling no skill can surpass: legal
dependence on its resident superorganism. The highest leapfrog available to an
individual is not cognitive but geographic — choosing the superorganism whose
rules maximize operation in the dimension where they want to grow.

## Module IV: Application to the Business Domain

SNT is not exclusive to geographic systems or individuals. The HackerEarth 2026
case showed the same satellization algorithm operating in digital business
ecosystems: the 7,478× Fractal Gap between Elite and Basic users, the 5-Event Wall
as a collapse threshold, and the cognitive leapfrog via AI-agent adoption.
Applicability condition: any firm with operational databases can apply the model —
not sector or size, but the availability of data to measure flows between nodes.

**IV.1 Two scales.** *Intra-corporate (Business Meso):* in a matrix-structured
corporation the parent company is the Central Hub (Level 0); regional subsidiaries
are nodes at different levels by their business gravitational mass (robust,
autonomous subsidiary = Level 1; small, decision-dependent operation = Level 3).
Extraction via profit transfer to the parent, centralization of strategic
decisions, and high-density talent migration from periphery to center. Intra-
corporate satellization is structural, not pathological — it maintains corporate
coherence. *Inter-corporate (Business Macro):* same-sector firms competing
constitute a business Macro system; horizontal (comparable mass) or vertical
(significant asymmetry). AWS vs Oracle in cloud, Google vs Yahoo in search,
language models across companies. The same preferential-attachment laws apply:
whoever first establishes advantage in a new dimension consolidates it via the
network effect before rivals can match it.

**IV.2 Business satellization metrics.** Five base metrics analogous to
HackerEarth's CSI V3, applicable to any firm with structured data: *Generated Data
Volume* (≈ credits_used) — each node's output; *Sustained Activity* (≈ active_days)
— continuous operation vs nominal existence; *Response Time* (≈ T2ST) — reaction
speed to new demands; *Functional Diversity* (≈ Tool Count) — the business
5-Event Wall is the minimum diversity below which obsolescence probability exceeds
90%; *Failure Resilience* (additional) — error reporting and resolution time,
capturing the node's Coherence Factor (Ck). Combined they form the Composite Score
Index Enterprise (CSIE), which classifies any company component into the SNT v2.0
five-level taxonomy, identifies the internal Fractal Gap, and detects nodes on an
irreversible satellization trajectory before it is hard to reverse.

**IV.3 Prescriptive use — from diagnosis to intervention.** Three sequenced
interventions: (1) *Orthogonal Technological Innovation* — identify the tools the
lagging node lacks that would let it operate where the hub has no accumulated
advantage (specific to the bottleneck, not generic tech); (2) *Homogenization of
lagging nodes* — bring lower-level nodes to minimum viable so they can join the
collective jump (enablement, not leveling); (3) *Projection and execution of the
jump* — execute the leapfrog when the window is open and resources suffice to
sustain it (too early = premature-execution failure; too late = thermodynamic
failure past the event horizon). Continuous improvement closes the loop: each
successful jump redefines the base state from which the next bottleneck and
orthogonal dimension are identified.

**IV.4 HackerEarth as the prototype.** The HackerEarth 2026 dataset (4,774 users,
409,287 events on the Canvas platform) was the first empirical demonstration of
SNT applied to a complex business system: a hub (the platform and its ranking
mechanisms), Elite nodes concentrating value, Basic nodes providing activity
without retaining proportional value. The 7,478× Fractal Gap in VDR is Pareto in
its most extreme form (99.5/0.5, not 80/20). The 5-Event Wall (<5 distinct event
types → >90% churn) is the business analogue of minimum functional diversity. The
key finding — that the dominant retention predictor is not usage volume but
AI-agent adoption (agent_accept_suggestion, SHAP importance ~0.5) — empirically
confirms the cognitive leapfrog is already happening in real time: those who
delegate execution to the agent and position as orchestrators escape
satellization; those who keep executing linearly are absorbed. Any firm measuring
its teams' AI-agent adoption is indirectly measuring resistance to cognitive
satellization. The model does not distinguish a nation, a firm or an individual —
it distinguishes nodes that accumulate advantage from nodes that transfer it.

## Module V: Empirical Verification of Previously Unproven Variables

This section integrates evidence from cognitive neuroscience, organizational
psychology, industrial economics and historical sociology to verify elements
previously marked as working hypotheses.

**V.1 Scalar Velocity Principle (TC_micro < TC_meso < TC_macro).** *TC_micro:*
generative AI reached 1.2 billion users in under three years — the fastest
individual adoption ever, beating smartphone (3 yr to 1 bn), internet (7 yr), TV
(13 yr); the project's own HackerEarth 2026 case documents a full cycle in 13.5
hours. Range: hours to months. *TC_meso:* firms normally take 1–5 years for
significant tech-adoption cycles; the COVID-19 extreme compressed a normally
one-year cycle to 11 days under existential pressure. Range: months to years.
*TC_macro:* internet took 30+ years (ARPANET 1969 → mass adoption 2000s); the
most-documented national leapfrog, M-Pesa in Kenya, took 4 years to 70% national
penetration. Range: years to decades. TC_micro is 10–100× faster than TC_meso,
which is 10–30× faster than TC_macro. The North/South AI-adoption gap (~2× faster
in countries above 20,000 USD GDP pc) confirms gravitational mass sets national
adoption speed.

**V.2 Hub immune response — Kill Zones and killer acquisitions.** GAFAM completed
855+ acquisitions through Aug 2020 with none blocked by antitrust regulators. The
OECD formally recognized "killer acquisitions" (eliminating potential competitors
before critical mass) as a systematic risk. The mechanism evolved to evade
antitrust: Microsoft paid $650M to Inflection AI in 2024, hiring nearly its entire
founding team without a formal acquisition — a pseudo-acquisition achieving node
absorption without triggering merger-review thresholds (the business analogue of
the mathematical bypass). The Kill Zone goes further: the mere presence of large
platforms in a sector reduces VC funding to adjacent startups even when they are
not acquired — preventive immune response that suppresses growth before the
detection threshold, confirming the non-linear scaling prediction.

**V.3 Qualitative-resource degradation — skill decay.** A meta-analysis of 53
studies (189 independent data points) quantifies it: d = −0.01 immediately after
training, rising to d = −1.4 after 365+ days without use — two orders of magnitude
in a year. Complex cognitive tasks decay faster than physical ones; in language,
vocabulary deteriorates first while grammar and phonology are more stable (high-
specificity qualitative resources are more vulnerable). Implication for the Micro
module and HackerEarth: excessive use of AI agents to execute tasks the individual
could do produces cognitive atrophy in the delegated skills. The same mechanism
that is the cognitive leapfrog (delegation to free executive bandwidth) becomes
second-order satellization if one delegates without maintaining practice. Critical
distinction: delegate execution while keeping understanding (orchestration) vs
delegate understanding (satellization). The first is the leapfrog; the second is
the trap.

**V.4 Coherence Factor Ck — Free Energy Principle (Friston).** Karl Friston
formalized the Free Energy Principle as the unifying mechanism of brain function
(Nature Reviews Neuroscience, 2010): the brain constantly minimizes variational
free energy — the discrepancy between its predictions and actual sensory input. A
highly entropic environment (chaos, constant interruptions, unpredictability)
forces the brain to spend excess ATP recomputing predictions, depleting the
prefrontal cortex and depressing executive functions. Cognitive Load Theory
(Sweller) and Attention Restoration Theory (Kaplan) complement it: a chaotic
environment generates extraneous cognitive load that consumes working-memory
bandwidth otherwise available for germane load (real productivity). Implication:
Ck is not a fuzzy psychological variable — it is the measure of cognitive
bandwidth available for executive function after subtracting the metabolic cost of
processing environmental chaos.

**V.5 The two jump dimensions — Psychological Capital (PsyCap).** Fred Luthans
developed PsyCap across four empirical dimensions: Hope (agency + alternative-path
planning), Self-efficacy, Resilience, Optimism. The Avey, Reichard, Luthans &
Mhatre meta-analysis (2011, HRDQ, 22, 127–152; 51 samples, N=12,567) showed
positive, significant relations between PsyCap and job performance across self-,
supervisor- and objective measures — exceeding traditional human capital
(technical education and experience). Bandura's self-efficacy provides the
mechanism: perceived self-efficacy determines what goals the individual sets, how
much energy they invest, how long they persevere — the psychological equivalent of
the activation threshold (E_a). Critical for the Micro module: PsyCap is a malleable
state, not a fixed trait — 1–3 hour training interventions produce measurable
gains, confirming intrapersonal development is incrementally buildable.

**V.6 Hub-expansion sequence — Principle of Least Action.** The hub's progression
(silent absorption → agreement → expropriation as last resort) is not cultural but
thermodynamic: all expansive systems seek the least-resistance, least-energy
configuration (physics' Principle of Least Action). The Spanish Empire in America
verifies it: co-opting local elites (encomiendas, indigenous cabildos,
collaborationist cacicazgos) acted as an enzymatic catalyst — lowering the
activation energy for assimilating new territories by turning local actors into
hub agents without direct military cost (the analogue of shared electrons in a
covalent bond). Violent expropriation and force-maintained order, by contrast,
produced metastable states that collapsed under their own institutional and
financial weight — exactly what the Gibbs free-energy equation predicts for high-
enthalpy processes: fast but thermodynamically unsustainable without continuous
external energy input.

**V.7 Silent absorption between superorganisms.** Post-WWI Hungarian counties at
twice the distance from the new international border showed 0.751 percentage points
more urbanization than border counties — proximity to the neighboring hub
reorients economic development before any formal jurisdiction change. Crimea 2014:
northern Russian regions bordering Ukraine lost market access when Ukraine closed
crossings; southern regions gained access when Crimea integrated into the Russian
system. In both cases economic flow reconfigured before political resolution was
final — silent absorption precedes institutional formalization.

**V.8 Verification status.** *Verified with own quantitative data:* the four SNT
v1.0 historical cases (power-law fit, Maddison), the Mexico 32-entity N-body matrix
(INEGI 2022, power law p<0.001), the eight 1940-2022 trajectories (Querétaro and
Nuevo León with significant b<0), and HackerEarth 2026 (ROC-AUC=0.9994, SHAP).
*Verified with external scientific literature:* Scalar Velocity, Hub Immune
Response (GAFAM 855 acquisitions, Kill Zones, pseudo-acquisitions), Qualitative
Degradation (53-study meta-analysis, d=−1.4 at 365+ days), Coherence Factor Ck
(Friston 2010), the Two Jump Dimensions (PsyCap meta-analysis N=12,567, Avey et
al. 2011), Hub-Expansion Sequence (Spanish Empire, Least Action), Silent
Absorption (Hungary border data, Crimea 2014). *Updated in Module XII:* the ASI is
operationalized with observable behavior from HackerEarth 2026 (N=4,774); its
three components (δH, α, F) have measurable proxies, classification precision 1.0
(zero false positives), Spearman ASI–CSI_V3 = 0.178 (p<0.001). The framework maps
the immutable laws of energy conservation, information thermodynamics and complex
networks onto human and institutional behavior.

## Module VI: Refutation Criteria — SNT v2.0

A scientific framework must specify the conditions under which its postulates would
be false. Six (plus one) refutation criteria, each refuting a specific postulate
under specific conditions.

**RC1 — Scalar Velocity.** Postulate: cycle time is inversely proportional to
hierarchical level. *RC1a:* refuted if a technology is systematically adopted
faster by Meso systems (firms) than by Atomic Nodes (individuals) in the same
context (must be systematic, not an isolated early-institutional case). *RC1b:*
partially refuted if a technology class requires institutional infrastructure
individuals cannot acquire (quantum computing, fusion, low-latency satellite nets),
where TC_macro could match or beat TC_micro. Declared applicability: holds for
individually accessible digital technologies; other classes need independent
verification.

**RC2 — Hub immune response.** Refuted if dominant hubs systematically incorporate
peripheral-node capabilities without acquiring or eliminating them — adapting
their own structures to assimilate the node (e.g. Linux, developed by resourceless
peripheral nodes and eventually adopted by the dominant hubs that originally
competed against it). The response is conditional: it activates when the node
competes on the hub's plane; it inverts when the node complements a capability the
hub lacks. If inversion is more frequent than suppression, the postulate (immune
suppression as the hub's dominant behavior) is refuted.

**RC3 — Inextractability of qualitative resources.** Refuted if a hub can
systematically neutralize the differential effect of a node's knowledge via three
indirect mechanisms: brain drain (conditions that make the node migrate voluntarily
with its knowledge), reverse engineering (replicating the knowledge by observing
the node's process), or deliberate saturation (providing enough quantitative
resources that the node stops applying/developing the threatening knowledge,
freezing its advantage). The condition is not raw extraction (impossible) but
neutralizing the differential effect at systematic scale.

**RC4 — Dual minimum-threshold condition.** Leapfrog requires both RQ and RL above
their respective minimums to be executable and sustainable. Refuted if a *sustained*
leapfrog is documented with RQ or RL below its operational minimum. Without minimum
RL the node can reach the new position but cannot sustain it; without minimum RQ it
has the maturity to sustain but cannot execute. No requirement of perfect RQ–RL
balance — only presence of both above their minimum.

**RC5 — Hub-expansion sequence.** Silent absorption → agreement → expropriation
(Least Action). Partially refuted if hubs that jumped straight to violent
expropriation achieved long-term stable states without sustained energy cost
(genuine integration, not temporary submission). Available cases (Tenochtitlan
1521, Kuwait 1990, Ukraine 2022) show the opposite — persistent structural
resistance. Declared applicability: the hub makes a rational cost-benefit
calculation; when time is the critical resource (a rival hub may close the window),
the calculation can invert and direct expropriation may be the first option despite
its high enthalpic cost. Fully refuted only if direct expropriation is shown to
produce more stable, lower-maintenance states than silent absorption for the same
node class.

**RC6 — Irreversibility of satellization.** Satellization is irreversible without
an exogenous intervention of scale comparable to the original trigger; a Shadow
Node cannot reverse it from inside without the hub simultaneously in internal
collapse. Refuted if a Shadow Node reversed satellization from inside meeting three
simultaneous conditions: no comparable-scale exogenous trigger; the hub not in
internal collapse (operating below K_max throughout); and the restructuring
completed without external actors. Strict because cases like Singapore-Malaysia
(1965) do not satisfy it (Malaysia had severe internal tensions reducing its
immune response — partial hub collapse). Internal reversion is technically possible
but its practical viability is extremely low.

**RC7 — ASI operationalization.** ASI > 1 identifies nodes with operative cognitive
sovereignty. Verified empirically in Module XII (HackerEarth 2026). Refuted if
ASI > 1 users systematically show performance comparable to ASI < 0.5 users on
tasks requiring cognitive sovereignty (orthogonal-dimension identification, new-
tool adoption under pressure, performance under adversity). Current validation
precision 1.0 (zero false positives) is promising but needs replication.

**VI.7 Implication.** No single criterion refutes the whole model — each refutes a
specific postulate under specific conditions, so the model can be partially
correct. RC1b, RC2, RC3 and RC6 are the four empirical questions most likely to
change the model. A model that cannot be refuted is not science but narrative; SNT
v2.0 defines exactly what would have to be true for it to be wrong.

## Module VII: Glossary (consolidated reference)

Consolidates all variables and concepts defined in detail in the modules above.
**Fundamental concepts:** *Satellization* (R(t)=a·t^b, b>0); *Leapfrog* (escape via
an orthogonal dimension where the hub has no accumulated advantage; needs minimum
RQ and RL); *Preferential Attachment* (Barabási-Albert 1999); *Fungal Network*
(living distributed information ecosystem, biological analogue of the Meso system);
*Trigger* (abrupt b>0.45 vs gradual b<0.45); *Event Horizon t_horizon* (point of no
return where residual energy falls below the activation threshold; leapfrog must be
in [t_min, t_horizon]). **Micro variables:** RQ, RL (decay d=−0.01 → −1.4 at 365+
days), DI (PsyCap), DP, Ck (Friston), χ_micro, ASI = (δH·α)/F (threshold ASI>1,
precision 1.0, Spearman with CSI_V3 = 0.178), δH (Elite 0.808 / Inter 0.498 / Basic
0.199), α (0.666 / 0.397 / 0.199), F (0.206 / 0.434 / 0.711), Sovereignty (ASI≥1,
only 0.27% of users). **Meso variables:** K_max, w_ij, I_hub (GAFAM evidence), DF,
χ_meso. **Macro variables:** MG, RI, DB, TC (micro<meso<macro), Ω. **Node taxonomy
quick reference:** Level 0 Central Hub (CDMX, 14.8% of national GDP); Level 1
Secondary Attractors (Nuevo León b=−0.058); Level 2 Orchestrator (Querétaro
b=−0.155, aerospace leapfrog); Level 3 Shadow Node (Tlaxcala b=0.147, compound
gradient 243.0k MXN = 9.3× the binary model); Exogenous (Campeche oil, Quintana Roo
tourism); Atomic Node (HackerEarth Elite, 0.05 percentile, 13.5-hour cycle).

## Module VIII: Diagnostic Protocol — Applying the Model

A domain-independent four-step protocol. **Step 1 — System identification and
level classification:** define the reference system (who is the Central Hub, which
are the nodes, which node is analyzed), gather the node's output/production data
(≈ RQ, or GDP pc) and compare with the others. Fit f(rank)=a·rank^b in log-log; if
R²>0.7 and p<0.05 the system operates under preferential attachment and the model
applies. Classification: Level 0 = upper outlier; Level 1 = above mean, below
outlier; Level 2 = near mean, above-mean growth; Level 3 = below mean, below-mean
growth; Level E = exogenous growth source. **Step 2 — Extraction gradients:**
compute w_ij for each relevant node pair (GDP-pc differential / productivity
differential / available-resources differential). Compute the *compound* gradient
if multiple hubs extract simultaneously — the most common error is measuring only
the immediate hub and ignoring the long-range one (Tlaxcala: long-range 216.8k MXN
is 8.3× the direct 26.2k MXN; the compound total is what matters for strategy).
**Step 3 — Event-horizon estimation:** fit the power law to the available series;
b>0 = satellization (growing gap), b<0 = convergence, b≈0 = steady state. If b>0,
estimate t_horizon = min{t | E_res(t) ≤ E_a}; as a proxy, use the point where the
gap becomes irreversible (typically ratio > 3–4× in the Mexican case). If b<0,
identify the convergence mechanism (Querétaro b=−0.155, Nuevo León b=−0.058 — both
via dimensional jumps to sectors where CDMX had no prior advantage). **Step 4 —
Orthogonal-dimension identification:** find dimensions where the hub has no
accumulated advantage via three criteria: (1) the hub has not invested
significantly there in 5–10 years; (2) the node has a measurable initial advantage
there (even small); (3) the dimension has preferential-attachment potential. Verify
it does not require hub-controlled infrastructure (RC1b) — otherwise the jump is
neutralized at the distribution stage. Then design the three-phase intervention
(Module IV). The protocol does not guarantee leapfrog success; it guarantees the
when/where decision is made with data, not intuition — the difference between
nodes that jumped and those that did not was usually not lack of resources but lack
of clarity about the right dimension at the right time.

## Module IX: Dialogue with the Complex-Systems Literature

**IX.1 Barabási & Albert (1999) — Preferential Attachment and Scale-Free
Networks** (Science, 286, 509-512): real networks follow a power law where a few
nodes concentrate most connections ("the rich get richer"). SNT uses this as the
base of the satellization algorithm and extends it: it quantifies satellization
*speed* via the exponent b on historical time series, and proposes a five-level
node taxonomy based on resource-processing/retention function, not just degree.
INEGI data confirm the Mexican national system follows the predicted distribution
(b=−0.473, R²=0.838, p<0.001).

**IX.2 Watts & Strogatz (1998) — Small-World Networks** (Nature, 393, 440-442):
high clustering with short path lengths. SNT adds the directional dimension:
two nodes can be close in connection distance yet in radically different SNT
hierarchical levels — one satellizing the other despite proximity. Clustering
measures local connection density, not the direction of resource flow.

**IX.3 Holland (1995) — Complex Adaptive Systems** ("Hidden Order"): simple agents
with local rules generate unpredictable emergent global behavior (aggregation,
non-linearity, flows, diversity). SNT operates within the CAS frame but specifies
satellization as one recurrent emergent dynamic: when two nodes of differing
gravitational mass orbit in critical proximity, preferential attachment generates a
mathematically predictable trajectory. Predictability is SNT's original
contribution relative to Holland's intrinsic-unpredictability description.

**IX.4 Friston (2010) — Free Energy Principle** (Nature Reviews Neuroscience): any
persisting living system minimizes variational free energy. SNT v2.0 extends it
beyond the individual brain to social systems: the hub's immune response, the
Coherence Factor Ck, and second-order satellization are manifestations of the same
principle at different scales — persisting systems concentrate energy flows toward
the nodes that best minimize the prediction–environment discrepancy. Satellization
is the aggregate result of that systemic optimization.

**IX.5 Brezis & Krugman (1993) — Technological Leapfrogging** (Journal of
International Economics): in periods of incremental innovation accumulated
experience reinforces leadership; in periods of radical innovation that experience
becomes a liability (the leader has a higher abandonment cost than the laggard with
nothing to abandon). SNT extends it to three simultaneous scales and formalizes the
leapfrog *failure* conditions (Modules I and VI) — answering why many nodes do not
jump even when the window is open (event horizon, activation energy, dual minimum
threshold). SNT v2.0 does not compete with the complex-systems literature — it
extends it, integrating established mechanisms into a unified, falsifiable
prediction: any node's satellization speed follows a power law with an exponent
estimable from historical data.

## Module X: Bibliographic References

*Networks and complex systems:* Barabási & Albert (1999), Science 286(5439),
509-512; Watts & Strogatz (1998), Nature 393(6684), 440-442; Holland (1995),
*Hidden Order*, Addison-Wesley; Strogatz (2001), Nature 410(6825), 268-276.
*Cognitive neuroscience and psychology:* Friston (2010), Nat. Rev. Neuroscience
11(2), 127-138; Avey, Reichard, Luthans & Mhatre (2011), HRDQ 22(2), 127-152;
Bandura (1997), *Self-efficacy*, W.H. Freeman; Sweller (1988), Cognitive Science
12(2), 257-285; Kaplan (1995), J. Environmental Psychology 15(3), 169-182.
*Economic history and development:* Bolt & van Zanden (2024), Maddison Project
Database 2023, U. Groningen; Brezis & Krugman (1993), American Economic Review
83(5), 1211-1219; Ringrose (1973), J. Economic History 33(2), 284-314; Van der Wee
(1963), *The Growth of the Antwerp Market*, Nijhoff; Gelderblom (2013), *Cities of
Commerce*, Princeton UP; Costa, Palma & Reis (2015), European Review of Economic
History 19(1), 1-22. *Industrial economics and digital competition:* OECD (2020),
*Start-ups, Killer Acquisitions and Merger Control*, DAF/COMP(2020)5; Furman et al.
(2019), *Unlocking Digital Competition*, HM Treasury; World Bank (2022), *Technology
Adoption in the Developing World*. *Own empirical data:* INEGI (2022), GDP per
capita by federal entity; Zainos Corona (2026), Shadow Node Theory Replication
Package v2.0, Zenodo 10.5281/zenodo.19131327; SSRN pre-print 6418778.

### 2.1 The Mechanism: Matthew Effect and Pareto Distribution

The central mechanism is cumulative advantage (the Matthew Effect / preferential
attachment). Once a dominant node gains an initial 10–15% advantage, the
opportunity cost of investing in the historical node becomes mathematically
prohibitive. This produces the 80/20 Pareto distribution: 80% of future resources
flow to 20% of nodes. The system self-perpetuates via three suppression vectors:
*Legal* (regulations acting as a firewall — investment prohibitions, asymmetric
rules); *Logistic* (physical-infrastructure bypass — rail diversions, trade
routes); *Gravitational* (human-capital flight toward the larger center of mass).

### 2.2 The Fractal Pattern: Four Comparative Cases

The theory is validated by identifying the same pattern across four completely
distinct historical and geographic contexts, separated by centuries and continents:

| Case | Shadow Node | Dominant Node | Trigger | Mechanism | Current Outcome |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Mesoamerican | Tlaxcala | Puebla | gradual accumulated advantage | Royal Decree 1535 / rail bypass 1873 | residential satellite; FDI ratio 25.5× |
| Castilian | Toledo | Madrid | pure political decree | court move 1561; Toledo loses 50% pop. by 1640 | museum city; 85k vs 3.4M |
| Flemish | Bruges | Antwerp | infrastructure collapse | Zwin canal silting c.1500; Bruges loses sea access | static UNESCO heritage |
| Iberian | Lisbon/Portugal | Madrid/Spain | external institutional vacuum | Iberian Union 1580; loss of Asia trade routes | 60 yrs of satellization until 1640 restoration |
| Digital (2026) | Basic users 93.1% | Elite 0.5% HackerEarth | behavioral Fractal Gap | <5 distinct event types, detectable in first session (5-Event Wall) | VDR ratio 7,478×; churn ROC-AUC 0.9994 |

Convergence across four cases with distinct activation mechanisms suggests the
suppression algorithm does not depend on the specific trigger but on the underlying
mathematical dynamic. Two trigger classes: *gradual accumulated advantage* (the
dominant node slowly builds advantage past the 10–15% threshold — Tlaxcala-Puebla,
Bruges-Antwerp; decades-to-centuries) and *exploited institutional vacuum* (an
abrupt institutional rupture opens a window — Toledo-Madrid 1561, Lisbon-Madrid
1580; punctual event, permanent consequences). Portugal-Spain is especially
valuable: satellization can occur between comparable-sized nodes given a power
vacuum. In 1580 Portugal was the world's leading naval power, yet King Sebastian's
heirless death (1578) and the defeat at Alcácer Quibir created a dynastic vacuum
Philip II exploited rapidly — absorbing the historical node in under two years
without a war of conquest; the mechanism was juridical and diplomatic, the
mathematics identical to the other three. *Toledo:* 56,270 inhabitants (1561) →
<25,000 (1640), −55% in under eighty years, while Madrid went from ~30,000 to
>150,000. *Bruges:* ~46,000 in the 14th century (the leading financial node of
northern Europe); by 1500, as the Zwin silted, Antwerp grew 33,000→55,000 while
Bruges contracted; the mechanism was physical, not political — the city simply
ceased to be accessible to deep-draft ships.

### 2.3 Quantitative Verification: The Four Cases with Maddison Data

Two independent analyses: INEGI/CONEVAL for Tlaxcala-Puebla (1993-2022), and the
Maddison Project Database 2023 to extend to the four cases with long historical
series, computing the power-law exponent and comparing satellization speed by
trigger type. **Velocity taxonomy (central result):** the four cases split into two
classes by divergence speed. *Class 1 — abrupt triggers* (Bruges-Antwerp,
Toledo-Madrid): mean b = 0.717, R²>0.87, p<0.001; super-linear power law. *Class 2
— gradual triggers* (Portugal-NW Europe, Tlaxcala-Puebla): mean b = 0.122,
R²=0.12-0.57; sub-linear, cumulative. The speed difference is 5.9× — abrupt
triggers produce nearly six times faster satellization; this number emerges from
the data, not assumed. **By case:** Bruges-Antwerp b=0.739, R²=0.868 (in 1300
Bruges was 4× Antwerp; by 1560 a 7:1 reversal favoring Antwerp); Toledo-Madrid
b=0.694, R²=0.924 (the best fit — pure political decree gives the mathematically
cleanest satellization); Portugal vs NW Europe b=0.060, R²=0.123 (low R² reflects
an oscillatory process — Brazilian gold caused partial recoveries 1700-1750; the
Netherlands already had 3,110 USD GDP pc vs Portugal's 1,290 in 1535, a 2.4× gap
before the 1580 Union, which accelerated and consolidated it); Tlaxcala-Puebla long
series (Maddison Mexico 1550-2022, INEGI-calibrated 1993) b=0.184, R²=0.567 (over
487 years the exponent converges to the gradual-trigger range; the gap amplifies
during Puebla's 1940-1980 industrialization as the 1873 rail bypass yields its
maximal cumulative effects; INEGI: Puebla 1993 advantage 48.8%, migration-divergence
r=0.9646, 2022 FDI ratio 25.5×). *Methodological note on Portugal:* the low R² is
information, not failure — Portugal is the only case with significant partial
recoveries (Brazilian gold), each followed by a larger collapse; the pattern is
oscillatory with a divergent trend (the Portugal-NW Europe gap multiplied 3.5×
between 1535 and 1913). Sources: Maddison Project Database 2023; Costa, Palma &
Reis (2015); INEGI/CONEVAL; Nicholas (1992), Van der Wee (1963), Gelderblom (2013);
Ringrose (1973), INE España.

### 2.4 The Leapfrog Strategy: Asymptotic Rupture

Simulations show it is impossible to close the gap competing linearly — Puebla's
accumulated advantage is insurmountable on the physical-infrastructure plane. The
only possible rupture is asymptotic: jump directly to a dimension where the
accumulated advantage does not yet exist. Verified successful leapfrogging cases:
Estonia (1991, economically destroyed, bet on digital infrastructure — now the
world's most digitalized country per capita); Rwanda (no traditional industry,
built an African tech hub via fiber optics); Medellín (from the world's most
violent city to a Latin American innovation hub in 15 years); Ireland (London's
backyard that surpassed UK GDP per capita via fiscal and technological strategy).
Proposal for Tlaxcala: become a high-quality-of-life, high-connectivity refuge for
the knowledge economy, operating in the cloud rather than on the ground — hacking
the neighboring giant's gravity by operating in a dimension where its accumulated
advantage does not apply.

### 2.5 Digital-Domain Validation: HackerEarth 2026 (Fractal Core Framework)

The same dynamic operates in a completely different domain: user-behavior data on a
technology platform, in real time, at individual-event resolution. The experiment
is the Fractal Core Framework (Captain 1n2a1n05) on the zerve_hackathon_dataset.csv.
**Dataset and pipeline:** 409,287 events from 4,774 unique users on HackerEarth
Canvas, 141 distinct event types. Fractal Core V3 processes them in five layers:
Ingestion (4,774×287 pivot matrix — each user a vector of event frequencies);
Feature engineering (Shannon entropy of the per-user event distribution,
interaction velocity, time-to-second-tool T2ST, and the VDR indicator — Velocity of
Dimensional Rotation); Scoring (CSI V3 = tool diversity 0.4 + retention/lifetime
0.3 + VDR 0.3, scaled to 100 with a 1.5× resonance boost for AI-native users);
Classification (Elite top 0.5%, Intermediate next 6.4%, Basic remaining 93.1%);
Prediction (GradientBoostingClassifier on 284 event features, stratified, balanced
class weights). **The Fractal Gap:** the gap between the 0.5% Elite and 93.1% Basic
is not a continuous gradient but a discontinuity — a qualitative jump, not
quantitative. Numerically: mean VDR Elite 47.86 vs Basic 0.0063 (ratio 7,478×);
active days 30.9 vs 1.2 (25×); tool diversity 8.5 vs 0.08 types (106×); credits
consumed ~6,000×. The churn model gives ROC-AUC = 0.9994 (test), 1.0000 (5-fold
CV). The 5-Event Wall: users with <5 distinct event types have >90% churn
probability, detectable within the first session. **Connection to SNT:** the same
preferential-attachment power-law distribution as in the historical cases, on a
weeks-scale instead of centuries. In the historical cases the dominant node
accumulates advantage via capital, infrastructure and political decision; in
HackerEarth the Elite node accumulates via iteration depth, tool adoption and
AI-agent use — same mechanism. The CSI V3 is functionally equivalent to the
Sentinel Omega pipeline (Appendix A): both normalize heterogeneous input signals to
a comparable space, compute a composite index, and produce a risk classification.
The 5-Event Wall parallels the 10–15% activation threshold of the historical cases:
a critical point before which the system can recover and after which the trajectory
becomes statistically irreversible.

**Implications.** Three for the general framework: (1) pattern invariance does not
require a long timescale — the same algorithm operates over centuries (historical
cases) and weeks (digital behavior), so the dynamic is timescale-independent; (2)
the pattern is detectable in high-frequency, high-resolution data, opening
real-time prospective verification; (3) the CSI V3 classification architecture is
exportable to other domains, including Sentinel Omega for geomagnetic risk.

**Pipeline visualizations (seven plots).** *Top-20 Event-Type Predictors
(SHAP-proxy):* the two dominant retention predictors are agent_accept_suggestion
(~0.5) and agent_worker_created_ratio (~0.4) — both AI-agent adoption signals. The
satellization threshold in the digital domain is not the *amount* of use but the
*quality of delegation*: the user who lets the agent decide has crossed a cognitive
threshold, freeing capacity to operate in more complex dimensions — exactly the
cognitive-leapfrog mechanism the theory predicts for nodes that escape
satellization. *Beeswarm (churn impact direction):* green points cluster near −0.8
churn probability for agent_accept_suggestion — accepting agent suggestions drives
churn toward zero; a qualitative jump, another Fractal-Gap manifestation. *Feature
Importance:* Tool Diversity dominates (0.430), CSI V3 second (0.334), VDR third
(0.150), Credits Used negligible (0.001) — counterintuitively, the user who stays
is the one who *explores* more tools, not the one who *spends* more; breadth
predicts retention better than intensity. *Survival-style chart:* the churn peak is
at ~5 total events and drops abruptly after — an inverted-J with a minimum near
2,500 events confirms the 5-Event Wall (the first 5 events of a session determine
whether the user crosses into deep-use mode; detectable in the first session). *2×2
Action Matrix:* 2,108 "Intervene Now" + 2,329 "Re-engage" = 92.5% in high-risk
zone; only 337 outside critical risk — bimodal, not Gaussian; the mathematical
signature of the Fractal Gap. *Risk Heatmap:* retained nodes have more active,
diversified connections; at-risk nodes have few connections concentrated in one
resource type — the same topology as the historical cases. *Credit Usage by
Lifetime Cohort:* the 8–30-active-day cohort has the highest credit variance;
long-life cohorts are compact near zero — the critical decision period is the first
30 active days, after which the pattern stabilizes into one of two attractors (deep
use or abandonment), with no stable long-term intermediate state. **Emergent
finding — delegation as escape mechanism:** the strongest retention predictor is
neither usage frequency nor credit volume nor tool diversity, but *willingness to
delegate processing to the AI agent*. In the digital domain the leapfrog occurs
when the user stops operating as a task executor and starts operating as an
orchestrator of agents — the digital equivalent of the cognitive leapfrog. The
digital Fractal Gap is not a metaphor for the historical cases; it is the same
algorithm running on a different substrate.

## Module XI: Analysis of the 57-Case Corpus — Results and Findings

The extension of the empirical corpus from 9 to 57 cases across four domains —
historical cities, countries, intra-national regions and digital ecosystems —
allows statistical verification of the model's central postulates. **XI.1 Corpus
description:** 57 cases — Domain A (historical cities, n=16; Bairoch et al. 1988,
Maddison 2023), Domain B (country pairs, n=17; Maddison Project 2023), Domain C
(intra-national regions, n=15; OECD Regional Database, INEGI, Eurostat, US BEA),
Domain D (digital ecosystems, n=9; StatCounter, Statista, IDC, SEC EDGAR).
Inclusion criterion: two nodes in critical proximity within the same system, an
identifiable trigger, and production data at ≥4 time points. Period: 7th century
(Alexandria-Cairo) to 2026 (HackerEarth).

### XI.2 Empirical corpus — FIGURES SUPERSEDED (see Part II/III, corpus v30)

**v30 notice:** the "final 502-case corpus" statistics that occupied this section
(31.1% significance, per-domain mean b, b range [−2.852, +7.086], etc.) are
OBSOLETE. The June 2026 audit found that corpus contained ~188 synthetic b values
(np.random.normal()) and an r² column with impossible values (down to −7.332).
They were never published as final. The current figures are those of the v30
corpus reconstructed from real primary data (721 cases, 89% significant, R² ∈ [0,1]
in all cases, reproducible from reconstruction_real/): friction → satellization
Spearman ρ=−0.68 (p=2.5e-97, n=714); regime separation friction-free-bio (b~+0.95)
vs friction-laden-economic (b~+0.09) Mann-Whitney p=2.4e-74; abrupt > gradual
triggers (ratio 5.9×, U=24,802, p=1.91e-5, n=486). Full detail in PART II and PART
III above. Module XI's qualitative finding — institutional friction orders the
domains by b, and political sovereignty brakes satellization — STANDS and is
strengthened by the real data; only the specific figures change.

## Module XII: Operationalizing the Atomic Sovereignty Index (ASI)

The ASI was previously a working hypothesis without empirical operationalization.
**XII.1 Operational definition:** the ASI measures the Atomic Node's capacity to
resolve its environment's entropy through observable behavior, not self-report.
ASI = (δH · α) / F, with three independent components: applied-knowledge breadth
(δH), expansion initiative (α), and performance consistency under variability (F).
**XII.2 The three components:** *δH — uncertainty reduction:* Shannon entropy of
the user's event-type distribution, H = −Σ p_i·log2(p_i), normalized to [0,1];
empirical (N=4,774): Elite 0.808, Intermediate 0.498, Basic 0.199 (a 4× Elite/Basic
gap — tool breadth is the strongest discriminator). *α — decision autonomy:* share
of autonomous events (run_block, block_create, agent_open, agent_message,
api_deploy, source_control_commit, 30+ types requiring active decision) over total
classified events vs reactive ones (onboarding, sign_up, banners, emails); Elite
0.666, Intermediate 0.397, Basic 0.199 (a sovereign node generates >65% of its
actions itself). *F — internal free energy:* F = tanh(std(events_per_day) /
mean(events_per_day) / 2); high F = inconsistent performance = high internal chaos;
Elite 0.206, Intermediate 0.434, Basic 0.711. **XII.3 Threshold calibration:**
compute ASI_raw for all users, take the Elite cohort median, scale so that median =
1.0 (pre-scaling Elite median 2.64; post-scaling Elite median 1.0, mean 1.59) — so
ASI>1 means operating above the typical Elite level. **XII.4 Validation:** ASI>1
identifies 13 users (0.3%); precision 1.0000 (no false positives — every ASI>1 user
is Elite or Intermediate); recall 0.039; F1 0.076. The low recall is a finding, not
a defect: most Elite/Intermediate users have ASI 0.5–1.0 (partial sovereignty,
latent-leapfrog candidates). Spearman ASI–CSI_V3 = 0.178 (p<0.001) — positive but
low, confirming complementarity: CSI_V3 measures accumulated production; ASI
measures the *way* of operating. High CSI_V3 with low ASI = reactive, variable
production; high ASI with low CSI_V3 = sovereign operation without yet-visible
accumulation (the latent leapfrog). **XII.5 Distribution:** severe satellization
(ASI<0.1) 4,460 users (93.4%); moderate (0.1–0.5) 281 (5.9%); pre-sovereignty
transition (0.5–1.0) 20 (0.4%); active cognitive sovereignty (1.0–2.0) 6 (0.1%);
advanced/Elite (>2.0) 7 (0.1%) — a power law, the Fractal Gap from the ASI
perspective. **XII.6 Implications:** ASI is empirically calibrable from observable
behavior (no self-report or neuroimaging needed); cognitive sovereignty is rare
even within the Elite (the leapfrog is gradual, with measurable intermediate
states); high-ASI/low-CSI_V3 users are the most valuable to intervene with — they
have the internal structure to jump but have not yet executed it. The ASI does not
measure what the node knows — it measures how it operates with what it knows.

## Module XIII: Biological Extension — Satellization in Ecological Systems

Does the central mechanism — satellization as a scale-invariant power law — operate
in biological systems where no human decision intervenes? If yes, the model is no
longer a theory of human behavior but a general complex-systems organizing
principle. Ten cases across three biological domains (E1, E2, E3), from mammals to
viruses, weeks to tens of thousands of years.

**XIII.1 Domain E1 — Interspecies competition.** Brown rat (Rattus norvegicus) over
black rat (R. rattus) in Europe: the black rat was dominant from Roman expansion to
the 18th century; the brown rat's arrival from Asia (genetically documented in He
Yu et al., Nature Communications 2022; Science 2024) produced the corpus's fastest
displacement, b=+1.401 (p=0.006) — an abrupt SNT trigger. African bee (Apis
mellifera scutellata) over European bee in Brazil: the highest biological exponent,
b=+2.437 (p=0.001) — the accidental 1957 introduction of 26 African queens (Warwick
Kerr) drove a 300–500 km/year expansion, comparable in speed to the digital domain;
a hybrid trigger (punctual event consolidated via genetic diffusion over decades).
Homo sapiens vs Neanderthal (45,000–30,000 BP): b=+0.454 (p=0.062, marginal) — the
only millennia-scale case; gradual substitution over 15,000 years via accumulated
advantages in social networks, symbolic technology and possibly disease; the lowest
E1 speed, consistent with the Scalar Velocity Principle.

**XIII.2 Domain E2 — Predator-prey.** The most counterintuitive finding. The
Canadian lynx-hare system (Hudson's Bay Company fur records 1845-1935 — the most
cited case in population ecology and the empirical source of Lotka-Volterra):
b=−0.201 (n.s.). Sharks over prey fish in the Adriatic (D'Ancona 1924; Volterra
1926): b=+0.198 (n.s.). Both non-significant. The reason is structural and reveals
a model limit: predator-prey relations are governed by oscillatory cycles, not
monotonic trajectories. The power-law model captures unidirectional divergence
(sustained b>0) well but not systems alternating between satellization and recovery
in ~10-year cycles — neither node can definitively satellize the other because one's
extinction would destroy the other. This opens refutation criterion RC8: the SNT
monotonic-satellization model does not apply where mutual interdependence between
hub and node creates stable oscillatory cycles.

**XIII.3 Domain E3 — Parasite-host.** The strongest biological case: antibiotic-
resistant bacteria (b=+1.401, R²=0.935, p<0.001). The clearest biological leapfrog:
the antibiotic is the exogenous trigger that inverts the dominance ratio between
sensitive bacteria (prior hub) and resistant ones (prior shadow node). In SNT terms
the antibiotic is the orthogonal dimension — the resistant strain exploits a
dimension where the sensitive strain has no accumulated advantage. Total hierarchy
inversion in 60 months — the microbiological equivalent of the Querétaro or Estonia
leapfrog.

HIV over CD4 cells (b=+1.113, R²=0.622, p=0.011) documents accelerated
satellization on a months scale — the purest direct extraction in the corpus: the
virus uses the host cell's replicative machinery to multiply while degrading the
immune response. Untreated, the HIV/CD4 ratio follows a power law with b near +1.0
(notable, as the model was not designed for viral dynamics). Antiretrovirals (HAART
from 1996) are the exogenous trigger that inverts the ratio: the node (immune
system) leapfrogs the hub (virus) via an orthogonal dimension — pharmacodynamics —
where the virus cannot compete. Phytophthora infestans over potato in Ireland
(1845-1852, the Great Famine): b=+1.096 but negative R² (high interannual
variability — the disease dynamics were strongly perturbed by climate, colonial
policy and potato variety); still, the positive b>1 confirms the satellization
direction over the documented 7-year horizon.

**XIII.4 Comparison with human domains.** E1 (Competition) mean b=+1.266; E2
(Predator-Prey) mean b=−0.002; E3 (Parasite-Host) mean b=+1.203. For reference,
human domains: historical cities +0.356, countries −0.037, regions +0.098, digital
+1.925. The pattern is systematic: interspecies competition and parasite-host
produce exponents equivalent to digital ecosystems (b>1), while predator-prey
produces near-zero exponents — like sovereign countries. The interpretation is
mechanically coherent: competition and parasite-host have a structurally determined
definitive winner (winner-take-all), while predator-prey, like sovereign-country
relations, is mutual interdependence that prevents definitive satellization (if the
predator saturates the prey-node, it self-destructs).

**XIII.5 Implications.** Four: (1) power-law satellization is universal — it
operates in biological systems without human intervention, confirming it is a
complex-systems organizing principle, not just social; (2) speed is specific to the
relation type, not the domain (direct competition b>1 is faster than mutual
interdependence b~0 in both biology and economics); (3) the biological leapfrog
exists with the same structure as the human one (antibiotics and antiretrovirals
are orthogonal dimensions inverting the dominance ratio, as aerospace manufacturing
inverted Querétaro's); (4) refutation criterion RC8 is established — the model does
not apply to cyclic mutual-interdependence systems where one node's extinction
destroys the hub. The deepest finding is theoretical: SNT converges with the
Principle of Least Action in physics and Friston's Free Energy Principle — the
satellization algorithm requires neither intention nor consciousness. It occurs in
bacteria, rats, viruses, medieval cities and digital platforms. The mechanism is
the same; the scale and speed change; the result does not.

## Module XIV: Astronomical Extension — Satellization in Cosmic Systems

Does the mechanism operate where no life is involved — planets, stars, black holes,
galaxies? Yes — and the most striking result is not that it works but that the b
exponents are quantitatively comparable to the human and biological domains. The
universe seems to operate under the same algorithm at all scales.

**XIV.1 Domain F1 — Planetary systems.** Jupiter vs the combined mass of the rest
of the Solar System: Jupiter has 318 Earth masses (2.5× all other planets
combined). This ratio did not exist at formation; accretion models (Pollack et al.
1996; D'Angelo et al. 2014; Helled et al. 2023) show Jupiter started as a ~0.01
Earth-mass core and reached its current mass in ~3 Myr via runaway accretion (past
~10 Earth masses its gravity captures nebular H/He at an exponential rate, opening
a gap smaller planets cannot close). b=+0.819 (p=0.053, marginal) documents this
acceleration. Jupiter vs Mars gives the most extreme astronomical ratio (2,972×):
Jupiter's resonances emptied the asteroid belt of solid material before Mars could
accrete it; Mars was "locked" at 0.107 Earth masses (Grand Tack models, Walsh et
al. 2011, suggest 1–2 Earth masses without Jupiter). In SNT terms Jupiter does not
merely grow — it extracts the resources that would have let Mars grow; the
planetary immune response is orbital resonance.

**XIV.2 Domain F2 — Binary systems.** Sirius A and B: Sirius B was originally the
more massive (the primary), evolved first, shed its envelope as a planetary nebula,
and is now a ~1.018 solar-mass white dwarf; Sirius A (originally the secondary,
~1.8 M☉) absorbed part of that mass and now dominates at 2.063 M☉ — the closest
astronomical leapfrog to Earth (the system inverted its dominance hierarchy).
b=+0.159 (n.s., 250 Myr scale, few points). Cataclysmic Variables are the cleanest
observable satellization: a white dwarf extracts mass from a low-mass companion via
Roche-lobe overflow at 10⁻¹¹–10⁻⁷ M☉/yr, sustained for Myr; the companion becomes a
satellized node transferring its residual energy (stellar mass) to the hub until an
unstable equilibrium ending in nova or Type Ia supernova. A white dwarf accreting
past the Chandrasekhar limit (1.4 M☉) does not collapse — it explodes: the system's
immune response when the hub accumulates too much (mutual destruction).

**XIV.3 Domain F3 — Black holes.** Sagittarius A* accreting the gas cloud G2
(observed in real time 2011-2014, Gillessen et al. 2012, Nature) gives the highest
astronomical exponent: b=+2.838 (p=0.045), final ratio 415 billion to 1 — the most
extreme dispersion in the whole SNT corpus, exceeding the digital Fractal Gap by
orders of magnitude, and observed in real time (a supermassive black hole actively
dismantling an orbiting object). Cygnus X-1, the first identified stellar-mass black
hole (Orosz et al. 2011), accretes from its supergiant companion's wind at ~2.5×10⁻⁶
M☉/yr; b=+0.031 (n.s.) — a near-stationary process; the companion is massive enough
to resist extraction without immediate collapse (the astronomical equivalent of a
region with high resource-regeneration capacity, high RL).

**XIV.4 Domain F4 — Galactic systems.** The Sagittarius dwarf (Sgr dSph) has lost
~97% of its original stellar mass in 4–5 orbits around the Milky Way: b=+1.989
(R²=0.716, p=0.0035) — pure tidal disruption; at each pericenter the Milky Way
strips outer layers and deposits them in its halo as stellar streams (the
Sagittarius Stream now wraps the entire Milky Way). M32, Andromeda's compact
satellite: b=−2.336 (R²=0.818, p=0.0003) — the negative sign reflects using M31 as
hub and M32 as shadow (the M31/M32 ratio grows because M32 is losing mass; evidence
in Dierickx et al. 2014, Graham 2002, suggests M32 was originally a spiral 5–8× its
current mass before M31's tides stripped its arms, leaving the dense bulge we see —
the inverted cosmic leapfrog: the node does not escape, it is reduced to its core).
The Large Magellanic Cloud: b=−0.415 (R²=0.861, p=0.0051) — the Milky Way/LMC ratio
is decreasing (the LMC, 1.38×10¹¹ M☉, Erkal et al. 2019, is the most massive and
resistant galactic node, like a region with high dimensional independence; per HST
2006 it may be on its first close encounter — an abrupt galactic trigger, as the
first orbit is the most destructive).

**XIV.5 The universal pattern.** Across all 14 SNT domains — from bacteria to
galaxies — power-law satellization operates everywhere, and speed (b) varies
systematically by relation type, not substrate. Relations with a structurally
determined winner (biological competition, parasite-host, digital ecosystems,
planetary formation, galactic disruption) give b>1. Mutual-interdependence
relations where complete satellization would destroy the hub (predator-prey,
sovereign countries, equilibrium binaries) give b~0. The same principle that stops
the lynx from exterminating the hare stops a white dwarf from fully consuming its
companion: co-dependence is the real brake in both. The most extreme case
(Sagittarius A* over G2, ratio 4.15×10¹¹ to 1) is the cosmic limit of the
mechanism. The scale changes by 30 orders of magnitude, time from decades to
billions of years, substrate from mammal populations to gravitational fields, b
between −2.3 and +2.8 — but the underlying power law is the same.

**XIV.6 Final theoretical implication.** The full SNT v2.2 corpus spans 77 cases
across 14 domains and 14 timescales — from hours (HackerEarth, 13.5-hour cycle) to
billions of years (Solar System formation, galactic disruption). In all of them,
dominance dynamics between proximate nodes follow a power law. Satellization is not
a social, biological or astronomical phenomenon — it is a complex-systems
organizing principle that emerges inevitably when two nodes of differing
accumulated mass orbit in critical proximity under a resource-transfer mechanism.
The satellization algorithm is a law of nature, not a metaphor. From the black hole
consuming a gas cloud in real time to the Roman Empire satellizing Hispania over
three centuries: the same algorithm. Humanity did not invent satellization — it
inherited it. And what is inherited can be studied, measured, predicted and
intervened upon. *"If you stay still long enough, you can see the algorithm that
moves the universe."* — Adapted from Alan Moore, Watchmen (1986).

## Module XV: The Satellization Cycle — From Child Node to Hub

Previous modules treated satellization as a structural condition. The observation
motivating Module XV is that across all corpus domains a cyclic pattern exists that
the static model did not capture: the child node is born satellized, accumulates
its own mass, reaches parity with the mother-hub, and eventually becomes the hub of
its own child nodes. The cycle restarts. (Biology: a daughter bacterium competes
with the mother from division — peer competition from the first instant. Astronomy:
two stars from the same nebula orbit as a peer binary if of similar mass; if one
accumulates faster it satellizes the other — the Solar System has planets rather
than a stellar binary precisely because Jupiter gained critical advantage before
Saturn could match it. Economics: Spanish colonies in America began as child nodes
satellized by Madrid, accumulated mass, became independent via an exogenous
trigger, and today Mexico and Argentina are hubs of their own regional systems.
Digital: Facebook created Instagram internally; it grew into a potential competitor;
Meta had to acquire it before it crossed the parity threshold.)

**XV.1 The four phases.** *Phase 1 — Total dependence (b>0.5):* the child node is
born fully structurally dependent; R(t) grows fast; the hub controls its
subsistence resources. *Phase 2 — Accumulation (0.1<b<0.5):* the child accumulates
its own mass without leaving the hub's network; the ratio grows more slowly; it has
own resources but depends on the hub for market access, legal protection or shared
infrastructure. *Phase 3 — Convergence/parity (b≈0):* the child has enough mass to
operate as a peer; hub extraction balances the node's own production; in some
systems this phase is stable and lasting, in others transitory (the system cannot
sustain two comparable-mass nodes in the same orbit). *Phase 4 — Inversion or own
hub (b<0):* the child surpasses the parent in a critical dimension, inverts the
hierarchy, or becomes the hub of its own child nodes — the complete leapfrog.

**XV.2 Model limit — non-rival resources.** SNT does not apply directly where the
transferred resource is non-rival. A rival resource is one whose use by the hub
prevents the node's use (labor, capital, territory, gravitational mass, food); a
non-rival resource can be used by both simultaneously without either losing it
(knowledge, information, culture, language, open science). When Tlaxcala loses a
worker to CDMX, Tlaxcala has less; when a bacterium transfers a resistance plasmid,
the first does not lose it — both have it. With non-rival resources b cannot grow
indefinitely. Yet the Child-Node cycle captures this: knowledge transmits from
mother-hub to child in Phase 1; the child applies it to generate its own resources
in Phase 2; both share it and compete as peers in Phase 3; the child can innovate
upon and surpass it in Phase 4. The b curve starts at 0 by definition (equal mass
in the knowledge resource) — satellization in the knowledge dimension is gradual
and reversible, while in rival resources it is cumulative and irreversible without
an exogenous trigger.

**XV.3 The cycle per domain.** *Biological* (fastest — bacteria divide in minutes;
the daughter inherits the full genome, a non-rival resource, but competes for
nutrients; antibiotic-resistant bacteria show the full cycle — sensitive strain =
historical hub, resistant = satellized child, antibiotic = inverting trigger,
resistant strain = new hub). *Astronomical* (slowest — Myr to Gyr; planets are
permanently satellized child nodes; comparable-mass binaries reach stable Phase 3;
the M31–Milky Way collision in 4 Gyr will be Phase 4). *Economic* (most variable —
decades to centuries; Phase 1: Chiapas, Oaxaca, Guerrero; Phase 2: Tlaxcala,
Veracruz, Puebla; Phase 3: Nuevo León, Querétaro; Phase 4: none yet in Mexico, but
South Korea vs Japan b=−0.456 and Ireland vs UK b=−0.222 document the full cycle).
*Digital* (fastest with institutional friction — months to years; Instagram,
YouTube, Android began as satellized children that the hub acquired before Phase 4 —
Module II's immune response; rare Phase-4 successes — Google over Yahoo, Chrome over
Internet Explorer, TikTok over Vine — all required an orthogonal dimension the hub
could not replicate or acquire in time).

**XV.4 The cycle and the Atomic Node.** The Atomic Node is not a state but a phase.
Every individual begins as a satellized child node (dependent on parents, community,
education, first employer); the goal of cognitive development is to transit the four
phases. The cognitive leapfrog HackerEarth documents — orchestrating AI agents
instead of executing linear tasks — is exactly the Phase 2 → Phase 3 transition in
the digital dimension. The ASI measures which phase the node is in: Phase 1 ASI<0.016
(below Basic median 0.0157); Phase 2 ASI 0.016–0.167 (between Basic and Intermediate
medians); Phase 3 ASI 0.167–1.0 (95.8% of Elite users exceed 0.5; minimum Elite
0.2449; the prior 0.5 threshold was arbitrary and is replaced by the empirically
calibrated Intermediate median); Phase 4 ASI≥1.0 (full sovereignty, precision 1.0,
only 0.27% of users). The ASI distribution follows the same skewed power law as
economic satellization: 93.4% in Phase 1, 0.27% in Phase 4.

**XV.5 The Universal Cycle Principle.** Every complex system with asymmetric-mass
nodes produces satellization cycles where child nodes transit from dependence to
parity and potentially to hierarchy inversion. Cycle speed is proportional to the
child node's resource-accumulation speed, which depends on the system's
institutional friction — frictionless systems (biological, unregulated digital) can
complete the full cycle in hours or days; high-friction systems (sovereign
countries, institutionally dependent regions) take decades or centuries. The
insurmountable limit is permanent Phase 3 — parity without possible Phase 4 — when
hub and node have mutual dependence preventing definitive satellization (sovereign
country pairs are the statistical example: political sovereignty creates a
structural Phase 3 where the cycle halts before inversion). Surpassing it requires
an exogenous trigger (war, political union, technological revolution) that breaks
the mutual-dependence symmetry. The node is not a state — it is a phase.
Satellization is not a destiny — it is a cycle. The leapfrog is simply the node
transiting to the next phase before the hub can stop it; the immune response is
simply the hub's attempt to keep the node in the phase where it is useful. The
algorithm has no morality. Only phases.

## Level 3: Active Hypotheses — Synchronization and Consciousness

Hypotheses with partial empirical support that require further research to confirm
or refute.

**3.1 Inter-brain synchronization.** Recent neuroscience confirms brains
synchronize during social interaction — not metaphorically, but electrically,
measurably and reproducibly. BrainNet (U. Washington + Carnegie Mellon): three
people communicate using only brain waves to solve cooperative tasks. Waseda
University (2024): pairs of strangers show more synchronized brain networks than
pairs of acquaintances during cooperative tasks. Dartmouth (2024, Nature
Communications): after consensus-reaching conversations, participants' brain-
processing patterns align. These connect with Grinberg-Zylberbaum (1994), who
reported "transferred potential" between brains in separate Faraday cages (Physics
Essays 7(4), 422-428). The difference is the proposed mechanism: Grinberg posited
an external field (the Lattice); current studies show synchronization via direct
electromagnetic signals. Both may be complementary.

**3.2 Microtubules and Orch-OR (Penrose-Hameroff).** Penrose and Hameroff (1994)
proposed Orch-OR: microtubules inside neurons might act as quantum processors. If
correct, the brain not only generates electrical signals but decodes information at
the quantum level. The hypothesis remains controversial — neither refuted nor
definitively confirmed; what is confirmed is that microtubules have structural
properties making them theoretically plausible candidates. The connection: if
microtubules are quantum-information decoders, the brain does not generate
consciousness but tunes it from an external field — coherent with inter-brain
synchronization and Grinberg's Lattice.

**3.3 Oceanic polymetallic nodules as natural capacitors.** In 2024 GEOMAR
researchers published evidence that polymetallic nodules on the Pacific floor
generate oxygen via electrochemical electrolysis without sunlight ("dark oxygen") —
implying they accumulate enough electrical charge to split water into hydrogen and
oxygen. They are, functionally, natural capacitors integrated into the planet's
electrical circuit; their distribution follows specific geological patterns (ocean
ridges, subduction zones). Derived hypothesis: these capacitors are active nodes in
Earth's energy-distribution network, and their charge/discharge cycle may correlate
with tectonic events. Proposed causal chain: solar activity → geomagnetic
perturbation → telluric-flux alteration → variation in nodule charge → pressure on
adjacent fault zones. Investigable with public data (NOAA, ISA; USGS seismic).
Status: active hypothesis with a proposed physical mechanism; the dark-oxygen
evidence confirms the nodules are electrochemically active; the seismic correlation
requires quantitative verification.

**3.4 Bitcoin as an index of global collective emotional state.** Traditional
financial markets have institutional buffers filtering short-term emotional
fluctuations (trading hours, circuit breakers, regulation, market makers). Bitcoin
has none: 24/7, decentralized global participation, no effective regulatory
intervention. This makes Bitcoin volatility a real-time proxy for the collective
human emotional state — a sensor of the aggregate emotional variance of millions of
simultaneous actors without an institutional filter; in the framework's language,
Bitcoin is the species' electroencephalogram. Published research correlates Kp-
index variations with financial-market behavior; the proposed biological mechanism
is that geomagnetic fields affect melatonin and cortisol, altering population-scale
decision-making. Proposed full chain: solar activity → geomagnetic perturbation →
biochemical alteration in humans → collective-behavior change → detectable Bitcoin
volatility. Each step has independent partial support; the full chain is an original
hypothesis. Status: requires systematic backtesting of historical Kp vs Bitcoin
volatility.

## Level 4: Open Frontier — Dark Matter as Substrate

The most speculative and original hypothesis, with no direct empirical confirmation,
presented as an open research question. **4.1 The hypothesis:** dark matter is 27%
of the universe, dark energy 68%, visible matter only 5%; dark matter does not
interact electromagnetically (hence invisible). The hypothesis: dark matter acts as
the connective substrate of the network of networks; the dark-matter filaments
mapped by the Sloan Digital Sky Survey have exactly the same topology as neural,
mycelial and urban networks — that scale invariance may not be geometric
coincidence. **4.2 The mechanism problem:** how would dark matter interact with
biological and social systems if not electromagnetically? Speculative options:
small-scale gravitational interaction not yet detected; an uncatalogued weak
interaction; or — most parsimonious — scale invariance requires no direct
interaction, merely reflecting that the same optimization algorithm operates at all
levels independent of substrate. The last best aligns with current evidence: the
pattern repeats not because dark matter causes it in biological systems, but because
the same distributed-optimization algorithm converges to the same topology on any
substrate. **4.3 GRB 250702B and the frontier:** GRB 250702B provides relevant
indirect evidence — a cosmic mechanism generating extreme phase transitions not
predicted by current models, consistent with the existence of cosmological dynamics
we do not yet fully understand, potentially including dark matter's role in
organizing complex systems.

## Conclusion: The Universal Algorithm

This framework proposes a common organizing algorithm operating at all scales of
the universe. The strongest evidence comes from three independent sources: *pure
mathematics* (scale-free networks emerge inevitably from two simple local rules,
independent of substrate); *experimental biology* (Physarum polycephalum builds the
same optimal network as human engineers with no centralized system); *socioeconomic
data* (Shadow Node Theory shows the same suppression-and-emergence algorithm
operating across historically distinct urban systems). What ancient civilizations
called "as within, so without" is an intuitive description of scale invariance;
sacred geometry is the symbolic language of patterns modern mathematics is
formalizing. The researcher's task is to complete that translation. Chaos is not the
absence of order — it is order at a scale we do not yet have the mathematical
resolution to see fully. Raising that resolution is the goal of this research.

## Principal References

Barabási, A.L. & Albert, R. (1999), Science 286(5439), 509-512. Tero, A. et al.
(2010), Science 327(5964), 439-442. Maldacena, J. & Susskind, L. (2013),
Fortschritte der Physik 61(9), 781-811. Grinberg-Zylberbaum, J. et al. (1994),
Physics Essays 7(4), 422-428. Penrose, R. & Hameroff, S. (1994), Mathematics and
Computers in Simulation 40(3-4), 453-480. INEGI (2022), Well-being indicators by
federal entity. GRB 250702B / AT2025ulz: ZTF, Einstein Probe, LIGO-Virgo-KAGRA
reports (August 2025). Gooday, A.J. et al. (2024), Nature Geoscience / GEOMAR.
Babayev, G.S. & Allahverdiyeva, A.A. (2007), Advances in Space Research 40(12),
1941-1951.

## Appendix A: Sentinel Omega System

Sentinel Omega is the framework's practical application at geophysical scale. If
SNT describes how social systems accumulate tension to a predictable collapse
point, Sentinel Omega instruments that prediction with real geophysical data.
**A.1 Multivariate precursor architecture** — five independent input layers: (1)
*Seismic* (USGS, 30-year history, global M4.5+ — the system's ground truth); (2)
*Space weather* (NOAA SWPC: Kp index, Bz vector, solar-wind speed and density); (3)
*Schumann resonance* (U. Tomsk: base 7.83 Hz and harmonics); (4) *Planetary
dynamics* (IERS: length of day — rotation changes correlate with crustal mass
redistribution); (5) *Geochemistry* (subsurface radon, SO2, CO2 — gases escaping
through micro-fractures before tectonic events). **A.2 Geophysical node-network
model:** Earth as a graph where nodes are tectonic-electromagnetic intersection
points and edges are weighted by telluric conductivity, geodesic distance and
acoustic attenuation; oceanic nodes in high polymetallic-nodule-density zones carry
special weight (the natural capacitors of §3.3; their charge state is a system
input). **A.3 Validation pipeline:** Prediction (per-zone risk estimate, 24–72 h
window) → Observation (USGS confirms or refutes) → Error (asymmetric loss; false
negatives penalized more than false positives) → Recalibration (weights auto-adjust
on error). **A.4 Unconfirmed hypotheses:** Kp–earthquake correlation (existing
research inconsistent; needs time-series analysis); Bitcoin as collective mood
(§3.4); LOD and tension release (rotation-speed variations imply mass redistribution;
correlation with later seismic increase plausible but unconfirmed). Sentinel Omega
does not predict the future — it measures the planetary system's tension state and
estimates the probability that tension releases in a specific zone within a defined
window. Probability, not certainty.

## Appendix B: Mathematical Tools of the System

The real mathematical tools integrated into Sentinel Omega; legitimate and
independent of any metaphorical interpretation. **B.1 Gaussian distribution —
initializing the probability space:** P(n) = (1/(σ√(2π)))·exp(−0.5·((n−μ)/σ)²);
normalizes each sensor's readings to standard deviations (the comparable unit
across heterogeneous sensors). Limitation: assumes normality; extreme events (X-class
storms, M8+ quakes) lie in the tails and are systematically underestimated without
heavy-tail distributions. **B.2 Gauss-Jordan elimination — cleaning data-matrix
redundancies:** reduces the augmented matrix to identify and remove collinear
predictors (e.g. if Kp and solar-wind speed are correlated r>0.95, including both
inflates confidence). Limitation: operates on linear relations only; non-linear
interactions need rank correlations or tree models. **B.3 Fourier Transform (FFT) —
detecting cycles in time series:** X(k) = Σ x(n)·[cos(2πkn/N) − i·sin(2πkn/N)];
applied to Schumann-resonance history to find recurrent frequencies (e.g. 27-day
solar-rotation cycles, 11-year solar cycle) and to per-zone seismic history for
fault periodicity. Limitation: assumes stationarity; geophysical systems are non-
stationary — for non-stationary signals the Wavelet Transform is recommended. **B.4
Bayesian inference — updating probabilities with new evidence:** P(H|D) =
[P(D|H)·P(H)]/P(D); the system maintains a per-zone seismic-risk distribution and
updates it Bayesianly with each sensor reading (e.g. 15% probability of M5+ in
Guerrero-Oaxaca within 72 h updates upward on sustained negative Bz). Limitation: as
good as its prior; a miscalibrated prior yields mathematically correct but real-
world-wrong updates. **B.5 Shannon entropy — measuring informational disorder:**
H(X) = −Σ P(xi)·log2(P(xi)); the system computes its per-zone risk-distribution
entropy each cycle — high entropy (flat distribution) inhibits the alert ("insufficient
data"); low entropy (clear peak) emits an alert with coordinates; also monitors data
quality (rising sensor entropy may indicate a failing sensor). Limitation: does not
distinguish uncertainty from missing data vs intrinsic unpredictability — high
entropy is a caution signal, not a failure signal. **B.6 Pipeline integration:** the
five tools operate iteratively — Gaussian (normalize) → Gauss-Jordan (remove
redundancy) → FFT (identify periodic features) → Bayes (update per-zone risk) →
Shannon (decide whether to emit an alert or block for excessive uncertainty). The
pipeline runs on each new data batch (hourly/6-hourly/daily); each cycle's result
becomes the next cycle's prior, implementing continuous learning without full
retraining. These tools are applied mathematics; their value depends not on the
surrounding framework but on data quality and the honesty with which their
limitations are reported.

---

*Annex A restored from the v27 framework. Conceptual body intact; corpus figures
updated to v30 (721 real cases).*

---

*Fractal Core Research — Tlaxcala, Mexico · Theoretical Framework v30 (English) ·
June 2026 · "Technical truth over numerical impression."*
