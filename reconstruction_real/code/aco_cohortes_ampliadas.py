"""
Punto 5 del pre-registro 2026-09-27 — cohortes ampliadas de ACO-A.

Pre-registro: `reconstruction_real/preregistro/PREREGISTRO_2026-09-27.md`.

5a. Ortogonalidad b ⊥ Δ (cripto, archivo público de Binance). Método idéntico a
    `orthogonality_test.py`: serie >= 200 días, pico con >= 120 días antes y
    después; b_subida = pendiente log-log del cierre contra días desde el primer
    dato hasta el máximo; Δ_caída = pendiente desde el máximo hasta el mínimo
    posterior; >= 20 puntos por ajuste. Criterio de equivalencia: respaldada si
    el IC 95% (Fisher) de Spearman cae en [-0.3, 0.3]; refutada si |ρ| >= 0.3 con
    p < 0.05; indeterminada en otro caso.
5b. Hazard h(τ) > 0.
    * Cripto (Binance): nacimiento = primera vela; extinción ACO = último cierre
      < 1% del máximo, fecha = último día sobre el umbral; censura al último dato.
      Secundaria: el retiro del par (última vela > 31 días antes de la última
      fecha del archivo) también cuenta como extinción.
    * Bancos (FDIC): nacimiento = ESTYMD; fin = institución inactiva (cualquier
      causa); secundaria: solo quiebras (lista de quiebras de la FDIC, por CERT;
      las demás salidas se censuran). Censura: 2026-09-27.
      Entrada tardía PRE-REGISTRADA: edad en 1934. DESVIACIÓN (documentada): la
      base de la FDIC no registra ningún cierre antes de 1970 (0 en 1934–1969,
      1,653 en 1970–1979), así que con entrada en 1934 el hazard de esas décadas
      sale en cero por construcción; se reporta también la entrada corregida en
      1970. Se excluyen fechas de fundación de relleno (01/01/1800) e inactivas
      sin fecha de cierre (12/31/9999).
    H5b-i (positividad): toda banda con >= 30 en riesgo tiene al menos un fin
    (1 año cripto, 5 años bancos). H5b-ii (forma, v30): Spearman entre edad de la
    banda y hazard > 0 (una cola, bandas con >= 30 en riesgo).
5c. Fricción → Δ: no se amplía (sin series públicas de absorción comparables).

Salidas
-------
    data/fdic_instituciones_2026-09-25.csv.gz, data/fdic_quiebras_2026-08-25.csv.gz
    reconstruction_real/data/aco_ortogonalidad_binance.csv
    reconstruction_real/data/aco_hazard_bandas.csv
    reconstruction_real/logs/aco_cohortes_ampliadas_log.txt

Uso (desde la raíz del repo, tras `descargar_binance_klines.py`):
    python reconstruction_real/code/aco_cohortes_ampliadas.py
"""

import hashlib
import logging
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_TOP = ROOT / "data"
DATA_RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
BIN = DATA_TOP / "binance_cierres_diarios.csv.gz"
FDIC_RAW_I = DATA_TOP / "raw_fdic" / "institutions.csv"
FDIC_RAW_F = DATA_TOP / "raw_fdic" / "failures.csv"
FDIC_I = DATA_TOP / "fdic_instituciones_2026-09-25.csv.gz"
FDIC_F = DATA_TOP / "fdic_quiebras_2026-08-25.csv.gz"
OUT_ORT = DATA_RR / "aco_ortogonalidad_binance.csv"
OUT_HAZ = DATA_RR / "aco_hazard_bandas.csv"
LOG_FILE = LOG_DIR / "aco_cohortes_ampliadas_log.txt"

CORTE = pd.Timestamp("2026-09-27")
DEAD_FRAC = 0.01
RETIRO_DIAS = 31
MIN_EN_RIESGO = 30
EQUIV = 0.3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("ACO-COHORTES")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def fit(x, y):
    """Igual que orthogonality_test.fit: polyfit log-log, >= 20 puntos."""
    ok = (x > 0) & (y > 0)
    x, y = x[ok], y[ok]
    if len(x) < 20:
        return None
    return float(np.polyfit(np.log(x), np.log(y), 1)[0])


