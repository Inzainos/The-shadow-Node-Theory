# Shadow Node Theory v2.5.0

**Elan Zainos Corona** | Fractal Core Research, Tlaxcala, Mexico

ORCID: [0009-0009-9125-253X](https://orcid.org/0009-0009-9125-253X)

[![SSRN](https://img.shields.io/badge/SSRN-6418778-blue)](https://ssrn.com/abstract=6418778)
[![Zenodo](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.19446521-blue)](https://doi.org/10.5281/zenodo.19446521)
[![GitHub](https://img.shields.io/badge/GitHub-Inzainos-black)](https://github.com/Inzainos/The-shadow-Node-Theory)

---

> **WARNING: PREVIOUS VERSION OBSOLETE**
> The 502-case corpus (v2.3.1 and earlier) contained synthetically generated
> values and an r2 column with impossible values (down to -7.332).
> Those files are preserved in `archive/` as historical record but
> **must not be cited in academic publications**.
> The active version is v2.5.0 (721-case corpus + coupled collapse layer).

---

> **NEW in v2.5.0 -- Coupled Orbital Collapse layer (ACO-A)**
> Collapse is reformulated as a **universal, transversal axis** of SNT, with
> evidence in **5 domains** (finance, history, crypto, biology, astronomy) from
> real data. See [Orbital Collapse Architecture (Coupled, v2.5.0)](#orbital-collapse-architecture-coupled-v250)
> below and the full theory in `papers/SNT_Colapso_Acoplado.md`.

---

## What Is Shadow Node Theory?

When two coupled entities interact over time -- a dominant **hub** and a
peripheral **node** -- the dominance ratio evolves in a regular way.
SNT characterizes that evolution through scaling exponents estimated by fitting
power laws on logarithmic axes. Two orthogonal axes describe a system:

- **Satellization (b):** `R(t) = metric_hub(t) / metric_node(t) = a*t^b` --
  how dominance evolves *while the coupled relationship runs*.
- **Collapse (Delta):** `A(tau) = c*tau^Delta` -- how the hub's mass is
  *absorbed once it undergoes functional extinction* (the v2.5.0 layer).

The sign and magnitude of **b** summarize the direction and speed of
**satellization** -- the process by which a peripheral entity loses or gains
relative standing against a dominant core.

```
b < 0    --> convergence (node gains ground)
b ~ 0    --> dynamic equilibrium
0 < b < 1 --> sublinear satellization (gradual)
b >= 1    --> superlinear satellization -- Roche Radius
```

---

## Corpus v2.4.0 -- 721 cases, 100% real data

| Domain | Friction | Cases | Sig. | b mean | Source |
|--------|----------|-------|------|--------|--------|
| A -- Cities | medium | 4 | 0% | +0.08 | UN Demographic Yearbook |
| B -- Countries | high | 446 | 84% | +0.09 | Maddison Project 2020 |
| C -- Regions | high | 24 | 100% | +0.09 | INEGI + US Census |
| D -- Digital | low | 3 | 100% | -1.36 | HackerEarth 2026 |
| E1 -- Invasion | none | 4 | 100% | +2.89 | OWID COVID (spatial) |
| E2 -- Predator-prey | high | 2 | 50% | +0.15 | MacLulich/Elton |
| E3 -- Parasite-host | none | 234 | 100% | +0.91 | JHU COVID-19 |
| F1 -- Planetary | medium | 2 | 100% | -1.81 | Open Exoplanet Cat. |
| F2 -- Stellar | medium | 1 | 100% | +1.27 | Open Exoplanet Cat. |
| F3 -- Multiplanet | low | 1 | 100% | +1.26 | Open Exoplanet Cat. |
| **TOTAL** | | **721** | **89%** | **+0.37** | |

**Integrity verified:** R2 in [0,1] for all cases. Zero corrupt values. All reproducible from public scripts.

---

## Central Finding

Institutional friction predicts the satellization exponent:

**Spearman rho = -0.68, p = 2.5x10^-97** (social/biological domains, n=714)

Systems without friction (E1, E3): b mean = +0.95
Systems with friction (A, B, C): b mean = +0.09
**Mann-Whitney p = 2.4x10^-74**

---

## Three Core Statistical Findings (v29)

| Finding | Result | Test |
|---------|--------|------|
| Abrupt triggers faster than gradual | Ratio 5.9x in historical corpus | Mann-Whitney U=24,802, p=1.91x10^-5, n=486 |
| Institutional friction is dominant predictor of b | Friction-free: b~+0.95 / High friction: b~+0.09 | Spearman rho=-0.68, p=2.5x10^-97, n=714 |
| Sovereignty = interdependence as brake | 230 country pairs vs 4 predator-prey | Mann-Whitney p=2.4x10^-74 |

---

## Publication Status

| Target | Status | Notes |
|--------|--------|-------|
| **SSRN** (abstract 6418778) | PUBLISHED | Active preprint, updated to v30 (721-case corpus) |
| **Zenodo** (DOI 10.5281/zenodo.19446521) | PUBLISHED | Updated to v30 (721-case corpus) |
| **PLOS Complex Systems** (PCSY-D-26-00059) | MAJOR REVISION | Deadline 10 Aug 2026; v29 draft ready |
| **J. Complex Networks** (COMNET-2026-214) | REJECTED | No external review |
| **MIT GCFP Conference** | PREPARING SUBMISSION | 13th Annual Conf, Oct 29-30 2026; deadline 17 Jul 2026; paper + abstract ready (`papers/mit_gcfp_2026_*`) |
| J. Theoretical Biology | NOT RELEASED | Requires v30 update |
| Astrophysical Journal | NOT RELEASED | Requires v30 update |
| Investigacion Economica | NOT RELEASED | Requires v30 update |

---

## N-Body Matrix Correction -- Mexican National System

Standard binary models (Tlaxcala vs Puebla) underestimate Tlaxcala's satellization
gradient by 9.3x because 89.2% of extraction flows toward CDMX, not Puebla.
The N-body correction (32 federal entities, INEGI 2022) reveals a power-law
distribution of satellization weights (b=-0.473, R2=0.838, p<0.001) consistent
with preferential attachment predictions. Queretaro (b=-0.155) and Nuevo Leon
(b=-0.058) document the first confirmed leapfrog cases within the national
system.

---

## Módulo XVI -- Arquitectura de Colapso Orbital (ACO)

ACO extends SNT to cases where a hub undergoes **functional extinction** and its
resources are **absorbed by an identifiable node**. Without both elements, the
case is classical SNT satellization, not ACO.

| Domain | Cases | b mean | Sig. | Notes |
|--------|-------|--------|------|-------|
| F -- Financial | 6 | +0.13 | 6/6 | 2008 crisis: Lehman, Bear Stearns, WaMu, Wachovia, Merrill, Chrysler |
| T -- Technological | 4 | +1.09 | 4/4 | Nokia, Compaq, Sun, MySpace |
| H -- Historical | 4 | +0.46 | 3/4 | USSR, Rome, Aztec Empire, Carthage |
| I -- Industrial | 4 | +0.96 | 4/4 | Pan Am, Polaroid, Kodak, Blockbuster |
| **TOTAL** | **18** | **+0.60** | **17/18** | 14 verified, 4 estimated (*) |

Reproduced via `reconstruction_real/code/build_aco_v29.py`.

---

## Orbital Collapse Architecture (Coupled, v2.5.0)

v2.5.0 reformulates collapse as a **universal, transversal axis** of SNT. A
system has two orthogonal coordinates **(b, Delta)**: satellization (b) and the
collapse/absorption exponent (Delta), fit on its own clock tau from functional
extinction. A third layer, the hazard **h(tau) > 0**, states the falsifiable
"no system is eternal".

**The collapse mode is governed by friction x trigger x (floor/ceiling):**

| Mode | Condition | Shape | Witness (real data) |
|------|-----------|-------|---------------------|
| **Regulated Orbital Decay** | high friction (physical or institutional) | smooth power law | 2008 cohort (R2 0.85-0.99); Rome/USSR; **astro** |
| **Cracquelure Decay** | friction~0 + gradual | erratic fragmentation | EOS (R2 0.10-0.70) |
| **Floor-Arrested** | friction~0 + abrupt + floor | power law to a residual floor | FTX/FTT (PL R2 0.875) |
| **Catastrophic Cliff** | friction~0 + abrupt + no floor | super-exponential, accelerating | LUNA (5.6 OOM / 11 days) |
| **Logistic Sweep** | bounded magnitude (frequency) | S-curve | Delta->Omicron (k=0.22/day) |

**Five-domain evidence (real data).** Collapse demonstrated in finance, history,
crypto, biology and astronomy. Highlights: solar flare X-ray decay (NOAA GOES,
power law R2=0.975); tidal disruption event AT2019qiz (NASA/ZTF, ~t^-5/3);
Delta->Omicron sweep (CoV-Spectrum). Full table:
`reconstruction_real/data/collapse_multidomain_v29.csv`.

**Principle of Least Friction (unifying).** Collapse follows the path that
minimizes integrated friction -- gradient flow on a stability landscape. The
friction field's geometry (x trigger x floor) decides which mode emerges. This
extends the central SNT finding: friction governs **b** (the satellization
speed) *and* the **shape of Delta** (the collapse mode).

Theory: `papers/SNT_Colapso_Acoplado.md`. Figures (stability landscapes / "valles"
+ fold catastrophe): `figures/fig_paisajes_colapso.*`,
`figures/fig_catastrofe_cuspide.*`. *(Draft -- correlational, see caveats.)*

---

## Atomic Sovereignty Index (ASI)

ASI = delta_H x alpha / F

Where delta_H = Shannon entropy of behavioral sequence, alpha = autonomy ratio
(self-directed vs prompted actions), F = friction index. Applied to 4,774
HackerEarth users (409,287 events), ASI achieves held-out ROC-AUC = 0.715
using exclusively first-session features. The 5-Event Wall is the activation
threshold. The dominant retention predictor is AI agent adoption -- interpreted
as cognitive leapfrog.

---

## Repository Structure

```
The-shadow-Node-Theory/
|
|-- README.md                          <-- this file (v2.5.0)
|-- requirements.txt                   <-- Python dependencies
|-- sources.md                         <-- Data provenance
|-- CITATION.cff                       <-- Citation metadata
|
|-- reconstruction_real/               <-- REAL CORPUS v2.4.0
|   |-- README.md                      <-- Methodology and sources
|   |-- data/
|   |   |-- snt_corpus_REAL_v5.csv     <-- 721 consolidated cases
|   |   |-- MASTER_cifras_v5.json      <-- All paper figures
|   |   |-- MASTER_resumen_v5.csv      <-- Summary by domain
|   |   |-- by_domain/                 <-- Individual CSVs per domain
|   |   |-- dominio_B_real.csv         <-- Maddison 446 country pairs
|   |   |-- DOMINIO_B_METODOLOGIA.md   <-- Domain B methodology
|   |   +-- phi_test_corpus_real_v4.csv
|   |-- code/
|   |   |-- expand_dominio_B.py        <-- Reproduces 446 cases (Maddison)
|   |   |-- build_dominio_B.py
|   |   |-- generate_figures_v29.py    <-- v29 PLOS-compliant figures (SVG+PNG)
|   |   |-- build_aco_v29.py           <-- ACO 18 cases, 4 domains (v2.4.0)
|   |   |-- collapse_multidomain.py    <-- Collapse repro manifest + fit funcs (v2.5.0)
|   |   +-- make_collapse_landscapes.py <-- Stability-landscape figures (v2.5.0)
|   |-- data/
|   |   +-- collapse_multidomain_v29.csv <-- 5-domain collapse table (v2.5.0)
|   +-- snt_phi_hypothesis.md          <-- H-phi REFUTED (4 rounds + placebo)
|
|-- hypotheses/
|   +-- snt_phi_hypothesis.md          <-- H-phi REFUTED (4 rounds + placebo)
|
|-- papers/                            <-- Academic submissions
|   |-- marco_teorico_v30.md           <-- COMPLETE framework v30 (full v27 body restored + corpus v30 + collapse layer + phi r4)
|   |-- marco_teorico_v30.pdf          <-- COMPLETE framework v30 (76 pp)
|   |-- marco_teorico_v30_EN.md        <-- COMPLETE framework v30 (English, full translation)
|   |-- marco_teorico_v30_EN.pdf       <-- COMPLETE framework v30 (English, 65 pp)
|   |-- phi_retest.py                  <-- H-phi re-test on current corpus
|   |-- phi_placebo.py                 <-- H-phi placebo control (band-coverage null)
|   |-- SNT_Colapso_Acoplado.md        <-- Coupled Collapse theory (v2.5.0)
|   |-- mit_gcfp_2026_paper.pdf        <-- MIT GCFP paper (friction regularizes collapse; 2008 + 5 domains)
|   |-- mit_gcfp_2026_paper.md         <-- MIT GCFP paper (source)
|   |-- mit_gcfp_2026_abstract.pdf     <-- MIT GCFP abstract
|   |-- mit_gcfp_2026_abstract.md      <-- MIT GCFP abstract (source)
|   |-- SNT_Project_Report_v29.pdf     <-- Handover document (v29)
|   |-- SNT_Genomic_Topologic_Analyzer_v3.pdf <-- Genomic agent docs
|   |-- snt_plos_721cases_v29_DRAFT.docx <-- PLOS revision draft (721 cases, v29)
|   |-- snt_oxford_submission.docx     <-- REJECTED (COMNET)
|   |-- snt_plos_submission.docx       <-- v28 OBSOLETE (502 cases)
|   |-- snt_plos_submission.pdf        <-- v28 OBSOLETE (502 cases)
|   |-- snt_paper_plos_complex_systems.docx <-- v28 OBSOLETE (502 cases)
|   |-- marco_teorico_v28.pdf          <-- Unified framework (ES) v28
|   |-- snt_ssrn_v30.md                <-- SSRN preprint v30 (721 real cases + collapse layer ACO-A) [CURRENT]
|   |-- snt_ssrn_v30.pdf               <-- SSRN preprint v30 (17 pp)
|   |-- snt_ssrn_v30.docx              <-- SSRN preprint v30 (Word)
|   |-- shadow_node_theory_SSRN_v10.docx <-- HISTORICAL preprint (SNT v2.0, 502-case era)
|   |-- snt_paper_theoretical_biology.docx
|   |-- snt_paper_astrophysical.docx
|   |-- snt_paper_investigacion_economica.docx
|   |-- snt_paper_regional_economics_en.pdf
|   |-- snt_english_v23.docx           <-- English translation v2.3
|   |-- abstracts_marco_teorico.docx   <-- Abstracts & framework
|   +-- cover_letter_comnet.txt
|
|-- code/                              <-- Analysis scripts (v28 -- historical)
|   |-- snt_utils.py                   <-- Shared utilities (power-law fitting)
|   |-- snt_corpus_502.py              <-- WARNING: v28 OBSOLETE
|   |-- snt_corpus_biological.py       <-- Biological domains (E1-E3)
|   |-- snt_corpus_astronomical.py     <-- Astronomical domains (F1-F4)
|   |-- hackerearth_validation_final.py <-- ASI / ROC-AUC validation
|   |-- generate_publication_figures.py <-- TIFF 300dpi figures
|   |-- snt_v2_vectorizacion.py        <-- Trajectory vectorization
|   |-- matriz_mexico_ncuerpos.py      <-- N-body matrix Mexico (32 states)
|   |-- snt_corpus_aco.py             <-- ACO 4 cases (DEPRECATED, see build_aco_v29.py)
|   +-- snt_corpus_aco_expanded.py    <-- ACO 18 cases (DEPRECATED, see build_aco_v29.py)
|
|-- data/                              <-- Data files (v28 -- historical)
|   |-- snt_asi_scores.csv             <-- ASI scores HackerEarth
|   |-- matriz_mexico_32.csv           <-- 32 states INEGI
|   |-- snt_v2_vectores.csv            <-- Trajectory vectors 8 states
|   |-- phi_validation_crypto.csv      <-- H-phi validation round 1
|   +-- phi_validation_bio_primary.csv <-- H-phi validation round 2
|
|-- genomic_agent/                     <-- SNT Genomic Topologic Analyzer v2
|   |-- agent_core/                    <-- Analysis engine + Streamlit UI
|   |-- genomic_database/             <-- HPA + UniProt database builder
|   |-- mock_services/                <-- Jira/Slack/Email mock integrations
|   |-- docker-compose.yml            <-- Container orchestration
|   +-- paciente_omega_rnaseq.csv     <-- Demo patient (dirty CSV for ETL test)
|
|-- figures/                           <-- Publication figures
|   |-- fig_paisajes_colapso.*         <-- Collapse stability landscapes (v2.5.0)
|   +-- fig_catastrofe_cuspide.*       <-- Fold catastrophe / friction control (v2.5.0)
|
+-- archive/                           <-- Superseded versions
```

---

## SNT Genomic Topologic Analyzer

Cross-domain application of SNT hub-satellite topology to functional genomics.
Instead of detecting structural mutations (wrong letters in the code), the
Genomic Agent detects **regulatory topology disruptions** (who stopped
controlling whom) using Z-score analysis against Human Protein Atlas baselines.

- **Two-Level Architecture:** Level-1 O(K) triage against 27 disease signatures
  across 9 cancers; Level-2 chromosome-by-chromosome orphan anomaly scan
- **Four anomaly types:** HUB_OVERACTIVATION, HUB_COLLAPSE,
  SATELLITE_CAPTURE, LEAPFROG
- **First ingestion (PX-OMEGA-001):** 8/27 confirmed signatures, 13 orphan
  anomalies (potential novel biomarkers), 4.3s total pipeline time

See `papers/SNT_Genomic_Topologic_Analyzer_v3.pdf` for full documentation.

---

## H-phi Hypothesis -- Closed

The hypothesis that **b** tends toward fractions of phi = 1.618... was
tested in three independent rounds:

| Round | Data | Result |
|-------|------|--------|
| 1 | Crypto (BTC/altcoins) | 0/4 |
| 2 | Primary biological literature | 0/6 |
| 3 | Real corpus n=188 (b>0) | p=0.642 -- identical to chance |

**H-phi refuted.** Does not affect the central friction-satellization finding.

---

## Falsifiability Criteria (RC1-RC8)

| RC | Refutation Condition | v29 Status |
|----|---------------------|------------|
| RC1 | Power law fits no better than linear/exponential across all domains | NOT REFUTED |
| RC2 | b is not reproducible from primary series | NOT REFUTED |
| RC3 | Abrupt triggers produce same b as gradual | NOT REFUTED |
| RC4 | Friction index is not correlated with b | NOT REFUTED |
| RC5 | N-body matrix does not change satellization estimates | NOT REFUTED |
| RC6 | Shadow node reverses satellization without exogenous trigger | NOT REFUTED |
| RC7 | ASI does not predict outcomes better than chance | NOT REFUTED |
| RC8 | Mutual interdependence does not brake satellization | NOT REFUTED |
| RC9 | Collapse axis is not orthogonal to satellization: corr(b, Delta) >> 0 | OPEN (test pending) |
| RC10 | A realized collapse takes a higher-friction path when a lower one exists | NOT REFUTED |
| RC11 | Absorber mass does not grow post-absorption (R does not increase) | NOT REFUTED |

---

## Reproducing the Analysis

```bash
# Clone and reproduce the full corpus
git clone https://github.com/Inzainos/The-shadow-Node-Theory.git
cd The-shadow-Node-Theory/reconstruction_real/code

# Regenerate domain B (446 cases -- requires owid-maddison.csv)
python3 expand_dominio_B.py

# Consolidated corpus
# reconstruction_real/data/snt_corpus_REAL_v5.csv
```

**Required primary sources** (all public):
- [Maddison Project Database 2020](https://www.rug.nl/ggdc/historicaldevelopment/maddison/)
- [OWID COVID-19 dataset](https://github.com/owid/covid-19-data)
- [Open Exoplanet Catalogue](https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue)
- [INEGI 2022](https://www.inegi.org.mx/temas/pib/)
- [US Census Bureau](https://www.census.gov/)

---

## Citation

```bibtex
@misc{zainoscorona2026snt,
  author       = {Zainos Corona, El{\'a}n},
  title        = {Shadow Node Theory v2.5.0: Scale-Invariant Satellization and
                  Coupled Orbital Collapse Across Empirical Domains},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19446521},
  url          = {https://ssrn.com/abstract=6418778}
}
```

---

## License

- **Code:** MIT License
- **Data:** CC BY 4.0 (derived datasets)
- **Paper:** CC BY-NC 4.0

---

## Contact

Elan Zainos Corona -- Fractal Core Research -- Tlaxcala, Mexico
GitHub: [Inzainos](https://github.com/Inzainos)

---

*Fractal Core Research -- Tlaxcala, Mexico*
*"Technical truth above numerical impression."*
*v2.5.0 | June 2026*
