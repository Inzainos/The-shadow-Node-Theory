"""
Figuras del README para la release v2.6.0 (reproducibles desde los CSV del repo).

Sustituye a las figuras `figures/snt_fig{1,2,3}_final.png` (rotuladas v2.5.0,
sin script generador y con significancia solo nominal). Cada figura se genera
en versión clara y oscura para el <picture> del README (GitHub elige según el
tema del lector).

Figuras
-------
1. Distribución de b por dominio (color = fricción a priori) y significancia:
   nominal (MCO sin corrección) frente a corregida por autocorrelación donde
   hay insumos (B: cotas AR(1) de la auditoría v32; E3: Newey-West sobre las
   series crudas de OWID).
2. b̄ por dominio con fricción, incluidos los dominios nuevos del pre-registro
   2026-09-27 (rayados) y el resultado de la prueba por dominio.
3. R² medio por dominio, con la advertencia de las dos definiciones mezcladas.
4. Disparadores codificados a ciegas (punto 4): b del caso vs b̄ de controles.
5. Hazard por edad (punto 5): cripto (Binance) y bancos (FDIC, entrada 1970).

Paleta: instancia de referencia validada (categórica slots 1–2 y rampa ordinal
azul, modos claro y oscuro; validador de la guía de visualización: todo PASS).

Salidas: figures/snt_v260_fig*_{light,dark}.png
Log:     reconstruction_real/logs/generate_readme_figures_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/generate_readme_figures.py
"""

import hashlib
import logging
import sys
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "reconstruction_real" / "data"
FIG = ROOT / "figures"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "generate_readme_figures_log.txt"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("FIGURAS-README")

TEMAS = {
    "light": dict(surface="#fcfcfb", text="#0b0b0b", text2="#52514e",
                  grid="#e6e5e0", neutral="#b9b8b1", s1="#2a78d6", s2="#eb6834",
                  friccion={0: "#86b6ef", 1: "#3987e5", 2: "#1c5cab", 3: "#0d366b"}),
    "dark": dict(surface="#1a1a19", text="#ffffff", text2="#c3c2b7",
                 grid="#33332f", neutral="#6b6a64", s1="#3987e5", s2="#d95926",
                 friccion={0: "#184f95", 1: "#3987e5", 2: "#86b6ef", 3: "#cde2fb"}),
}
FRICCION = {"A": 2, "A2": 2, "B": 3, "B-comercio": 3, "C": 3, "D": 1, "D2": 1,
            "E1": 0, "E2": 3, "E3": 0, "E4": 0, "F1": 2, "F2": 2, "F3": 1}
NOMBRE_FRIC = {0: "nula", 1: "baja", 2: "media", 3: "alta"}
NUEVOS = {"A2", "B-comercio", "D2", "E4"}
ETIQ = {"A": "A ciudades", "B": "B pares de países", "C": "C regiones",
        "D": "D digital (distribución)", "E1": "E1 COVID espacial",
        "E2": "E2 depredador-presa", "E3": "E3 COVID por país",
        "F1": "F1 planetario", "F2": "F2 estelar", "F3": "F3 multiplanetario",
        "A2": "A2 ciudades ONU", "B-comercio": "B hub de comercio",
        "D2": "D2 cuotas digitales", "E4": "E4 mpox 2022"}


def estilo(ax, T):
    ax.set_facecolor(T["surface"])
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    for lado in ("left", "bottom"):
        ax.spines[lado].set_color(T["grid"])
    ax.tick_params(colors=T["text2"], labelsize=8.5)
    ax.xaxis.label.set_color(T["text2"])
    ax.yaxis.label.set_color(T["text2"])
    ax.grid(color=T["grid"], linewidth=0.6)
    ax.set_axisbelow(True)


def figura(T, ancho, alto, ncols=1):
    fig, axs = plt.subplots(1, ncols, figsize=(ancho, alto))
    fig.patch.set_facecolor(T["surface"])
    axs = np.atleast_1d(axs)
    for ax in axs:
        estilo(ax, T)
    return fig, axs


def titulos(fig, T, titulo, sub):
    fig.suptitle(titulo, x=0.01, ha="left", y=0.99, fontsize=12.5,
                 fontweight="bold", color=T["text"])
    ancho = int(fig.get_figwidth() * 15)  # ~caracteres por línea a 9 pt
    fig.text(0.01, 0.925, textwrap.fill(sub, ancho), ha="left", va="top",
             fontsize=9, color=T["text2"], linespacing=1.4)


def leyenda(ax, T, handles, **kw):
    lg = ax.legend(handles=handles, frameon=False, fontsize=8, labelcolor=T["text2"],
                   **kw)
    return lg


