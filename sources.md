# Data Sources — Shadow Node Theory v2.6.1

**Fractal Core Research · Elan Zainos Corona · Tlaxcala, Mexico · 2026**
All data used in the active SNT v2.6.1 repository release (721 real cases) are either publicly available or clearly marked as proprietary with aggregate results only.

> **Note:** This file serves the active v2.6.1 repository release (new sources
> of the pre-registered tests of 2026-09-27 — OWID COVID/mpox, StatCounter, UN
> WUP 2018, Binance, FDIC — are anchored in `data/FUENTES.md`), built on the
> 721-case real corpus introduced in v2.4.0
> (`reconstruction_real/data/snt_corpus_REAL_v5.csv`). Each domain header gives
> the **active** case count and the source the active cases actually use (the
> `fuente` column of `reconstruction_real/data/by_domain/`). The bibliography
> listed under each header is the research background of the **historical
> (pre-v2.5.0) corpus**, which in several domains was larger and built from different
> sources; it is kept as reference, not as the source of the active cases.
> Editions, download dates and SHA-256 checksums of external files:
> `data/FUENTES.md`. Last verified against the corpus: 2026-09-26.

---

## Domain A — Cities (active n=4)

**Active corpus (4 cases):** UN Demographic Yearbook, modern population series 2000–2023 (Tokyo→Osaka, Tokyo→Yokohama, Paris→Lyon, Madrid→Barcelona). The historical-city bibliography below belongs to the historical corpus; long historical series would require Bairoch (1988).

**Primary source:**
- Bairoch, P., Batou, J. & Chèvre, P. (1988). *La Population des Villes Européennes de 800 à 1850*. Centre d'Histoire Économique Internationale, Université de Genève. Covers 2,200 European cities.
- Chandler, T. (1987). *Four Thousand Years of Urban Growth: An Historical Census*. St. David's University Press.

**Secondary sources by case:**
- **Bruges–Antwerp:** Nicholas, D. (1992). *Medieval Flanders*. Longman. Van der Wee, H. (1963). *The Growth of the Antwerp Market*. Martinus Nijhoff. Gelderblom, O. (2013). *Cities of Commerce*. Princeton University Press.
- **Toledo–Madrid:** Ringrose, D.R. (1973). Madrid and the Spanish Economy. *Journal of Economic History* 33(2), 284–314. INE Spain historical census.
- **Venice–Amsterdam, Genoa–Amsterdam:** Israel, J.I. (1989). *Dutch Primacy in World Trade 1585–1740*. Oxford University Press.
- **Kyoto–Tokyo:** Rozman, G. (1973). *Urban Networks in Russia, 1750–1800, and Pre-Modern Periodization*. Princeton University Press.
- **Nanjing–Beijing:** Rozman, G. (1973). ibid.
- **Alexandria–Cairo:** Kennedy, H. (1985). *From Polis to Madina*. Past and Present 106, 3–27.
- **Philadelphia–New York:** U.S. Census Bureau Historical Statistics.
- **Lima–Buenos Aires:** Maddison Project Database 2023.

---

## Domain B — Country Pairs (active n=446)

**Active corpus (446 cases):** Maddison Project Database **2020**, committed as `data/mpd2020.xlsx` (converted to `data/maddison_mpd2020.csv` with OWID country names). Verified 2026-09-27: `expand_B_massive.py` reproduces all 446 cases byte for byte from it. The later OWID edition in `data/owid-maddison.csv` only reproduces the domain approximately. SHA-256 of both in `data/FUENTES.md`.

**Discriminant test (Block 2) — bilateral trade:** Barbieri, K. & Keshk, O. M. G. (2016). *Correlates of War Project Trade Data Set Codebook, Version 4.0*; Barbieri, K., Keshk, O. M. G. & Pollins, B. (2009). Trading Data: Evaluating our Assumptions and Coding Rules. *Conflict Management and Peace Science* 26(5), 471–491. Committed as `data/COW_Trade_4.0.zip`.

