"""
Punto 1 del pre-registro 2026-09-27 — hub VARIABLE en el tiempo (pares de países).

Pre-registro: `reconstruction_real/preregistro/PREREGISTRO_2026-09-27.md`.

Pregunta: ¿el país diverge de su hub comercial VIGENTE más que de un país con
la misma brecha inicial con el que casi no comercia?

Diseño (fijado en el pre-registro)
----------------------------------
* Nodos: los 103 países del dominio B publicado.
* Arranques s = 1900, 1910, ..., 1990. hub_s = socio con la mayor suma de
  exportaciones del nodo en la ventana previa [s-4, s] (COW desde 1870, mismas
  reglas de entidad y de mapeo a Maddison 2020 que la reconstrucción estática).
* Trayectoria R(t) = PIBpc_hub / PIBpc_nodo en [s, s+H-1]; t = 1..n sobre las
  observaciones comunes (igual que `calc()` de `expand_B_massive.py`).
  H = 20 (principal); 10 y 30 (sensibilidad). Mínimo de observaciones:
  15 para H = 20 (pre-registro); para 10 y 30 se usa la misma proporción,
  ceil(0.75·H) = 8 y 23 (el pre-registro no lo fijaba; se anota en el informe).
* Controles: socios con serie Maddison fuera de los 5 principales destinos del
  nodo en [s-4, s], n >= 90% del hub, |Δg| <= 0.25 (g = media de log R en las 5
  primeras observaciones), K = 5 más cercanos en g. d = b_hub - media(b_ctrl).
* Marca CMEA: miembro del CMEA, 1949 <= s <= 1991 y exportaciones a la URSS
  faltantes o cero en >= 3 de los 5 años de la ventana previa.

Pruebas
-------
Principal (H1: d > 0): media de d por nodo -> Wilcoxon de una cola sobre nodos.
Secundarias: media de d por hub (Wilcoxon), solo hub más rico (g > 0), sin
marcas CMEA, H = 10 y 30; descriptivos (b > 0 con hub más rico, cambios de hub).
Decisión: respaldada si p < 0.05 y mediana por hub > 0; contraria si la prueba
de dos colas da p < 0.05 con d < 0; no respaldada en otro caso.

Salidas
-------
    reconstruction_real/data/hub_temporal_espacios.csv   (1 fila por nodo × arranque × H)
    reconstruction_real/logs/prueba_hub_temporal_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/prueba_hub_temporal.py
"""

import logging
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comercio_maddison import (CMEA, ROOT, cargar_pib,  # noqa: E402
                               leer_cow, sha256)

DATA_RR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
IN_B = DATA_RR / "by_domain" / "dominio_B_real.csv"
OUT = DATA_RR / "hub_temporal_espacios.csv"
LOG_FILE = LOG_DIR / "prueba_hub_temporal_log.txt"

ARRANQUES = list(range(1900, 1991, 10))
VENTANA_PREVIA = 5          # [s-4, s]
HORIZONTES = [20, 10, 30]   # el primero es el principal
N_BRECHA = 5
TOP_EXCLUIR = 5
K_CONTROLES = 5
CALIPER = 0.25
COBERTURA_CONTROL = 0.9
ANIO_COW = 1870
SEED = 20260927

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("HUB-TEMPORAL")


def ajuste_np(yh, yn, n_min):
    """b, g y n de log(yh/yn) contra log(t), t = 1..n sobre los años comunes."""
    ok = ~(np.isnan(yh) | np.isnan(yn))
    n = int(ok.sum())
    if n < n_min:
        return None
    lR = np.log(yh[ok] / yn[ok])
    lt = np.log(np.arange(1, n + 1))
    ltc = lt - lt.mean()
    b = float(np.sum(ltc * (lR - lR.mean())) / np.sum(ltc ** 2))
    return b, float(np.mean(lR[:N_BRECHA])), n


