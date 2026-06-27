# Orbital Collapse Architecture: A Power-Law Model of Institutional Absorption Following Systemic Financial Failure

**Elán Zainos Corona**
Fractal Core Research, Tlaxcala, Mexico
ORCID: 0009-0009-9125-253X · elan.zainos.corona@gmail.com

*Prepared for the MIT Golub Center for Finance and Policy (GCFP) 13th Annual
Conference — "Financial Regulation in an Era of Innovation and Disruption,"
October 29–30, 2026.*

*Working paper — preliminary draft. Data and code:
github.com/Inzainos/The-shadow-Node-Theory*

---

## Abstract

When a dominant financial institution fails, its assets, counterparties, and
market position are not destroyed — they are *absorbed* by an identifiable
successor, and the speed of that absorption is empirically regular. We model
the post-failure dominance ratio R(t) = mass_absorber(t) / mass_collapsed_peak
as a power law, R(t) = a·t^b, and interpret the exponent **b** as the velocity
of institutional absorption following functional extinction of a failed hub.
Applying this *Orbital Collapse Architecture* (ACO) framework to the six
canonical absorptions of the 2008–2009 crisis — Lehman Brothers, Bear Stearns,
Washington Mutual, Wachovia, Merrill Lynch, and Chrysler — we recover
statistically significant power-law absorption curves in every case
(R² = 0.85–0.99, all p < 0.01), reconstructed entirely from primary sources.
The central regulatory observation is that **the resolution regime is legible
in the absorption exponent**: regulator-brokered resolutions (Washington
Mutual via FDIC, Bear Stearns via the Federal Reserve) exhibit near-instant
absorption (b → 0), whereas the single disorderly bankruptcy in the sample
(Lehman Brothers) shows the slowest, most drawn-out absorption (highest b).
We position these absorption signatures as a quantitative, falsifiable lens on
too-big-to-fail concentration and on how resolution policy shapes the speed and
concentration of post-crisis market restructuring.

---

## 1. Introduction

The 2008–2009 financial crisis produced a wave of institutional failures whose
common structural feature has been under-theorized: in nearly every case, a
failing institution's balance sheet, client relationships, and market position
did not evaporate but were *captured* by an identifiable successor. Bear
Stearns became part of JPMorgan; Merrill Lynch became part of Bank of America;
Washington Mutual's banking operations passed, within 48 hours, to JPMorgan
under FDIC receivership. The crisis was, in large part, an episode of
accelerated **concentration** — the very dynamic that "too-big-to-fail"
regulation is meant to constrain.

This paper asks a simple quantitative question: *how fast* does absorption
happen, and *what governs that speed*? We argue that the post-failure dominance
ratio between absorber and absorbed follows a power law, and that the fitted
exponent carries policy-relevant information about the resolution regime under
which the failure was processed.

The framework is a financial-sector application of a more general model —
Shadow Node Theory (SNT) — which characterizes how dominance evolves between a
coupled "hub" and "node" across domains as diverse as demography, epidemiology,
and astronomy. The financial cases analyzed here are one domain-specific slice
of a larger 721-case cross-domain validation, which we draw on only to
establish that the mechanism is not financial-sector-specific.

## 2. Model

Let the absorber's captured mass at time *t* after the trigger event be
M_A(t), and let the failed institution's peak pre-failure mass be M_C. Define
the **absorption ratio**

> R(t) = M_A(t) / M_C.

We posit that R(t) follows a power law in time since the trigger,

> **R(t) = a · t^b**,    (Eq. 1)

estimated by ordinary least squares on log-transformed axes,
log R = log a + b · log t. The exponent **b** is the object of interest:

- **b → 0**: near-instantaneous absorption — the successor captures the bulk
  of the mass almost immediately, then plateaus. Characteristic of brokered or
  pre-arranged resolutions.
- **moderate b > 0**: gradual absorption — the successor accretes mass over an
  extended window, consistent with contested, market-driven, or
  litigation-encumbered transfers.

"Mass" is operationalized per case by the most defensible primary-source
quantity (assets under the successor's control, market capitalization, market
share, or government-injected capital); see Section 3 and the appendix table.

