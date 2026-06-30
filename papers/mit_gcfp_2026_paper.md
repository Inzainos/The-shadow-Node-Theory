# Orbital Collapse Architecture: Institutional Friction as the Regulator of Systemic Collapse

**Evidence from the 2008 crisis and seven empirical domains**

Elán Zainos Corona — Fractal Core Research, Tlaxcala, Mexico
ORCID 0009-0009-9125-253X · elan.zainos.corona@gmail.com

*Prepared for the MIT Golub Center for Finance and Policy (GCFP) 13th Annual Conference — "Financial Regulation in an Era of Innovation and Disruption," October 29–30, 2026. Working paper — preliminary draft. Data and code: github.com/Inzainos/The-shadow-Node-Theory*

---

## Abstract

When a dominant institution fails, its assets and market position are not destroyed — they are **absorbed** by an identifiable successor, and both the speed *and the shape* of that absorption are empirically regular. We model the post-failure dominance ratio A(τ) = mass_absorber(τ) / mass_collapsed_peak as a power law, A(τ) = c·τ^Δ, on a clock τ that starts at functional extinction, and treat the exponent **Δ** as a collapse coordinate orthogonal to the satellization exponent b.

Applied to 18 ACO cases across four institutional domains — six canonical absorptions of the 2008–2009 financial crisis, four technology-sector collapses, four industrial-era failures, and four historical imperial absorptions — the framework recovers statistically significant power-law absorption in 17 of 18 cases (R² = 0.77–0.99, all significant p < 0.05), reconstructed entirely from verifiable primary sources. The ordering of Δ tracks the **resolution channel and friction level** across all domains: regulator-brokered failures produce low-Δ, high-R² absorption, while disorderly or frictionless collapses produce high-Δ or erratic signatures.

Our central claim is sharper than speed: **institutional friction does not merely slow collapse — it *regularizes its shape* into a smooth power law.** The decisive contrast is the **frictionless** domain of crypto-assets: LUNA collapses as a *catastrophic cliff* (super-exponential, 5.6 orders of magnitude in 11 days), FTX/FTT as a *floor-arrested* power law, and EOS as *erratic fragmentation* — none of them the orderly power law that regulated failures exhibit. Astrophysical collapse (a solar flare, R²=0.975; a tidal disruption event, ~t^−5/3) and a biological succession (Delta→Omicron) confirm the generality of the form.

We organize these into a five-mode taxonomy governed by **friction × trigger × (floor/ceiling)**, unified by a **Principle of Least Friction**. The policy implication is direct: **orderly resolution machinery is what buys a power-law decay instead of a cliff** — and frictionless venues are structurally prone to catastrophic, not graceful, failure.

---

## 1. Introduction

The 2008–2009 crisis was, structurally, an episode of accelerated **concentration**: failing institutions did not vanish, their balance sheets and franchises were captured by identifiable successors. JPMorgan absorbed both Bear Stearns and Washington Mutual; Bank of America absorbed Merrill Lynch. This is precisely the dynamic too-big-to-fail regulation aims to constrain.

We ask two quantitative questions: *how fast* does post-failure absorption happen, and — more importantly — *what governs its shape*? We show that absorption follows a power law whose exponent and **regularity** encode the institutional environment in which the failure was processed.

This pattern is not unique to finance. The same structure appears in technology-sector collapses (Nokia absorbed by Microsoft's ecosystem, Blockbuster by Dish Network, Kodak's film division by a patent consortium, MySpace by Facebook), in industrial-era failures (Pan Am, Polaroid), and across centuries of historical imperial absorption (the Western Roman Empire, the USSR, the Aztec Empire, Carthage). Across all 18 cases, the mechanism is the same: **institutional friction regularizes the collapse shape; its absence produces catastrophic or erratic failure.** The financial cases are one slice of a broader program (Shadow Node Theory, SNT) that finds the same structure across 721 empirical cases.

---

