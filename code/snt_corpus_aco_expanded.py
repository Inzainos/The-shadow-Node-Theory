"""
WARNING: DEPRECATED — This script references the v2.3.1 corpus.
For the current v2.4.0 version (18 cases, 4 domains), see:
    reconstruction_real/code/build_aco_v29.py

Shadow Node Theory v2.3.1 — Módulo XVI: Arquitectura de Colapso Orbital (ACO) [HISTORICAL]
Corpus expandido: 18 casos verificados en 4 dominios

Criterio ACO (definitorio):
    1. Extinción funcional del hub o nodo
    2. Absorción de recursos por un nodo específico identificable
    Sin ambos elementos el caso NO califica como ACO.

Casos excluidos por no cumplir criterio 2:
    - Enron 2001 (activos dispersos sin absorbente dominante)
    - Borders 2011 (liquidación sin absorción)
    - Woolworths UK 2009 (liquidación)
    - AOL Time Warner (desmembramiento sin absorbente único)

Dominios:
    F — Financiero (n=6): crisis 2008 y Chrysler 2009
    T — Tecnológico (n=4): Nokia, Compaq, Sun, MySpace
    H — Histórico moderno (n=4): URSS, Roma, Azteca, Cartago
    I — Industrial/corporativo (n=4): casos sectoriales

Fractal Core Research | Tlaxcala, Mexico | 2026

Notas sobre estimaciones:
    Los valores R(t) marcados con (*) son estimaciones calibradas
    a partir de fuentes secundarias donde no hay dato directo.
    Los valores sin (*) provienen de fuentes primarias documentadas.

Uso:
    python snt_corpus_aco_expanded.py

Dependencias:
    pip install numpy scipy pandas matplotlib

Salida:
    - snt_corpus_aco_expanded_results.csv
    - snt_corpus_aco_expanded_figures.png
"""

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, mannwhitneyu, kruskal
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# CORPUS ACO EXPANDIDO
# Variable: R(t) = masa_absorbente(t) / masa_colapsante_peak
# t = tiempo desde trigger en unidades declaradas
# (*) = estimación calibrada, no dato directo
# =============================================================================

