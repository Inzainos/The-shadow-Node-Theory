"""
Recálculo de la afirmación "los disparadores abruptos satelizan más rápido que
los graduales" (hallazgo 1 del README: razón 5.9×, Mann-Whitney U=24,802,
p=1.91e-5, n=486; criterios RC3 y RC-ACO-2).

La auditoría v32 marcó esa cifra como NO REPRODUCIBLE: el corpus activo de 721
casos no tiene variable de disparador utilizable (`trigger` está fijo en
'gradual' para los 446 casos del dominio B) y n=486 no es subconjunto de 721.
Este script recalcula la comparación sobre TODOS los conjuntos del repo que sí
traen etiqueta abrupto/gradual y separa lo activo de lo histórico:

  1. ACTIVO    reconstruction_real/data/snt_corpus_aco_v29.csv   (ACO, 18 casos)
  2. HISTÓRICO data/shadow_node_maddison_resumen.csv            (v1.0, 4 casos)
  3. HISTÓRICO data/snt_corpus_50_resultados_v2.csv             (v2.0, 57 casos)
  4. ACTIVO    reconstruction_real/data/by_domain/dominio_B_real.csv
               (446 casos, todos 'gradual' por asignación -> no testeable)

Ojo con qué mide cada b: en el corpus de satelización, R = dominancia
hub/nodo (criterio RC3 del README); en ACO, R = masa del absorbente / masa
pico del hub que colapsa, un exponente de ABSORCIÓN (criterio RC-ACO-2). Las
filas ACO NO prueban RC3; se reportan porque son los únicos datos activos
con etiqueta de disparador. En ACO el disparador está confundido con el
dominio (F: todo abrupto; I: todo gradual), así que además de la comparación
global se reporta una prueba de permutación EXACTA estratificada por dominio,
que solo usa la variación de disparador dentro de cada dominio.

Datos reales, sin imputación: los casos sin b se excluyen y se registran.
Los conjuntos históricos son anteriores a v2.4.0 y NO son citables (aviso del
README); se recalculan solo para rastrear el origen de la cifra.

Salidas:
    reconstruction_real/data/trigger_abrupto_gradual_recalculo.csv
    reconstruction_real/logs/recalculo_trigger_abrupto_gradual_log.txt

Uso:
    python reconstruction_real/code/recalculo_trigger_abrupto_gradual.py
"""

import itertools
import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

# =============================================================================
# RUTAS
# =============================================================================

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

IN_ACO = DATA_DIR / "snt_corpus_aco_v29.csv"
IN_B = DATA_DIR / "by_domain" / "dominio_B_real.csv"
IN_V10 = ROOT / "data" / "shadow_node_maddison_resumen.csv"
IN_V20 = ROOT / "data" / "snt_corpus_50_resultados_v2.csv"

OUT_CSV = DATA_DIR / "trigger_abrupto_gradual_recalculo.csv"
LOG_FILE = LOG_DIR / "recalculo_trigger_abrupto_gradual_log.txt"

# Cifra publicada que se recalcula (README, hallazgo 1)
PUBLICADO = "razón 5.9x; Mann-Whitney U=24,802, p=1.91e-5, n=486"

# =============================================================================
# LOGGING (misma convención que build_dominio_G.py)
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("TRIGGER-RECALC")


# =============================================================================
# FUNCIONES
# =============================================================================

def normalizar_trigger(serie):
    """Unifica etiquetas: 'Abrupto'/'abrupto' -> 'abrupto', etc."""
    return serie.astype(str).str.strip().str.lower()


DENOM_MIN = 0.01  # |b| por debajo de esto: razón no definida


def razon(num, den):
    """num/den, o NaN si el denominador es casi nulo o no existe."""
    if den is None or np.isnan(den) or abs(den) < DENOM_MIN:
        return np.nan
    return num / den


def comparar(abr, gra):
    """Compara b entre abruptos y graduales.

    Devuelve medias, medianas, razones, Mann-Whitney (dos colas y una cola
    abrupto > gradual) y la correlación rango-biserial. Usa el método exacto
    cuando no hay empates; si los hay, el asintótico.
    """
    abr = np.asarray(abr, dtype=float)
    gra = np.asarray(gra, dtype=float)
    res = {
        "n_abrupto": len(abr),
        "n_gradual": len(gra),
        "b_media_abrupto": abr.mean() if len(abr) else np.nan,
        "b_media_gradual": gra.mean() if len(gra) else np.nan,
        "b_mediana_abrupto": np.median(abr) if len(abr) else np.nan,
        "b_mediana_gradual": np.median(gra) if len(gra) else np.nan,
    }
    # Una razón con denominador casi nulo no tiene interpretación: NaN.
    res["razon_medias"] = razon(res["b_media_abrupto"], res["b_media_gradual"])
    res["razon_medianas"] = razon(res["b_mediana_abrupto"],
                                  res["b_mediana_gradual"])
    if len(abr) >= 2 and len(gra) >= 2:
        empates = len(np.unique(np.concatenate([abr, gra]))) < len(abr) + len(gra)
        metodo = "asymptotic" if empates else "exact"
        u2, p2 = mannwhitneyu(abr, gra, alternative="two-sided", method=metodo)
        _, p1 = mannwhitneyu(abr, gra, alternative="greater", method=metodo)
        res.update({
            "U": float(u2), "p_dos_colas": float(p2),
            "p_una_cola_abrupto_mayor": float(p1),
            "rango_biserial": 2.0 * u2 / (len(abr) * len(gra)) - 1.0,
            "metodo_mw": metodo,
        })
    else:
        res.update({"U": np.nan, "p_dos_colas": np.nan,
                    "p_una_cola_abrupto_mayor": np.nan,
                    "rango_biserial": np.nan, "metodo_mw": "n insuficiente"})
    return res