**The ACO criterion (definitional).** A case qualifies as Orbital Collapse
Architecture only if both (1) the hub undergoes *functional extinction* and
(2) its resources are absorbed by a *specific, identifiable* node. Failures
that dissolve without capture (e.g., outright liquidation) are excluded; this
distinguishes ACO from generic decline.

## 3. Data

All six cases are reconstructed from primary regulatory and corporate records:
SEC EDGAR filings (8-K, S-4, 10-K), the Federal Reserve Flow of Funds, FDIC
failure and acquisition records, SIGTARP reports, the U.S. Treasury TARP
tracker, and the Valukas Lehman Examiner Report. No values are synthetic.
Time series are reconstructed at monthly resolution from the trigger event
(the failure or forced-sale date) forward.

The six cases:

| # | Hub → Absorber | Resolution channel | Trigger |
|---|----------------|--------------------|---------|
| 1 | Lehman Brothers → Barclays + JPMorgan | Disorderly bankruptcy (Chapter 11) | Sep 2008 |
| 2 | Bear Stearns → JPMorgan | Fed-brokered (Maiden Lane) | Mar 2008 |
| 3 | Washington Mutual → JPMorgan | FDIC receivership (P&A) | Sep 2008 |
| 4 | Wachovia → Wells Fargo | Open-bank, FDIC-adjacent | Oct 2008 |
| 5 | Merrill Lynch → Bank of America | Negotiated merger | Sep 2008 |
| 6 | Chrysler → Fiat + US Treasury | Government-managed (TARP/§363) | Apr–Jun 2009 |

## 4. Results

Every case yields a statistically significant power-law absorption curve.

| Hub → Absorber | b | R² | p | n |
|----------------|------|------|--------|---|
| Washington Mutual → JPMorgan (FDIC) | +0.009 | 0.946 | 0.001 | 6 |
| Bear Stearns → JPMorgan (Fed) | +0.043 | 0.926 | 0.002 | 6 |
| Chrysler → Fiat + Treasury | +0.138 | 0.990 | <0.001 | 6 |
| Wachovia → Wells Fargo | +0.153 | 0.892 | 0.004 | 6 |
| Merrill Lynch → Bank of America | +0.217 | 0.846 | 0.005 | 6 |
| Lehman Brothers → Barclays + JPMorgan | +0.246 | 0.892 | <0.001 | 7 |

Reproduced via `reconstruction_real/code/build_aco_v29.py`.

**The ordering is the finding.** Ranked by absorption velocity, the sequence
tracks the *degree of regulatory pre-arrangement* of each resolution:

- The two fastest absorptions (lowest b) are the two most actively brokered
  failures: **Washington Mutual** (b = 0.009), resolved by the FDIC in a
  purchase-and-assumption completed within 48 hours, and **Bear Stearns**
  (b = 0.043), resolved through a Federal Reserve–backed sale to JPMorgan.
  In both, the successor was effectively pre-selected and the transfer
  near-instantaneous.
- The slowest absorption (highest b) is **Lehman Brothers** (b = 0.246), the
  one failure allowed to proceed as a disorderly bankruptcy. Its assets were
  carved up and absorbed only gradually (Barclays' North American operations,
  then a long bankruptcy-administered wind-down).
- Government-managed and negotiated-merger cases (Chrysler, Wachovia, Merrill)
  fall in between.

In other words, **the absorption exponent is a readout of resolution policy**:
the more orderly and pre-arranged the resolution, the closer b is to zero
(instantaneous capture); the more disorderly the failure, the larger b
(protracted, piecemeal absorption).

## 5. Discussion — regulatory implications

**5.1 A quantitative signature of "too-big-to-fail" consolidation.** Each curve
documents mass flowing *toward* an already-large successor (JPMorgan absorbed
both Bear Stearns and Washington Mutual; Bank of America absorbed Merrill).
The ACO framework gives a single number — b — summarizing how quickly that
concentration completed. This complements concentration metrics (e.g.,
deposit-share HHI) by adding a *temporal* dimension: not just how much
consolidation, but how fast.

**5.2 Resolution design is legible after the fact — and potentially ex ante.**
If absorption velocity reflects the resolution channel, then b is a candidate
*ex post* diagnostic for evaluating whether orderly-resolution mechanisms
(e.g., Title II of Dodd-Frank, FDIC single-point-of-entry) achieve their stated
aim of rapid, predictable transfer. A well-functioning orderly-resolution
regime should, on this logic, produce low-b absorptions; a regime that lets
failures become disorderly should produce high-b, drawn-out ones.

