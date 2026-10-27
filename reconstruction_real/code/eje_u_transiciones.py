"""Evaluate the preregistered transition-entropy candidate for the u axis.

Pre-registration:
    reconstruction_real/preregistro/PREREGISTRO_EJE_U_TRANSICIONES_2026-10-17.md

The candidate remains a descriptive transition entropy unless it passes every
pre-registered gate independently in Domain B and crypto. The script has no
network calls and uses only the versioned inputs named in that protocol.

Outputs:
    reconstruction_real/data/eje_u_transiciones_por_caso.csv
    reconstruction_real/data/eje_u_transiciones_resumen.csv
    reconstruction_real/audits/RESULTADOS_EJE_U_TRANSICIONES_2026-10-17.md
    reconstruction_real/logs/eje_u_transiciones_2026-10-17.log

Run from the repository root:
    python reconstruction_real/code/eje_u_transiciones.py
"""

import csv
import gzip
import logging
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))
from snt import sha256 as sha256_file  # noqa: E402
MADDISON = ROOT / "data" / "maddison_mpd2020.csv"
B_PUBLISHED = (
    ROOT / "reconstruction_real" / "data" / "by_domain" / "dominio_B_real.csv"
)
CRYPTO = ROOT / "data" / "binance_cierres_diarios.csv.gz"
OUT_CASES = ROOT / "reconstruction_real" / "data" / "eje_u_transiciones_por_caso.csv"
OUT_SUMMARY = ROOT / "reconstruction_real" / "data" / "eje_u_transiciones_resumen.csv"
OUT_AUDIT = (
    ROOT
    / "reconstruction_real"
    / "audits"
    / "RESULTADOS_EJE_U_TRANSICIONES_2026-10-17.md"
)
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_FILE = LOG_DIR / "eje_u_transiciones_2026-10-17.log"

YEAR_MIN = 1900
YEAR_MAX = 2018
MIN_B_OBSERVATIONS = 40
MIN_CRYPTO_DAYS = 200
MIN_ALIGNED_POSITIONS = 12
MIN_DOMAIN_CASES = 30

INVARIANCE_MEDIAN_MIN = 0.60
INVARIANCE_CASE_MIN = 0.30
INVARIANCE_CASE_SHARE_MIN = 2.0 / 3.0
EVALUABLE_SHARE_MIN = 0.90
IQR_MIN = 0.05
COLLAPSE_CORRELATION_MIN = 0.90
COLLAPSE_CASE_SHARE_MAX = 0.75
B_REPRODUCTION_TOLERANCE = 1e-4

CASE_FIELDS = [
    "dominio",
    "id",
    "etiqueta",
    "n_observaciones",
    "origen_elegible",
    "motivo_origen",
    "b_delta_reproduccion",
    "theta1_estado",
    "theta2_estado",
    "n_theta1",
    "n_theta2",
    "n_alineadas",
    "elegible_compuertas",
    "motivo_exclusion",
    "spearman_theta1_theta2",
    "invarianza_evaluable",
    "invarianza_caso_pasa",
    "iqr_h_theta1",
    "rho_abs_h_m",
    "rho_abs_h_v",
    "no_colapso_evaluable",
    "caso_colapsa_m_o_v",
]
SUMMARY_FIELDS = [
    "dominio",
    "compuerta",
    "estado",
    "n_total",
    "n_elegibles",
    "n_evaluables",
    "n_cumplen",
    "valor",
    "umbral",
    "detalle",
]

log = logging.getLogger("EJE_U_TRANSICIONES")


@dataclass(frozen=True)
class ProjectionSpec:
    """A fully declared measurement frame for one transition projection."""

    name: str
    step: int
    quantiles: tuple[float, ...]
    state_count: int
    history_size: int


@dataclass
class Projection:
    """Values produced by one projection, or its explicit exclusion reason."""

    status: str
    reason: str | None
    rows: list[dict[str, float | int]]


