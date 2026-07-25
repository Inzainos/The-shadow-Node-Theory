# Registro de cambios (Changelog)

Todas las versiones relevantes de **Shadow Node Theory (SNT)** se documentan en
este archivo. El formato se basa en [Keep a Changelog](https://keepachangelog.com/es/1.1.0/)
y el proyecto sigue [Versionado Semántico](https://semver.org/lang/es/).

Las fechas corresponden a la integración de cada versión en la rama `main`.

## [No publicado] — 2026-07

### Añadido
- **Prueba discriminante del dominio B — acoplamiento vs convergencia**
  (`reconstruction_real/code/prueba_discriminante_dominio_B.py`,
  `audits/DISCRIMINANTE_DOMINIO_B.md`). Separa dos hipótesis sobre qué mide el
  exponente `b` del dominio B (62% del corpus): acoplamiento hub-satélite (SNT)
  vs β-convergencia de PIB per cápita. **Bloque 0** (diagnóstico estructural, sin
  datos externos) muestra que el rol de "hub" es una propiedad del par, no del
  país — **85% de los hubs también aparecen como satélites** (Italia: hub en 3
  pares, satélite en 12; México 1/9) — y que `b` depende fuertemente de la región
  (Kruskal-Wallis H=63.5, p=1.2e-8) con un gradiente coherente con convergencia
  (negativo en regiones ya convergidas, positivo en rezagadas). Mueve el *prior*
  hacia H-CONVERGENCIA sin cerrarla. Bloques 1–3 (b vs brecha inicial de PIB; b
  vs comercio bilateral; modelo conjunto) quedan BLOQUEADOS por datos ausentes
  (`owid-maddison.csv` + matriz de comercio bilateral direccional).
- **Auditoría integral v32 (`reconstruction_real/audits/`).** Recorrido completo
  de las cifras publicadas: 14/33 replican exacto; la aritmética del corpus está
  limpia (`MASTER_cifras_v5.json` 8/8, `MASTER_resumen_v5.csv` 40/40). Lo que
  falla es la capa de inferencia, en cuatro puntos independientes:
  (1) **autocorrelación serial** del dominio B —62% del corpus— con DW mediana
  0.112, 99.8% de casos con DW<1, ρ AR(1)≈0.944 y **n efectivo mediano ≈2.2**
  (no 69), que infla la significancia por caso; (2) el **régimen superlineal
  b≥1 puede ser artefacto de modelo** (por AIC sobre las 18 series ACO la
  potencia gana 13/18, pero los 4 casos exponenciales tienen b̄ +1.54:
  a mayor b, peor ajusta la ley de potencia); (3) **la dirección aguanta pero el
  p no** (doble inflación: autocorrelación + 714 casos no independientes);
  (4) **defectos de reporte** (557/721 p-values truncados a `0.0` por
  `round(p,6)`, dos definiciones de R² promediadas juntas, `trigger`
  hardcodeado a `'gradual'`). Nuevos scripts, retrocompatibles:
  `code/snt_utils_v32.py` (extiende `snt_utils.py`: DW para todos los ajustes,
  `rho_ar1`/`n_eff`/`p_ar1` Newey-West, `r2_log`+`r2_raw`, `p_exacto`,
  `comparar_modelos` por AIC —la prueba RC1 que el README afirmaba sin
  implementar—, `ajustar_mle_clauset`, `spearman_cluster`, `corregir_corpus`,
  `fdr_bh`, `plegado_trigger`) y
  `reconstruction_real/code/snt_auditoria_integral_v32.py` (runner único, 43
  cifras, salida a CSV; absorbe rc12/rc13) y una prueba de regresión
  `reconstruction_real/tests/test_correccion_ar1.py`. Salidas:
  `dominio_B_corregido_ar1_v32.csv` y `auditoria_integral_v32_resultados.csv`.
  **Corrección AR(1): estimabilidad primero (dos rondas de revisión cruzada
  2026-07-25).** El conteo original de 145/446 significativos del dominio B
  estaba mal por dos razones independientes: (1) media corrección incoherente
  (recortaba gl pero no inflaba el error estándar `√((1+ρ)/(1−ρ))`, mediana
  5.9×); (2) contaba como significativos casos con `n_eff < 3`, que no admiten
  un ajuste de dos parámetros. Marco correcto, tres cifras: **156/446 estimables
  (n_eff≥3), 290/446 NO estimables (n_eff<3)** —reportados como no estimables,
  no como no significativos: el hallazgo más limpio, sale directo de n_eff sin
  convenciones—; entre los 156 estimables, los significativos caen a un rango
  **[33 (21.2%), 112 (71.8%)]** según la variante analítica; el valor puntual
  requiere Newey-West/GLS sobre residuos crudos (ausentes del repo).
  `corregir_corpus()` expone `estimable`/`se_infl` por caso y emite un
  `UserWarning`; `reconstruction_real/tests/test_correccion_ar1.py` fija
  156/290/33/112 (cifras invariantes a la convención de gl — no 145).

### Corregido
- **Provenance y circularidad (higiene de la auditoría v32).** `data/FUENTES.md`
  ancla las fuentes externas (Maddison Project y OWID COVID) con URL, edición,
  fecha y SHA-256, y documenta que `data/owid-maddison.csv` está **ausente** en
  el repo (por eso el dominio B, 62% del corpus, no se regenera clonando).
  `data/snt_asi_scores_README.md` marca la columna `soberania` como **umbral de
  ASI** (separación perfecta ASI>~1), advirtiendo que usarla como target sería
  circular por construcción (solo 13/4,774 = 0.27% positivos).

- **v31 — Patch Módulo Micro + Macro (2026-07-06):** integración de Principio
  del Paisaje Vivo, axiomas Ax-M1 a Ax-M4, dinámica del 5-Event Wall (cuatro
  trayectorias tipo), Análisis de Divergencia Retrospectiva, extensión de
  Filogenia Predictiva a clados biológicos, y Recurrencia de Poincaré
  operacionalizada. Operador universal (b, F, E_res, C_k) demostrado invariante
  a cualquier escala (individuo, linaje, civilización, planeta). Roadmap Item 5
  abierto: corpus multi-escala con trayectorias completas etiquetadas.
  Archivo: `papers/marco_teorico_v31_patch.md`.
- **Validación del agente genómico con datos reales de paciente**: el pipeline
  completo (Triage Nivel 1 → Escáner de bloques Nivel 2 → análisis ACO-A) se
  ejecutó de extremo a extremo contra un caso TCGA-BRCA genuino y de acceso
  abierto (`TCGA-BH-A18H`, vía la API pública NIH GDC), confirmando que corre
  sin errores sobre RNA-seq real (59/60 genes del panel SNT, 23 coincidencias
  confirmadas, 23 anomalías huérfanas). Script reproducible, datos y reporte en
  `genomic_agent/analysis/real_patient_validation/`.
- **Validación a escala (976 pacientes reales)**: el pipeline se ejecutó contra
  la cohorte completa de tumor primario TCGA-BRCA (976 casos únicos, descarga en
  10 lotes de ~100 vía GDC POST /data), contra el baseline empírico. 976/976 sin
  excepciones; distribuciones estables y discriminantes (confirmadas media 7.49,
  huérfanas 14.79, hubs ACO-A 3.86). Reporte, agregado y runner en
  `genomic_agent/analysis/real_patient_validation/scale_976/`.
- **Ronda 2 de validación (lote de 8 pacientes reales)**: el pipeline se ejecutó
  en batch contra 8 casos TCGA-BRCA de tumor primario (vía API NIH GDC), esta vez
  contra el baseline empírico. 0 excepciones; resultados heterogéneos y
  biológicamente plausibles por paciente (confirmadas media 5.5, huérfanas media
  13.75, hubs ACO-A media 2.5). Runner, datos y reporte en
  `genomic_agent/analysis/real_patient_validation/round2/`.
- **Baseline genómico derivado de tejido sano real**: `BASELINE_NETWORK` (el
  denominador del Z-score en los escáneres Nivel 1/2) pasó de valores sintéticos
  calibrados a mano a valores derivados de n=40 muestras TCGA-BRCA de tejido
  normal-adyacente (vía API NIH GDC). 50/51 pares empíricos; solo `NRAS→PI3K`
  permanece sintético. Con el nuevo baseline el escáner es más selectivo en el
  paciente real (confirmadas 23→10, huérfanas 23→14) y los Z-scores caen a un
  rango biológicamente plausible. Script y procedencia en
  `genomic_agent/analysis/baseline_derivation/`.
- **Carpeta del proyecto Delta** (`delta/`): scaffold del modelo independiente
  de predicción cripto & bolsa sobre el exponente de colapso Δ (ACO-A), con la
  línea Omega (Ω(t)) como precursor.
- **Delta — motor SNT + datos reales**: núcleo de satelización portado
  self-contained (R(t)=a·t^b + régimen), motor de señal (b vs fricción →
  DeltaSignal), y adaptadores de datos reales sin API key (CoinGecko para
  cripto BTC vs top-10 alts; Yahoo Finance para bolsa S&P 500 + IPC/BMV).
  Corrida real: 23 señales (`delta/real_delta_signals.json`). Señal descriptiva,
  no consejo financiero.
- **`.flake8`**: configuración de linting como fuente única (antes vivía solo
  inline en el flujo de CI).
- **`SECURITY.md`**: política de seguridad y manejo de datos sensibles (PHI,
  secretos, datos propietarios).
- **`AGENTS.md` + `CLAUDE.md`**: guía operativa para agentes de IA en la raíz,
  espejo del estándar del repo `workspaces` (rama→PR→merge, datos reales,
  Conventional Commits, no PHI/secretos, CI verde antes de merge).

### Documentación
- `genomic_agent/README.md`: documenta el baseline empírico (n=40 tejido sano
  TCGA) y las validaciones con pacientes reales (rondas 1/2 + escala 976).
- `README.md`: árbol de archivos de `delta/` actualizado con los adaptadores de
  datos reales (`data_adapters.py`, `run_real_delta.py`).

### Cambiado
- Estado de publicaciones: revisión v30 de **PLOS Complex Systems** (PCSY-D-26-00059)
  enviada; ponencia **MIT GCFP** (13ª conferencia anual) enviada.
- CI: el paso de `flake8` ahora lee su configuración desde `.flake8` en vez de
  pasar las banderas `--select`/`--exclude` inline.

## [2.5.0] — 2026-06-28

### Añadido
- **Capa de Colapso Orbital Acoplado (ACO-A)**: el colapso se reformula como un
  eje universal y transversal de SNT, con un segundo exponente ortogonal (Δ)
  ajustado sobre el reloj propio τ desde la extinción funcional.
- **Capa de hazard `h(τ) > 0`**: enunciado falsable de que "ningún sistema es eterno".
- **Taxonomía de modos de colapso** en tres factores (fricción × disparador ×
  piso/techo): Decaimiento Orbital Regulado, Cracquelure, Floor-Arrested,
  Catastrophic Cliff y Logistic Sweep.
- **Principio de Mínima Fricción** como criterio unificador (flujo de gradiente
  sobre un paisaje de estabilidad).
- Evidencia de colapso en **5 dominios** con datos reales (finanzas, historia,
  cripto, biología y astronomía): `reconstruction_real/data/collapse_multidomain_v29.csv`.
- Teoría completa en `papers/SNT_Colapso_Acoplado.md`; figuras de paisajes de
  estabilidad y catástrofe de cúspide (`figures/fig_paisajes_colapso.*`,
  `figures/fig_catastrofe_cuspide.*`).
- Marco teórico v30 (ES + EN, MD/PDF/DOCX) y preprint SSRN v30 (ES + EN).
- Criterios de refutación ampliados a RC9–RC11.

### Cambiado
- Revisión SSRN v30 enviada el 2026-06-28; estado del registro Zenodo
  actualizado al corpus de 721 casos.

## [2.4.0] — 2026-06-26

### Añadido
- **Corpus REAL de 721 casos** reconstruido íntegramente desde fuentes primarias
  públicas (`reconstruction_real/`), reemplazando el corpus sintético previo.
- **Módulo XVI — Arquitectura de Colapso Orbital (ACO)**: 18 casos verificados
  en 4 dominios (financiero, tecnológico, histórico, industrial).
- **SNT Genomic Topologic Analyzer** (`genomic_agent/`): agente de análisis de
  topología regulatoria con arquitectura de dos niveles.
- Dashboard interactivo en Streamlit (`dashboard/`).
- Figuras de publicación v29 generadas desde el corpus real (SVG + PNG).
- Reporte de proyecto `SNT_Project_Report_v29.pdf`.

### Cambiado
- Auditoría v2.4.0: scripts v28 marcados como obsoletos/deprecados.
- Verificación de integridad: R² ∈ [0,1] en todos los casos.

### Obsoleto
- Datos y papers de la era de 502 casos movidos a `archive/` (no citables).

## [2.3.1] — 2026 (preprint y validación)

### Añadido
- Paquete de replicación completo y envío a J. Complex Networks (rechazado).
- Validación de la hipótesis H-φ: resultado negativo en rondas independientes
  (H-φ refutada; no afecta el hallazgo central fricción–satelización).
- Corrección de fuga de datos en validación HackerEarth (ROC-AUC corregido).
- ORCID del autor y DOI de Zenodo v2.3.1.

## [2.2.0] — 2026 (paquete de replicación)

### Añadido
- Paquete de replicación v2.2 y figuras de publicación (Fig1–4, 300 dpi).
- Envío a PLOS Complex Systems.

## [2.0.0] — Inicial

### Añadido
- Publicación inicial del marco SNT, preprint SSRN y primeras versiones del
  corpus y del marco teórico.

---

> **Nota histórica.** El corpus de 502 casos (v2.3.1 y anteriores) contenía
> valores generados sintéticamente y una columna r² con valores imposibles.
> Esos archivos se conservan en `archive/` como registro histórico, pero
> **no deben citarse en publicaciones académicas**. La versión activa es la v2.5.0.
