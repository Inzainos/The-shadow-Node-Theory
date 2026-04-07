# Shadow Node Theory — Replication Package v2.2

**Paper:** Shadow Node Theory v2.2: Scale Invariance in the Node Satellization Algorithm  
**Subtitle:** 502 Verified Cases · 11 Domains · 30 Orders of Magnitude of Temporal Scale  
**Author:** Elan Zainos Corona (Captain 1n2a1n05)  
**Institution:** Fractal Core Research — Tlaxcala, Mexico  
**Version:** Pre-print v2.2 — 2026  
**SSRN:** https://ssrn.com/abstract=6418778  
**Zenodo DOI v2.0:** https://doi.org/10.5281/zenodo.19131327  
**Zenodo DOI v1.0:** https://doi.org/10.5281/zenodo.19027089

---

## What's New in v2.2

SNT v2.2 extends the Triple Resolution Model (v2.0) with four major contributions:

**1 — Corpus expansion: 9 → 57 → 502 verified cases**  
The empirical corpus now covers 502 cases across 11 domains, spanning 30 orders of magnitude in temporal scale — from hours (HackerEarth 2026, 13.5-hour cycle) to billions of years (galactic disruption systems).

**2 — Biological domain extension (Modules XIII)**  
Three new biological domains verified: species competition (E1, n=20, b_mean=+1.435), predator-prey (E2, n=4, b_mean=+0.102), and parasite-host (E3, n=20, b_mean=+1.148). Key finding: antibiotic-resistant bacteria as the clearest biological leapfrog in the corpus (b=+1.401, R²=0.935, p<0.001).

**3 — Astronomical domain extension (Module XIV)**  
Four astronomical domains verified: planetary systems (F1, n=14), stellar binaries (F2, n=8), black holes (F3, n=13), and galactic systems (F4, n=12). The Sagittarius A* / G2 cloud case produces the highest exponent in the full corpus: b=+2.838 (p=0.045), ratio 4.15×10¹¹.

**4 — Atomic Sovereignty Index (ASI) — operationalized**  
The ASI is now empirically calibrated with HackerEarth 2026 data (N=4,774 users). Formula: ASI = (δH × α) / F. Classification precision: 1.0000 (zero false positives). Spearman correlation ASI-CSI_V3: rs=0.178 (p<0.001). Only 0.27% of users reach ASI ≥ 1.0 (full cognitive sovereignty).

**5 — Module XV: The Satellization Cycle**  
Formalization of the four-phase cycle (Dependence → Accumulation → Parity → Inversion) with the epigraph:

> *"Si te quedas quieto el tiempo suficiente, puedes ver el algoritmo que mueve el universo."*  
> — Zainos Corona, E. (2026)

---

## Three Central Statistical Findings — Corpus of 502 Cases

| Finding | Result | Test |
|---|---|---|
| Abrupt triggers faster than gradual | b_abrupt=+0.552 vs b_gradual=−0.013 | Mann-Whitney p=1.91×10⁻⁵, n=486 |
| Institutional friction is the main speed predictor | No-friction systems b>1 / High-friction b≈0 | Systematic across all 11 domains |
| Political sovereignty = satellization brake | Countries: b_mean=−0.098 | n=230 pairs, Maddison 2023 |

---

## Corpus Summary — 11 Domains

| Domain | n | b mean | Sig. (%) | Notes |
|---|---|---|---|---|
| A — Historical cities | 64 | +0.068 | 44 | Medieval to 20th century |
| B — Countries (Maddison) | 230 | −0.098 | 18 | Political sovereignty as brake |
| C — Intra-national regions | 64 | +0.053 | 33 | OECD, INEGI, Eurostat, US BEA |
| D — Digital ecosystems | 53 | +0.297 | 32 | Includes HackerEarth 2026 |
| E1 — Biological invasion | 20 | +1.435 | 75 | Highest rate in bio domains |
| E2 — Predator-prey | 4 | +0.102 | 50 | Oscillatory mutual dependency |
| E3 — Parasite-host | 20 | +1.148 | 60 | HIV/CD4, P. infestans, MRSA |
| F1 — Planetary | 14 | +1.029 | 50 | Jupiter vs rest of Solar System |
| F2 — Stellar binaries | 8 | +0.108 | 13 | Sirius A/B, cataclysmic variables |
| F3 — Black holes | 13 | +0.645 | 15 | Sgr A* / G2: b=+2.838 |
| F4 — Galactic | 12 | +0.299 | 75 | Sagittarius dSph: b=+1.989 |
| **TOTAL** | **502** | — | **31.1** | b range: [−2.852, +7.086] |

