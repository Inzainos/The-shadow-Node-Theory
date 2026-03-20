# Shadow Node Theory — Replication Package v2.0

**Paper:** Shadow Node Theory v2.0: Scale Invariance in the Node Satellization Algorithm — Triple Resolution Model  
**Author:** Elan Zainos Corona (Captain 1n2a1n05)  
**Institution:** Fractal Core Research — Tlaxcala, Mexico  
**Version:** Pre-print v2.0 — 2026  
**SSRN:** https://ssrn.com/abstract=6418778  
**Zenodo DOI v1.0:** https://doi.org/10.5281/zenodo.19027089

---

## What's New in v2.0

The SNT v2.0 extends the binary model with three major contributions:

1. **Triple Resolution Model** — formalizes satellization across three distinct scales: Micro (Atomic Node / individual), Meso (Fungal Network / intra-national), and Macro (superorganism collision between nations/corporations)

2. **N-Body Matrix — Mexico** — empirical verification of the five-level taxonomy with INEGI 2022 data for all 32 Mexican states. Power law confirmed: b = -0.473, R² = 0.838, p < 0.001

3. **Trajectory Vectorization** — eight Mexican states tracked 1940–2022. First documented cases of successful leapfrog within the national system: Querétaro (b = -0.155, p < 0.01) and Nuevo León (b = -0.058, p < 0.001)

4. **Enterprise Domain Extension** — formal application of the model to corporate ecosystems. HackerEarth 2026 as prototype of the enterprise complex system

---

## Repository Structure

```
shadow-node-theory/
│
├── README.md                              ← This file
├── requirements.txt                       ← Python dependencies
├── sources.md                             ← Data provenance
│
├── code/
│   ├── shadow_node_verification_v2.py     ← Original analysis (v1.0 cases)
│   ├── snt_v2_vectorizacion.py            ← Trajectory vectorization (v2.0)
│   └── matriz_mexico_ncuerpos.py          ← N-body matrix analysis
│
├── data/
│   ├── shadow_node_maddison_resumen.csv   ← v1.0 results summary
│   ├── shadow_node_resultados_v2.csv      ← v1.0 case results
│   ├── matriz_mexico_32.csv               ← 32 states INEGI classification
│   ├── snt_v2_vectores.csv                ← Trajectory vectors 8 states
│   └── dataset_historico_ampliado.csv     ← Extended historical dataset (9 cases)
│
└── figures/
    ├── shadow_node_maddison_final.png     ← Main figure v1.0 (4 cases + taxonomy)
    ├── matriz_mexico_graficas.png         ← N-body matrix visualization
    ├── snt_v2_vectorizacion.png           ← Trajectory vectorization panels
    └── red_ncuerpos_mexico.png            ← Network visualization with extraction vectors
```

---

## Data Sources

### 1. Maddison Project Database 2023 (Primary — v1.0 and v2.0)
**Citation:** Bolt, J. and van Zanden, J.L. (2024). Maddison Project Database 2023. University of Groningen.  
**Access:** https://www.rug.nl/ggdc/historicaldevelopment/maddison/  
**License:** CC BY 4.0

### 2. INEGI — Sistema de Cuentas Nacionales de México (New in v2.0)
**Variables:** PIB per capita by state 2022, % of national GDP  
**Access:** https://www.inegi.org.mx/temas/pib/  
**Coverage:** 32 estados, 2022

### 3. Historical Demographic Data (v1.0)
See `sources.md` for full citations by case (Bruges-Antwerp, Toledo-Madrid, Portugal-NW Europe, Tlaxcala-Puebla)

### 4. HackerEarth 2026 (Digital Domain)
Proprietary dataset — not redistributable. Aggregate results available in `data/` directory.

---

## Reproducing the v2.0 Analysis

### Requirements
```bash
pip install numpy scipy pandas matplotlib networkx openpyxl
```

### Step 1 — Download Maddison Project Database
Place `mpd2023_web.xlsx` in the `data/` directory.

### Step 2 — Run N-body matrix (Mexico)
```bash
python code/matriz_mexico_ncuerpos.py
```
Outputs: `data/matriz_mexico_32.csv`, `figures/matriz_mexico_graficas.png`, `figures/red_ncuerpos_mexico.png`

