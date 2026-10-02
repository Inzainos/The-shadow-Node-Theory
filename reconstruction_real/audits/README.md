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

### Valor puntual del Dominio B (2026-10-02) — cerrado como indecidible

- **Pre-registro:** [`../preregistro/PREREGISTRO_DOMINIO_B_PUNTUAL_2026-10-02.md`](../preregistro/PREREGISTRO_DOMINIO_B_PUNTUAL_2026-10-02.md)
  (commit `05bc9ee`, subido antes de correr el script).
- **Informe:** [`RESULTADOS_DOMINIO_B_PUNTUAL_2026-10-02.md`](RESULTADOS_DOMINIO_B_PUNTUAL_2026-10-02.md).
- **Script:** [`../code/dominio_B_valor_puntual.py`](../code/dominio_B_valor_puntual.py) (con log).
- **Salidas:** `reconstruction_real/data/dominio_B_calibracion.csv` (tamaño y poder
  por método) y `dominio_B_valor_puntual.csv` (p de los doce métodos, por caso).
- **Cómo regenerar:** `python reconstruction_real/code/dominio_B_valor_puntual.py`
  (sin red; ~2 min).

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
- **Re-corrida con la edición del corpus (MPD2020), 2026-09-27.** La corrida
  anterior usó la edición OWID posterior (441 pares). Con MPD2020 (446 pares) y
  5000 iteraciones: Bloque 1 ρ = −0.4893 vs nulo −0.4226 [−0.5765, −0.2418] →
  DENTRO (p empírico 0.213); Bloque 1c ρ = −0.3846 vs nulo −0.2508 [−0.4050,
  −0.0788] → DENTRO, pero **en el límite** (p empírico 0.050, a 0.020 del
  borde). Veredicto con el criterio IC95: **sigue INCONCLUSO**; el test limpio
  se acerca a β-convergencia (p 0.080 → 0.050) sin ser concluyente.
- **Veredicto honesto:** el dominio B **no queda respaldado ni como β-convergencia
  ni como acoplamiento SNT**; el constructo de hub es post hoc (Bloque 0) y el
  estadístico está dominado por un artefacto de asignación (Bloque 1d).
- **Bloques 2–3 (corridos 2026-09-27, COW Trade v4.0, 432/446 pares):** el
  acoplamiento SNT **no se sostiene**: la participación media del comercio
  nodo→hub no se relaciona con `b` (ρ = −0.043; permutación intra-región
  p = 0.72) y no añade R² (0.0001). La participación **inicial** se asocia con
  **menor** `b` (ρ = −0.185; cluster por nodo p = 0.022; permutación p = 0.026),
  signo opuesto al predicho. Modelo conjunto R² 0.290 (solo brecha 0.286).