THETA1 = ProjectionSpec(
    name="theta1",
    step=1,
    quantiles=(1.0 / 3.0, 2.0 / 3.0),
    state_count=3,
    history_size=12,
)
THETA2 = ProjectionSpec(
    name="theta2",
    step=2,
    quantiles=(0.2, 0.4, 0.6, 0.8),
    state_count=5,
    history_size=20,
)


def configure_log() -> None:
    """Configure run logging only when the analysis is executed."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def repository_revision() -> str:
    """Require a git revision so each result is tied to executable code."""
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def _require_columns(
    fieldnames: list[str] | None, expected: set[str], path: Path
) -> None:
    available = set(fieldnames or [])
    missing = expected - available
    if missing:
        raise ValueError(
            f"{path.relative_to(ROOT)} missing required columns: {sorted(missing)}"
        )


def _csv_rows(path: Path, expected: set[str]) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        _require_columns(reader.fieldnames, expected, path)
        return list(reader)


def _quantile(values: np.ndarray, q: float) -> float:
    return float(np.quantile(values, q, method="linear"))


def classify_states(
    values: np.ndarray, quantiles: tuple[float, ...], state_count: int
) -> tuple[np.ndarray | None, np.ndarray | None, str | None]:
    """Discretize values with the protocol's right-closed state intervals."""
    if values.size == 0 or not np.all(np.isfinite(values)):
        return None, None, "incrementos_no_finitos"

    cutpoints = np.array([_quantile(values, q) for q in quantiles], dtype=float)
    states = np.searchsorted(cutpoints, values, side="left").astype(int)
    if len(np.unique(states)) != state_count:
        return None, cutpoints, f"menos_de_{state_count}_estados_no_vacios"
    return states, cutpoints, None


def _entropy(counts: np.ndarray) -> float:
    probabilities = counts[counts > 0].astype(float) / float(counts.sum())
    return float(-np.sum(probabilities * np.log(probabilities)))


def transition_entropy_rows(
    states: np.ndarray,
    increments: np.ndarray,
    original_indices: np.ndarray,
    x: np.ndarray,
    state_count: int,
    history_size: int,
) -> list[dict[str, float | int]]:
    """Build entropy values using only historical transitions after state fixing."""
    rows: list[dict[str, float | int]] = []
    for position, state in enumerate(states):
        origins = np.flatnonzero(states[:position] == state)
        if origins.size < history_size:
            continue
        origins = origins[-history_size:]
        successors = states[origins + 1]
        counts = np.bincount(successors, minlength=state_count)
        entropy = _entropy(counts)
        history_increments = increments[origins]
        original_index = int(original_indices[position])
        rows.append(
            {
                "time_index": original_index,
                "h": entropy / np.log(state_count),
                "u_effective": float(np.exp(entropy)),
                "m": float(x[original_index]),
                "v": float(
                    np.median(
                        np.abs(history_increments - np.median(history_increments))
                    )
                ),
            }
        )
    return rows


def build_projection(x: np.ndarray, spec: ProjectionSpec) -> Projection:
    """Apply one pre-registered theta frame to an already valid log-ratio."""
    if x.size <= spec.step:
        return Projection("excluida", "observaciones_insuficientes", [])

    increments = x[spec.step:] - x[:-spec.step]
    states, _, reason = classify_states(
        increments, spec.quantiles, spec.state_count
    )
    if states is None:
        return Projection("excluida", reason, [])

    original_indices = np.arange(spec.step, x.size, dtype=int)
    rows = transition_entropy_rows(
        states,
        increments,
        original_indices,
        x,
        spec.state_count,
        spec.history_size,
    )
    if not rows:
        return Projection(
            "excluida",
            f"sin_{spec.history_size}_transiciones_historicas_del_mismo_estado",
            [],
        )
    return Projection("ok", None, rows)