## 2. Model

A system carries two orthogonal coordinates:

- **Satellization b:** R(t) = m_hub(t)/m_node(t) = a·t^b — how dominance evolves while the coupled relationship runs.
- **Collapse Δ:** A(τ) = c·τ^Δ, with A = m_absorber(τ)/m_collapsed_peak and τ = time since **functional extinction**.

Δ is fit by OLS on log–log axes. **b ⊥ Δ** is a falsifiable claim: collapse can strike at any point of a satellization trajectory, so it is an orthogonal axis, not a terminal stage.

**ACO criterion (definitional):** a case qualifies as Orbital Collapse only if (1) the hub undergoes functional extinction and (2) its mass is absorbed by a specific, identifiable successor. Failures that dissolve without capture are excluded.

---

## 3. Data

The corpus comprises **18 ACO cases** across four institutional domains, all reconstructed from verifiable primary sources with no synthetic values:

- **Finance (F, n=6):** SEC EDGAR (8-K, S-4, 10-K), Federal Reserve Flow of Funds, FDIC failure/acquisition records, SIGTARP, U.S. Treasury TARP tracker, Valukas Lehman Examiner Report. Monthly resolution from trigger date.
- **Technology (T, n=4):** IDC Worldwide Quarterly Mobile Phone Tracker, Gartner Mobile Phone Sales, Comscore Media Metrix, SEC EDGAR corporate 10-K filings. Annual series.
- **Industrial (I, n=4):** U.S. DOT Air Carrier Financial Reports, SEC EDGAR Chapter 11 filings, IDC Digital Camera Market Share, Dish Network Form 8-K. Annual series.
- **History (H, n=4):** Maddison Project Database 2023 (Bolt & van Zanden); Bakewell (1984), Ward-Perkins (2005), Wickham (2005), Lazenby (1996). Decadal series; 3 of 4 cases rely on historiographic estimates and are flagged accordingly.

Cross-domain contrast data: Yahoo Finance (crypto), CoV-Spectrum/LAPIS (variant genomics), NOAA SWPC GOES (solar X-ray), NASA IRSA/ZTF (tidal disruption photometry).

---

## 4. Results

### 4.1 The 2008 financial cohort: the resolution channel is legible in Δ

Every case yields a significant power-law absorption. Ranked by absorption speed (Δ):

| Hub → Absorber | Resolution channel | Δ | R² | p |
|---|---|---|---|---|
| Washington Mutual → JPMorgan | FDIC receivership (P&A) | +0.009 | 0.946 | 0.001 |
| Bear Stearns → JPMorgan | Fed-brokered (Maiden Lane) | +0.043 | 0.926 | 0.002 |
| Chrysler → Fiat + US Treasury | Government-managed (TARP) | +0.138 | 0.990 | <0.001 |
| Wachovia → Wells Fargo | Open-bank, FDIC-adjacent | +0.153 | 0.892 | 0.004 |
| Merrill Lynch → Bank of America | Negotiated merger | +0.217 | 0.846 | 0.005 |
| Lehman Brothers → Barclays + JPMorgan | Disorderly bankruptcy | +0.246 | 0.892 | 0.001 |

The two fastest absorptions are the two most actively brokered failures; the slowest is the one allowed to proceed as a disorderly bankruptcy. All six fit a smooth power law (R² = 0.85–0.99) — the signature of regulated orbital decay.

### 4.2 Technology collapses: platform-era absorption

Four technology-sector collapses extend the ACO corpus into the digital economy:

| Hub → Absorber | Trigger | Δ | R² | p |
|---|---|---|---|---|
| Compaq → Hewlett-Packard | Gradual (2001) | +0.153 | 0.991 | <0.001 |
| Sun Microsystems → Oracle | Gradual (2009) | +0.208 | 0.919 | 0.009 |
| Nokia (mobile) → Microsoft ecosystem | Gradual (2007) | +1.814 | 0.819 | <0.001 |
| MySpace → Facebook | Gradual (2008) | +2.195 | 0.906 | 0.003 |