**5.3 Genuine absorption vs. obsolescence-without-capture.** The ACO criterion
deliberately excludes failures where no successor captures the mass. This
distinction matters for regulators: a firm that is *absorbed* transmits its
risk and relationships into the successor (raising concentration and
interconnectedness), whereas a firm that is merely *made obsolete* does not.
The framework provides an empirical test for which is occurring.

## 6. Robustness and falsifiability

The model is stated to be refutable. We pre-commit to three refutation
conditions (RC-ACO):

- **RC-ACO-1**: the framework is refuted for a case if the absorber's mass
  does not increase post-absorption (R does not grow).
- **RC-ACO-2**: refuted if absorption velocity (b) shows no systematic
  relationship to resolution channel across an expanded sample.
- **RC-ACO-3**: refuted if a vestigial-successor pattern (a heir institution
  recovering R > 1 over the long run) fails to appear where the mechanism
  predicts it.

**Generality.** The financial cases are one domain of a 721-case corpus in
which institutional *friction* is the dominant predictor of the satellization
exponent (Spearman ρ = −0.68, p = 2.5×10⁻⁹⁷, n = 714). That friction–velocity
relationship is the cross-domain analogue of the resolution-channel ordering
documented here: more institutional friction (here, more regulatory
intervention) slows the dominance dynamic. The financial results are therefore
not an isolated curve-fit but a sectoral instance of a general pattern.

## 7. Limitations

This is a preliminary draft. (i) The sample is six cases; the
resolution-channel ordering is descriptive, not yet a powered statistical
test. (ii) Each R(t) series is reconstructed at coarse (monthly) resolution and
the "mass" proxy varies by case; we report per-case sources and invite
scrutiny. (iii) Absorption curves are sensitive to the choice of trigger date.
A full paper will (a) expand the sample to additional resolution episodes
(S&L era, European 2011–2012, regional-bank failures of 2023), (b) formalize
the resolution-channel variable and test b against it, and (c) add explicit
comparison to the too-big-to-fail and orderly-resolution literatures.

## 8. Conclusion

Institutional failure in finance is, structurally, a transfer of dominance to
an identifiable successor at an empirically regular rate. That rate — the
absorption exponent b — is legible, reproducible from primary sources, and
appears to encode the resolution regime under which a failure was processed.
For a conference on financial regulation in an era of disruption, ACO offers a
compact, falsifiable instrument for asking whether our resolution machinery
actually delivers the orderly, rapid transfers it promises.

---

## Appendix — data sources by case

- **Lehman Brothers**: Valukas A.R. (2010), *Lehman Brothers Holdings Inc.
  Chapter 11 Examiner Report*, U.S. Bankruptcy Court SDNY; Federal Reserve Flow
  of Funds 2008–2013; SEC EDGAR 10-K filings, Barclays and JPMorgan 2008–2009.
- **Bear Stearns**: Federal Reserve Bank of New York (2008), Bear Stearns /
  Maiden Lane transaction; SEC Form 8-K, JPMorgan Chase, March 2008;
  Sorkin A.R. (2009), *Too Big To Fail*.
- **Washington Mutual**: FDIC (2008), WaMu failure and acquisition press
  release, Sep 25 2008; JPMorgan Chase Form 8-K, Sep 2008; FDIC Failed Bank
  List.
- **Wachovia**: SEC Form 8-K, Wells Fargo, Oct 2008; FDIC statement, Oct 3
  2008; Wessel D. (2009), *In Fed We Trust*.
- **Merrill Lynch**: SEC Form S-4, Bank of America, Dec 2008 (Merrill merger
  proxy); BofA 10-K 2009; Lewis K. testimony to the FCIC (2010).
- **Chrysler**: SIGTARP (2012), Chrysler Bailout Report; Chrysler Group LLC
  10-K 2010; U.S. Treasury TARP tracker; Rattner S. (2010), *Overhaul*.

*Full corpus, code, and reproduction instructions:
github.com/Inzainos/The-shadow-Node-Theory*
