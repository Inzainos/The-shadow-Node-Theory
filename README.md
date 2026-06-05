# Shadow Node Theory — Replication Package v2.3.1

**Paper:** Shadow Node Theory v2.3.1: Scale Invariance in the Node Satellization Algorithm  
**Subtitle:** 502 Verified Cases · 11 Domains · 30 Orders of Magnitude of Temporal Scale  
**Author:** Elán Zainos Corona  
**Institution:** Fractal Core Research — Tlaxcala, Mexico  
**Version:** v2.3.1 — 2026  
**Status:** 🟢 SUBMITTED — Journal of Complex Networks (Oxford University Press) | Manuscript: COMNET-2026-214 | Submitted: June 4, 2026  
**Zenodo DOI v2.3.1:** https://doi.org/10.5281/zenodo.19446521  
**Zenodo DOI v2.0:** https://doi.org/10.5281/zenodo.19131327  
**Zenodo DOI v1.0:** https://doi.org/10.5281/zenodo.19027089  
**SSRN:** https://ssrn.com/abstract=6418778

---

## What's New in v2.3.1

SNT v2.3.1 restructures the unified theoretical framework into four specialized papers targeting domain-specific journals, while maintaining the complete corpus and all prior results intact.

**1 — Target journal update**  
Submission moved from PLOS Complex Systems → **Journal of Complex Networks (Oxford University Press)** (no APC). Paper: `papers/snt_oxford_submission.docx`.

**2 — ROC-AUC corrected**  
HackerEarth validation: ROC-AUC = **0.715** (verified with real dataset, no data leakage). Dominant predictor: `n_event_types + delta_H`. 5-Event Wall validated.

**3 — H-φ validation completed** *(see `snt_phi_hypothesis.md` and `data/`)*  
Two independent validation rounds (crypto + primary biological data). Result: **negative** — H-φ classified as speculative second-order hypothesis. Does not affect main SNT results. H-3 permanently discarded.

**4 — Four specialized papers derived from marco_teorico_v28**

| File | Target journal | Language | Domain |
|---|---|---|---|
| `papers/snt_oxford_submission.docx` | Journal of Complex Networks | English | Full corpus (502 cases, 11 domains) |
| `papers/snt_paper_regional_economics_en.docx` | SSRN / regional economics journals | English | Historical + Mexico + Maddison |
| `papers/snt_paper_investigacion_economica.docx` | Investigación Económica (UNAM) | Spanish | Historical + Mexico + Maddison |
| `papers/snt_paper_theoretical_biology.docx` | Journal of Theoretical Biology | English | Domains E1, E2, E3 (biological) |
| `papers/snt_paper_astrophysical.docx` | The Astrophysical Journal | English | Domains F1, F2, F3, F4 (astronomical) |

**5 — Corpus expansion: 9 → 57 → 502 verified cases** *(v2.2)*  
11 domains spanning 30 orders of magnitude of temporal scale — from hours (HackerEarth 2026, 13.5-hour cycle) to billions of years (galactic disruption systems).

**6 — Biological domain extension — Module XIII** *(v2.2)*  
Species competition (E1, n=20, b_mean=+1.435), predator-prey (E2, n=4, b_mean=+0.102), parasite-host (E3, n=20, b_mean=+1.148). Key finding: antibiotic-resistant bacteria as the clearest biological leapfrog in the corpus (b=+1.401, R²=0.935, p<0.001).

**7 — Astronomical domain extension — Module XIV** *(v2.2)*  
Planetary systems (F1, n=14), stellar binaries (F2, n=8), black holes (F3, n=13), galactic systems (F4, n=12). The TON 618 quasar case produces the highest exponent in the full corpus: b=+6.498 (p=0.002).

**8 — Atomic Sovereignty Index (ASI) — operationalized — Module XII** *(v2.2)*  
Empirically calibrated with HackerEarth 2026 data (N=4,774 users). Formula: ASI = (δH × α) / F. Only 0.27% of users reach ASI ≥ 1.0. Precision: 1.0000 (zero false positives).

---

## Three Central Statistical Findings — Corpus of 502 Cases

| Finding | Result | Test |
|---|---|---|
| Abrupt triggers faster than gradual | b_abrupt=+0.552 vs b_gradual=−0.013 | Mann-Whitney U=24,802, p=1.91×10⁻⁵, n=486 |
| Institutional friction is the main speed predictor | No-friction b>1 · High-friction b≈0 | Systematic across all 11 domains |
| Political sovereignty = satellization brake | Countries: b_mean=−0.098 | n=230 pairs, Maddison 2023 |

Result stable across three successive corpus expansions (57 → 114 → 502 cases).

---

## Corpus Summary — 11 Domains

