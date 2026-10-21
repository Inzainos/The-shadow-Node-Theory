#!/usr/bin/env python3
"""
Tela de Incertidumbre — SNT (Shadow Node Theory)
================================================

Implementa el cubo de incertidumbre 𝒞(u, m, τ) del Axioma 0.1 del marco
teórico v34 (papers/marco_teorico.md, líneas 97-118).

DEFINICIONES DEL MARCO v34 (obligatorias, no negociables):

    m = R — el proxy declarado de cada dominio
          (ACO: masa_absorbente/masa_pico; B: PIBpc_hub/PIBpc_nodo;
           E3: casos acumulados; etc.)
          NO es |b|. Es la RAZÓN medida en cada punto temporal.

    τ = fase temporal normalizada del proceso — la fase sobre la que
        ya opera h(τ). Es el tiempo transcurrido desde el trigger
        (satelización) o extinción funcional (colapso), normalizado
        a [0, 1] dentro de la ventana observada del caso.

    u = NO ESTÁ DEFINIDO EN NINGÚN DOMINIO (marco v34, línea 112).
        "Es el eje que hace del cubo un cubo y hoy está vacío."
        "Lo que falta se queda faltando y no se rellena con un
        proxy inventado para completar la figura."
        → u = NULL para todos los casos. Sin excepciones.

    φ = campo escalar de fricción sobre el volumen (Axioma 0.1 §fricción).
        POSTULADO, NO MEDIDO. Existe como fricción categórica por dominio
        (11 dominios del README) y ordinal 1-6 para la cohorte 2008 (n=6).

REGLA DE ADMISIÓN DE EJES (v34, línea 114):
    Un eje entra a 𝒞 cuando tiene definición operativa en dos dominios
    o más. Con uno solo es etiqueta, no coordenada.
    → m entra (todos los dominios miden R).
    → τ entra (todos los dominios miden tiempo desde trigger).
    → u NO entra (cero dominios lo definen).
    → El volumen opera en (m, τ).

SOMBRA (Axioma 0.2):
    𝒮ᶿ = Π_θ(𝒞) con θ = (B, V, ρ, W, λ) declarado:
      B = base de observación (ejes m, τ)
      V = variables: R crudo (serie real) / R ajustado R=a·t^b (sombras)
      ρ = 1 punto por dato (serie real) / 1 punto por caso (sombras)
      W = ventana completa de cada caso
      λ = sin corte (todos los puntos)

v2 (2026-10-21): INTEGRADA. La tela prefiere la SERIE REAL de la capa
exógena (data/tela_exogena_series.csv — E3 234, B 446, ACO 18, G 1) y
solo mapea como sombra los casos sin serie cruda versionada
(A, C, D, E1, E2, F: 41 casos). Genera tela_exogena_series.csv primero
(code/tela_exogena.py) — sin ella este script degrada a ACO + sombras.

Uso (desde la raíz del repo):
    python reconstruction_real/code/tela_de_incertidumbre.py
"""

import csv
import logging
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "code"))

DATA = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "tela_de_incertidumbre.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("tela_de_incertidumbre")

# Fricción categórica por dominio (11 dominios del README SNT).
# POSTULADO NO MEDIDO — ver Axioma 0.1 §fricción del marco v34.
FRICCION_POR_DOMINIO = {
    "A": "media",    # ciudades: fricción institucional media
    "B": "alta",     # países: fricción institucional alta
    "C": "alta",     # estados EEUU: fricción alta
    "D": "nula",     # HackerEarth: digital, sin fricción medida
    "E1": "nula",    # expansión territorial: sin fricción
    "E2": "alta",    # biológico presa-depredador: alta
    "E3": "nula",    # epidémico: sin fricción
    "F": "fisica",   # planetario: fricción física (dinámica)
    "F1": "fisica",
    "F2": "fisica",
    "F3": "fisica",
    "G": "fisica",    # geoquímico/planetario (Bennu): fricción física
    "ACO": "variable",  # colapso: depende del caso (regulado/craquelado/etc)
    "ACO-F": "alta",
    "ACO-H": "alta",
    "ACO-I": "alta",
    "ACO-T": "alta",
}