def guardar(fig, nombre, modo, salidas):
    ruta = FIG / f"snt_v260_{nombre}_{modo}.png"
    fig.savefig(ruta, dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig)
    salidas.append(ruta)


# ------------------------------------------------------------------ datos
def cargar():
    C = pd.read_csv(DATA / "snt_corpus_REAL_v5.csv")
    B = pd.read_csv(DATA / "dominio_B_corregido_ar1_v32.csv")
    E3 = pd.read_csv(DATA / "dominio_E3_series_crudas.csv")
    N = pd.read_csv(DATA / "friccion_dominios_nuevos_casos.csv")
    R = pd.read_csv(DATA / "friccion_dominios_nuevos_resumen.csv")
    D = pd.read_csv(DATA / "disparadores_ciudades_casos.csv")
    H = pd.read_csv(DATA / "aco_hazard_bandas.csv")
    for nombre in ["snt_corpus_REAL_v5.csv", "dominio_B_corregido_ar1_v32.csv",
                   "dominio_E3_series_crudas.csv",
                   "friccion_dominios_nuevos_casos.csv",
                   "friccion_dominios_nuevos_resumen.csv",
                   "disparadores_ciudades_casos.csv", "aco_hazard_bandas.csv"]:
        h = hashlib.sha256((DATA / nombre).read_bytes()).hexdigest()
        log.info("Insumo %-40s SHA-256 %s", nombre, h)
    return C, B, E3, N, R, D, H


# ------------------------------------------------------------------ fig 1
def fig1(C, B, E3, T, modo, salidas):
    orden = C.groupby("dominio").b.median().sort_values().index.tolist()
    fig, (a1, a2) = figura(T, 12, 4.6, 2)
    datos = [C.loc[C.dominio == d, "b"].values for d in orden]
    bp = a1.boxplot(datos, patch_artist=True, widths=0.55, showfliers=True,
                    medianprops=dict(color=T["surface"], linewidth=1.6),
                    whiskerprops=dict(color=T["text2"], linewidth=1),
                    capprops=dict(color=T["text2"], linewidth=1),
                    flierprops=dict(marker="o", markersize=2.5,
                                    markerfacecolor=T["text2"],
                                    markeredgecolor="none", alpha=0.5))
    for caja, d in zip(bp["boxes"], orden):
        caja.set_facecolor(T["friccion"][FRICCION[d]])
        caja.set_edgecolor(T["surface"])
    rng = np.random.default_rng(20260927)
    for i, (d, v) in enumerate(zip(orden, datos), start=1):
        chico = len(v) < 5
        a1.scatter(i + rng.uniform(-0.12, 0.12, len(v)), v,
                   s=26 if chico else 4, color=T["friccion"][FRICCION[d]],
                   edgecolor=T["text2"] if chico else "none",
                   linewidth=0.8, alpha=1 if chico else 0.35, zorder=3)
    a1.set_xticks(range(1, len(orden) + 1), orden)
    a1.axhline(0, color=T["text2"], linewidth=1, linestyle="--")
    a1.axhline(1, color=T["text2"], linewidth=0.8, linestyle=":")
    a1.set_ylabel("exponente b")
    a1.set_title("Exponente b por dominio (721 casos; color = fricción a priori)",
                 fontsize=10, color=T["text"], loc="left")
    leyenda(a1, T, [Patch(color=T["friccion"][k], label=f"fricción {v}")
                    for k, v in NOMBRE_FRIC.items()], loc="upper left", ncol=2)

    orden2 = C.groupby("dominio").size().index.tolist()
    nominal = C.groupby("dominio").significativo.mean() * 100
    y = np.arange(len(orden2))
    a2.barh(y, [nominal[d] for d in orden2], height=0.6, color=T["neutral"],
            edgecolor=T["surface"], linewidth=1)
    iB, iE = orden2.index("B"), orden2.index("E3")
    lo = 100 * B.sig_ar1.sum() / len(B)
    hi = 100 * B.sig_ar1_solo_gl.sum() / len(B)
    nw = 100 * (E3.p_newey_west < 0.05).mean()
    extra = {"B": f"  → corregido {lo:.0f}–{hi:.0f}%",
             "E3": f"  → Newey-West {nw:.1f}%"}
    for yi, d in zip(y, orden2):
        n = int((C.dominio == d).sum())
        a2.text(nominal[d] + 1.5, yi, f"{nominal[d]:.0f}%  (n={n}){extra.get(d, '')}",
                va="center", fontsize=8, color=T["text2"])
    a2.plot([lo, hi], [iB, iB], color=T["s2"], linewidth=4, solid_capstyle="butt",
            zorder=3)
    a2.plot([nw], [iE], marker="D", markersize=6, color=T["s2"],
            markeredgecolor=T["surface"], zorder=3)
    a2.set_yticks(y, orden2)
    a2.set_xlim(0, 185)
    a2.set_xticks([0, 25, 50, 75, 100])
    a2.set_xlabel("% de casos con p < 0.05")
    a2.set_title("Significancia: nominal vs corregida por autocorrelación",
                 fontsize=10, color=T["text"], loc="left")
    leyenda(a2, T, [Patch(color=T["neutral"], label="nominal (MCO sin corrección)"),
                    Line2D([], [], color=T["s2"], linewidth=4,
                           label="corregida (B: cotas AR(1) v32; E3: Newey-West)")],
            loc="lower right")
    titulos(fig, T, "Shadow Node Theory v2.6.0 — corpus de 721 casos reales",
            "Solo B y E3 tienen insumos para corregir la autocorrelación; en el "
            "resto la significancia sigue siendo nominal.")
    fig.subplots_adjust(left=0.05, right=0.99, top=0.8, bottom=0.12, wspace=0.18)
    guardar(fig, "fig1_distribucion", modo, salidas)