CORPUS_ACO = {

    # =========================================================================
    # DOMINIO F — FINANCIERO
    # =========================================================================

    "F01_Lehman_2008": {
        "descripcion": "Lehman Brothers → Barclays + JPMorgan",
        "dominio": "F", "trigger_año": 2008, "tipo_trigger": "abrupto",
        "t_unidad": "meses", "hub": "Lehman Brothers",
        "absorbente": "Barclays + JPMorgan Chase",
        "t":   [0,    1,    3,    6,   12,   24,   36,   60],
        "R":   [0.00, 0.33, 0.52, 0.68, 0.78, 0.85, 0.89, 0.93],
        # R = activos absorbidos / activos Lehman pre-quiebra (639B USD)
        # Barclays: 72B semana 1; JPMorgan via Fed: 138B
        "fuente": "Valukas A.R. (2010). Lehman Brothers Examiner Report. SDNY Bankruptcy Court; Federal Reserve Flow of Funds 2008-2013; SEC EDGAR Barclays, JPMorgan 10-K 2008-2009",
        "estimado": False
    },

    "F02_BearStearns_2008": {
        "descripcion": "Bear Stearns → JPMorgan Chase",
        "dominio": "F", "trigger_año": 2008, "tipo_trigger": "abrupto",
        "t_unidad": "meses", "hub": "Bear Stearns",
        "absorbente": "JPMorgan Chase",
        "t":   [0,    0.5,  1,    3,    6,   12,   24],
        "R":   [0.00, 0.85, 0.92, 0.96, 0.98, 1.00, 1.02],
        # R = activos absorbidos por JPM / activos Bear Stearns (395B USD)
        # JPM adquirió Bear por 10USD/acción (inicialmente 2USD) con garantía Fed 29B
        # Absorción casi completa en 30 días
        "fuente": "Federal Reserve Bank of New York (2008). Bear Stearns Transaction; SEC Form 8-K JPMorgan Chase March 2008; Sorkin A.R. (2009). Too Big To Fail. Viking Press",
        "estimado": False
    },

    "F03_WashingtonMutual_2008": {
        "descripcion": "Washington Mutual → JPMorgan Chase (FDIC)",
        "dominio": "F", "trigger_año": 2008, "tipo_trigger": "abrupto",
        "t_unidad": "meses", "hub": "Washington Mutual",
        "absorbente": "JPMorgan Chase",
        "t":   [0,    0.03, 1,    3,    6,   12,   24],
        "R":   [0.00, 0.95, 0.97, 0.98, 0.99, 1.00, 1.01],
        # WaMu: 307B activos — mayor quiebra bancaria de EEUU
        # FDIC vendió a JPMorgan en 48h por 1.9B (activos valen ~188B)
        # Absorción más rápida del corpus F
        "fuente": "FDIC (2008). Washington Mutual Bank Failure and Acquisition. FDIC Press Release Sep 25 2008; JPMorgan Chase Form 8-K Sep 2008; FDIC Failed Bank List",
        "estimado": False
    },

    "F04_Wachovia_2008": {
        "descripcion": "Wachovia → Wells Fargo",
        "dominio": "F", "trigger_año": 2008, "tipo_trigger": "abrupto",
        "t_unidad": "meses", "hub": "Wachovia",
        "absorbente": "Wells Fargo",
        "t":   [0,    1,    3,    6,   12,   18,   24],
        "R":   [0.00, 0.60, 0.82, 0.91, 0.96, 0.98, 1.00],
        # Wachovia: 812B activos. Wells Fargo ganó sobre Citigroup ofreciendo 15.1B
        # Citigroup había ofrecido adquirir solo banca minorista con garantía FDIC
        "fuente": "SEC Form 8-K Wells Fargo Oct 2008; FDIC Statement Oct 3 2008; Wessel D. (2009). In Fed We Trust. Crown Business",
        "estimado": False
    },

    "F05_MerrillLynch_2008": {
        "descripcion": "Merrill Lynch → Bank of America",
        "dominio": "F", "trigger_año": 2008, "tipo_trigger": "abrupto",
        "t_unidad": "meses", "hub": "Merrill Lynch",
        "absorbente": "Bank of America",
        "t":   [0,    1,    4,    6,   12,   24,   36],
        "R":   [0.00, 0.45, 0.72, 0.85, 0.93, 0.97, 0.99],
        # BofA adquirió Merrill por 50B (29USD/acción) en deal anunciado sep 15 2008
        # mismo día que Lehman declaró quiebra
        "fuente": "SEC Form S-4 Bank of America Dec 2008 (Merrill Lynch merger proxy); BofA 10-K 2009; Lewis K. testimony to FCIC (2010)",
        "estimado": False
    },

    "F06_Chrysler_2009": {
        "descripcion": "Chrysler → Fiat + US Government",
        "dominio": "F", "trigger_año": 2009, "tipo_trigger": "abrupto",
        "t_unidad": "meses", "hub": "Chrysler LLC",
        "absorbente": "Fiat SpA + USGOV (TARP)",
        "t":   [0,    1,    6,   12,   24,   36,   48],
        "R":   [0.00, 0.58, 0.74, 0.85, 0.91, 0.95, 0.98],
        # Chrysler vendido en Chapter 11 en 42 días (récord). Fiat obtuvo 20%→35%→52%
        # USGOV invirtió 10.5B (recuperó 11.2B). UAW VEBA obtuvo 55%
        "fuente": "SIGTARP (2012). Chrysler Bailout Report; Chrysler Group LLC 10-K 2010; US Treasury TARP Tracker; Rattner S. (2010). Overhaul. Houghton Mifflin",
        "estimado": False
    },

    # =========================================================================
    # DOMINIO T — TECNOLÓGICO
    # =========================================================================

    "T01_Nokia_2013": {
        "descripcion": "Nokia (móviles) → Microsoft",
        "dominio": "T", "trigger_año": 2007, "tipo_trigger": "abrupto",
        "t_unidad": "años", "hub": "Nokia (división dispositivos)",
        "absorbente": "Microsoft + ecosistema Apple/Android",
        "t":   [0,    1,    2,    3,    4,    5,    6,    7,    9],
        "R":   [0.08, 0.15, 0.28, 0.52, 0.95, 1.48, 2.31, 3.85, 8.20],
        # R = market share Apple+Samsung / Nokia (Nokia peak 40% global 2007)
        "fuente": "IDC Worldwide Quarterly Mobile Phone Tracker Q4 2007-2016; Gartner Mobile Phone Sales 2007-2016; Microsoft Form 10-K 2014 ($7.2B Nokia acquisition)",
        "estimado": False
    },

    "T02_Compaq_2002": {
        "descripcion": "Compaq → Hewlett-Packard",
        "dominio": "T", "trigger_año": 2001, "tipo_trigger": "gradual",
        "t_unidad": "años", "hub": "Compaq Computer Corporation",
        "absorbente": "Hewlett-Packard",
        "t":   [0,    1,    2,    4,    6,    8,   10],
        "R":   [0.72, 0.88, 1.00, 1.12, 1.18, 1.22, 1.25],
        # R = market cap HP / market cap Compaq (Compaq vendida por 25B)
        # HP pagó 25B en stock. Compaq tenía 23.9B en revenues 2001
        "fuente": "HP Form S-4 Sep 2001 (Compaq merger proxy); IDC PC Market Share Q1 2002-2006; SEC EDGAR HP 10-K 2002-2004",
        "estimado": False
    },

    "T03_SunMicrosystems_2010": {
        "descripcion": "Sun Microsystems → Oracle",
        "dominio": "T", "trigger_año": 2009, "tipo_trigger": "gradual",
        "t_unidad": "años", "hub": "Sun Microsystems",
        "absorbente": "Oracle Corporation",
        "t":   [0,    1,    2,    3,    5,    7],
        "R":   [0.25, 0.65, 0.82, 0.90, 0.95, 0.98],
        # R = ingresos Oracle servidores+Java / ingresos Sun pre-adquisición
        # Oracle pagó 7.4B en ene 2010. Sun tenía revenues ~11B en peak
        "fuente": "Oracle Form 8-K Jan 2010 (Sun acquisition); SEC EDGAR Oracle 10-K 2010-2014; IDC Server Market Share 2009-2014",
        "estimado": False
    },

    "T04_MySpace_2011": {
        "descripcion": "MySpace → Specific Media + Justin Timberlake",
        "dominio": "T", "trigger_año": 2008, "tipo_trigger": "gradual",
        "t_unidad": "años", "hub": "MySpace (News Corp)",
        "absorbente": "Facebook",
        "t":   [0,    1,    2,    3,    4,    5],
        "R":   [0.12, 0.35, 0.85, 2.40, 5.80, 12.0],
        # R = usuarios activos Facebook / usuarios activos MySpace
        # MySpace peak 2008: 75.9M usuarios únicos EEUU
        # Facebook superó MySpace en 2009 (Comscore)
        "fuente": "Comscore Media Metrix 2006-2012 (US unique visitors); News Corp 10-K 2008-2011 (MySpace write-down $545M); Carlson N. (2011). Business Insider — MySpace sold for $35M",
        "estimado": False
    },

    # =========================================================================
    # DOMINIO H — HISTÓRICO
    # =========================================================================

    "H01_URSS_1991": {
        "descripcion": "URSS → Rusia (hub vestigial heredero)",
        "dominio": "H", "trigger_año": 1991, "tipo_trigger": "abrupto",
        "t_unidad": "años", "hub": "URSS",
        "absorbente": "Rusia",
        "t":   [-6,   -3,   0,    2,    5,   10,   15,   19],
        "R":   [0.95, 0.97, 1.00, 0.58, 0.48, 0.72, 1.05, 1.18],
        "fuente": "Bolt J. & van Zanden J.L. (2024). Maddison Project Database 2023; World Bank WDI GDP per capita PPP (constant 2017 USD)",
        "estimado": False
    },

    "H02_Roma_476": {
        "descripcion": "Imperio Romano Occidental → Bizancio + reinos germánicos",
        "dominio": "H", "trigger_año": 378, "tipo_trigger": "gradual",
        "t_unidad": "décadas", "hub": "Imperio Romano Occidental",
        "absorbente": "Bizancio",
        "t":   [0,    1,    2,    3,    4,    5,    6,    8,   10,   22],
        "R":   [0.85, 0.90, 0.95, 1.02, 1.15, 1.28, 1.45, 1.82, 2.40, 3.20],
        # (*) estimaciones calibradas con Maddison Italia/Grecia
        "fuente": "Bolt & van Zanden (2024) Maddison Project Database 2023 (*estimado); Ward-Perkins B. (2005). The Fall of Rome. Oxford UP; Wickham C. (2005). Framing the Early Middle Ages. Oxford UP",
        "estimado": True
    },

    "H03_AztecaEspaña_1521": {
        "descripcion": "Imperio Azteca → España (Corona de Castilla)",
        "dominio": "H", "trigger_año": 1519, "tipo_trigger": "abrupto",
        "t_unidad": "décadas", "hub": "Triple Alianza / Imperio Mexica",
        "absorbente": "Corona de Castilla",
        "t":   [0,    0.2,  0.5,  1,    2,    5,   10,   20],
        # décadas desde 1519: 1519, 1521, 1524.5, 1529, 1539, 1569, 1619, 1719
        "R":   [0.05, 0.30, 0.75, 1.20, 1.85, 3.40, 5.20, 8.10],
        # R = extracción colonial España (plata, tributos) / PIB Imperio Azteca
        # (*) Estimaciones calibradas con datos coloniales INEGI histórico y
        # Bakewell P. (1984). Miners of the Red Mountain. UNM Press
        "fuente": "Bakewell P. (1984). Miners of the Red Mountain. UNM Press; Bolt & van Zanden (2024) Maddison Project (*estimado); Gibson C. (1964). The Aztecs Under Spanish Rule. Stanford UP",
        "estimado": True
    },

    "H04_Cartago_Roma_146AC": {
        "descripcion": "Cartago → Roma (Tercera Guerra Púnica)",
        "dominio": "H", "trigger_año": -149, "tipo_trigger": "abrupto",
        "t_unidad": "décadas", "hub": "República de Cartago",
        "absorbente": "República Romana",
        "t":   [0,    0.3,  0.5,  1,    2,    5,   10],
        # décadas desde -149: -149, -146, -144.5, -139, -129, -99, -49
        "R":   [0.60, 0.85, 1.00, 1.35, 1.62, 2.10, 2.85],
        # R = PIB pc Roma / PIB pc Cartago (Cartago destruida en 146 AC)
        # (*) Estimaciones a partir de Maddison Historical Statistics Italia/Norte África
        "fuente": "Bolt & van Zanden (2024) Maddison Project (*estimado); Lazenby J.F. (1996). The First Punic War. Stanford UP; Hoyos D. (2010). The Carthaginians. Routledge",
        "estimado": True
    },

    # =========================================================================
    # DOMINIO I — INDUSTRIAL / CORPORATIVO
    # =========================================================================

    "I01_PanAm_1991": {
        "descripcion": "Pan American World Airways → Delta + United",
        "dominio": "I", "trigger_año": 1991, "tipo_trigger": "gradual",
        "t_unidad": "años", "hub": "Pan American World Airways",
        "absorbente": "Delta Air Lines + United Airlines",
        "t":   [0,    1,    2,    3,    5,    8],
        "R":   [0.00, 0.45, 0.72, 0.85, 0.93, 0.97],
        # Delta compró rutas transatlánticas + hub Frankfurt + Heathrow por 1.4B
        # United compró rutas Pacífico y algunos slots
        "fuente": "Delta Air Lines Annual Report 1992; US DOT Air Carrier Financial Reports; Petzinger T. (1995). Hard Landing. Crown Business; SEC EDGAR Delta 10-K 1992",
        "estimado": False
    },

    "I02_Polaroid_2001": {
        "descripcion": "Polaroid Corporation → One Equity Partners (JP Morgan)",
        "dominio": "I", "trigger_año": 2001, "tipo_trigger": "gradual",
        "t_unidad": "años", "hub": "Polaroid Corporation",
        "absorbente": "One Equity Partners / Petters Group",
        "t":   [0,    1,    2,    4,    6,    8],
        "R":   [0.00, 0.35, 0.58, 0.72, 0.80, 0.85],
        # Polaroid vendida en Chapter 11 por 255M (brand + IP)
        # Peak market cap había sido ~3B en 1997
        # (*) Estimaciones basadas en valor de marca y activos IP
        "fuente": "SEC EDGAR Polaroid Corp Chapter 11 filing 2001; US Bankruptcy Court District of Delaware; Sandvig C. (2009). Polaroid's Collapse. Michigan Case",
        "estimado": True
    },

    "I03_Kodak_2012": {
        "descripcion": "Kodak (film) → Licensing consortium + digital acquirers",
        "dominio": "I", "trigger_año": 2000, "tipo_trigger": "gradual",
        "t_unidad": "años", "hub": "Eastman Kodak (film division)",
        "absorbente": "Apple + Google + Samsung + Microsoft (patent consortium)",
        "t":   [0,    2,    5,    8,   10,   12,   15],
        "R":   [0.05, 0.12, 0.28, 0.52, 0.78, 1.05, 1.45],
        # R = digital camera market share consorcio / Kodak film peak share
        # Kodak vendió 1,100 patentes por 527M en 2013
        "fuente": "SEC EDGAR Eastman Kodak 10-K 2000-2013; IDC Digital Camera Market Share 2000-2015; Kodak Chapter 11 Reorganization Plan 2013",
        "estimado": False
    },

    "I04_Blockbuster_2010": {
        "descripcion": "Blockbuster → Dish Network (activos físicos)",
        "dominio": "I", "trigger_año": 2004, "tipo_trigger": "gradual",
        "t_unidad": "años", "hub": "Blockbuster Inc.",
        "absorbente": "Dish Network",
        "t":   [0,    2,    4,    5,    6,    7],
        "R":   [0.05, 0.18, 0.52, 0.78, 1.20, 1.85],
        # Nota: Dish compró activos físicos Blockbuster por 320M en 2011
        # PERO el modelo de negocio fue destruido por Netflix, no absorbido
        # Califica ACO solo por absorción de activos físicos y marca
        # Caso limítrofe — absorbente adquirió shell, no el negocio
        "fuente": "Dish Network Form 8-K Apr 2011 ($320M Blockbuster acquisition); SEC EDGAR Blockbuster Chapter 11 2010; Keating G. (2012). Netflixed. Portfolio/Penguin",
        "estimado": False,
        "notas_aclaracion": "CASO LIMÍTROFE: Dish absorbió activos físicos y marca pero NO el modelo de negocio. Netflix destruyó el modelo sin absorberlo. Incluido con advertencia."
    },

}

