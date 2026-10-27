"""Regression tests for the public SNT log-log fitting API."""

import numpy as np
import pytest

import snt


def test_loglog_entry_points_share_canonical_result():
    t = np.array([1.0, 2.0, 3.0, np.nan, 0.0])
    y = np.array([3.0, 12.0, 27.0, 9.0, 1.0])

    fit_power = snt.fit_power_law(t, y)
    fit_spanish = snt.ajuste_loglog(t, y)

    assert len(fit_power) == len(fit_spanish) == 3
    assert fit_power[0] == pytest.approx(2.0)
    assert fit_power[1] == pytest.approx(np.log(3.0))
    np.testing.assert_allclose(fit_power[2], np.zeros(3), atol=1e-12)
    assert fit_spanish[0] == pytest.approx(fit_power[0])
    assert fit_spanish[1] == pytest.approx(fit_power[1])
    np.testing.assert_allclose(fit_spanish[2], fit_power[2])


def test_loglog_fit_requires_three_valid_observations():
    for fit in (snt.fit_power_law, snt.ajuste_loglog):
        slope, log_a, residuals = fit([1, 2, np.nan], [2, 4, 8])
        assert np.isnan(slope)
        assert np.isnan(log_a)
        assert residuals is None


def test_sha256_reads_pathlike_files(tmp_path):
    path = tmp_path / "source.bin"
    path.write_bytes(b"SNT utility test")

    assert snt.sha256(path) == (
        "a86f9dae328df3d7315f244d655a683d6f8c985a3330b4ba1c4d1f11d43fe192")


def test_configurar_logging_uses_shared_file_and_console_format(
        tmp_path, monkeypatch):
    import logging

    captured = {}

    def fake_basic_config(**kwargs):
        captured.update(kwargs)

    monkeypatch.setattr(logging, "basicConfig", fake_basic_config)
    log_path = tmp_path / "run.log"
    logger = snt.configurar_logging(log_path)

    assert logger is logging.getLogger()
    assert captured["level"] == logging.INFO
    assert len(captured["handlers"]) == 2
    assert isinstance(captured["handlers"][0], logging.FileHandler)
    assert captured["handlers"][0].baseFilename == str(log_path)
    assert isinstance(captured["handlers"][1], logging.StreamHandler)
    captured["handlers"][0].close()