---

## Repository Structure

```
shadow-node-theory/
│
├── README.md                              ← This file (v2.2)
├── requirements.txt                       ← Python dependencies
├── sources.md                             ← Data provenance
│
├── papers/
│   ├── marco_teorico_v28.pdf              ← Unified Theoretical Framework (SNT v2.2)
│   └── shadow_node_theory_SSRN_v10.docx  ← Main paper (SSRN pre-print)
│
├── abstracts/
│   └── abstracts_marco_teorico.docx      ← Abstract ES + EN
│
├── code/
│   ├── shadow_node_verification_v2.py    ← Original analysis (v1.0 cases)
│   ├── snt_v2_vectorizacion.py           ← Trajectory vectorization (v2.0)
│   ├── matriz_mexico_ncuerpos.py         ← N-body matrix analysis
│   └── snt_corpus_502.py                ← Extended corpus analysis (v2.2) [forthcoming]
│
├── data/
│   ├── shadow_node_maddison_resumen.csv  ← v1.0 results summary
│   ├── shadow_node_resultados_v2.csv     ← v1.0 case results
│   ├── matriz_mexico_32.csv              ← 32 states INEGI classification
│   ├── snt_v2_vectores.csv               ← Trajectory vectors 8 states
│   ├── dataset_historico_ampliado.csv    ← Extended historical dataset (9 cases)
│   └── corpus_502_summary.csv           ← 502-case corpus summary by domain [forthcoming]
│
└── figures/
    ├── shadow_node_maddison_final.png    ← Main figure v1.0 (4 cases + taxonomy)
    ├── matriz_mexico_graficas.png        ← N-body matrix visualization
    ├── snt_v2_vectorizacion.png          ← Trajectory vectorization panels
    └── red_ncuerpos_mexico.png           ← Network visualization with extraction vectors
```

---

## Key Results

### v1.0 — Power Law Fit (4 Historical Cases)

| Case | Mechanism | b | R² | Sig. | Type |
|---|---|---|---|---|---|
| Bruges → Antwerp | Infrastructure collapse | 0.787 | 0.987 | ** | Abrupt |
| Toledo → Madrid | Political decree | 0.687 | 0.894 | ** | Abrupt |
| Portugal → NW Europe | Iberian Union | 0.060 | 0.123 | n.s. | Gradual |
| Tlaxcala → Puebla | Accumulated advantage | 0.184 | 0.567 | *** | Gradual |

Two-speed taxonomy: abrupt triggers (b ≈ 0.74) are **5.9× faster** than gradual (b ≈ 0.12)

### v2.0 — N-Body Matrix (Mexico, 32 States)

| Level | N | PIB pc mean | % National GDP |
|---|---|---|---|
| 0 — Macro-Hub (CDMX) | 1 | 285.2k MXN | 14.8% |
| 1 — Secondary Attractors | 9 | 158.9k MXN | 41.0% |
| 2 — Bypass Logistic | 8 | 126.5k MXN | 20.2% |
| 3 — Shadow Nodes | 11 | 80.7k MXN | 16.8% |
| E — Exogenous | 3 | 183.8k MXN | 4.3% |

Power law: f(rank) = 396.8 × rank^(−0.473), R² = 0.838, p < 0.001  
Tlaxcala composite gradient: 243.0k MXN (9.3× the binary model estimate)

### v2.0 — Trajectory Vectorization (8 States, 1940–2022)

| State | b | R² | Sig. | Type |
|---|---|---|---|---|
| Chiapas | 0.229 | 0.839 | ** | Satellization |
| Veracruz | 0.181 | 0.719 | ** | Satellization |
| Guerrero | 0.176 | 0.808 | ** | Satellization |
| Oaxaca | 0.176 | 0.791 | ** | Satellization |
| Tlaxcala | 0.147 | 0.600 | * | Satellization |
| Puebla | 0.116 | 0.653 | * | Satellization |
| Querétaro | −0.155 | 0.782 | ** | **Leapfrog** |
| Nuevo León | −0.058 | 0.935 | *** | **Convergence** |

