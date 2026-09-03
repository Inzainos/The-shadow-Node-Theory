# Scale-Invariant Satellization: A Power-Law Framework for Node Dominance Governed by Institutional Friction


Elán Zainos Corona
Fractal Core Research, Tlaxcala, Mexico
ORCID: 0009-0009-9125-253X
Correspondence: elan.zainos.corona@gmail.com

Preprint identifiers: SSRN 6418778 · Zenodo DOI 10.5281/zenodo.19446521
Code and data: github.com/Inzainos/The-shadow-Node-Theory
JEL: O11, O18, R11, D85, C22, O33


---


## Abstract

When two coupled entities interact over time — a dominant "hub" and a peripheral "node" — the ratio of their relative standing often evolves in a regular way. This paper introduces a descriptive framework, Shadow Node Theory (SNT), that characterizes this evolution through a single scaling exponent b, estimated by fitting the dominance ratio R(t) = metric_hub(t) / metric_node(t) to a power law R(t) = a·t^b on logarithmic axes. The sign and magnitude of b summarize the direction and speed of "satellization" — the process by which a peripheral entity loses or gains relative standing against a dominant core.

We assemble a corpus of 721 empirical cases spanning eleven domains and reconstructed entirely from verifiable primary sources: national GDP per capita (Maddison Project Database), subnational economic hierarchy (INEGI, US Census), epidemic growth (Johns Hopkins/OWID COVID-19 records), predator–prey cycles (Hudson Bay records), planetary and stellar mass ratios (Open Exoplanet Catalogue), and developer-platform behavioral data (HackerEarth). Every value of b and every coefficient of determination is reproducible from the primary series via published scripts; no value is synthetically generated.

The central finding is that the satellization exponent varies systematically with institutional friction. Across 714 social and biological cases, the Spearman correlation between an a-priori ordinal friction index and b is ρ = −0.68 (p = 2.5×10⁻⁹⁷). Systems lacking institutional or interdependence-based friction — invasion wavefronts and epidemic growth — exhibit strongly positive, often superlinear exponents (mean b ≈ +0.95), whereas systems with strong friction — sovereign national economies and subnational hierarchies — cluster near b ≈ +0.09 (Mann–Whitney U = 103,538, p = 2.4×10⁻⁷⁴). We do not claim that the power law is the unique generative model in every domain; formal model comparison shows it is the best fit where friction is low and is one of several competitive forms where friction is high. Rather, b serves as a comparable cross-domain metric of satellization. We provide a behavioral application — an Atomic Sovereignty Index (ASI) — that predicts user attrition on a developer platform (held-out ROC-AUC = 0.715).


---


## Author Summary

Why do some weaker entities slowly catch up to dominant ones, while others are rapidly absorbed? A struggling national economy may converge toward a wealthier neighbor over a century; an invasive species may overrun a territory in a few seasons; a new user on a platform may either build a durable foothold or churn within days. This paper asks whether a single number can describe the direction and speed of these very different processes.

We define that number as a scaling exponent, b, measured from how the ratio between a dominant "hub" and a peripheral "node" changes over time. A negative b means the node is catching up; a positive b means it is falling behind; a value above one means it is being absorbed at an accelerating rate.

Our key result is that b is governed by what we call institutional friction — the resistance a system has against rapid absorption. National economies, protected by sovereignty and institutions, show b near zero: friction holds them in place. Epidemics and biological invasions, which face no such brake until immunity or saturation sets in, show large positive b. The relationship is strong and holds across 721 cases drawn entirely from public, verifiable data. We are explicit about where the power law is and is not the best statistical model, and we treat b as a descriptive yardstick rather than a universal law of nature.


---


# 1. Introduction

Across the social, biological, and physical sciences, researchers repeatedly encounter a common structural situation: a dominant entity (a "hub") and a dependent or peripheral entity (a "node") that interact over time, with the relative standing of the two shifting in a measurable way. Economists study whether poorer countries converge toward richer ones. Ecologists study how an invasive species displaces native populations. Astronomers describe how a massive body gravitationally dominates smaller ones. In each case there is an implicit dynamic of relative dominance evolving in time.

