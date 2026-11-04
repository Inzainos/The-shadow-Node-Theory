"""Regression tests for the preregistered operational-u metrics."""

import os
import sys
from unittest.mock import patch

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "reconstruction_real", "code"))

from eje_u_metrics import (  # noqa: E402
    correlation_dimension_pair,
    correlation_radii,
    effective_pattern_count,
    estimate_correlation_dimension,
)


def test_permutation_entropy_is_reported_as_effective_pattern_count():
    assert np.allclose(
        effective_pattern_count(np.array([0.0, 1.0]), m=3),
        [1.0, 6.0],
    )
    assert np.allclose(
        effective_pattern_count(np.array([0.0, 1.0]), m=4),
        [1.0, 24.0],
    )


def test_correlation_dimension_is_regressed_over_registered_radius_range():
    radii = np.linspace(0.05, 0.3, 11)
    distances = np.sqrt(np.linspace(0, 0.3 ** 2, 100_000, endpoint=False))

    estimate = estimate_correlation_dimension(distances, radii)

    assert abs(estimate - 2.0) < 0.01


def test_embedding_dimensions_share_window_standard_deviation_radii():
    window = np.sin(np.linspace(0, 8 * np.pi, 200))
    captured_radii = []

    def capture_estimator(distances, radii):
        captured_radii.append(radii.copy())
        return 1.0

    with patch(
        "eje_u_metrics.estimate_correlation_dimension",
        side_effect=capture_estimator,
    ):
        estimates = correlation_dimension_pair(window)

    assert set(estimates) == {2, 3}
    assert len(captured_radii) == 2
    assert np.array_equal(captured_radii[0], captured_radii[1])
    assert np.allclose(
        captured_radii[0],
        np.std(window) * np.linspace(0.05, 0.3, 11),
    )
    assert np.allclose(correlation_radii(window), captured_radii[0])


def test_constant_window_has_no_correlation_dimension():
    assert correlation_dimension_pair(np.ones(200)) == {2: np.nan, 3: np.nan}
