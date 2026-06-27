"""
Shadow Node Theory — Shared utilities
Fractal Core Research | Tlaxcala, Mexico | 2026
"""

import numpy as np
from scipy.stats import pearsonr


def ajustar_ley_potencia(años, sombra, dominante, trigger_año):
    """
    Compute R(t) = dominante/sombra and fit f(t) = a * t^b via log-log OLS.
    Returns (result_dict, tiempos_array, ratios_array).
    """
    result = {
        "a": None, "b": None, "r2": None,
        "r_pearson": None, "p_value": None,
        "clasificacion": "", "n": 0
    }

    tiempos, ratios = [], []
    for i, año in enumerate(años):
        if sombra[i] > 0 and dominante[i] > 0:
            t = abs(año - trigger_año) + 1e-6
            tiempos.append(t)
            ratios.append(dominante[i] / sombra[i])

    result["n"] = len(tiempos)
    if len(tiempos) < 3:
        result["clasificacion"] = "Datos insuficientes"
        return result, np.array(tiempos), np.array(ratios)

    try:
        t = np.array(tiempos, dtype=float)
        r = np.array(ratios, dtype=float)
        log_t = np.log(t)
        log_r = np.log(r)
        coef = np.polyfit(log_t, log_r, 1)
        b = coef[0]
        a = np.exp(coef[1])

        r_pred = a * t**b
        ss_res = np.sum((r - r_pred)**2)
        ss_tot = np.sum((r - r.mean())**2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
        rp, pv = pearsonr(log_t, log_r)

        if b > 2.0:
            clf = "Satelizacion extrema (b>2)"
        elif b > 1.0:
            clf = "Satelizacion rapida sin friccion"
        elif b > 0.3:
            clf = "Satelizacion activa"
        elif b > 0.05:
            clf = "Satelizacion gradual"
        elif b > -0.1:
            clf = "Estado estacionario / equilibrio"
        else:
            clf = "Convergencia / leapfrog"

        result.update({
            "a": round(a, 6), "b": round(b, 4),
            "r2": round(r2, 4), "r_pearson": round(rp, 4),
            "p_value": round(pv, 6), "clasificacion": clf
        })
    except Exception as e:
        result["clasificacion"] = f"Error: {e}"

    return result, np.array(tiempos), np.array(ratios)
