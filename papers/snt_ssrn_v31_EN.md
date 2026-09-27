# Shadow Node Theory v2.5.2 (manuscript r31):
## Scale Invariance in the Node Satellization Algorithm — and a Universal Coupled Orbital Collapse Layer (ACO-A)

*Empirical Verification Across 721 Real Cases, plus Collapse Evidence in Five Domains*

**Elán Zainos Corona**  
Fractal Core Research · Tlaxcala, Mexico · elan.zainos.corona@gmail.com  
DOI: https://doi.org/10.5281/zenodo.19446521 · SSRN: https://ssrn.com/abstract=6418778  
GitHub: https://github.com/Inzainos/The-shadow-Node-Theory  
Pre-print, manuscript revision r31 (2026-09-27; supersedes the v30 posted 2026-06-28) — repository release v2.5.2 — not peer reviewed. Data and methodology available for review.

> **Revision note (r31, 2026-09-27).** An internal integral audit (v32) re-derived
> every published figure from the committed data, and the Domain B data were
> re-verified. The arithmetic of the corpus replicates exactly; the inference
> layer does not. This revision therefore **withdraws** or **corrects** the
> following claims of v30, each with the evidence given in the section cited:
> (1) the "abrupt triggers are 5.9× faster than gradual" result is **withdrawn**:
> the ratio originates in a table of 2 abrupt vs 2 gradual cases (5.87×,
> p = 0.33), the reported test (U = 24,802, n = 486) matches no dataset in the
> repository, and the active corpus carries no usable trigger variable (§5, §12);
> (2) the HackerEarth churn model's ROC-AUC = 0.9994 was affected by data leakage;
> the corrected, first-session value is **0.715 ± 0.019** (§6.3);
> (3) the ASI "precision = 1.0, zero false positives" is **withdrawn as
> tautological**: it was measured against a label defined by the same ASI > 1
> threshold (§6.6); (4) the friction finding keeps its direction but its per-case
> p-value is inflated by serial autocorrelation and by treating 714 clustered
> cases as independent (cluster-level ρ = −0.56, p = 0.25; §12); (5) the
> friction-free pole of the regime contrast is COVID-19 data (§12); (6) Domain B
> (62% of the corpus) is now reproduced byte for byte from the Maddison Project
> Database **2020**, but a discriminant test leaves it supported neither as SNT
> coupling nor as β-convergence (§12). The v30 note below is kept for history.

> **Version note (v30).** This revision supersedes the previously posted SNT v2.3.1
> (502-case corpus). A June 2026 audit found that the 502-case corpus contained
> ~188 synthetically generated b values (`np.random.normal()`) and an R² column
> with impossible values (down to −7.332); it has been **retired**. This version
> uses a **721-case corpus reconstructed entirely from verifiable primary
> sources** (R² ∈ [0,1] for every case; reproducible from `reconstruction_real/`),
> and integrates a new **Coupled Orbital Collapse layer (ACO-A)**. The golden-ratio
> hypothesis (H-φ) was tested and **refuted across four rounds** (placebo control
> included) and is excluded from the main claims.

---

## Abstract

This paper presents Shadow Node Theory (SNT), a formal model of node satellization
operating across three scales of systemic resolution — Micro (Atomic Node /
individual), Meso (intra-national Fungal Network), and Macro (superorganism
collision between nations and digital platforms). The central hypothesis holds
that when two power nodes orbit in critical proximity, the node with greater
accumulated advantage satellizes the historically dominant node through an
algorithm whose dynamics follow a power law invariant to temporal scale and
substrate: R(t) = a·t^b, where b is the satellization velocity parameter.

SNT delivers four empirical contributions: (1) formalization of the
Triple-Resolution Systemic Model with distinct applicability conditions across
scales; (2) N-body matrix verification with Mexican INEGI data (32 federal
entities, b = −0.473, R² = 0.838, p < 0.001), revealing that the binary model
underestimated Tlaxcala's satellization gradient by 9.3×; (3) operationalization
of the Atomic Sovereignty Index (ASI) on behavioral data from 4,774 users and
409,287 events (HackerEarth 2026; its first-session churn model reaches
ROC-AUC = 0.715 ± 0.019 after correcting a data leakage); and (4)
a corpus of **721 cases reconstructed from verifiable primary sources** spanning
historical, economic, biological, astronomical and digital domains.

Two findings emerge from the real corpus, both with explicit inference caveats.
First, **institutional friction is negatively associated with satellization
velocity** in every analysis variant: per case, Spearman ρ = −0.68 (n = 714);
because the 714 cases are clustered in six domains and Domain B's per-case fits
are serially autocorrelated, the per-case p-value (2.5×10⁻⁹⁷) is inflated — at the
domain-cluster level ρ = −0.56 (p = 0.25, n = 6) and the cluster bootstrap
interval is [−0.72, −0.01]. Second, **regime separation**: the friction-free
domains (b̄ ≈ +0.95) satellize faster than friction-laden economic domains
(b̄ ≈ +0.09); the friction-free pole consists entirely of COVID-19 spread data
(238 cases), and removing its 234 E3 cases shrinks the friction correlation to
ρ = −0.12 (n = 480). A
previously reported third finding — abrupt triggers 5.9× faster than gradual —
is **withdrawn** in this revision (see the revision note). Domain B (country
pairs, 62% of the corpus) is reproduced exactly from the Maddison Project
Database 2020, but a discriminant test (calibrated null plus bilateral trade
from the Correlates of War) supports it neither as hub–node coupling nor as
β-convergence, so the claim that political sovereignty brakes satellization like
ecological interdependence is retained only as a hypothesis.

This revision adds a **Coupled Orbital Collapse layer (ACO-A)**: collapse is
reformulated as an orthogonal axis (Δ), with a falsifiable hazard layer
h(τ) > 0 ("no system is eternal"), a three-factor taxonomy of collapse modes
(friction × trigger × floor/ceiling), and a Principle of Least Friction unifying
them, demonstrated with real data in five domains (finance, history, crypto,
biology, astronomy). The model is accompanied by eight falsifiability criteria
(RC1–RC8) plus collapse-axis criteria, a four-step diagnostic protocol, and a
public replication package.

