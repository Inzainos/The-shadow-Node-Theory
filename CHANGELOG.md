# Registro de cambios (Changelog)

Todas las versiones relevantes de **Shadow Node Theory (SNT)** se documentan en
este archivo. El formato se basa en [Keep a Changelog](https://keepachangelog.com/es/1.1.0/)
y el proyecto sigue [Versionado Semántico](https://semver.org/lang/es/).

Las fechas corresponden a la integración de cada versión en la rama `main`.

## [No publicado] — 2026-07

### Añadido
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
