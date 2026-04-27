# Shadow Node Theory — Replication Package v2.3.1

**Paper:** Shadow Node Theory v2.3.1: Scale Invariance in the Node Satellization Algorithm  
**Subtitle:** 502 Verified Cases · 11 Domains · 30 Orders of Magnitude of Temporal Scale  
**Author:** Elan Zainos Corona (Captain 1n2a1n05)  
**Institution:** Fractal Core Research — Tlaxcala, Mexico  
**Version:** v2.3.1 — 2026  
**Status:** 🟡 Under peer review — PLOS Complex Systems (submitted April 2026)  
**Zenodo DOI v2.3.1:** https://doi.org/10.5281/zenodo.19446521
**Zenodo DOI v2.0:** https://doi.org/10.5281/zenodo.19131327  
**Zenodo DOI v1.0:** https://doi.org/10.5281/zenodo.19027089

---

## What's New in v2.3.1

SNT v2.3.1 restructures the unified theoretical framework into four specialized papers targeting domain-specific journals, while maintaining the complete corpus and all prior results intact.

**1 — Four specialized papers derived from marco_teorico_v28**

| File | Target journal | Language | Domain |
|---|---|---|---|
| `snt_paper_plos_complex_systems.docx` | PLOS Complex Systems | English | Full corpus (502 cases, 11 domains) |
| `snt_paper_regional_economics_en.docx` | SSRN / regional economics journals | English | Historical + Mexico + Maddison |
| `snt_paper_investigacion_economica.docx` | Investigación Económica (UNAM) | Spanish | Historical + Mexico + Maddison |
| `snt_paper_theoretical_biology.docx` | Journal of Theoretical Biology | English | Domains E1, E2, E3 (biological) |
| `snt_paper_astrophysical.docx` | The Astrophysical Journal | English | Domains F1, F2, F3, F4 (astronomical) |

**2 — Corpus expansion: 9 → 57 → 502 verified cases** (v2.2)  
11 domains spanning 30 orders of magnitude of temporal scale — from hours (HackerEarth 2026, 13.5-hour cycle) to billions of years (galactic disruption systems).

**3 — Biological domain extension — Module XIII** (v2.2)  
Species competition (E1, n=20, b_mean=+1.435), predator-prey (E2, n=4, b_mean=+0.102), parasite-host (E3, n=20, b_mean=+1.148). Key finding: antibiotic-resistant bacteria as the clearest biological leapfrog in the corpus (b=+1.401, R²=0.935, p<0.001).

**4 — Astronomical domain extension — Module XIV** (v2.2)  
Planetary systems (F1, n=14), stellar binaries (F2, n=8), black holes (F3, n=13), galactic systems (F4, n=12). The TON 618 quasar case produces the highest exponent in the full corpus: b=+6.498 (p=0.002). Sagittarius A*/G2 cloud: b=+2.838 (p=0.045), ratio 4.15×10¹¹.

**5 — Atomic Sovereignty Index (ASI) — operationalized — Module XII** (v2.2)  
Empirically calibrated with HackerEarth 2026 data (N=4,774 users). Formula: ASI = (δH × α) / F. Classification precision: 1.0000 (zero false positives). Only 0.27% of users reach ASI ≥ 1.0 (full cognitive sovereignty).