**Keywords:** complex systems, power law, satellization, scale invariance,
preferential attachment, institutional friction, coupled orbital collapse,
hazard function, leapfrog, Atomic Sovereignty Index, AI orchestration, digital
ecosystems, regional inequality, Tlaxcala, Mexico.

**JEL:** O18, O33, D85, C63, O11, R11, C22.

---

## 1. Introduction

### 1.1 The Scale Invariance Problem

Why do some regions remain poor despite decades of policy intervention? Why do
some nations converge toward global leaders while others diverge irreversibly?
These questions share a structural feature that aggregate models consistently
fail to capture: the dynamics of resource extraction between proximate nodes
operating at different hierarchical levels. Standard development economics models
the poverty trap as a problem of insufficient capital accumulation. Shadow Node
Theory proposes a different mechanism: satellization — the progressive extraction
of productive residual energy from a peripheral node by a dominant hub — whose
dynamics follow a power law invariant to temporal scale and substrate.

### 1.2 Theoretical Background

The preferential attachment mechanism (Barabási & Albert, 1999) establishes that
scale-free networks emerge inevitably when new connections form with probability
proportional to existing degree. SNT formalizes the directional flow of resources
within such networks, quantifying the rate of divergence between hub and shadow
node through the power-law exponent b. Leapfrogging theory (Brezis & Krugman,
1993) identifies conditions under which a peripheral node can bypass a dominant
one through orthogonal-dimension investment. SNT extends this to three scales and
formalizes the failure conditions the original model left undeveloped.

### 1.3 The Gap in the Literature

Three gaps motivate this work. First, no existing model quantifies satellization
dynamics across historical cities, nation-states, intra-national regions and
digital platforms within a unified formal framework. Second, the trigger taxonomy
in leapfrogging theory collapses event types into a single category, missing a
possible distinction between abrupt and gradual triggers (an empirical question
the current corpus cannot yet test; see §5). Third, no operational index of
cognitive sovereignty exists for the Atomic Node (individual) computable from
observable behavioral data without self-report. A fourth gap, addressed by this
revision, is the absence of a unified, falsifiable account of how systems
**collapse** once the satellization relationship ends — the Coupled Orbital
Collapse layer (Section 13).

---

## 2. Formal Theoretical Framework

### 2.1 Definitions

A **Shadow Node** (or Peripheral Node) is any system component whose productive
output is systematically extracted by a dominant hub over time, resulting in
progressive divergence of productive capacity. A **Hub Node** is the dominant
component that absorbs the residual productive energy of shadow nodes, increasing
its own gravitational-mass advantage. **Critical Proximity** is the spatial,
institutional, or digital proximity threshold below which the hub can extract
resources at rates exceeding the shadow node's regeneration capacity.

The satellization ratio R(t) = production_hub(t) / production_shadow(t) is the
central observable. When R(t) follows a power law R(t) = a·t^b with b > 0,
satellization is active. When b < 0, convergence or leapfrog is occurring. The
exponent b is the velocity parameter: b > 0.45 indicates accelerated satellization;
0.1 < b < 0.45 indicates gradual satellization; −0.1 < b < 0.1 indicates
approximate steady state; b < −0.1 indicates convergence or leapfrog. (v30 tied
the accelerated band to an "abrupt-trigger class"; that link is withdrawn in r31.
The superlinear band b ≥ 1 may partly reflect model misspecification — see
Finding 5 in §12.)

### 2.2 Central Hypothesis

When two nodes orbit in critical proximity within the same system, the
satellization ratio R(t) = production_hub(t) / production_shadow(t) follows a
power law R(t) = a·t^b where b > 0 represents the satellization velocity and t is
elapsed time since the trigger event. This relationship is invariant to: (a)
temporal scale — it holds from medieval city-pairs to digital platform rivalries;
(b) production substrate — it holds for population, GDP per capita, behavioral
event counts, and market share; and (c) system level — it holds for individuals,
cities, regions, nations, and digital ecosystems.

### 2.3 Falsifiability Criteria

RC1 — Scalar Velocity: falsified if a technology is systematically adopted faster
by institutions than by individuals (RC1a), or if a technology emerges without
individual access that inverts the TC_micro < TC_meso < TC_macro hierarchy (RC1b).
RC2 — Immune Response: falsified if hubs systematically adapt toward peripheral
node capabilities rather than suppress them. RC3 — Qualitative Inextractability:
falsified if a hub systematically neutralizes a node's knowledge differential
through brain drain, reverse engineering, or deliberate saturation. RC4 — Dual
Minimum Threshold: falsified if a leapfrog sustains itself with either RQ or RL
below the operational minimum. RC5 — Expansion Sequence: falsified if direct
expropriation produces more stable outcomes than silent absorption for the same
node class. RC6 — Irreversibility: falsified if a Shadow Node reverses
satellization from inside the system without an exogenous trigger, with the hub
operating normally.

---

## 3. Methodology

### 3.1 General Design

The study follows a mixed quantitative design combining historical case analysis,
N-body matrix modeling for the Mexican regional system, machine-learning
validation on digital behavioral data, and survival analysis for the collapse
layer. The unifying analytical pipeline consists of: (1) construction of the
satellization ratio time series R(t) for each case pair; (2) log-log
linearization; (3) ordinary least-squares regression to estimate parameters a and
b; (4) Pearson correlation in log space for significance testing; and (5)
interpretation via the SNT taxonomy.

### 3.2 Case Selection Criteria

Cases were included if they satisfy four conditions: (a) two nodes in critical
proximity within the same system; (b) an identifiable trigger event or process;
(c) production or population data at a minimum of four temporal points spanning at
least 50 years (or 5 years for digital cases); and (d) the satellization process
has either completed or is actively ongoing. No cases were excluded based on
outcome direction — both satellization (b > 0) and convergence/leapfrog (b < 0)
cases are included to avoid confirmation bias.