**Primary source:**
- Bolt, J. & van Zanden, J.L. (2020). *Maddison style estimates of the evolution of the world economy. A new 2020 update.* Maddison Project Working Paper WP-15, University of Groningen. Maddison Project Database 2020: GDP per capita 1–2018 AD, 169 countries. [https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2020](https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2020) — License: CC BY 4.0. *(This entry previously read "Maddison Project Database 2023 (2024)", but the coverage it described, 1–2018 and 169 countries, is that of the 2020 edition — the one the corpus was built with.)*

**Secondary sources:**
- **Portugal–NW Europe:** Costa, L.F., Palma, N. & Reis, J. (2015). The great escape? *European Review of Economic History* 19(1), 1–22. Allen, R.C. (2001). The Great Divergence in European wages. *Explorations in Economic History* 38(4), 411–447.
- **Ireland–UK:** Barry, F. (2002). The Celtic Tiger era. *World Economy* 25(12), 1745–1762.
- **Singapore–Malaysia, South Korea–Japan, Estonia–Finland:** Maddison Project Database 2023 (as above).
- **Germany East–West:** Bundesbank Historical Time Series.

---

## Domain C — Intra-national Regions (active n=24; historical corpus n=64)

**Active corpus (24 cases):** US Census historical state populations 1900–2025 (23 state pairs) + INEGI 2022 N-body matrix for Mexico (1 case).

