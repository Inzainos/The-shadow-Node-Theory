"""Shadow Node Theory — core package.

Consolidates the duplicated utilities that lived in
code/snt_utils.py, code/snt_utils_v32.py and inline in scripts:
sha256, configurar_log, fit_power_law, ajuste_loglog, etc.
"""
from snt.utils import sha256, configurar_log, fit_power_law, ajuste_loglog

__all__ = ["sha256", "configurar_log", "fit_power_law", "ajuste_loglog"]