def safe_spearman(first: np.ndarray, second: np.ndarray) -> float | None:
    """Return only a defined rank correlation; constants are not evaluable."""
    if first.size < 2 or second.size != first.size:
        return None
    if not np.all(np.isfinite(first)) or not np.all(np.isfinite(second)):
        return None
    if np.ptp(first) == 0 or np.ptp(second) == 0:
        return None
    statistic = float(stats.spearmanr(first, second).statistic)
    return statistic if np.isfinite(statistic) else None


def aligned_projection_values(
    theta1: Projection, theta2: Projection
) -> dict[str, np.ndarray] | None:
    """Align normalized entropies by original series position."""
    values1 = {int(row["time_index"]): row for row in theta1.rows}
    values2 = {int(row["time_index"]): row for row in theta2.rows}
    shared = sorted(set(values1) & set(values2))
    if len(shared) < MIN_ALIGNED_POSITIONS:
        return None
    return {
        "indices": np.array(shared, dtype=int),
        "h1": np.array([values1[index]["h"] for index in shared], dtype=float),
        "h2": np.array([values2[index]["h"] for index in shared], dtype=float),
        "m": np.array([values1[index]["m"] for index in shared], dtype=float),
        "v": np.array([values1[index]["v"] for index in shared], dtype=float),
    }


def _load_maddison() -> dict[str, dict[int, float]]:
    rows = _csv_rows(MADDISON, {"Entity", "Year", "GDP per capita"})
    series: dict[str, dict[int, float]] = defaultdict(dict)
    for row in rows:
        try:
            value = float(row["GDP per capita"])
            year = int(row["Year"])
        except (TypeError, ValueError):
            continue
        if value > 0:
            series[row["Entity"]][year] = value
    return series


def load_domain_b() -> list[dict[str, object]]:
    """Load published B pairs with the exact MPD2020 ratio construction."""
    series = _load_maddison()
    rows = _csv_rows(B_PUBLISHED, {"id", "hub", "nodo", "b"})
    cases: list[dict[str, object]] = []
    seen_ids: set[str] = set()

    for row in rows:
        case_id = row["id"]
        if case_id in seen_ids:
            raise ValueError(f"Duplicate Domain B identifier: {case_id}")
        seen_ids.add(case_id)

        hub = series.get(row["hub"], {})
        node = series.get(row["nodo"], {})
        years = sorted(
            year
            for year in hub
            if year in node and YEAR_MIN <= year <= YEAR_MAX
        )
        ratio = np.array([hub[year] / node[year] for year in years], dtype=float)
        case: dict[str, object] = {
            "dominio": "B",
            "id": case_id,
            "etiqueta": f"{row['hub']}->{row['nodo']}",
            "ratio": ratio,
            "source_ok": False,
            "source_reason": "",
            "b_delta": None,
        }
        if ratio.size < MIN_B_OBSERVATIONS:
            case["source_reason"] = "menos_de_40_anios_comunes"
        elif not np.all(np.isfinite(ratio)) or np.any(ratio <= 0):
            case["source_reason"] = "cociente_no_positivo_o_no_finito"
        else:
            x = np.log(ratio)
            slope = float(
                stats.linregress(
                    np.log(np.arange(1, ratio.size + 1, dtype=float)), x
                ).slope
            )
            b_delta = abs(slope - float(row["b"]))
            case["b_delta"] = b_delta
            if b_delta > B_REPRODUCTION_TOLERANCE:
                case["source_reason"] = "b_publicada_no_reproducida"
            else:
                case["source_ok"] = True
        cases.append(case)
    return cases