- **Mexico (32 federal entities):** INEGI. (2022–2023). *Sistema de Cuentas Nacionales de México (SCNM)*. PIB per capita by federal entity. [https://www.inegi.org.mx/temas/pib/](https://www.inegi.org.mx/temas/pib/)
- **Mexico historical 1940–1993:** Maddison Project Database 2023, calibrated with INEGI series. See `code/snt_v2_vectorizacion.py` for methodology.
- **Italian Mezzogiorno:** Istat; Banca d'Italia; Svimez (various years).
- **Hauts-de-France, Île-de-France:** INSEE; OECD Regional Database (TL2 GDP per capita from 1990). [https://stats.oecd.org/](https://stats.oecd.org/)
- **Appalachia, US states:** U.S. Bureau of Economic Analysis State GDP series. [https://www.bea.gov/data/gdp/gdp-state](https://www.bea.gov/data/gdp/gdp-state). Appalachian Regional Commission reports.
- **Andalucía, Cataluña:** INE Spain; Eurostat NUTS2. [https://ec.europa.eu/eurostat/](https://ec.europa.eu/eurostat/)
- **Gansu, Guangdong:** National Bureau of Statistics China (NBS); World Bank China provincial data.

---

## Domain D — Digital Ecosystems (active n=3; historical corpus n=53)

**Active corpus (3 cases):** HackerEarth 2026 power laws (activity, credits, runs; 4,771 users). The market-share sources below belong to the historical corpus.

- **HackerEarth 2026 — zerve_hackathon_dataset.csv:** Proprietary dataset, 4,774 users, 409,287 events, 141 event types. **Not redistributable.** Aggregate results available in `data/snt_asi_scores.csv` and `reconstruction_real/data/snt_corpus_REAL_v5.csv`.
- **Browser market share (Chrome, IE, etc.):** StatCounter GlobalStats. [https://gs.statcounter.com/](https://gs.statcounter.com/)
- **Smartphone market share (Apple, Nokia, BlackBerry):** IDC Worldwide Quarterly Mobile Phone Tracker. [https://www.idc.com/](https://www.idc.com/)
- **Social network users (Facebook, MySpace):** Statista; Comscore historical data.
- **Streaming/Video (Netflix, Blockbuster):** Netflix 10-K filings (SEC EDGAR). [https://www.sec.gov/cgi-bin/browse-edgar](https://www.sec.gov/cgi-bin/browse-edgar)
- **Search engine (Google, Yahoo):** StatCounter; Statista; Kinsta historical search share.
- **Kodak vs digital cameras:** Kodak Annual Reports; IDC Imaging Market Reports.

---

## Domain E1 — Invasion / Territorial Spread (active n=4; historical corpus n=20)

**Active corpus (4 cases):** OWID COVID-19 spatial spread, 2020 (global, Asia-Pacific, Europe, Americas wavefronts), modeled as territorial expansion — mathematically equivalent to an invasion front, **not** biological species invasions (GBIF species data were not available). The species-invasion bibliography below belongs to the historical corpus. **Reproducibility:** tested on 2026-09-27 against the raw OWID series with the natural constructions (countries reached over time, thresholds 1/10/100 cases, start at the data origin or at the first regional case) — none reproduces the 4 published values, so E1 is declared **not reproducible**.

- **Rattus norvegicus vs R. rattus (Europe):** He Yu et al. (2022). Introgression, displacement, and collapse. *Nature Communications* 13, 2656. [https://doi.org/10.1038/s41467-022-30080-8](https://doi.org/10.1038/s41467-022-30080-8)
- **African honeybee vs European honeybee (Brazil):** Kerr, W.E. (1967). The history of the introduction of African bees in Brazil. *South African Bee Journal* 39, 3–5.
- **Zebra mussel vs native unionids (Great Lakes):** Ricciardi, A. et al. (1998). Impending extinctions of North American freshwater mussels. *Conservation Biology* 12(6), 1295–1304.
- **Common carp vs native fish (Murray-Darling):** Koehn, J.D. (2004). Carp as a powerful invader. *Freshwater Biology* 49, 882–894.
- **Bullfrog vs native amphibians (Europe):** Ficetola, G.F. et al. (2007). *Molecular Ecology Notes* 7(4), 587–590.
- **Brown tree snake vs Guam birds:** Savidge, J.A. (1987). *Conservation Biology* 1(4), 247–260.
- **Homo sapiens vs Homo neanderthalensis:** Hublin, J.J. et al. (2020). *PNAS* 117(14), 8001–8009. Higham, T. et al. (2014). *Nature* 512, 306–309.
- **Argentine ant (Linepithema humile):** Human, K.G. & Gordon, D.M. (1997). *Oecologia* 109(3), 405–412.
- **Green crab (Carcinus maenas):** Grosholz, E. & Ruiz, G. (1996). *Biological Conservation* 78(1–2), 59–66.
- **Kudzu (Pueraria montana) vs SE US vegetation:** Blaustein, R.J. (2001). *BioScience* 51(2), 154.
- **European starling (Sturnus vulgaris) vs North America:** Koenig, W.D. (2003). *Biological Conservation* 114(2), 307–308.
- **Rainbow trout vs native Patagonia fish:** Habit, E. et al. (2010). *Biological Invasions* 12(3), 583–596.
- **Lionfish (Pterois volitans) vs Caribbean reef fish:** Albins, M.A. & Hixon, M.A. (2008). *Marine Ecology Progress Series* 367, 233–238.
- **Caulerpa taxifolia vs Posidonia (Mediterranean):** Boudouresque, C.F. et al. (2009). *Cryptogamie Algologie* 30(1), 3–19.
- **American mink vs European mink:** Maran, T. et al. (1998). *Biological Conservation* 85(1–2), 77–85.

---

## Domain E2 — Predator-Prey (active n=2; historical corpus n=4)

**Active corpus (2 cases):** Lynx→hare, Hudson Bay Company records (MacLulich 1937) and Elton & Nicholson 1942 (via Rdatasets).

- **Canadian lynx vs snowshoe hare:** Maclulich, D.A. (1937). *Fluctuations in the numbers of the varying hare*. University of Toronto Studies, Biol. Ser. 43. Elton, C. & Nicholson, M. (1942). *Journal of Animal Ecology* 11(2), 215–244. Hudson Bay Company fur records 1845–1935.
- **Adriatic shark vs prey fish:** D'Ancona, U. (1926) cited in Volterra, V. (1926). Fluctuations in the abundance of a species. *Nature* 118, 558–560.
- **Wolf vs elk (Yellowstone):** Beschta, R.L. & Ripple, W.J. (2009). *Biological Conservation* 142(11), 2401–2414.
- **Lion vs wildebeest (Serengeti):** Sinclair, A.R.E. et al. (1975). *East African Wildlife Journal* 13(2), 169–189. Packer, C. et al. (2005). *Science* 307(5712), 990–993.

---

## Domain E3 — Parasite-Host (active n=234)

**Active corpus (234 cases):** OWID COVID-19 per-country curves (JHU CSSE), one case per country. The raw series were recovered on 2026-09-27 (OWID `owid-covid-data.csv`, versioned subset `data/owid_covid_casos_totales.csv.gz`; 233/234 cases reproduced; AR(1)/Newey-West correction done in `reconstruction_real/code/covid_E3_series_crudas.py`). Before that, only fitted summaries were committed, which blocked the AR(1) correction of E3. The other pathogen references below belong to the historical corpus.

- **MRSA vs S. aureus (antibiotic resistance):** CDC. (2019). *Antibiotic Resistance Threats in the United States*. WHO GLASS 2022.
- **HIV vs CD4+ T cells:** Pantaleo, G. et al. (1993). *NEJM* 328(5), 327–335. Ho, D.D. et al. (1995). *Nature* 373, 123–126.
- **Phytophthora infestans vs potato (Ireland):** Turner, P.D. (1981). *Plant Pathology* 30(1), 1–10. Bourke, P.M.A. (1964). *Nature* 203, 805–808.
- **Batrachochytrium dendrobatidis vs amphibians:** Scheele, B.C. et al. (2019). Amphibian fungal panzootic. *Science* 363(6434), 1459–1463.
- **Ebola vs gorillas:** Walsh, P.D. et al. (2003). Catastrophic ape decline. *Nature* 422, 611–614.
- **Plasmodium relictum vs Hawaii birds:** Warner, R.E. (1968). *Condor* 70(2), 101–120.
- **Varroa destructor vs Apis mellifera:** Rosenkranz, P. et al. (2010). *Journal of Invertebrate Pathology* 103(Suppl 1), S96–S119.
- **Cryphonectria parasitica vs American chestnut:** Anagnostakis, S.L. (1987). *Plant Disease* 71(6), 489–493.
- **Yersinia pestis — Black Death (1347–1351):** Benedictow, O.J. (2004). *The Black Death 1346–1353*. Boydell Press.
- **SARS-CoV-2 vs global population:** WHO Coronavirus Dashboard; Our World in Data COVID-19 Dataset. [https://ourworldindata.org/covid-cases](https://ourworldindata.org/covid-cases)
- **Xylella fastidiosa vs olives (Puglia):** EFSA (2020). *EFSA Journal* 18(1), e05908.
- **Pseudogymnoascus destructans vs Myotis lucifugus (WNS):** Frick, W.F. et al. (2010). *Science* 329(5992), 679–682.

---

## Domain F1 — Planetary Systems (active n=2; historical corpus n=14)

**Active corpus (2 cases):** Open Exoplanet Catalogue (stellar/planetary mass dominance vs orbit) + NASA planetary fact sheet (Solar System, Jupiter dominance).

- **Jupiter formation and runaway accretion:** Pollack, J.B. et al. (1996). Formation of the giant planets by concurrent accretion. *Icarus* 124(1), 62–85. D'Angelo, G. et al. (2014). Giant planet formation. In *Planets, Stars and Stellar Systems*. Springer.
- **Grand Tack (Jupiter–Mars):** Walsh, K.J. et al. (2011). A low mass for Mars from Jupiter's early gas-driven migration. *Nature* 475, 206–209.
- **Kuiper Belt dispersal:** Levison, H.F. et al. (2008). Origin of the structure of the Kuiper belt. *Icarus* 196(1), 258–273. Gomes, R. et al. (2005). *Nature* 435, 466–469.
- **Hot Jupiter exclusion of inner planets:** Huang, C.X. et al. (2016). Warm Jupiters are less lonely. *ApJL* 825, L17. Mustill, A.J. et al. (2015). *ApJ* 808(1), 14.
- **Uranus and Neptune formation:** Helled, R. et al. (2023). *A&A*. Pollack et al. (1996) ibid.
- **Moon-forming impact:** Canup, R.M. (2012). Forming a Moon with an Earth-like composition. *Science* 338(6110), 1052–1055.
- **Exoplanet architectures (TRAPPIST-1, Kepler-442b):** Gillon, M. et al. (2017). *Nature* 542, 456–460. Torres, G. et al. (2015). *ApJ* 800(2), 99. NASA Exoplanet Archive. [https://exoplanetarchive.ipac.caltech.edu/](https://exoplanetarchive.ipac.caltech.edu/)

---

## Domain F2 — Stellar (active n=1; historical corpus: stellar binaries, n=8)

**Active corpus (1 case):** Open Exoplanet Catalogue — stellar mass-radius relation of exoplanet hosts. The binary-star references below belong to the historical corpus.

- **Sirius A/B system:** Holberg, J.B. (2009). Sirius B: A new, more accurate view. *The Astronomical Journal* 135(3), 1239–1247. Bond, H.E. et al. (2017). *ApJ* 840(1), 70.
- **Cataclysmic variables (SS Cygni):** Patterson, J. (1984). The evolution of cataclysmic and low-mass X-ray binaries. *ApJS* 54, 443–493.
- **OJ 287 binary BH:** Valtonen, M.J. et al. (2016). OJ287: Deciphering the 'Rosetta Stone'. *ApJL* 819, L37. Dey, L. et al. (2018). *ApJ* 866(1), 11.
- **Algol system:** Zavala, R.T. et al. (2010). *AJ* 139(6), 2557–2571.
- **Beta Lyrae:** Harmanec, P. & Scholz, G. (1993). *A&A* 279, 571–584.
- **Cygnus X-1:** Orosz, J.A. et al. (2011). The mass of the black hole in Cygnus X-1. *ApJ* 742, 84. Gou, L. et al. (2011). *ApJ* 742, 85.
- **RS Ophiuchi (recurrent nova):** Mikołajewska, J. & Shara, M.M. (2017). *ApJ* 847(1), 99.

---

## Domain F3 — Multiplanet (active n=1) · Black Hole Accretion (historical corpus only, n=13)

**Active corpus (1 case):** Open Exoplanet Catalogue — multiplanet mass dominance (11 planets). Black-hole accretion is **not** in the active corpus; the references below belong to the historical corpus.

- **Sagittarius A* / G2 cloud (real-time):** Gillessen, S. et al. (2012). A gas cloud on its way towards the supermassive black hole. *Nature* 481, 51–54. Gillessen, S. et al. (2013). *ApJ* 763(2), 78.
- **M87* (Event Horizon Telescope):** Event Horizon Telescope Collaboration (2019). First M87 Event Horizon Telescope Results. *ApJL* 875, L1–L17. Walsh, J.L. et al. (2013). *ApJ* 770(2), 86.
- **TON 618:** Shemmer, O. et al. (2004). *ApJ* 614(2), 547–560. King, A. (2016). *MNRAS Letters* 456(1), L109.
- **GW150914:** Abbott, B.P. et al. LIGO/Virgo (2016). Observation of gravitational waves. *Physical Review Letters* 116, 061102.
- **GRS 1915+105:** Mirabel, I.F. & Rodriguez, L.F. (1994). A superluminal source in the Galaxy. *Nature* 371, 46–48. Greiner, J. et al. (2001). *A&A* 373, L37.
- **3C 273:** Schmidt, M. (1963). 3C 273: A star-like object. *Nature* 197, 1040–1041.
- **NGC 4889 BH:** McConnell, N.J. et al. (2011). Two ten-billion-solar-mass black holes. *Nature* 480, 215–218.

---

## Domain F4 — Galactic Systems (historical corpus only, n=12; not in the active corpus)

- **Sagittarius dwarf spheroidal:** Majewski, S.R. et al. (2003). A 2MASS view of the Sagittarius dwarf galaxy. *ApJ* 599(2), 1082–1115. Law, D.R. & Majewski, S.R. (2010). The Sagittarius dwarf galaxy. *ApJ* 714(1), 229–254.
- **M32 / Andromeda:** Graham, A.W. (2002). Evidence for an outer Sérsic profile. *ApJL* 568(1), L13–L17. Dierickx, M. et al. (2014). *ApJ* 789(1), 16.
- **Large Magellanic Cloud:** Erkal, D. et al. (2019). Constraining the mass of the LMC. *MNRAS* 487(2), 2685–2700. Besla, G. et al. (2007). *ApJ* 668(2), 949–967.
- **Fornax dwarf spheroidal:** Simon, J.D. (2019). The faintest dwarf galaxies. *ARA&A* 57, 375–415. Walker, M.G. et al. (2009). *ApJ* 704(2), 1274–1287.
- **NGC 147/185 / Andromeda:** Collins, M.L.M. et al. (2013). *ApJ* 768(2), 172.
- **Antennae galaxies (NGC 4038/4039):** Renaud, F. et al. (2015). *MNRAS* 454(3), 3299–3310.
- **Local Group (Milky Way–M31 future merger):** van der Marel, R.P. et al. (2012). *ApJ* 753(1), 9. Cox, T.J. & Loeb, A. (2008). *MNRAS* 386(1), 461–474.

---

## Atomic Sovereignty Index (ASI) — HackerEarth 2026

- **Dataset:** zerve_hackathon_dataset.csv — proprietary, 4,774 users, 409,287 events. Aggregate results only in `data/snt_asi_scores.csv`.
- **Theoretical basis:** Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience* 11(2), 127–138. Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal* 27(3), 379–423.
- **PsyCap validation:** Avey, J.B., Reichard, R.J., Luthans, F. & Mhatre, K.H. (2011). Meta-analysis of the impact of positive psychological capital. *Human Resource Development Quarterly* 22(2), 127–152.

---

## Additional Theoretical References

- Barabási, A.L. & Albert, R. (1999). Emergence of scaling in random networks. *Science* 286(5439), 509–512.
- Watts, D.J. & Strogatz, S.H. (1998). Collective dynamics of small-world networks. *Nature* 393(6684), 440–442.
- Holland, J.H. (1995). *Hidden Order: How Adaptation Builds Complexity*. Addison-Wesley.
- Brezis, E.S. & Krugman, P.R. (1993). Leapfrogging in international competition. *American Economic Review* 83(5), 1211–1219.
- Lotka, A.J. (1925). *Elements of Physical Biology*. Williams & Wilkins.
- Volterra, V. (1926). Fluctuations in the abundance of a species. *Nature* 118, 558–560.
- Gause, G.F. (1934). *The Struggle for Existence*. Williams & Wilkins.

---

## Replication Package

All scripts, processed data files, and figures are available at:
- **GitHub:** [https://github.com/Inzainos/The-shadow-Node-Theory](https://github.com/Inzainos/The-shadow-Node-Theory)
- **Zenodo archive (721-case corpus / v2.5.0 snapshot):** [https://doi.org/10.5281/zenodo.19446521](https://doi.org/10.5281/zenodo.19446521)
- **Zenodo v2.0:** [https://doi.org/10.5281/zenodo.19131327](https://doi.org/10.5281/zenodo.19131327)

*Last updated: September 2026 (v2.6.1)*