The two enterprise absorptions (Compaq, Sun) — where regulatory and contractual friction governed the transfer — yield low-Δ, high-R² signatures identical in character to the regulated financial collapses. The two platform-era absorptions (Nokia, MySpace) — where the "mass" transferred was audience attention with no regulatory scaffolding — yield superlinear Δ > 1, consistent with accelerating absorption in a low-friction environment.

### 4.3 Industrial collapses: gradual dissolution under moderate friction

| Hub → Absorber | Trigger | Δ | R² | p |
|---|---|---|---|---|
| Pan Am → Delta + United | Gradual (1991) | +0.362 | 0.835 | 0.020 |
| Polaroid → One Equity Partners | Gradual (2001) | +0.412 | 0.934 | 0.007 |
| Kodak (film) → Patent consortium | Gradual (2000) | +1.244 | 0.971 | <0.001 |
| Blockbuster → Dish Network | Gradual (2004) | +1.806 | 0.954 | 0.001 |

Pan Am and Polaroid — absorbed under bankruptcy court supervision with identifiable acquirers — sit in the moderate-Δ range. Kodak and Blockbuster — where the absorber was a distributed consortium rather than a single regulated entity — yield superlinear Δ, consistent with less structured resolution.

### 4.4 Historical imperial absorptions: centuries-long orbital decay

| Hub → Absorber | Trigger | Δ | R² | p | Note |
|---|---|---|---|---|---|
| Cartago → República Romana | Abrupt (−149) | +0.336 | 0.993 | <0.001 | est. |
| URSS → Rusia | Abrupt (1991) | +0.349 | 0.773 | 0.080 | n.s. |
| W. Roman Empire → Byzantium | Gradual (376) | +0.453 | 0.916 | <0.001 | est. |
| Aztec Empire → Castile | Abrupt (1519) | +0.693 | 0.992 | <0.001 | est. |

Three of four are statistically significant. The USSR case is not significant (n=5, p=0.080), likely a consequence of the short post-collapse measurement window available in the Maddison data; it is reported for completeness. The three significant historical cases all yield smooth power laws (R² = 0.92–0.99), consistent with the regulated regime — here the "friction" is the institutional weight of the absorbing civilization rather than modern resolution law.

### 4.5 The frictionless counterexamples (the regulatory payoff)

What does collapse look like with **no** institutional friction? Crypto-assets provide the natural experiment:

| Case (friction ≈ 0) | Trigger | Floor? | Mode | Signature |
|---|---|---|---|---|
| **LUNA / Terra** (May 2022) | Abrupt | None | **Catastrophic Cliff** | Super-exponential; 5.6 OOM in 11 days |
| **FTX / FTT** (Nov 2022) | Abrupt | Floor ~$1 | **Floor-Arrested** | Power-law to residual floor (R²=0.875) |
| **EOS** (2018–) | Gradual | None | **Cracquelure** | Erratic fragmentation (R²=0.10–0.70) |

None of these is the orderly power law of regulated failure. **Without institutional friction, collapse is catastrophic, arrested, or erratic — never graceful.**

### 4.6 Cross-domain universality of the form

The smooth-power-law (regulated) mode also appears where the regulating "friction" is *physical*: a GOES M6.9 solar flare decays as a power law (R²=0.975; radiative/conductive cooling); the tidal disruption event AT2019qiz (a star accreted by a black hole) decays as ~t^−5/3 (R²=0.84), with disk viscosity as the literal friction. A bounded biological succession (Delta→Omicron, South Africa) is a fast logistic sweep (k=0.218/day). The mechanism is not finance-specific.

---

## 5. Taxonomy and unifying principle

**Five modes, governed by friction × trigger × (floor/ceiling):**