# ------------------------------------------------------------------ fig 2
def fig2(C, N, R, T, modo, salidas):
    base = C[["dominio", "b"]]
    nuevos = N[N.dominio.isin(NUEVOS)][["dominio", "b"]]
    todo = pd.concat([base, nuevos])
    med = todo.groupby("dominio").b.agg(["mean", "size"]).sort_values("mean")
    fig, (ax,) = figura(T, 10, 6.2)
    y = np.arange(len(med))
    for yi, (d, r) in zip(y, med.iterrows()):
        ax.barh(yi, r["mean"], height=0.62, color=T["friccion"][FRICCION[d]],
                edgecolor=T["surface"], linewidth=1,
                hatch="////" if d in NUEVOS else None)
        x = r["mean"]
        ax.text(x + (0.05 if x >= 0 else -0.05), yi, f"{x:+.2f}  (n={int(r['size'])})",
                va="center", ha="left" if x >= 0 else "right", fontsize=8,
                color=T["text2"])
    ax.set_yticks(y, [ETIQ[d] + (" · nuevo" if d in NUEVOS else "")
                      for d in med.index])
    ax.axvline(0, color=T["text2"], linewidth=1, linestyle="--")
    ax.axvline(1, color=T["text2"], linewidth=0.8, linestyle=":")
    ax.set_xlabel("b medio del dominio")
    ax.set_xlim(med["mean"].min() - 0.8, med["mean"].max() + 0.9)
    principal = R[R.prueba.str.startswith("PRINCIPAL")].iloc[0]
    hand = [Patch(color=T["friccion"][k], label=f"fricción {v}")
            for k, v in NOMBRE_FRIC.items()]
    hand.append(Patch(facecolor=T["surface"], edgecolor=T["text2"], hatch="////",
                      label="dominio nuevo (pre-registro 2026-09-27)"))
    leyenda(ax, T, hand, loc="lower right")
    titulos(fig, T, "b medio por dominio y fricción a priori",
            "Prueba pre-registrada sin COVID (7 dominios): ρ(fricción, b̄) = "
            f"{principal.rho:+.3f}, permutación exacta p = {principal.p_una_cola:.2f} "
            "— no respaldada. Solo las epidemias (fricción nula) se separan.")
    fig.subplots_adjust(left=0.24, right=0.98, top=0.84, bottom=0.09)
    guardar(fig, "fig2_friccion", modo, salidas)


# ------------------------------------------------------------------ fig 3
def fig3(C, T, modo, salidas):
    r2 = C.groupby("dominio").r2.mean().sort_values(ascending=False)
    fig, (ax,) = figura(T, 10, 4.2)
    x = np.arange(len(r2))
    ax.bar(x, r2.values, width=0.6, color=T["s1"], edgecolor=T["surface"],
           linewidth=1)
    for xi, v in zip(x, r2.values):
        ax.text(xi, v + 0.02, f"{v:.2f}", ha="center", fontsize=8, color=T["text2"])
    ax.set_xticks(x, r2.index)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("R² medio")
    titulos(fig, T, "Bondad de ajuste por dominio (721 casos; R² ∈ [0, 1] en todos)",
            "Definiciones mezcladas (auditoría v32): B usa r² de Pearson en escala "
            "log; el resto, 1 − SSres/SStot en escala original.")
    fig.subplots_adjust(left=0.07, right=0.99, top=0.8, bottom=0.1)
    guardar(fig, "fig3_r2", modo, salidas)