def permutacion_estratificada(df, col_estrato, col_trigger="trigger",
                              col_b="b"):
    """Prueba de permutación EXACTA estratificada por dominio.

    Estadístico: suma, sobre los estratos que tienen ambos disparadores, de
    (media b abrupto - media b gradual). Se enumeran todas las asignaciones de
    etiquetas que conservan el número de abruptos de cada estrato. Los
    estratos con un solo tipo de disparador no aportan variación y se
    reportan aparte.
    """
    informativos, no_informativos = [], []
    for nombre, g in df.groupby(col_estrato):
        tipos = set(g[col_trigger])
        if {"abrupto", "gradual"} <= tipos:
            informativos.append((nombre, g[col_b].to_numpy(float),
                                 (g[col_trigger] == "abrupto").to_numpy()))
        else:
            no_informativos.append((nombre, len(g), ",".join(sorted(tipos))))

    def estadistico(asignaciones):
        total = 0.0
        for (_, b, _), mask in zip(informativos, asignaciones):
            total += b[mask].mean() - b[~mask].mean()
        return total

    if not informativos:
        return None, no_informativos, informativos

    observado = estadistico([m for _, _, m in informativos])
    espacios = []
    for _, b, mask in informativos:
        k = int(mask.sum())
        combos = []
        for idx in itertools.combinations(range(len(b)), k):
            m = np.zeros(len(b), dtype=bool)
            m[list(idx)] = True
            combos.append(m)
        espacios.append(combos)
    valores = np.array([estadistico(a) for a in itertools.product(*espacios)])
    p_mayor = float(np.mean(valores >= observado - 1e-12))
    p_dos = float(np.mean(np.abs(valores) >= abs(observado) - 1e-12))
    return ({"observado": observado, "n_permutaciones": len(valores),
             "p_una_cola_abrupto_mayor": p_mayor, "p_dos_colas": p_dos},
            no_informativos, informativos)


def fila(dataset, estatus, analisis, res, nota=""):
    base = {"dataset": dataset, "estatus": estatus, "analisis": analisis}
    base.update(res)
    base["nota"] = nota
    return base


def fmt(res):
    return (f"n_abr={res['n_abrupto']} n_grad={res['n_gradual']} | "
            f"b̄ abr={res['b_media_abrupto']:+.4f} grad={res['b_media_gradual']:+.4f} "
            f"razón={res['razon_medias']:.3f} | "
            f"mediana abr={res['b_mediana_abrupto']:+.4f} grad={res['b_mediana_gradual']:+.4f} "
            f"razón={res['razon_medianas']:.3f} | U={res['U']} "
            f"p2={res['p_dos_colas']:.4g} p1(abr>grad)={res['p_una_cola_abrupto_mayor']:.4g} "
            f"r_rb={res['rango_biserial']:+.3f} [{res['metodo_mw']}]")


# =============================================================================
# EJECUCIÓN
# =============================================================================