| Mode | Condition | Shape | Examples |
|---|---|---|---|
| Regulated Orbital Decay | High friction (any trigger) | Smooth power law | All 6 financial; Compaq, Sun; Cartago, Roma |
| Superlinear Absorption | Low-moderate friction + platform/distributed absorber | Power law, Δ > 1 | Nokia, MySpace, Kodak, Blockbuster |
| Cracquelure Decay | Friction ≈ 0 + gradual | Erratic fragmentation | EOS |
| Floor-Arrested | Friction ≈ 0 + abrupt + floor | Power law to residual floor | FTX/FTT |
| Catastrophic Cliff | Friction ≈ 0 + abrupt + no floor | Super-exponential | LUNA/Terra |

**Principle of Least Friction.** Collapse follows the trajectory that minimizes integrated friction — gradient flow on a stability landscape. The geometry of the friction field (× trigger × floor) selects which mode emerges. The stability-landscape picture connects SNT to catastrophe theory, the Waddington landscape, ecological resilience (Holling), and climate tipping points.

---

## 6. Regulatory implications

1. **Orderly resolution buys power-law decay instead of a cliff.** Δ and R² of absorption are an *ex post* diagnostic of whether resolution machinery (Title II, FDIC single-point-of-entry) delivered the rapid, predictable transfer it promises. Low-Δ, high-R² = the regime worked; cliffs or erratic fragmentation = it did not, or was absent.

2. **The technology and industrial cases extend the policy horizon.** Nokia and Blockbuster — with superlinear Δ — show that even non-financial collapses with distributed absorbers and no regulatory scaffolding exhibit the hallmarks of low-friction failure. This is relevant for competition policy and for thinking about what "orderly failure" means in platform markets.

3. **Frictionless venues are structurally cliff-prone.** The 2022 crypto collapses are not anomalies — they are what the model predicts for abrupt failure with no institutional friction and no value floor. This is a financial-stability argument for extending resolution-style friction (circuit breakers, disclosure, capital/withdrawal gates) to crypto and shadow-banking venues.

4. **A temporal dimension for too-big-to-fail.** Δ quantifies *how fast* concentration completes after a failure, complementing static concentration metrics.

---

## 7. Falsifiability

- **RC-Δ1 (orthogonality):** refuted if corr(b, Δ) ≫ 0 across systems with both coordinates.
- **RC-Δ2 (least friction):** refuted if a realized collapse takes a higher-friction path when a lower-friction one was available.
- **RC-Δ3 (absorption):** refuted if the absorber's mass does not grow post-absorption.
- **RC-Δ4 (regularization):** refuted if frictionless collapses fit a power law as well as regulated ones.

---

## 8. Limitations

This is a preliminary draft. Findings are **correlational**: the domains differ in more than friction (timescale, the meaning of "mass", microstructure). The historical cases (H) rely partly on historiographic estimates and are flagged as such; the USSR case is not statistically significant. The crypto sample is small (n≈3) and LUNA/the solar flare are collapse-*shape* evidence, not ACO absorptions with a single absorber. The TDE exponent (−1.07) is shallower than the canonical −5/3 (g-band, imperfect host subtraction). "Time to 90%" is threshold-dependent, though the abrupt<gradual ordering is robust to 0.5/0.9/0.95. A full version will operationalize "friction along a path", expand cases per mode, and test orthogonality directly.

---

## 9. Conclusion

Institutional failure is a transfer of dominance to an identifiable successor at an empirically regular rate and shape. Across 18 ACO cases spanning finance, technology, industry, and history — and in contrast to three frictionless crypto collapses — that shape encodes the resolution regime. The decisive, policy-relevant finding is that **institutional friction is what makes collapse follow an orderly power law; remove it and failure becomes a catastrophic cliff.** For a conference on financial regulation in an era of disruption, this offers a compact, falsifiable instrument for asking whether our resolution machinery delivers orderly transfers — and a structural argument for why frictionless venues fail catastrophically rather than gracefully.

---