- **Antes (2026-07-25):** Bloques 2–3 deliberadamente NO corridos (traer comercio bilateral es
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
| Valor puntual | **cerrado 2026-10-02 como indecidible**: de doce correcciones evaluadas por su tasa de falso positivo medida, ninguna alcanza la banda [2.5%, 7.5%] (mejor: 11.7% la cota inferior; GLS 17.1%; bloques 24.1%; OLS 67.0%). Sobre los datos reales la cuenta va de 33 a 134 de 156 según el método. Informe: [`RESULTADOS_DOMINIO_B_PUNTUAL_2026-10-02.md`](RESULTADOS_DOMINIO_B_PUNTUAL_2026-10-02.md) |

La partición **290/446 no estimables** es el hallazgo más limpio: sale directo de
`n_eff < 3`, sin convenciones ni aproximación de Bartlett. La cota inferior 33 es
la corrección coherente (**inflar el SE** `√((1+ρ)/(1−ρ))`, mediana 5.9×, *además*
de recortar gl) y es invariante a la convención de gl. El valor puntual **se cerró el 2026-10-02, y la respuesta es que no hay número**
(pre-registro `../preregistro/PREREGISTRO_DOMINIO_B_PUNTUAL_2026-10-02.md`, commit
`05bc9ee`, informe `RESULTADOS_DOMINIO_B_PUNTUAL_2026-10-02.md`). En vez de elegir
una corrección por autoridad se midió la de cada una: 2,000 casos sintéticos con
`b = 0` y la terna `(n, ρ, σ)` de un caso real, donde todo rechazo es un falso
positivo por construcción. Ninguno de los doce métodos cae en la banda de admisión
[2.5%, 7.5%] fijada por anticipado — la cota inferior AR(1) da 11.7%, Prais-Winsten
GLS 17.1%, el bootstrap por bloques 24.1%, Newey-West 52.3% y el **OLS del corpus
67.0%** — y el poder es del 74% al 98% a `b = −0.30`, así que el fallo es de tamaño y
no de conservadurismo. Sobre los 446 casos reales la cuenta va de **33 a 134 de 156**
según el método: ese abanico es el argumento. Tres validaciones salieron del diseño:
446/446 series reproducen su `b` publicada, `nw_auto` devuelve el 120/156 de la
auditoría y `ar1_inf` devuelve el 33/156 publicado. **El método mejor calibrado de los
doce es el que ya se citaba como conservador, y da exactamente 33.** Nota de margen:
recomputada desde las series crudas la cota superior da 113 y no 112, por el redondeo
de un `dw` a tres decimales en un único caso (`B042`, Belgium→Spain, p = 0.0490 contra
0.0503); la cota inferior da 33 por las dos vías.
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
| **Recálculo abrupto vs gradual** (hallazgo 1 del README; RC3, RC-ACO-2) | Nuevo script `code/recalculo_trigger_abrupto_gradual.py` → `data/trigger_abrupto_gradual_recalculo.csv` (+ log en `reconstruction_real/logs/`). **Origen del 5.9×:** tabla v1.0 de **2 abruptos vs 2 graduales** (`data/shadow_node_maddison_resumen.csv`): 0.717 / 0.122 = **5.87×**, Mann-Whitney p = 0.33. **Histórico v2.0** (57 casos, sin 13 híbridos): razón 6.3, p = 0.053, pero 7 casos tienen R² < 0 (era obsoleta, no citable). n = 486 no corresponde a ningún conjunto del repo. El corpus de satelización activo no tiene variable de disparador. **ACO (n = 18: 10 abruptos, 8 graduales)** sí la tiene, pero su b es un **exponente de absorción** (R = masa absorbente / masa pico del hub): prueba RC-ACO-2, no el RC3. Ahí gradual ≥ abrupto: b̄ +0.85 vs +0.40, razón 0.47, Mann-Whitney p = 0.10 (dos colas); solo verificados (n = 14): razón 0.37, p = 0.14; intra-dominio (permutación exacta estratificada, H y T, 16 permutaciones) p = 0.94; disparador confundido con el dominio (F todo abrupto, I todo gradual). **Veredicto: RC3 pasa a UNTESTABLE** (prueba publicada no reproducible, corpus activo sin variable de disparador); RC-ACO-2 queda indeciso con n = 18. |
| **Fila `dominio_B_regenerable`** (fija en `NO`) | **Causa:** era un literal escrito cuando faltaba `owid-maddison.csv`; nunca comprobaba nada. **Corregido:** el runner regenera B en un directorio temporal y lo compara caso a caso y por SHA-256 contra `by_domain/dominio_B_real.csv`. **Edición del corpus identificada:** Maddison Project Database 2020 (`data/mpd2020.xlsx`, descargado de la GGDC; en Google Drive solo estaba la edición 2023). Con ella `expand_B_massive.py` reproduce los 446 casos **byte a byte** (SHA-256 idéntico, 19 columnas iguales) → `REPLICA`. Con la edición OWID posterior: 441 vs 446, corr(b) = 0.979, 12/408 b idénticos → `PARCIAL` (sensibilidad a la edición). `expand_dominio_B.py` (script previo): 254 casos → `PARCIAL`. |
| **Fila RC9** (fija en `NO_REPRODUCIBLE`) | Mismo defecto. Ahora se calcula desde `orthogonality_crypto_v25.csv`: ρ = +0.009, p = 0.98, n = 11 → `REPLICA`. |
| **Prueba discriminante con MPD2020** | Re-corrida con la edición del corpus (446 pares; antes 441 con OWID) y 5000 iteraciones. Bloque 1: −0.4893, DENTRO (p 0.213). Bloque 1c: −0.3846, DENTRO en el límite (p 0.050, margen 0.020). **Veredicto: sigue INCONCLUSO.** El script ahora calcula este veredicto por sí mismo (antes imprimía "RESPALDADA" por la comparación contra cero) y acepta `--omitir-1b`. Salidas `discrim_bloque1*.csv` regeneradas con MPD2020. |
| **Bloques 2–3 de la prueba discriminante** | Corridos con Correlates of War Trade v4.0 (`data/COW_Trade_4.0.zip` → `build_comercio_bilateral_cow.py` → `data/comercio_bilateral.csv`; reglas de entidad para URSS, Yugoslavia, Vietnam del Norte y Pakistán unificado). 432/446 pares. Participación media nodo→hub: ρ = −0.043 (p = 0.37; permutación intra-región p = 0.72). Participación inicial: ρ = −0.185 (cluster por nodo p = 0.022; permutación p = 0.026), **signo opuesto** al predicho por SNT. Modelo conjunto: R² 0.290; solo comercio 0.0001. **Acoplamiento SNT no respaldado** (con el hub asignado). |
| **Reconstrucción del dominio B con hub emergente del comercio** | Informe [`RECONSTRUCCION_DOMINIO_B_HUB_COMERCIO.md`](RECONSTRUCCION_DOMINIO_B_HUB_COMERCIO.md); script `code/reconstruccion_B_hub_comercio.py` → `data/dominio_B_hub_comercio.csv` + `data/dominio_B_hub_comercio_intra_nodo.csv` (+ log). Hub = mayor destino de exportación del nodo en su primera década de datos COW (predeterminado), mismo ajuste que B. 102/103 países; 19 hubs (Reino Unido 37, Estados Unidos 27). Solo **9/102** pares hub–nodo comerciales existen en B; el hub cambia para 2005–2014 en 77/102. Con hub más rico, **62/95 convergen** (b < 0). ρ(b, brecha) = −0.153 (p = 0.125) vs −0.489 en B. **Hub vs controles con la misma brecha:** d mediana −0.014, 45/102 > 0, Wilcoxon p = 0.78 (cluster por hub p = 0.62) → **sin acoplamiento**. Hub de ventana completa da d > 0 (p = 5×10⁻¹⁰), pero es causalidad inversa por gravedad (endógeno). Dentro de cada nodo: ρ parcial mediana +0.115 (Wilcoxon p = 0.046; permutación p = 0.15; con control de tamaño, signo p = 0.10) → no concluyente. Calidad: Mongolia y Vietnam con comercio CMEA faltante en COW (excluirlos no cambia nada). **Veredicto: la reconstrucción no rescata el acoplamiento.** |
| **Runner v32** | 51 filas: 28 REPLICA, 1 REPLICA_SIGNO, 1 RANGO, 2 OK, 2 PARCIAL (sensibilidad a la edición y script previo), 3 NO_REPRODUCIBLE, 2 BLOQUEADO, 1 CIRCULAR, 11 INFO. Ninguna discrepancia. |

Pendientes que siguen abiertos: series crudas de E3 (corrección AR(1) de E3),
prueba de b ≥ 1 en otros dominios, p sin truncar + `r2_log`/`r2_raw`
separados en el corpus consolidado, y una definición de hub variable en el
tiempo antes de volver a usar pares de países como evidencia (PLOS queda para el
reenvío de la teoría una vez afinada). Hechos el 2026-09-27: ~~fijar la edición
exacta de Maddison~~ (MPD2020, reproducción byte a byte), ~~re-correr la prueba
discriminante con MPD2020~~ (sigue inconclusa), ~~bloque 2 con comercio
bilateral~~ (acoplamiento no respaldado), ~~actualizar el preprint de SSRN~~
(revisión r31 en inglés y español, `papers/snt_ssrn_v31*`, sustituida antes de
subirse por la r32, `papers/snt_ssrn_v32*`, que agrega el pre-registro; la subida la
hace el autor) y ~~reconstruir el dominio B con hub emergente del comercio~~ (no rescata
el acoplamiento).

## Pre-registro 2026-09-27 — seis puntos pedidos por el autor

- **Pre-registro:** [`../preregistro/PREREGISTRO_2026-09-27.md`](../preregistro/PREREGISTRO_2026-09-27.md)
  (commit `c319fac`, subido antes de descargar datos nuevos o correr pruebas).
- **Informe:** [`RESULTADOS_PREREGISTRO_2026-09-27.md`](RESULTADOS_PREREGISTRO_2026-09-27.md).

| Punto | Script | Decisión pre-registrada |
|---|---|---|
| 1. Hub variable en el tiempo | `code/prueba_hub_temporal.py` | **No respaldada** (H = 20: d mediana −0.009, p = 0.95); H = 30 **contraria** (p = 0.0002, d < 0) |
| 2. Fricción con dominios nuevos sin COVID | `code/prueba_friccion_dominios_nuevos.py` | **No respaldada** (7 dominios, ρ = −0.131, permutación exacta p = 0.39) |
| 3. Series crudas COVID | `code/covid_E3_series_crudas.py` | E3 reproducido 233/234 y **robusto** a la autocorrelación (cota AR(1) conservadora: 176 de 198 estimables; Newey-West estándar subcorrige); E1 no reproducible |
| 4. Disparadores codificados a ciegas | `code/prueba_disparadores_ciudades.py` | **Respaldada** (8/8, Wilcoxon p = 0.0039; salvedad de supervivencia de WUP) |
| 5. Cohortes ACO-A | `code/descargar_binance_klines.py`, `code/aco_cohortes_ampliadas.py` | 5a ortogonalidad **respaldada** (242 pares, ρ = −0.119, IC [−0.241, +0.007]); 5b h > 0 **respaldada** en cripto (663) y bancos (27,771); h creciente solo en cripto (confundida con el calendario), bancos en bañera; 5c no ampliable |
| 6. Pre-registro | — | hecho antes de todo lo anterior |
