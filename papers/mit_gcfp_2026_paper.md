# Orbital Collapse Architecture: Institutional Friction as the Regulator of Systemic Collapse

**Evidence from the 2008 crisis and four further empirical domains**

Elán Zainos Corona — Fractal Core Research, Tlaxcala, Mexico
ORCID 0009-0009-9125-253X · elan.zainos.corona@gmail.com

*Prepared for the MIT Golub Center for Finance and Policy (GCFP) 13th Annual Conference — "Financial Regulation in an Era of Innovation and Disruption," October 29–30, 2026. Working paper — preliminary draft. Data and code: github.com/Inzainos/The-shadow-Node-Theory*

---

## Abstract

When a dominant institution fails, its assets and market position are not destroyed — they are **absorbed** by an identifiable successor, and both the speed *and the shape* of that absorption are empirically regular. We model the post-failure dominance ratio A(τ) = mass_absorber(τ) / mass_collapsed_peak as a power law, A(τ) = c·τ^Delta, on a clock τ that starts at functional extinction, and treat the exponent **Delta** as a collapse coordinate orthogonal to the satellization exponent b.

Applied to the six canonical absorptions of the 2008–2009 crisis (Lehman Brothers, Bear Stearns, Washington Mutual, Wachovia, Merrill Lynch, Chrysler), the framework recovers statistically significant power-law absorption in every case (R² = 0.85–0.99, all p < 0.01), reconstructed entirely from primary sources. The ordering of Delta tracks the **resolution channel**: regulator-brokered failures (WaMu via FDIC, Bear Stearns via the Fed) are absorbed near-instantly, while the single disorderly bankruptcy (Lehman) is the slowest.

Our central claim is sharper than speed: **institutional friction does not merely slow collapse — it *regularizes its shape* into a smooth power law.** We test this against four further domains with real data. The decisive contrast is the **frictionless** domain of crypto-assets: LUNA (May 2022) collapses as a *catastrophic cliff* (super-exponential, 5.6 orders of magnitude in 11 days), FTX/FTT as a *floor-arrested* power law, and EOS as *erratic fragmentation* — none of them the orderly power law that regulated failures exhibit. Astrophysical collapse (a solar flare, R²=0.975; a tidal disruption event, ~t^−5/3) and a biological succession (Delta→Omicron) confirm the generality of the form.