### 3.3 Data Sources (real corpus, v30)

The 721-case corpus is reconstructed entirely from verifiable primary sources:
Maddison Project Database 2020 (country pairs; the committed edition reproduces
all 446 Domain B cases byte for byte), INEGI and
US Census (intra-national regions), Our World in Data / Johns Hopkins CSSE
(COVID-19 spatial and parasite-host series), the Open Exoplanet Catalogue
(planetary/stellar/multiplanetary), MacLulich (1937) and Elton & Nicholson (1942)
(predator-prey), and the HackerEarth 2026 dataset (digital; N=4,774 users,
409,287 events, 141 event types; proprietary, aggregate results only).
Integrity: R² ∈ [0,1] for all cases (zero negative, zero above 1). 89% of cases
are **nominally** significant (p < 0.05, OLS on log-log without autocorrelation
correction); after an AR(1) correction, only 156 of Domain B's 446 cases are
estimable (effective n ≥ 3) and 33–112 of those remain significant.
Reproducibility is partial: Domain B regenerates exactly from the committed
Maddison 2020 file; the raw COVID-19 series behind Domains E1/E3 are public but
not committed (only fitted summaries); the HackerEarth data are proprietary.

### 3.4 Analysis Pipeline

For each case pair, R(t) is computed at each temporal observation point. Time t is
measured in years (or days for digital cases) elapsed since the trigger. The
log-log transformation log(R) = log(a) + b·log(t) enables OLS estimation. We
report (a) the power-law exponent b; (b) R² of the log-log fit; (c) the Pearson
correlation coefficient and p-value; and (d) the SNT classification. For the
N-body Mexican matrix, we additionally compute the composite gradient — the total
satellization force on each node accounting for all higher-level hubs.

### 3.5 Statistical Tests

Institutional-friction effect: Spearman correlation between an a-priori friction
index (ordinal 0–3) and b per case (social/biological domains). Regime separation:
Mann-Whitney U between friction-free and friction-laden economic domains.
Because cases are clustered within domains, r31 adds cluster-level Spearman
(domain means), a cluster bootstrap and domain-exclusion variants (without E3;
without E3 and B); serial
autocorrelation of Domain B fits is handled with an AR(1) effective-n correction
(Durbin-Watson). The trigger-type effect (abrupt vs gradual) was recalculated on
every trigger-labeled dataset in the repository (§5). Domain B's construct is
examined with a discriminant test: correlation of b with the initial GDP gap
compared against a synthetic null calibrated to the Maddison data (the hub is
assigned by mean GDP, which couples gap and slope by construction), and
correlation of b with bilateral trade shares (Correlates of War Trade v4.0).
Collapse layer: Spearman ρ(b, Δ) for orthogonality and Kaplan-Meier survival for
the hazard. Significance threshold α = 0.05; all tests in Python 3.11
(scipy.stats); scripts in the public repository.

---

## 4. Results — Historical Case Studies

*Note (r31): the four historical cases below come from the original v1.0 study.
They are illustrative case studies, not part of the 721-case active corpus, and
their values are reported as originally estimated.*

### 4.1 Bruges → Antwerp (1300–1560)

Mechanism: physical infrastructure collapse (silting of the Zwin Canal, c.1490).
R(t) = Antwerp/Bruges population follows a power law with b = +0.739 (R² = 0.868).
Classified as accelerated satellization with abrupt trigger. Bruges had been the
dominant commercial hub of Northern Europe for two centuries before the canal
silting cut off maritime access; Antwerp, with open Scheldt access, absorbed the
commercial network within two generations.

### 4.2 Toledo → Madrid (1528–1787)

Mechanism: pure political decree (Philip II's transfer of the imperial court,
1561). R(t) = Madrid/Toledo population: b = +0.694 (R² = 0.924), the best fit of
the set. Toledo was the largest city in Castile; Madrid a village of fewer than
4,000 in 1528. Within 40 years of the court transfer, Madrid had surpassed Toledo
— political decree alone, without geographic advantage, is sufficient to generate
high-velocity satellization.

### 4.3 Portugal vs. Northwestern Europe (1535–1980)

Mechanism: Iberian Union (1580) combined with the accumulated Atlantic advantage
of NW European powers. Trigger classified as hybrid. R(t) = NW Europe GDP pc /
Portugal GDP pc: b = +0.060, R² = 0.123 — the low fit reflects an oscillatory
process (Brazilian gold caused partial recoveries 1700–1750). The long-run trend
is unambiguously divergent (the gap multiplied 3.5× between 1535 and 1913).

### 4.4 Tlaxcala → Puebla (1550–2022)

Mechanism: cumulative colonial extraction + differential industrialization.
R(t) = Puebla/Tlaxcala GDP per capita: b = +0.184 (R² = 0.567), gradual
satellization. Critically, the binary model underestimates Tlaxcala's actual
satellization by measuring only the Tlaxcala–Puebla gradient; the N-body matrix
(Section 8) reveals that 89.2% of extraction flows directly to Mexico City,
making the true composite gradient 9.3× larger.

---

## 5. Discussion: The Two-Speed Taxonomy

### 5.1 The Central Finding

The historical cases suggest two classes of satellization dynamics.
Abrupt-trigger cases (Bruges-Antwerp, Toledo-Madrid) generate exponents in the
range b = 0.69–0.74; gradual/hybrid cases (Portugal, Tlaxcala) generate b =
0.06–0.18; the ratio of class means is 5.87×. **This is a hypothesis, not a
confirmed result** (revised in r31). With 2 cases per class the Mann-Whitney test
cannot reach significance (p = 0.33, its smallest attainable value). v30 stated
that the ordering was "confirmed at scale" in the 721-case corpus (U = 24,802,
p = 1.91×10⁻⁵, n = 486); the audit found that n = 486 matches no dataset in the
repository and that the active corpus has no usable trigger variable (the
446 Domain B cases are all coded "gradual" by assignment), so that statement is
withdrawn. A historical 57-case corpus gives a ratio of 6.3 (p = 0.053), but it
predates the verified corpus and contains impossible R² values, so it is not
citable. The only active data with a trigger label are the 18 cases of the
collapse layer, which measure a different exponent (absorption after the hub's
functional extinction); there gradual ≥ abrupt (ratio 0.47, p = 0.10), with the
trigger confounded with domain. Testing the two-speed hypothesis requires a
satellization corpus with independently coded triggers.