def load_crypto() -> list[dict[str, object]]:
    """Load all positive non-BTCUSDT close-ratio series with common dates."""
    if not CRYPTO.exists():
        raise FileNotFoundError(CRYPTO)
    closes: dict[str, dict[str, float]] = defaultdict(dict)
    with gzip.open(CRYPTO, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        _require_columns(reader.fieldnames, {"par", "fecha", "close"}, CRYPTO)
        for row in reader:
            try:
                value = float(row["close"])
            except (TypeError, ValueError):
                continue
            if value > 0:
                closes[row["par"]][row["fecha"]] = value

    hub = closes.get("BTCUSDT", {})
    if not hub:
        raise ValueError("BTCUSDT has no positive close values in the crypto source")

    cases: list[dict[str, object]] = []
    for pair, series in sorted(closes.items()):
        if pair == "BTCUSDT":
            continue
        dates = sorted(date for date in series if date in hub)
        ratio = np.array([series[date] / hub[date] for date in dates], dtype=float)
        source_ok = ratio.size >= MIN_CRYPTO_DAYS
        reason = "" if source_ok else "menos_de_200_dias_comunes_con_BTCUSDT"
        if source_ok and (
            not np.all(np.isfinite(ratio)) or np.any(ratio <= 0)
        ):
            source_ok = False
            reason = "cociente_no_positivo_o_no_finito"
        cases.append(
            {
                "dominio": "Cripto",
                "id": pair,
                "etiqueta": pair,
                "ratio": ratio,
                "source_ok": source_ok,
                "source_reason": reason,
                "b_delta": None,
            }
        )
    return cases


def _base_case_row(case: dict[str, object]) -> dict[str, object]:
    return {
        "dominio": case["dominio"],
        "id": case["id"],
        "etiqueta": case["etiqueta"],
        "n_observaciones": int(np.asarray(case["ratio"]).size),
        "origen_elegible": bool(case["source_ok"]),
        "motivo_origen": case["source_reason"],
        "b_delta_reproduccion": case["b_delta"],
        "theta1_estado": "",
        "theta2_estado": "",
        "n_theta1": 0,
        "n_theta2": 0,
        "n_alineadas": 0,
        "elegible_compuertas": False,
        "motivo_exclusion": "",
        "spearman_theta1_theta2": None,
        "invarianza_evaluable": False,
        "invarianza_caso_pasa": False,
        "iqr_h_theta1": None,
        "rho_abs_h_m": None,
        "rho_abs_h_v": None,
        "no_colapso_evaluable": False,
        "caso_colapsa_m_o_v": False,
    }


def analyze_case(case: dict[str, object]) -> dict[str, object]:
    """Analyze one source-eligible case without using b or other model labels."""
    row = _base_case_row(case)
    if not case["source_ok"]:
        row["motivo_exclusion"] = case["source_reason"]
        return row

    x = np.log(np.asarray(case["ratio"], dtype=float))
    theta1 = build_projection(x, THETA1)
    theta2 = build_projection(x, THETA2)
    row["theta1_estado"] = theta1.status if theta1.reason is None else theta1.reason
    row["theta2_estado"] = theta2.status if theta2.reason is None else theta2.reason
    row["n_theta1"] = len(theta1.rows)
    row["n_theta2"] = len(theta2.rows)

    if theta1.status != "ok" or theta2.status != "ok":
        row["motivo_exclusion"] = ";".join(
            reason
            for reason in (theta1.reason, theta2.reason)
            if reason is not None
        )
        return row

    aligned = aligned_projection_values(theta1, theta2)
    if aligned is None:
        row["motivo_exclusion"] = "menos_de_12_posiciones_alineadas"
        return row

    h1 = aligned["h1"]
    h2 = aligned["h2"]
    row["n_alineadas"] = int(h1.size)
    row["elegible_compuertas"] = True
    row["iqr_h_theta1"] = _quantile(h1, 0.75) - _quantile(h1, 0.25)

    invariance = safe_spearman(h1, h2)
    row["spearman_theta1_theta2"] = invariance
    if invariance is not None:
        row["invarianza_evaluable"] = True
        row["invarianza_caso_pasa"] = invariance >= INVARIANCE_CASE_MIN

    rho_m = safe_spearman(h1, aligned["m"])
    rho_v = safe_spearman(h1, aligned["v"])
    if rho_m is not None and rho_v is not None:
        row["rho_abs_h_m"] = abs(rho_m)
        row["rho_abs_h_v"] = abs(rho_v)
        row["no_colapso_evaluable"] = True
        row["caso_colapsa_m_o_v"] = (
            abs(rho_m) >= COLLAPSE_CORRELATION_MIN
            or abs(rho_v) >= COLLAPSE_CORRELATION_MIN
        )
    return row


def _summary_row(
    domain: str,
    gate: str,
    status: str,
    total: int,
    eligible: int,
    evaluable: int | str,
    passing: int | str,
    value: float | int | str,
    threshold: str,
    detail: str,
) -> dict[str, object]:
    return {
        "dominio": domain,
        "compuerta": gate,
        "estado": status,
        "n_total": total,
        "n_elegibles": eligible,
        "n_evaluables": evaluable,
        "n_cumplen": passing,
        "valor": value,
        "umbral": threshold,
        "detalle": detail,
    }


def _format_number(value: float | int | str | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float):
        return f"{value:.12g}"
    return str(value)


def summarize_domain(
    domain: str, rows: list[dict[str, object]]
) -> tuple[list[dict[str, object]], str]:
    """Apply the pre-registered gates to one domain and never pool domains."""
    eligible_rows = [row for row in rows if row["elegible_compuertas"]]
    total = len(rows)
    eligible = len(eligible_rows)
    summary: list[dict[str, object]] = []

    if eligible < MIN_DOMAIN_CASES:
        summary.append(
            _summary_row(
                domain,
                "A_cobertura",
                "SIN_COBERTURA",
                total,
                eligible,
                "",
                "",
                eligible,
                f">={MIN_DOMAIN_CASES}",
                "El protocolo no interpreta cobertura insuficiente como negativo.",
            )
        )
        for gate in ("B_invarianza", "C_variacion", "D_no_colapso"):
            summary.append(
                _summary_row(
                    domain,
                    gate,
                    "NO_EVALUABLE",
                    total,
                    eligible,
                    "",
                    "",
                    "",
                    "",
                    "No se evalua antes de pasar la compuerta de cobertura.",
                )
            )
        return summary, "SIN_COBERTURA"

    summary.append(
        _summary_row(
            domain,
            "A_cobertura",
            "PASA",
            total,
            eligible,
            eligible,
            eligible,
            eligible,
            f">={MIN_DOMAIN_CASES}",
            "Casos con ambas proyecciones y al menos 12 posiciones alineadas.",
        )
    )

    inv_rows = [row for row in eligible_rows if row["invarianza_evaluable"]]
    inv_values = [
        float(row["spearman_theta1_theta2"])
        for row in inv_rows
        if row["spearman_theta1_theta2"] is not None
    ]
    inv_passes = sum(
        value >= INVARIANCE_CASE_MIN for value in inv_values
    )
    inv_share = len(inv_rows) / eligible
    inv_median = float(np.median(inv_values)) if inv_values else None
    inv_case_share = inv_passes / len(inv_values) if inv_values else 0.0
    inv_status = (
        "PASA"
        if inv_share >= EVALUABLE_SHARE_MIN
        and inv_median is not None
        and inv_median >= INVARIANCE_MEDIAN_MIN
        and inv_case_share >= INVARIANCE_CASE_SHARE_MIN
        else "FALLA"
    )
    summary.append(
        _summary_row(
            domain,
            "B_invarianza",
            inv_status,
            total,
            eligible,
            len(inv_rows),
            inv_passes,
            inv_median if inv_median is not None else "",
            (
                f"evaluables>={EVALUABLE_SHARE_MIN:.0%}; "
                f"mediana>={INVARIANCE_MEDIAN_MIN:.2f}; "
                f"casos>={INVARIANCE_CASE_SHARE_MIN:.0%} con "
                f"rho>={INVARIANCE_CASE_MIN:.2f}"
            ),
            (
                f"fraccion_evaluable={inv_share:.3f}; "
                f"fraccion_casos={inv_case_share:.3f}"
            ),
        )
    )

    iqr_values = [
        float(row["iqr_h_theta1"])
        for row in eligible_rows
        if row["iqr_h_theta1"] is not None
    ]
    iqr_median = float(np.median(iqr_values)) if iqr_values else None
    variation_status = (
        "PASA"
        if len(iqr_values) == eligible
        and iqr_median is not None
        and iqr_median >= IQR_MIN
        else "FALLA"
    )
    summary.append(
        _summary_row(
            domain,
            "C_variacion",
            variation_status,
            total,
            eligible,
            len(iqr_values),
            sum(value >= IQR_MIN for value in iqr_values),
            iqr_median if iqr_median is not None else "",
            f"mediana_IQR>={IQR_MIN:.2f}",
            "IQR de h_t bajo theta1.",
        )
    )

    collapse_rows = [row for row in eligible_rows if row["no_colapso_evaluable"]]
    collapse_count = sum(
        bool(row["caso_colapsa_m_o_v"]) for row in collapse_rows
    )
    collapse_share = collapse_count / len(collapse_rows) if collapse_rows else 0.0
    collapse_evaluable_share = len(collapse_rows) / eligible
    no_collapse_status = (
        "PASA"
        if collapse_evaluable_share >= EVALUABLE_SHARE_MIN
        and collapse_share < COLLAPSE_CASE_SHARE_MAX
        else "FALLA"
    )
    summary.append(
        _summary_row(
            domain,
            "D_no_colapso",
            no_collapse_status,
            total,
            eligible,
            len(collapse_rows),
            eligible - collapse_count,
            collapse_share,
            (
                f"evaluables>={EVALUABLE_SHARE_MIN:.0%}; "
                f"casos_colapsados<{COLLAPSE_CASE_SHARE_MAX:.0%} "
                f"con |rho|>={COLLAPSE_CORRELATION_MIN:.2f}"
            ),
            (
                f"fraccion_evaluable={collapse_evaluable_share:.3f}; "
                f"casos_colapsados={collapse_count}"
            ),
        )
    )

    statuses = {row["compuerta"]: row["estado"] for row in summary}
    decision = (
        "PASA_TODAS"
        if all(
            statuses[gate] == "PASA"
            for gate in (
                "A_cobertura",
                "B_invarianza",
                "C_variacion",
                "D_no_colapso",
            )
        )
        else "NO_ADMITIDO"
    )
    return summary, decision


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    """Write a reproducible UTF-8 CSV with explicit missing cells."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fieldnames, lineterminator="\n"
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {field: _format_number(row.get(field)) for field in fieldnames}
            )


def _gate_map(
    summary_rows: list[dict[str, object]], domain: str
) -> dict[str, dict[str, object]]:
    return {
        str(row["compuerta"]): row
        for row in summary_rows
        if row["dominio"] == domain
    }


def overall_decision(decisions: dict[str, str]) -> str:
    """Return only the preregistered interpretation of the two domain results."""
    if all(decisions[domain] == "PASA_TODAS" for domain in ("B", "Cripto")):
        return (
            "`u^H` queda admitido como definicion operativa candidata de `u` "
            "en dos dominios; su entrada en `C` requiere la revision posterior."
        )
    if any(decision == "PASA_TODAS" for decision in decisions.values()):
        return (
            "`u^H` queda solo como descriptor del dominio que paso; `u` no "
            "entra a `C` porque falta el segundo dominio."
        )
    if any(decision == "SIN_COBERTURA" for decision in decisions.values()):
        return (
            "El eje `u` sigue sin definicion operativa: al menos un dominio no "
            "alcanzo cobertura suficiente."
        )
    return (
        "El eje `u` sigue sin definicion operativa: el candidato no supero todas "
        "las compuertas en ambos dominios."
    )


def write_audit(
    revision: str,
    input_hashes: dict[Path, str],
    output_hashes: dict[Path, str],
    summary_rows: list[dict[str, object]],
    decisions: dict[str, str],
) -> None:
    """Produce the pre-registered audit without a cross-domain aggregate."""
    lines = [
        "# Resultados — eje `u` por entropia condicional de transiciones",
        "",
        "**Pre-registro:** "
        "`reconstruction_real/preregistro/PREREGISTRO_EJE_U_TRANSICIONES_2026-10-17.md`",
        f"**Revision ejecutada:** `{revision}`",
        "",
        "Esta corrida evalua `u^H` por dominio. No promedia ni ordena B y cripto, "
        "no usa `b`, `Delta` ni friccion como descriptor, y no hace una afirmacion "
        "causal o predictiva.",
        "",
        "## Procedencia",
        "",
        "| Archivo | SHA-256 |",
        "|---|---|",
    ]
    for path, digest in input_hashes.items():
        lines.append(f"| `{path.relative_to(ROOT)}` | `{digest}` |")
    for path, digest in output_hashes.items():
        lines.append(f"| `{path.relative_to(ROOT)}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## Compuertas por dominio",
            "",
            "| Dominio | Compuerta | Estado | Valor | Umbral | Detalle |",
            "|---|---|---|---:|---|---|",
        ]
    )
    for domain in ("B", "Cripto"):
        for gate in (
            "A_cobertura",
            "B_invarianza",
            "C_variacion",
            "D_no_colapso",
        ):
            row = _gate_map(summary_rows, domain)[gate]
            lines.append(
                "| {domain} | {gate} | **{status}** | {value} | {threshold} | "
                "{detail} |".format(
                    domain=domain,
                    gate=gate,
                    status=row["estado"],
                    value=_format_number(row["valor"]) or "—",
                    threshold=row["umbral"] or "—",
                    detail=row["detalle"],
                )
            )

    lines.extend(
        [
            "",
            "## Decision pre-especificada",
            "",
            f"- **B:** `{decisions['B']}`",
            f"- **Cripto:** `{decisions['Cripto']}`",
            f"- **Resultado:** {overall_decision(decisions)}",
            "",
            "## Desviaciones",
            "",
            "Ninguna. Se ejecutaron las fuentes, proyecciones, umbrales y "
            "desenlaces fijados en el pre-registro.",
            "",
        ]
    )
    OUT_AUDIT.parent.mkdir(parents=True, exist_ok=True)
    OUT_AUDIT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    configure_log()
    revision = repository_revision()
    input_paths = (MADDISON, B_PUBLISHED, CRYPTO)
    input_hashes = {path: sha256_file(path) for path in input_paths}
    log.info("Eje u por entropia condicional de transiciones")
    log.info("Revision: %s", revision)
    for path, digest in input_hashes.items():
        log.info("Entrada %s | SHA-256 %s", path.relative_to(ROOT), digest)

    cases = load_domain_b() + load_crypto()
    case_rows = [analyze_case(case) for case in cases]
    domains = {
        domain: [row for row in case_rows if row["dominio"] == domain]
        for domain in ("B", "Cripto")
    }

    summary_rows: list[dict[str, object]] = []
    decisions: dict[str, str] = {}
    for domain in ("B", "Cripto"):
        domain_summary, decision = summarize_domain(domain, domains[domain])
        summary_rows.extend(domain_summary)
        decisions[domain] = decision
        log.info(
            "%s: %s (%d/%d casos elegibles)",
            domain,
            decision,
            sum(bool(row["elegible_compuertas"]) for row in domains[domain]),
            len(domains[domain]),
        )

    write_csv(OUT_CASES, CASE_FIELDS, case_rows)
    write_csv(OUT_SUMMARY, SUMMARY_FIELDS, summary_rows)
    output_hashes = {
        OUT_CASES: sha256_file(OUT_CASES),
        OUT_SUMMARY: sha256_file(OUT_SUMMARY),
    }
    write_audit(revision, input_hashes, output_hashes, summary_rows, decisions)
    output_hashes[OUT_AUDIT] = sha256_file(OUT_AUDIT)
    for path, digest in output_hashes.items():
        log.info("Salida %s | SHA-256 %s", path.relative_to(ROOT), digest)
    log.info("Decision: %s", overall_decision(decisions))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