### v2.2 — Atomic Sovereignty Index (ASI)

| Cohort | δH | α | F | ASI (median) | Phase |
|---|---|---|---|---|---|
| Elite (0.5%) | 0.808 | 0.666 | 0.206 | 1.00 | Sovereignty |
| Intermediate (6.4%) | 0.498 | 0.397 | 0.434 | 0.17 | Accumulation |
| Basic (93.1%) | 0.199 | 0.199 | 0.711 | 0.016 | Satellization |

ASI ≥ 1.0 reached by 13 users (0.27% of N=4,774). Precision: 1.0000. Zero false positives.

---

## Data Sources

**1. Maddison Project Database 2023** *(Primary — v1.0 and v2.0)*  
Bolt, J. and van Zanden, J.L. (2024). University of Groningen.  
https://www.rug.nl/ggdc/historicaldevelopment/maddison/ · License: CC BY 4.0

**2. INEGI — Sistema de Cuentas Nacionales de México** *(v2.0)*  
PIB per capita by state 2022. https://www.inegi.org.mx/temas/pib/ · 32 states

**3. Historical Demographic Data** *(v1.0)*  
See `sources.md` — Bruges-Antwerp, Toledo-Madrid, Portugal-NW Europe, Tlaxcala-Puebla

**4. HackerEarth 2026 — zerve_hackathon_dataset.csv** *(Digital Domain)*  
Proprietary dataset — not redistributable. Aggregate results in `data/` directory.

**5. Biological domains** *(v2.2)*  
He Yu et al. (2022) *Nature Communications* (rat displacement); Nakagaki (2010) *Science*;  
WHO AMR surveillance data (MRSA); UNAIDS HIV/CD4 longitudinal data.

**6. Astronomical domains** *(v2.2)*  
Maddison 2023 (economic analogy); Gillessen et al. (2012) *Nature* (Sgr A*/G2);  
Erkal et al. (2019) (LMC mass); Dierickx et al. (2014) (M32/M31).

---

## Reproducing the Analysis

### Requirements
```bash
pip install numpy scipy pandas matplotlib networkx openpyxl
```

### Step 1 — Download Maddison Project Database
Place `mpd2023_web.xlsx` in the `data/` directory.

### Step 2 — N-body matrix (Mexico)
```bash
python code/matriz_mexico_ncuerpos.py
```
Outputs: `data/matriz_mexico_32.csv`, `figures/matriz_mexico_graficas.png`, `figures/red_ncuerpos_mexico.png`

### Step 3 — Trajectory vectorization
```bash
python code/snt_v2_vectorizacion.py
```
Outputs: `data/snt_v2_vectores.csv`, `figures/snt_v2_vectorizacion.png`

### Step 4 — Original v1.0 analysis
```bash
python code/shadow_node_verification_v2.py
```

---

## Refutation Criteria (SNT v2.2)

The model specifies six explicit refutation criteria (RC1–RC6) plus RC7 (ASI operationalization) and RC8 (oscillatory mutual dependency systems). A model that cannot be refuted is not science — it is narrative. Full criteria in `marco_teorico_v28.pdf`, Module VI.

---

## Citation

```
Zainos Corona, E. (2026). Shadow Node Theory v2.2: Scale Invariance in the Node
Satellization Algorithm. Fractal Core Research Pre-print v2.2.
SSRN: https://ssrn.com/abstract=6418778
Zenodo: https://doi.org/10.5281/zenodo.19131327
```

### BibTeX
```bibtex
@misc{zainos2026shadowv22,
  author    = {Zainos Corona, Elan},
  title     = {Shadow Node Theory v2.2: Scale Invariance in the Node
               Satellization Algorithm — 502 Verified Cases, 11 Domains},
  year      = {2026},
  publisher = {SSRN / Zenodo},
  note      = {Pre-print v2.2},
  doi       = {10.5281/zenodo.19131327},
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

> *"Si te quedas quieto el tiempo suficiente, puedes ver el algoritmo que mueve el universo."*  
> — Zainos Corona, E. (2026)

> *"El algoritmo de satelización es predecible. La taxonomía de fallos del leapfrog es conocida.  
> Lo que sigue es una decisión que ningún modelo puede tomar por el nodo."*  
> — Shadow Node Theory v2.2, Conclusiones
