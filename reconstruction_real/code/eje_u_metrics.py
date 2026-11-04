"""Pure metric helpers for the preregistered operational-u analysis."""

import math

import numpy as np
from scipy.spatial.distance import pdist


def permutation_entropy_window(series, m=3):
    if len(series) < m:
        return np.nan
    patterns = [
        tuple(np.argsort(series[i:i + m]))
        for i in range(len(series) - m + 1)
    ]
    if not patterns:
        return np.nan
    _, counts = np.unique(patterns, axis=0, return_counts=True)
    probabilities = counts / counts.sum()
    entropy = -np.sum(probabilities * np.log(probabilities))
    return float(entropy / np.log(math.factorial(m)))


def permutation_entropy_series(series, m=3, window=20):
    values = np.asarray(series, dtype=float)
    out = np.full(values.size, np.nan)
    for i in range(window - 1, values.size):
        out[i] = permutation_entropy_window(
            values[i - window + 1:i + 1], m=m
        )
    return out


def effective_pattern_count(entropy, m):
    return np.exp(np.asarray(entropy, dtype=float) * np.log(math.factorial(m)))


def correlation_radii(window):
    sigma = float(np.std(window))
    if not np.isfinite(sigma) or sigma <= 0:
        return np.array([], dtype=float)
    return sigma * np.linspace(0.05, 0.3, 11)


def estimate_correlation_dimension(distances, radii):
    distances = np.asarray(distances, dtype=float)
    radii = np.asarray(radii, dtype=float)
    if distances.size == 0:
        return np.nan
    correlation_sums = np.array(
        [np.mean(distances < radius) for radius in radii], dtype=float
    )
    valid = (
        np.isfinite(radii)
        & (radii > 0)
        & np.isfinite(correlation_sums)
        & (correlation_sums > 0)
    )
    if valid.sum() < 3:
        return np.nan
    log_r = np.log(radii[valid])
    log_c = np.log(correlation_sums[valid])
    if np.unique(log_r).size < 3 or np.unique(log_c).size < 2:
        return np.nan
    slope, _ = np.polyfit(log_r, log_c, 1)
    return float(slope)


def correlation_dimension_pair(window, embeddings=(2, 3), tau=1,
                               sample_n=400):
    values = np.asarray(window, dtype=float)
    radii = correlation_radii(values)
    result = {embedding: np.nan for embedding in embeddings}
    if radii.size == 0 or not np.isfinite(values).all():
        return result

    centered = values - np.mean(values)
    for embedding in embeddings:
        n_vectors = len(centered) - (embedding - 1) * tau
        if n_vectors < 10:
            continue
        vectors = np.array([
            centered[i:i + embedding * tau:tau]
            for i in range(n_vectors)
        ])
        indices = np.linspace(
            0, n_vectors - 1, min(sample_n, n_vectors), dtype=int
        )
        distances = pdist(vectors[indices], metric="euclidean")
        result[embedding] = estimate_correlation_dimension(distances, radii)
    return result


def correlation_dimension_pair_series(series, window=200, embeddings=(2, 3),
                                      tau=1):
    values = np.asarray(series, dtype=float)
    out = {embedding: np.full(values.size, np.nan) for embedding in embeddings}
    for i in range(window - 1, values.size):
        estimates = correlation_dimension_pair(
            values[i - window + 1:i + 1],
            embeddings=embeddings,
            tau=tau,
        )
        for embedding in embeddings:
            out[embedding][i] = estimates[embedding]
    return out