### 5.2 Qualitative Interpretation (hypothesis)

The key theoretical distinction is not the magnitude of the trigger but its
reversibility. An abrupt trigger — infrastructure collapse, political decree —
produces irreversible structural change the shadow node cannot compensate through
internal resource mobilization. A gradual trigger — differential industrialization,
slow technological diffusion — allows temporary adaptive responses that compress
the b exponent without reversing the underlying dynamic.

### 5.3 Implications for Early Intervention

The b exponent has direct policy implications. A node with b = 0.70 faces a
satellization horizon on the order of decades before the gap becomes structurally
irreversible. A node with b = 0.18 has a longer window but the same terminal
outcome absent intervention. The SNT diagnostic protocol (Section 11) provides a
four-step procedure for estimating the current b, identifying the horizon of
events, and designing orthogonal-dimension interventions that can generate b < 0
(convergence) without triggering the hub's immune response.

---

## 6. Digital Validation: HackerEarth 2026

### 6.1 The Experiment

The HackerEarth 2026 dataset provides a behavioral event log for 4,774 users of
the Zerve data-science platform across a 98-day window: 409,287 events, 141 event
types. This constitutes a closed Meso-level system: the platform (hub) and its
users (nodes), with resource flows measured as behavioral engagement metrics.

### 6.2 The Fractal Gap

The Composite Success Index v3 (CSI_V3), a weighted combination of tool diversity
(0.40), platform lifetime (0.30) and Velocity of Diversification Rate (VDR, 0.30),
reveals a fractal discontinuity. The Elite cohort (top 0.5%, n=24) shows a VDR
7,478× greater than the Basic cohort median (bottom 93.1%, n=4,444). This is not a
power-law tail — it is a fractal discontinuity consistent with the SNT prediction
of a Hub–Shadow Node separation following preferential attachment.

### 6.3 The 5-Event Wall

A Gradient Boosting Classifier predicting churn from **first-session** features
reaches ROC-AUC = 0.715 ± 0.019 (5-fold CV). *Correction (r31):* v30 reported
ROC-AUC = 0.9994 (1.0000 in CV); that model used features accumulated over each
user's whole trajectory, including post-churn activity — a data leakage already
corrected in the repository's validation script. Users triggering fewer than five
distinct event types churn far more often — the 5-Event Wall — detectable within
the first session. These figures come from the proprietary event log and cannot
be re-derived from the public repository (the retention target is not
distributed).

### 6.4 SHAP Rankings and the Cognitive Leapfrog

The top SHAP-ranked predictor is AI-agent orchestration (agent_accept_suggestion,
SHAP proxy ~0.5). Users who delegate execution to the AI agent rather than
executing linearly are the strongest predictor of Elite-trajectory behavior — the
cognitive leapfrog: transitioning from linear execution to agent orchestration, a
dimension where accumulated hub advantage does not apply and which is currently
accessible to new entrants.

### 6.5 Extension to the Enterprise Domain

The HackerEarth case is the first empirical demonstration of SNT applied to a
closed enterprise ecosystem. The applicability condition is not sector or size but
the availability of structured behavioral event data measuring inter-node resource
flows. Five metrics of the Composite Enterprise Sovereignty Index (CSIE) — event
volume per node, sustained activity, response time, functional diversity, and
failure resilience — identify satellization within organizational structures
before it becomes structurally irreversible.

### 6.6 The Atomic Sovereignty Index (ASI) — status (r31)

ASI = δH · α / F is computable from behavioral data (the formula replicates from
the published scores to numerical precision), and the threshold ASI > 1 singles
out 13 of 4,774 users (0.27%). v30 reported that ASI classifies sovereignty with
"precision = 1.0, zero false positives". That figure is **withdrawn**: the
sovereignty label it was scored against is defined as ASI > 1, so the
classification is tautological. A valid test requires an outcome measured
independently of ASI (e.g., observed retention); the corrected first-session
churn model (§6.3) is the only external check available so far, and it is not
reproducible from public data.

---

## 7. SNT Triple-Resolution Systemic Model

The model extends the original binary model across three scales with distinct
dynamics, actors, and incompatible competitive rules. The five-level taxonomy and
INEGI 2022 verification are consistent with the Mexican national system operating
under preferential attachment (a rank-size fit; see the caveat in §8);
trajectory vectorization for eight entities (1940–2022)
documents the first cases of successful leapfrog within the system: Querétaro
(b = −0.155, p < 0.01) and Nuevo León (b = −0.058, p < 0.001).

**7.1 Micro Resolution — The Atomic System.** The base scale of processing and
survival. Resources divide into Quantitative (RQ, extractable: capital, time,
infrastructure) and Qualitative (RL, inherent: knowledge, skills, cognitive
maturity). RL cannot be directly extracted but degrades through disuse when RQ
scarcity prevents its maintenance. Leapfrog requires two parallel dimensions:
Intrapersonal (DI, mandatory base) and Professional (DP, visible leap).

**7.2 Meso Resolution — The Intra-national Fungal Network.** A closed ecosystem
delimited by geopolitical or institutional jurisdiction. The Central Hub
administers the network through continuous extraction of residual energy from
Shadow Nodes. The hub is practically immovable from inside; its immune response
activates based on growth direction, not size. The hub expands via silent
absorption, peaceful agreement, or expropriation — in that order of energetic-cost
preference.

