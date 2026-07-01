# Response to Reviewers — PCSY-D-26-00059

**Manuscript:** Scale-Invariant Satellization: A Power-Law Framework for Node
Dominance (formerly "…verified across 502 cases in 11 domains")
**Journal:** PLOS Complex Systems · **Decision:** Major revision
**Academic Editor:** Haroldo V. Ribeiro · **EIC:** Hocine Cherifi

Dear Dr. Ribeiro and the reviewers,

We thank the editor and both reviewers for a careful, constructive review. The
central criticisms — over-broad universality claims, weak statistical evidence
(the 31.1% significance figure, no model comparison, no uncertainty
quantification), an under-defined "friction" concept, and an over-stated
behavioral application — were well taken. We have **substantially revised the
manuscript along exactly these axes**, and in doing so we discovered and corrected
a deeper problem in the original submission.

**Most important change.** During revision we audited the original 502-case corpus
and found that a portion of it had been parametrically generated (≈188 b values
from a normal draw, and an out-of-range R² column). **We have discarded that
corpus entirely** and rebuilt the empirical base as **721 cases reconstructed
exclusively from verifiable primary sources**, each reproducible from the
underlying series by published scripts, with R² ∈ [0,1] for every case. This
directly resolves Reviewer #1's data-transparency and significance concerns: on
the real corpus, **644/721 (89.3%) of cases are statistically significant**, not
31.1%. We also narrowed the scope and moderated the claims throughout, as both
reviewers requested. A point-by-point response follows; manuscript sections are
cited by their numbers in the revised version.

---

## Editor

> "…an original and potentially valuable idea that merits further consideration if
> the scope, methodology, evidence, and claims are substantially revised."

- **Scope** narrowed: the paper now claims only that *b is a comparable
  cross-domain descriptor whose value is structured by friction* — explicitly
  **not** that all systems are "really" power laws (§1 scope note, §3.4, §4.1).
- **Methodology**: per-case model comparison (AICc vs linear/exponential/
  logarithmic), bootstrap/analytic uncertainty on b, and residual-autocorrelation
  diagnostics are now part of Methods (§2.1, §2.4) and Results (§3.4).
- **Evidence**: the synthetic corpus is replaced by 721 reproducible real cases.
- **Claims**: universality language removed; the astrophysical domain is reported
  separately because its "friction" is physical, not institutional (§4.4).

---

## Reviewer #1

**1.1 — Strong universality claims without methodological support; comparability
of "productive output" across heterogeneous domains; case selection.**
We agree and have retreated from the universality framing. The revised paper makes
a deliberately **narrower, falsifiable claim** (§1, §4.1): b is a *descriptive,
cross-domain–comparable* metric of the direction and speed of satellization, and
its variation is organized by an a-priori friction ordering. On comparability, we
now state explicitly what is and is not being equated: in every case the dependent
variable is the *same dimensionless construction* R(t)=metric_hub/metric_node and
the estimand is the log-log slope b; we do **not** claim the underlying substrates
are physically identical (§2.1, §4.1). Case-selection criteria are stated
explicitly (two coupled entities in critical proximity, an identifiable trigger,
≥4 temporal points; no exclusion by outcome direction, to avoid confirmation
bias) (§2.2).

**1.2 — Statistical evidence not convincing: 31.1% significance; R²>0.7
insufficient; need model comparison, robustness, uncertainty, autocorrelation.**
This was the most important methodological point and we have addressed every part.
(i) The 31.1% figure was an artifact of the synthetic corpus; on the real
721-case corpus **89.3% are significant** at p<0.05 (§3.1). (ii) We no longer use
"R²>0.7" as a universality criterion — that criterion is gone. (iii) We now perform
**formal per-case model comparison** by AICc against linear, exponential, and
logarithmic alternatives (§2.4 H3, §3.4); the result is reported honestly — the
power law is the best model in only ~8% of high-friction country cases and in the
*majority* of zero-friction epidemic cases — and is used as *evidence for the
friction thesis*, not against it. (iv) For every case we now report the **standard
error and 95% CI of b** and the **Durbin–Watson statistic** for residual
autocorrelation (§2.1). (v) We frame b as a descriptor interpreted *alongside*
model-comparison context, not as proof of a generative power law (§3.4, §4.1).

**1.3 — "Institutional friction" insufficiently defined; risks being post hoc;
used differently across domains; not measured independently of the outcome.**
We have made friction an **explicit, pre-registered, ordinal variable assigned
before any exponent was examined** (§2.3): a 0–3 scale fixed a priori from the
documented *mechanism* of resistance (sovereignty/borders/monetary policy for
economies; mutual ecological dependence for predator–prey; absence of any brake
for naive-population epidemics). Because the index is fixed from mechanism and
before estimation, it cannot be post-hoc with respect to b. On the cross-domain
heterogeneity the reviewer rightly flags: we now **separate the physical-friction
(astrophysical) domains from the central social/biological correlation** and
report them apart (§4.4(iii)), so the headline result ρ=−0.68 is computed only
where "friction" has a consistent institutional/interdependence meaning (n=714).

