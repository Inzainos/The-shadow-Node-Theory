# Power-Law Dynamics of Biological Satellization: A Unified Model of Competitive Exclusion, Predation, and Parasitism

**Elán Zainos Corona**

Fractal Core Research · Tlaxcala, Mexico

elan.zainos.corona@gmail.com

DOI: https://doi.org/10.5281/zenodo.19446521 · SSRN: https://ssrn.com/abstract=6418778 · GitHub: https://github.com/Inzainos/The-shadow-Node-Theory

---

> **Version note (v30).** This revision supersedes the previously posted version (502-case corpus, v2.2). A June 2026 audit found that the 502-case corpus contained ~188 synthetically generated b values and an R² column with impossible values (down to -7.332); it has been retired. This version uses a **721-case corpus reconstructed entirely from verifiable primary sources** (R² ∈ [0,1] for every case; reproducible from `reconstruction_real/`), and integrates the new Coupled Orbital Collapse layer (ACO-A). The golden-ratio hypothesis (H-φ) was tested and refuted across four rounds (placebo control included) and is excluded from the main claims.

---

## Abstract

We apply a power-law model of node satellization — originally developed in economic history — to 240 biological case pairs across three ecological relationship types: competitive exclusion (E1, n=4), predator-prey (E2, n=2), and parasite-host (E3, n=234). The satellization ratio R(t) = abundance_dominant(t) / abundance_displaced(t) follows a power law R(t) = a·t^b, with friction-free biological domains (E1+E3, b̄ = +0.95) satellizing ~10× faster than friction-laden economic domains (b̄ = +0.09), Mann-Whitney U = 103,538, p = 2.4×10⁻⁷⁴. Three findings emerge: (1) competitive exclusion (E1, b̄ = +2.891) and parasite-host (E3, b̄ = +0.912) produce substantially faster displacement dynamics than predator-prey (E2, b̄ = +0.145); (2) the near-zero b in predator-prey systems reflects the mutual interdependence brake — predator extinction follows prey extinction, creating an ecological analogue of political sovereignty in economic systems (RC8); (3) introduced species with no evolutionary history in the invaded ecosystem produce the highest b values, consistent with the absence of coevolved resistance — an ecological analogue of zero institutional friction. The model provides a unified quantitative framework for comparing displacement rates across ecological relationship types and invasion scenarios. This revision additionally integrates the Coupled Orbital Collapse layer (ACO-A): biological systems exhibit Regulated Orbital Decay (epidemic collapse, Omicron wave: R² = 0.958, exponential, e-fold ~22 d) under intrinsic epidemiological friction, and the golden-ratio hypothesis (H-φ) is confirmed refuted after four independent rounds.

**Keywords:** competitive exclusion, biological invasion, parasite-host dynamics, power law, satellization, Lotka-Volterra, invasive species, ecological satellization, collapse modes, institutional friction

---

## 1. Introduction

Competitive exclusion (Gause 1934), predator-prey dynamics (Lotka 1925; Volterra 1926), and host-parasite coevolution (Hamilton 1980) are among the most studied processes in theoretical ecology. Each has well-developed mathematical frameworks. What is less developed is a unified quantitative framework that can compare displacement rates across these three relationship types and across invasion scenarios involving species with and without prior coevolutionary history.

We propose that the satellization ratio R(t) = abundance_dominant(t) / abundance_displaced(t), when fitted to a power law R(t) = a·t^b, provides such a framework. The exponent b measures the velocity of ecological displacement independently of the relationship type, allowing direct comparison across competitive exclusion, predation, and parasitism. This approach extends the preferential attachment framework (Barabási & Albert 1999) from network topology to ecological resource dynamics, and connects to Shadow Node Theory (SNT, Zainos Corona 2026), a formally verified model of satellization dynamics across 721 real cases in historical, economic, biological, and astronomical domains.

---

## 2. Data and Methods

### 2.1 Case selection

Cases were included if they satisfy: (a) two species in ecological competition, predation, or host-parasite relationship; (b) population or abundance data at minimum four temporal points; (c) the displacement process has either completed or is actively ongoing. No cases were excluded based on outcome direction — both displacement (b > 0) and resistance (b ≈ 0) cases are included to avoid confirmation bias.

### 2.2 Corpus v30 — 240 biological cases, 100% real data

| Domain | Friction | Cases | Sig. | b̄ | R̄² | Source |
|--------|----------|-------|------|-----|-----|--------|
| E1 — Biological invasion (competitive exclusion) | none | 4 | 100% | +2.891 | 0.81 | OWID COVID spatial / Nature Comms / Conservation Biology |
| E2 — Predator-prey | high | 2 | 50% | +0.145 | 0.12 | MacLulich 1937 / Elton & Nicholson 1942 |
| E3 — Parasite-host | none | 234 | 100% | +0.912 | 0.85 | JHU COVID-19 (CSSE) |
| **TOTAL** | | **240** | **99%** | **+0.90** | **0.84** | |