**7.3 Macro Resolution — The Superorganism Collision.** Competition between
complete fungal networks; no central hub arbitrates. Relative position is set by
Gravitational Mass (MG: total GDP, population density, technological level,
territorial area). The real brake on aggressive expansion is the internal node
network, not international regulators. The Atomic Node never fully escapes the
Macro system: its legal and fiscal existence is anchored to its resident
superorganism.

**7.4 Cross-Scale Interaction Principles.** Cascade Transmission: Macro events
impact all three systems in descending cascade (Macro → Meso → Micro), at a speed
depending on each node's dimensional independence. Scalar Velocity:
TC_micro (hours–months) < TC_meso (months–years) < TC_macro (decades–generations),
differing by 10–100× per level. Speed is the structural advantage of the Atomic
Node.

---

## 8. Empirical Verification: N-Body Matrix — Mexico

The five-level taxonomy is verified with INEGI 2022–2023 data for the 32 federal
entities. Level 0 (Mexico City): 14.8% of national GDP. Level 1 (9 secondary
attractors): 41.0%. Level 2 (8 logistic-bypass nodes): 20.2%. Level 3 (11 shadow
nodes): 16.8% with the largest number of entities. Level E (3 exogenous
anomalies): 4.3%. The rank-size power-law fit gives b = −0.473, R² = 0.838,
p < 0.001 (re-derived in the audit: b = −0.4732, R² = 0.8377). A rank-size fit
over 32 ordered entities yields a high R² almost by construction, so this is
consistent with, but not by itself evidence of, preferential attachment; a
comparison against a lognormal alternative (Clauset et al., 2009) is pending.

The composite gradient of Tlaxcala is the central N-body result: the binary model
measured w_ij(Tlaxcala→Puebla) = 26.2k MXN; the N-body matrix reveals
w_ij(Tlaxcala→Mexico City, long-range) = 216.8k MXN. Total composite gradient:
243.0k MXN — the binary model underestimated Tlaxcala's satellization by 9.3×;
89.2% of extraction flows directly to Mexico City, bypassing the intermediary.
Trajectory vectorization for eight entities (1940–2022) reveals two natural
groups: Satellization (b > 0): Chiapas (+0.229), Oaxaca (+0.176), Guerrero
(+0.176), Veracruz (+0.181), Tlaxcala (+0.147), Puebla (+0.116); Convergence
(b < 0): Querétaro (−0.155, R²=0.782) and Nuevo León (−0.058, R²=0.935) — the
first documented leapfrog cases within the national system (Querétaro via
aerospace manufacturing, Nuevo León via independent export manufacturing).

---

## 9. Limitations

Original corpus limitations remain: data uncertainty (±20%) for pre-1820 historical
estimates, low R² for the Portugal case (oscillatory process), possible reverse
causality in the digital case, selection bias in case choice, and sensitivity to
trigger definition in gradual cases. The Triple-Resolution Model's Micro and Macro
modules are conceptual frameworks with partial operationalization; variables RQ,
RL, DI, DP, and MG have proposed measurement criteria not yet validated with
structured data series. The ASI is computable on HackerEarth 2026, but its
v30 "precision = 1.0" is withdrawn as tautological (§6.6); it requires validation
against an independent outcome. The Ck Coherence
Factor has a verified neurological mechanism (Friston 2010) but its
operationalization is untested.

**On the corpus:** this version retires the previously posted 502-case corpus,
which contained synthetic values, and replaces it with 721 cases reconstructed
from verifiable primary sources (R² ∈ [0,1]; 89% significant). The collapse layer
(Section 13) is correlational and, on the crypto side, based on small n; it is
framed as a strong hypothesis, not causal proof.

**Integral audit v32 and re-verification (added in r31).** (i) *Serial
autocorrelation:* Domain B fits have median Durbin-Watson 0.112 and median AR(1)
ρ 0.944, i.e. a median effective n of 2.2 (nominal 69); 290 of 446 cases are not
estimable (effective n < 3), and among the 156 estimable ones 33–112 remain
significant depending on the correction variant. (ii) *Pseudo-replication:* the
714 cases behind the friction finding are clustered in six domains; the
cluster-level test is not significant (§12). (iii) *Construct validity of Domain
B:* the hub is assigned by mean GDP, and 77 of 91 countries (85%) appear both as
hub and as satellite, so the role is a property of the pair, not a network
position. (iv) *Superlinear regime:* in the 18 raw collapse-layer series, AIC
prefers the power law in 13, an exponential in 4 (mean b = +1.54) and a linear
model in 1; the higher b, the worse the power law fits, so part of the b ≥ 1 band
(102 of 721 cases) may be misspecification. (v) *Reporting:* per-case p-values
were rounded to six decimals (557 of 721 read 0.0), and two R² definitions (log
and raw scale) were averaged together. (vi) *Composition:* the friction-free
pole (E1 + E3) is COVID-19 data; E1 models territorial spread, not species
invasion. (vii) *Reproducibility:* Domain B reproduces exactly from the committed
Maddison 2020 file; E1/E3 raw series and the HackerEarth data are not
distributed.

---

## 10. Falsifiability Criteria

RC1 — Scalar Velocity: falsified if a technology is systematically adopted faster
by firms than by individuals (RC1a), or if a technology emerges without individual
access that inverts the TC hierarchy (RC1b). RC2 — Immune Response: falsified if
hub adaptation toward the peripheral node is documented more frequently than
suppression. RC3 — Qualitative Inextractability: falsified if hubs systematically
neutralize node knowledge differentials. RC4 — Dual Minimum Threshold: falsified
if a leapfrog sustains itself with either dimension below minimum. RC5 — Expansion
Sequence: falsified if direct expropriation produces more stable states than silent
absorption. RC6 — Irreversibility: falsified if a Shadow Node reverses
satellization endogenously without an exogenous trigger. RC7 — ASI
Operationalization: falsified if users with ASI > 1 show performance comparable to
users with ASI < 0.5 in tasks requiring cognitive sovereignty (untested: the v30
"precision = 1.0" was tautological, §6.6). RC8 — Mutual-interdependence brake:
falsified if predator-prey or sovereign-state systems produce sustained b > 0.5
without exogenous perturbation.