# ------------------------------------------------------------------ 5a
def ortogonalidad(B):
    filas = []
    for par, g in B.groupby("par"):
        px = g.close.values.astype(float)
        dias = (g.fecha - g.fecha.iloc[0]).dt.days.values.astype(float)
        ok = px > 0
        px, dias = px[ok], dias[ok]
        if len(px) < 200:
            continue
        pk = int(np.argmax(px))
        if pk < 120 or len(px) - pk < 120:
            continue
        br = fit(dias[:pk + 1], px[:pk + 1])
        end = pk + max(int(np.argmin(px[pk:])), 1)
        dfall = fit(dias[pk:end + 1] - dias[pk], px[pk:end + 1])
        if br is None or dfall is None:
            continue
        filas.append(dict(par=par, b_subida=br, delta_caida=dfall,
                          dias=len(px), pico=str(g.fecha.iloc[pk].date())))
    O = pd.DataFrame(filas)
    n = len(O)
    rho, p = stats.spearmanr(O.b_subida, O.delta_caida)
    z, se = np.arctanh(rho), 1 / np.sqrt(n - 3)
    lo, hi = np.tanh(z - 1.96 * se), np.tanh(z + 1.96 * se)
    if lo >= -EQUIV and hi <= EQUIV:
        dec = "RESPALDADA (equivalencia)"
    elif abs(rho) >= EQUIV and p < 0.05:
        dec = "REFUTADA"
    else:
        dec = "INDETERMINADA"
    rp, pp = stats.pearsonr(O.b_subida, O.delta_caida)
    log.info("5a ORTOGONALIDAD — pares que cumplen las reglas: %d (antes n = 11)", n)
    log.info("   Spearman ρ = %+.3f (p = %.3g) | IC 95%% [%+.3f, %+.3f] | "
             "Pearson r = %+.3f (p = %.3g)", rho, p, lo, hi, rp, pp)
    log.info("   b_subida mediana %+.3f | Δ_caída mediana %+.3f", O.b_subida.median(),
             O.delta_caida.median())
    log.info("   DECISIÓN PRE-REGISTRADA 5a: %s", dec)
    return O, dict(prueba="5a ortogonalidad", n=n, rho=rho, p=p, ic_lo=lo,
                   ic_hi=hi, decision=dec)


# ------------------------------------------------------------------ 5b
def bandas(entrada, salida, evento, ancho, etiqueta):
    """Hazard por banda de edad con entrada tardía (años)."""
    entrada, salida, evento = (np.asarray(v, float) for v in (entrada, salida, evento))
    mx = int(np.ceil(salida.max() / ancho)) * ancho
    filas = []
    for a in np.arange(0, mx, ancho):
        b = a + ancho
        en_riesgo = (entrada < b) & (salida >= a) & (salida > entrada)
        pa = np.clip(np.minimum(salida, b) - np.maximum(entrada, a), 0, None)
        muertes = int(((salida >= a) & (salida < b) & (evento == 1)
                       & (salida > entrada)).sum())
        py = float(pa[en_riesgo].sum())
        filas.append(dict(cohorte=etiqueta, banda_ini=a, banda_fin=b,
                          en_riesgo=int(en_riesgo.sum()), fines=muertes,
                          persona_anios=py,
                          hazard=muertes / py if py > 0 else np.nan))
    return pd.DataFrame(filas)