This paper proposes a deliberately minimal, descriptive framework for that dynamic. We define the dominance ratio

    R(t) = metric_hub(t) / metric_node(t)

where the metric is whatever quantity expresses standing in the domain (GDP per capita, population, accumulated cases, mass). We then ask how R(t) scales with elapsed time t, fitting

    R(t) = a · t^b   ⟺   log R(t) = log a + b · log t

by ordinary least squares on logarithmic axes. The exponent b is the object of interest. We call the process satellization, by analogy with a small body falling into a stable or decaying orbit around a larger one, and we call b the satellization exponent.

The interpretation of b is straightforward:
- b < 0: the node is gaining relative standing (convergence).
- b ≈ 0: the relationship is roughly stable.
- 0 < b < 1: the node is losing standing sublinearly (gradual satellization).
- b ≥ 1: the node is losing standing superlinearly (accelerating absorption). We refer to the threshold b = 1 as the Roche Radius of the framework, borrowing the astronomical term for the distance within which tidal forces overwhelm a satellite's self-cohesion.

The classification of b into these regimes, and the identification of b = 1 as a critical threshold, are the original conceptual contributions of this framework; the log-log fitting procedure itself is standard.

We make a specific, testable claim: the satellization exponent is governed by institutional friction — the structural resistance a system possesses against rapid absorption. Sovereign nations possess strong friction (monetary policy, borders, institutions); epidemics in a naive population possess essentially none. If the claim holds, b should correlate negatively with any reasonable a-priori ordering of domains by friction.

We are careful about scope. We do not claim that R(t) is generated by a power law in any deep mechanistic sense, nor that the power law outperforms all alternative functional forms in every domain. As we show in Section 3.4, the power law is the best-fitting model precisely where friction is lowest and is merely competitive where friction is high. Our claim is narrower and, we argue, more defensible: b is a useful, comparable cross-domain descriptor of the direction and speed of satellization, and its variation is structured by friction.

A note on this version. An earlier formulation of this corpus relied in part on parametrically generated case values. The present version replaces that corpus entirely with cases reconstructed from primary data sources, each reproducible from the underlying series. This was done specifically to ensure that every reported statistic can be independently verified, in keeping with the data-transparency standards expected of computational work.


---


# 2. Methods

## 2.1 The dominance ratio and exponent estimation

For each case we obtain two time series: a hub metric and a node metric, sampled at common time points. We compute R(t) = metric_hub(t) / metric_node(t), set the time index t = 1, 2, …, n over the observed window, and estimate b by ordinary least squares of log R(t) on log t. We record:
- b: the slope (satellization exponent);
- R²: the coefficient of determination of the log-log fit (by construction in [0, 1]);
- the Pearson r and its two-sided p-value;
- the standard error of b and the implied 95% confidence interval;
- the Durbin–Watson statistic for residual autocorrelation;
- n: the number of observations.

A case is labeled statistically significant when the slope's p-value is below 0.05. We emphasize that R² here is a genuine coefficient of determination bounded in [0, 1]; the corpus contains no out-of-range values.

## 2.2 Corpus construction from primary sources

The corpus comprises 721 cases across eleven domains, each drawn from a documented
public source. Cases were included by fixed criteria — two coupled entities in
critical proximity, an identifiable onset, and at least four temporal points — with
no exclusion by outcome direction (both converging, b<0, and absorbing, b>0, cases
are retained) to avoid confirmation bias.

**Table 1. Corpus by domain.** (Friction = a-priori ordinal level, §2.3.)

