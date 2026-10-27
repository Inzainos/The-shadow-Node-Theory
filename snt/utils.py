"""Utilities consolidadas del ecosistema SNT (pendiente 3.1).

Fuente de consolidación:
  - sha256: duplicada ×11 en scripts
  - configurar_log: duplicada ×6
  - fit_power_law / ajustar_ley_potencia: ×3 (snt_utils, snt_utils_v32, scripts)
  - ajuste_loglog: ×2 (rc1_superlineal, nulos_ar1_aco)
"""
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


def fit_power_law(t, r):
    """OLS log-log: b, log_a, residuos. (Versión unificada de las ×3.)"""
    import numpy as np
    t = np.asarray(t, dtype=float)
    r = np.asarray(r, dtype=float)
    mask = (t > 0) & (r > 0) & np.isfinite(t) & np.isfinite(r)
    t, r = t[mask], r[mask]
    if len(t) < 4:
        return float("nan"), float("nan"), None
    lt, lr = np.log(t), np.log(r)
    b, a = np.polyfit(lt, lr, 1)
    return float(b), float(a), lr - (a + b * lt)


def ajuste_loglog(t, y):
    """b y log_a por OLS log-log. (Versión unificada de las ×2.)"""
    import numpy as np
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)
    ok = (t > 0) & (y > 0)
    t, y = t[ok], y[ok]
    if len(t) < 3:
        return float("nan"), float("nan")
    b, a = np.polyfit(np.log(t), np.log(y), 1)
    return float(b), float(a)