**6 — Module XV: The Satellization Cycle** (v2.2)  
Formalization of the four-phase cycle (Dependence → Accumulation → Parity → Inversion) operating across all 11 domains. The Atomic Node is not a state — it is a phase.

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
├── README.md                                    ← This file (v2.3.1)
├── requirements.txt                             ← Python dependencies
├── sources.md                                   ← Data provenance
│
├── papers/
│   ├── marco_teorico_v28.pdf                    ← Unified Theoretical Framework (ES)
│   ├── snt_paper_plos_complex_systems.docx      ← Full corpus paper — PLOS Complex Systems
│   ├── snt_paper_regional_economics_en.docx     ← Economics paper (EN) — SSRN
│   ├── snt_paper_investigacion_economica.docx   ← Economics paper (ES) — Inv. Económica
│   ├── snt_paper_theoretical_biology.docx       ← Biology paper — J. Theoretical Biology
│   ├── snt_paper_astrophysical.docx             ← Astronomy paper — Astrophysical Journal
│   └── shadow_node_theory_SSRN_v10.docx         ← Original SSRN pre-print (v2.2)
│
├── abstracts/
│   └── abstracts_marco_teorico.docx             ← Abstract ES + EN
│
├── code/
│   ├── shadow_node_verification_v2.py           ← Original analysis (v1.0 cases)
│   ├── snt_v2_vectorizacion.py                  ← Trajectory vectorization (v2.0)
│   ├── matriz_mexico_ncuerpos.py                ← N-body matrix analysis
│   └── snt_corpus_502.py                        ← Extended corpus analysis (v2.2)
│
├── data/
│   ├── shadow_node_maddison_resumen.csv         ← v1.0 results summary
│   ├── shadow_node_resultados_v2.csv            ← v1.0 case results
│   ├── matriz_mexico_32.csv                     ← 32 states INEGI classification
│   ├── snt_v2_vectores.csv                      ← Trajectory vectors 8 states
│   ├── dataset_historico_ampliado.csv           ← Extended historical dataset
│   └── corpus_502_summary.csv                   ← 502-case corpus summary by domain
│
└── figures/
    ├── shadow_node_maddison_final.png           ← Main figure v1.0 (4 cases + taxonomy)
    ├── matriz_mexico_graficas.png               ← N-body matrix visualization
    ├── snt_v2_vectorizacion.png                 ← Trajectory vectorization panels
    └── red_ncuerpos_mexico.png                  ← Network with extraction vectors