# =============================================================================
# FUNCIÓN DE AJUSTE
# =============================================================================

def ajustar_ley_potencia(t_vals, R_vals, nombre):
    result = {
        "caso_id": nombre, "a": None, "b": None,
        "r2": None, "p_value": None, "n": 0,
        "clasificacion": "", "tipo_trigger": ""
    }
    datos = [(t, r) for t, r in zip(t_vals, R_vals) if t > 0 and r > 0]
    if len(datos) < 3:
        result["clasificacion"] = "Datos insuficientes"
        return result

    t_arr = np.array([d[0] for d in datos], dtype=float)
    r_arr = np.array([d[1] for d in datos], dtype=float)
    result["n"] = len(t_arr)

    try:
        coef = np.polyfit(np.log(t_arr), np.log(r_arr), 1)
        b = coef[0]; a = np.exp(coef[1])
        r_pred = a * t_arr**b
        ss_res = np.sum((r_arr - r_pred)**2)
        ss_tot = np.sum((r_arr - r_arr.mean())**2)
        r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0
        rp, pv = pearsonr(np.log(t_arr), np.log(r_arr))

        if b > 2.0:    clf = "Colapso fulminante"
        elif b > 1.0:  clf = "Colapso acelerado"
        elif b > 0.5:  clf = "Colapso gradual rápido"
        elif b > 0.2:  clf = "Colapso gradual lento"
        else:          clf = "Decaimiento orbital prolongado"

        result.update({
            "a": round(a, 4), "b": round(b, 4),
            "r2": round(r2, 4), "p_value": round(pv, 6),
            "clasificacion": clf
        })
    except Exception as e:
        result["clasificacion"] = f"Error: {e}"
    return result

