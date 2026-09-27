"""
Reconstrucción del dominio B con un hub que EMERGE de la red de comercio
(pendiente 9 de la auditoría v32; sigue a los Bloques 2–3 de la prueba
discriminante, `audits/DISCRIMINANTE_DOMINIO_B.md`).

Problema que atiende
--------------------
En el dominio B publicado (446 pares, `expand_B_massive.py`) el "hub" de cada
par se asigna por PIB per cápita MEDIO de toda la ventana. Esa regla acopla por
construcción la brecha inicial con la pendiente b y hace que el 85% de los
países sean hub y satélite a la vez. Aquí el hub deja de asignarse: se toma de
los datos de comercio.

Definiciones
------------
* Nodo: cada uno de los 103 países del dominio B publicado (91 aparecen como
  hub y 89 como satélite; mismos nombres Maddison 2020), con las mismas reglas de entidad que
  `build_comercio_bilateral_cow.py` (sus exportaciones solo cuentan en los años
  en que el código COW corresponde al mismo territorio).
* Década de referencia del nodo: 10 años desde el primer año (>= 1900) con
  exportaciones totales positivas registradas en COW y PIB Maddison.
* Hub emergente (definición primaria): el socio que recibe la mayor suma de
  exportaciones del nodo en la década de referencia, entre los socios que
  corresponden a una entidad de Maddison 2020 con el mismo territorio
  (`socio_maddison`). Si el primer destino no tiene entidad Maddison se registra
  y se toma el siguiente.
* Serie: R(t) = PIBpc_hub / PIBpc_nodo, años comunes en [inicio de la década de
  referencia, 2018], t = 1..n; b por MCO en log-log — idéntico a `calc()` de
  `expand_B_massive.py` (mismo ajuste que el dominio B publicado).
* Brecha inicial g = media de log R en las primeras 5 observaciones.

Pruebas (predicción SNT de acoplamiento: el hub comercial diverge más)
----------------------------------------------------------------------
1. Hub vs controles emparejados por brecha. Para cada nodo, controles = socios
   con serie Maddison que NO están entre sus 5 principales destinos en la
   década de referencia, misma ventana (n >= 90% de la del hub), con
   |g_control - g_hub| <= CALIPER; se toman los K más cercanos en g.
   d = b_hub - media(b_controles). SNT predice d > 0. Unidades: nodos
   (Wilcoxon, signo) y clusters por hub (media de d por hub).
2. Dentro de cada nodo: entre todos sus socios más ricos al inicio (g > 0) con
   registro comercial válido en la década de referencia, ρ de Spearman parcial
   entre b y la participación de exportaciones, controlando g (rangos
   residualizados). SNT predice ρ > 0. Agregado entre nodos.
   Variante con control de gravedad: además de g, se controla el tamaño
   económico inicial del socio (log PIB total = PIBpc × población de
   `data/mpd2020.xlsx`, media de las 5 primeras observaciones), porque el
   comercio crece con el tamaño del socio.
3. Descriptivos: distribución de b, fracción b > 0 entre hubs más ricos,
   correlación b–brecha inicial (en B publicado ρ = −0.489), coincidencia con
   los pares del dominio B, cambio de hub entre la década de referencia y
   2005–2014.
Robustez: hub definido por el total de exportaciones de toda la ventana
(endógeno; solo comparativo), excluyendo los hubs aproximados (RFA -> Germany)
y excluyendo los nodos con cobertura CMEA dudosa: miembros del CMEA cuya década
de referencia cae en 1949–1991 y cuyas exportaciones a la URSS figuran en COW
como faltantes o cero en 5 o más de los 10 años (verificado para Mongolia
1958–1967: flujo a la URSS -9 o 0 en los 10 años).

Salidas
-------
    reconstruction_real/data/dominio_B_hub_comercio.csv          (1 fila por nodo)
    reconstruction_real/data/dominio_B_hub_comercio_intra_nodo.csv (prueba 2)
    reconstruction_real/logs/reconstruccion_B_hub_comercio_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/reconstruccion_B_hub_comercio.py
"""

import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comercio_maddison import (APROX, CMEA, IN_MADDISON,  # noqa: E402
                               IN_MPD_XLSX, IN_ZIP, RENOMBRE_SOCIO, cargar_pib,
                               cargar_poblacion, leer_cow, partial_spearman,
                               sha256, socio_maddison)

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_TOP = ROOT / "data"
DATA_RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

IN_B = DATA_RR / "by_domain" / "dominio_B_real.csv"
OUT_NODOS = DATA_RR / "dominio_B_hub_comercio.csv"
OUT_INTRA = DATA_RR / "dominio_B_hub_comercio_intra_nodo.csv"
LOG_FILE = LOG_DIR / "reconstruccion_B_hub_comercio_log.txt"

