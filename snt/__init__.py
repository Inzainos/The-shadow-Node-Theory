"""Shadow Node Theory utilities package.

The package API is being adopted incrementally; repository-wide utility
consolidation is not yet complete.
"""
from snt.utils import (
    ajuste_loglog,
    configurar_log,
    configurar_logging,
    fit_power_law,
    sha256,
)

__all__ = [
    "sha256", "configurar_log", "configurar_logging",
    "fit_power_law", "ajuste_loglog",
]