*Numbering note (r31): these are the conceptual criteria of the framework. The
repository README keeps a separate empirical checklist with its own numbering
(e.g., its "RC3" is the abrupt-vs-gradual test, now marked untestable).*

**Collapse-axis criteria (new).** RC-Δ1 — Orthogonality: falsified if corr(b, Δ)
is significantly different from zero across paired cases (first test: crypto n=11,
ρ = +0.009, not refuted). RC-Δ2 — Friction governs collapse shape: falsified if
resolution friction does not predict Δ (first test: 2008 cohort n=6,
ρ = −1.000). RC-Δ3 — Hazard positivity: falsified if a system with hazard = 0 is
found.

---

## 11. Diagnostic Protocol

SNT is prescriptive as well as descriptive. Four steps to apply the model to any
real system. **Step 1 — Level Classification:** collect node production data;
verify whether the distribution follows a power law (log-log fit, R² > 0.7,
p < 0.05); classify in the five-level taxonomy. **Step 2 — Gradient Calculation:**
calculate w_ij for each hub extracting from the node; compute the composite
gradient if there are multiple hubs (the Tlaxcala case shows the long-range
gradient can be 8.3× larger than the direct one). **Step 3 — Event Horizon
Estimation:** fit the historical trajectory; if b > 0, estimate t_horizon; if
b < 0, identify the mechanism and verify its sustainability. **Step 4 — Orthogonal
Dimension Identification:** search for dimensions where the hub has not invested in
5–10 years, where the node has a measurable initial advantage, and which have
preferential-attachment potential; verify they do not require hub-controlled
infrastructure; then design the intervention (address the critical deficiency at
minimum, build capacity without triggering the immune response, execute the
leapfrog when the window is open).

---

## 12. Corpus of 721 Real Cases — Definitive Findings

The empirical corpus comprises 721 cases reconstructed entirely from verifiable
primary sources, replacing the previous 502-case corpus (retired after an audit
found ~188 synthetic b values and an impossible R² column). Distribution by domain
(friction, n, b̄): A Cities (medium, 4); B Country pairs, Maddison 2020 (high,
446, +0.092); C Regions US Census + INEGI (high, 24, +0.091); D Digital (low, 3,
−1.364); E1 Territorial spread, COVID-19 (none, 4, +2.891); E2 Predator-prey
(high, 2, +0.145); E3 Parasite-host, COVID-19 (none, 234, +0.912); F1–F3
Astronomical (medium/low, 4). Total 721, global b̄ = +0.366; integrity R² ∈ [0,1]
for all; 89% nominally significant (see §3.3 and §9 for the corrected figures).

**Finding 1 — Institutional friction is negatively associated with
satellization (central result, with inference caveats).** Spearman correlation
between the a-priori friction index and b (social/biological domains):

| Analysis | ρ | p | n |
|---|---:|---:|---:|
| Per case | −0.678 | 2.5×10⁻⁹⁷ | 714 |
| Per domain cluster (domain means) | −0.556 | 0.25 | 6 domains |
| Cluster bootstrap | −0.434 | 95% CI [−0.722, −0.006] | 6 domains |
| Without E3 (COVID-19) | −0.116 | 0.011 | 480 |
| Without E3 and B | −0.426 | 0.012 | 34 |

The negative sign survives every variant; the per-case p-value does not, because
it treats clustered and autocorrelated cases as independent. The result is a
consistent direction, not a precisely estimated effect.

**Finding 2 — Regime separation.** Friction-free domains (E1+E3)
produce b̄ ≈ +0.95; friction-laden economic domains (A+B+C) produce b̄ ≈ +0.09.
Mann-Whitney U = 103,538, p = 2.4×10⁻⁷⁴ (per case; subject to the same
clustering caveat). All 238 friction-free cases are COVID-19 spread data (E1
territorial spread, E3 per-country curves), so the contrast compares one
epidemic with economic series; it is suggestive, not a general law.

**Finding 3 — Abrupt vs gradual triggers: withdrawn (r31).** v30 reported a
ratio of 5.9× (U = 24,802, p = 1.91×10⁻⁵, n = 486) "stable across 57 → 114 →
721 cases". Recalculated on every trigger-labeled dataset: the ratio comes from
2 vs 2 historical cases (5.87×, p = 0.33); n = 486 matches no dataset; the
active 721-case corpus has no usable trigger variable; the non-citable 57-case
corpus gives 6.3× (p = 0.053); the collapse-layer cases (a different exponent)
give 0.47× (p = 0.10). The claim is withdrawn pending a corpus with
independently coded triggers (§5).

**Finding 4 — Political sovereignty as a brake: hypothesis (revised in r31).**
Sovereign country pairs (b̄ ≈ +0.09) and predator-prey systems (E2, b̄ = +0.145,
n = 2) have similar mean exponents, which v30 read as two mechanisms anchoring b
near zero because complete node extinction would destroy the hub. The reading
rests on Domain B, whose construct a discriminant test does not validate: (a)
the correlation of b with the initial GDP gap (ρ = −0.489, n = 446) falls inside
a synthetic null calibrated to the Maddison data (95% interval [−0.577, −0.242];
split-sample version ρ = −0.385, empirical p = 0.050, borderline); (b) with
bilateral trade from the Correlates of War (432 pairs), the node's export share
to its hub does not predict b (ρ = −0.043; within-region permutation p = 0.72;
partial R² = 0.0001), and the initial share goes with **lower** b (ρ = −0.185;
cluster-by-node p = 0.022), opposite to the coupling prediction. Domain B is
therefore supported neither as hub–node coupling nor as β-convergence, and the
sovereignty-as-brake statement is kept as a hypothesis. v30 closed this finding
with the contrast that, when resource transfer is direct and unmediated (a
herring shoal cannot negotiate with a school of mackerel; a Hot Jupiter does not
apply for regulatory approval), b exceeds 1 regardless of substrate. In the
corpus 94 of the 102 cases with b ≥ 1 are COVID-19 spread series (E1 + E3), and
the band may partly reflect misspecification (Finding 5), so r31 states it as a
conjecture.

