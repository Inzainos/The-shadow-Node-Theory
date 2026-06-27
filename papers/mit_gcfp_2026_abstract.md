# MIT GCFP 13th Annual Conference — Submission Materials

**Conference:** Financial Regulation in an Era of Innovation and Disruption
**Dates:** October 29–30, 2026 — Cambridge, MA
**Submission deadline:** July 17, 2026
**Submit to:** deirdre@mit.edu — subject line: `GCFP 13th Annual Conference Submission`

---

## Working Title

**Orbital Collapse Architecture: A Power-Law Model of Institutional
Absorption Following Systemic Financial Failure**

*(A focused financial-stability application of Shadow Node Theory)*

---

## Abstract (≈250 words)

When a dominant financial institution fails, its assets, counterparties, and
market position do not dissolve — they are *absorbed* by an identifiable
successor, and the speed of that absorption is empirically regular. We model
the post-failure dominance ratio R(t) = mass_absorber(t) / mass_collapsed_peak
as a power law, R(t) = a·t^b, where the exponent **b** measures the velocity
of institutional absorption following functional extinction of the failed hub.

Applying this Orbital Collapse Architecture (ACO) framework to the six
canonical absorptions of the 2008–2009 crisis — Lehman Brothers → Barclays +
JPMorgan, Bear Stearns → JPMorgan, Washington Mutual → JPMorgan (FDIC),
Wachovia → Wells Fargo, Merrill Lynch → Bank of America, and Chrysler → Fiat +
US Treasury — we recover statistically significant power-law absorption curves
in every case (R² = 0.85–0.99, all p < 0.01), reconstructed entirely from
primary sources (SEC EDGAR, Federal Reserve Flow of Funds, FDIC, SIGTARP, the
Valukas Examiner Report).

The central regulatory finding is that **institutional friction governs
absorption velocity**: abrupt, disorderly failures (Lehman) and
regulator-brokered resolutions (WaMu, FDIC) produce distinct absorption
signatures, and the framework distinguishes genuine absorption from
obsolescence-without-capture. These signatures offer a quantitative,
falsifiable lens on "too-big-to-fail" concentration dynamics and on how
resolution policy shapes the speed and concentration of post-crisis market
restructuring — directly relevant to financial-stability risk and the design
of orderly-resolution regimes.

The financial corpus is a domain-specific extract of a larger 721-case,
cross-domain validation of the underlying satellization model, ensuring the
mechanism is not financial-sector-specific but a general feature of coupled
dominance dynamics.

---

## Why this fits the GCFP theme

- **Financial-stability risk:** quantifies post-failure concentration (the
  too-big-to-fail consolidation that followed 2008).
- **Market structure / resolution policy:** absorption velocity (b) is shaped
  by whether a failure is disorderly vs. regulator-brokered — a direct
  policy lever.
- **Empirical + reproducible:** every case is traceable to SEC/FDIC/Fed/SIGTARP
  primary records; nothing synthetic.

## Six financial cases (primary-source, v2.4.0)

| Hub → Absorber | Trigger | b | R² | p |
|----------------|---------|------|------|------|
| Lehman Brothers → Barclays + JPMorgan | abrupt (2008) | +0.246 | 0.892 | <0.001 |
| Bear Stearns → JPMorgan | abrupt (2008) | +0.043 | 0.926 | 0.002 |
| Washington Mutual → JPMorgan (FDIC) | abrupt (2008) | +0.009 | 0.946 | 0.001 |
| Wachovia → Wells Fargo | abrupt (2008) | +0.153 | 0.892 | 0.004 |
| Merrill Lynch → Bank of America | abrupt (2008) | +0.217 | 0.846 | 0.005 |
| Chrysler → Fiat + US Treasury (TARP) | abrupt (2009) | +0.138 | 0.990 | <0.001 |

Reproduced via `reconstruction_real/code/build_aco_v29.py`.

---

## Notes for the full paper (to expand before submission)

1. Frame R(t) explicitly in resolution-policy terms: orderly (FDIC-brokered,
   purchase-and-assumption) vs. disorderly (bankruptcy) absorption.
2. Add a short comparison to the friction-vs-b finding from the full corpus
   (Spearman rho = -0.68) to show the financial cases are one slice of a
   general law.
3. Add the RC-ACO falsification criteria as the paper's robustness section.
4. Position against the too-big-to-fail / concentration literature
   (e.g., FCIC 2011; Sorkin 2009; Acharya et al.).