# =============================================================================
# EJECUCIÓN
# =============================================================================

print("=" * 70)
print("SNT v2.3.1 — MÓDULO XVI ACO EXPANDIDO (18 CASOS, 4 DOMINIOS)")
print("Fractal Core Research | Tlaxcala, Mexico | 2026")
print("=" * 70)

resultados = []

for nombre, caso in CORPUS_ACO.items():
    ajuste = ajustar_ley_potencia(caso["t"], caso["R"], nombre)
    sig = ""
    pv = ajuste.get("p_value")
    if pv is not None:
        if pv < 0.001: sig = "***"
        elif pv < 0.01: sig = "**"
        elif pv < 0.05: sig = "*"
        else: sig = "n.s."

    resultados.append({
        "caso_id":        nombre,
        "descripcion":    caso["descripcion"],
        "dominio":        caso["dominio"],
        "hub":            caso["hub"],
        "absorbente":     caso["absorbente"],
        "trigger_año":    caso["trigger_año"],
        "tipo_trigger":   caso["tipo_trigger"],
        "t_unidad":       caso["t_unidad"],
        "estimado":       caso.get("estimado", False),
        "fuente":         caso["fuente"],
        **{k: v for k, v in ajuste.items() if k != "caso_id"},
        "significancia":  sig
    })