## Appendix — Data sources by case

**Finance**
- **Lehman Brothers:** Valukas A.R. (2010), Examiner Report, SDNY; Fed Flow of Funds 2008–2013; SEC EDGAR 10-K Barclays & JPMorgan.
- **Bear Stearns:** FRBNY (2008), Maiden Lane; SEC 8-K JPMorgan Mar 2008; Sorkin A.R. (2009). *Too Big To Fail*. Viking Press.
- **Washington Mutual:** FDIC (2008), Sep 25 release; JPMorgan 8-K Sep 2008; FDIC Failed Bank List.
- **Wachovia:** SEC 8-K Wells Fargo Oct 2008; FDIC statement Oct 3 2008; Wessel D. (2009). *In Fed We Trust*. Crown Business.
- **Merrill Lynch:** SEC S-4 BofA Dec 2008; BofA 10-K 2009; Lewis K. testimony to the FCIC (2010).
- **Chrysler:** SIGTARP (2012); Chrysler Group 10-K 2010; US Treasury TARP tracker; Rattner S. (2010). *Overhaul*. Houghton Mifflin.

**Technology**
- **Nokia:** IDC Worldwide Quarterly Mobile Phone Tracker Q4 2007–2016; Gartner Mobile Phone Sales 2007–2016; Microsoft Form 10-K 2014.
- **Compaq:** HP Form S-4 Sep 2001; IDC PC Market Share Q1 2002–2006; SEC EDGAR HP 10-K 2002–2004.
- **Sun Microsystems:** Oracle Form 8-K Jan 2010; SEC EDGAR Oracle 10-K 2010–2014; IDC Server Market Share 2009–2014.
- **MySpace:** Comscore Media Metrix 2006–2012; News Corp 10-K 2008–2011; Carlson N. (2011). *Business Insider*.

**Industrial**
- **Pan Am:** Delta Air Lines Annual Report 1992; US DOT Air Carrier Financial Reports; Petzinger T. (1995). *Hard Landing*. Crown Business.
- **Polaroid:** SEC EDGAR Polaroid Corp Chapter 11 filing 2001; US Bankruptcy Court District of Delaware.
- **Kodak:** SEC EDGAR Eastman Kodak 10-K 2000–2013; IDC Digital Camera Market Share 2000–2015; Kodak Chapter 11 Reorganization Plan 2013.
- **Blockbuster:** Dish Network Form 8-K Apr 2011; SEC EDGAR Blockbuster Chapter 11 2010; Keating G. (2012). *Netflixed*. Portfolio/Penguin.

**History**
- **Cartago:** Bolt & van Zanden (2024) Maddison Project Database 2023 (*est.*); Lazenby J.F. (1996). *The First Punic War*. Stanford UP; Hoyos D. (2010). *The Carthaginians*. Routledge.
- **W. Roman Empire:** Bolt & van Zanden (2024) Maddison 2023 (*est.*); Ward-Perkins B. (2005). *The Fall of Rome*. Oxford UP; Wickham C. (2005). *Framing the Early Middle Ages*. Oxford UP.
- **Aztec Empire:** Bakewell P. (1984). *Miners of the Red Mountain*. UNM Press; Bolt & van Zanden (2024) Maddison 2023 (*est.*); Gibson C. (1964). *The Aztecs Under Spanish Rule*. Stanford UP.
- **USSR:** Bolt & van Zanden (2024) Maddison 2023; World Bank WDI GDP per capita PPP.

**Cross-domain contrast**
- **Crypto:** Yahoo Finance (LUNA1-USD, FTT-USD, EOS-USD, ETH-USD).
- **Astrophysics:** NOAA SWPC GOES X-ray archive; NASA IRSA/ZTF (AT2019qiz).
- **Biology:** CoV-Spectrum/LAPIS open data (GenBank), South Africa.

*Full corpus, code and reproduction: github.com/Inzainos/The-shadow-Node-Theory*
