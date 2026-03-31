# Data Sources — Shadow Node Theory v2.2

Complete data provenance for all 502 verified cases across 11 domains.

---

## Domain A — Historical Cities (n=64)

**Primary source:**  
Bairoch, P., Batou, J. & Chèvre, P. (1988). *La Population des Villes Européennes de 800 à 1850.* Centre d'Histoire Économique Internationale, Geneva. 2,200 cities, 800–1850.

**Case-specific sources:**
- **Bruges → Antwerp:** Van der Wee, H. (1963). *The Growth of the Antwerp Market and the European Economy.* Martinus Nijhoff. / Gelderblom, O. (2013). *Cities of Commerce.* Princeton University Press.
- **Toledo → Madrid:** Ringrose, D.R. (1973). Madrid and the Spanish Economy, 1560–1850. *Journal of Economic History*, 33(2), 284–314. / INE España, series históricas de población municipal.
- **Additional city pairs:** Bairoch et al. (1988) primary. Maddison Project 2023 as economic proxy where population series are incomplete.

---

## Domain B — Country Pairs (n=230)

**Primary source:**  
Bolt, J. & van Zanden, J.L. (2024). *Maddison Project Database 2023.* Groningen Growth and Development Centre, University of Groningen.  
URL: https://www.rug.nl/ggdc/historicaldevelopment/maddison/  
License: CC BY 4.0  
Coverage: GDP per capita 1–2018, 169 countries, 2011 international dollars PPP.

**Case-specific sources:**
- **Portugal vs. Northwestern Europe:** Costa, L.F., Palma, N. & Reis, J. (2015). The great escape? *European Review of Economic History*, 19(1), 1–22.
- **Korea vs. Japan (leapfrog):** World Bank Open Data. GDP per capita (constant 2015 USD). https://data.worldbank.org
- **Ireland vs. UK:** OECD National Accounts Statistics. GDP per capita PPP, 1970–2023.

---

## Domain C — Intra-national Regions (n=64)

**Mexico (primary):**  
INEGI (2022). PIB per cápita por entidad federativa. *Sistema de Cuentas Nacionales de México.*  
URL: https://www.inegi.org.mx/temas/pib/ · 32 federal entities, 2003–2022.

- CONEVAL. Indicadores de bienestar por entidad federativa, 1990–2022. https://www.coneval.org.mx
- Secretaría de Economía México. IED por entidad federativa, 2010–2022.
- CONAPO. Matrices de migración interestatal, 1990–2020.

**OECD regions:**  
OECD Regional Database. TL2/TL3 GDP per capita, 1990–2022. https://stats.oecd.org/

**European regions:**  
Eurostat NUTS2 regional accounts. GDP per inhabitant, 1995–2022. https://ec.europa.eu/eurostat/

**United States:**  
U.S. Bureau of Economic Analysis (BEA). State GDP series, 1963–2022. https://www.bea.gov/data/gdp/gdp-state

---

## Domain D — Digital Ecosystems (n=53)

- StatCounter GlobalStats. Browser, search engine, OS market share. https://gs.statcounter.com
- Statista. Platform user bases and market share, 2000–2026. https://www.statista.com
- IDC Market Research. Technology market share reports.
- SEC EDGAR. 10-K annual filings, revenue and user data. https://www.sec.gov/edgar
- **HackerEarth 2026 — Zerve dataset:** Proprietary, N=4,774 users, 409,287 events, 141 event types. Not redistributable. Aggregate results available in `data/` directory.

---

## Domain E1 — Biological Invasion (n=20)

- He Yu et al. (2022). Spatiotemporal patterns of rat displacement in Europe. *Nature Communications.*
- Abdelkrim, J. et al. (2005). Island colonization and founder effects. *Molecular Ecology.*
- Kerr, W.E. (1967). The history of the introduction of African bees in Brazil. *South African Bee Journal*, 39, 3–5.
- Koch, L.K. et al. (2020). Population genetics of the invasive common carp. *Freshwater Biology.*
- Stoks, R. et al. (2021). Range expansions under global change. *Functional Ecology.*
- Prüfer, K. et al. (2014). The complete genome sequence of a Neanderthal from the Altai Mountains. *Nature*, 505, 43–49.

---

## Domain E2 — Predator-Prey (n=4)

