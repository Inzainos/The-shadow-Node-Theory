"""
Shadow Node Theory v2.4.0 — Interactive Dashboard
Fractal Core Research | Tlaxcala, Mexico | 2026

721 empirical cases across 10 domains and 30 orders of magnitude.
Deploy: Hugging Face Spaces (Streamlit) or local.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="Shadow Node Theory v2.4.0",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "reconstruction_real" / "data"
if not DATA_DIR.exists():
    DATA_DIR = Path(__file__).resolve().parent / "data"

DOMAIN_LABELS = {
    "A": "Cities",
    "B": "Countries (Maddison)",
    "C": "Regions (MX/US)",
    "D": "Digital (HackerEarth)",
    "E1": "Biological invasion",
    "E2": "Predator-prey",
    "E3": "Parasite-host (COVID)",
    "F1": "Planetary",
    "F2": "Stellar",
    "F3": "Multiplanet",
}

FRICTION_MAP = {
    "A": "medium", "B": "high", "C": "high", "D": "low",
    "E1": "none", "E2": "high", "E3": "none",
    "F1": "medium", "F2": "medium", "F3": "low",
}

FRICTION_ORDER = {"none": 0, "low": 1, "medium": 2, "high": 3}

OKABE_ITO = [
    "#E69F00", "#56B4E9", "#009E73", "#F0E442",
    "#0072B2", "#D55E00", "#CC79A7", "#000000",
    "#999999", "#44AA99",
]


@st.cache_data
def load_corpus():
    df = pd.read_csv(DATA_DIR / "snt_corpus_REAL_v5.csv")
    df["domain_label"] = df["dominio"].map(DOMAIN_LABELS).fillna(df["dominio"])
    df["friction"] = df["dominio"].map(FRICTION_MAP).fillna("unknown")
    df["friction_ord"] = df["friction"].map(FRICTION_ORDER).fillna(-1)
    return df


@st.cache_data
def load_aco():
    path = DATA_DIR / "snt_corpus_aco_v29.csv"
    if path.exists():
        return pd.read_csv(path)
    return None


df = load_corpus()
df_aco = load_aco()

# ── Sidebar ──────────────────────────────────────────────────────────────────

st.sidebar.title("🔬 Shadow Node Theory")
st.sidebar.markdown("**v2.4.0** | 721 cases | 10 domains")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Corpus Explorer", "Friction vs b",
     "ACO Module", "Domain Deep Dive", "About"],
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Fractal Core Research**  \n"
    "Tlaxcala, Mexico  \n"
    "[GitHub](https://github.com/Inzainos/The-shadow-Node-Theory) · "
    "[SSRN](https://ssrn.com/abstract=6418778) · "
    "[Zenodo](https://doi.org/10.5281/zenodo.19446521)"
)

# ── Page: Overview ───────────────────────────────────────────────────────────

if page == "Overview":
    st.title("Shadow Node Theory v2.4.0")
    st.markdown(
        "*Scale-Invariant Satellization Across 721 Empirical Cases*  \n"
        "**Elan Zainos Corona** — Fractal Core Research, Tlaxcala, Mexico"
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Cases", f"{len(df):,}")
    col2.metric("Domains", df["dominio"].nunique())
    sig_pct = df["significativo"].mean() * 100
    col3.metric("Significant", f"{sig_pct:.0f}%")
    col4.metric("Mean b", f"{df['b'].mean():+.3f}")

    st.markdown("---")

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Distribution of b by Domain")
        domain_order = (df.groupby("domain_label")["b"].median()
                        .sort_values().index.tolist())
        fig_box = px.box(
            df, x="domain_label", y="b", color="domain_label",
            color_discrete_sequence=OKABE_ITO,
            category_orders={"domain_label": domain_order},
        )
        fig_box.add_hline(y=0, line_dash="dash", line_color="gray",
                          opacity=0.5)
        fig_box.add_hline(y=1, line_dash="dot", line_color="red",
                          opacity=0.4,
                          annotation_text="Roche Radius (b=1)")
        fig_box.update_layout(
            showlegend=False, xaxis_title="", yaxis_title="Exponent b",
            height=450,
        )
        st.plotly_chart(fig_box, use_container_width=True)

    with col_right:
        st.subheader("Cases per Domain")
        domain_counts = (df.groupby("domain_label").size()
                         .reset_index(name="count")
                         .sort_values("count", ascending=True))
        fig_bar = px.bar(
            domain_counts, x="count", y="domain_label",
            orientation="h", color="domain_label",
            color_discrete_sequence=OKABE_ITO,
        )
        fig_bar.update_layout(
            showlegend=False, xaxis_title="Number of Cases",
            yaxis_title="", height=450,
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")
    st.subheader("Summary Table")
    summary = (df.groupby("dominio").agg(
        Domain=("domain_label", "first"),
        Friction=("friction", "first"),
        Cases=("b", "count"),
        b_mean=("b", "mean"),
        b_std=("b", "std"),
        R2_mean=("r2", "mean"),
        Significant_pct=("significativo", "mean"),
    ).reset_index(drop=True))
    summary["b_mean"] = summary["b_mean"].map("{:+.3f}".format)
    summary["b_std"] = summary["b_std"].map("{:.3f}".format)
    summary["R2_mean"] = summary["R2_mean"].map("{:.3f}".format)
    summary["Significant_pct"] = (summary["Significant_pct"] * 100).map(
        "{:.0f}%".format)
    st.dataframe(summary, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.subheader("Central Finding")
    st.info(
        "**Institutional friction is the dominant predictor of b**  \n"
        "Spearman rho = **-0.68**, p = 2.5×10⁻⁹⁷ (n=714)  \n"
        "Friction-free systems: b = +0.95 | High friction: b = +0.09  \n"
        "Mann-Whitney p = 2.4×10⁻⁷⁴"
    )

# ── Page: Corpus Explorer ────────────────────────────────────────────────────

elif page == "Corpus Explorer":
    st.title("Corpus Explorer")
    st.markdown("Explore all 721 cases interactively.")

    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        domains = st.multiselect(
            "Filter by domain",
            options=sorted(df["domain_label"].unique()),
            default=sorted(df["domain_label"].unique()),
        )
    with col_f2:
        b_range = st.slider("b range", float(df["b"].min()),
                             float(df["b"].max()),
                             (float(df["b"].min()), float(df["b"].max())))
    with col_f3:
        sig_only = st.checkbox("Significant only (p<0.05)", value=False)

    mask = (
        df["domain_label"].isin(domains)
        & df["b"].between(*b_range)
    )
    if sig_only:
        mask = mask & df["significativo"]
    df_filt = df[mask]

    st.markdown(f"**{len(df_filt):,}** cases selected")

    fig_scatter = px.scatter(
        df_filt, x="r2", y="b", color="domain_label",
        hover_data=["id", "descripcion", "p", "n"],
        color_discrete_sequence=OKABE_ITO,
        opacity=0.7,
    )
    fig_scatter.add_hline(y=0, line_dash="dash", line_color="gray",
                          opacity=0.4)
    fig_scatter.add_hline(y=1, line_dash="dot", line_color="red",
                          opacity=0.3)
    fig_scatter.update_layout(
        xaxis_title="R²", yaxis_title="Exponent b",
        height=550, legend_title="Domain",
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Distribution of b")
    fig_hist = px.histogram(
        df_filt, x="b", color="domain_label", nbins=50,
        color_discrete_sequence=OKABE_ITO, barmode="stack",
    )
    fig_hist.update_layout(
        xaxis_title="Exponent b", yaxis_title="Count", height=400,
    )
    st.plotly_chart(fig_hist, use_container_width=True)

    with st.expander("Raw data"):
        st.dataframe(df_filt, use_container_width=True, hide_index=True)

# ── Page: Friction vs b ──────────────────────────────────────────────────────

elif page == "Friction vs b":
    st.title("Institutional Friction vs Satellization Exponent")
    st.markdown(
        "The central finding of SNT: friction governs the speed "
        "of satellization."
    )

    df_soc = df[df["dominio"].isin(
        ["A", "B", "C", "D", "E1", "E2", "E3"])].copy()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("b by Friction Level")
        friction_order = ["none", "low", "medium", "high"]
        fig_fric = px.box(
            df_soc, x="friction", y="b", color="friction",
            color_discrete_map={
                "none": "#D55E00", "low": "#E69F00",
                "medium": "#56B4E9", "high": "#009E73",
            },
            category_orders={"friction": friction_order},
        )
        fig_fric.add_hline(y=0, line_dash="dash", line_color="gray",
                           opacity=0.4)
        fig_fric.update_layout(
            showlegend=False, xaxis_title="Friction Level",
            yaxis_title="Exponent b", height=450,
        )
        st.plotly_chart(fig_fric, use_container_width=True)

    with col2:
        st.subheader("Friction-free vs High Friction")
        df_compare = df_soc[df_soc["friction"].isin(["none", "high"])].copy()
        fig_vio = px.violin(
            df_compare, x="friction", y="b", color="friction",
            box=True, points="all",
            color_discrete_map={"none": "#D55E00", "high": "#009E73"},
            category_orders={"friction": ["none", "high"]},
        )
        fig_vio.update_layout(
            showlegend=False,
            xaxis_title="", yaxis_title="Exponent b", height=450,
        )
        st.plotly_chart(fig_vio, use_container_width=True)

    st.markdown("---")
    st.subheader("Case-Level Spearman Scatter")
    fig_spear = px.scatter(
        df_soc, x="friction_ord", y="b", color="domain_label",
        hover_data=["id", "descripcion"],
        color_discrete_sequence=OKABE_ITO, opacity=0.5,
    )
    fig_spear.update_layout(
        xaxis=dict(
            tickvals=[0, 1, 2, 3],
            ticktext=["None", "Low", "Medium", "High"],
            title="Friction Level (ordinal)",
        ),
        yaxis_title="Exponent b", height=500,
    )
    st.plotly_chart(fig_spear, use_container_width=True)

    st.success(
        "**Spearman rho = -0.68**, p = 2.5×10⁻⁹⁷ (n=714)  \n"
        "**Mann-Whitney p = 2.4×10⁻⁷⁴** "
        "(friction-free b=+0.95 vs high friction b=+0.09)"
    )

# ── Page: ACO Module ─────────────────────────────────────────────────────────

elif page == "ACO Module":
    st.title("Module XVI — Orbital Collapse Architecture (ACO)")
    st.markdown(
        "Cases where a hub undergoes **functional extinction** and its "
        "resources are **absorbed by an identifiable node**."
    )

    if df_aco is not None:
        col1, col2, col3 = st.columns(3)
        col1.metric("ACO Cases", len(df_aco))
        col2.metric("Significant",
                     f"{df_aco['significativo'].sum()}/{len(df_aco)}")
        col3.metric("Mean b", f"{df_aco['b'].mean():+.3f}")

        st.markdown("---")

        ACO_LABELS = {
            "F": "Financial", "T": "Technological",
            "H": "Historical", "I": "Industrial",
        }
        df_aco_plot = df_aco.copy()
        df_aco_plot["domain_label"] = df_aco_plot["dominio"].map(ACO_LABELS)

        col_left, col_right = st.columns(2)

        with col_left:
            st.subheader("Absorption Speed by Domain")
            fig_aco_box = px.box(
                df_aco_plot, x="domain_label", y="b",
                color="domain_label",
                color_discrete_sequence=OKABE_ITO, points="all",
            )
            fig_aco_box.add_hline(y=1, line_dash="dot", line_color="red",
                                  opacity=0.4,
                                  annotation_text="Accelerated collapse")
            fig_aco_box.update_layout(
                showlegend=False, xaxis_title="",
                yaxis_title="Exponent b", height=400,
            )
            st.plotly_chart(fig_aco_box, use_container_width=True)

        with col_right:
            st.subheader("Abrupt vs Gradual Triggers")
            fig_trig = px.box(
                df_aco_plot, x="tipo_trigger", y="b",
                color="tipo_trigger", points="all",
                color_discrete_map={
                    "abrupto": "#D55E00", "gradual": "#0072B2"},
            )
            fig_trig.update_layout(
                showlegend=False, xaxis_title="",
                yaxis_title="Exponent b", height=400,
            )
            st.plotly_chart(fig_trig, use_container_width=True)

        st.subheader("ACO Ranking — Absorption Speed")
        df_rank = df_aco_plot.sort_values("b", ascending=True)
        est_marker = df_rank["estimado"].map({True: " (*)", False: ""})
        df_rank["label"] = df_rank["descripcion"] + est_marker
        fig_rank = px.bar(
            df_rank, x="b", y="label", orientation="h",
            color="domain_label",
            color_discrete_sequence=OKABE_ITO,
            hover_data=["r2", "p", "tipo_trigger"],
        )
        fig_rank.add_vline(x=1.0, line_dash="dot", line_color="red",
                           opacity=0.4)
        fig_rank.update_layout(
            xaxis_title="Exponent b", yaxis_title="",
            height=500, legend_title="Domain",
        )
        st.plotly_chart(fig_rank, use_container_width=True)

        st.markdown("(*) = calibrated estimates from secondary sources")

        with st.expander("ACO raw data"):
            st.dataframe(df_aco, use_container_width=True, hide_index=True)
    else:
        st.warning("ACO data not found.")

# ── Page: Domain Deep Dive ───────────────────────────────────────────────────

elif page == "Domain Deep Dive":
    st.title("Domain Deep Dive")

    domain_sel = st.selectbox(
        "Select domain",
        options=sorted(df["domain_label"].unique()),
    )
    df_dom = df[df["domain_label"] == domain_sel]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Cases", len(df_dom))
    col2.metric("Mean b", f"{df_dom['b'].mean():+.3f}")
    col3.metric("Mean R²", f"{df_dom['r2'].mean():.3f}")
    sig_d = df_dom["significativo"].mean() * 100
    col4.metric("Significant", f"{sig_d:.0f}%")

    fig_dom = px.scatter(
        df_dom, x="r2", y="b",
        hover_data=["id", "descripcion", "p", "n"],
        color_discrete_sequence=[OKABE_ITO[0]],
        size="n", size_max=15,
    )
    fig_dom.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.4)
    fig_dom.update_layout(
        xaxis_title="R²", yaxis_title="Exponent b", height=500,
    )
    st.plotly_chart(fig_dom, use_container_width=True)

    fig_hist_d = px.histogram(df_dom, x="b", nbins=30,
                              color_discrete_sequence=[OKABE_ITO[1]])
    fig_hist_d.update_layout(
        xaxis_title="Exponent b", yaxis_title="Count", height=350,
    )
    st.plotly_chart(fig_hist_d, use_container_width=True)

    with st.expander("Domain data"):
        st.dataframe(df_dom, use_container_width=True, hide_index=True)

# ── Page: About ──────────────────────────────────────────────────────────────

elif page == "About":
    st.title("About Shadow Node Theory")

    st.markdown("""