def pruebas(E, etiqueta):
    """Principal por nodo y secundaria por hub sobre un conjunto de espacios."""
    x = E.dropna(subset=["d"])
    if len(x) == 0:
        log.info("[%s] sin espacios con controles", etiqueta)
        return None
    nodo = x.groupby("nodo")["d"].mean()
    hub = x.groupby("hub")["d"].mean()
    out = dict(espacios=len(x), nodos=len(nodo), hubs=len(hub),
               d_mediana_nodo=float(nodo.median()),
               d_pos_nodo=int((nodo > 0).sum()),
               d_mediana_hub=float(hub.median()) if len(hub) else np.nan)
    if len(nodo) >= 5:
        out["p1_nodo"] = float(stats.wilcoxon(nodo, alternative="greater").pvalue)
        out["p2_nodo"] = float(stats.wilcoxon(nodo).pvalue)
    if len(hub) >= 5:
        out["p1_hub"] = float(stats.wilcoxon(hub, alternative="greater").pvalue)
        out["d_pos_hub"] = int((hub > 0).sum())
    log.info("[%s] espacios %d | nodos %d: d mediana %+.4f, d>0 en %d/%d, "
             "Wilcoxon 1 cola p = %.4g (2 colas p = %.4g) | hubs %d: d mediana "
             "%+.4f, d>0 en %s/%d, Wilcoxon 1 cola p = %s",
             etiqueta, len(x), len(nodo), out["d_mediana_nodo"],
             out["d_pos_nodo"], len(nodo), out.get("p1_nodo", np.nan),
             out.get("p2_nodo", np.nan), len(hub), out["d_mediana_hub"],
             out.get("d_pos_hub", "-"), len(hub),
             f"{out['p1_hub']:.4g}" if "p1_hub" in out else "-")
    return out


def decision(res):
    if res is None or "p1_nodo" not in res:
        return "sin datos suficientes"
    if res["p1_nodo"] < 0.05 and res["d_mediana_hub"] > 0:
        return "RESPALDADA"
    if res["p2_nodo"] < 0.05 and res["d_mediana_nodo"] < 0:
        return "CONTRARIA"
    return "NO RESPALDADA"