ANIO_MIN = 1900
ANIO_MAX_PIB = 2018
DECADA = 10
N_MIN = 10            # mínimo de observaciones por serie (igual que dominio B)
N_BRECHA = 5          # observaciones iniciales para la brecha g
TOP_EXCLUIR = 5       # principales destinos que no pueden ser control
K_CONTROLES = 5
CALIPER = 0.25        # |Δg| máximo en log (≈ 28% de diferencia de ratio)
COBERTURA_CONTROL = 0.9
MIN_SOCIOS_INTRA = 8
SEED = 20260927

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("B-HUB-COMERCIO")


def ajuste(pib, hub, nodo, y0, y1=ANIO_MAX_PIB, pobl=None):
    """Mismo ajuste que calc() de expand_B_massive.py (sin redondeo).
    Con `pobl`, añade `tam` = media de log PIB total del hub en las primeras
    N_BRECHA observaciones con población."""
    if hub not in pib.columns or nodo not in pib.columns:
        return None
    m = pib.loc[(pib.index >= y0) & (pib.index <= y1), [hub, nodo]].dropna()
    if len(m) < N_MIN:
        return None
    R = m[hub].values / m[nodo].values
    t = np.arange(1, len(m) + 1)
    lt, lR = np.log(t), np.log(R)
    sl, ic, rv, pv, se = stats.linregress(lt, lR)
    res = lR - (ic + sl * lt)
    dw = np.sum(np.diff(res) ** 2) / np.sum(res ** 2)
    tam = np.nan
    if pobl is not None and hub in pobl.columns:
        pt = pobl[hub].reindex(m.index)
        tot = np.log(m[hub] * pt).dropna()
        if len(tot):
            tam = float(tot.iloc[:N_BRECHA].mean())
    return dict(b=sl, r2=rv ** 2, p=pv, dw=dw, n=len(m),
                g=float(np.mean(lR[:N_BRECHA])), tam=tam,
                year_min=int(m.index.min()), year_max=int(m.index.max()))


def resumen_d(df, etiqueta):
    """Pruebas de d = b_hub - media(b_controles) por nodo y por cluster-hub."""
    x = df.dropna(subset=["d"])
    if len(x) < 5:
        log.info("[%s] n = %d nodos con controles: insuficiente", etiqueta, len(x))
        return
    w = stats.wilcoxon(x.d)
    s = stats.binomtest(int((x.d > 0).sum()), len(x), 0.5)
    log.info("[%s] nodos = %d | d mediana %+.4f, media %+.4f | d>0 en %d/%d | "
             "Wilcoxon p = %.4g | signo p = %.4g", etiqueta, len(x),
             x.d.median(), x.d.mean(), int((x.d > 0).sum()), len(x),
             w.pvalue, s.pvalue)
    h = x.groupby("hub")["d"].mean()
    if len(h) >= 6:
        wh = stats.wilcoxon(h)
        log.info("[%s] cluster por hub: %d hubs | d>0 en %d/%d | Wilcoxon p = %.4g",
                 etiqueta, len(h), int((h > 0).sum()), len(h), wh.pvalue)
    else:
        log.info("[%s] cluster por hub: solo %d hubs", etiqueta, len(h))


