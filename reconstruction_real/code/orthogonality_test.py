"""
Roadmap #2 — orthogonality test corr(b, Delta).

The 721-case satellization corpus (b) and the collapse cases (Delta) are
DISJOINT entity sets, so a direct corr(b, Delta) is impossible. This test uses
a paired within-domain dataset instead: cryptocurrencies, where the SAME coin
has a rise (ascent to all-time-high -> exponent b_rise) and a collapse
(descent from ATH to the next trough -> exponent Delta_fall).

Orthogonality (b ⊥ Delta) predicts corr(b_rise, Delta_fall) ≈ 0.

Result (n=11, Yahoo Finance daily close):
  Spearman rho = +0.009 (p=0.98)  -> consistent with orthogonality (RC-Δ1 not refuted)

Caveats: within one domain (crypto); b_rise is a price-ascent exponent
(analogue of satellization, not the canonical hub/node b); per-phase power-law
fits vary in R² (Spearman is robust to the LUNA outlier). Cross-domain
orthogonality remains untestable with current data.

Run (network required): python orthogonality_test.py
"""
import json
import urllib.request
import numpy as np
from scipy.stats import spearmanr, pearsonr

COINS = ["BTC", "ETH", "XRP", "ADA", "DOGE", "LTC", "BCH", "TRX",
         "EOS", "XLM", "LINK", "LUNA1", "FTT"]
UA = {"User-Agent": "Mozilla/5.0"}
URL = ("https://query1.finance.yahoo.com/v8/finance/chart/"
       "{c}-USD?period1=1262304000&period2=1893456000&interval=1d")


def fetch(c):
    req = urllib.request.Request(URL.format(c=c), headers=UA)
    d = json.load(urllib.request.urlopen(req, timeout=60))["chart"]["result"][0]
    t = np.array(d["timestamp"], float)
    px = np.array([x if x is not None else np.nan
                   for x in d["indicators"]["quote"][0]["close"]], float)
    ok = ~np.isnan(px) & (px > 0)
    return t[ok], px[ok]


def fit(x, y):
    ok = (x > 0) & (y > 0)
    x, y = x[ok], y[ok]
    if len(x) < 20:
        return None, None
    b, a = np.polyfit(np.log(x), np.log(y), 1)
    yl = np.log(y); pred = a + b*np.log(x)
    r2 = 1 - np.sum((yl-pred)**2)/np.sum((yl-yl.mean())**2)
    return b, r2


def main():
    bs, ds = [], []
    print(f"{'coin':<8}{'b_rise':>9}{'Delta_fall':>12}")
    for c in COINS:
        try:
            t, px = fetch(c)
        except Exception as e:
            print(f"{c:<8} fetch error: {e}"); continue
        if len(px) < 200:
            continue
        pk = int(np.argmax(px))
        if pk < 120 or len(px) - pk < 120:
            continue
        br, _ = fit((t[:pk+1]-t[0])/86400.0, px[:pk+1])
        end = pk + max(int(np.argmin(px[pk:])), 1)
        df, _ = fit((t[pk:end+1]-t[pk])/86400.0, px[pk:end+1])
        if br is None or df is None:
            continue
        bs.append(br); ds.append(df)
        print(f"{c:<8}{br:>+9.2f}{df:>+12.2f}")
    bs, ds = np.array(bs), np.array(ds)
    rs, ps = spearmanr(bs, ds)
    rp, pp = pearsonr(bs, ds)
    print(f"\nn={len(bs)}  corr(b_rise, Delta_fall): "
          f"Spearman rho={rs:+.3f} (p={ps:.3f}); Pearson r={rp:+.3f} (p={pp:.3f})")
    print("Orthogonality b ⊥ Delta predicts rho ≈ 0.")


if __name__ == "__main__":
    main()