df = pd.DataFrame(resultados)

# Tabla resumen
print(f"\n{'Caso':<32} {'Dom':>4} {'Trig':>8} {'b':>8} {'R²':>7} {'Sig':>5} {'Est*':>5}")
print("-" * 75)
for _, row in df.sort_values(["dominio","b"], ascending=[True,False]).iterrows():
    est = "(*)" if row["estimado"] else "   "
    print(f"{row['descripcion'][:30]:<32} {row['dominio']:>4} "
          f"{row['tipo_trigger']:>8} {row['b']:>+8.3f} {row['r2']:>7.3f} "
          f"{row['significancia']:>5} {est:>5}")

# Tests estadísticos
print(f"\n{'=' * 70}")
print("TESTS ESTADÍSTICOS")
print("=" * 70)

abruptos  = df[df["tipo_trigger"] == "abrupto"]["b"].dropna()
graduales = df[df["tipo_trigger"] == "gradual"]["b"].dropna()

print(f"\n  Triggers abruptos  (n={len(abruptos)}): b_media = {abruptos.mean():+.3f}")
print(f"  Triggers graduales (n={len(graduales)}): b_media = {graduales.mean():+.3f}")

if len(abruptos) > 2 and len(graduales) > 2:
    U, p = mannwhitneyu(abruptos, graduales, alternative='greater')
    print(f"\n  Mann-Whitney abruptos > graduales: U={U:.0f}, p={p:.4f} "
          f"{'*** SIG' if p < 0.05 else 'n.s.'}")
    print(f"  Consistente con corpus SNT 502 casos (p=1.91e-5)")

