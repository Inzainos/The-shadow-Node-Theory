# MIT GCFP 13th Annual Conference — Submission Materials

**Conference:** Financial Regulation in an Era of Innovation and Disruption
**Dates:** October 29–30, 2026 — Cambridge, MA
**Submission deadline:** July 17, 2026
**Submit to:** deirdre@mit.edu — subject line: `GCFP 13th Annual Conference Submission`

---

## Working Title

**Orbital Collapse Architecture: Institutional Friction as the Regulator of Systemic Collapse**

*(A power-law framework applied to finance, technology, industry, and history)*

---

## Abstract (≈250 words)

When a dominant institution fails, its assets and market position are not destroyed — they are absorbed by an identifiable successor, and both the speed and the shape of that absorption are empirically regular. We model the post-failure dominance ratio A(τ) = mass_absorber(τ) / mass_collapsed_peak as a power law, A(τ) = c·τ^Δ, on a clock τ that starts at functional extinction, and treat the exponent Δ as a collapse coordinate orthogonal to the satellization exponent b.

Applied to 18 ACO cases across four institutional domains — six canonical absorptions of the 2008–2009 financial crisis, four technology-sector collapses, four industrial-era failures, and four historical imperial absorptions — the framework recovers statistically significant power-law absorption in 17 of 18 cases (R² = 0.77–0.99), reconstructed entirely from verifiable primary sources (SEC EDGAR, FDIC, Fed Flow of Funds, SIGTARP, Valukas Report, IDC, Maddison Project Database 2023).

The central regulatory finding is that **institutional friction governs absorption shape, not just speed**: regulator-brokered resolutions (WaMu, FDIC receivership) and enterprise mergers under legal scaffolding (Compaq→HP) produce low-Δ, smooth power-law absorption, while the disorderly bankruptcy (Lehman) and platform-era absorptions with distributed acquirers (Nokia, MySpace) produce higher Δ. The decisive contrast is the frictionless crypto domain: LUNA collapses as a catastrophic cliff (super-exponential), FTX/FTT as a floor-arrested power law, and EOS as erratic fragmentation — none of them the orderly power law that regulated failures exhibit.

The framework offers a compact, falsifiable instrument for assessing whether resolution machinery delivers orderly transfers — and a structural argument for why frictionless venues fail catastrophically rather than gracefully.

---

## Why this fits the GCFP theme

- **Financial stability risk:** quantifies post-failure concentration (the too-big-to-fail consolidation that followed 2008).
- **Resolution policy:** absorption shape (Δ, R²) is an ex post diagnostic of whether Title II / FDIC single-point-of-entry delivered its promise.
- **Cross-sector extension:** technology and industrial collapses show the same structure holds outside finance, extending policy relevance to platform markets.
- **Empirical + reproducible:** all 18 cases traceable to primary records; nothing synthetic.

## Full ACO corpus (primary-source, v2.5.0)

### Finance (F)

| Hub → Absorber | Trigger | Δ | R² | p |
|---|---|---|---|---|
| Washington Mutual → JPMorgan (FDIC) | Abrupt (2008) | +0.009 | 0.946 | 0.001 |
| Bear Stearns → JPMorgan | Abrupt (2008) | +0.043 | 0.926 | 0.002 |
| Chrysler → Fiat + US Treasury | Abrupt (2009) | +0.138 | 0.990 | <0.001 |
| Wachovia → Wells Fargo | Abrupt (2008) | +0.153 | 0.892 | 0.004 |
| Merrill Lynch → Bank of America | Abrupt (2008) | +0.217 | 0.846 | 0.005 |
| Lehman Brothers → Barclays + JPMorgan | Abrupt (2008) | +0.246 | 0.892 | 0.001 |

### Technology (T)

| Hub → Absorber | Trigger | Δ | R² | p |
|---|---|---|---|---|
| Compaq → Hewlett-Packard | Gradual (2001) | +0.153 | 0.991 | <0.001 |
| Sun Microsystems → Oracle | Gradual (2009) | +0.208 | 0.919 | 0.009 |
| Nokia (mobile) → Microsoft ecosystem | Gradual (2007) | +1.814 | 0.819 | <0.001 |
| MySpace → Facebook | Gradual (2008) | +2.195 | 0.906 | 0.003 |

### Industrial (I)

| Hub → Absorber | Trigger | Δ | R² | p |
|---|---|---|---|---|
| Pan Am → Delta + United | Gradual (1991) | +0.362 | 0.835 | 0.020 |
| Polaroid → One Equity Partners | Gradual (2001) | +0.412 | 0.934 | 0.007 |
| Kodak (film) → Patent consortium | Gradual (2000) | +1.244 | 0.971 | <0.001 |
| Blockbuster → Dish Network | Gradual (2004) | +1.806 | 0.954 | 0.001 |

### History (H) — *est. = historiographic estimate*

| Hub → Absorber | Trigger | Δ | R² | p |
|---|---|---|---|---|
| Cartago → República Romana | Abrupt (−149) | +0.336 | 0.993 | <0.001 |
| URSS → Rusia | Abrupt (1991) | +0.349 | 0.773 | 0.080 (n.s.) |
| W. Roman Empire → Byzantium | Gradual (376) | +0.453 | 0.916 | <0.001 |
| Aztec Empire → Castile | Abrupt (1519) | +0.693 | 0.992 | <0.001 |

Reproduced via `reconstruction_real/data/snt_corpus_aco_v29.csv` and `reconstruction_real/data/collapse_multidomain_v29.csv`.