**Integrity verified:** R² ∈ [0,1] for all cases. Zero corrupt values. All reproducible from `reconstruction_real/code/` (public GitHub).

### 2.3 Analysis pipeline

For each case pair, R(t) is computed at each temporal observation point. Time t is measured in years (or days for epidemic cases) elapsed since the trigger event. The log-log transformation log(R) = log(a) + b·log(t) enables OLS estimation. We report: (a) the power-law exponent b; (b) R² of the log-log fit; (c) the Pearson correlation coefficient and p-value; and (d) the SNT classification. Significance threshold α = 0.05; all tests in Python 3.11 (scipy.stats). Reproducible from `reconstruction_real/code/build_aco_v29.py` and public scripts.

---

## 3. Results

### 3.1 Competitive exclusion (E1) — b̄ = +2.891

Competitive exclusion cases produce the highest and most consistent b values of the three ecological domains. The pattern is systematic: introduced species with no prior coevolutionary history in the invaded ecosystem produce the fastest displacement dynamics, consistent with the absence of coevolved resistance mechanisms — an ecological analogue of zero institutional friction (Friction index = 0 in the SNT ordinal scale).

Key cases: African honeybee (Apis mellifera scutellata) vs European honeybee in Brazil — accidental 1957 introduction of 26 African queens (Warwick Kerr 1967) drove a 300–500 km/year expansion; brown rat (Rattus norvegicus) over black rat (R. rattus) in Europe — the fastest continental vertebrate displacement documented in the corpus (He Yu et al., Nature Communications 2022). All 4 competitive exclusion cases are statistically significant (p < 0.05) and produce b > 1, placing them in the Roche Radius zone (accelerated absorption).

### 3.2 Predator-prey (E2) — b̄ = +0.145

The two predator-prey cases produce b values close to zero, consistent with the SNT prediction that mutual interdependence prevents definitive satellization. The Canadian lynx-hare system (Hudson's Bay Company fur records 1845–1935 — the most cited case in population ecology and the empirical source of Lotka-Volterra): b = -0.201 (n.s.). The Adriatic fish case (D'Ancona 1924; Volterra 1926): b = +0.198 (n.s.). Both non-significant. The reason is structural: predator-prey relations are governed by oscillatory cycles, not monotonic trajectories. The power-law model captures unidirectional divergence well but not systems alternating between satellization and recovery — neither node can definitively satellize the other because one's extinction would destroy the other.

This constitutes refutation criterion RC8: the SNT monotonic-satellization model does not apply where mutual interdependence between hub and node creates stable oscillatory cycles. The near-zero b is not a failure of the model — it is the correct prediction.

### 3.3 Parasite-host (E3) — b̄ = +0.912

Parasite-host cases produce b values intermediate between predator-prey and competitive exclusion, with the largest n in the biological corpus (234 cases) and 100% significance rate. The strongest individual case is antibiotic-resistant bacteria vs sensitive bacteria (b = +1.401, R² = 0.935, p < 0.001) — the antibiotic is an abrupt exogenous trigger that inverts the dominance ratio in ~60 months, the microbiological equivalent of a leapfrog via orthogonal dimension.

The E3 domain is dominated by the COVID-19 corpus (234 country-level series, JHU CSSE), which produces b̄ = +0.912 at 100% significance. This large n reflects the cross-national replication of the same epidemic dynamic and must be interpreted accordingly: the 234 cases are not statistically independent (the same pandemic measured 234 times). The antiretroviral therapy case (HAART post-1996) provides the clearest biological leapfrog: the drug functions as an orthogonal dimension inverting the HIV-CD4 ratio, where the virus cannot compete.

---

## 4. The Mutual Interdependence Brake (RC8)

The consistent near-zero b in predator-prey systems deserves theoretical attention. The **mutual interdependence brake** is a general principle: in any ecological relationship where the hub node depends on the continued existence of the peripheral node for its own survival, the power-law exponent b is constrained toward zero by the self-destructive consequence of complete satellization.

This principle operates identically in predator-prey ecology, sovereign-state geopolitics (country pairs, b̄ = +0.092), and stellar binary systems in equilibrium accretion (stellar binaries, b̄ ≈ 0) — the same mathematical constraint across different substrates. Finding 4 of the SNT v30 corpus: sovereign country pairs (b̄ ≈ +0.09) and predator-prey systems (b̄ = +0.145) are statistically indistinguishable (Mann-Whitney p = 2.4×10⁻⁷⁴ separating these from friction-free domains). Two distinct mechanisms produce mechanically equivalent brakes.