| Domain | Description | n | Primary source | Friction |
|--------|-------------|---|----------------|----------|
| A | Historical cities (urban population ratios) | 4 | UN Demographic Yearbook (modern window) | moderate |
| B | Countries (GDP per capita; hub = higher mean-GDP economy) | 446 | Maddison Project Database 2020 (Bolt & van Zanden) | high |
| C | Subnational regions (per-capita GDP hierarchy) | 24 | INEGI 2022 (Mexico); US Census historical series | high |
| D | Digital ecosystems (activity/credit/run distributions) | 3 | HackerEarth 2026 (4,771 users) | low |
| E1 | Biological/territorial invasion (colonization wavefronts) | 4 | OWID COVID-19 spatial spread | none |
| E2 | Predator–prey (lynx–hare ratios) | 2 | Hudson Bay records (MacLulich 1937; Elton & Nicholson 1942) | high |
| E3 | Parasite–host (epidemic growth phase, one case/country) | 234 | Johns Hopkins / OWID COVID-19 | none |
| F1 | Planetary systems (stellar/planetary mass dominance) | 2 | Open Exoplanet Catalogue | moderate |
| F2 | Stellar (mass–radius relation) | 1 | Open Exoplanet Catalogue | moderate |
| F3 | Multiplanet hierarchy (intra-system mass dominance) | 1 | Open Exoplanet Catalogue | low |

All series, extraction scripts, and per-case outputs are published in the project
repository, allowing every reported value to be regenerated.

## 2.3 The institutional friction index

We assign each domain an a-priori ordinal friction level on a 0–3 scale, fixed before examining the exponents, reflecting the structural resistance to rapid absorption:
- 3 (high): national economies (B), subnational hierarchies (C), predator–prey systems (E2, mutual ecological dependence).
- 2 (moderate): historical cities (A), planetary and stellar systems (F1, F2; orbital resonance / radiative limits).
- 1 (low): digital ecosystems (D), multiplanet hierarchy (F3).
- 0 (none): biological invasion (E1), epidemic growth (E3), where no institutional or immune brake operates during the observed window.

## 2.4 Hypothesis tests

We state, for each test, what it evaluates and why it is appropriate.
- **H1 (does friction co-vary with b?):** Spearman rank correlation between the
  a-priori domain friction level and case-level b. Spearman (not Pearson) is used
  because the relationship is expected to be monotonic but not necessarily linear,
  and it is robust to non-normal exponent distributions and outliers.
- **H2 (do the regimes separate?):** Mann–Whitney U, a distribution-free two-sample
  test, comparing b in zero-friction biological domains (E1, E3) against
  high-friction economic domains (A, B, C). It asks whether the two regimes are
  drawn from different distributions without assuming normality.
- **H3 (is the power law actually the best functional form, per case?):** AICc
  model comparison of the power law against linear, exponential, and logarithmic
  alternatives, case by case. This directly tests — rather than assumes — the
  adequacy of the power-law description and quantifies where it does and does not
  win.

## 2.5 Behavioral application: the Atomic Sovereignty Index

For the digital domain we define an Atomic Sovereignty Index (ASI) from first-session behavioral features (event-type breadth and an entropy term), normalized so that complete sovereignty (ASI ≥ 1) is rare. We evaluate whether ASI and related first-session features predict user attrition using logistic regression with a 70/30 stratified train/test split, reporting held-out ROC-AUC.


---


# 3. Results

## 3.1 Corpus overview

Of 721 cases, 644 (89.3%) are statistically significant at p < 0.05 — a marked increase over what parametric noise would produce, and a direct consequence of using real series. The mean exponent is b = +0.366 and the median is +0.179. Positive exponents (active satellization) constitute 74.1% of the corpus; superlinear exponents (b > 1) constitute 14.1%. The mean R² among significant cases is 0.58. The corpus contains zero out-of-range R² values and zero invalid p-values.

## 3.2 Finding 1: satellization rate is structured by domain

The mean exponent varies sharply and systematically across domains. Ordered from highest to lowest friction:

  Domain  Friction  n     b̄        R̄²
  B       high      446   +0.092   0.35
  C       high      24    +0.091   0.53
  E2      high      2     +0.145   0.12
  A       moderate  4     +0.082   0.18
  F1      moderate  2     −1.807   0.40
  F2      moderate  1     +1.273   0.48
  D       low       3     −1.364   0.88
  F3      low       1     +1.264   0.90
  E1      none      4     +2.891   0.81
  E3      none      234   +0.912   0.85

