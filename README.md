# Shadow Node Theory — Replication Package

**Paper:** Shadow Node Theory: Invarianza de Escala en el Algoritmo de Satelizacion de Nodos  
**Author:** Elan Zainos Corona (Captain 1n2a1n05)  
**Institution:** Fractal Core Research — Tlaxcala, Mexico  
**Version:** Pre-print v1.0 — 2026  
**SSRN:** [link pending after submission]  
**Zenodo DOI:** [assigned after deposit]

-----

## Overview

This repository contains all data, code, and supplementary materials needed to reproduce the quantitative results reported in the paper. The Shadow Node Theory (SNT) postulates that when two power nodes orbit in critical proximity, the node with greater accumulated advantage satellizes the historical node through a predictable power-law algorithm. This repository documents the empirical verification of that hypothesis across five cases in three domains.

-----

## Repository Structure

```
shadow-node-theory/
│
├── README.md                          ← This file
│
├── data/
│   ├── maddison_extracted.csv         ← GDP per capita series extracted from MPD 2023
│   ├── shadow_node_resultados_v2.csv  ← Power law fit results by case
│   ├── shadow_node_maddison_resumen.csv ← Summary table: exponents + R2 + taxonomy
│   └── sources.md                     ← Data provenance and access instructions
│
├── code/
│   ├── shadow_node_verification_v2.py ← Main analysis script (power law fitting)
│   ├── requirements.txt               ← Python dependencies
│   └── notebooks/
│       └── exploratory_analysis.md   ← Notes on data exploration
│
├── figures/
│   ├── shadow_node_maddison_final.png ← Main 4-panel figure + taxonomy bar chart
│   └── figure_caption.md             ← Caption for the main figure
│
└── supplementary/
    ├── protocolo_verificacion_v2.docx ← Verification protocol (Spanish)
    └── marco_teorico_v08.docx         ← Full theoretical framework (Spanish)
```

-----

## Data Sources

### 1. Maddison Project Database 2023 (Primary)

**Citation:** Bolt, J. and van Zanden, J.L. (2024). Maddison Project Database 2023. Groningen Growth and Development Centre, University of Groningen.

**Access:** https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2023

**License:** Creative Commons Attribution 4.0 (CC BY 4.0)

**Variables used:**

- `gdppc` — GDP per capita in international dollars, 2011 PPP
- `pop` — Population in thousands
- Countries: Mexico, Spain, Portugal, Netherlands, United Kingdom

**File in this repository:** `data/maddison_extracted.csv` contains only the rows and columns used in the analysis. The full database (mpd2023_web.xlsx) must be downloaded directly from the Groningen website due to its size.

### 2. Historical Demographic Data (Bruges-Antwerp, Toledo-Madrid)

These are estimates from published academic sources, not raw archival data. See `data/sources.md` for full citations.

|Case          |Variable                |Key Source                                            |Uncertainty                      |
|--------------|------------------------|------------------------------------------------------|---------------------------------|
|Bruges-Antwerp|Population (thousands)  |Nicholas (1992); Van der Wee (1963); Gelderblom (2013)|±20% for medieval estimates      |
|Toledo-Madrid |Population (inhabitants)|Ringrose (1973); INE España                           |±15% for 1600-1750 interpolations|

### 3. INEGI Mexico (Tlaxcala-Puebla 1993-2022)

**Access:** https://www.inegi.org.mx/temas/pib/

**Variables used:**

- GDP per capita by state (entidad federativa), 1993-2022
- Foreign direct investment by state (Secretaría de Economía)
- Labor migration by state (ENOE, CONEVAL)

**Key calibration anchor:** Puebla/Tlaxcala GDP per capita ratio = 1.49 in 1993 (48.8% advantage). This datum anchors the long historical series.

### 4. HackerEarth 2026 (Digital Domain)

**Dataset:** zerve_hackathon_dataset.csv  
**Source:** HackerEarth Hackathon 2026 — proprietary dataset, not redistributable.  
**Description:** 409,287 events from 4,774 unique users, 141 event types, HackerEarth Canvas platform.  
**Pipeline:** Fractal Core Framework V3 (Captain 1n2a1n05, 2026)

> **Note:** The raw dataset cannot be redistributed due to platform data terms. The analysis code (`shadow_node_verification_v2.py`) documents the pipeline methodology. The aggregate results (cohort sizes, VDR ratios, model metrics) are reproduced in `data/shadow_node_maddison_resumen.csv`.

-----

## Reproducing the Analysis

### Requirements

```bash
pip install numpy scipy pandas matplotlib openpyxl
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

### Step 1 — Download Maddison Project Database

Download `mpd2023_web.xlsx` from:  
https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2023

Place the file in the `data/` directory.

### Step 2 — Run the main analysis

```bash
python code/shadow_node_verification_v2.py
```

This script:

1. Loads the Maddison Project data (requires `mpd2023_web.xlsx` in `data/`)
1. Constructs ratio time series for all four historical cases
1. Fits power law models using log-log linear regression
1. Computes exponents (b), R², Pearson correlation, and p-values
1. Identifies the activation threshold (10-15% advantage) for each case
1. Calculates divergence velocity post-trigger
1. Generates the main figure (`figures/shadow_node_maddison_final.png`)
1. Exports results to `data/shadow_node_maddison_resumen.csv`

### Step 3 — Expected output

```
======================================================================
SHADOW NODE THEORY — VERIFICACION CON MADDISON PROJECT 2023
======================================================================