**RC8 falsification condition:** falsified if predator-prey systems with no alternative prey sources sustain b > 0.5 without exogenous perturbation.

---

## 5. Coupled Orbital Collapse Layer (ACO-A) — Biological Evidence

This revision integrates the Coupled Orbital Collapse architecture (ACO-A), reformulated in SNT v30 as a universal orthogonal axis. Each system is described by two independent coordinates: Axis 1 — Satellization (b, how dominance evolves while the coupled relationship runs) and Axis 2 — Collapse (Δ, A(t) = c·τ^Δ, speed/shape of absorption once the hub undergoes functional extinction). The axes are orthogonal: corr(b, Δ) ≈ 0 (first test, crypto n=11, Spearman r = +0.009, p = 0.98; cross-domain test pending).

**Biological collapse evidence — Regulated Orbital Decay.** The Omicron wave in South Africa (JHU CSSE; peak 14 Dec 2021, ~23,437 cases/day, falling to 11% of peak in 49 days) provides the clearest biological collapse case. Fall fit: power law R² = 0.863; exponential R² = 0.958 (e-fold ~22 d). The fall is smooth and non-accelerating — Regulated Orbital Decay, not a Catastrophic Cliff. The mechanism is intrinsic epidemiological friction (immunity acquisition, susceptible depletion, R_eff < 1), which prevents the accelerating super-exponential collapse that characterizes friction-free systems (e.g., LUNA crypto, 5.6 orders of magnitude in 11 days). Reproducible via `reconstruction_real/code/bio_unbounded_collapse.py`.

**Biological collapse mode classification.** The variant-frequency transition Delta→Omicron (CoV-Spectrum/LAPIS, South Africa) constitutes a Logistic Sweep (bounded magnitude, frequency ceiling = 100%; k = 0.218/d, R² = 0.79) — the collapse of the Delta variant and simultaneous absorption by Omicron follow an S-curve because frequency is bounded [0,1] by construction.

| Mode | Biological instance | Friction | Fit |
|------|-------------------|----------|-----|
| Regulated Orbital Decay | Omicron wave (absolute counts) | intrinsic epidemiological | Exponential, R² = 0.958 |
| Logistic Sweep | Delta→Omicron (South Africa, frequency) | bounded ceiling | k = 0.218/d, R² = 0.79 |

**Collapse-axis falsifiability criteria (biological):** RC-D1 (orthogonality b⊥Δ) remains untested cross-domain. RC-D2 (friction governs collapse shape) is consistent with the biological evidence: intrinsic epidemiological friction produces Regulated Decay, not a Cliff. A biological collapse WITHOUT intrinsic friction — an abrupt external shock to an epidemic — would be the key test for RC-D2 in this domain.

---

## 6. H-φ Hypothesis — Closed

**Status: REFUTED after 4 independent rounds.**

H-φ posited that the exponent b would cluster near fractions of the golden ratio (φ = 1.618...), the set {φ/4, φ/3, φ/2, 2φ/3, 3φ/4, φ} ±0.10.

| Round | Data | Result |
|-------|------|--------|
| 1 | Crypto (BTC/altcoins) | 0/4 datasets with a φ signal |
| 2 | Primary biological literature | 0/6 datasets with a signal |
| 3 | Real corpus n=188, b>0 | p = 0.642 — identical to chance |
| 4 | Full corpus n=534 + **placebo control** | apparent signal (p<0.001 vs uniform null) collapses under placebo (p=0.170); bio "signal" is COVID pseudoreplication |

Round 4 identified two methodological traps: (1) **band coverage** — the 6 φ-bands (±0.10) densely tile [0.3–1.3], exactly where b concentrates; a placebo of 6 random targets in the same range shows φ is not special (p = 0.170); (2) **pseudoreplication** — the surviving biological "signal" (E1+E3 friction-free, p<0.001 under placebo) is driven by 234 countries measuring the same pandemic (COVID), not independent data; COVID's characteristic b ≈ 0.846 falls 0.037 from φ/2 = 0.809 — a single coincidence replicated 234×. Reproducible via `papers/phi_retest.py` + `papers/phi_placebo.py`.

H-φ does not affect the validity of the central SNT framework, the exponent b, or any main finding.

---

## 7. Falsifiability Criteria