The economic and subnational domains (B, C), which possess the strongest institutional friction, cluster tightly near b ≈ +0.09. The zero-friction biological domains (E1, E3) show strongly positive exponents, with E1 (invasion wavefronts) reaching b̄ ≈ +2.9.

## 3.3 Finding 2: institutional friction predicts the exponent

Across all 714 social and biological cases, the Spearman correlation between the a-priori friction index and the case-level exponent b is

    ρ = −0.68, p = 2.5×10⁻⁹⁷.

This is the central quantitative result. More friction is associated with a lower satellization exponent — peripheral entities are held in place by the structural resistance of the system. The relationship is not an artifact of a few domains: it is computed over hundreds of individual cases.

The regime separation is confirmed directly. Comparing the zero-friction biological domains (E1, E3; b̄ = +0.95) against the high-friction economic domains (A, B, C; b̄ = +0.09):

    Mann–Whitney U = 103,538, p = 2.4×10⁻⁷⁴.

Biological systems without institutional brakes satellize far faster than sovereign economic systems — exactly as the friction hypothesis predicts.

## 3.4 Finding 3: where the power law fits, and where it does not

We are explicit about the limits of the power-law description. Per-case AICc model comparison on the country domain (B) shows the power law is the single best model in only ~8% of cases and statistically competitive (ΔAIC < 2) in ~21%; over a century-long window, GDP-ratio trajectories are often closer to exponential or linear. By contrast, in the zero-friction epidemic domain (E3), the power law is the best model in the majority of cases (6 of 8 in a representative subset), consistent with the unconstrained growth phase.

This pattern is itself informative. The power-law regime emerges precisely where the theory predicts satellization should be unconstrained (low friction) and flattens where friction dominates the dynamics. We therefore treat b not as evidence of a universal generative power law, but as a descriptive metric whose value, interpreted alongside model-comparison context, captures the direction and speed of satellization in a cross-domain–comparable way. This is a deliberately moderated claim relative to a strong universality reading.

## 3.5 Finding 4: sovereignty and interdependence as equivalent brakes

Within the high-friction tier, two structurally different mechanisms produce the same effect. Sovereign national economies (B, b̄ = +0.09) and mutually dependent predator–prey systems (E2, b̄ = +0.14) both hold b near zero. Political sovereignty and ecological interdependence — very different mechanisms — operate as functionally equivalent brakes on satellization, each pinning the exponent near the no-change line.

## 3.6 Finding 5: behavioral prediction (Atomic Sovereignty Index)

On the HackerEarth developer platform (n = 4,771 users; 84.8% attrition), first-session behavioral features predict churn with held-out ROC-AUC = 0.715 (train AUC = 0.719, test AUC = 0.697), confirming the absence of overfitting. Users engaging five or more distinct event types in their first session churn at 74%, versus 93% for single-event-type users — a 19 percentage-point reduction. The activity, credit, and run distributions across users follow clear power laws (R² = 0.95, 0.72, 0.95 respectively), the signature of preferential attachment in the digital domain.


---


# 4. Discussion

## 4.1 What the framework does and does not claim

The contribution of this work is a single comparable metric — the satellization exponent b — together with the empirical finding that its value is governed by institutional friction. We deliberately avoid the stronger claim that all these systems are "really" power laws. The model-comparison results in Section 3.4 would not support that claim, and we do not make it. Instead, the value of b lies in its comparability: it places a national economy, an epidemic, and a planetary system on the same descriptive axis, and that axis turns out to be organized by friction.

## 4.2 Why friction matters

The friction result has a natural interpretation. Institutions, sovereignty, and mutual dependence all act to slow the transfer of relative standing between coupled entities. Where they are present, the periphery is buffered and b stays near zero. Where they are absent — an epidemic in a naive population, an invasive species in a new range — nothing checks the accelerating transfer, and b climbs into the superlinear regime. The framework thus reframes "resilience" as the engineering of friction: a peripheral entity that wishes to avoid absorption must increase the structural resistance of its coupling to the hub.