def main():
    log.info("=" * 78)
    log.info("RECONSTRUCCIÓN DEL DOMINIO B CON HUB EMERGENTE DE COMERCIO")
    log.info("=" * 78)
    M, pib = cargar_pib(log)
    entidades = set(pib.columns)
    pobl = cargar_poblacion(M, log)
    B = pd.read_csv(IN_B)
    nodos = sorted(set(B.hub) | set(B.nodo))
    parB = {(h, n): b for h, n, b in zip(B.hub, B.nodo, B.b)}
    log.info("Nodos (países del dominio B publicado): %d", len(nodos))

    exp = leer_cow(entidades, ANIO_MIN, log)
    exp = exp[exp.nodo.isin(nodos)]

    filas, intra = [], []
    for nodo in nodos:
        e = exp[exp.nodo == nodo]
        tot_anio = e.groupby("anio")["v"].sum()
        # primer año con PIB del nodo y exportaciones totales positivas
        anios_ok = [a for a in tot_anio[tot_anio > 0].index
                    if not np.isnan(pib[nodo].get(a, np.nan))] \
            if nodo in pib.columns else []
        if not anios_ok:
            filas.append(dict(nodo=nodo, estado="sin exportaciones válidas "
                              "del mismo territorio con PIB"))
            continue
        y0 = anios_ok[0]
        ref = e[(e.anio >= y0) & (e.anio < y0 + DECADA)]
        total_ref = ref.v.sum()
        if total_ref <= 0:
            filas.append(dict(nodo=nodo, y0=y0, estado="exportaciones 0 en referencia"))
            continue
        por_socio_raw = ref.groupby("s")["v"].sum().sort_values(ascending=False)
        top_raw = por_socio_raw.index[0]
        mapeado = ref.dropna(subset=["socio"])
        por_socio = mapeado.groupby("socio")["v"].sum().sort_values(ascending=False)
        por_socio = por_socio.drop(nodo, errors="ignore")
        share = por_socio / total_ref
        aprox_socios = set(mapeado.loc[mapeado.aprox, "socio"])
        anios_urss = ref.loc[(ref.socio == "Former USSR") & (ref.v > 0),
                             "anio"].nunique()
        cmea_dudoso = (nodo in CMEA and 1949 <= y0 <= 1991
                       and anios_urss < DECADA / 2)

        # hub primario: primer destino mapeado con serie ajustable
        hub = fit_h = None
        for cand in por_socio.index:
            fit_h = ajuste(pib, cand, nodo, y0)
            if fit_h is not None:
                hub = cand
                break
        if hub is None:
            filas.append(dict(nodo=nodo, y0=y0, estado="ningún socio con serie"))
            continue

        # hub de ventana completa (robustez, endógeno)
        comp = e[(e.anio >= y0)].dropna(subset=["socio"])
        comp = comp.groupby("socio")["v"].sum().drop(nodo, errors="ignore")
        hub_comp = next((c for c in comp.sort_values(ascending=False).index
                         if ajuste(pib, c, nodo, y0) is not None), None)
        # hub reciente (2005-2014)
        rec = e[(e.anio >= 2005)].dropna(subset=["socio"])
        rec = rec.groupby("socio")["v"].sum().drop(nodo, errors="ignore")
        hub_rec = rec.idxmax() if len(rec) else None

        # ajustes con todos los socios posibles (misma ventana)
        top_excl = set(por_socio.index[:TOP_EXCLUIR])
        socios = {}
        for c in pib.columns:
            if c == nodo:
                continue
            f = ajuste(pib, c, nodo, y0, pobl=pobl)
            if f is not None:
                socios[c] = f

        def controles(h, fh):
            cand = [(abs(f["g"] - fh["g"]), c, f["b"]) for c, f in socios.items()
                    if c not in top_excl and c != h
                    and f["n"] >= COBERTURA_CONTROL * fh["n"]
                    and abs(f["g"] - fh["g"]) <= CALIPER]
            cand.sort()
            return cand[:K_CONTROLES]

        ctl = controles(hub, fit_h)
        d = fit_h["b"] - np.mean([c[2] for c in ctl]) if ctl else np.nan
        d_comp = np.nan
        if hub_comp is not None:
            fc = socios.get(hub_comp)
            ctl_c = controles(hub_comp, fc) if fc else []
            if ctl_c:
                d_comp = fc["b"] - np.mean([c[2] for c in ctl_c])

        filas.append(dict(
            nodo=nodo, estado="ok", y0=y0, ref_fin=y0 + DECADA - 1,
            destino1_cow=top_raw,
            destino1_sin_entidad=socio_maddison(top_raw, y0, entidades) is None,
            share_destino1_cow=por_socio_raw.iloc[0] / total_ref,
            hub=hub, share_hub=float(share[hub]),
            hub_aprox=hub in aprox_socios,
            anios_ref_con_export_urss=anios_urss, cmea_dudoso=cmea_dudoso,
            hub_mas_rico=fit_h["g"] > 0, g=fit_h["g"],
            b=fit_h["b"], r2=fit_h["r2"], p=fit_h["p"], dw=fit_h["dw"],
            n=fit_h["n"], year_min=fit_h["year_min"], year_max=fit_h["year_max"],
            n_controles=len(ctl),
            b_controles=np.mean([c[2] for c in ctl]) if ctl else np.nan,
            controles="; ".join(c[1] for c in ctl), d=d,
            hub_ventana_completa=hub_comp, d_ventana_completa=d_comp,
            hub_2005_2014=hub_rec,
            par_en_B=(hub, nodo) in parB,
            b_en_B=parB.get((hub, nodo), np.nan),
            par_invertido_en_B=(nodo, hub) in parB,
        ))

        # prueba 2: dentro del nodo, socios más ricos con registro comercial
        conocidos = set(mapeado.socio) - {nodo}
        xs = [(f["b"], float(share.get(c, 0.0)), f["g"], f["tam"])
              for c, f in socios.items()
              if c in conocidos and f["g"] > 0
              and f["n"] >= COBERTURA_CONTROL * fit_h["n"]]
        if len(xs) >= MIN_SOCIOS_INTRA:
            arr = np.array(xs)
            fila = dict(nodo=nodo, n_socios=len(xs),
                        rho_parcial=partial_spearman(arr[:, 0], arr[:, 1],
                                                     arr[:, 2]),
                        rho_simple=stats.spearmanr(arr[:, 0], arr[:, 1])[0],
                        rho_parcial_gravedad=np.nan, n_socios_gravedad=0)
            conpob = arr[~np.isnan(arr[:, 3])]
            if len(conpob) >= MIN_SOCIOS_INTRA:
                fila.update(rho_parcial_gravedad=partial_spearman(
                    conpob[:, 0], conpob[:, 1], conpob[:, 2], conpob[:, 3]),
                    n_socios_gravedad=len(conpob))
            intra.append(fila)

    N = pd.DataFrame(filas)
    ok = N[N.estado == "ok"].copy()
    log.info("-" * 78)
    log.info("Nodos con hub emergente: %d de %d", len(ok), len(N))
    for est, k in N[N.estado != "ok"].estado.value_counts().items():
        log.info("  sin reconstruir (%s): %d -> %s", est, k,
                 ", ".join(N.loc[N.estado == est, "nodo"]))
    for c in ["destino1_sin_entidad", "hub_aprox", "hub_mas_rico", "par_en_B",
              "par_invertido_en_B", "cmea_dudoso"]:
        ok[c] = ok[c].astype(bool)
    log.info("Primer destino COW sin entidad Maddison del mismo territorio "
             "(se usa el siguiente): %d nodos -> %s",
             int(ok.destino1_sin_entidad.sum()),
             ", ".join(f"{n} ({d})" for n, d in zip(
                 ok.loc[ok.destino1_sin_entidad, "nodo"],
                 ok.loc[ok.destino1_sin_entidad, "destino1_cow"])) or "ninguno")
    log.info("Año de inicio de la década de referencia: mediana %d, rango %d-%d",
             int(ok.y0.median()), int(ok.y0.min()), int(ok.y0.max()))
    log.info("Participación del hub en las exportaciones (referencia): mediana "
             "%.1f%%, rango %.1f%%-%.1f%%", 100 * ok.share_hub.median(),
             100 * ok.share_hub.min(), 100 * ok.share_hub.max())
    log.info("Hubs emergentes distintos: %d", ok.hub.nunique())
    for h, k in ok.hub.value_counts().head(12).items():
        log.info("  %-28s %2d nodos", h, k)
    log.info("Hub aproximado (RFA -> Germany): %d nodos", int(ok.hub_aprox.sum()))
    dud = ok[ok.cmea_dudoso]
    log.info("Cobertura CMEA dudosa (URSS sin flujo positivo en >= 5 de 10 años "
             "de referencia): %d nodos -> %s", len(dud),
             ", ".join(f"{n} {int(y)} (hub COW: {h}; años con export. a URSS: "
                       f"{int(k)}/10)" for n, y, h, k in zip(
                           dud.nodo, dud.y0, dud.hub,
                           dud.anios_ref_con_export_urss)) or "ninguno")

    log.info("-" * 78)
    log.info("DESCRIPTIVOS")
    rico = ok[ok.hub_mas_rico]
    log.info("Hub más rico que el nodo al inicio: %d/%d (%.0f%%)", len(rico),
             len(ok), 100 * len(rico) / len(ok))
    log.info("b (todos): media %+.3f, mediana %+.3f | b>0: %d/%d", ok.b.mean(),
             ok.b.median(), int((ok.b > 0).sum()), len(ok))
    log.info("b (hub más rico): media %+.3f, mediana %+.3f | b>0 (diverge): %d/%d",
             rico.b.mean(), rico.b.median(), int((rico.b > 0).sum()), len(rico))
    log.info("DW mediana %.3f | p<0.05 nominal: %d/%d", ok.dw.median(),
             int((ok.p < 0.05).sum()), len(ok))
    rho, p = stats.spearmanr(ok.g, ok.b)
    log.info("ρ(b, brecha inicial g) = %+.3f (p = %.3g, n = %d)  [B publicado: -0.489]",
             rho, p, len(ok))
    log.info("Par (hub, nodo) presente en el dominio B publicado: %d | invertido: %d "
             "| ausente: %d", int(ok.par_en_B.sum()), int(ok.par_invertido_en_B.sum()),
             int((~ok.par_en_B & ~ok.par_invertido_en_B).sum()))
    cmp_ = ok.dropna(subset=["b_en_B"])
    if len(cmp_) >= 5:
        log.info("  en los %d pares comunes: ρ(b_nuevo, b_B) = %+.3f (ventanas distintas)",
                 len(cmp_), stats.spearmanr(cmp_.b, cmp_.b_en_B)[0])
    cambia = ok.dropna(subset=["hub_2005_2014"])
    log.info("Hub 2005-2014 distinto del hub de referencia: %d/%d",
             int((cambia.hub_2005_2014 != cambia.hub).sum()), len(cambia))

    log.info("-" * 78)
    log.info("PRUEBA 1 — hub vs controles emparejados por brecha "
             "(K=%d, caliper %.2f, excluye top-%d) — SNT predice d > 0",
             K_CONTROLES, CALIPER, TOP_EXCLUIR)
    log.info("Nodos con al menos 1 control: %d/%d (controles por nodo: mediana %d)",
             int(ok.d.notna().sum()), len(ok),
             int(ok.loc[ok.d.notna(), "n_controles"].median()))
    resumen_d(ok, "todos")
    resumen_d(rico, "hub más rico")
    resumen_d(ok[~ok.hub_aprox], "sin hub aproximado")
    resumen_d(ok[~ok.cmea_dudoso], "sin cobertura CMEA dudosa")
    resumen_d(ok.assign(d=ok.d_ventana_completa, hub=ok.hub_ventana_completa),
              "hub de ventana completa (endógeno)")

    log.info("-" * 78)
    log.info("PRUEBA 2 — dentro de cada nodo: ρ parcial(b, participación | g) "
             "entre socios más ricos — SNT predice ρ > 0")
    I = pd.DataFrame(intra)
    if len(I) >= 5:
        v = I.rho_parcial.dropna()
        w = stats.wilcoxon(v)
        s = stats.binomtest(int((v > 0).sum()), len(v), 0.5)
        log.info("Nodos: %d (socios por nodo: mediana %d) | ρ parcial mediana %+.3f, "
                 "media %+.3f | ρ>0 en %d/%d | Wilcoxon p = %.4g | signo p = %.4g",
                 len(v), int(I.n_socios.median()), v.median(), v.mean(),
                 int((v > 0).sum()), len(v), w.pvalue, s.pvalue)
        vs = I.rho_simple.dropna()
        log.info("ρ simple (sin controlar g): mediana %+.3f | ρ>0 en %d/%d | "
                 "Wilcoxon p = %.4g", vs.median(), int((vs > 0).sum()), len(vs),
                 stats.wilcoxon(vs).pvalue)
        # permutación: invierte signos al azar (nulo simétrico) sobre la media
        rng = np.random.default_rng(SEED)
        obs = v.mean()
        perm = np.array([(v.values * rng.choice([-1, 1], len(v))).mean()
                         for _ in range(10000)])
        log.info("Permutación de signos sobre la media (10000, semilla %d): "
                 "p bilateral = %.4g", SEED,
                 float(np.mean(np.abs(perm) >= abs(obs))))
        vg = I.rho_parcial_gravedad.dropna()
        if len(vg) >= 5:
            log.info("Con control de gravedad (g + log PIB total del socio): "
                     "nodos %d | ρ parcial mediana %+.3f, media %+.3f | ρ>0 en "
                     "%d/%d | Wilcoxon p = %.4g | signo p = %.4g", len(vg),
                     vg.median(), vg.mean(), int((vg > 0).sum()), len(vg),
                     stats.wilcoxon(vg).pvalue,
                     stats.binomtest(int((vg > 0).sum()), len(vg), 0.5).pvalue)
        log.info("Nota: los socios ricos (EE.UU., Reino Unido, ...) se repiten en "
                 "casi todos los nodos, así que los nodos no son unidades "
                 "independientes; los p de esta prueba son optimistas.")

    for c in ["share_destino1_cow", "share_hub", "g", "b", "r2", "p", "dw",
              "b_controles", "d", "d_ventana_completa", "b_en_B"]:
        if c in N:
            N[c] = N[c].astype(float).round(6)
    N.to_csv(OUT_NODOS, index=False)
    I.round(6).to_csv(OUT_INTRA, index=False)
    log.info("-" * 78)
    log.info("CSV -> %s (%d filas) | SHA-256 %s", OUT_NODOS.relative_to(ROOT),
             len(N), sha256(OUT_NODOS))
    log.info("CSV -> %s (%d filas) | SHA-256 %s", OUT_INTRA.relative_to(ROOT),
             len(I), sha256(OUT_INTRA))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