```

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
| E — Exogenous | 3 | 183.8k MXN | 4.3% |

Power law: f(rank) = 396.8 × rank^(−0.473), R² = 0.838, p < 0.001  
Tlaxcala composite gradient: 243.0k MXN — **9.3× the binary model estimate**  
89.2% of Tlaxcala's extraction flows directly to CDMX, bypassing Puebla.

### v2.0 — Trajectory Vectorization (8 States, 1940–2022)

| State | b | R² | Sig. | Classification |
|---|---|---|---|---|
| Chiapas | +0.229 | 0.839 | ** | Satellization |
| Veracruz | +0.181 | 0.719 | ** | Satellization |
| Guerrero | +0.176 | 0.808 | ** | Satellization |
| Oaxaca | +0.176 | 0.791 | ** | Satellization |
| Tlaxcala | +0.147 | 0.600 | * | Satellization |
| Puebla | +0.116 | 0.653 | * | Satellization |
| Querétaro | −0.155 | 0.782 | ** | **Leapfrog** |
| Nuevo León | −0.058 | 0.935 | *** | **Convergence** |

### v2.2 — Atomic Sovereignty Index (ASI) — HackerEarth 2026, N=4,774

| Cohort | δH | α | F | ASI (median) | Phase |
|---|---|---|---|---|---|
| Elite (0.5%) | 0.808 | 0.666 | 0.206 | 1.00 | Phase 4 — Sovereignty |
| Intermediate (6.4%) | 0.498 | 0.397 | 0.434 | 0.17 | Phase 3 — Parity |
| Basic (93.1%) | 0.199 | 0.199 | 0.711 | 0.016 | Phase 1 — Satellization |

ASI ≥ 1.0: 13 users (0.27% of N=4,774). Precision: 1.0000. Zero false positives.  
Spearman correlation ASI-CSI_V3: rs=0.178 (p<0.001).

### v2.2 — Extreme Cases Across All Domains

| Case | Domain | b | R² | p |
|---|---|---|---|---|
| TON 618 quasar accretion | F3 — Black holes | +6.498 | — | 0.002 |
| Sgr A* / G2 cloud | F3 — Black holes | +2.838 | — | 0.045 |
| Zebra mussel vs native unionids | E1 — Bio invasion | +2.543 | 0.885 | <0.001 |
| African honeybee vs European | E1 — Bio invasion | +2.437 | 0.376 | 0.001 |
| Sagittarius dSph disruption | F4 — Galactic | +1.989 | 0.716 | 0.0035 |
| Resistant bacteria (MRSA) | E3 — Parasite-host | +1.401 | 0.935 | <0.001 |
| M32 / Andromeda tidal stripping | F4 — Galactic | −2.336 | 0.818 | 0.0003 |

---

## Data Sources

**1. Maddison Project Database 2023** *(Primary — v1.0, v2.0, v2.2)*  
Bolt, J. and van Zanden, J.L. (2024). University of Groningen.  
https://www.rug.nl/ggdc/historicaldevelopment/maddison/ · License: CC BY 4.0

**2. INEGI — Sistema de Cuentas Nacionales de México** *(v2.0)*  
PIB per capita by state 2022. https://www.inegi.org.mx/temas/pib/ · 32 states

**3. Historical Demographic Data** *(v1.0)*  
See `sources.md` — Bruges-Antwerp, Toledo-Madrid, Portugal-NW Europe, Tlaxcala-Puebla

**4. HackerEarth 2026 — zerve_hackathon_dataset.csv** *(Digital Domain — D)*  
Proprietary dataset — not redistributable. Aggregate results in `data/` directory.

**5. Biological domains E1, E2, E3** *(v2.2)*  
He Yu et al. (2022) *Nature Communications* (rat displacement Europe);  
WHO AMR surveillance data (MRSA); UNAIDS HIV/CD4 longitudinal data;  
Hudson Bay Company fur records 1845–1935 (lynx-hare).

**6. Astronomical domains F1–F4** *(v2.2)*  
Gillessen et al. (2012) *Nature* (Sgr A*/G2); Erkal et al. (2019) *MNRAS* (LMC mass);  
Majewski et al. (2003) *ApJ* (Sagittarius dSph); Pollack et al. (1996) *Icarus* (planetary formation);  
Valtonen et al. (2016) *ApJL* (OJ287 binary BH).

---

## Reproducing the Analysis

### Requirements
```bash
pip install numpy scipy pandas matplotlib networkx openpyxl
```

### Step 1 — Download Maddison Project Database
Place `mpd2023_web.xlsx` in the `data/` directory.

### Step 2 — N-body matrix (Mexico, 32 states)
```bash
python code/matriz_mexico_ncuerpos.py
```
Outputs: `data/matriz_mexico_32.csv`, `figures/matriz_mexico_graficas.png`, `figures/red_ncuerpos_mexico.png`

### Step 3 — Trajectory vectorization (8 states, 1940–2022)
```bash
python code/snt_v2_vectorizacion.py
```
Outputs: `data/snt_v2_vectores.csv`, `figures/snt_v2_vectorizacion.png`

### Step 4 — Original v1.0 analysis (4 historical cases)
```bash
python code/shadow_node_verification_v2.py
```

### Step 5 — Extended 502-case corpus
```bash
python code/snt_corpus_502.py
```
Outputs: `data/corpus_502_summary.csv`

### Step 6 — Biological corpus (E1, E2, E3 — 44 cases)
```bash
python code/snt_corpus_biological.py
```
Outputs: `data/snt_corpus_biological_results.csv`, `figures/snt_corpus_biological_figures.png`

### Step 7 — Astronomical corpus (F1, F2, F3, F4 — 47 cases)
```bash
python code/snt_corpus_astronomical.py
```
Outputs: `data/snt_corpus_astronomical_results.csv`, `figures/snt_corpus_astronomical_figures.png`

### Step 8 — Publication-quality figures (PLOS-ready)
```bash
python code/generate_publication_figures.py
```
Outputs: `figures/fig1–4 (.svg + .png 300dpi)`

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

A model that cannot be refuted is not science — it is narrative. Full criteria in `marco_teorico_v28.pdf`, Module VI.

---

## Citation

```
Zainos Corona, E. (2026). Shadow Node Theory v2.3.1: Scale Invariance in the Node
Satellization Algorithm — 502 Verified Cases, 11 Domains, 30 Orders of Magnitude.
Fractal Core Research Pre-print v2.3.1.
SSRN: https://ssrn.com/abstract=6418778
Zenodo: https://doi.org/10.5281/zenodo.19446521
```

### BibTeX
```bibtex
@misc{zainos2026shadowv231,
  author    = {Zainos Corona, Elan},
  title     = {Shadow Node Theory v2.3.1: Scale Invariance in the Node
               Satellization Algorithm — 502 Verified Cases, 11 Domains,
               30 Orders of Magnitude of Temporal Scale},
  year      = {2026},
  publisher = {SSRN / Zenodo},
  note      = {Pre-print v2.3.1},
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

Elan Zainos Corona — Fractal Core Research — Tlaxcala, Mexico  
GitHub: [Inzainos](https://github.com/Inzainos)

---

> *"If you remain still long enough, you can see the algorithm that moves the universe."*  
> — Zainos Corona, E. (2026)

> *"The satellization algorithm is predictable. The leapfrog failure taxonomy is known.  
> What follows is a decision that no model can make for the node."*  
> — Shadow Node Theory v2.3.1, Conclusions
