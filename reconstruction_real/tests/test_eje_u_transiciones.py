"""Unit tests for the preregistered transition-entropy construction."""

import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "reconstruction_real", "code"))

from eje_u_transiciones import (  # noqa: E402
    classify_states,
    safe_spearman,
    transition_entropy_rows,
    write_csv,
)


def test_state_intervals_are_closed_on_the_right():
    values = np.arange(9, dtype=float)
    states, cuts, reason = classify_states(values, (1 / 3, 2 / 3), 3)

    assert reason is None
    assert cuts.tolist() == [8 / 3, 16 / 3]
    assert states.tolist() == [0, 0, 0, 1, 1, 1, 2, 2, 2]


def test_tied_quantiles_do_not_invent_empty_states():
    states, _, reason = classify_states(
        np.ones(12, dtype=float), (1 / 3, 2 / 3), 3
    )

    assert states is None
    assert reason == "menos_de_3_estados_no_vacios"


def test_transition_entropy_uses_only_prior_origin_states():
    states = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0], dtype=int)
    increments = np.arange(states.size, dtype=float)
    indices = np.arange(states.size, dtype=int)
    x = np.arange(states.size, dtype=float)

    initial = transition_entropy_rows(states, increments, indices, x, 2, 2)
    altered = states.copy()
    altered[-1] = 1
    changed_future = transition_entropy_rows(
        altered, increments, indices, x, 2, 2
    )

    initial_by_time = {row["time_index"]: row for row in initial}
    changed_by_time = {row["time_index"]: row for row in changed_future}
    for time_index in (4, 5, 6, 7):
        assert initial_by_time[time_index]["h"] == changed_by_time[time_index]["h"]
        assert (
            initial_by_time[time_index]["u_effective"]
            == changed_by_time[time_index]["u_effective"]
        )


def test_constant_vectors_are_not_spearman_evaluable():
    assert safe_spearman(np.ones(4), np.arange(4, dtype=float)) is None


def test_result_csvs_use_lf_line_endings(tmp_path):
    output = tmp_path / "result.csv"
    write_csv(output, ["valor"], [{"valor": 1.0}])

    assert b"\r\n" not in output.read_bytes()
