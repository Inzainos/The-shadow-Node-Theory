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

### Prueba discriminante del dominio B (2026-07-25)

- **Informe:** [`DISCRIMINANTE_DOMINIO_B.md`](DISCRIMINANTE_DOMINIO_B.md).
- **Script:** [`code/prueba_discriminante_dominio_B.py`](../code/prueba_discriminante_dominio_B.py).
- **Pregunta:** ¿el exponente `b` del dominio B mide acoplamiento hub-satélite
  (SNT) o β-convergencia de PIB per cápita? Si gana convergencia, el 62% del
  corpus no es evidencia de SNT.
- **Bloque 0 (corre ya, firme):** el rol de "hub" es una propiedad del PAR, no
  del país — **85% de los hubs también aparecen como satélites** (Italia: hub en
  3 pares, satélite en 12). Sale de contar filas, sin supuestos.
- **Bloque 1 (corrido 2026-07-25) — INCONCLUSO (confundido).** El ρ=−0.4725 de
  `b` vs brecha inicial parecía respaldar convergencia **vs cero**, pero brecha y
  `b` salen del mismo ajuste y el hub se asigna por PIB promedio → anticorrelación
  por construcción. El **nulo correcto es sintético calibrado al Maddison real
  (Bloque 1d)**: full media −0.4244 [−0.5796, −0.2608], split −0.2465
  [−0.4132, −0.0902]. **Los dos observados (−0.4725 y −0.3676) caen DENTRO del
  nulo → no hay señal por encima del artefacto de asignación de hub**, ni en el
  test completo ni en el de datos disjuntos. El Bloque 1b (re-emparejamiento,
  media −0.57) NO es un nulo válido (conserva el mecanismo); se reporta como
  observación aparte. ⚠️ Este documento corrige dos redacciones previas.
- **Veredicto honesto:** el dominio B **no queda respaldado ni como β-convergencia
  ni como acoplamiento SNT**; el constructo de hub es post hoc (Bloque 0) y el
  estadístico está dominado por un artefacto de asignación (Bloque 1d).
- **Bloques 2–3:** deliberadamente NO corridos aún (traer comercio bilateral es
  reconstruir el dominio con un hub emergente, no rescatarlo).

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
   hardcodeado a `'gradual'` en los constructores del dominio B
   (`expand_B_massive.py` y `expand_dominio_B.py`).

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

## Seguimiento — re-verificación 2026-09-26

Re-corrida completa de `snt_auditoria_integral_v32.py` sobre `main` y
recálculo independiente de las cifras que el runner no emite:

