"""Shared utility API for SNT; repository-wide consolidation is still in progress."""
import hashlib
import logging
import sys
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
    """Logger configurado con archivo + consola (versión reutilizable y sin duplicados)."""
    logger = logging.getLogger(nombre)
    logger.setLevel(level)
    logger.propagate = False

    fmt = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")

    # El logger se puede reusar con distinta ruta de salida o con varios scripts en
    # el mismo proceso. En ese caso hay que reconfigurarlo de forma idempotente.
    for handler in list(logger.handlers):
        if isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler):
            logger.removeHandler(handler)
        elif isinstance(handler, logging.FileHandler):
            if log_dir is None:
                logger.removeHandler(handler)
                continue
            target = (Path(log_dir) / (log_file or f"{nombre}.log")).resolve()
            if Path(handler.baseFilename).resolve() != target:
                logger.removeHandler(handler)

    if not any(
        isinstance(handler, logging.StreamHandler)
        and not isinstance(handler, logging.FileHandler)
        for handler in logger.handlers
    ):
        stream = logging.StreamHandler()
        stream.setFormatter(fmt)
        logger.addHandler(stream)

    if log_dir is not None:
        Path(log_dir).mkdir(parents=True, exist_ok=True)
        target = (Path(log_dir) / (log_file or f"{nombre}.log")).resolve()
        if not any(
            isinstance(handler, logging.FileHandler)
            and Path(handler.baseFilename).resolve() == target
            for handler in logger.handlers
        ):
            file_handler = logging.FileHandler(target, mode="w", encoding="utf-8")
            file_handler.setFormatter(fmt)
            logger.addHandler(file_handler)

    return logger


def configurar_logging(ruta, level=logging.INFO):
    """Configure the root logger with the repository's file-and-console format."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        handlers=[
            logging.FileHandler(ruta, mode="w", encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    return logging.getLogger()


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