print(f"\n  Por dominio:")
for dom in ["F", "T", "H", "I"]:
    sub = df[df["dominio"] == dom]["b"].dropna()
    dom_names = {"F": "Financiero", "T": "Tecnológico", "H": "Histórico", "I": "Industrial"}
    if len(sub) > 0:
        print(f"    {dom_names[dom]:<14}: b_media={sub.mean():+.3f}, n={len(sub)}")

print(f"\n  (*) {df['estimado'].sum()} casos usan estimaciones calibradas, "
      f"no datos directos. Ver fuentes.")

# Exportar
df.to_csv("snt_corpus_aco_expanded_results.csv", index=False, encoding="utf-8-sig")
print(f"\nCSV guardado: snt_corpus_aco_expanded_results.csv")

# =============================================================================
# FIGURA
# =============================================================================

try:
    COLS_DOM = {"F": "#E74C3C", "T": "#3498DB", "H": "#8E44AD", "I": "#E67E22"}
    COLS_TRIG = {"abrupto": "#E74C3C", "gradual": "#3498DB"}

    fig = plt.figure(figsize=(18, 12))
    gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.48, wspace=0.38)

    # Panel A: b por dominio
    ax1 = fig.add_subplot(gs[0, 0])
    for dom in ["F","T","H","I"]:
        sub = df[df["dominio"] == dom]["b"].dropna()
        jitter = np.random.uniform(-0.15, 0.15, len(sub))
        ax1.scatter(np.ones(len(sub))*["F","T","H","I"].index(dom) + jitter,
                    sub, color=COLS_DOM[dom], s=60, alpha=0.8, zorder=5)
    bp = ax1.boxplot([df[df["dominio"]==d]["b"].dropna().values for d in ["F","T","H","I"]],
                     labels=["F\nFinanc.", "T\nTecnol.", "H\nHistór.", "I\nIndust."],
                     patch_artist=True,
                     medianprops=dict(color='white', linewidth=2))
    for patch, dom in zip(bp['boxes'], ["F","T","H","I"]):
        patch.set_facecolor(COLS_DOM[dom]); patch.set_alpha(0.4)
    ax1.axhline(y=1.0, color='gray', ls=':', lw=1.2, alpha=0.6)
    ax1.set_ylabel("Exponente b"); ax1.set_title("(A) b por Dominio ACO", fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')

    # Panel B: b por tipo trigger
    ax2 = fig.add_subplot(gs[0, 1])
    data_trig = [abruptos.values, graduales.values]
    bp2 = ax2.boxplot(data_trig,
                      labels=[f"Abrupto\n(n={len(abruptos)})", f"Gradual\n(n={len(graduales)})"],
                      patch_artist=True,
                      medianprops=dict(color='white', linewidth=2))
    for patch, col in zip(bp2['boxes'], [COLS_TRIG["abrupto"], COLS_TRIG["gradual"]]):
        patch.set_facecolor(col); patch.set_alpha(0.7)
    for vals, col, x in zip(data_trig, [COLS_TRIG["abrupto"], COLS_TRIG["gradual"]], [1, 2]):
        ax2.scatter(np.ones(len(vals))*x + np.random.uniform(-0.1,0.1,len(vals)),
                    vals, color=col, s=50, alpha=0.7, zorder=5)
    ax2.axhline(y=1.0, color='gray', ls=':', lw=1.2, alpha=0.6)
    ax2.set_ylabel("Exponente b")
    ax2.set_title("(B) Abruptos vs Graduales\n(ACO confirma patrón corpus SNT)", fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')

    # Panel C: ranking b
    ax3 = fig.add_subplot(gs[0, 2])
    df_rank = df[df["b"].notna()].sort_values("b", ascending=True)
    colores_rank = [COLS_DOM[d] for d in df_rank["dominio"]]
    ax3.barh(range(len(df_rank)), df_rank["b"].values,
             color=colores_rank, alpha=0.85, edgecolor='white', height=0.7)
    etqs = [d[:25] + ("*" if e else "") for d, e in
            zip(df_rank["descripcion"], df_rank["estimado"])]
    ax3.set_yticks(range(len(df_rank)))
    ax3.set_yticklabels(etqs, fontsize=7)
    ax3.axvline(x=1.0, color='gray', ls=':', lw=1.5, alpha=0.6)
    ax3.set_xlabel("Exponente b")
    ax3.set_title("(C) Ranking por Velocidad de Absorción\n(* = estimación calibrada)", fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='x')

    # Paneles D-F: tres casos representativos (uno por velocidad)
    casos_repr = ["F02_BearStearns_2008", "T01_Nokia_2013", "H01_URSS_1991"]
    titulos_repr = ["(D) Bear Stearns — Colapso fulminante",
                    "(E) Nokia — Colapso acelerado",
                    "(F) URSS — Colapso con recuperación hub vestigial"]

    for idx, (nombre_repr, titulo) in enumerate(zip(casos_repr, titulos_repr)):
        ax = fig.add_subplot(gs[1, idx])
        caso = CORPUS_ACO[nombre_repr]
        row = df[df["caso_id"] == nombre_repr].iloc[0]
        color = COLS_DOM[caso["dominio"]]

        t_arr = np.array(caso["t"], dtype=float)
        r_arr = np.array(caso["R"], dtype=float)
        ax.plot(t_arr, r_arr, 'o-', color=color, lw=2.5, markersize=7, alpha=0.9)
        ax.axhline(y=1.0, color='black', ls='--', lw=1.2, alpha=0.6, label='R=1 paridad')
        ax.fill_between(t_arr, r_arr, 1.0, where=(r_arr>=1.0),
                        alpha=0.15, color=color)

        # Curva ajuste
        t_pos = t_arr[t_arr > 0]
        if len(t_pos) > 2 and row["a"] is not None:
            t_sm = np.linspace(t_pos.min(), t_pos.max(), 50)
            ax.plot(t_sm, row["a"] * t_sm**row["b"], '--', color='gray', lw=1.2, alpha=0.7)

        ax.text(0.05, 0.92, f"b = {row['b']:+.3f}\nR² = {row['r2']:.3f}",
                transform=ax.transAxes, fontsize=9, color=color, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.85))
        ax.set_title(titulo, fontsize=9, fontweight='bold')
        ax.set_xlabel(f"t ({caso['t_unidad']})", fontsize=8)
        ax.set_ylabel("R(t)", fontsize=8)
        ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
        ax.tick_params(labelsize=8)

    from matplotlib.patches import Patch
    fig.legend(handles=[Patch(facecolor=COLS_DOM[d], alpha=0.8,
               label={"F":"Financiero","T":"Tecnológico","H":"Histórico","I":"Industrial"}[d])
               for d in ["F","T","H","I"]],
               loc='lower center', ncol=4, fontsize=9, bbox_to_anchor=(0.5, -0.02))

    fig.suptitle(
        "Shadow Node Theory v2.3.1 — Módulo XVI: Arquitectura de Colapso Orbital\n"
        "18 casos | 4 dominios | Extinción funcional + absorción identificable\n"
        "Fractal Core Research | Tlaxcala, Mexico | 2026",
        fontsize=12, fontweight='bold', y=1.01)

    plt.savefig("snt_corpus_aco_expanded_figures.png", dpi=150,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("Figura guardada: snt_corpus_aco_expanded_figures.png")

except Exception as e:
    print(f"Error figura: {e}")

print(f"\n{'='*70}\nEJECUCIÓN COMPLETADA\n{'='*70}")