| Domain | n | b mean | Sig. (%) | Notes |
|---|---|---|---|---|
| A — Historical cities | 64 | +0.068 | 44 | Medieval to 20th century |
| B — Countries (Maddison) | 230 | −0.098 | 18 | Political sovereignty as brake |
| C — Intra-national regions | 64 | +0.053 | 33 | OECD, INEGI, Eurostat, US BEA |
| D — Digital ecosystems | 53 | +0.297 | 32 | Includes HackerEarth 2026 |
| E1 — Biological invasion | 20 | +1.435 | 75 | Highest significance rate in bio |
| E2 — Predator-prey | 4 | +0.102 | 50 | Oscillatory mutual dependency |
| E3 — Parasite-host | 20 | +1.148 | 60 | HIV/CD4, P. infestans, MRSA |
| F1 — Planetary | 14 | +1.029 | 50 | Jupiter vs rest of Solar System |
| F2 — Stellar binaries | 8 | +0.108 | 13 | Sirius A/B, cataclysmic variables |
| F3 — Black holes | 13 | +0.645 | 15 | TON 618: b=+6.498 (highest in corpus) |
| F4 — Galactic | 12 | +0.299 | 75 | Sagittarius dSph: b=+1.989 |
| **TOTAL** | **502** | — | **31.1** | b range: [−2.852, +7.086] |

---

## Repository Structure

```
shadow-node-theory/
│
├── README.md                                     ← This file (v2.3.1)
├── requirements.txt                              ← Python dependencies
├── sources.md                                    ← Data provenance
├── CITATION.cff                                  ← Citation metadata
├── snt_phi_hypothesis.md                         ← H-φ hypothesis + validation results
│
├── papers/
│   ├── snt_oxford_submission.docx                ← Main paper — J. Complex Networks ★
│   ├── marco_teorico_v28.pdf                     ← Unified Theoretical Framework (ES)
│   ├── snt_paper_regional_economics_en.docx      ← Economics paper (EN) — SSRN
│   ├── snt_paper_investigacion_economica.docx    ← Economics paper (ES) — Inv. Económica
│   ├── snt_paper_theoretical_biology.docx        ← Biology paper — J. Theoretical Biology
│   └── snt_paper_astrophysical.docx              ← Astronomy paper — Astrophysical Journal
│
├── code/
│   ├── snt_corpus_502.py                         ← Extended corpus analysis
│   ├── snt_corpus_biological.py                  ← Biological domains (E1–E3)
│   ├── snt_corpus_astronomical.py                ← Astronomical domains (F1–F4)
│   ├── hackerearth_validation_final.py           ← ASI / ROC-AUC validation
│   ├── generate_publication_figures.py           ← TIFF 300dpi figures
│   ├── snt_v2_vectorizacion.py                   ← Trajectory vectorization
│   └── shadow_node_verification_v2.py            ← Original v1.0 analysis
│
├── data/
│   ├── snt_corpus_final.csv                      ← Full 502-case corpus
│   ├── phi_validation_crypto.csv                 ← H-φ validation round 1 (crypto) ★
│   ├── phi_validation_bio_primary.csv            ← H-φ validation round 2 (biological) ★
│   ├── snt_corpus_500.csv                        ← Corpus v2.2
│   ├── snt_asi_scores.csv                        ← ASI scores HackerEarth
│   ├── matriz_mexico_32.csv                      ← 32 states INEGI classification
│   └── snt_v2_vectores.csv                       ← Trajectory vectors 8 states
│
└── figures/
    ├── Fig1.tif / Fig2.tif / Fig3.tif / Fig4.tif ← Publication figures (300dpi)
    └── shadow_node_maddison_final.png             ← Main figure v1.0
```
★ New in v2.3.1

---

## Key Results

### v1.0 — Power Law Fit (4 Historical Cases)

| Case | Mechanism | b | R² | Sig. | Type |
|---|---|---|---|---|---|
| Bruges → Antwerp | Infrastructure collapse | +0.787 | 0.987 | *** | Abrupt |
| Toledo → Madrid | Political decree | +0.687 | 0.894 | *** | Abrupt |
| Portugal → NW Europe | Iberian Union | +0.060 | 0.123 | n.s. | Gradual |
| Tlaxcala → Puebla | Accumulated advantage | +0.184 | 0.567 | *** | Gradual |

Two-speed taxonomy: abrupt triggers (b ≈ 0.74) are **5.9× faster** than gradual (b ≈ 0.12).

### v2.0 — N-Body Matrix (Mexico, 32 States)

| Level | N | PIB pc mean | % National GDP |
|---|---|---|---|
| 0 — Macro-Hub (CDMX) | 1 | 285.2k MXN | 14.8% |
| 1 — Secondary Attractors | 9 | 158.9k MXN | 41.0% |
| 2 — Logistic Bypass | 8 | 126.5k MXN | 20.2% |
| 3 — Shadow Nodes | 11 | 80.7k MXN | 16.8% |

Power law: f(rank) = 396.8 × rank^(−0.473), R² = 0.838, p < 0.001

### v2.2 — Atomic Sovereignty Index (ASI) — HackerEarth 2026, N=4,774

| Cohort | ASI (median) | Phase |
|---|---|---|
| Elite (0.27%) | ≥ 1.00 | Phase 4 — Full Sovereignty |
| Intermediate (6.4%) | 0.17 | Phase 3 — Parity |
| Basic (93.1%) | 0.016 | Phase 1 — Satellization |

