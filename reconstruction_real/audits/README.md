# Auditorías del corpus SNT

Registro de auditorías estadísticas del corpus reconstruido. Cada auditoría
recorre las cifras publicadas y las vuelve a calcular desde los datos
committeados.

## v32 — auditoría integral (2026-07)

- **Informe:** [`AUDITORIA_INTEGRAL_v32.md`](AUDITORIA_INTEGRAL_v32.md) — 33
  cifras recorridas; 14 replican exacto, 19 cambian o no son verificables.
- **Machinery:** [`code/snt_utils_v32.py`](../../code/snt_utils_v32.py) —
  extiende `code/snt_utils.py` de forma retrocompatible (DW para todos los
  ajustes, `rho_ar1`/`n_eff`/`p_ar1` Newey-West, `r2_log`+`r2_raw`, `p_exacto`,
  `comparar_modelos`, `ajustar_mle_clauset`, `spearman_cluster`,
  `corregir_corpus`, `fdr_bh`, `plegado_trigger`).
- **Runner:** [`code/snt_auditoria_integral_v32.py`](../code/snt_auditoria_integral_v32.py)
  — un solo `run`, salida a CSV. Reproduce lo reproducible desde los CSV del
  repo; marca `NO_REPRODUCIBLE` / `BLOQUEADO` lo que necesita datos ausentes.
- **Salida:** `reconstruction_real/data/auditoria_integral_v32_resultados.csv`
  (regenerable).
- **Corrección aplicada:** `reconstruction_real/data/dominio_B_corregido_ar1_v32.csv`
  — dominio B con `rho_ar1`, `n_eff`, `p_ar1`, `sig_ar1` por caso.

### Cómo regenerar

```sh
python reconstruction_real/code/snt_auditoria_integral_v32.py
```

### Los cuatro hallazgos que cambian algo

1. **Autocorrelación serial (dominio B, 62% del corpus).** DW mediana 0.112,
   99.8% con DW<1, ρ AR(1) ≈ 0.944, **n efectivo mediano ≈ 2.2** (no 69). La
   significancia por caso está inflada. Replica exacto desde
   `by_domain/dominio_B_real.csv`.
2. **Régimen superlineal b≥1 puede ser artefacto de modelo.** Por AIC sobre las
   18 series ACO: potencia gana 13/18, exponencial 4/18 (b̄ +1.54), lineal 1/18.
   A mayor b, peor ajusta la ley de potencia.
3. **Dirección aguanta, p no.** El p por caso está doblemente inflado
   (autocorrelación + pseudo-replicación de 714 casos no independientes).
4. **Defectos de reporte.** 557/721 p-values truncados a `0.0` por
   `round(p,6)`; dos definiciones de R² promediadas juntas; `trigger`
   hardcodeado a `'gradual'` en `expand_dominio_B.py`.

### Importante — la corrección es un RANGO acotado, no un punto

Revisión cruzada (2026-07-25): la cifra puntual original de 145/446 era una
**media corrección incoherente** (recortaba gl pero dejaba `t` intacto). La
corrección coherente **infla el error estándar además de recortar gl** (factor
`√((1+ρ)/(1−ρ))`, mediana 5.9×). Resultado:

| Cota | Método | B sig. | pct_sig corpus |
|---|---|---:|---:|
| **Inferior** | SE inflado + gl recortado | **33 (7.4%)** | **42.0%** |
| Superior | solo gl recortado | 145 (32.5%) | 57.6% |

El valor puntual verdadero vive **dentro de [33, 145]** y solo se fija con
**Newey-West** o **GLS con estructura AR(1)** (ambos en `snt_utils_v32.py`) sobre
los residuos crudos —ausentes del repo (`data/owid-maddison.csv`)—. `n_eff` y el
factor de inflación son la aproximación de Bartlett, derivada para la media de un
AR(1), no para una pendiente: **acotan, no cierran**. `corregir_corpus()` emite
ambas cotas con un warning; `tests/test_correccion_ar1.py` las fija (33 y 145).
La dirección —una caída fuerte desde 374— no está en duda.