### Step 3 — Run trajectory vectorization
```bash
python code/snt_v2_vectorizacion.py
```
Outputs: `data/snt_v2_vectores.csv`, `figures/snt_v2_vectorizacion.png`

### Step 4 — Run original v1.0 analysis
```bash
python code/shadow_node_verification_v2.py
```

---

## Key Results

### v1.0 — Power Law Fit (4 Historical Cases)

| Case | Mechanism | b | R² | Sig. | Type |
|------|-----------|---|-----|------|------|
| Bruges → Antwerp | Infrastructure collapse | 0.787 | 0.987 | ** | Abrupt |
| Toledo → Madrid | Political decree | 0.687 | 0.894 | ** | Abrupt |
| Portugal → NW Europe | Iberian Union | 0.060 | 0.123 | n.s. | Gradual |
| Tlaxcala → Puebla | Accumulated advantage | 0.184 | 0.567 | *** | Gradual |

**Two-speed taxonomy:** Abrupt triggers (b ≈ 0.74) are 5.9× faster than gradual (b ≈ 0.12)

### v2.0 — N-Body Matrix (Mexico, 32 States)

| Level | N | PIB pc mean | % National GDP |
|-------|---|------------|----------------|
| 0 — Macro-Hub (CDMX) | 1 | 285.2k MXN | 14.8% |
| 1 — Secondary Attractors | 9 | 158.9k MXN | 41.0% |
| 2 — Bypass Logistic | 8 | 126.5k MXN | 20.2% |
| 3 — Shadow Nodes | 11 | 80.7k MXN | 16.8% |
| E — Exogenous | 3 | 183.8k MXN | 4.3% |

**Power law:** f(rank) = 396.8 × rank^(-0.473), R² = 0.838, p < 0.001  
**Tlaxcala composite gradient:** 243.0k MXN (9.3× the binary model estimate)

### v2.0 — Trajectory Vectorization (8 States, 1940–2022)

| State | b | R² | Sig. | Type |
|-------|---|-----|------|------|
| Chiapas | 0.229 | 0.839 | ** | Satellization |
| Veracruz | 0.181 | 0.719 | ** | Satellization |
| Guerrero | 0.176 | 0.808 | ** | Satellization |
| Oaxaca | 0.176 | 0.791 | ** | Satellization |
| Tlaxcala | 0.147 | 0.600 | * | Satellization |
| Puebla | 0.116 | 0.653 | * | Satellization |
| **Querétaro** | **-0.155** | **0.782** | **\*\*** | **Leapfrog** |
| **Nuevo León** | **-0.058** | **0.935** | **\*\*\*** | **Convergence** |

---

## Citation

```
Zainos Corona, E. (2026). Shadow Node Theory v2.0: Scale Invariance in the Node 
Satellization Algorithm — Triple Resolution Model. Fractal Core Research Pre-print v2.0. 
SSRN: https://ssrn.com/abstract=6418778
Zenodo: https://doi.org/10.5281/zenodo.19027089
```

BibTeX:
```bibtex
@misc{zainos2026shadowv2,
  author    = {Zainos Corona, Elan},
  title     = {Shadow Node Theory v2.0: Scale Invariance in the Node
               Satellization Algorithm — Triple Resolution Model},
  year      = {2026},
  publisher = {SSRN / Zenodo},
  note      = {Pre-print v2.0},
  doi       = {10.5281/zenodo.19027089},
  url       = {https://ssrn.com/abstract=6418778}
}
```

---

## License

**Code:** MIT License  
**Data:** CC BY 4.0 for derived datasets  
**Paper:** CC BY-NC 4.0

---

## Contact

Elan Zainos Corona — Fractal Core Research — Tlaxcala, Mexico  
GitHub: Inzainos

---

*"El algoritmo de satelizacion es predecible. La taxonomia de fallos del leapfrog es conocida. Lo que sigue es una decision que ningun modelo puede tomar por el nodo."*  
*— Shadow Node Theory v2.0, Conclusiones*
