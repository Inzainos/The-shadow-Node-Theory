"""
Roadmap #3 — biology with an UNBOUNDED collapse magnitude.

Variant *frequency* is bounded [0,1] and therefore logistic by construction
(see Delta→Omicron). To test whether biology can leave the logistic regime,
we analyse the post-peak collapse of an epidemic wave in ABSOLUTE daily cases
(unbounded): the South Africa Omicron wave (JHU CSSE confirmed).

Result: the decline is smooth EXPONENTIAL (R²≈0.96, e-fold ≈22 d), NOT a cliff
(log-returns do not accelerate). Even unbounded, biological collapse stays
regulated — epidemiological feedback (immunity, susceptible depletion, R_eff<1)
is intrinsic 'friction'.

Refinement to the taxonomy: 'Regulated Orbital Decay' is smooth/non-accelerating
and may be POWER-LAW (scale-free: finance, astro) OR EXPONENTIAL (constant-rate:
epidemics). What separates regulated from a Catastrophic Cliff is whether the
decay rate ACCELERATES — only the cliff does (super-exponential).

Source: JHU CSSE time_series_covid19_confirmed_global.csv. Run: network required.
"""
import csv, io, datetime as dt, urllib.request
import numpy as np

URL = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/"
       "csse_covid_19_data/csse_covid_19_time_series/"
       "time_series_covid19_confirmed_global.csv")


def r2(y, yh):
    return 1 - np.sum((y-yh)**2)/np.sum((y-y.mean())**2)


def main():
    raw = urllib.request.urlopen(URL, timeout=90).read().decode()
    rows = list(csv.reader(io.StringIO(raw)))
    hdr = rows[0]
    sa = [r for r in rows if r[1] == "South Africa"][0]
    dates = [dt.datetime.strptime(d, "%m/%d/%y").date() for d in hdr[4:]]
    cum = np.array([float(x) for x in sa[4:]])
    daily = np.clip(np.diff(cum, prepend=cum[0]), 0, None)
    sm = np.convolve(daily, np.ones(7)/7, mode="same")

    idx = [i for i, d in enumerate(dates)
           if dt.date(2021, 11, 15) <= d <= dt.date(2022, 2, 1)]
    wd = [dates[i] for i in idx]
    wv = sm[idx]
    pk = int(np.argmax(wv))
    tr = pk + int(np.argmin(wv[pk:]))
    tau = np.arange(1, tr - pk + 1, dtype=float)
    y = wv[pk+1:tr+1]
    ok = y > 0
    tau, R = tau[ok], (y[ok] / wv[pk])
    yl = np.log(R)
    bpl, apl = np.polyfit(np.log(tau), yl, 1)
    bex, aex = np.polyfit(tau, yl, 1)
    lr = np.diff(yl)
    acc = np.polyfit(np.arange(len(lr)), lr, 1)[0]

    print(f"Omicron wave (South Africa): peak {wd[pk]} ~{wv[pk]:,.0f}/day")
    print(f"  decline {len(tau)} d to {wd[tr]} ({R[-1]*100:.0f}% of peak)")
    print(f"  POWER LAW   exp={bpl:+.2f}  R2={r2(yl, apl+bpl*np.log(tau)):.3f}")
    print(f"  EXPONENTIAL k={bex:+.3f}/d R2={r2(yl, aex+bex*tau):.3f}")
    print(f"  log-return trend {acc:+.4f}/d -> "
          f"{'accelerating (cliff)' if acc < -1e-3 else 'NOT accelerating (regulated)'}")


if __name__ == "__main__":
    main()