def evaluar_hazard(H, etiqueta):
    v = H[H.en_riesgo >= MIN_EN_RIESGO]
    ceros = v[v.fines == 0]
    pos = "RESPALDADA" if len(ceros) == 0 else \
        f"SIN EVIDENCIA en {len(ceros)} banda(s)"
    rho, p2 = stats.spearmanr((v.banda_ini + v.banda_fin) / 2, v.hazard)
    p1 = p2 / 2 if rho > 0 else 1 - p2 / 2
    forma = "RESPALDADA" if (rho > 0 and p1 < 0.05) else "NO RESPALDADA"
    log.info("[%s] bandas con >= %d en riesgo: %d | con 0 fines: %s | "
             "H5b-i positividad: %s", etiqueta, MIN_EN_RIESGO, len(v),
             ", ".join(f"{int(a)}-{int(b)} (n={n}, cota 3/n={3 / n:.3f})"
                       for a, b, n in zip(ceros.banda_ini, ceros.banda_fin,
                                          ceros.en_riesgo)) or "ninguna", pos)
    log.info("[%s] H5b-ii hazard crece con la edad: ρ = %+.3f, p 1 cola = %.4g "
             "-> %s", etiqueta, rho, p1, forma)
    for r in v.itertuples():
        log.info("    %5.0f-%-5.0f en riesgo %6d | fines %5d | persona-años %10.1f | "
                 "h = %.4f/año", r.banda_ini, r.banda_fin, r.en_riesgo, r.fines,
                 r.persona_anios, r.hazard)
    return dict(prueba=f"5b {etiqueta}", n=len(v), rho=rho, p=p1,
                decision=f"positividad {pos}; forma {forma}")


def hazard_cripto(B):
    ultimo_archivo = B.fecha.max()
    filas = []
    for par, g in B.groupby("par"):
        px = g.close.values.astype(float)
        f = g.fecha.values
        if len(px) < 2:
            continue
        nac = pd.Timestamp(f[0])
        ath_i = int(np.argmax(px))
        thr = DEAD_FRAC * px[ath_i]
        ult = pd.Timestamp(f[-1])
        if px[-1] < thr:
            sobre = np.where(px[ath_i:] >= thr)[0]
            muerte = pd.Timestamp(f[ath_i + (sobre[-1] if len(sobre) else 0)])
            aco = (1, (muerte - nac).days / 365.25)
        else:
            aco = (0, (ult - nac).days / 365.25)
        retirado = (ultimo_archivo - ult).days > RETIRO_DIAS
        if aco[0] == 1:
            sec = aco
        elif retirado:
            sec = (1, (ult - nac).days / 365.25)
        else:
            sec = aco
        filas.append(dict(par=par, edad_aco=aco[1], fin_aco=aco[0],
                          edad_sec=sec[1], fin_sec=sec[0], retirado=retirado))
    C = pd.DataFrame(filas)
    log.info("5b CRIPTO — cohorte %d pares | extinciones ACO %d | retirados %d | "
             "extinción ACO o retiro %d", len(C), int(C.fin_aco.sum()),
             int(C.retirado.sum()), int(C.fin_sec.sum()))
    H1 = bandas(np.zeros(len(C)), C.edad_aco, C.fin_aco, 1, "cripto ACO")
    H2 = bandas(np.zeros(len(C)), C.edad_sec, C.fin_sec, 1, "cripto ACO+retiro")
    return [H1, H2], [evaluar_hazard(H1, "cripto ACO (principal)"),
                      evaluar_hazard(H2, "cripto ACO+retiro (secundaria)")]