**Finding 5 — Modeling regimes.** The power law is the best description where
friction is low (epidemic spread, E1 and E3); under high friction (countries)
exponential and linear models compete. In the 18 raw collapse-layer series, AIC
prefers the power law in 13, the exponential in 4 (mean b = +1.54) and the
linear model in 1: the higher b, the worse the power law fits. The exponent b is
a descriptive, cross-domain comparable metric — not a claim that the power law
is the only generative model in all domains — and the superlinear band b ≥ 1
should be re-tested against alternative models.

---

## 13. Coupled Orbital Collapse Layer (ACO-A)

The Orbital Collapse Architecture ceases to be a separate module and is
reformulated as a **universal, transversal layer** of SNT: collapse is an
**orthogonal axis** that can activate in any system, in any domain, at any point of
its trajectory. A single principle (least friction) generates distinct collapse
modes depending on boundary conditions, demonstrated with real data in five
domains.

**13.1 Two orthogonal axes (b ⊥ Δ).** Each system is a pair of independent
coordinates. Axis 1 — Satellization: R(t) = a·t^b, how dominance evolves while the
coupled relationship runs. Axis 2 — Collapse: A(τ) = c·τ^Δ, with τ = time since
functional extinction; Δ measures the speed/shape of absorption once the hub
collapses. Collapse does not wait for the satellization cycle to end (different
clock, τ ≠ t). Falsifiable prediction: corr(b, Δ) ≈ 0. First test (paired crypto,
n = 11): Spearman ρ(b_rise, Δ_fall) = +0.009 (p = 0.98) — consistent with
orthogonality.

**13.2 Hazard layer h(τ).** "No system is eternal" = h(τ) > 0 for every system
(refutable if a system with hazard = 0 is found). First estimate (crypto cohort,
n = 41; functional extinction = price < 1% of all-time high): 15 extinctions across
the whole age range (0.27–8.6 years), no death-free era; Kaplan-Meier declining;
hazard positive and rising with age — consistent with h(τ) > 0. Caveats:
survivorship bias (true hazard higher), age/calendar confound, limited n.

**13.3 Taxonomy of collapse modes (three factors).** Governed by friction ×
trigger × (floor/ceiling on magnitude): Regulated Orbital Decay (high friction →
smooth power law or exponential, non-accelerating; 2008 cohort R²=0.85–0.99,
Rome/USSR, solar flare R²=0.975, TDE R²=0.84); Cracquelure Decay (friction≈0 +
gradual → erratic fragmentation; EOS R²=0.10–0.70); Floor-Arrested (friction≈0 +
abrupt + floor → power law to a residual floor; FTX R²=0.875); Catastrophic Cliff
(friction≈0 + abrupt + no floor → super-exponential; LUNA, 5.6 orders of magnitude
in 11 days); Logistic Sweep (bounded magnitude → S-curve; Delta→Omicron k=0.22/d).

**13.4 Principle of Least Friction (unifier).** Every collapse follows the
trajectory that minimizes integrated friction (variational family: Fermat, least
action, minimum dissipation) — a gradient flow over a stability landscape.
Falsifiable version: the realized collapse has lower integrated friction than
counterfactual trajectories (WaMu via the pre-arranged FDIC channel = least
friction → 21 h; Lehman without it → slow fragmentation, 30,681 h; range ~1,460×,
monotonic with the degree of regulatory intervention).

**13.5 Results with real data (four roadmap items).** (1) Friction operationalized:
within the 2008 financial cohort (n=6), resolution-channel friction (ordinal 1–6)
vs Δ: Spearman ρ = −1.000, p < 0.001 — more friction, more frontal and orderly
absorption. (2) Orthogonality b ⊥ Δ: crypto n=11, ρ = +0.009 (§13.1). (3) Unbounded
biology: the Omicron wave in absolute counts (South Africa, JHU) decays smoothly
exponential (R² = 0.96, e-fold ~22 d), NOT a cliff — epidemiological feedback is
intrinsic friction. (4) Hazard h(τ) > 0 (§13.2). Connection to the central finding:
friction is negatively associated with b (ρ = −0.68 per case; direction robust,
significance not — §12) and, in the 2008 cohort (n = 6), with the shape of Δ — a
candidate lever for both axes, to be tested on larger cohorts.

---

## 14. Dialogue with the Literature

**Barabási & Albert (1999):** SNT extends preferential attachment by quantifying
satellization velocity through the exponent b and proposing a five-level functional
taxonomy. INEGI data are consistent with the predicted rank-size distribution
(b = −0.473, R² = 0.838), pending a lognormal comparison (§8). **Watts & Strogatz (1998):** SNT adds the directional
dimension of resource flow to the clustering coefficient — two nodes may be close
in connection distance but at radically different hierarchical levels. **Holland
(1995):** SNT specifies satellization as a recurring emergent dynamic with a
mathematically predictable trajectory within Complex Adaptive Systems. **Friston
(2010):** SNT extends the Free Energy Principle beyond the individual brain to
social systems; the hub immune response and the Coherence Factor Ck are
manifestations of the same principle at different scales. **Brezis & Krugman
(1993):** SNT extends technological leapfrogging to three scales and formalizes the
failure conditions the original model did not develop. **Catastrophe and resilience
theory (Thom 1972; Waddington 1957; Holling 1973; Lenton et al. 2008):** the
collapse layer's stability-landscape language connects SNT to fold catastrophes,
the epigenetic landscape, ecological "ball-in-cup" resilience, and climate tipping
points.

---

## 15. Conclusions