# Marco de medición θ (Axioma 0.2) — declarado, no configurable en runtime
THETA = {
    "B": "(m, τ)",       # base de observación: ejes m y τ
    "V": "R crudo (ACO) / R ajustado a·t^b (otros dominios)",
    "rho": "1 punto por dato (ACO) / 1 punto por caso (otros)",
    "W": "ventana completa del caso (t_min a t_max)",
    "lambda": "sin corte",
}


def _f(x, default=float("nan")):
    try:
        v = float(x)
        return v if v == v else default
    except (TypeError, ValueError):
        return default


def _f_int(x, default=None):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return default


def cargar_series_reales() -> dict[str, dict]:
    """
    Carga las series (t, R) reales de la capa exógena
    (data/tela_exogena_series.csv — 699 casos: E3, B, ACO, G).

    Si la capa exógena no existe (p. ej. checkout limpio sin correr
    tela_exogena.py), degrada a la serie ACO v29 sola (18 casos) — el
    resto del pipeline sigue funcionando con sombras.
    """
    ruta_exogena = DATA / "tela_exogena_series.csv"
    ruta_aco = DATA / "snt_corpus_aco_timeseries_v29.csv"
    series: dict[str, dict] = {}
    if ruta_exogena.exists():
        for r in csv.DictReader(ruta_exogena.open(encoding="utf-8")):
            cid = r.get("id", "")
            t = _f(r.get("t"), None)
            R = _f(r.get("R"), None)
            if not cid or t is None or R is None or t <= 0 or R <= 0:
                continue
            series.setdefault(cid, {
                "dominio": r.get("dominio", ""),
                "unidad": r.get("t_unidad", ""),
                "puntos": [],
            })["puntos"].append({"t": t, "R": R})
        for cid in series:
            series[cid]["puntos"].sort(key=lambda p: p["t"])
        return series
    if ruta_aco.exists():
        log.warning("Sin capa exógena — degradando a serie ACO v29 (18 casos)")
        for r in csv.DictReader(ruta_aco.open(encoding="utf-8-sig")):
            cid = r.get("id", "")
            t = _f(r.get("t"), None)
            R = _f(r.get("R"), None)
            if t is not None and R is not None and t > 0 and R > 0:
                series.setdefault(cid, {
                    "dominio": "ACO",
                    "unidad": r.get("t_unidad", ""),
                    "puntos": [],
                })["puntos"].append({"t": t, "R": R})
        for cid in series:
            series[cid]["puntos"].sort(key=lambda p: p["t"])
    return series


def cargar_corpus_v5() -> list[dict]:
    """Carga el corpus consolidado v5 (721 casos)."""
    ruta = DATA / "snt_corpus_REAL_v5.csv"
    if not ruta.exists():
        raise FileNotFoundError(f"No se encuentra {ruta}")
    return list(csv.DictReader(ruta.open(encoding="utf-8-sig")))


def calcular_m(R: float | None) -> float | None:
    """m = R. El proxy declarado del dominio. NO es |b|."""
    if R is None or R != R:
        return None
    return round(float(R), 6)


def calcular_tau(t: float, t_min: float, t_max: float) -> float | None:
    """τ = fase temporal normalizada a [0, 1] dentro de la ventana del caso."""
    if t_max <= t_min:
        return None
    tau = (t - t_min) / (t_max - t_min)
    return round(max(0.0, min(1.0, tau)), 4)


