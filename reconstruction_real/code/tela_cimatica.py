#!/usr/bin/env python3
"""
CAPA CIMÁTICA DE LA TELA DE INCERTIDUMBRE — SNT v34 (Axioma 0.1 + 0.2)
=======================================================================

Lee la tela (data/tela_de_incertidumbre.csv, 7306 puntos) y produce la
lectura cimática del cubo C(u, m, tau):

  * La placa   : mapa de densidad (tau x log10 m) de los 7306 puntos —
                 dónde se acumula la arena.
  * La figura  : trayectoria mediana de log10 m(tau) por dominio, con banda
                 IQR — la figura que dibuja cada "tono" (phi fricción).
  * Los tonos  : espectro FFT (armónicos 1..16 de la fase tau) de cada
                 trayectoria, mediana por dominio — el tono resonante.
  * Las huellas: CSV por dominio con m en tau=0/0.25/0.5/0.75/1, amplitud
                 espectral A1/A2/A3, m_max — la tabla de identificación.
  * La prueba  : clasificación leave-one-out por centroide más cercano
                 (forma de la trayectoria sola) — ¿viendo la figura se
                 identifica el dominio?

Honestidad declarada:
  - Las sombras (dominios sin serie cruda) son curvas del modelo R=t^b
    (a=1): su forma está determinada por (b, n). m(tau=0)=1 por
    construcción — por eso la prueba se corre DOS veces: con todos los
    rasgos y SOLO-FORMA (sin tau=0).
  - Solo ACO (18 casos, 109 puntos) tiene serie (t, R) real.

Salidas:
  figures/fig_tela_cimatica_chladni.{png,svg}
  figures/fig_tela_cimatica_tonos.{png,svg}
  data/tela_cimatica_huellas.csv
  data/tela_cimatica_clasificacion.csv
  logs/tela_cimatica_log.txt
"""

import os
import logging

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import rcParams  # noqa: E402
from scipy.ndimage import gaussian_filter  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
FIG_DIR = os.path.join(SCRIPT_DIR, "..", "..", "figures")
LOG_DIR = os.path.join(SCRIPT_DIR, "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(
            os.path.join(LOG_DIR, "tela_cimatica_log.txt"), mode="w"
        ),
    ],
)
log = logging.getLogger("tela_cimatica")