**15.1 What SNT demonstrates.** The satellization cycle — from dependent child node
to peer to hub of new children — operates across all domains. The five-level
taxonomy is verifiable with INEGI data and follows a power law; the binary model
underestimated Tlaxcala's satellization by 9.3×; the first documented leapfrog
cases within the Mexican national system are verified (Querétaro b = −0.155, Nuevo
León b = −0.058); the ASI is computable from behavior on 4,774 users (its
validation remains open, §6.6). With the real 721-case corpus, **institutional
friction is negatively associated with b in every analysis variant** (ρ = −0.68
per case; not significant at the domain-cluster level, ρ = −0.56, p = 0.25) and,
in the 2008 cohort, with the shape of collapse (Δ). The golden-ratio hypothesis
(H-φ) was tested and refuted across four rounds, and the abrupt-vs-gradual
ordering reported in v30 is withdrawn (§5); both are excluded from the claims.

**15.2 What SNT does not demonstrate.** That leapfrog is always possible for any
node. The model formalizes viability conditions and failure mechanisms but does not
guarantee success. The Micro and Macro modules require independent empirical
validation; the ASI requires validation against an outcome independent of its
own threshold; the collapse layer is correlational and requires larger cohorts
and cross-domain tests. SNT does not demonstrate that Domain B measures hub–node
coupling: a discriminant test with a calibrated null and bilateral trade data
does not support that reading (§12, Finding 4).

**15.3 Future research lines.** Validation of the Micro Module with longitudinal
individual trajectory data; ASI operationalization with other platforms; extension
of the N-body matrix to other national systems; cross-domain orthogonality test
for b ⊥ Δ; larger survivorship-unbiased cohorts for h(τ); pre-registration before
claiming causality. Added in r31: Newey-West/GLS estimation on raw residuals to
pin the autocorrelation-corrected significance of Domain B; recovery of the raw
COVID-19 series to correct E1/E3; re-testing the superlinear band against
exponential and lognormal models; a satellization corpus with independently
coded triggers; and rebuilding Domain B with a hub that emerges from the trade
network instead of being assigned by GDP.

**15.4 The major implication.** Not theoretical but practical. If satellization
follows a predictable algorithm with an identifiable failure taxonomy, it is
intervene-able. For Tlaxcala: 89.2% of the gradient comes not from Puebla but from
Mexico City — any strategy targeting only the Tlaxcala–Puebla relationship solves
10.8% of the problem. For the Atomic Node: the cognitive leapfrog — orchestrating
AI agents rather than executing tasks linearly — is the first dimension in recent
history where the accumulated advantage of dominant nodes does not apply directly,
and the HackerEarth 2026 evidence suggests that window is open now.

> *"The satellization algorithm is predictable. The leapfrog failure taxonomy is
> known. What follows is a decision that no model can make for the node."*

---

## References

Avey, J.B., Reichard, R.J., Luthans, F. & Mhatre, K.H. (2011). Meta-analysis of the
impact of positive psychological capital on employee attitudes, behaviors, and
performance. *Human Resource Development Quarterly*, 22(2), 127–152.

Barabási, A.L. & Albert, R. (1999). Emergence of scaling in random networks.
*Science*, 286(5439), 509–512.

Barbieri, K. & Keshk, O.M.G. (2016). *Correlates of War Project Trade Data Set
Codebook, Version 4.0.* Online: http://correlatesofwar.org.

Barbieri, K., Keshk, O.M.G. & Pollins, B. (2009). Trading data: Evaluating our
assumptions and coding rules. *Conflict Management and Peace Science*, 26(5),
471–491.

Bolt, J. & van Zanden, J.L. (2020). Maddison style estimates of the evolution of
the world economy. A new 2020 update. Maddison Project Working Paper WP-15,
University of Groningen. [Maddison Project Database 2020; the edition that
reproduces Domain B.]

Brezis, E.S. & Krugman, P.R. (1993). Leapfrogging in international competition.
*American Economic Review*, 83(5), 1211–1219.

Clauset, A., Shalizi, C.R. & Newman, M.E.J. (2009). Power-law distributions in
empirical data. *SIAM Review*, 51(4), 661–703.

Dong, E., Du, H. & Gardner, L. (2020). An interactive web-based dashboard to track
COVID-19 in real time. *The Lancet Infectious Diseases*, 20(5), 533–534. [JHU CSSE]

Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature
Reviews Neuroscience*, 11(2), 127–138.

Holland, J.H. (1995). *Hidden Order: How Adaptation Builds Complexity.*
Addison-Wesley.

Holling, C.S. (1973). Resilience and stability of ecological systems. *Annual
Review of Ecology and Systematics*, 4, 1–23.

INEGI (2022). PIB per cápita por entidad federativa. Sistema de Cuentas Nacionales
de México.

Lenton, T.M. et al. (2008). Tipping elements in the Earth's climate system. *PNAS*,
105(6), 1786–1793.

Thom, R. (1972). *Stabilité structurelle et morphogénèse.* [fold catastrophe]

Waddington, C.H. (1957). *The Strategy of the Genes.* [epigenetic landscape]

Watts, D.J. & Strogatz, S.H. (1998). Collective dynamics of small-world networks.
*Nature*, 393(6684), 440–442.

Zainos Corona, E. (2026). Shadow Node Theory — Replication Package v2.5.0
(721-case real corpus + Coupled Collapse layer ACO-A). Zenodo.
https://doi.org/10.5281/zenodo.19446521. Current repository (release v2.5.2,
integral audit v32, discriminant test of Domain B):
https://github.com/Inzainos/The-shadow-Node-Theory

Collapse-layer data sources: Yahoo Finance (LUNA, FTT, EOS); NOAA SWPC GOES (solar
X-ray); NASA IRSA / ZTF (TDE AT2019qiz); CoV-Spectrum / LAPIS (SARS-CoV-2
variants); SEC, FDIC, Federal Reserve, SIGTARP (2008 cohort).

---

*— Fractal Core Research — Pre-print, manuscript revision r31 (2026-09-27), repository release v2.5.2 — Tlaxcala, Mexico — 2026 —*
