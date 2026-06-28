"""
Stability-landscape ("gráficas de valles") figures for the SNT collapse theory.
Fig 1: the collapse-mode taxonomy as potential landscapes (6 panels).
Fig 2: the cusp/fold catastrophe — friction as control parameter.
Okabe-Ito palette, SVG + PNG 300dpi.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

FIG = Path("/home/user/The-shadow-Node-Theory/figures")
FIG.mkdir(parents=True, exist_ok=True)

OK = {"orange": "#E69F00", "sky": "#56B4E9", "green": "#009E73",
      "yellow": "#F0E442", "blue": "#0072B2", "verm": "#D55E00",
      "purple": "#CC79A7", "gray": "#999999"}
BALL = "#D55E00"


def ball(ax, x, y, c=BALL):
    ax.plot(x, y, "o", ms=15, color=c, mec="black", mew=1.2, zorder=10)


# ============================ FIG 1: 6 landscapes ============================
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
x = np.linspace(-3, 3, 600)

# 1. Decaimiento Orbital Regulado: single well, gently tilted -> smooth roll
ax = axes[0, 0]
V = 0.5*x**2 + 0.9*x          # tilted parabola
ax.plot(x, V, color=OK["blue"], lw=2.5)
ball(ax, -0.9, 0.5*0.81 - 0.9*0.9)
ax.annotate("", xy=(-1.6, 0.5*1.6**2-0.9*1.6), xytext=(-0.9, 0.5*0.81-0.81),
            arrowprops=dict(arrowstyle="->", color=BALL, lw=2))
ax.set_title("Decaimiento Orbital Regulado\n(fricción alta → pendiente suave, ley de potencia)",
             fontsize=10, fontweight="bold", color=OK["blue"])

# 2. Acantilado Catastrófico: fold — wall vanishes, plunge to deep basin (zero)
ax = axes[0, 1]
V = np.where(x < 0.5, 0.6*(x+1.2)**2 - 0.4, -3.5 - 0.8*(x-0.5))
V = np.clip(V, -5, 5)
ax.plot(x, V, color=OK["verm"], lw=2.5)
ball(ax, 0.45, 0.6*(0.45+1.2)**2 - 0.4)
ax.annotate("", xy=(2.4, -5.0), xytext=(0.55, -0.3),
            arrowprops=dict(arrowstyle="->", color=BALL, lw=2.5,
                            connectionstyle="arc3,rad=-0.3"))
ax.text(1.4, -2.0, "sin piso → 0", fontsize=8, color=OK["verm"], style="italic")
ax.set_title("Acantilado Catastrófico\n(fricción≈0 + abrupto + sin piso) — LUNA",
             fontsize=10, fontweight="bold", color=OK["verm"])

# 3. Caída-a-piso: like cliff but a secondary well (floor) catches the ball
ax = axes[0, 2]
V = 0.6*(x+1.2)**2 - 0.4
V2 = 1.2*(x-1.6)**2 - 2.3      # secondary (floor) well
V = np.minimum(V, V2)
ax.plot(x, V, color=OK["orange"], lw=2.5)
ball(ax, -1.2, -0.4)
ax.annotate("", xy=(1.6, -2.3), xytext=(-0.2, -0.2),
            arrowprops=dict(arrowstyle="->", color=BALL, lw=2.2,
                            connectionstyle="arc3,rad=-0.25"))
ax.axhline(-2.3, ls=":", color=OK["gray"], lw=1)
ax.text(0.9, -1.6, "piso residual", fontsize=8, color=OK["orange"], style="italic")
ax.set_title("Caída-a-piso\n(fricción≈0 + abrupto + con piso) — FTX",
             fontsize=10, fontweight="bold", color=OK["orange"])

# 4. Craquelado: rugged/fractal landscape, many shallow channels
ax = axes[1, 0]
rng = np.random.default_rng(7)
V = 0.4*x**2 + 0.55*x + 0.45*np.sin(6*x) + 0.25*np.sin(13*x+1) + 0.12*np.sin(23*x)
ax.plot(x, V, color=OK["green"], lw=2.2)
for xb in (-1.4, -0.6, 0.2):
    ax.plot(xb, 0.4*xb**2+0.55*xb+0.45*np.sin(6*xb)+0.25*np.sin(13*xb+1)+0.12*np.sin(23*xb),
            "o", ms=8, color=BALL, mec="black", mew=0.8, alpha=0.8, zorder=10)
ax.set_title("Decaimiento Craquelado\n(fricción≈0 + gradual) — fragmentación errática (EOS)",
             fontsize=10, fontweight="bold", color=OK["green"])

# 5. Doble pozo (barrido logístico): Delta well -> deeper Omicron well
ax = axes[1, 1]
V = 0.7*(x**2-1.6)**2 + 0.8*x        # double well, right (Omicron) deeper
ax.plot(x, V, color=OK["purple"], lw=2.5)
ball(ax, -1.27, 0.7*((-1.27)**2-1.6)**2 + 0.8*(-1.27))
ax.annotate("", xy=(1.27, 0.7*(1.27**2-1.6)**2+0.8*1.27),
            xytext=(-1.0, 0.7*(1.0-1.6)**2-0.8),
            arrowprops=dict(arrowstyle="->", color=BALL, lw=2,
                            connectionstyle="arc3,rad=0.3"))
ax.text(-1.9, 1.2, "Delta", fontsize=8, color=OK["purple"])
ax.text(1.0, 0.2, "Ómicron", fontsize=8, color=OK["purple"], fontweight="bold")
ax.set_title("Barrido logístico (doble pozo)\n(magnitud acotada) — Delta→Ómicron",
             fontsize=10, fontweight="bold", color=OK["purple"])

# 6. Leapfrog: escape UPWARD to a better (higher-but-renewing) basin
ax = axes[1, 2]
V = 0.6*x**2 - 0.0*x
ax.plot(x, V, color=OK["sky"], lw=2.5)
# a higher new basin to the right (renewal)
xn = np.linspace(1.8, 3, 100)
ax.plot(xn, 0.6*1.8**2 + 0.8 - 1.0*(xn-1.8) + 0.8*(xn-2.4)**2, color=OK["sky"], lw=2.5)
ball(ax, -0.0, 0.0)
ax.annotate("", xy=(2.4, 0.6*1.8**2+0.8-1.0*0.6), xytext=(0.0, 0.05),
            arrowprops=dict(arrowstyle="->", color=BALL, lw=2.2,
                            connectionstyle="arc3,rad=-0.45"))
ax.text(1.4, 2.4, "salto ↑\n(renovación)", fontsize=8, color=OK["sky"],
        fontweight="bold", ha="center")
ax.set_title("Leapfrog (bifurcación: brincar)\nescape a un valle mejor — Querétaro, N.León",
             fontsize=10, fontweight="bold", color=OK["sky"])

for ax in axes.flat:
    ax.set_xlabel("estado del sistema", fontsize=8)
    ax.set_ylabel("potencial (− estabilidad)", fontsize=8)
    ax.set_xticks([]); ax.set_yticks([])
    ax.grid(alpha=0.15)

fig.suptitle("Shadow Node Theory — Paisajes de Estabilidad del Colapso\n"
             "Un mismo principio (mínima fricción = flujo gradiente), "
             "distintas geometrías del paisaje",
             fontsize=13, fontweight="bold", y=1.00)
fig.tight_layout(rect=[0, 0, 1, 0.96])
fig.savefig(FIG/"fig_paisajes_colapso.svg", bbox_inches="tight", facecolor="white")
fig.savefig(FIG/"fig_paisajes_colapso.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.close(fig)
print("fig_paisajes_colapso written")

# ====== FIG 2: fold catastrophe — friction as control parameter ======
# V(x) = (1/3)x^3 - c·x : local min at +sqrt(c) (stable valley), barrier (max)
# at -sqrt(c). As c -> 0 the valley and barrier annihilate (fold/saddle-node)
# and the system slides off the cliff. c is set by friction.
fig, axes = plt.subplots(1, 3, figsize=(15, 4.6), sharey=True)
x = np.linspace(-3, 3, 600)
configs = [
    ("Fricción ALTA", 1.6, OK["blue"], "valle profundo + barrera alta (estable)"),
    ("Fricción MEDIA", 0.5, OK["orange"], "valle somero, barrera baja"),
    ("Fricción ≈ 0", -0.15, OK["verm"], "valle y barrera se aniquilan → cae"),
]
for ax, (lab, c, col, sub) in zip(axes, configs):
    V = (1/3)*x**3 - c*x
    ax.plot(x, V, color=col, lw=2.6)
    if c > 0:
        xm = np.sqrt(c)
        ax.plot(xm, (1/3)*xm**3 - c*xm, "o", ms=15, color=BALL,
                mec="black", mew=1.2, zorder=10)
        xb = -np.sqrt(c)
        ax.annotate("barrera", xy=(xb, (1/3)*xb**3 - c*xb),
                    xytext=(xb-0.2, (1/3)*xb**3 - c*xb + 1.2),
                    fontsize=8, color=OK["gray"], ha="center")
    else:
        ax.plot(0.05, (1/3)*0.05**3, "o", ms=15, color=BALL,
                mec="black", mew=1.2, zorder=10)
        ax.annotate("", xy=(-2.6, (1/3)*(-2.6)**3 + 0.15*2.6), xytext=(0.0, 0),
                    arrowprops=dict(arrowstyle="->", color=BALL, lw=2.5,
                                    connectionstyle="arc3,rad=0.25"))
        ax.text(-1.8, -3.5, "acantilado", fontsize=9, color=OK["verm"],
                style="italic", fontweight="bold")
    ax.set_title(f"{lab}\n{sub}", fontsize=10, fontweight="bold", color=col)
    ax.set_xlabel("estado", fontsize=9)
    ax.set_xticks([]); ax.set_yticks([]); ax.grid(alpha=0.15)
    ax.set_ylim(-6, 6)
axes[0].set_ylabel("potencial", fontsize=9)
fig.suptitle("Catástrofe de pliegue: la fricción es el parámetro de control\n"
             "Al perder fricción, el valle estable y su barrera se aniquilan "
             "y el sistema cae (acantilado)",
             fontsize=12, fontweight="bold", y=1.02)
fig.tight_layout(rect=[0, 0, 1, 0.9])
fig.savefig(FIG/"fig_catastrofe_cuspide.svg", bbox_inches="tight", facecolor="white")
fig.savefig(FIG/"fig_catastrofe_cuspide.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.close(fig)
print("fig_catastrofe_cuspide written")