rcParams.update({
    "font.family": "Liberation Sans",
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 7,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "axes.linewidth": 0.8,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

N_GRID = 32
TAU_GRID = np.linspace(0.0, 1.0, N_GRID)

PALETA = {
    "A": "#E69F00", "ACO": "#000000", "B": "#56B4E9", "C": "#009E73",
    "D": "#F0E442", "E1": "#0072B2", "E2": "#D55E00", "E3": "#CC79A7",
    "F1": "#8B4513", "F2": "#7F7F7F", "F3": "#17BECF",
}

ETIQUETAS = {
    "A": "A ciudades", "ACO": "ACO colapsos", "B": "B países",
    "C": "C estados EEUU", "D": "D HackerEarth", "E1": "E1 territorial",
    "E2": "E2 biológico", "E3": "E3 epidémico", "F1": "F1 impacto",
    "F2": "F2 parametrización", "F3": "F3 integración",
}


def cargar_tela():
    ruta = os.path.join(DATA_DIR, "tela_de_incertidumbre.csv")
    df = pd.read_csv(ruta)
    log.info("Tela cargada: %d puntos, %d casos, %d dominios",
             len(df), df["id"].nunique(), df["dominio"].nunique())
    if (df["m"] <= 0).any():
        malos = int((df["m"] <= 0).sum())
        log.warning("m<=0 en %d puntos: excluidos del analisis log", malos)
        df = df[df["m"] > 0]
    return df


def trayectorias(df):
    """Interpola log10 m(tau) de cada caso a la retícula común TAU_GRID."""
    trajs = {}
    for (dom, cid), g in df.groupby(["dominio", "id"], sort=False):
        g = g.sort_values("tau")
        tau = g["tau"].to_numpy(dtype=float)
        lm = np.log10(g["m"].to_numpy(dtype=float))
        if len(tau) > 1:
            tau_u, idx = np.unique(tau, return_index=True)
            lm = lm[idx]
        else:
            tau_u = np.array([tau[0]])
            lm = np.array([lm[0]])
        if tau_u[-1] > tau_u[0]:
            interp = np.interp(TAU_GRID, tau_u, lm)
        else:
            interp = np.full_like(TAU_GRID, lm[0])
        fuente = g["fuente"].iloc[0]
        trajs[(dom, cid)] = {"lm": interp, "fuente": fuente}
    log.info("Trayectorias interpoladas: %d casos en retícula de %d fases",
             len(trajs), N_GRID)
    return trajs


def espectro(lm):
    """FFT real de la trayectoria log10 m(tau); amplitudes de armónicos 1..16."""
    coef = np.fft.rfft(lm - lm.mean())
    return np.abs(coef)[1:]


def rasgos(lm):
    """Vector de rasgos de un caso: m en 5 fases + 3 armónicos (log10)."""
    fases = [0.0, 0.25, 0.5, 0.75, 1.0]
    en_fase = [lm[int(round(f * (N_GRID - 1)))] for f in fases]
    amps = espectro(lm)[:3].tolist()
    return en_fase + amps


def clasificacion_loo(casos, usar_tau0=True, por_phi=False):
    """Leave-one-out por centroide cercano. Devuelve (df_pred, resumen).

    por_phi=False clasifica por dominio; por_phi=True clasifica por tono
    (phi de friccion) — la prediccion cimatica: la figura identifica el
    tono, no el instrumento.
    """
    if por_phi:
        claves = {(d, c): casos[(d, c)]["phi"] for (d, c) in casos}
    else:
        claves = {(d, c): d for (d, c) in casos}
    grupos = sorted(set(claves.values()))
    filas = []
    for (dom, cid), r in sorted(casos.items()):
        x = np.array(r["rasgos" if usar_tau0 else "rasgos_forma"],
                     dtype=float)
        filas.append({"id": cid, "dominio": dom, "grupo": claves[(dom, cid)],
                      "x": x})
    X = np.stack([f["x"] for f in filas])
    mu, sd = X.mean(axis=0), X.std(axis=0)
    sd[sd == 0] = 1.0
    Xz = (X - mu) / sd

    grupos_evaluables = sorted({
        f["grupo"] for f in filas
        if sum(1 for g in filas if g["grupo"] == f["grupo"]) >= 2
    })
    preds = []
    for i, f in enumerate(filas):
        if f["grupo"] not in grupos_evaluables:
            preds.append((f, "no_evaluable", np.nan))
            continue
        centroidas = {}
        for g_ in grupos:
            otros = [Xz[j] for j, g2 in enumerate(filas)
                     if g2["grupo"] == g_ and j != i]
            if otros:
                centroidas[g_] = np.mean(otros, axis=0)
        dists = {g_: float(np.linalg.norm(Xz[i] - c))
                 for g_, c in centroidas.items()}
        pred = min(dists, key=dists.get)
        preds.append((f, pred, dists[pred]))

    correctos = sum(1 for f, p, _ in preds
                    if p != "no_evaluable" and p == f["grupo"])
    evaluables = sum(1 for f, p, _ in preds if p != "no_evaluable")
    acc = correctos / evaluables if evaluables else float("nan")

    df_pred = pd.DataFrame([{
        "id": f["id"], "dominio": f["dominio"], "grupo_real": f["grupo"],
        "predicho": p,
        "correcto": int(p == f["grupo"]) if p != "no_evaluable" else "",
        "distancia_min": dist,
    } for f, p, dist in preds])

    log.info("LOO por %s (%s): %d evaluables, %d correctos → exactitud %.1f%%",
             "TONO φ" if por_phi else "dominio",
             "todos los rasgos" if usar_tau0 else "solo-forma (sin tau=0)",
             evaluables, correctos, 100 * acc)

    por_g = {}
    for g_ in grupos_evaluables:
        n = sum(1 for f, p, _ in preds if f["grupo"] == g_)
        ok = sum(1 for f, p, _ in preds
                 if f["grupo"] == g_ and p == g_)
        por_g[g_] = (ok, n)
    log.info("Por grupo: " + " | ".join(
        f"{g_} {ok}/{n}" for g_, (ok, n) in por_g.items()))

    return df_pred, acc, por_g, grupos_evaluables


def figura_chladni(df, trajs):
    """Placa continua: densidad desde trayectorias interpoladas.

    Cada caso se muestrea en 200 fases (interpolación lineal de su serie)
    con peso 1/n_muestras por punto — la densidad cuenta CASOS que pasan
    por cada celda, no puntos crudos. Esto elimina la rejilla discreta de
    las sombras (las 'peras' en columnas tau = k/9) y deja solo el abanico
    físico.
    """
    fig, (axa, axb) = plt.subplots(
        1, 2, figsize=(9.0, 4.0), gridspec_kw={"width_ratios": [1.1, 1.0]})

    tau_densa = np.linspace(0.0, 1.0, 200)
    taus, lms, pesos = [], [], []
    for r in trajs.values():
        lm_d = np.interp(tau_densa, TAU_GRID, r["lm"])
        taus.append(tau_densa)
        lms.append(lm_d)
        pesos.append(np.full_like(tau_densa, 1.0 / len(tau_densa)))
    tau_todos = np.concatenate(taus)
    lm_todos = np.concatenate(lms)
    w = np.concatenate(pesos)

    nb_t, nb_m = 100, 80
    H, xe, ye = np.histogram2d(
        tau_todos, lm_todos, bins=[nb_t, nb_m], weights=w,
        range=[[0, 1], [lm_todos.min(), lm_todos.max()]])
    Hs = gaussian_filter(H, sigma=1.5)
    pc = axa.pcolormesh(xe, ye, Hs.T, cmap="magma", shading="auto")
    fig.colorbar(pc, ax=axa, label="densidad (suavizada)")
    niveles = [Hs.max() * 0.02]
    cs = axa.contour((xe[:-1] + xe[1:]) / 2, (ye[:-1] + ye[1:]) / 2,
                     Hs.T, levels=niveles, colors="#00FFFF",
                     linewidths=0.7, linestyles="--")
    axa.clabel(cs, fmt="línea nodal", fontsize=6)
    aco = df[df["dominio"] == "ACO"]
    axa.scatter(aco["tau"], np.log10(aco["m"]), s=2, c="white",
                edgecolors="none", alpha=0.7, label="ACO real (109 pts)")
    axa.set_xlabel("τ fase temporal normalizada")
    axa.set_ylabel("log₁₀ m  (m = R)")
    axa.set_title("A · La placa continua: densidad de casos "
                  "(200 fases interpoladas)")
    axa.legend(loc="lower right", framealpha=0.7)

    for dom in sorted({d for (d, _) in trajs}):
        lms = np.stack([r["lm"] for (d, _), r in trajs.items() if d == dom])
        med = np.median(lms, axis=0)
        q1, q3 = np.percentile(lms, [25, 75], axis=0)
        estilo = "-" if dom != "ACO" else "-"
        lw = 2.2 if dom == "ACO" else 1.2
        axb.plot(TAU_GRID, med, estilo, color=PALETA[dom], lw=lw,
                 label=f"{ETIQUETAS[dom]} (n={lms.shape[0]})")
        axb.fill_between(TAU_GRID, q1, q3, color=PALETA[dom], alpha=0.10,
                         linewidth=0)
    axb.set_xlabel("τ fase temporal normalizada")
    axb.set_ylabel("log₁₀ m mediana (banda IQR)")
    axb.set_title("B · La figura: trayectoria por dominio")
    axb.legend(loc="upper left", framealpha=0.85, fontsize=6,
               handlelength=1.2)
    fig.suptitle("Tela de incertidumbre C(u, m, tau) — lectura cimática "
                 "(7306 puntos, 739 casos)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(FIG_DIR, f"fig_tela_cimatica_chladni.{ext}"),
                    format=ext, bbox_inches="tight", dpi=300)
    plt.close(fig)
    log.info("Figura chladni escrita en %s", FIG_DIR)


def figura_tonos(trajs):
    fig, ax = plt.subplots(figsize=(7.0, 4.0))
    for dom in sorted({d for (d, _) in trajs}):
        espec = np.stack([espectro(r["lm"]) for (d, _), r in trajs.items()
                          if d == dom])
        med = np.median(espec, axis=0)
        arm = np.arange(1, len(med) + 1)
        ax.plot(arm, med, "o-", color=PALETA[dom], lw=1.4, ms=3.5,
                label=f"{ETIQUETAS[dom]} (n={espec.shape[0]})")
    ax.set_xlabel("armónico de la fase τ (1 … 16)")
    ax.set_ylabel("amplitud FFT mediana de log₁₀ m(τ)")
    ax.set_yscale("log")
    ax.set_title("Los tonos: espectro mediano por dominio — "
                 "la firma resonante de cada φ")
    ax.legend(fontsize=6.5, framealpha=0.85, ncol=2)
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(FIG_DIR, f"fig_tela_cimatica_tonos.{ext}"),
                    format=ext, bbox_inches="tight", dpi=300)
    plt.close(fig)
    log.info("Figura tonos escrita en %s", FIG_DIR)


def main():
    log.info("=" * 78)
    log.info("CAPA CIMÁTICA DE LA TELA — SNT v34")
    log.info("=" * 78)

    df = cargar_tela()
    trajs = trayectorias(df)

    casos = {}
    for (dom, cid), r in trajs.items():
        ras = rasgos(r["lm"])
        phi = df[(df["dominio"] == dom) & (df["id"] == cid)][
            "phi_friccion"].iloc[0]
        casos[(dom, cid)] = {
            "lm": r["lm"], "fuente": r["fuente"], "phi": phi,
            "rasgos": ras, "rasgos_forma": ras[1:],
        }

    reales = sum(1 for r in casos.values() if r["fuente"] == "serie_cruda")
    sombras = len(casos) - reales
    log.info("Casos: %d reales (serie cruda ACO) + %d sombras (modelo t^b)",
             reales, sombras)

    filas_h = []
    for dom in sorted({d for (d, _) in casos}):
        lms = np.stack([r["lm"] for (d, _), r in casos.items() if d == dom])
        espec = np.stack([espectro(r["lm"]) for (d, _), r in casos.items()
                          if d == dom])
        fases = [0.0, 0.25, 0.5, 0.75, 1.0]
        med_f = [float(np.median(lms[:, int(round(f * (N_GRID - 1)))]))
                 for f in fases]
        filas_h.append({
            "dominio": dom,
            "n_casos": lms.shape[0],
            "etiqueta": ETIQUETAS.get(dom, dom),
            "log_m_tau0": med_f[0], "log_m_tau25": med_f[1],
            "log_m_tau50": med_f[2], "log_m_tau75": med_f[3],
            "log_m_tau100": med_f[4],
            "log_m_max_mediana": float(np.median(lms.max(axis=1))),
            "amp_A1_mediana": float(np.median(espec[:, 0])),
            "amp_A2_mediana": float(np.median(espec[:, 1])),
            "amp_A3_mediana": float(np.median(espec[:, 2])),
        })
    df_h = pd.DataFrame(filas_h)
    ruta_h = os.path.join(DATA_DIR, "tela_cimatica_huellas.csv")
    df_h.to_csv(ruta_h, index=False)
    log.info("Huellas por dominio → %s", ruta_h)

    log.info("--- Prueba de identificación: ¿viendo la figura se reconoce "
             "el dominio? ---")
    df1, acc1, _, _ = clasificacion_loo(casos, usar_tau0=True)
    df2, acc2, _, _ = clasificacion_loo(casos, usar_tau0=False)
    log.info("Exactitud por dominio — todos los rasgos: %.1f%% | "
             "solo-forma: %.1f%%", 100 * acc1, 100 * acc2)
    ruta_c = os.path.join(DATA_DIR, "tela_cimatica_clasificacion.csv")
    df1.to_csv(ruta_c, index=False)
    log.info("Predicciones LOO por dominio → %s", ruta_c)

    log.info("--- Prueba cimática: ¿la figura identifica el TONO (φ)? ---")
    df3, acc3, _, _ = clasificacion_loo(casos, usar_tau0=True, por_phi=True)
    df4, acc4, _, _ = clasificacion_loo(casos, usar_tau0=False, por_phi=True)
    log.info("Exactitud por tono φ — todos los rasgos: %.1f%% | "
             "solo-forma: %.1f%%", 100 * acc3, 100 * acc4)
    ruta_p = os.path.join(DATA_DIR, "tela_cimatica_clasificacion_phi.csv")
    df3.to_csv(ruta_p, index=False)
    log.info("Predicciones LOO por tono φ → %s", ruta_p)

    figura_chladni(df, trajs)
    figura_tonos(trajs)

    log.info("EJECUCION COMPLETADA — capa cimática")


if __name__ == "__main__":
    main()