## 4.3 The behavioral application

The Atomic Sovereignty Index demonstrates that the framework is not merely descriptive of historical series but can be operationalized predictively. A modest but genuine ROC-AUC of 0.715, validated out of sample, shows that first-session "sovereignty" — behavioral breadth — carries real signal about whether a node will persist or be absorbed (churn). This is an existence proof rather than a state-of-the-art churn model.

## 4.4 Limitations

We note several honestly. (i) Domain A (historical cities) is represented only by modern UN data with short windows and is not statistically significant; the long historical series (e.g., Bairoch) needed to test the framework on pre-modern urban dominance are not yet digitized in our corpus. (ii) Domains E1 and E3 model invasion and epidemic spread as territorial/temporal colonization using COVID-19 records; species-occurrence data (e.g., GBIF) would strengthen the strictly biological reading. (iii) The astrophysical domains (F) follow power laws but their "friction" is physical (radiative limits, orbital resonance) rather than institutional, so they sit outside the central social/biological correlation and are reported separately. (iv) The friction index is ordinal and assigned a priori; finer, continuous operationalizations are a target for future work.

## 4.5 Relation to existing literature

The friction–satellization relationship is consistent with the preferential-attachment and cumulative-advantage literatures, in which the rate of advantage accumulation depends on structural constraints. The contribution here is the cross-domain measurement of that rate via a single exponent and the demonstration that it is organized by an a-priori friction ordering spanning economics, epidemiology, and ecology.


---


# 5. Conclusion

We have introduced a minimal, descriptive framework that summarizes the direction and speed of satellization between a hub and a node through a single scaling exponent b, and we have shown, across 721 cases reconstructed entirely from verifiable primary sources, that b is governed by institutional friction (Spearman ρ = −0.68, p = 2.5×10⁻⁹⁷). Systems with strong institutional or interdependence-based friction hold their exponents near zero; systems without such friction satellize rapidly and often superlinearly (Mann–Whitney p = 2.4×10⁻⁷⁴). We are explicit that the power law is the best generative description only where friction is low, and we treat b as a comparable cross-domain metric rather than a universal law. The framework yields an operational, out-of-sample-validated predictor of absorption in a behavioral setting (ROC-AUC = 0.715).

The satellization exponent is predictable, and its governing variable — friction — is identifiable and, in principle, engineerable. What a peripheral entity does with that knowledge is not a question the model can answer.


---


## Data Availability

All primary series, extraction and analysis scripts, per-case outputs, and the consolidated 721-case corpus are openly available at github.com/Inzainos/The-shadow-Node-Theory (reconstruction_real/). Every reported statistic is reproducible from the primary sources via the included scripts. Primary data sources: Maddison Project Database 2020; INEGI 2022; US Census Bureau historical series; Johns Hopkins University / Our World in Data COVID-19 dataset; Open Exoplanet Catalogue; Hudson Bay Company records (MacLulich 1937; Elton & Nicholson 1942); HackerEarth 2026.

## Figure Legends (Figures To Be Attached At Compilation)

Figure 1. Satellization exponent distribution across domains, ordered by institutional friction, with the Roche Radius (b = 1) marked.
Figure 2. Case-level friction index versus exponent b (Spearman ρ = −0.68, p = 2.5×10⁻⁹⁷), and mean b by domain group.
Figure 3. Per-case AICc model comparison (power law vs. linear, exponential, logarithmic) and the corpus-wide distribution of b.
Figure 4. Atomic Sovereignty Index validation on HackerEarth: ASI distribution, held-out ROC curve, the 5-event threshold, and churn by sovereignty zone.


---

*Revised manuscript (v30) — PCSY-D-26-00059 — corpus of 721 real cases. Figures provided as separate high-resolution items at resubmission.*