ROC-AUC = 0.715. Precision = 1.0000. Zero false positives.

### v2.2 — Extreme Cases Across All Domains

| Case | Domain | b | p |
|---|---|---|---|
| TON 618 quasar accretion | F3 — Black holes | +6.498 | 0.002 |
| Zebra mussel vs native unionids | E1 — Bio invasion | +2.543 | <0.001 |
| African honeybee vs European | E1 — Bio invasion | +2.437 | 0.001 |
| Resistant bacteria (MRSA) | E3 — Parasite-host | +1.401 | <0.001 |
| M32 / Andromeda tidal stripping | F4 — Galactic | −2.336 | 0.0003 |

---

## H-φ Hypothesis Status

The φ-attractor hypothesis (H-φ) proposes that satellization exponents b cluster around rational fractions of φ ≈ 1.618 in systems with coupled feedback constraints.

**Validation completed — May 2026:**

| Round | Dataset | Confirmed |
|---|---|---|
| 1 — Crypto | 4 BTC/altcoin pairs (N=1374–2893 obs) | 0/4 |
| 2 — Biological primary | 6 published time series (MRSA, HIV, Trypanosoma) | 0/6 |
| **Total** | **10 independent datasets** | **0/10** |

**Conclusion:** H-φ is a speculative second-order hypothesis. It does not affect the main SNT framework, the b exponent, or the ASI Index. Full methodology and data in `snt_phi_hypothesis.md` and `data/phi_validation_*.csv`.

Sub-hypothesis H-3 (denominator-3 pattern): permanently discarded.

---

## Falsifiability Criteria (SNT v2.3.1)

| Code | Criterion | Falsified if |
|---|---|---|
| RC1 | Scalar velocity | Technology systematically adopted faster by firms than by individuals |
| RC2 | Immune response | Hub adaptation toward peripheral nodes documented more frequently than suppression |
| RC3 | Qualitative inextractability | Hub systematically neutralizes node knowledge differential at scale |
| RC4 | Dual minimum threshold | Leapfrog sustains with either RQ or RL below operational minimum |
| RC5 | Expansion sequence | Direct expropriation produces more stable states than silent absorption |
| RC6 | Irreversibility | Shadow Node reverses satellization endogenously with hub operating normally |
| RC7 | ASI operationalization | Users with ASI>1 show outcomes comparable to ASI<0.5 in cognitive sovereignty tasks |
| RC8 | Mutual interdependence brake | Predator-prey or sovereign-state systems produce sustained b>0.5 without exogenous perturbation |

---

## Reproducing the Analysis

```bash
pip install numpy scipy pandas matplotlib networkx openpyxl
python code/snt_corpus_502.py          # Full 502-case corpus
python code/hackerearth_validation_final.py   # ASI + ROC-AUC
python code/generate_publication_figures.py   # TIFF 300dpi figures
```

Full step-by-step in prior README version or `requirements.txt`.

---

## Data Sources

**1. Maddison Project Database 2023** — Bolt & van Zanden (2024). CC BY 4.0  
**2. INEGI — Sistema de Cuentas Nacionales de México** — PIB per capita by state 2022  
**3. HackerEarth 2026** — `zerve_hackathon_dataset.csv` (proprietary, not redistributable)  
**4. Biological E1–E3** — He Yu et al. (2022) *Nature Communications*; WHO AMR; UNAIDS  
**5. Astronomical F1–F4** — Gillessen et al. (2012) *Nature*; Majewski et al. (2003) *ApJ*  
**6. H-φ validation crypto** — Kaggle CryptoCompare historical price data (CC BY 4.0)  
**7. H-φ validation biological** — Norway MRSA (PLoS ONE 2013); ECDC EARS-Net; CDC AR Threats 2019

Full provenance in `sources.md`.

---

## Citation

```
Zainos Corona, E. (2026). Shadow Node Theory v2.3.1: Scale Invariance in the Node
Satellization Algorithm — 502 Verified Cases, 11 Domains, 30 Orders of Magnitude.
Fractal Core Research. SSRN: https://ssrn.com/abstract=6418778
Zenodo: https://doi.org/10.5281/zenodo.19446521
```

```bibtex
@misc{zainos2026shadowv231,
  author    = {Zainos Corona, Elan},
  title     = {Shadow Node Theory v2.3.1: Scale Invariance in the Node
               Satellization Algorithm},
  year      = {2026},
  doi       = {10.5281/zenodo.19446521},
  url       = {https://ssrn.com/abstract=6418778}
}
```

---

## License

- **Code:** MIT License  
- **Data:** CC BY 4.0 (derived datasets)  
- **Paper:** CC BY-NC 4.0

---

## Contact

Elán Zainos Corona — Fractal Core Research — Tlaxcala, México  
GitHub: [Inzainos](https://github.com/Inzainos)

---

> *"If you remain still long enough, you can see the algorithm that moves the universe."*  
> — Zainos Corona, E. (2026)

> *"The satellization algorithm is predictable. The leapfrog failure taxonomy is known.  
> What follows is a decision that no model can make for the node."*  
> — Shadow Node Theory v2.3.1, Conclusions