def generar_trayectoria_ajustada(b: float, n: int, t_min: float = 1.0) -> list[tuple[float, float]]:
    """
    Genera la trayectoria R(t) = a·t^b desde los parámetros ajustados.

    Para dominios sin serie cruda (B, E3, A, C, etc.) solo conocemos
    (b, n). La escala 'a' no está en el corpus v5, pero para mapear
    la FORMA de la trayectoria en (m, τ), normalizamos a = 1
    (R relativa) y usamos t = 1..n como proxy temporal.

    ADVERTENCIA: esto es una sombra del modelo ajustado, NO los datos
    crudos. El marco v34 (Axioma 0.2) permite sombras — son proyecciones
    legítimas del volumen, no el volumen mismo.
    """
    if b is None or n is None or n < 2:
        return []
    ts = np.arange(1.0, float(n) + 1.0)
    Rs = ts ** float(b)
    return [(float(t), float(R)) for t, R in zip(ts, Rs)]


def main():
    log.info("=" * 78)
    log.info("TELA DE INCERTIDUMBRE — SNT v34 (Axioma 0.1)")
    log.info("=" * 78)
    log.info("θ = (B=%s, V=%s, ρ=%s, W=%s, λ=%s)",
             THETA["B"], THETA["V"], THETA["rho"], THETA["W"], THETA["lambda"])
    log.info("")
    log.info("Ejes del cubo 𝒞(u, m, τ):")
    log.info("  m = R (proxy del dominio) — DEFINIDO en todos los dominios")
    log.info("  τ = fase temporal normalizada — DEFINIDO (fase de h(τ))")
    log.info("  u = NO DEFINIDO en ningún dominio — NULL (regla v34:112)")
    log.info("  φ = fricción, campo POSTULADO (categórico por dominio)")
    log.info("")

    # Cargar datos
    series_reales = cargar_series_reales()
    corpus = cargar_corpus_v5()
    log.info("Series reales (capa exógena): %d casos", len(series_reales))
    log.info("Corpus v5: %d casos", len(corpus))

    filas_tela = []

    # ---- Casos con serie real (exógena: E3, B, ACO, G) ----
    for cid in sorted(series_reales):
        info = series_reales[cid]
        dominio = info["dominio"]
        t_vals = [p["t"] for p in info["puntos"]]
        R_vals = [p["R"] for p in info["puntos"]]
        t_min, t_max = min(t_vals), max(t_vals)

        for t, R in zip(t_vals, R_vals):
            tau = calcular_tau(t, t_min, t_max)
            m = calcular_m(R)
            filas_tela.append({
                "id": cid,
                "dominio": dominio,
                "fuente": "serie_cruda",
                "t": round(t, 4),
                "R": round(R, 6),
                "m": m,
                "tau": tau,
                "u": None,  # NO DEFINIDO (marco v34:112)
                "phi_friccion": FRICCION_POR_DOMINIO.get(dominio, ""),
                "theta_B": THETA["B"],
                "theta_V": "R crudo",
            })

    log.info("Serie cruda: %d puntos mapeados al cubo desde series reales",
             len(filas_tela))

    # ---- Casos del corpus SIN serie real: sombra del modelo ajustado ----
    # Solo los casos sin serie cruda versionada (A, C, D, E1, E2, F) se
    # mapean como sombra R(t) = a·t^b con a=1 (R relativa) y t=1..n.
    # Marco v34 Axioma 0.2: "una sombra es válida y parcial a la vez".
    casos_con_sombra = 0
    for r in corpus:
        cid = r.get("id", "")
        dominio = r.get("dominio", "")

        # Ya mapeado arriba con serie real
        if cid in series_reales:
            continue

        b = _f(r.get("b"), None)
        n = _f_int(r.get("n"), None)

        if b is None or n is None or n < 2:
            continue

        trayectoria = generar_trayectoria_ajustada(b, n)
        if not trayectoria:
            continue

        casos_con_sombra += 1
        t_min = trayectoria[0][0]
        t_max = trayectoria[-1][0]

        # Muestrear 10 puntos por trayectoria (sombra, no datos crudos)
        indices = np.linspace(0, len(trayectoria) - 1,
                               min(10, len(trayectoria))).astype(int)
        for idx in indices:
            t, R = trayectoria[idx]
            tau = calcular_tau(t, t_min, t_max)
            m = calcular_m(R)
            filas_tela.append({
                "id": cid,
                "dominio": dominio,
                "fuente": "sombra_modelo_ajustado",
                "t": round(t, 4),
                "R": round(R, 6),
                "m": m,
                "tau": tau,
                "u": None,  # NO DEFINIDO (marco v34:112)
                "phi_friccion": FRICCION_POR_DOMINIO.get(dominio, ""),
                "theta_B": THETA["B"],
                "theta_V": "R ajustado a·t^b (a=1 relativa)",
            })

    log.info("Otros dominios (sin serie real): %d casos con sombra del "
             "modelo ajustado", casos_con_sombra)
    log.info("Total de puntos en la tela: %d", len(filas_tela))

    # ---- Escribir CSV ----
    columnas = [
        "id", "dominio", "fuente", "t", "R", "m", "tau", "u",
        "phi_friccion", "theta_B", "theta_V",
    ]
    out_path = DATA / "tela_de_incertidumbre.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=columnas)
        w.writeheader()
        for fila in filas_tela:
            w.writerow({k: fila.get(k, "") for k in columnas})
    log.info("Escrito %s (%d puntos)", out_path, len(filas_tela))

    # ---- Estadísticas por dominio ----
    log.info("")
    log.info("=" * 78)
    log.info("ESTADO DEL CUBO 𝒞(u, m, τ) — OPERA EN (m, τ)")
    log.info("=" * 78)

    por_dominio = {}
    for f in filas_tela:
        d = f["dominio"]
        if d not in por_dominio:
            por_dominio[d] = {"n_puntos": 0, "casos": set(),
                             "m_min": None, "m_max": None, "m_mediana": []}
        por_dominio[d]["n_puntos"] += 1
        por_dominio[d]["casos"].add(f["id"])
        if f["m"] is not None:
            por_dominio[d]["m_mediana"].append(f["m"])
            if por_dominio[d]["m_min"] is None or f["m"] < por_dominio[d]["m_min"]:
                por_dominio[d]["m_min"] = f["m"]
            if por_dominio[d]["m_max"] is None or f["m"] > por_dominio[d]["m_max"]:
                por_dominio[d]["m_max"] = f["m"]

    log.info("")
    log.info("Dominio | Casos | Puntos | m=R mínimo | m=R máximo | φ fricción")
    log.info("-" * 70)
    for d, st in sorted(por_dominio.items()):
        phi = FRICCION_POR_DOMINIO.get(d, "?")
        log.info("  %5s | %5d | %6d | %10.4f | %10.4f | %s" % (
            d, len(st["casos"]), st["n_puntos"],
            st["m_min"] if st["m_min"] is not None else float("nan"),
            st["m_max"] if st["m_max"] is not None else float("nan"),
            phi))

    log.info("")
    log.info("Eje u: %d/%d puntos definidos (0%%) — PENDIENTE (marco v34:112)",
             sum(1 for f in filas_tela if f["u"] is not None),
             len(filas_tela))
    log.info("Eje m: %d/%d puntos definidos — R, proxy del dominio",
             sum(1 for f in filas_tela if f["m"] is not None),
             len(filas_tela))
    log.info("Eje τ: %d/%d puntos definidos — fase temporal normalizada",
             sum(1 for f in filas_tela if f["tau"] is not None),
             len(filas_tela))
    log.info("Campo φ: POSTULADO, no medido (categórico por dominio)")

    log.info("")
    log.info("NOTA: los puntos de dominios sin serie cruda son SOMBRAS")
    log.info("del modelo ajustado R=a·t^b (a=1 relativa), no datos crudos.")
    reales = sum(1 for f in filas_tela if f["fuente"] == "serie_cruda")
    sombras = sum(1 for f in filas_tela
                  if f["fuente"] == "sombra_modelo_ajustado")
    log.info("Serie real: %d puntos | Sombras: %d puntos", reales, sombras)

    return 0


if __name__ == "__main__":
    sys.exit(main())