"""Shared utility API for SNT; repository-wide consolidation is still in progress."""
import hashlib
import logging
from pathlib import Path


def sha256(path):
    """SHA-256 de un archivo (versión unificada de las 11 copias)."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def configurar_log(nombre="snt", log_dir=None, log_file=None,
                   level=logging.INFO):
    """Logger configurado con archivo + consola (versión de las 6 copias)."""
    logger = logging.getLogger(nombre)
    logger.setLevel(level)
    if logger.handlers:
        return logger
    fmt = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
    sh = logging.StreamHandler()
    sh.setFormatter(fmt)
    logger.addHandler(sh)
    if log_dir:
        Path(log_dir).mkdir(parents=True, exist_ok=True)
        ruta = Path(log_dir) / (log_file or f"{nombre}.log")
        fh = logging.FileHandler(ruta, mode="w", encoding="utf-8")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger


def _ajuste_loglog(t, y):
    """Canonical OLS log-log fit: slope, log-intercept, and residuals."""
    import numpy as np

    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)
    mask = (t > 0) & (y > 0) & np.isfinite(t) & np.isfinite(y)
    t, y = t[mask], y[mask]
    if len(t) < 3:
        return float("nan"), float("nan"), None
    lt, ly = np.log(t), np.log(y)
    b, log_a = np.polyfit(lt, ly, 1)
    return float(b), float(log_a), ly - (log_a + b * lt)


def fit_power_law(t, r):
    """Fit ``r = a*t**b``; return ``(b, log(a), residuals)``.

    At least three finite, positive observations are required. Residuals are
    in log space and correspond to the retained observations.
    """
    return _ajuste_loglog(t, r)


def ajuste_loglog(t, y):
    """Spanish alias for the canonical ``(b, log(a), residuals)`` fit."""
    return _ajuste_loglog(t, y)