We organize these into a five-mode taxonomy governed by **friction × trigger × (floor/ceiling)**, unified by a **Principle of Least Friction** (collapse follows the minimum-friction path; the friction field's geometry selects the mode). The policy implication is direct: **orderly resolution machinery is what buys a power-law decay instead of a cliff** — and frictionless venues are structurally prone to catastrophic, not graceful, failure.

---

## 1. Introduction

The 2008–2009 crisis was, structurally, an episode of accelerated **concentration**: failing institutions did not vanish, their balance sheets and franchises were captured by identifiable successors. JPMorgan absorbed both Bear Stearns and Washington Mutual; Bank of America absorbed Merrill Lynch. This is precisely the dynamic too-big-to-fail regulation aims to constrain.

We ask two quantitative questions: *how fast* does post-failure absorption happen, and — more importantly — *what governs its shape*? We show that absorption follows a power law whose exponent and **regularity** encode the institutional environment in which the failure was processed. The financial cases are one slice of a broader program (Shadow Node Theory, SNT) that finds the same structure across demography, epidemiology and astrophysics; we use that breadth here only to argue that what we observe in finance is an instance of a general law, and to isolate, by contrast, what regulation specifically contributes.

---

## 2. Model

A system carries two orthogonal coordinates:

- **Satellization b:** R(t) = m_hub(t)/m_node(t) = a·t^b — how dominance evolves while the coupled relationship runs.
- **Collapse Delta:** A(τ) = c·τ^Delta, with A = m_absorber(τ)/m_collapsed_peak and τ = time since **functional extinction**.

Delta is fit by OLS on log–log axes. **b ⊥ Delta** is a falsifiable claim (corr(b, Delta) ≈ 0 across systems with both measured): collapse can strike at any point of a satellization trajectory, so it is an orthogonal axis, not a terminal stage.

**ACO criterion (definitional):** a case qualifies as Orbital Collapse only if (1) the hub undergoes functional extinction and (2) its mass is absorbed by a specific, identifiable successor. Failures that dissolve without capture are excluded.

---

## 3. Data

The six 2008–2009 cases are reconstructed from primary records: SEC EDGAR (8-K, S-4, 10-K), Federal Reserve Flow of Funds, FDIC failure/acquisition records, SIGTARP, the U.S. Treasury TARP tracker, and the Valukas Lehman Examiner Report. Monthly resolution from the trigger date forward. No synthetic values. Cross-domain data: Yahoo Finance (crypto), CoV-Spectrum/LAPIS (variant genomics), NOAA SWPC GOES (solar X-ray), NASA IRSA/ZTF (tidal disruption photometry), Maddison 2023 (historical).

---

## 4. Results

### 4.1 The 2008 cohort: the resolution channel is legible in Delta

Every case yields a significant power-law absorption. Ranked by absorption speed (time to 90% absorption, in hours):

| Hub → Absorber | Resolution channel | Delta | R² | time→90% |
|----------------|--------------------|------|------|----------|
| Washington Mutual → JPMorgan | FDIC receivership (P&A) | +0.009 | 0.946 | 21 h |
| Bear Stearns → JPMorgan | Fed-brokered (Maiden Lane) | +0.043 | 0.926 | 626 h |
| Wachovia → Wells Fargo | open-bank, FDIC-adjacent | +0.153 | 0.892 | 4,140 h |
| Merrill Lynch → Bank of America | negotiated merger | +0.217 | 0.846 | 7,122 h |
| Chrysler → Fiat + US Treasury | government-managed (TARP) | +0.138 | 0.990 | 16,071 h |
| Lehman Brothers → Barclays + JPMorgan | disorderly bankruptcy | +0.246 | 0.892 | 30,681 h |

The two fastest absorptions are the two most actively brokered failures; the slowest is the one allowed to proceed as a disorderly bankruptcy. The span is ~1,460×. WaMu's 21 h matches the real FDIC weekend seizure (~48 h) in order of magnitude — a sanity check that the method tracks reality.

### 4.2 Friction regularizes the *shape* (not just the speed)

In all six cases — and across the high-friction historical cases (Rome, USSR; R²=0.77–0.99) — absorption is a **smooth power law** (R²=0.85–0.99). This is the regulated regime: institutional scaffolding channels the failure into an orderly, scale-free decay.

### 4.3 The frictionless counterexamples (the regulatory payoff)

What does collapse look like with **no** institutional friction? Crypto-assets provide the natural experiment (real data, Yahoo Finance / user corpus):

| Case (friction ≈ 0) | Trigger | Floor? | Mode | Signature |
|---------------------|---------|--------|------|-----------|
| **LUNA / Terra** (May 2022) | abrupt | none | **Catastrophic Cliff** | super-exponential; 5.6 OOM in 11 days; exponential beats power law and still under-fits (returns accelerate) |
| **FTX / FTT** (Nov 2022) | abrupt | floor ~$1 | **Floor-Arrested** | sharp drop to a residual floor; power-law-like (R²=0.875) |
| **EOS** (2018–) | gradual | none | **Cracquelure** | erratic fragmentation; power-law R²=0.10–0.70 |

None of these is the orderly power law of regulated failure. **Without institutional friction, collapse is catastrophic, arrested, or erratic — never graceful.** This is the core regulatory message: regulation is what converts a cliff into a power law.

### 4.4 Cross-domain universality of the form

The smooth-power-law (regulated) mode also appears where the regulating "friction" is *physical*: a GOES M6.9 solar flare decays as a power law (R²=0.975; radiative/conductive cooling); the tidal disruption event AT2019qiz (a star accreted by a black hole — the most literal collapse-with-absorption) decays as ~t^−5/3 (R²=0.84), with disk viscosity as the literal friction. A bounded biological succession (Delta→Omicron, South Africa) is a fast logistic sweep (k=0.218/day). The mechanism is not finance-specific.

---

## 5. Taxonomy and unifying principle

**Five modes, governed by friction × trigger × (floor/ceiling):**

| Mode | Condition | Shape |
|------|-----------|-------|
| Regulated Orbital Decay | high friction (any trigger) | smooth power law |
| Cracquelure Decay | friction≈0 + gradual | erratic fragmentation |
| Floor-Arrested | friction≈0 + abrupt + floor | power law to a residual floor |
| Catastrophic Cliff | friction≈0 + abrupt + no floor | super-exponential |
| Logistic Sweep | bounded magnitude | S-curve |

**Principle of Least Friction.** Collapse follows the trajectory that minimizes integrated friction — gradient flow on a stability landscape. The geometry of the friction field (× trigger × floor) selects which mode emerges. Names have established anchors: the *catastrophic cliff* is a fold catastrophe (Thom); *cracquelure* is desiccation cracking (stress relief along least-resistance paths). The stability-landscape picture connects SNT to catastrophe theory, the Waddington landscape, ecological resilience (Holling) and climate tipping points. See `figures/fig_paisajes_colapso` and `figures/fig_catastrofe_cuspide` (SVG + PNG).

---

## 6. Regulatory implications

1. **Orderly resolution buys power-law decay instead of a cliff.** Delta and the regularity (R²) of absorption are an *ex post* diagnostic of whether resolution machinery (Title II, FDIC single-point-of-entry) delivered the rapid, predictable transfer it promises. Low-Delta, high-R² = the regime worked; cliffs or erratic fragmentation = it did not, or was absent.
2. **Frictionless venues are structurally cliff-prone.** The 2022 crypto collapses are not anomalies — they are what the model predicts for abrupt failure with no institutional friction and no value floor. This is a financial-stability argument for extending resolution-style friction (circuit breakers, disclosure, capital/withdrawal gates) to crypto and shadow-banking venues.
3. **A temporal dimension for too-big-to-fail.** Delta quantifies *how fast* concentration completes after a failure (JPMorgan absorbing Bear + WaMu), complementing static concentration metrics.

---

## 7. Falsifiability

- **RC-Delta1 (orthogonality):** refuted if corr(b, Delta) ≫ 0 across systems with both coordinates.
- **RC-Delta2 (least friction):** refuted if a realized collapse takes a higher-friction path when a lower-friction one was available.
- **RC-Delta3 (absorption):** refuted if the absorber's mass does not grow post-absorption.
- **RC-Delta4 (regularization):** refuted if frictionless collapses fit a power law as well as regulated ones.

---

## 8. Limitations

This is a preliminary draft. Findings are **correlational**: the domains differ in more than friction (timescale, the meaning of "mass", microstructure). The crypto sample is small (n≈3) and LUNA/the solar flare are collapse-*shape* evidence, not ACO absorptions with a single absorber. The TDE exponent (−1.07) is shallower than the canonical −5/3 (g-band, imperfect host subtraction); the point is power-law regularity, not the exact value. "Time to 90%" is threshold-dependent, though the abrupt<gradual ordering is robust to 0.5/0.9/0.95. A full version will operationalize "friction along a path", expand cases per mode, and test orthogonality directly.

---

## 9. Conclusion

Institutional failure is a transfer of dominance to an identifiable successor at an empirically regular rate and shape. That shape — the collapse exponent Delta and its regularity — encodes the resolution regime. The decisive, policy-relevant finding is that **institutional friction is what makes collapse follow an orderly power law; remove it and failure becomes a catastrophic cliff.** For a conference on financial regulation in an era of disruption, this offers a compact, falsifiable instrument for asking whether our resolution machinery delivers orderly transfers — and a structural argument for why frictionless venues fail catastrophically rather than gracefully.

---

## Appendix — data sources by case

- **Lehman Brothers:** Valukas A.R. (2010), Examiner Report, SDNY; Fed Flow of Funds 2008–2013; SEC EDGAR 10-K Barclays & JPMorgan.
- **Bear Stearns:** FRBNY (2008), Maiden Lane; SEC 8-K JPMorgan Mar 2008; Sorkin (2009), *Too Big To Fail*.
- **Washington Mutual:** FDIC (2008), Sep 25 release; JPMorgan 8-K Sep 2008; FDIC Failed Bank List.
- **Wachovia:** SEC 8-K Wells Fargo Oct 2008; FDIC statement Oct 3 2008; Wessel (2009), *In Fed We Trust*.
- **Merrill Lynch:** SEC S-4 BofA Dec 2008; BofA 10-K 2009; Lewis testimony to the FCIC (2010).
- **Chrysler:** SIGTARP (2012); Chrysler Group 10-K 2010; US Treasury TARP tracker; Rattner (2010), *Overhaul*.
- **Crypto:** Yahoo Finance (LUNA1-USD, FTT-USD); user corpus (EOS, ETH).
- **Astro:** NOAA SWPC GOES X-ray; NASA IRSA/ZTF (AT2019qiz).
- **Biology:** CoV-Spectrum/LAPIS open (GenBank), South Africa.

*Full corpus, code and reproduction: github.com/Inzainos/The-shadow-Node-Theory*