When two coupled entities interact over time — a dominant **hub** and a
peripheral **node** — the dominance ratio evolves following a power law:

**R(t) = a · t^b**

The sign and magnitude of **b** summarize the direction and speed of
**satellization** — the process by which a peripheral entity loses or gains
relative standing against a dominant core.

```
b < 0     → convergence (node gains ground)
b ~ 0     → dynamic equilibrium
0 < b < 1 → sublinear satellization (gradual)
b >= 1    → superlinear satellization — Roche Radius
```

### Falsifiability Criteria (RC1-RC8)

| RC | Refutation Condition | v29 Status |
|----|---------------------|------------|
| RC1 | Power law fits no better than alternatives | NOT REFUTED |
| RC2 | b is not reproducible from primary series | NOT REFUTED |
| RC3 | Abrupt triggers produce same b as gradual | NOT REFUTED |
| RC4 | Friction index is not correlated with b | NOT REFUTED |
| RC5 | N-body matrix does not change estimates | NOT REFUTED |
| RC6 | Shadow node reverses without trigger | NOT REFUTED |
| RC7 | ASI does not predict better than chance | NOT REFUTED |
| RC8 | Mutual interdependence does not brake | NOT REFUTED |

### Citation

```
Zainos Corona, E. (2026). Shadow Node Theory v2.4.0:
Scale-Invariant Satellization Across 721 Empirical Cases.
Zenodo. doi:10.5281/zenodo.19446521
```

### Contact

Elan Zainos Corona — Fractal Core Research — Tlaxcala, Mexico
- ORCID: 0009-0009-9125-253X
- GitHub: [Inzainos](https://github.com/Inzainos)
    """)