def hazard_bancos():
    if FDIC_RAW_I.exists():
        pd.read_csv(FDIC_RAW_I).to_csv(FDIC_I, index=False,
                                       compression={"method": "gzip", "mtime": 0})
        pd.read_csv(FDIC_RAW_F).to_csv(FDIC_F, index=False,
                                       compression={"method": "gzip", "mtime": 0})
    log.info("FDIC instituciones: %s | SHA-256 %s", FDIC_I.relative_to(ROOT),
             sha256(FDIC_I))
    log.info("FDIC quiebras: %s | SHA-256 %s", FDIC_F.relative_to(ROOT),
             sha256(FDIC_F))
    I = pd.read_csv(FDIC_I)
    Fl = pd.read_csv(FDIC_F)
    est = pd.to_datetime(I.ESTYMD, format="%m/%d/%Y", errors="coerce")
    fin = pd.to_datetime(I.ENDEFYMD, format="%m/%d/%Y", errors="coerce")
    relleno = I.ESTYMD == "01/01/1800"
    sin_fin = (I.ACTIVE == 0) & (I.ENDEFYMD == "12/31/9999")
    ok = ~relleno & ~sin_fin & est.notna()
    log.info("5b BANCOS — instituciones %d | excluidas: fundación de relleno "
             "01/01/1800 %d, inactivas sin fecha de cierre %d | cohorte %d",
             len(I), int(relleno.sum()), int(sin_fin.sum()), int(ok.sum()))
    fin_ok = fin.where(I.ACTIVE == 0, CORTE)
    x = pd.DataFrame(dict(est=est, fin=fin_ok, activa=I.ACTIVE, cert=I.CERT))[ok]
    x["edad_fin"] = (x.fin - x.est).dt.days / 365.25
    x = x[x.edad_fin > 0]
    quiebras = set(pd.to_numeric(Fl.CERT, errors="coerce").dropna().astype(int))
    x["evento_todo"] = (x.activa == 0).astype(int)
    x["evento_quiebra"] = ((x.activa == 0) & x.cert.isin(quiebras)).astype(int)
    log.info("   fines (cualquier causa) %d | quiebras emparejadas por CERT %d "
             "(de %d con CERT en la lista) | cierres antes de 1970: %d",
             int(x.evento_todo.sum()), int(x.evento_quiebra.sum()), len(quiebras),
             int(((x.activa == 0) & (x.fin < "1970-01-01")).sum()))
    out_H, out_R = [], []
    for anio_ent, rotulo in ((1934, "pre-registro 1934 (sesgada)"),
                             (1970, "corregida 1970")):
        ent = ((pd.Timestamp(f"{anio_ent}-01-01") - x.est).dt.days / 365.25) \
            .clip(lower=0)
        for ev, nom in (("evento_todo", "cualquier fin"),
                        ("evento_quiebra", "solo quiebras")):
            et = f"bancos {nom}, entrada {rotulo}"
            H = bandas(ent, x.edad_fin, x[ev], 5, et)
            out_H.append(H)
            out_R.append(evaluar_hazard(H, et))
    return out_H, out_R


def main():
    log.info("=" * 78)
    log.info("PUNTO 5 (pre-registro 2026-09-27) — COHORTES AMPLIADAS ACO-A")
    log.info("=" * 78)
    log.info("Binance: %s | SHA-256 %s", BIN.relative_to(ROOT), sha256(BIN))
    B = pd.read_csv(BIN, parse_dates=["fecha"]).sort_values(["par", "fecha"])
    log.info("   %d pares, %d filas, %s..%s", B.par.nunique(), len(B),
             B.fecha.min().date(), B.fecha.max().date())
    log.info("-" * 78)
    O, r5a = ortogonalidad(B)
    log.info("-" * 78)
    Hc, rc = hazard_cripto(B)
    log.info("-" * 78)
    Hb, rb = hazard_bancos()
    log.info("-" * 78)
    log.info("5c FRICCIÓN -> Δ: no se amplía (sin series públicas de absorción "
             "post-quiebra comparables a la cohorte 2008, n = 6)")
    log.info("-" * 78)
    for r in [r5a] + rc + rb:
        log.info("RESUMEN %-58s %s", r["prueba"], r["decision"])
    O.round(6).to_csv(OUT_ORT, index=False)
    pd.concat(Hc + Hb).round(6).to_csv(OUT_HAZ, index=False)
    log.info("CSV -> %s (%d filas) | SHA-256 %s", OUT_ORT.relative_to(ROOT),
             len(O), sha256(OUT_ORT))
    log.info("CSV -> %s | SHA-256 %s", OUT_HAZ.relative_to(ROOT), sha256(OUT_HAZ))
    log.info("LOG -> %s (corte %s)", LOG_FILE.relative_to(ROOT), date(2026, 9, 27))


if __name__ == "__main__":
    main()