def main():
    log.info("=" * 78)
    log.info("RECÁLCULO abrupto vs gradual — cifra publicada: %s", PUBLICADO)
    log.info("=" * 78)
    filas = []

    # ---------------------------------------------------------------- 1. ACO
    aco = pd.read_csv(IN_ACO)
    aco["trigger"] = normalizar_trigger(aco["tipo_trigger"])
    sin_b = aco["b"].isna().sum()
    aco = aco.dropna(subset=["b"])
    log.info("[1] ACTIVO  %s  n=%d (sin b excluidos: %d)",
             IN_ACO.name, len(aco), sin_b)

    r = comparar(aco.loc[aco.trigger == "abrupto", "b"],
                 aco.loc[aco.trigger == "gradual", "b"])
    log.info("    Global            : %s", fmt(r))
    filas.append(fila("ACO v29 (18 casos)", "ACTIVO", "global", r,
                      "b de absorción (RC-ACO-2), no de satelización (RC3); "
                      "trigger confundido con dominio (F todo abrupto, I todo gradual)"))

    ver = aco[~aco["estimado"].astype(bool)]
    r = comparar(ver.loc[ver.trigger == "abrupto", "b"],
                 ver.loc[ver.trigger == "gradual", "b"])
    log.info("    Solo verificados  : %s", fmt(r))
    filas.append(fila("ACO v29 (solo verificados)", "ACTIVO",
                      "sensibilidad: excluye casos estimado=True", r,
                      f"excluidos {int(aco['estimado'].astype(bool).sum())} estimados"))

    for dom, g in aco.groupby("dominio"):
        log.info("    Dominio %s: %s", dom,
                 ", ".join(f"{t}={v:+.3f}" for t, v in
                           zip(g.trigger, g.b)))

    perm, no_inf, inf = permutacion_estratificada(aco, "dominio")
    for nombre, n, tipos in no_inf:
        log.info("    Estrato %s (n=%d) sin variación de disparador (%s): "
                 "no aporta a la prueba intra-dominio", nombre, n, tipos)
    if perm:
        log.info("    Permutación exacta estratificada (estratos %s): "
                 "estadístico=%+.4f, %d permutaciones, p1(abr>grad)=%.4f, p2=%.4f",
                 ",".join(n for n, _, _ in inf), perm["observado"],
                 perm["n_permutaciones"], perm["p_una_cola_abrupto_mayor"],
                 perm["p_dos_colas"])
        filas.append(fila(
            "ACO v29 (intra-dominio)", "ACTIVO",
            "permutación exacta estratificada por dominio",
            {"n_abrupto": int(sum(m.sum() for _, _, m in inf)),
             "n_gradual": int(sum((~m).sum() for _, _, m in inf)),
             "U": np.nan, "p_dos_colas": perm["p_dos_colas"],
             "p_una_cola_abrupto_mayor": perm["p_una_cola_abrupto_mayor"],
             "metodo_mw": f"permutación exacta ({perm['n_permutaciones']})"},
            f"estratos informativos: {','.join(n for n, _, _ in inf)}; "
            f"estadístico Σ(b̄abr−b̄grad)={perm['observado']:+.4f}"))

    # ------------------------------------------------------------ 2. v1.0
    v10 = pd.read_csv(IN_V10)
    v10["trigger"] = normalizar_trigger(v10["tipo_trigger"])
    r = comparar(v10.loc[v10.trigger == "abrupto", "exponente_b"],
                 v10.loc[v10.trigger == "gradual", "exponente_b"])
    log.info("[2] HISTÓRICO %s (v1.0): %s", IN_V10.name, fmt(r))
    filas.append(fila("v1.0 Maddison resumen (4 casos)", "HISTÓRICO (no citable)",
                      "global", r,
                      "origen de la razón ~5.9x: 2 abruptos vs 2 graduales"))

    # ------------------------------------------------------------ 3. v2.0
    v20 = pd.read_csv(IN_V20)
    v20["trigger"] = normalizar_trigger(v20["tipo_trigger"])
    n_hib = int((v20.trigger == "hibrido").sum())
    n_r2neg = int((v20["r2"] < 0).sum())
    v20 = v20.dropna(subset=["b"])
    r = comparar(v20.loc[v20.trigger == "abrupto", "b"],
                 v20.loc[v20.trigger == "gradual", "b"])
    log.info("[3] HISTÓRICO %s (v2.0): %s", IN_V20.name, fmt(r))
    log.info("    excluidos 'hibrido': %d | casos con R² < 0 (imposible): %d",
             n_hib, n_r2neg)
    filas.append(fila("v2.0 corpus 57 casos", "HISTÓRICO (no citable)",
                      "global (sin híbridos)", r,
                      f"{n_hib} híbridos excluidos; {n_r2neg} casos con R²<0"))

    # --------------------------------------------------------- 4. Dominio B
    b = pd.read_csv(IN_B)
    conteo = normalizar_trigger(b["trigger"]).value_counts().to_dict()
    log.info("[4] ACTIVO  %s: trigger=%s -> NO TESTEABLE "
             "(asignación fija en expand_dominio_B.py)", IN_B.name, conteo)
    filas.append(fila("Dominio B (446 casos)", "ACTIVO", "no testeable",
                      {"n_abrupto": conteo.get("abrupto", 0),
                       "n_gradual": conteo.get("gradual", 0)},
                      "trigger fijo en 'gradual' para todos los casos"))

    log.info("[5] n=486 publicado: no corresponde a ningún conjunto del repo "
             "(721 activo; 18 ACO; 57 v2.0; 4 v1.0).")

    out = pd.DataFrame(filas)
    out.to_csv(OUT_CSV, index=False, float_format="%.6g")
    log.info("CSV -> %s", OUT_CSV.relative_to(ROOT))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
