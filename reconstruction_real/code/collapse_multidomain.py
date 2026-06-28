"""
Collapse across 5 domains — reproducibility of the multi-domain collapse table
(reconstruction_real/data/collapse_multidomain_v29.csv) and the stability-landscape
figures (figures/fig_paisajes_colapso, figures/fig_catastrofe_cuspide).

This documents HOW each domain's collapse case was obtained and characterised.
Live-data domains fetch from public sources at runtime (network required):

  - Crypto LUNA / FTX : Yahoo Finance chart API (LUNA1-USD, FTT-USD), daily.
  - Crypto EOS        : user CSV (Kaggle "cryptocurrency historical prices");
                        absorber ETH from same source.
  - Biology           : CoV-Spectrum / LAPIS open API (GenBank), South Africa,
                        Delta (B.1.617.2*) vs Omicron (BA.1*).
  - Astro flare       : NOAA SWPC GOES X-ray (0.1-0.8 nm) 7-day JSON.
  - Astro TDE         : NASA IRSA ZTF light-curve API, AT2019qiz (g band).
  - Socioeconomic     : corpus ACO v2.4.0 (reconstruction_real/code/build_aco_v29.py).

Method (common): fit the post-extinction trajectory to a power law A(τ)=c·τ^Δ
on log-log axes; compare to an exponential where a cliff is suspected; classify
the collapse mode by (friction × trigger × floor/ceiling).

Findings are descriptive and correlational — see papers/SNT_Colapso_Acoplado.md
for the full theory, caveats, and the falsifiable formulations.

Fractal Core Research | Tlaxcala, Mexico | 2026
"""
import numpy as np


def fit_power_law(tau, R):
    """OLS on log-log. Returns (exponent, r2) for tau>0, R>0."""
    tau, R = np.asarray(tau, float), np.asarray(R, float)
    ok = (tau > 0) & (R > 0)
    tau, R = tau[ok], R[ok]
    if len(tau) < 4:
        return None, None
    b, lc = np.polyfit(np.log(tau), np.log(R), 1)
    pred = np.exp(lc) * tau ** b
    ss_res = np.sum((R - pred) ** 2)
    ss_tot = np.sum((R - R.mean()) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return round(b, 3), round(r2, 3)


def fit_exponential(tau, R):
    """OLS of log R on tau (linear time). Better than power law => cliff."""
    tau, R = np.asarray(tau, float), np.asarray(R, float)
    ok = R > 0
    tau, R = tau[ok], R[ok]
    if len(tau) < 4:
        return None, None
    k, a = np.polyfit(tau, np.log(R), 1)
    pred = a + k * tau
    y = np.log(R)
    ss_res = np.sum((y - pred) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return round(k, 4), round(r2, 3)


# Data-source URLs (documented for reproducibility) -----------------------------
SOURCES = {
    "luna":  "https://query1.finance.yahoo.com/v8/finance/chart/LUNA1-USD"
             "?period1=1648771200&period2=1655251200&interval=1d",
    "ftx":   "https://query1.finance.yahoo.com/v8/finance/chart/FTT-USD"
             "?period1=1665792000&period2=1669852800&interval=1d",
    "omicron": "https://lapis.cov-spectrum.org/open/v2/sample/aggregated"
               "?country=South%20Africa&pangoLineage=BA.1*"
               "&dateFrom=2021-09-01&dateTo=2022-02-28&fields=date",
    "delta":   "https://lapis.cov-spectrum.org/open/v2/sample/aggregated"
               "?country=South%20Africa&pangoLineage=B.1.617.2*"
               "&dateFrom=2021-09-01&dateTo=2022-02-28&fields=date",
    "solar_flare": "https://services.swpc.noaa.gov/json/goes/primary/"
                   "xrays-7-day.json",
    "tde": "https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves"
           "?POS=CIRCLE 71.65786 -10.22641 0.0014&BANDNAME=g&FORMAT=CSV",
}

if __name__ == "__main__":
    print("Multi-domain collapse — reproducibility manifest")
    print("=" * 64)
    print("See reconstruction_real/data/collapse_multidomain_v29.csv for the")
    print("compiled results, and papers/SNT_Colapso_Acoplado.md for the theory.\n")
    print("Data sources:")
    for k, v in SOURCES.items():
        print(f"  {k:<12} {v}")
    print("\nSocioeconomic cases: reconstruction_real/code/build_aco_v29.py")
    print("Figures: reconstruction_real/code/ (landscape script) -> figures/")