**1.4 — N-body matrix and ASI underdeveloped; ASI proprietary; precision=1.0
needs an independent test set and a transparent target definition.**
We have **moderated the ASI claim substantially**. The precision=1.0 statement is
removed. The ASI is now evaluated as an out-of-sample predictor with a **70/30
stratified split and held-out ROC-AUC = 0.715** (train 0.719 / test 0.697,
evidencing no overfitting) (§2.5, §3.6); the target class (first-window attrition)
and the features (first-session event-type breadth + entropy) are defined
explicitly. We present it as an **existence proof** that the construct carries
predictive signal, not a state-of-the-art churn model (§4.3). The Mexico N-body
matrix is **out of scope for this paper** and has been removed from the main
claims to keep the focus on the friction–satellization result, per the reviewer's
and editor's request to narrow scope (it remains in the broader project
repository).

**1.5 — Overall: narrow scope, define variables, justify comparability,
transparent case-level data, model comparison, moderate claims.**
All six are now in place: narrowed scope (§1, §4.1); a-priori friction definition
(§2.3); comparability statement (§2.1, §4.1); fully public, per-case reproducible
data (Data Availability); formal AICc model comparison (§3.4); and universality
claims removed throughout.

---

## Reviewer #2

**2.1 — Abstract confusing; define satellization; less numerical, more qualitative;
title more engaging.**
The abstract is rewritten to (a) **define satellization in plain language first**,
(b) give the motivating question, and (c) lead with the *qualitative* finding
(friction governs the rate), with the key numbers kept brief and the rest moved to
the main text. The title is revised toward accessibility.

**2.2 — Introduction more accessible/engaging; more background and intuition.**
The introduction now opens with concrete, cross-disciplinary motivating examples
(converging economies, invasive species, platform users) before any formalism, and
states the scope limits in plain terms (§1).

**2.3 — Equation notation (a·t^b is not appropriate scientific notation).**
All equations are set in standard math notation in the typeset manuscript
(R(t)=a\,t^{b}; \log R(t)=\log a + b\log t), rather than inline ASCII.

**2.4 — State whether the b classification is the authors' contribution or from
the literature.**
We now state this explicitly (§1): the **classification of b into regimes and the
identification of b=1 ("Roche Radius") as a critical threshold are the original
conceptual contributions** of this work, whereas the log-log estimation procedure
is standard. No prior-literature attribution is claimed for the classification.

**2.5 — Data Sources as a table.**
The data sources are now presented as a **structured table** (Table 1: domain,
description, n, primary source, friction level), replacing the narrative list.

**2.6 — Statistical Tests section too technical; explain purpose of each test.**
Each test now carries a one-line plain-language rationale (§2.4): H1 (does friction
co-vary with b? — Spearman, robust to non-normality and monotonic but non-linear
relations); H2 (do zero-friction and high-friction regimes separate? —
Mann–Whitney, a distribution-free two-sample test); H3 (is the power law actually
the best functional form per case? — AICc model comparison).

**2.7 — Corpus Overview as a table.**
The per-domain overview is presented as **Table 2** (domain, friction, n, mean b,
mean R²), and the corpus-level summary statistics are tabulated rather than only
narrated (§3.1–3.2).

**2.8 — Figures: low resolution, appear copied from a PDF.**
All figures are **regenerated from source at publication resolution** (vector SVG +
300-dpi PNG) by the published plotting scripts, using an Okabe–Ito colorblind-safe
palette; none are screen-captured. Figure files are provided as separate
high-resolution items at resubmission.

**2.9 — Writing style lacks narrative flow; conclusion is bullet-like.**
We have revised for connected prose throughout and **rewritten the Conclusion as a
synthesized narrative** (§5) rather than a list, tying the friction result, the
model-comparison caveat, and the behavioral application into a single argument.

---

## Journal requirements

1. **Data availability / minimal data set:** all primary series, extraction and
   analysis scripts, and per-case outputs are public
   (github.com/Inzainos/The-shadow-Node-Theory, `reconstruction_real/`); the
   consolidated corpus and master figures will additionally be deposited with the
   Zenodo record (DOI 10.5281/zenodo.19446521) and cited as Supporting Information.
2. **Source file** provided as .docx at revision.
3. **Title** in the manuscript and submission form are matched.
4. **Author Summary** (150–200 words) included between Abstract and Introduction.
5. **Supporting Information** figure/data files uploaded as separate items.

We believe the revision meets the reviewers' substantive concerns — most
importantly by replacing the synthetic corpus with fully reproducible real data,
adding formal model comparison and uncertainty quantification, pre-registering the
friction index, moderating the universality and ASI claims, and improving the
presentation (tables, figures, narrative). We thank the reviewers again for
feedback that materially strengthened the paper.

Sincerely,
Elán Zainos Corona — Fractal Core Research, Tlaxcala, Mexico