| Punto | Estado 2026-09-26 |
|---|---|
| Runner v32 | Corre limpio; **ninguna discrepancia**: 26 REPLICA, 1 REPLICA_SIGNO, 1 RANGO, 1 OK. El resto no es replicable por diseño: 5 NO_REPRODUCIBLE y 2 BLOQUEADO (requieren datos ausentes del repo), 1 CIRCULAR (`soberania` = umbral de ASI) y 7 INFO. |
| `data/owid-maddison.csv` (hallazgo #7) | **PRESENTE** — la fila del CSV de salida pasó de `AUSENTE/NO_REPRODUCIBLE` a `PRESENTE/OK`. La fila `dominio_B_regenerable` sigue fija en `NO` dentro del runner (pendiente de actualizar el script). |
| Hallazgo central por cluster | Recalculado con `spearman_cluster()`: ρ = −0.5555, p = 0.2525 (6 dominios); bootstrap por cluster IC95 [−0.7219, −0.0063]; sin E3 ρ = −0.1162 (p = 0.011, n = 480); sin E3 ni B ρ = −0.4264 (p = 0.0119, n = 34). **Replica exacto.** |
| RC9 (§5 del informe: "no verificable") | **Corregido:** los pares (b_rise, Δ_fall) sí están versionados en `data/orthogonality_crypto_v25.csv`; Spearman ρ = +0.009, p = 0.98, n = 11. Replica exacto. Alcance: solo cripto. |
| Origen del 5.9× (§8) | **Localizado:** aparece como texto fijo en el script histórico v28 `code/generate_publication_figures.py` (líneas del texto de la figura y del pie), no como cálculo sobre el corpus v5. Confirma la hipótesis del informe. |
| Composición del polo sin fricción | E1 (4) + E3 (234) = 238 casos, **todos OWID COVID-19** según la columna `fuente` de `by_domain/`. E1 no son invasiones biológicas. |
| Checksums de `data/FUENTES.md` | Los 6 SHA-256 coinciden con los archivos actuales. |
| Prueba de regresión | `pytest reconstruction_real/tests` → 4 passed. |

## Seguimiento — 2026-09-27: recálculo del 5.9× y filas fijas del runner

| Punto | Resultado |
|---|---|
| **Recálculo abrupto vs gradual** (hallazgo 1 del README; RC3, RC-ACO-2) | Nuevo script `code/recalculo_trigger_abrupto_gradual.py` → `data/trigger_abrupto_gradual_recalculo.csv` (+ log en `reconstruction_real/logs/`). **Origen del 5.9×:** tabla v1.0 de **2 abruptos vs 2 graduales** (`data/shadow_node_maddison_resumen.csv`): 0.717 / 0.122 = **5.87×**, Mann-Whitney p = 0.33. **Corpus activo ACO (n = 18: 10 abruptos, 8 graduales):** b̄ abrupto +0.40 vs gradual +0.85 → razón **0.47** (dirección inversa), Mann-Whitney p = 0.10 (dos colas), p = 0.96 (abrupto > gradual). Solo verificados (n = 14): razón 0.37, p = 0.14. **Intra-dominio** (permutación exacta estratificada; solo H y T tienen ambos disparadores; 16 permutaciones): p = 0.94. El disparador está confundido con el dominio (F todo abrupto, I todo gradual). **Histórico v2.0** (57 casos, sin 13 híbridos): razón 6.3, p = 0.053, pero 7 casos tienen R² < 0 (era obsoleta, no citable). n = 486 no corresponde a ningún conjunto del repo. **Veredicto: la afirmación no está respaldada por los datos activos.** |
| **Fila `dominio_B_regenerable`** (fija en `NO`) | **Causa:** era un literal escrito cuando faltaba `owid-maddison.csv`; nunca comprobaba nada. **Corregido:** el runner ahora regenera B en un directorio temporal con cada script constructor y lo compara contra `by_domain/dominio_B_real.csv`. Resultado: `expand_B_massive.py` → 441 casos vs 446 (408 pares comunes, corr(b) = 0.979, signo 396/408, **12/408 b idénticos**) → `PARCIAL`; `expand_dominio_B.py` → 254 casos (no reproduce el dominio) → `PARCIAL`. La edición de Maddison usada originalmente no se fijó. |
| **Fila RC9** (fija en `NO_REPRODUCIBLE`) | Mismo defecto. Ahora se calcula desde `orthogonality_crypto_v25.csv`: ρ = +0.009, p = 0.98, n = 11 → `REPLICA`. |
| **Runner v32** | 50 filas: 27 REPLICA, 1 REPLICA_SIGNO, 1 RANGO, 1 OK, 2 PARCIAL, 3 NO_REPRODUCIBLE, 2 BLOQUEADO, 1 CIRCULAR, 12 INFO (4 de ellas, el recálculo del disparador). Ninguna discrepancia. |

Pendientes que siguen abiertos: series crudas de E3 (corrección AR(1) de E3),
prueba de b ≥ 1 en otros dominios, p sin truncar + `r2_log`/`r2_raw`
separados en el corpus consolidado, fijar la edición exacta de Maddison que
reproduzca B (o re-publicar B con la edición versionada), nota al editor de
PLOS, y bloque 2 de la prueba discriminante (comercio bilateral).