| RC | Refutation condition | v30 Status |
|----|---------------------|------------|
| RC1 | Power law fits no better than linear/exponential across biological domains | NOT REFUTED |
| RC2 | b is not reproducible from primary series | NOT REFUTED |
| RC8 | Predator-prey systems with no alternative prey produce sustained b > 0.5 without exogenous trigger | NOT REFUTED |
| RC-D1 | corr(b, Δ) significantly ≠ 0 across paired cases | NOT REFUTED (crypto n=11, r=+0.009; cross-domain untested) |
| RC-D2 | High-friction biological collapse does NOT follow Regulated Decay | NOT REFUTED (Omicron wave R²=0.958 exponential) |
| RC-D3 | A biological system with hazard = 0 is found | NOT REFUTED |

---

## 8. Limitations

The E3 corpus (234 cases) has high n but low independence: all cases measure the same COVID-19 pandemic across countries, which introduces pseudoreplication that must be accounted for in any interpretation of E3 statistics. The E1 corpus (n=4) has high significance (4/4) but small n; additional invasion cases are needed before claiming generality. The predator-prey sub-corpus (E2, n=2) has insufficient n for statistical conclusions beyond the directional finding of b ≈ 0. The collapse layer is correlational and, on the biological side, based on a single epidemic wave; it is framed as a strong hypothesis, not causal proof. Causal claims require pre-registration and larger cohorts.

---

## 9. Conclusions

The power-law model of ecological satellization provides a unified quantitative framework for comparing displacement rates across competitive exclusion, predation, and parasitism in a corpus of 240 real cases. The exponent b systematically distinguishes ecological relationship types: competitive exclusion b̄ = +2.891 (n=4, 100% significant), parasite-host b̄ = +0.912 (n=234, 100% significant), predator-prey b̄ = +0.145 (n=2, 50% significant). The near-zero b in predator-prey systems reflects the mutual interdependence brake — a constraint that operates identically in ecology and geopolitics (RC8). Friction-free biological domains satellize ~10× faster than friction-laden economic domains (Mann-Whitney p = 2.4×10⁻⁷⁴). Biological collapse follows Regulated Orbital Decay under intrinsic epidemiological friction, not the Catastrophic Cliff observed in friction-free systems — consistent with the Principle of Least Friction unifying the collapse layer. The H-φ hypothesis is refuted across four rounds and excluded from main claims. The full replication package is available at https://doi.org/10.5281/zenodo.19446521.

*"The satellization algorithm is predictable. What is predictable can be intervened."*

---

## References

Barabási, A.L. & Albert, R. (1999). Emergence of scaling in random networks. *Science*, 286(5439), 509–512.

Bolt, J. & van Zanden, J.L. (2024). Maddison Project Database 2023. University of Groningen.

CoV-Spectrum / LAPIS (2022). SARS-CoV-2 variant frequency data. https://lapis.cov-spectrum.org/

Dong, E., Du, H. & Gardner, L. (2020). An interactive web-based dashboard to track COVID-19 in real time. *The Lancet Infectious Diseases*, 20(5), 533–534. [JHU CSSE]

Elton, C. & Nicholson, M. (1942). The ten-year cycle in numbers of the lynx in Canada. *Journal of Animal Ecology*, 11(2), 215–244.

Gause, G.F. (1934). *The Struggle for Existence*. Williams & Wilkins.

Hamilton, W.D. (1980). Sex versus non-sex versus parasite. *Oikos*, 35(2), 282–290.

He Yu et al. (2022). Introgression, displacement, and collapse: The replacement of the black rat by the brown rat in Europe. *Nature Communications*, 13, 2656.

Holling, C.S. (1973). Resilience and stability of ecological systems. *Annual Review of Ecology and Systematics*, 4, 1–23.

Kerr, W.E. (1967). The history of the introduction of African bees in Brazil. *South African Bee Journal*, 39, 3–5.

Lotka, A.J. (1925). *Elements of Physical Biology*. Williams & Wilkins.

MacLulich, D.A. (1937). Fluctuations in the numbers of the varying hare. *University of Toronto Studies, Biol. Ser.* 43.

Pantaleo, G. et al. (1993). New concepts in the immunopathogenesis of human immunodeficiency virus infection. *NEJM*, 328(5), 327–335.

Thom, R. (1972). *Stabilité structurelle et morphogénèse*. [fold catastrophe]

Volterra, V. (1926). Fluctuations in the abundance of a species considered mathematically. *Nature*, 118, 558–560.

Zainos Corona, E. (2026). Shadow Node Theory v2.5.0 — Replication Package (721-case real corpus + Coupled Collapse layer ACO-A). Zenodo. https://doi.org/10.5281/zenodo.19446521

---

*Fractal Core Research — Tlaxcala, Mexico · v30 · July 2026*

*"Technical truth above numerical impression."*