TABLA COMPARATIVA — EXPONENTES CON DATOS MADDISON REALES
              caso                mecanismo  exponente_b     r2
    Brujas_Amberes  Infraestructura (Zwin)       0.7390  0.8684
     Toledo_Madrid  Decreto politico (1561)      0.6944  0.9239
Portugal_NW_Europa  Satelizacion sistemica       0.0602  0.1229
   Tlaxcala_Puebla  Ventaja acumulada (1535)     0.1842  0.5672

Triggers abruptos  (Brujas, Toledo):  b_media=0.7165
Triggers graduales (Portugal, Tlaxc): b_media=0.1222
Ratio de velocidades: 5.9x
```

-----

## Key Results

|Case                   |Mechanism                           |Exponent b|R²        |p-value |Trigger type|
|-----------------------|------------------------------------|----------|----------|--------|------------|
|Bruges → Antwerp       |Physical infrastructure collapse    |0.739     |0.868     |< 0.001 |Abrupt      |
|Toledo → Madrid        |Political decree                    |0.694     |0.924     |< 0.001 |Abrupt      |
|Portugal → NW Europe   |Institutional vacuum (Iberian Union)|0.060     |0.123     |0.277*  |Gradual     |
|Tlaxcala → Puebla      |Accumulated colonial advantage      |0.184     |0.567     |< 0.001 |Gradual     |
|HackerEarth Elite/Basic|Digital behavioral gap              |—         |ROC 0.9994|CV=1.000|Digital     |

*Portugal R² is low due to oscillatory process (Brazilian gold cycle). Long-run divergence trend confirmed: ratio 1.85 (1535) → 3.68 (1913).

**Two-speed taxonomy:** Abrupt triggers produce satellization 5.9× faster than gradual triggers. This ratio emerges from the data without being assumed in the model.

-----

## Methodological Notes

### Power law fitting

All fits use log-log linear regression (standard method per Clauset, Shalizi & Newman, 2009). R² is reported on the original scale. The p-value corresponds to the Pearson correlation in log-log space.

### Portugal case

The low R² (0.123) reflects the oscillatory nature of the process, not absence of the pattern. The Brazilian gold cycle (1700-1750) produces a partial recovery that breaks the monotonic fit. The long-run divergence trend is unambiguous: ratio multiplied 3.5× between 1535 and 1913.

### Tlaxcala-Puebla calibration

Pre-1993 data are constructed estimates based on:

- Maddison Project Mexico national series as a proxy for regional differential
- Two anchors: estimated 12% initial advantage in 1535 (post-Real Cédula) and verified 48.8% advantage in 1993 (INEGI direct data)
- The trajectory between these anchors reflects national development patterns (Maddison), not necessarily the specific regional differential at each point

### Digital case

The GradientBoostingClassifier achieving ROC-AUC = 1.000 in cross-validation reflects the bimodal (non-Gaussian) distribution of user behavior, not overfitting. The churn early warning model using only raw event features (284 features, no CSI V3) achieves ROC-AUC = 0.9994, confirming the pattern is present in raw behavioral data.

-----

## Limitations

1. Pre-1820 historical data have uncertainty of ±20% for medieval estimates
1. Small N (four historical cases) limits statistical inference on exponent distribution
1. Portugal’s low R² requires a power law model with exogenous perturbations
1. Digital case: reverse causality cannot be ruled out without longitudinal data
1. Case selection bias: cases were selected with prior knowledge of pattern visibility

Full discussion in Section 7 of the paper.

-----

## Citation

If you use this code or data, please cite:

```
Zainos Corona, E. (2026). Shadow Node Theory: Invarianza de Escala en el 
Algoritmo de Satelizacion de Nodos. Fractal Core Research Pre-print v1.0. 
SSRN: [link]. Zenodo DOI: [DOI].
```

BibTeX:

```bibtex
@misc{zainos2026shadow,
  author       = {Zainos Corona, Elan},
  title        = {Shadow Node Theory: Scale Invariance in the Node 
                  Satellization Algorithm},
  year         = {2026},
  publisher    = {SSRN / Zenodo},
  note         = {Pre-print v1.0},
  doi          = {[DOI pending]},
  url          = {[URL pending]}
}
```

-----

## License

**Code:** MIT License — free to use, modify and distribute with attribution.  
**Data:** CC BY 4.0 for derived datasets. Original sources retain their own licenses (see `data/sources.md`).  
**Paper:** CC BY-NC 4.0 — free to share with attribution, non-commercial use only.

-----

## Contact

Elan Zainos Corona  
Fractal Core Research — Tlaxcala, Mexico  
GitHub: Captain 1n2a1n05

-----

*“El algoritmo de satelizacion es predecible. Y lo que es predecible puede ser intervenido.”*  
*— Shadow Node Theory, Conclusiones*