def main():
    log.info("=" * 78)
    log.info("PUNTO 1 (pre-registro 2026-09-27) — HUB VARIABLE EN EL TIEMPO")
    log.info("=" * 78)
    M, pib = cargar_pib(log)
    entidades = set(pib.columns)
    anios = pib.index.values
    cols = list(pib.columns)
    P = pib.values
    col_i = {c: i for i, c in enumerate(cols)}
    B = pd.read_csv(IN_B)
    nodos = sorted(set(B.hub) | set(B.nodo))
    log.info("Nodos (países del dominio B): %d | arranques %s | horizontes %s",
             len(nodos), ARRANQUES, HORIZONTES)

    exp = leer_cow(entidades, ANIO_COW, log)
    exp = exp[exp.nodo.isin(nodos)]

    filas = []
    for nodo in nodos:
        if nodo not in col_i:
            continue
        e = exp[exp.nodo == nodo]
        yn_all = P[:, col_i[nodo]]
        hub_prev = None
        for s in ARRANQUES:
            prev = e[(e.anio >= s - VENTANA_PREVIA + 1) & (e.anio <= s)]
            if prev.v.sum() <= 0:
                continue
            total = prev.v.sum()
            mapeado = prev.dropna(subset=["socio"])
            por_socio = mapeado.groupby("socio")["v"].sum().drop(
                nodo, errors="ignore").sort_values(ascending=False)
            top = set(por_socio.index[:TOP_EXCLUIR])
            anios_urss = prev.loc[(prev.socio == "Former USSR") & (prev.v > 0),
                                  "anio"].nunique()
            cmea = (nodo in CMEA and 1949 <= s <= 1991 and anios_urss < 3)
            for H in HORIZONTES:
                n_min = 15 if H == 20 else math.ceil(0.75 * H)
                sel = (anios >= s) & (anios <= s + H - 1)
                yn = yn_all[sel]
                hub = fit_h = None
                for cand in por_socio.index:
                    if cand not in col_i:
                        continue
                    f = ajuste_np(P[sel, col_i[cand]], yn, n_min)
                    if f is not None:
                        hub, fit_h = cand, f
                        break
                if hub is None:
                    continue
                ctl = []
                for c in cols:
                    if c == nodo or c == hub or c in top:
                        continue
                    f = ajuste_np(P[sel, col_i[c]], yn, n_min)
                    if (f is None or f[2] < COBERTURA_CONTROL * fit_h[2]
                            or abs(f[1] - fit_h[1]) > CALIPER):
                        continue
                    ctl.append((abs(f[1] - fit_h[1]), c, f[0]))
                ctl.sort()
                ctl = ctl[:K_CONTROLES]
                filas.append(dict(
                    nodo=nodo, arranque=s, H=H, hub=hub,
                    share_hub=float(por_socio[hub] / total),
                    hub_cambia=(H == HORIZONTES[0] and hub_prev is not None
                                and hub != hub_prev),
                    b=fit_h[0], g=fit_h[1], n=fit_h[2],
                    hub_mas_rico=fit_h[1] > 0, cmea_dudoso=cmea,
                    n_controles=len(ctl),
                    b_controles=np.mean([c[2] for c in ctl]) if ctl else np.nan,
                    controles="; ".join(c[1] for c in ctl),
                    d=fit_h[0] - np.mean([c[2] for c in ctl]) if ctl else np.nan))
                if H == HORIZONTES[0]:
                    hub_prev = hub

    E = pd.DataFrame(filas)
    log.info("-" * 78)
    resultados = {}
    for H in HORIZONTES:
        EH = E[E.H == H]
        log.info("HORIZONTE H = %d años: %d espacios nodo×arranque, %d nodos, "
                 "%d hubs distintos, %d con controles", H, len(EH),
                 EH.nodo.nunique(), EH.hub.nunique(), int(EH.d.notna().sum()))
        resultados[H] = pruebas(EH, f"H={H} todos")
        if H == HORIZONTES[0]:
            ric = EH[EH.hub_mas_rico]
            log.info("  hub más rico: %d/%d espacios | b > 0 (diverge) en %d/%d "
                     "| b mediana %+.4f", len(ric), len(EH), int((ric.b > 0).sum()),
                     len(ric), ric.b.median())
            log.info("  cambios de hub entre arranques consecutivos: %d | nodos "
                     "con al menos un cambio: %d/%d", int(EH.hub_cambia.sum()),
                     EH[EH.hub_cambia].nodo.nunique(), EH.nodo.nunique())
            for h, k in EH.hub.value_counts().head(10).items():
                log.info("    hub %-24s %3d espacios", h, k)
            pruebas(ric, f"H={H} hub más rico")
            pruebas(EH[~EH.cmea_dudoso], f"H={H} sin CMEA dudoso")
            log.info("  marcas CMEA dudoso: %d espacios (%s)",
                     int(EH.cmea_dudoso.sum()),
                     ", ".join(sorted(set(EH.loc[EH.cmea_dudoso, "nodo"] + " "
                                          + EH.loc[EH.cmea_dudoso, "arranque"]
                                          .astype(str)))) or "ninguno")
            por_dec = EH.dropna(subset=["d"]).groupby("arranque")["d"].agg(
                ["count", "median"])
            for s, r in por_dec.iterrows():
                log.info("    arranque %d: %3d espacios, d mediana %+.4f",
                         s, int(r["count"]), r["median"])
        log.info("-" * 78)

    log.info("DECISIÓN PRE-REGISTRADA (H = %d, principal): %s", HORIZONTES[0],
             decision(resultados[HORIZONTES[0]]))
    for H in HORIZONTES[1:]:
        log.info("  sensibilidad H = %d: %s", H, decision(resultados[H]))

    for c in ["share_hub", "b", "g", "b_controles", "d"]:
        E[c] = E[c].astype(float).round(6)
    E.to_csv(OUT, index=False)
    log.info("CSV -> %s (%d filas) | SHA-256 %s", OUT.relative_to(ROOT), len(E),
             sha256(OUT))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
