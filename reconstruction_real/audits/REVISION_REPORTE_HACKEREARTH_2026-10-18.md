# Revisión — Reporte HackerEarth "Fractal V3" (2026-10-18)

**Objeto:** `HackerEarth User Retention Analysis_ Fractal V3 Insights &
Intervention Strategy.pdf` (Downloads de Windows, 18-oct-2026, 7 páginas;
SHA-256 `92fa43f7b67c6236bcfaab00003ec9ba5c8a68c9fe65dd9e85426fd0d4196d52`).
**Proyecto:** rama `zerve` (commit `a4fef75`, 18-oct-2026 09:58 UTC),
directorio `79d2da5a-bd19-47f0-8eab-3f9d426e1f46/` — código sin datos
(21 archivos: 18 scripts, narrativa, canvas.yaml).

**Veredicto corto:** la segmentación descriptiva es razonable y la matriz de
acción es útil como herramienta de negocio, pero **las dos cifras principales
del reporte (ROC-AUC 0.9994 y ROC-AUC 1.0 / precision 1.0) son circulares por
construcción** — verificado en el código de la rama — y son **las mismas cifras
que la auditoría v32 ya retiró del preprint v30** (0.9994 filtrado → corregido a
0.715 ± 0.019; "precision = 1.0" → retirada como tautológica).

## 1. La circularidad, verificada línea por línea

La cadena completa (rama `zerve`, archivos `Development/`):

1. `cohort_segmentation_csi_v3.py` define las cohortes como **cortes de
   percentil de CSI_V3** (Elite ≥ p99.5; Intermediate p93.1–p99.5; Basic <
   p93.1), donde CSI_V3 = f(días activos, diversidad de herramientas,
   créditos, Coder Agent, VDR).
2. `retention_prediction_model.py`:
   ```python
   feature_cols = ["dias_activos", "herramientas_unicas", "total_creditos",
                   "pct_coder_agent", "VDR", "CSI_V3", ...]
   retention_df["retained"] = (retention_df["cohort"] != "Basic").astype(int)
   ```
   **La etiqueta es `cohort ≠ Basic` y `CSI_V3` — la variable que define la
   etiqueta — está literalmente en la matriz de features.** El modelo puede
   aprender el corte de percentil y separar perfectamente: ROC-AUC 1.0,
   precision 1.0, recall 1.0 **están garantizados por construcción**. El
   reporte lo presenta como "perfect separation... reflects clean cohort
   definition" — no es separación, es definición.
3. `retention_scoring.py` construye el score compuesto
   `0.50·prob + 0.30·CSI_V3 + 0.20·días_activos` y con él los `risk_tier`
   (High Risk = 4,444 = exactamente el conteo de Basic).
4. `churn_early_warning_classifier.py`:
   ```python
   _labeled["churn_label"] = (_labeled["risk_tier"].astype(str) == "High Risk")
   ```
   La etiqueta de churn es el tier — otra vez f(compromiso) — y los 284
   features son **eventos de compromiso** (créditos usados, uso de
   herramientas, velocidad de eventos). El 0.9994 mide cuán bien el
   compromiso predice el compromiso.

**Consecuencia:** los "churn lifts" (p. ej. "layer delete → 0.0× churn") son la
misma tautología: quien ejecuta acciones avanzadas no puede estar en Basic por
definición, así que su "churn" es 0 por construcción. No son señales predictivas
delatoras; son re-descripciones de la definición de la cohorte.

## 2. Conexión con la auditoría v32 — esto ya había pasado

| Cifra del reporte nuevo | Historial en el repo |
|---|---|
| ROC-AUC 0.9994 (churn early warning) | Es el número **exacto** del "leaked HackerEarth ROC-AUC" del v30, corregido en r31/r32 a **0.715 ± 0.019** tras la auditoría v32 |
| ROC-AUC 1.0, precision 1.0 (retención) | Es la "ASI precision = 1.0" retirada como **tautológica** ("measured against a label defined by the same ASI"). El reporte nuevo repite el patrón con CSI_V3 en lugar de ASI |