- Hudson's Bay Company Archives (1845–1935). Fur trade records — lynx and snowshoe hare. Manitoba, Canada.
- D'Ancona, U. (1926). Dell'influenza della stasi peschereccia del periodo 1914–18 sul patrimonio ittico. *Memorie R. Comitato Talassografico Italiano*, 126.
- Volterra, V. (1926). Fluctuations in the abundance of a species considered mathematically. *Nature*, 118, 558–560.
- Creel, S. & Winnie, J.A. (2005). Responses of elk herd size to fine-scale spatial and temporal variation in the risk of predation by wolves. *Animal Behaviour*, 69(5), 1181–1189.

---

## Domain E3 — Parasite-Host (n=20)

- UNAIDS (2023). Global HIV & AIDS statistics. https://www.unaids.org/en/resources/fact-sheet
- Perelson, A.S. et al. (1996). HIV-1 dynamics in vivo. *Science*, 271(5255), 1582–1586.
- WHO AMR surveillance data. Global Antimicrobial Resistance and Use Surveillance System (GLASS). https://www.who.int/glass
- Andersson, D.I. & Hughes, D. (2010). Antibiotic resistance and its cost. *Nature Reviews Microbiology*, 8, 260–271.
- Bourke, P.M.A. (1964). *The Visitation of God? The Potato and the Great Irish Famine.* Lilliput Press.
- Yoshida, K. et al. (2013). The rise and fall of the Phytophthora infestans lineage that triggered the Irish potato famine. *eLife*, 2, e00731.

---

## Domain F1 — Planetary Systems (n=14)

- Pollack, J.B. et al. (1996). Formation of the giant planets by concurrent accretion of solids and gas. *Icarus*, 124(1), 62–85.
- Walsh, K.J. et al. (2011). A low mass for Mars from Jupiter's early gas-driven migration. *Nature*, 475, 206–209.
- Helled, R. et al. (2023). Jupiter's formation and internal structure. *Space Science Reviews.*
- NASA JPL. Planetary Fact Sheets. https://nssdc.gsfc.nasa.gov/planetary/factsheet/
- D'Angelo, G. & Lissauer, J.J. (2018). Formation of giant planets. In *Handbook of Exoplanets.* Springer.

---

## Domain F2 — Stellar Binaries (n=8)

- Bond, H.E. et al. (2017). The Sirius system and its astrophysical puzzles. *Astrophysical Journal*, 840(2), 70.
- Warner, B. (1995). *Cataclysmic Variable Stars.* Cambridge University Press.
- Knigge, C., Baraffe, I. & Patterson, J. (2011). The evolution of cataclysmic variables as revealed by their donor stars. *Astrophysical Journal Supplement*, 194(2), 28.
- Ritter, H. & Kolb, U. (2003). Catalogue of cataclysmic binaries. *Astronomy & Astrophysics*, 404, 301.

---

## Domain F3 — Black Holes (n=13)

- Gillessen, S. et al. (2012). A gas cloud on its way towards the supermassive black hole at the Galactic Centre. *Nature*, 481, 51–54.
- Orosz, J.A. et al. (2011). The mass of the black hole in Cygnus X-1. *Astrophysical Journal*, 742(2), 84.
- Event Horizon Telescope Collaboration (2019). First M87 Event Horizon Telescope results. *Astrophysical Journal Letters*, 875, L1.
- Gravity Collaboration (2018). Detection of orbital motions near the last stable circular orbit of the massive black hole SgrA\*. *Astronomy & Astrophysics*, 618, L10.

---

## Domain F4 — Galactic Systems (n=12)

- Ibata, R.A. et al. (1994). A dwarf satellite galaxy in Sagittarius. *Nature*, 370, 194–196.
- Law, D.R. & Majewski, S.R. (2010). The Sagittarius dwarf galaxy. *Astrophysical Journal*, 714(1), 229.
- Erkal, D. et al. (2019). The total mass of the Large Magellanic Cloud from its perturbation on the Milky Way. *Monthly Notices of the Royal Astronomical Society*, 487(2), 2685.
- Dierickx, M. et al. (2014). Predicted extension of the Sagittarius stream to the Northern Galactic sky. *Astrophysical Journal*, 791(1), 7.
- van der Marel, R.P. et al. (2012). The M31 velocity vector. *Astrophysical Journal*, 753(1), 8.

---

## Replication Package

Full replication package with code and data available at:  
**Zenodo DOI v2.2:** https://doi.org/10.5281/zenodo.19131327  
**Zenodo DOI v1.0:** https://doi.org/10.5281/zenodo.19027089

For questions about data access or methodology, contact:  
Elan Zainos Corona — elan.zainos.corona@gmail.com — Fractal Core Research, Tlaxcala, Mexico.
