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

### Importante — estimabilidad primero, luego un rango entre los estimables

Dos rondas de revisión cruzada (2026-07-25) fijaron el marco correcto. No se
reporta un conteo sobre 446 —eso trata a los casos no estimables como
"testeados y no significativos"—, sino tres cifras:

| Paso | Cifra |
|---|---:|
| Estimables (`n_eff ≥ 3`) | **156 / 446 (35.0%)** |
| **No estimables** (`n_eff < 3`) | **290 / 446 (65.0%)** |
| Sig. entre estimables — cota inf. (SE inflado + gl) | **33 (21.2%)** |
| Sig. entre estimables — cota sup. (solo gl, `df>0`) | 112 (71.8%) |
| Valor puntual | pendiente Newey-West/GLS |

La partición **290/446 no estimables** es el hallazgo más limpio: sale directo de
`n_eff < 3`, sin convenciones ni aproximación de Bartlett. La cota inferior 33 es
la corrección coherente (**inflar el SE** `√((1+ρ)/(1−ρ))`, mediana 5.9×, *además*
de recortar gl) y es invariante a la convención de gl. El valor puntual necesita
**Newey-West/GLS** sobre residuos crudos, ausentes del repo (`owid-maddison.csv`).
`corregir_corpus()` emite la partición y ambas cotas con un warning;
`tests/test_correccion_ar1.py` fija 156/290/33/112 — **no** 145, que dependía de
una guarda de implementación. La dirección —una caída fuerte desde 374— no está
en duda.
