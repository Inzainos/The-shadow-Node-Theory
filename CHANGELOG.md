# Registro de cambios (Changelog)

Todas las versiones relevantes de **Shadow Node Theory (SNT)** se documentan en
este archivo. El formato se basa en [Keep a Changelog](https://keepachangelog.com/es/1.1.0/)
y el proyecto sigue [Versionado Semántico](https://semver.org/lang/es/).

Las fechas corresponden a la integración de cada versión en la rama `main`.

## [Marco teórico v34] — 2026-09-14 — Capa de proyección
*Cruzado contra el corpus Shadow Node Theory v2.5.2. Las dos numeraciones son independientes: esta entrada versiona el marco teórico, no el corpus.*

### Agregado

- **Axioma 0.1 (ESTRUCTURAL) — Cubo de incertidumbre.** Corolario estructural del Axioma 0. Formaliza el volumen de estados `𝒞 ⊂ ℝⁿ × T`, instanciado de trabajo como `𝒞(u, m, τ)` con `u` = apertura de posibilidades, `m` = magnitud o capacidad de sostén, `τ` = fase normalizada. Lectura vinculante: **cubo de estados** (no de observación, no ontológico). Se declara de forma explícita que **`u` carece de definición operativa en todos los dominios actuales** y que el volumen opera en `(m, τ)` hasta que se resuelva: sin proxies, misma regla que rige las series vacías del Dominio G. Regla de admisión de ejes: un eje entra a `𝒞` con definición operativa en dos dominios o más; con uno es etiqueta, no coordenada. Responde al horizonte que el cierre de la v33 dejó escrito ("traducir los axiomas a variables, ejes y dinámicas dentro de un espacio 3D").

- **Axioma 0.2 (OBSERVABLE) — Sombra / proyección.** Establece la capa entre el cubo y el dato: `𝒮ᶿ = Π_θ(𝒞)`. Marco de medición obligatorio **`θ = (B, V, ρ, W, λ)`** — base de observación, selección de variables, resolución, ventana temporal y umbral de corte. Define cinco clases de corte admitidas, la **no identificabilidad** de `Π_θ` con sus tres consecuencias normativas, el criterio de **invarianza de proyección** (dos `θ` independientes, diferentes en al menos dos componentes, uno de ellos `B` o `V`), y la reconstrucción como **conjunto `ℛ`** en vez de elemento único. Se ancla el criterio en un caso real del repo: la autocorrelación del Dominio B (99.8 % de 446 casos, `n` efectivo mediano 2.2) es invarianza de proyección fallida.

- **Geometría de la fricción.** La fricción entra al Axioma 0.1 como **campo escalar `φ` sobre el volumen**, no como eje coordenado ni como parámetro por caso, apoyada en el Principio de Mínima Fricción de ACO-A §5 (flujo gradiente sobre un paisaje de estabilidad). El cubo deja de ser espacio neutro y pasa a ser paisaje; los seis paneles de `figures/fig_paisajes_colapso` son ese paisaje dibujado. Se declara que **`φ` está postulado y no medido** — hoy existe fricción por dominio (categórica, 11 dominios) y por caso (ordinal 1–6, cohorte 2008, n=6) — y que operacionalizarla a lo largo de un camino sigue siendo el pendiente prioritario que ACO-A ya registraba.

- **Extensión del Axioma 12 — Cimática del colapso.** Extiende el axioma del extremo de la forma que emerge al de la forma que aparece cuando un sistema pierde o reorganiza regiones del volumen. Toma los modos de ACO-A como familias morfológicas iniciales; fija las cuatro condiciones simultáneas para declarar subfamilia (residual no explicado por la familia madre, `n ≥ 3` en dos dominios o más, separabilidad no explicable por ruido ni por el `n` efectivo, invarianza verificada), con figura de "candidato" para quien cumpla tres de cuatro. Incorpora **cláusula anti-metáfora** explícita (analogía de forma, sin campo vibratorio, sin placa material). Acota el alcance actual al eje **acelera / no acelera** conforme a ACO-A §6.5, porque el piso sigue siendo factor y no variable medida. **Estatus del Axioma 12 sin cambio: CONCEPTUAL**, con condición escrita para pasar a METODOLÓGICO.

- **Etiquetas de estatus.** Tres nuevas: **ESTRUCTURAL** (modelo, obliga a definición operativa por dominio), **OBSERVABLE** (capa que se mide, exige `θ` declarado) y **ESPECULATIVO** (fuera del cuerpo axiomático, no citable como premisa).

- **Cláusulas metodológicas 6, 7, 8 y 9.**
  - **6.** Marco de medición obligatorio: toda figura, sombra o volumen lleva su `θ` completo en el pie; sin `θ` no se cita como evidencia. Aplica también a las figuras ya existentes en `figures/`.
  - **7.** Protocolo ciego con pre-registro: los descriptores morfológicos se calculan sobre la serie cruda `t/R` y **nunca** sobre `b`, `Δ` ni fricción, por ser insumos definicionales del modo; hipótesis fechadas antes de correr.
  - **8.** Prohibición de imputar descriptores faltantes; se registran como faltantes con motivo.
  - **9.** El alcance del marco no se encoge entre versiones: el marco es cosmológico, geofísico y evolutivo, y SNT está contenido en él. Un axioma que pierde anclaje cambia de etiqueta, no se borra ni se subordina.

- **Apéndice especulativo — cubo ontológico.** Se aísla la lectura ontológica del volumen fuera del cuerpo axiomático, junto a la capa humana de la v33, e impide su uso como premisa de resultados del marco o del paper empírico.

- **Cadena operativa.** Capa transversal de proyección que atraviesa los pasos medibles de la cadena 0–8: datos heterogéneos → sombra con `θ` → secuencia → repetición bajo `θ'` → reconstrucción del volumen → familias morfológicas.

### Modificado

- **Aclaración semántica.** "Tela" queda reservada con exclusividad para el Axioma 0. Todo material observado o reconstruido se denomina **sombra** (uso descriptivo) o **proyección** `Π_θ` (contexto matemático). La ambigüedad venía de la propia v33, que usaba "tela" para el lienzo del Axioma 0 y "la tela ya tejida" para lo que SNT describe.
- **Encabezado del documento.** Deja de subtitularse como marco *de* la Shadow Node Theory. Se declara el alcance real y la independencia de las dos numeraciones.

### Mantenido

- **Integridad de la v33.** La v34 es aditiva. Axiomas 1 al 12 intactos, cláusulas 1 a 5 intactas, cadena operativa original intacta. Ninguna cifra, dominio ni etiqueta de estatus de la v33 cambió de valor. Verificado línea por línea: las 115 líneas de la v33 desde la convención de estatus en adelante están presentes sin parafraseo.

### Pendientes declarados en esta versión

- Eje `u` del Axioma 0.1 sin definición operativa en ningún dominio.
- Campo de fricción `φ` postulado, no medido.
- El piso sigue siendo factor y no variable, lo que acota la cimática del colapso al eje acelera / no acelera.

## [2.6.0] — 2026-09-27

Auditoría, prueba discriminante y reconstrucción del dominio B, revisión r31 del
preprint de SSRN y **pre-registro con cinco pruebas** de la teoría. El corpus de 721
casos no cambia. PR [#42](https://github.com/Inzainos/The-shadow-Node-Theory/pull/42)
a [#46](https://github.com/Inzainos/The-shadow-Node-Theory/pull/46).

> **Nota de trazabilidad.** Las entradas fechadas en julio de 2026 (auditoría
> integral v32 y su runner, prueba discriminante inicial del dominio B y
> `owid-maddison.csv`, parche v31 del marco, validaciones del agente genómico,
> Delta, `.flake8`, `SECURITY.md`, `AGENTS.md`/`CLAUDE.md`) ya estaban en el
> código de la etiqueta 2.5.2, pero su entrada no las listaba; se conservan aquí
> como registro. Lo nuevo de 2.6.0 son las entradas del 26 y 27 de septiembre de
> 2026.

### Documentación
- **Marco v34, nota de auditoría en el Axioma 5** (2026-09-27, a pedido del
  autor): sin cambiar el texto ni la etiqueta ANCLADO, registra que fricción → b
  no es significativo por dominio (ρ = −0.556, p = 0.25), que el n = 714 excluye
  el Dominio D (con D, sin E3 ni B: ρ = −0.145, p = 0.39) y que la prueba
  pre-registrada con dominios nuevos sin COVID no lo respalda (ρ = −0.131,
  p = 0.39); el polo sin fricción (E3) sí es robusto con series crudas. La fila
  del Axioma 5 en la tabla de estatus remite a la nota. Registrado en
  `papers/CHANGELOG_marco.md`.
- **Preprint SSRN r31 en español y notas del formulario** (2026-09-27): nuevo
  `papers/snt_ssrn_v31.md` (+ `.pdf`, `.docx`), traducción completa de la r31 en
  inglés con la tabla de metadatos en español (JEL, palabras clave, datos,
  conflicto de interés); `snt_ssrn_v30.*` queda intacto. Nuevo
  `papers/SSRN_revision_v31.md` con título, resumen (1,877 caracteres), palabras
  clave, JEL y comentarios de revisión listos para el formulario "Revise my
  Submission"; `SSRN_revision_v30.md` queda como registro de lo enviado. La r31
  en inglés incorpora la reconstrucción del dominio B (resumen, §3.5, §9 (iii),
  Hallazgo 4 (c), §15.2–15.3) y corrige tres detalles de la primera redacción:
  "89% significant" → nominal en §9, la redacción del 77/91 (son 77 de los 91
  países que actúan como hub) y §15.1 ("operates across all domains" / "follows a
  power law" → propuesta con salvedades; rango-tamaño pendiente de lognormal).
  PLOS y la figura del ASI de `generate_figures_v29.py` (paquete PLOS) no se
  tocan, por indicación del autor.
- **Preprint SSRN, revisión r31** (2026-09-27): nuevo
  `papers/snt_ssrn_v31_EN.md` (+ `.pdf` y `.docx`); `snt_ssrn_v30_EN.*` queda
  intacto como registro de lo enviado el 2026-06-28. Nota de revisión al inicio
  y cambios, todos con la cifra verificada contra los archivos del repo:
  - **Retirado** "abrupto 5.9× más rápido que gradual" (resumen, §1.3, §2.1,
    §5.1, Hallazgo 3): proviene de 2 vs 2 casos (5.87×, p = 0.33); n = 486 no
    corresponde a ningún conjunto; el corpus activo no tiene disparador.
  - **§6.3 HackerEarth:** ROC-AUC 0.9994 (fuga de datos) → **0.715 ± 0.019**
    (primera sesión, como documenta `code/hackerearth_validation_final.py`).
  - **ASI "precision = 1.0, cero falsos positivos" retirado** (resumen, §9, §10
    RC7, §15.1; nueva §6.6): la etiqueta `soberania` es ASI > 1, así que la
    clasificación es tautológica (verificado: TP 13, FP 0, FN 0 por
    construcción; 13/4,774 = 0.27 %).
  - **Hallazgo 1 (fricción):** tabla por caso / por cluster (ρ −0.556,
    p = 0.25, n = 6) / bootstrap (−0.434, IC95 [−0.722, −0.006]) / sin E3 /
    sin E3 ni B; se deja de llamar "estadísticamente robusto".
  - **Hallazgo 2:** el polo sin fricción son 238 casos COVID-19 (E1 ya no se
    llama "invasión biológica").
  - **Hallazgo 4 (soberanía como freno):** pasa a hipótesis con los resultados
    de la prueba discriminante (nulo calibrado + comercio bilateral COW). La
    frase "b > 1 sin importar el sustrato" pasa a conjetura: 94 de los 102
    casos con b ≥ 1 son series COVID-19 (E1 + E3).
  - **Hallazgo 5 / §9:** AIC en las 18 series crudas (potencia 13, exponencial
    4 con b̄ +1.54, lineal 1); posible mala especificación en b ≥ 1.
  - **§3.3 / §9:** 89 % de significancia marcado como nominal (B: 156/446
    estimables, 33–112 significativos tras AR(1)); reproducibilidad parcial
    (B exacto con MPD2020; E1/E3 crudos ausentes; HackerEarth propietario);
    p truncados (557/721) y dos definiciones de R².
  - **§8 / §14 N-cuerpos:** "confirma el apego preferencial" → consistente con,
    pendiente de comparar contra lognormal (Clauset et al. 2009).
  - **Referencias:** Maddison 2023/2024 → Bolt & van Zanden (2020), MPD2020;
    añadidos Barbieri & Keshk (2016), Barbieri, Keshk & Pollins (2009) y
    Clauset, Shalizi & Newman (2009).
- **`md_to_pdf.py` / `md_to_docx.py`** (2026-09-27): las líneas consecutivas
  forman un solo párrafo (antes cada línea del Markdown era un párrafo, lo que
  dejaba `**` literales en negritas partidas entre líneas), soporte de salto
  duro (dos espacios finales), citas `>` de varias líneas como un párrafo, y
  log en `reconstruction_real/logs/`. El PDF usa DejaVu Sans (sistema o la que
  trae matplotlib): con la Helvetica base-14 el PDF v30 mostraba ρ como "r",
  b̄ como "bn", ≈ como "»" y 10⁻⁹⁷ como "10nnn". El encabezado de las tablas del
  PDF ahora es blanco (antes gris sobre fondo negro, ilegible).
- **Actualización integral de la documentación a la versión actual (release
  2.5.2, marco teórico v34) e integración de los hallazgos de la auditoría v32**
  (2026-09-26). Toda cifra nueva se recalculó desde los datos versionados.
  - `README.md`: marco activo v34 y numeraciones independientes; aviso de estado
    de la inferencia; tabla del corpus con fuentes reales por dominio (E1 =
    OWID COVID-19 *spatial spread*, no invasiones biológicas; C = US Census 23 +
    INEGI 1; F1 = Open Exoplanet + NASA) y significancia marcada como nominal;
    hallazgo central con variantes por cluster/bootstrap/sin E3 (ρ por cluster
    −0.556, p = 0.25, n = 6); columna de estado en los tres hallazgos (5.9× **no
    reproducible**; hallazgo 3 apoyado en el dominio B, **inconcluso**); nueva
    sección *Audit v32 — inference status*; advertencias en N-cuerpos y ASI;
    notas de auditoría en RC1–RC11; árbol del repositorio completo (`audits/`,
    `tests/`, `dashboard/`, todos los scripts); sección de reproducción con
    fuentes por dominio.
  - `AGENTS.md`, `CONTRIBUTING.md`, `dev-guide.md`: marco v34, mapa completo,
    comandos de prueba de regresión y de la auditoría, regla de inferencia
    honesta; `dev-guide.md` alinea `compileall` con el CI (incluye `delta`).
  - `CITATION.cff`: marco v34 y salvedad de inferencia en el resumen (versión
    y fecha de release sin cambio).
  - `reconstruction_real/README.md`: **E2 corregido de 4 a 2 casos** (el corpus
    tiene 2; con 4 el total sumaría 723), fuentes reales por dominio, salvedades
    de integridad (557/721 p truncados, dos R², `trigger` fijo), estado de
    reproducibilidad y lista de archivos.
  - `reconstruction_real/audits/`: sección de seguimiento con la re-verificación
    del 2026-09-26 y aviso fechado en `AUDITORIA_INTEGRAL_v32.md`. **Corrige el
    §5 de la auditoría:** RC9 sí es verificable desde
    `data/orthogonality_crypto_v25.csv` (ρ = +0.009, p = 0.98, n = 11). **Localiza
    el origen del 5.9×:** texto fijo en `code/generate_publication_figures.py` (v28).
  - `sources.md`: encabezados con el conteo activo real y la fuente que usan los
    casos activos (C 24, D 3, E1 4, E2 2, F1 2, F2 1, F3 = Multiplanet; F4 y
    agujeros negros no están en el corpus activo); la bibliografía previa se
    conserva como corpus histórico.
  - `data/FUENTES.md`: estado real por fuente, checksums re-verificados (6/6
    coinciden), bloque del Dominio G actualizado (G03 ajustado).
  - `genomic_agent/README.md` + `SCALING.md`: oráculo de 44 filas / 17
    enfermedades (no 9), baseline empírico de 51 pares / 14 hubs / 11
    cromosomas, árbol con `analysis/` y `hpa_db_builder.py`.
  - **Release de origen del corpus corregida:** el corpus de 721 casos entró en
    **2.4.0** (según la entrada `[2.4.0]` de este CHANGELOG), no en 2.5.0 como
    decían `README.md`, `sources.md` y `CONTRIBUTING.md`; 2.5.0 introdujo la
    capa acoplada ACO-A.
  - `delta/README.md`: tabla de módulos con adaptadores reales y nota sobre el
    prior de fricción. `dashboard/`: versión 2.5.2 (antes 2.4.0/2.5.0) y
    salvedad de la auditoría junto al hallazgo central.
- **Datos:** `reconstruction_real/data/auditoria_integral_v32_resultados.csv`
  regenerado; única diferencia: `data/owid-maddison.csv` pasa de
  `AUSENTE/NO_REPRODUCIBLE` a `PRESENTE/OK`.
- **Estructura de esta entrada:** los ítems de adición que estaban bajo
  *Corregido* (patch v31, validaciones del agente genómico, Delta, `.flake8`,
  `SECURITY.md`, `AGENTS.md`/`CLAUDE.md`) se movieron a *Añadido*.
- Alineación de metadatos y documentación principal con la versión activa
  **2.5.2**: `CITATION.cff`, `README.md`, `reconstruction_real/README.md` y
  `sources.md` distinguen ahora entre el release activo del repositorio, el
  corpus real de 721 casos introducido en `2.5.0` y el marco teórico activo
  **v33**.
- `genomic_agent/README.md`: documenta el baseline empírico (n=40 tejido sano
  TCGA) y las validaciones con pacientes reales (rondas 1/2 + escala 976).
- `README.md`: árbol de archivos de `delta/` actualizado con los adaptadores de
  datos reales (`data_adapters.py`, `run_real_delta.py`).

### Añadido
- **Pre-registro y cinco pruebas de la SNT** (2026-09-27, seis puntos pedidos por el
  autor). Pre-registro `reconstruction_real/preregistro/PREREGISTRO_2026-09-27.md`
  subido (commit `c319fac`) antes de descargar datos o correr pruebas; informe
  `reconstruction_real/audits/RESULTADOS_PREREGISTRO_2026-09-27.md` con desviaciones.
  - **Punto 1, hub variable en el tiempo** (`prueba_hub_temporal.py`): no
    respaldada (H = 20: d mediana −0.009, p = 0.95); H = 30 contraria (p = 0.0002).
    Funciones COW/Maddison compartidas en `comercio_maddison.py` (la reconstrucción
    estática reproduce salidas y log idénticos).
  - **Punto 2, fricción con dominios nuevos sin COVID**
    (`prueba_friccion_dominios_nuevos.py`; E4 mpox, D2 StatCounter, A2 ciudades
    WUP, B-comercio): no respaldada (ρ = −0.131, permutación exacta p = 0.39).
  - **Punto 3, series crudas de COVID** (`covid_E3_series_crudas.py`): receta de E3
    identificada (233/234); Newey-West p < 0.05 en 233/234; E1 no reproducible.
  - **Punto 4, disparadores a ciegas** (`prueba_disparadores_ciudades.py`):
    respaldada (8/8, Wilcoxon p = 0.0039; capitales 5.1×; salvedad de
    supervivencia de WUP).
  - **Punto 5, cohortes ACO-A** (`descargar_binance_klines.py` con reintentos,
    `aco_cohortes_ampliadas.py`): ortogonalidad respaldada por equivalencia (242
    pares, ρ = −0.119); h > 0 respaldada en cripto (663) y bancos FDIC (27,771);
    hazard creciente solo en cripto (confundido con el calendario), bancos en
    bañera; fricción → Δ no ampliable.
  - Subconjuntos versionados de cada fuente nueva y SHA-256 en `data/FUENTES.md`;
    README (RC3 no refutado por prueba pre-registrada; fila de fricción; RC9; hazard)
    e índice de auditorías actualizados.
- **Reconstrucción del dominio B con hub emergente del comercio** (2026-09-27;
  pendiente 9 de la auditoría). Nuevo
  `reconstruction_real/code/reconstruccion_B_hub_comercio.py` (con log) →
  `reconstruction_real/data/dominio_B_hub_comercio.csv` y
  `dominio_B_hub_comercio_intra_nodo.csv`; informe
  `reconstruction_real/audits/RECONSTRUCCION_DOMINIO_B_HUB_COMERCIO.md`. Hub =
  mayor destino de exportación de cada país (COW v4.0, entidades del mismo
  territorio en Maddison 2020) en su primera década de datos; mismo ajuste que
  `expand_B_massive.py`. 102/103 países, 19 hubs; solo 9/102 pares existen en el
  dominio B; 62/95 nodos convergen hacia su hub; hub vs controles con la misma
  brecha: d mediana −0.014, Wilcoxon p = 0.78 (cluster por hub p = 0.62) — **sin
  acoplamiento**; la prueba dentro de cada nodo (ρ parcial mediana +0.115,
  permutación p = 0.15) no es concluyente. Marca de cobertura CMEA dudosa
  (Mongolia, Vietnam: comercio con la URSS faltante en COW; verificado). El
  dominio B del corpus no cambia.
- **Bloques 2–3 de la prueba discriminante del dominio B (comercio bilateral)**
  (2026-09-27). Fuente: Correlates of War Trade v4.0 (`data/COW_Trade_4.0.zip`,
  SHA-256 `c44c4b5c…`). Nuevo `reconstruction_real/code/build_comercio_bilateral_cow.py`
  → `data/comercio_bilateral.csv` (exportaciones direccionales por espejo,
  ventana de cada par, reglas de entidad para URSS / Yugoslavia / Vietnam del
  Norte / Pakistán unificado, fila RESTO_DEL_MUNDO con control exacto de
  totales; log). 432/446 pares. **Acoplamiento SNT no respaldado:** participación
  media nodo→hub ρ = −0.043 (permutación intra-región p = 0.72), R² parcial
  0.0001; participación inicial ρ = −0.185 (cluster por nodo p = 0.022,
  permutación p = 0.026), **signo opuesto** al predicho. Modelo conjunto R²
  0.290 (solo brecha 0.286). El Bloque 2 del script ahora descarta los años con
  exportaciones totales = 0 (share 0/0 indefinido; antes daba `nan`) e informa
  cluster por nodo y región, permutación intra-región y ρ por región. Salida
  `discrim_bloque2_acoplamiento.csv`.
- **Recálculo de "abrupto vs gradual" (cifra 5.9×)** (2026-09-27):
  `reconstruction_real/code/recalculo_trigger_abrupto_gradual.py` →
  `reconstruction_real/data/trigger_abrupto_gradual_recalculo.csv` (con log).
  Recalcula la comparación sobre todos los conjuntos del repo con etiqueta de
  disparador. **Origen del 5.9×:** tabla v1.0 de 2 abruptos vs 2 graduales
  (5.87×, Mann-Whitney p = 0.33). Histórico v2.0 (57 casos): razón 6.3,
  p = 0.053, no citable (7 casos con R² < 0). n = 486 no corresponde a ningún
  conjunto. El corpus de satelización activo (721) no tiene variable de
  disparador. Los 18 casos ACO sí la tienen, pero su b es un **exponente de
  absorción** (R = masa absorbente / masa pico del hub), así que prueban
  RC-ACO-2, no esta afirmación: ahí gradual ≥ abrupto (0.47×, p = 0.10, n.s.;
  permutación intra-dominio p = 0.94; disparador confundido con dominio).
- **RC3 del README pasa de NOT REFUTED a UNTESTABLE** (2026-09-27, decisión del
  autor tras la revisión): la prueba publicada no es reproducible y el corpus
  activo no puede evaluarla. Se agrega una nota de numeración: el RC3 del
  README (abrupto vs gradual) no es el RC3 del marco v30 / SSRN v30 EN
  (inextractabilidad cualitativa) ni el del SSRN v30 ES §2.3 (convergencia
  espontánea). **Pendiente del autor:** el resumen del preprint SSRN v30 EN
  (en revisión) afirma la cifra 5.9× y su estabilidad "57 → 114 → 721".
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
  hacia H-CONVERGENCIA sin cerrarla. **Bloque 1 corrido (2026-07-25) con
  `data/owid-maddison.csv` real, contra su nulo correcto: INCONCLUSO
  (confundido).** El Spearman `b` vs brecha inicial `log(PIB_hub/PIB_nodo)` =
  −0.4725 (n=441) *parecía* respaldar convergencia contra cero, pero brecha y `b`
  salen del mismo ajuste y el hub se asigna por PIB promedio → anticorrelación por
  construcción. El **nulo que corresponde es sintético calibrado al Maddison real
  (Bloque 1d):** deriva +0.0215, volatilidad 0.0647, nivel inicial log media 7.804
  sd 0.670, n=446, semilla 20260725. Da media −0.4244, IC95 [−0.5796, −0.2608]
  para el test completo y −0.2465, [−0.4132, −0.0902] para el partido. **Los dos
  observados (−0.4725 y −0.3676) caen DENTRO del nulo → no hay señal por encima
  del artefacto de asignación de hub**, ni en el test completo ni en el de datos
  disjuntos (1c). El Bloque 1b (re-emparejamiento, media −0.57) NO es un nulo
  válido —conserva el mecanismo que se quiere aislar— y se conserva sólo como
  observación aparte. **Conclusión:** el dominio B no queda respaldado ni como
  β-convergencia ni como acoplamiento SNT; lo único firme (sin supuestos ni
  nulos) es el Bloque 0 (85% de dualidad de rol hub/satélite). Se añaden Bloques
  1b/1c/1d al script (`--n-placebo`) y las salidas
  `discrim_bloque1_convergencia.csv` / `discrim_bloque1c_split.csv`. **Corrige la
  redacción de dos commits previos de esta rama** ("RESPALDADA" primero, y luego
  la justificación vía el nulo 1b inválido). Bloque 2 (comercio bilateral) sigue
  sin correrse: reconstruir el dominio con un hub emergente, no rescatarlo.
- **`data/owid-maddison.csv`** — descargado del grapher OWID
  `gdp-per-capita-maddison` (Maddison Project Database, cobertura 1–2022, 178
  entidades; CC BY 4.0). Cierra el hallazgo de reproducibilidad #7 de la
  auditoría v32 para el dominio B. Provenance (URL, fecha, SHA-256) en
  `data/FUENTES.md`.
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

### Corregido
- **Prueba discriminante del dominio B re-corrida con la edición del corpus**
  (2026-09-27). La corrida original usó la edición OWID posterior (441 pares).
  Con MPD2020 (446 pares) y 5000 iteraciones de los nulos: Bloque 1 ρ = −0.4893
  vs nulo calibrado −0.4226 [−0.5765, −0.2418] → DENTRO (p empírico 0.213);
  Bloque 1c ρ = −0.3846 vs −0.2508 [−0.4050, −0.0788] → DENTRO **en el límite**
  (p empírico 0.050, margen 0.020). **Veredicto con el criterio IC95: sigue
  INCONCLUSO**; el test limpio se acerca a β-convergencia (p 0.080 → 0.050).
  El script ya no imprime "VEREDICTO H-CONVERGENCIA: RESPALDADA" por la
  comparación contra cero (declarada inválida): calcula el veredicto contra el
  nulo calibrado (`veredicto_nulo_calibrado`), usa MPD2020 por defecto y acepta
  `--omitir-1b`. Salidas `discrim_bloque1_convergencia.csv` y
  `discrim_bloque1c_split.csv` regeneradas con MPD2020.
- **Filas fijas del runner de la auditoría v32** (2026-09-27).
  `dominio_B_regenerable` era un literal (`NO`) escrito cuando faltaba
  `owid-maddison.csv` y nunca comprobaba nada; ahora el runner regenera el
  dominio B en un directorio temporal con cada script constructor y lo compara
  caso a caso: `expand_B_massive.py` → 441 vs 446 casos, corr(b) = 0.979,
  12/408 b idénticos (`PARCIAL`); `expand_dominio_B.py` → 254 casos
  (`PARCIAL`). La fila de RC9 (fija en `NO_REPRODUCIBLE`) ahora se calcula desde
  `orthogonality_crypto_v25.csv` (ρ = +0.009 → `REPLICA`). *(Esa medición usó la
  edición OWID posterior; con la edición del corpus, MPD2020, la reproducción
  es exacta — ver "Dominio B: edición de Maddison identificada" abajo.)*
- **Script regenerador del dominio B mal atribuido.** README,
  `reconstruction_real/README.md`, `DOMINIO_B_METODOLOGIA.md` y
  `data/FUENTES.md` decían que `expand_dominio_B.py` reproduce los 446 casos;
  produce 254. El que genera el dominio es `expand_B_massive.py`. El `trigger`
  fijo en `'gradual'` está en ambos scripts.
- **Dominio B: edición de Maddison identificada y fijada; reproducción exacta**
  (2026-09-27). La edición del corpus nunca se había fijado: era el **Maddison
  Project Database 2020** (cobertura 1–2018), no la 2023 que citaban README,
  `sources.md` y `CITATION.cff`. Se buscó en Google Drive del autor (solo estaba
  `mpd2023_web.xlsx`) y se descargó la 2020 de la GGDC. Nuevo
  `data/mpd2020.xlsx` (SHA-256 `d20853c2…`) y
  `reconstruction_real/code/build_maddison_mpd2020_csv.py` →
  `data/maddison_mpd2020.csv` (nombres OWID por ISO3; "Sudan (Former)" →
  "Sudan"). Con ella `expand_B_massive.py` reproduce los 446 casos **byte a
  byte** (SHA-256 idéntico, 19 columnas iguales). `expand_B_massive.py` acepta
  `--maddison`/`--salida` y por defecto lee la edición fijada; el runner de la
  auditoría verifica la reproducción exacta (`REPLICA`) y mide la sensibilidad
  a la edición OWID posterior (`PARCIAL`, 441 vs 446). Citas corregidas de 2023
  a 2020 en README, `reconstruction_real/README.md`, `sources.md`,
  `DOMINIO_B_METODOLOGIA.md`, `data/FUENTES.md` y `CITATION.cff`. No fue
  necesario re-publicar B.
- **Dashboard:** las 16 llamadas con `use_container_width=True` (deprecado)
  pasan a `width="stretch"`; verificado con Streamlit 1.58.0 (versión del
  despliegue en Hugging Face) y 1.64.0: 6/6 páginas, 0 excepciones, 0 avisos.
- **Provenance y circularidad (higiene de la auditoría v32).** `data/FUENTES.md`
  ancla las fuentes externas (Maddison Project y OWID COVID) con URL, edición,
  fecha y SHA-256, y documenta que `data/owid-maddison.csv` está **ausente** en
  el repo (por eso el dominio B, 62% del corpus, no se regenera clonando).
  `data/snt_asi_scores_README.md` marca la columna `soberania` como **umbral de
  ASI** (separación perfecta ASI>~1), advirtiendo que usarla como target sería
  circular por construcción (solo 13/4,774 = 0.27% positivos).

### Cambiado
- `dashboard/requirements.txt`: `streamlit>=1.58.0` (antes `>=1.30.0`, que no
  garantiza el parámetro `width`); `.gitignore`: ignora `reconstruction_real/logs/`.
- Estado de publicaciones: revisión v30 de **PLOS Complex Systems** (PCSY-D-26-00059)
  enviada; ponencia **MIT GCFP** (13ª conferencia anual) enviada.
- CI: el paso de `flake8` ahora lee su configuración desde `.flake8` en vez de
  pasar las banderas `--select`/`--exclude` inline.

## [2.5.2] — 2026-09-10

[Release en GitHub](https://github.com/Inzainos/The-shadow-Node-Theory/releases/tag/2.5.2) ·
PR [#37](https://github.com/Inzainos/The-shadow-Node-Theory/pull/37) +
[#38](https://github.com/Inzainos/The-shadow-Node-Theory/pull/38)

### Añadido
- **Dominio G — Paquetes cósmicos / desempaquetado de vida** (`reconstruction_real/code/build_dominio_G.py`,
  `data/snt_corpus_dominio_G.csv`, `data/snt_corpus_dominio_G_fuentes.md`,
  `data/snt_corpus_dominio_G_ajustes_complementarios.csv`). Primer puente entre
  el marco teórico v33 (Axiomas 1 y 8) y el aparato ACO-A. 5 casos con
  metadatos y citas primarias (4 verificadas en sesión). Registra una relación
  transversal candidata (ratio purina/pirimidina vs amoníaco entre Ryugu,
  Bennu y Orgueil) sobre el eje del receptor (Axioma 2), no ajustada — n limpio
  con ambas variables = 2, sigue sin ajustar.
- **G03 Bennu — primera serie real poblada (n = 3).** Fuente: Mojarro A. et al.
  (2025), PNAS 122(49) e2512461122, Table 2 (datos crudos en Astromat). Tres
  piedras de Bennu, mismo protocolo, medición única por piedra:
  t = ΣC1-alquilnaftalenos/fenantreno (proxy de alteración acuosa),
  R = fracción de los 20 α-aminoácidos proteicos detectados.
  Puntos: angular (8.6, 11/20), hummocky (9.4, 8/20), mottled (17, 4/20).
  Ajuste principal: **b = -1.371, R² = 0.931, p = 0.123, n = 3**
  (no significativo al 5 %; 1 grado de libertad). Complementarios:
  sensibilidad con el agregado (excluido por los autores por sesgo de masa,
  punto medio 8.1, 15/20): b = -1.587, R² = 0.846, p = 0.042, n = 4;
  forma ACO-A A = 1 − div/15: Δ = +1.223, R² = 0.869, p = 0.296, n = 3.
  Signo del exponente coherente con la lectura de los autores ("α-amino acid
  diversity decreased with increasing ΣC1-Np/Ph") y con el modo "regulado"
  de ACO-A (ley de potencia suave, exponente negativo, como en astro).
- Cifras de Glavin et al. (2025, Nat. Astron.) agregadas a G01/G02/G03/G04
  (mismo protocolo hot-water): aminoácidos C2–C6 Murchison 250, Bennu ~70,
  Ryugu 15 nmol/g; purina/pirimidina Bennu 0.55, Orgueil ~1.1, Murchison
  ~2.8; amoníaco Bennu 13.6 µmol/g (12× Murchison, 75× Ryugu). GX01 sigue
  sin ajustar: n limpio con ambas variables = 2.
- **Marco teórico v33 — marco conceptual con base** (`papers/marco_teorico_v33.md`,
  `papers/CHANGELOG_marco.md`). v32 íntegra + **Axioma 0: tela de incertidumbre**
  (capa FUNDAMENTAL: vacío cuántico + fondo estocástico de ondas
  gravitacionales; no medible por SNT ni pretende serlo; relación con
  `h(τ) > 0` escrita como lectura de compatibilidad, no derivación) + etiqueta
  de estatus en cada axioma (FUNDAMENTAL 0; ANCLADO 4, 5, 10; INFRAESTRUCTURA
  1, 8; CONCEPTUAL 2, 3, 6, 7, 9, 11, 12) + cavidad/modos propios como
  vocabulario del Axioma 2 (Schumann como caso medido) + cimática como
  evidencia del Axioma 12 + cadena operativa renumerada 0–8 + cinco cláusulas
  metodológicas (metáfora vs validación; etiquetas visibles; Dominio G no es
  evidencia hasta n≥3; marco y paper empírico separados; capa humana fuera del
  cuerpo axiomático) + nota fechada bajo Axioma 8 con el resultado de G03.

### Cambiado
- Versión activa: **2.5.2**. `README.md`, `AGENTS.md` (marco teórico v33
  activo) y `data/FUENTES.md` (bloque Dominio G regenerado) actualizados.
  El corpus de 721 casos y los 18 casos ACO no cambian. Etiqueta de estatus
  del Axioma 8 **sin cambio** (INFRAESTRUCTURA) hasta decisión del autor.

### Nota metodológica
- n = 3 es el mínimo que `fit_power_law` acepta. R es un conteo de diversidad
  (entero de 0 a 20), no una concentración; una sola medición por piedra; los
  autores advierten heterogeneidad a masas < 1 mg. El ajuste existe y es
  real; su peso inferencial es bajo. La regla 3 de v33 ("G no es evidencia
  hasta n ≥ 3") se cumple en su umbral literal, no en su espíritu.

### Nota de nomenclatura
- Existen dos "v32" no relacionadas: el marco teórico v32 (fusión v31 + marco
  conceptual, 2026-07-24, no versionada en el repo) y `AUDITORIA_INTEGRAL_v32.md`
  / `snt_utils_v32.py` (auditoría estadística del corpus). Los items de
  `[No publicado] — 2026-07` no se incluyen en 2.5.2 hasta decisión del autor.
  Nota histórica: este trabajo se integró a `main` en dos PRs consecutivos
  (esqueleto del Dominio G + marco v33, y luego el ajuste de G03); ambos
  quedan bajo esta única entrada y etiqueta `2.5.2`, sin release `2.5.1`
  separado en GitHub.

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
> **no deben citarse en publicaciones académicas**. La versión activa es la v2.5.2.