La rama `zerve` es probablemente **el origen (o una re-corrida) de las cifras
que se filtraron al v30** — lo cual, visto en positivo, documenta el mecanismo
que la auditoría sólo pudo inferir. El PDF de hoy titula con las cifras
retiradas ("exceptional predictive accuracy") cuando su propia sección de
limitaciones reconoce el problema a medias ("survivorship bias… anchor events
may be consequences of retention").

## 3. Qué SÍ vale del reporte

- **Segmentación descriptiva**: 4,774 usuarios; Basic 93.1% con ~0 engagement;
  Elite 24 con 31 días activos. Como **descripción** del snapshot es coherente
  (los números de cohortes cuadran entre scripts).
- **Matriz 2×2 de acción**: útil como organizador de negocio (2,108 / 2,329 /
  330 / 7) — con la salvedad de que "riesgo" y "engagement" son la misma
  variable, así que los cuadrantes son cortes de una dimensión, no dos.
- **Caveats**: la sección "Model Confidence & Caveats" del PDF reconoce
  supervivencia, causalidad, n pequeño (Elite n=24, At-Risk n=21) y drift — es
  la parte más honesta del documento; debería ir arriba, no abajo.

## 4. Para el Dominio D del corpus SNT

- La rama `zerve` trae **código sin datos** (ningún CSV/parquet de los 4,774
  usuarios) → el Dominio D **sigue NO_REPRODUCIBLE** para los 3 casos del
  corpus (los datos no se distribuyen).
- Lo nuevo: el mecanismo detrás de las cifras retiradas (0.9994 / 1.0) queda
  **documentado en el repo** con código citable, lo que refuerza la historia
  de la auditoría v32 si alguna vez hay que explicarla.

## 5. El arreglo, si se quiere un modelo honesto

1. **Etiqueta externa y temporal, no definida por engagement**: churn = "sin
   login en 60/90 días" medido hacia adelante desde una fecha de corte. El
   reporte mismo lo insinúa ("cross-sectional, not longitudinal").
2. **Nunca** CSI_V3 (ni sus componentes) como feature contra una etiqueta
   derivada de CSI_V3. Con la etiqueta temporal, CSI_V3 pasa a ser un
   *predictor legítimo* y el AUC resultante significará algo.
3. Reportar AUC contra la etiqueta temporal con su desbalance real, e
   idealmente con un holdout temporal (entrenar con datos hasta T, evaluar
   en T+90d), no un split aleatorio del snapshot.

## 6. Recomendaciones concretas

- **No citar 0.9994 ni 1.0/precision 1.0 en ningún lado** — el repo ya los
  retiró una vez; volver a publicarlos desharía la corrección de r31/r32.
- Si este reporte va a circular externamente (HackerEarth/consultoría),
  reescribir la cabecera: el valor real es la segmentación + matriz de acción,
  no el AUC.
- Si se quiere, implementar el arreglo §5 sobre la rama `zerve` (los scripts ya
  tienen la infraestructura; sólo la etiqueta y el split cambian) — requiere
  exportar el dataset de usuarios (que no está en la rama).

## 6. Verificación empírica con los datos — mismo día (agregada)

Con el dataset descargado (eventos PostHog crudos, 409,287 filas,
2025-09-01 → 2025-12-08, 4,774 usuarios; SHA en `data/FUENTES.md`) la
verificación (`code/hackerearth_verificacion.py` →
`data/hackerearth_verificacion_resultados.csv`) confirma y mide todo lo
anterior:

**Parte 1 — las cifras del PDF reproducen y son circulares:**

| Verificación | Resultado |
|---|---|
| Conteos del PDF (usuarios, cohortes, tiers) | **Exactos**: 4,774; 4,444/306/24; 4,444/299/21/10 |
| ¿"High Risk" es la cohorte Basic? | **4,774/4,774 usuarios idénticos** — la etiqueta de churn ES la cohorte |
| Modelo de retención reproducido (features incl. CSI_V3, label = cohort ≠ Basic) | **AUC 1.0000 exacto** (PDF: 1.0000); CSI_V3 = 43% de la importancia |
| **CSI_V3 SOLO** contra la etiqueta de churn (sin los 284 features) | **AUC 1.0000** — el modelo de 284 features del PDF (0.9994) es *peor* que la variable que define la etiqueta |

**Parte 2 — la prueba honesta (temporal prospectiva):** corte T1 = 2025-11-08,
features sólo de eventos pre-T1, etiqueta = inactividad los 30 días siguientes:

| Población | n | tasa churn | GBM AUC (CV 5-fold) | AUC de sólo recencia |
|---|---:|---:|---:|---:|
| Todos los usuarios pre-T1 | 2,058 | 92.7% | **0.836 ± 0.038** | 0.791 |
| Antigüedad ≥ 7 días | 137 | 62.0% | **0.893 ± 0.041** | 0.907 |

Importancias honestas: **recencia y antigüedad** dominan (no los "anchor
events" del reporte). Caveats declarados: censura a la derecha (el dato
termina 2025-12-08), una sola ventana de 30 días, un solo corte.

**Lectura conjunta:**

1. El gap **1.0000 → 0.836** es la circularidad removida. El sistema sí tiene
   señal predictiva real de dormancia (~0.84–0.89 honesto) — modesta y
   utilizable, no "excepcional".
2. La cifra honesta cae en la **vecindad de la corrección de la auditoría v32
   (0.715 ± 0.019)**, no en la del leak (0.9994) — la corrección de la
   auditoría queda validada retrospectivamente con datos que entonces no
   estaban distribuidos.
3. El 0.9994 del PDF de hoy queda **empíricamente caracterizado**: es el AUC de
   predecir una etiqueta con la variable que la define, mediada por 284
   features redundantes.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-18*