# ------------------------------------------------------------------ fig 4
def fig4(D, T, modo, salidas):
    x = D[(D.base_anio == "efectivo") & D.d.notna()].sort_values("d")
    fig, (ax,) = figura(T, 10, 4.6)
    y = np.arange(len(x))
    for yi, (_, r) in zip(y, x.iterrows()):
        ax.plot([r.b_controles, r.b], [yi, yi], color=T["neutral"], linewidth=1.5)
    ax.scatter(x.b_controles, y, s=42, color=T["s1"], edgecolor=T["surface"],
               linewidth=1, zorder=3)
    ax.scatter(x.b, y, s=42, color=T["s2"], edgecolor=T["surface"], linewidth=1,
               zorder=3)
    etiquetas = [f"{r.retador} / {r.incumbente.split(',')[0]} ({int(r.anio)})"
                 for _, r in x.iterrows()]
    ax.set_yticks(y, etiquetas)
    ax.axvline(0, color=T["text2"], linewidth=1, linestyle="--")
    ax.set_xlabel("exponente b (retador / incumbente desde el año del disparador)")
    leyenda(ax, T, [Line2D([], [], marker="o", linestyle="", color=T["s2"],
                           markersize=7, label="ciudad del decreto"),
                    Line2D([], [], marker="o", linestyle="", color=T["s1"],
                           markersize=7,
                           label="media de 5 ciudades con la misma razón inicial")],
            loc="lower right")
    titulos(fig, T, "Disparadores abruptos codificados a ciegas (pre-registro)",
            "Traslados de capital y Zonas Económicas Especiales de 1980: el retador "
            "supera a sus controles en 8/8 casos (Wilcoxon 1 cola p = 0.004). "
            "ONU WUP 2018, ciudades ≥ 300 mil en 2018.")
    fig.subplots_adjust(left=0.26, right=0.98, top=0.8, bottom=0.12)
    guardar(fig, "fig4_disparadores", modo, salidas)


# ------------------------------------------------------------------ fig 5
def fig5(H, T, modo, salidas):
    fig, (a1, a2) = figura(T, 12, 4.4, 2)
    paneles = [
        (a1, [("cripto ACO", "extinción funcional ACO", T["s1"]),
              ("cripto ACO+retiro", "extinción ACO o retiro del par", T["s2"])],
         "Cripto (Binance, 663 pares; bandas de 1 año)"),
        (a2, [("bancos cualquier fin, entrada corregida 1970",
               "cualquier fin (fusión, quiebra…)", T["s1"]),
              ("bancos solo quiebras, entrada corregida 1970", "solo quiebras",
               T["s2"])],
         "Bancos (FDIC, 27,771; bandas de 5 años; entrada 1970)"),
    ]
    for ax, series, titulo in paneles:
        for coh, etiqueta, color in series:
            h = H[(H.cohorte == coh) & (H.en_riesgo >= 30)]
            xm = (h.banda_ini + h.banda_fin) / 2
            ax.plot(xm, h.hazard, color=color, linewidth=1.8, marker="o",
                    markersize=4.5, markeredgecolor=T["surface"], label=etiqueta)
        ax.set_xlabel("edad (años)")
        ax.set_ylabel("hazard h (fines por año)")
        ax.set_ylim(0, ax.get_ylim()[1] * 1.28)
        ax.set_title(titulo, fontsize=10, color=T["text"], loc="left")
        leyenda(ax, T, ax.get_legend_handles_labels()[0], loc="upper left",
                ncol=2)
    titulos(fig, T, "Ningún sistema es eterno: h(τ) > 0 en dos cohortes grandes",
            "Hay fines en todas las bandas con ≥ 30 en riesgo. El hazard crece con la "
            "edad solo en cripto (confundido con el ciclo 2022–2025); en bancos tiene "
            "forma de bañera.")
    fig.subplots_adjust(left=0.06, right=0.99, top=0.8, bottom=0.13, wspace=0.16)
    guardar(fig, "fig5_hazard", modo, salidas)


def main():
    log.info("=" * 78)
    log.info("FIGURAS DEL README — release v2.6.0")
    log.info("=" * 78)
    plt.rcParams["font.family"] = "DejaVu Sans"
    C, B, E3, N, R, D, H = cargar()
    salidas = []
    for modo, T in TEMAS.items():
        fig1(C, B, E3, T, modo, salidas)
        fig2(C, N, R, T, modo, salidas)
        fig3(C, T, modo, salidas)
        fig4(D, T, modo, salidas)
        fig5(H, T, modo, salidas)
    for ruta in salidas:
        log.info("PNG -> %s", ruta.relative_to(ROOT))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
