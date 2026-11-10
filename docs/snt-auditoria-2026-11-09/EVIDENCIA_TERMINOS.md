# Auditoría de evidencia — terminología mezclada en la Shadow Node Theory (SNT)

**Fecha:** 2026-11-09
**Solicitada por:** Elán Zainos Corona (dueño de la teoría), vía el agente principal.
**Motivo declarado por Elán:** un agente inventó el término "luz/light" — él nunca definió "luz" en la teoría; estaban hablando del Shadow Node y el agente interpretó cosas. Hay que auditar qué términos se están mezclando que no existen en la teoría desde el inicio.
**Naturaleza de este archivo:** SOLO EVIDENCIA. No se modificó el espacio ni ningún archivo de la teoría ni de los derivados. No se emite veredicto de "remover" o "integrar" — eso lo decide el agente principal con Elán. Las valoraciones de conflicto ("ALTO/MEDIO/BAJO") son una lectura de la evidencia, no una orden.

## 0. Método y alcance

**Fuente canónica:** `Inzainos/The-shadow-Node-Theory` (clon, v2.7.5.1, marco v34): `README.md`, `CHANGELOG.md`, `docs/DOMINIOS.md`, `docs/HISTORIA.md`, `CASOS_DE_USO.md`, `AGENTS.md`, `papers/marco_teorico.md` (v34) y barrido completo del repo con `grep -rniE` (excluidos `.git`, `Legacy/`, `archive/`; los hallazgos en `Legacy/`/`archive/` y en `marco_teorico_v30.md` se señalan aparte porque son versiones supersedidas).

**Materiales derivados revisados:**
- Espacio SNT (slug `shadow-node-theory`): respaldo `space-index-backup-2026-11-07.html` (respaldo local del espacio) (§1–§15) **más la inspección del espacio en vivo** (`artifact.inspect`, ID `594ee4d2-9151-4031-b94a-0bca4e4adee9`, resultado recibido 2026-11-09 ~10:33): texto renderizado completo vigente (1.071 líneas, auditoría 2026-11-09T05-15-46Z, index.html v2.7.5.1 / marco v34). La inspección **confirma** la evidencia del respaldo: "luz", "puente" y "ficha" aparecen solo en la sección Ueno; "light" solo como sufijo `_light.png`; "bridge"/"flow" cero ocurrencias visibles. Añade dos hallazgos que el respaldo no distinguía: "satélite" solo 2 ocurrencias en el texto visible, y "tono" en dos acepciones sin desambiguar (ver §3.14 y §3.15). Limitación del inspector: sin herramienta de shell, los términos ubicuos se reportan con citas representativas, no con cifras exactas; no comparó contra el repo GitHub ni el agente de Kaggle (esa comparación es este archivo).
- `taxonomia-por-dominio.md` (archivo local de trabajo) (193 líneas) — documento origen de la plantilla.
- `finanzas-mundo-snt.md` (archivo local de trabajo), `estado-snt.md`, `DOMINIOS.md`, `modelo-ueno-resultados-v2.md`, `forecast-ueno-2026-11-06.md`, `rastro-del-dinero-ueno.md`, `linkedin-estrategia-reels.md`, `taxonomia-721-casos.md`.
- `snt_agent.py` (agente SNT de Kaggle, local), `kaggle-agente-informe.md`, `snt-agente.ipynb`, `salida-snt/informe-finanzas_mundo.md`, `salida-snt/informe-estado.md`, `salida-snt/informe-salud.md`.
- `report.md` (nota local de investigación, 2026-11-08) (§16–§20) y `libro-completo.txt` (solo barrido de "luz", como control).
- `kaggle-genomico-informe.md` (archivo local de trabajo), `genomico-agent-core.py`.
- `~/memory/2026-11-07.md` (solo como evidencia de la cadena de atribución; no como fuente de la teoría).

**Conteo:** los números de "ocurrencias" son coincidencias de palabra con `grep -ciE` (insensible a mayúsculas). Incluyen usos genéricos (p. ej. "flujo mensual" = cash-flow). Cada cita clave se verificó leyendo la línea; los conteos son orientativos, las citas son la evidencia.

---

## 1. Inventario canónico — lo que la teoría define de verdad

Fuente: repo v2.7.5.1, marco v34. "Archivo" = dónde aparece la definición.

| Término | Definición en el repo | Archivo |
|---|---|---|
| `R(t)` | `R(t) = métrica_del_hub / métrica_del_nodo`, resumida —cuando los datos lo permiten— por `R(t) = a·t^b`. Capa 1. | `README.md:7-8, 25-26` |
| ACO-A | `A(τ) = c·τ^Δ`. Colapso orbital acoplado: absorción posterior a ciertos colapsos. Capa 2. | `README.md:10, 30` |
| φ (fricción) | Campo de fricción: `φ: 𝒞 × T → ℝ⁺`, flujo `-∇_γ φ`. Axioma 0.1. **Estatus: postulado, no medido** ("la fricción está postulada por dominio, no medida como campo continuo"). | `README.md:33-34`; `papers/marco_teorico.md:120`; `CHANGELOG.md:31, 300` |
| Tela de incertidumbre | 740 trayectorias: 699 series reales versionadas + 41 sombras. LOO dominio 50.7%, tono 66.2%. Capa 4. | `README.md:38-39` |
| Tela simática / cimática | Representación cimática de patrones de resonancia entre dominios (analogía de forma; cláusula anti-metáfora en Axioma 12). Capa 5. | `README.md:43-46`; `papers/marco_teorico.md:303-312` |
| ASI | Índice de Soberanía Atómica: `ASI = δH · α / F`. Umbral ASI > 1 define soberanía; en HackerEarth el umbral se recalibró 0.5 → 0.167. | `README.md:48-49, 329-341` |
| Muro de 5 eventos / 5-Event Wall | Umbral crítico en dominios digital y genómico: <5 tipos de evento distintos → >90% probabilidad de churn; en TCGA, 2-5% de pacientes con ≥5 eventos hub simultáneos. | `README.md:131-132, 343-344` |
| leapfrog | Lectura descriptiva de `b < 0`: "Convergencia / leapfrog" (el nodo gana terreno relativo). | `README.md:302` |
| Nodo Hub | "Absorbe energía productiva residual y aumenta masa gravitacional." | `README.md:312-313` (Módulo 0, Definiciones nodales) |
| Nodo Sombra | "Producción extraída sistemáticamente, divergencia progresiva." | `README.md:314` |
| Proximidad Crítica | "Umbral de extracción > regeneración." | `README.md:315` |
| Taxonomía 5 niveles | Nivel 0 Macro-Hub Central; Nivel 1 Atractores Secundarios; Nivel 2 Bypass Logístico; Nivel 3 Nodos Sombra Profundo; Nivel E Exógeno. | `README.md:317-327`; marco v30 §2.0 |
| Nodo Atómico | RQ recursos cuantitativos extractables, RL cualitativos inherentes. | `README.md:329-330` |
| Eje `u` | Cubo ontológico `𝒞(u, m, τ)`; "El eje `u` no tiene definición operativa y no se rellena con un proxy." | `README.md:230` |
| sombra (Axioma 0.2, v34) | "Una **sombra** es la imagen de `𝒞` bajo un operador de **proyección** `Π_θ` con marco de medición `θ` declarado." Estatus: OBSERVABLE (agregado v34). | `papers/marco_teorico.md:144-146` |
| 41 sombras (tela) | Casos sin serie temporal cruda versionada; "las sombras no amplían el corpus de casos reales". | `README.md:39, 175`; `docs/DOMINIOS.md` |
| Radio / Ratio de Roche | "Entrada al radio de Roche → colapso abrupto, Δ negativo, A(τ) decreciente"; "Ratio de Roche, ventanas cortas de colapso vs ventanas largas régimen superlineal." Sin operacionalización C/R/S en el repo. | `README.md:52, 370` |
| Dominios | A Ciudades, B Países, C Estados EEUU, D Digital/HackerEarth, E1 Territorial, E2 Depredador-presa, E3 Epidémico, F Planetario, G Geoquímica (Bennu), ACO Colapsos. | `README.md:170-186`; `docs/DOMINIOS.md` |
| flujo (sentido 1) | Flujo gradiente del campo φ: `-∇_γ φ` ("el colapso sigue el flujo que minimiza la fricción integrada"). | `README.md:34`; `CHANGELOG.md:31, 300` |
| flujo (sentido 2) | Flujo compuesto de la taxonomía v2.0: `Flujo_total = w(Nivel 3 → Nivel 1) + w(Nivel 3 → Nivel 0)`, con `w_ij = PIB_pc,j − PIB_pc,i`. | `README.md:324` (tabla Nivel 3) |
| puente (sentido repo) | Dominio G: "Se declara como puente construido, no como evidencia." (Infraestructura metodológica, no evidencia empírica.) | `papers/marco_teorico.md:56, 329`; `CHANGELOG.md:1417` |
| tono (φ) | Tono nominal de φ en la tela (LOO tono 66.2%). φ sigue siendo categórica/postulada, no variable física medida. | `README.md:39`; `docs/DOMINIOS.md` |

### 1.1 Lo que NO existe en el repo (barrido completo verificado)

- **"luz" como término teórico: NO EXISTE.** Cero ocurrencias en `README.md`, `docs/DOMINIOS.md`, `docs/HISTORIA.md`, `CASOS_DE_USO.md`. Sus únicas apariciones en todo el repo activo son:
  - `papers/marco_teorico.md:165` — metáfora dentro del Axioma 0.2: *"cambiar solo resolución y umbral no es mover la luz, es enfocar la misma sombra"* (la "luz" ahí es el marco de proyección θ, no un observable ni un costo).
  - `CHANGELOG.md:985` — nombres de archivo de figuras `figures/snt_v260_fig*_{light,dark}.png` (tema claro/oscuro).
  - `reconstruction_real/code/generate_readme_figures.py:57` — paleta de colores `"light"`.
  - `reconstruction_real/code/md_to_docx.py:97` — estilo `"Light Grid Accent 1"`.
  - `reconstruction_real/code/collapse_multidomain.py:15` — "NASA IRSA ZTF light-curve API" (curva de luz astronómica, dato).
  - `papers/marco_teorico_v30.md:657, 671, 1969` — narrativa astronómica ("años luz", "la luz de esta kilonova brilla roja", "sin luz solar") y su traducción inglesa. v30 está supersedida por v34.
  - `Legacy/code/snt_corpus_astronomical.py:282` — "curva de luz" (Legacy, supersedido).
- **"puente" como rol conector hub↔sombra que cobra por traducir: NO EXISTE.** Solo el sentido "puente construido" (Dominio G, arriba) y la categoría de dato `"web-bridge"` en `reconstruction_real/data/deriva_forma_por_caso.csv:1464` (npm).
- **"ficha (por nodo)" y sus categorías: NO EXISTEN.** Cero ocurrencias de "ficha" en todo el repo activo. Cero "simbionte". Cero "hiberna". "Parásito" solo como "parásito-huésped" (etiqueta del dominio E3 en los manuscritos SSRN v31/v32/v33, p. ej. `papers/snt_ssrn_v33.md:314`). Las categorías de naturaleza (simbionte, parásito, depredador paciente) y de patrón (acumula, distribuye, extrae, replica, hiberna) no aparecen en el repo.
- **"R-análogo": NO EXISTE.** "Análogo" aparece solo en otros sentidos (p. ej. `papers/marco_teorico.md:244`: "concepto análogo a F de ACO-A"; cláusula anti-metáfora del Axioma 12).
- **Roche-C / Roche-R / Roche-S (operacionalización): NO EXISTEN.** El repo no define esos tres ratios. Nota adicional: `CHANGELOG.md:726-729` registra la **retirada de la etiqueta "Roche Radius"** como régimen de `b > 1` (RC1, 2026-10-02): el enum `ROCHE_RADIUS` de `delta/snt_market_core.py` pasó a `UNCLASSIFIED_B_GT_1`.
- **"micelial / red micelial": NO EXISTE en el marco activo (v34) ni en el README.** Antecedente solo en v30 (supersedida): "Red Fúngica: ecosistema de información vivo y distribuido… el hub central es el micelio principal y los nodos sombra son los capilares de extracción" (`papers/marco_teorico_v30.md:1343`); "Nodo Orquestador — Nivel 2 (Micelio / DAG)" (`:847`).

---

## 2. Tabla de ocurrencias — dónde aparece cada término en los materiales derivados

### 2.1 Resumen de conteos por archivo (coincidencias de palabra, `grep -ciE`)

| Archivo | luz/light | flujo/flow | puente/bridge | sombra/shadow | hub | nodo | ficha |
|---|---|---|---|---|---|---|---|
| **Repo canónico** (README+CHANGELOG+docs) | 1* | — | 1† | canónico | canónico | canónico | **0** |
| `papers/marco_teorico.md` (v34) | 1‡ | — | 3§ | 12 | 3 | — | 0 |
| `snt-taxonomia/taxonomia-por-dominio.md` | 8 | 10 | 9 | 19 | 15 | 5 | 4 |
| `snt-taxonomia/taxonomia-721-casos.md` | 21 | 29 | 22 | 39 | 59 | 43 | 6 |
| `snt-taxonomia/finanzas-mundo-snt.md` | 13 | 19 | 4 | 10 | 18 | 8 | 3 |
| `snt-taxonomia/estado-snt.md` | 15 | 43 | 5 | 15 | 23 | 8 | 1 |
| `snt-taxonomia/modelo-ueno-resultados-v2.md` | 2 | 0 | 0 | 1 | 6 | 0 | 0 |
| `snt-taxonomia/forecast-ueno-2026-11-06.md` | 0 | 1 | 0 | 1 | 9 | 1 | 0 |
| `snt-taxonomia/rastro-del-dinero-ueno.md` | 0 | 0 | 0 | 2 | 2 | 0 | 0 |
| `snt-taxonomia/linkedin-estrategia-reels.md` | 3 | 1 | 0 | 8 | 4 | 5 | 0 |
| `snt-taxonomia/DOMINIOS.md` | 0 | 0 | 0 | 0 | 4 | 1 | 0 |
| `kaggle-snt/snt_agent.py` | 39 | 18 | 14 | 17 | 28 | 32 | 3 |
| `kaggle-snt/kaggle-agente-informe.md` | 10 | 2 | 5 | 5 | 7 | 6 | 0 |
| `kaggle-snt/snt-agente.ipynb` | 4 | — | — | — | — | — | — |
| `kaggle-snt/salida-snt/informe-finanzas_mundo.md` | 17 | 2 | 1 | 1 | 3 | 4 | 0¶ |
| `kaggle-snt/salida-snt/informe-estado.md` | 20 | 2 | 1 | 1 | 7 | 4 | 0¶ |
| `kaggle-snt/salida-snt/informe-salud.md` | 3 | — | — | — | — | — | — |
| `research_notes/.../report.md` (§16–§20) | 2# | 2 | 4 | 4 | 5 | 2 | 0 |
| `kaggle-genomico/kaggle-genomico-informe.md` | 0 | 0 | 0 | 0 | — | — | 0 |
| `kaggle-genomico/genomico-agent-core.py` | 0 | 0 | 0 | 0 | — | — | 0 |
| Espacio SNT, respaldo 2026-11-07 (§1–§15) | 11 | 27 | 9 | 89 | 95 | 59 | 2 |
| Libro SUDO UNIVERSE (`libro-completo.txt`, control) | 8** | — | — | — | — | — | — |

\* La 1 en CHANGELOG es `figures/snt_v260_fig*_{light,dark}.png` (tema). README: 0.
† La 1 en CHANGELOG es "Primer puente entre el marco teórico v33 y el aparato ACO-A" (Dominio G).
‡ La 1 en marco v34 es la metáfora de `marco_teorico.md:165` (ver §1.1).
§ Las 3 en marco v34 son el sentido Dominio G ("puente construido, no evidencia").
¶ "Fichas por nodo" aparece como encabezado de sección en las salidas del agente (p. ej. `snt_agent.py:1123` genera `## 4. Fichas por nodo`); el conteo 0 es solo por el singular "ficha".
\# Las 2 en `report.md` son "años luz" (distancia astronómica).
\** Las 8 del libro: "años luz" (2×), "luz solar" (2×), "luz de la Macro-Espiral", "luz del Teseracto", "Interacción luz-materia" (2×). Ninguna es un término SNT.

Notas de control: `snt-taxonomia/DOMINIOS.md` es **byte-idéntica** a `snt-repo/docs/DOMINIOS.md` (`diff` sin diferencias) — copia limpia, sin contaminación de la plantilla. El agente genómico **no usa** la plantilla (0 ocurrencias en informe y código).

### 2.2 Citas textuales por término (archivo:línea — cita exacta)

#### LUZ
- `taxonomia-por-dominio.md:9-10` — *"Por dominio, 4 definiciones: flujo, luz (qué cuesta estar visible), hub (concentra el flujo, tiene licencia o legitimidad, punto único de falla), sombra (mueve el mismo flujo sin pagar la luz, pegada al hub). Puente: conecta hub con sombra y cobra por traducir."*
- `taxonomia-por-dominio.md:3-5` (fuente declarada del documento) — *"Fecha: 2026-11-06. Fuente: repo Inzainos/The-shadow-Node-Theory v2.7.5.1 (docs/DOMINIOS.md, papers cripto y México, espacio SNT) + definiciones de Elán en chat 2026-11-06 (finanzas, Estado, medios, salud, energía) + aplicación independiente EFIPEM."*
- `finanzas-mundo-snt.md:12` — *"Este documento somete Finanzas-mundo a la SNT con la plantilla por dominio (flujo, luz, hub, sombra, puente) y la ficha por nodo (origen, posición, naturaleza, patrón), usando como molde el caso Ueno…"*
- `finanzas-mundo-snt.md:47-49` — *"## 3. LUZ: qué cuesta estar en regla, y quién la paga / La luz en Finanzas-mundo es el capital, las provisiones y la distancia a la insolvencia."*
- `finanzas-mundo-snt.md:58` — *"**La luz que se deja de pagar es la provisión:** 22 países provisionan menos del 40% de su morosidad, y 5 menos del 25%…"*
- `estado-snt.md:53-55` — *"## 3. LUZ: qué cuesta estar en regla, y quién la paga / La luz en Estado es licitar, rendir cuentas y dejar trazabilidad."*
- `estado-snt.md:150` y `:158` (fichas) — *"**Naturaleza:** no paga la luz. **Patrón: extrae.**"*
- `modelo-ueno-resultados-v2.md:159` — *"φ no es una métrica con unidad; es la **trazabilidad normativa** del desplazamiento: qué actos retiraron luz, cuándo, con qué observable."*
- `modelo-ueno-resultados-v2.md:169` — *"Las φ son **causas formales**: cada paso retiró luz."*
- `snt_agent.py:73-75` — *"Cada dominio define: flujo, luz, hub, sombra, puente (definiciones de Elán + repo v2.7.5.1); cómo se construye su R-análogo; sus umbrales de banda (del propio dominio); sus umbrales de luz; y qué le falta (gaps)."*
- `snt_agent.py:84-85` — *`"luz": "Capital regulatorio (Basilea 8%), capital/activos, provisiones/morosidad, Z-score (distancia a la insolvencia)."`*
- `snt_agent.py:120-122` — *`"luz": "Licitar (modalidad competitiva), rendir cuentas (ejecución del PGN), dejar trazabilidad (registro DNCP completo, oferentes, fecha de firma del contrato)."`*
- `snt_agent.py:531-534` — *"-> tabla nodo×tiempo con tasa = morosidad % y luz por país."*
- `kaggle-agente-informe.md:111-112` — *"**Corregido:** el fixture ahora incluye luz por entidad-año (competitiva %, oferente único %, ejecución PGN %) con las mismas definiciones del script original."*
- `kaggle-agente-informe.md:48` — *"Si falta algo, devuelve DATOS [INSUFICIENTES]"* (contexto: la puerta de suficiencia exige, entre otras cosas, un proxy de luz; ver `:41-43`: *"sin proxy de luz por nodo"*).
- `salida-snt/informe-finanzas_mundo.md:64-67` — *"**Naturaleza:** parásito (por observables: luz no pagada) / **Patrón:** extrae (no paga la luz) / **Luz no pagada:** capital_activos_pct 4.86 < alerta 5.0 (2020); provisiones_morosidad_pct 25.6 < alerta 40.0 (2009)"*
- `taxonomia-721-casos.md:67` — *"**Luz:** GAP. El corpus no define qué cuesta estar visible en este dominio: no hay variable de costo (ni licencia, ni registro, ni tributo) para las ciudades del corpus."* (El mismo "Luz: GAP" se repite en `:93, :118, :160, :179, :198, :217` para B, C, D, E1, E2, E3, F.)
- `taxonomia-721-casos.md:141` — *"**Luz:** GAP en los términos del corpus. Lo más cercano son los componentes del ASI (diversidad de problemas δH, autonomía α, caos interno F), que miden soberanía, no el costo de estar visible. No se fuerza la equivalencia."*
- `linkedin-estrategia-reels.md:26` — *"Qué es un nodo sombra, qué es un hub, qué es la luz (lo que cuesta estar en regla, distinto por dominio)."*
- Espacio, respaldo `:1211` — *"La corrección de fondo de la noche: una taxonomía universal para todo era el error. El esqueleto — flujo, luz, hub, sombra, puente — se mantiene; lo que segmenta es cada dominio, porque **la sombra se define por lo que cuesta la luz en ese dominio**, y la luz cuesta distinto en cada uno."*
- Espacio, respaldo `:1217, :1227, :1238, :1248, :1258` — definiciones de Luz por dominio (Finanzas: *"Capital, provisión, auditoría, cuota al FGD, límite a partes relacionadas"*; Estado: *"Licitar, rendir cuentas, dejar trazabilidad"*; Medios: *"Dar la cara, firmar, asumir responsabilidad editorial, exponerse a demandas"*; Salud: *"Protocolo, registro sanitario, trazabilidad del medicamento"*; Energía: *"Concesión, tarifa regulada, despacho. Solo la luz está definida en este dominio."*).
- Espacio, respaldo `:1524` — *"Medir la luz (licitar, rendir cuentas) y detectar su ausencia."*

#### FLUJO
- `taxonomia-por-dominio.md:9` — ver cita de LUZ (flujo = primera de las 4 definiciones por dominio).
- `finanzas-mundo-snt.md:24` — *"| **Flujo** | Dinero y crédito entre países y dentro de cada sistema bancario: crédito al sector privado (% PIB), crédito/depósitos, morosidad (la parte dañada del flujo), reservas totales (el stock acumulado) |"*
- `finanzas-mundo-snt.md:32` — *"El flujo es dinero y crédito."*
- `finanzas-mundo-snt.md:45` — *"**La morosidad es el flujo dañado, no el flujo.**"*
- `estado-snt.md:24` — *"| **Flujo** | Fondos públicos contratados: valor licitado (tender) y valor adjudicado (award) por entidad compradora, en guaraníes |"*
- `estado-snt.md:32` — *"El flujo son los fondos públicos contratados."*
- `snt_agent.py:81-83` — *`"flujo": "Dinero y crédito: crédito al sector privado (% PIB), crédito/depósitos, morosidad (la parte dañada del flujo), reservas totales (el stock acumulado)."`*
- `forecast-ueno-2026-11-06.md:279` — *"**Haberes mensuales de los 32.000 jubilados** | Sin ellos no se cuantifica el flujo mensual de la reasignación"* (uso genérico: cash-flow, no plantilla).
- Espacio, respaldo `:611` (sentido canónico v2.0) — *"Flujo_total = w(Nivel 3 → Nivel 1) + w(Nivel 3 → Nivel 0) · w_ij = PIB_pc,j − PIB_pc,i"*
- Espacio, respaldo `:658, :662, :966` (sentido canónico φ) — *"φ: 𝒞 × T → ℝ⁺ · −∇_γ φ … el colapso sigue el flujo que minimiza la fricción integrada"*.
- `report.md:45` (§16, Ley Matroska, libro Cap. 21) — *"Flujo Total — Resonancia de Schumann — sincroniza el sistema con el latido de la Tierra (7.83 Hz)."* (Metáfora del libro; ver §3.12.)
- `report.md:88` (§17, Manifiesto 4D) — *"la quietud no es pasividad, es optimización del flujo de información hacia el Gran Atractor."*

#### PUENTE
- `taxonomia-por-dominio.md:10` — *"Puente: conecta hub con sombra y cobra por traducir."*
- `finanzas-mundo-snt.md:28` — *"| **Puente** | Corresponsalía bancaria, centros offshore, corredores de remesas: conectan hub con sombra y cobran por traducir — **rol definido, NO medido con estos datos** (gap, §9) |"*
- `finanzas-mundo-snt.md:246` — *"9. **El puente no está medido.** Corresponsalía, offshore y remesas son el rol puente a escala mundo, pero estos datos no los miden."*
- `estado-snt.md:28` — *"| **Puente** | El funcionario que mueve fondos de un lado a otro y cobra por saber dónde están (definición de Elán) — **rol definido, NO medido con estos datos** (gap, §9) |"*
- `estado-snt.md:300` — *"9. **El puente no está medido.** El funcionario que mueve fondos y cobra por saber dónde están es el rol puente a escala Estado, pero estos datos no lo miden. Sin dataset candidato por ahora."*
- `snt_agent.py:92-93` — *`"puente": "Corresponsalía bancaria, centros offshore, corredores de remesas — rol definido, NO medido con estos datos (gap)."`*
- `snt_agent.py:130-131` — *`"puente": "El funcionario que mueve fondos de un lado a otro y cobra por saber dónde están (definición de Elán) — rol definido, NO medido con estos datos (gap)."`*
- `snt_agent.py:159` — *`"puente": "Farmacia."`* (Salud); `:175` — *`"puente": "VACÍO."`* (Energía); `:192-193` — *`"puente": "Influencer que traduce lo del hub a su comunidad y cobra por eso."`* (Medios); `:212` — *`"puente": "Wallet (fintech), casa de bolsa que coloca CDA."`* (Ueno).
- `taxonomia-721-casos.md:121` — *"**Puente:** GAP como nodo nombrado. Lo más cercano es el **Nivel 2 Bypass Logístico** de la tabla de 5 niveles ("intercepta desbordamiento del Nivel 0, crecimiento parasitario"): es un nivel de la taxonomía, no un nodo identificado con nombre. Se registra como tal, no como puente medido."*
- Espacio, respaldo `:838` (sentido repo, Dominio G) — *"**Dominio G:** primer puente entre el marco v33 (Axiomas 1 y 8) y ACO-A — 5 casos con metadatos y citas primarias."*
- Espacio, respaldo `:1220, :1230, :1241, :1251, :1261` — Puente por dominio (Finanzas: *"Fintech wallet; el fideicomiso"*; Estado: *"El funcionario que mueve fondos y cobra por saber dónde están"*; Medios: *"El influencer que traduce lo del hub a su comunidad y cobra por eso"*; Salud: *"Farmacia"*; Energía: *"**PENDIENTE**"*).
- Espacio, respaldo `:1232` — *"El fideicomiso aparece como sombra y como puente según la operación: la ficha es por nodo y por momento, no por nombre."*
- `report.md:47, 53` (§16) — *"Puente Bayesiano: P(H|D) = P(D|H)·P(H) / P(D)."* / *"3. PUENTE (Bayes): actualiza creencias con evidencia, posterior limpio."* (Metáfora del libro; ver §3.12.)

#### SOMBRA
- `taxonomia-por-dominio.md:9-10` — *"sombra (mueve el mismo flujo sin pagar la luz, pegada al hub)"* (cuarto sentido; ver §3.4).
- `finanzas-mundo-snt.md:27` — *"| **Sombra** | Los sistemas bancarios con señales de decaimiento (92 países con ≥1 señal; 19 con ≥3): mueven el mismo flujo sin pagar la luz (no provisionan, no capitalizan) |"*
- `finanzas-mundo-snt.md:83` — *"La sombra en Finanzas-mundo es el sistema bancario que mueve el mismo flujo sin pagar la luz: no provisiona, no capitaliza, deja que la morosidad crezca."*
- `estado-snt.md:27` — *"| **Sombra** | Las entidades que mueven flujo sin pagar la luz (no-competitiva, oferente único, ejecución baja) y las que no aparecen en DNCP teniendo PGN grande (MEF, Caja de Bancos) |"*
- `estado-snt.md:86` — *"La sombra en Estado es la entidad que mueve flujo sin pagar la luz: no licita como tal, licita con un solo oferente, ejecuta poco de su presupuesto, o no aparece en el registro teniendo presupuesto grande."*
- `modelo-ueno-resultados-v2.md:269` — *"La sombra se mueve dentro del hub (fideicomiso interno)"*
- `rastro-del-dinero-ueno.md:27` — *"La sombra se mueve dentro del hub (fideicomiso interno)."*; `:32` — *"### El fideicomiso (el cuerpo de la sombra)"*
- `forecast-ueno-2026-11-06.md:246` — *"el nodo sombra institucional del dominio IPS"* (la ausencia de protocolo de contingencia).
- `taxonomia-721-casos.md:143` — *"**Sombra:** GAP como nodo nombrado. Los usuarios que abandonan (churn) son la sombra en sentido funcional, pero el corpus no los identifica como nodos con ficha."*

#### HUB
- `taxonomia-por-dominio.md:9` — *"hub (concentra el flujo, tiene licencia o legitimidad, punto único de falla)"*.
- `finanzas-mundo-snt.md:25-26` — hub = *"Los acumuladores de reservas"* (N0 China 23.25% en 2024, etc.).
- `estado-snt.md:25-26` — hub = *"Las entidades que concentran el valor licitado (Nivel 0: MSPBS 27.71%, MOPC 16.52%, IPS 15.08% en 2025; top 3 = 59.31%)"*.
- `rastro-del-dinero-ueno.md:21` — *"El hub ya no prestaba, acumulaba — en ambas series."*
- `snt_agent.py:86-88` — *`"hub": "Los acumuladores de reservas (Nivel 0: China 23.25% del mundo en 2024; Nivel 1: Japón, Suiza, EE. UU., India, Rusia, Arabia Saudita)."`*

#### FICHA POR NODO (origen / posición / naturaleza / patrón)
- `taxonomia-por-dominio.md:13-15` — *"Por nodo, ficha corta: origen (nació formal y se fue a sombra / nació en sombra / híbrido / comunitario, estatal, privado, criminal), posición (centro, borde, puente, sombra), naturaleza (simbionte, parásito, depredador paciente; el mismo puesto puede ser los tres en distintos momentos), patrón (acumula, distribuye, extrae, replica, hiberna)."*
- `taxonomia-por-dominio.md:17-19` — *"Observables (no lo que el nodo dice que es): de dónde le entra el flujo y a dónde lo saca; qué le pasa cuando cae el hub (¿se cae también o sobrevive?); qué gana en sombra que perdería en luz."*
- Espacio, respaldo `:1265-1268` — *"Ficha por nodo — se define por observables, no por lo que dice ser"*; *"Posición: Centro, borde, puente, sombra."*
- `taxonomia-721-casos.md:127` — *"**Niveles 1–3 y E:** ficha por nivel, no por entidad: Nivel 1 atractores secundarios (posición centro-secundario, patrón acumula propio pero drenado por Nivel 0); Nivel 2 bypass (posición puente, patrón extrae del desbordamiento); Nivel 3 sombra profunda (posición sombra, patrón extrae unidireccional); E exógeno (posición fuera, patrón GAP)."*
- `taxonomia-721-casos.md:148` — *"El ASI (δH·α/F, umbral 0,167) es la ficha cuantitativa: por encima, soberanía; por debajo, satelización."*
- `snt_agent.py:907` — campo `"ficha": {…}` en el reporte por nodo; `:1123-1125` — genera `## 4. Fichas por nodo (top 10 por cuota)`.

#### Términos derivados adicionales (para el análisis)
- **R-análogo:** `finanzas-mundo-snt.md:14` — *"construye el análogo de R(t) por país"*; `snt_agent.py:74` — *"cómo se construye su R-análogo"*; `snt_agent.py:105-107` — *"NO es el 0.10 de Ueno transferido"* (umbrales del propio dominio).
- **Roche-C / Roche-R / Roche-S (Ueno):** `snt_agent.py:218-222` — *"umbral_alerta: 0.10, # Roche-R: R(t) > 0.10 … umbral_origen: "Roche-R del backcast (R > 0.10). Roche-C: fondos públicos / patrimonio efectivo > 1.0. Roche-S: solvencia reportada / 12% < 0.50.""*
- **Bandas tipo Roche:** `finanzas-mundo-snt.md:14` — *"define bandas tipo Roche desde la serie propia de cada país"*; `estado-snt.md:14` — ídem por entidad.
- **Red micelial:** `finanzas-mundo-snt.md:14` — *"lee la red mundial como red micelial con competencia entre países"*; `estado-snt.md:14` — *"lee la red estatal como red micelial/fractal en el nivel municipal (sin competencia entre municipios, regla de Elán)"*.

---

## 3. Análisis de conflicto por término

Lectura de la evidencia. "Conflicto" = distancia entre el uso derivado y la definición del repo. Sin veredicto de remover/integrar.

### 3.1 LUZ — conflicto ALTO

- **No existe en el repo como término teórico.** La única aparición conceptual es una metáfora en `papers/marco_teorico.md:165` (*"no es mover la luz, es enfocar la misma sombra"*), donde "luz" significa el marco de proyección θ — sentido distinto al de la plantilla. Todo lo demás son tema de figuras, narrativa astronómica o estilos.
- **La plantilla la convierte en el observable central del método:** "qué cuesta estar visible / estar en regla", con umbrales medibles por dominio (capital/provisiones/Z-score; competitiva/oferente único/ejecución), "señales de luz", "luz no pagada" como observable, y puerta de suficiencia del agente Kaggle (sin proxy de luz → DATOS INSUFICIENTES; `kaggle-agente-informe.md:41-43, 48, 111-112`).
- **Atribución en conflicto con lo que dice Elán hoy.** El documento origen atribuye las definiciones a *"definiciones de Elán en chat 2026-11-06"* (`taxonomia-por-dominio.md:3-5`); el código repite *"(definiciones de Elán + repo v2.7.5.1)"* (`snt_agent.py:73-74`). La mitad "repo" de esa atribución está verificada como falsa: el repo no contiene la definición. La mitad "chat" no es verificable desde archivos. Lo que sí consta en archivo: `~/memory/2026-11-07.md:81` registra que el 2026-11-06 ~23:58 las definiciones de luz ya se trataban como *"already defined"* (Salud: "flujo, luz and puente/farmacia already defined"; Energía: "only luz: concesión, tarifa regulada, despacho defined"), y que los huecos que "solo Elán puede llenar" eran otros (hub/sombra de Salud; flujo/hub/sombra/puente de Energía). Es decir: para esa noche, "luz" ya circulaba como definida, sin que el repo la definiera. Elán hoy niega haberla definido.
- **Dependencia en cadena:** la sombra de la plantilla se define *en función de* la luz (*"la sombra se define por lo que cuesta la luz en ese dominio"*, espacio respaldo `:1211`). Un término sin base canónica sostiene a otro término redefinido (§3.4).
- **Alcance del uso:** no es solo una etiqueta. "Luz" aparece como sección propia (§3) en Finanzas-mundo y Estado, como columna de datos ("luz por entidad-año"), como criterio de suficiencia del agente, como observable en fichas ("Naturaleza: no paga la luz"), y como mensaje público planeado ("qué es la luz (lo que cuesta estar en regla…)", `linkedin-estrategia-reels.md:26` — reel concepto, en espera por decisión de Elán 2026-11-07).
- **Matiz a favor de la plantilla:** la propia `taxonomia-721-casos.md` es honesta al respecto: marca "Luz: GAP" en todos los dominios del corpus (`:67, :93, :118, :141, :160, :179, :198, :217`) y en `:141` se niega a forzar la equivalencia con el ASI (*"No se fuerza la equivalencia"*). El inventario del corpus NO presenta la luz como si estuviera en el repo; el problema está en los documentos de aplicación (Finanzas-mundo, Estado, agente Kaggle, espacio §9), que la usan como término establecido.

### 3.2 FLUJO — conflicto MEDIO-BAJO (redefinición de sentido, no de fórmula)

- El repo tiene dos sentidos formales: (a) flujo gradiente `-∇_γ φ` del campo de fricción; (b) `Flujo_total` compuesto entre niveles de la taxonomía v2.0.
- La plantilla lo redefine como "qué se mide en el dominio" — el caudal observable (dinero y crédito; fondos licitados; pacientes, recetas, datos; atención y legitimidad). No toca ninguna fórmula, pero cambia el referente: de constructo formal a variable medida.
- En el espacio conviven los dos sentidos sin distinguirlos: `:611/:658/:966` (canónico: Flujo_total v2.0 y flujo de φ) frente a `:1211` y la tabla por dominio (plantilla).
- Usos genéricos sin conflicto: `forecast-ueno-2026-11-06.md:279` ("flujo mensual de la reasignación" = cash-flow).

### 3.3 PUENTE — conflicto MEDIO-ALTO

- El repo solo conoce "puente" como infraestructura metodológica: Dominio G es un "puente construido, no evidencia" (`marco_teorico.md:56, 329`). Nada que ver con un intermediario que "conecta hub con sombra y cobra por traducir".
- La plantilla lo convierte en rol económico + posición de nodo ("posición: puente", espacio `:1268`; "el fideicomiso aparece como sombra y como puente según la operación", `:1232`).
- Agravante: **el puente nunca se mide en ningún dominio.** Gap declarado en Finanzas-mundo (`:246`), Estado (`:300`), agente (`snt_agent.py:92-93, 130-131` "rol definido, NO medido") e informe (`kaggle-agente-informe.md:39-40`). Es una etiqueta estructural sin observable.
- Colisión de nombres: "Puente Bayesiano" (§16, `report.md:47, 53`) es un tercer sentido (bayesiano, del libro), etiquetado explícitamente como metáfora. En el mismo espacio, "puente" significa tres cosas distintas (Dominio G `:838`; rol plantilla `:1220-1261`; bayesiano §16).

### 3.4 SOMBRA — conflicto ALTO

- El repo tiene **tres** sentidos distintos, ninguno igual al de la plantilla:
  1. **Nodo Sombra** (v2.0, `README.md:314`): "producción extraída sistemáticamente, divergencia progresiva" — definido por extracción.
  2. **Sombra** (Axioma 0.2, v34, `marco_teorico.md:144-146`): imagen de `𝒞` bajo proyección `Π_θ` — concepto epistémico/observable, con regla explícita: "Una sombra única no clasifica: genera candidatos, nunca asignación."
  3. **41 sombras** (tela): casos sin serie temporal cruda versionada — etiqueta de reconstrucción, no de nodo.
- La plantilla añade un **cuarto** sentido: "mueve el mismo flujo sin pagar la luz" — definido por no-pago de un término que no existe en el repo (§3.1). Y lo usa como categoría de nodo con ficha (naturaleza/parásito, patrón/extrae), mientras el repo no asigna fichas.
- La propia `taxonomia-721-casos.md` marca la distancia: *"Sombra: GAP como nodo nombrado"* (`:143`) y aclara que el Nivel 2 Bypass *"es un nivel de la taxonomía, no un nodo identificado con nombre. Se registra como tal, no como puente medido"* (`:121`).
- Uso en Ueno (`modelo-ueno-resultados-v2.md:269`, `rastro-del-dinero-ueno.md:27, 32`): "La sombra se mueve dentro del hub (fideicomiso interno)" / "El fideicomiso (el cuerpo de la sombra)" — sentido operativo del caso (el fideicomiso como cuerpo de la sombra), coherente con el Nodo Sombra v2.0 por extracción, pero sin anclaje explícito a esa definición.

### 3.5 HUB — conflicto BAJO-MEDIO

- Núcleo canónico intacto: Nodo Hub (`README.md:313`), `métrica_hub` en `R(t)`, niveles 0–3. Los usos derivados ("acumuladores de reservas", "entidades que concentran el valor licitado") son compatibles con ese núcleo.
- Añadidos de la plantilla sin base en el repo: *"tiene licencia o legitimidad, punto único de falla"* (`taxonomia-por-dominio.md:9-10`). "Licencia/legitimidad" y "punto único de falla" no aparecen en la definición del repo. Son calificaciones normativas nuevas, no una redefinición del núcleo.

### 3.6 NODO — conflicto BAJO

- Canónico (`R(t)` hub/nodo; taxonomía de nodos). El uso derivado es coherente; la novedad está en la ficha (§3.7), no en el término.

### 3.7 FICHA POR NODO (origen / posición / naturaleza / patrón) — conflicto MEDIO-ALTO

- **Instrumento entero sin base en el repo:** 0 ocurrencias de "ficha"; 0 de "simbionte"; 0 de "hiberna"; "parásito" solo como "parásito-huésped" (etiqueta de dominio E3). Las categorías de naturaleza (simbionte, parásito, depredador paciente) y de patrón (acumula, distribuye, extrae, replica, hiberna) son invención del material derivado.
- **Se aplica a entidades reales con etiquetas valorativas:** *"Naturaleza: parásito (por observables: luz no pagada)"* (`salida-snt/informe-finanzas_mundo.md:64`) — un país etiquetado "parásito" porque no pagó la "luz" (§3.1). La cadena completa (luz inventada → sombra redefinida → ficha con naturaleza) produce juicios sobre países y entidades.
- **La propia taxonomia-721-casos.md marca GAP en casi todas las fichas del corpus** (`:79, :102, :127, :148, :205`) — evidencia interna de que el corpus no sostiene el instrumento. Excepción honesta en `:148`: *"El ASI (δH·α/F, umbral 0,167) es la ficha cuantitativa"* — ahí la ficha se ancla a un término canónico (ASI), no a las categorías inventadas.

### 3.8 R-ANÁLOGO — conflicto BAJO

- No existe en el repo, pero se presenta explícitamente como analogía ("análogo de R(t)"), no como `R(t)`. Los documentos declaran que los umbrales son "del propio dominio" y que *"NO es el 0.10 de Ueno transferido"* (`snt_agent.py:105-107, 149-151`). Riesgo menor: el nombre sugiere una equivalencia formal que los propios documentos niegan.

### 3.9 ROCHE-C / ROCHE-R / ROCHE-S y "bandas tipo Roche" — conflicto BAJO-MEDIO

- El repo menciona "radio de Roche" y "Ratio de Roche" (`README.md:52, 370`) como descripción, sin operacionalizar C/R/S. La operacionalización Ueno (Roche-C: fondos públicos/patrimonio efectivo > 1.0; Roche-R: R(t) > 0.10; Roche-S: solvencia/12% < 0.50) es derivada y se declara como del backcast (`snt_agent.py:218-222`).
- Contexto de cautela en el propio repo: la etiqueta "Roche Radius" como régimen de `b > 1` fue **retirada** (RC1, `CHANGELOG.md:726-729`). Las "bandas tipo Roche" de Finanzas-mundo/Estado se declaran "desde la serie propia de cada país/entidad" — analogía declarada, no transferencia.

### 3.10 RED MICELIAL / MICELIAL — conflicto BAJO-MEDIO

- Antecedente solo en marco v30 (supersedida): "Red Fúngica… el hub central es el micelio principal y los nodos sombra son los capilares de extracción" (`marco_teorico_v30.md:1343`); "Nodo Orquestador — Nivel 2 (Micelio / DAG)" (`:847`). Ausente del marco v34 activo y del README.
- Uso derivado como marco interpretativo: *"lee la red mundial como red micelial con competencia entre países"* (`finanzas-mundo-snt.md:14`); *"red micelial/fractal en el nivel municipal (sin competencia entre municipios, regla de Elán)"* (`estado-snt.md:14`). La regla "sin competencia entre municipios" es premisa de Elán, no del repo — consta como tal en el documento.

### 3.11 φ EN EL MODELO UENO v2 — conflicto MEDIO

- Repo: φ = campo de fricción postulado (Axioma 0.1), no medido; su relación general con `b` no está respaldada (`README.md` tabla de afirmaciones).
- `modelo-ueno-resultados-v2.md:159, 169` redefine φ operativamente: *"trazabilidad normativa del desplazamiento: qué actos retiraron luz, cuándo, con qué observable"*; *"Las φ son causas formales: cada paso retiró luz."* Es decir: de campo escalar a lista de 5 actos normativos, anclada a "luz" (§3.1). El propio documento admite: *"φ no fue cuantificado como campo continuo (el estado actual del marco lo postula por dominio, no lo mide)"* — la admisión está, la redefinición también.

### 3.12 PUENTE BAYESIANO / FLUJO TOTAL (§16–§20) — conflicto BAJO

- Usos del libro Cap. 21 (Ley Matroska), **explícitamente etiquetados** en el propio informe: *"Fuente: libro Cap. 21. Nivel: Metáfora (marco pedagógico); el puente bayesiano y la limpieza Gauss-Jordan sí son verificables como herramientas."* (`report.md:35`).
- No se presentan como términos SNT. El riesgo es de colisión de nombres, no de mezcla conceptual: "puente" ya significa tres cosas en el espacio (§3.3) y "flujo" también (§3.2). "Años luz" (`report.md:232, 300`) es distancia astronómica, sin relación.

### 3.14 SATÉLITE — sin conflicto (marginal)

- Hallazgo de la inspección del espacio en vivo: "satélite" aparece solo 2 veces en el texto visible — (1) alt-text del hero (*"[image: Hub central con nodos satélite orbitando…]"*) y (2) taxonomía de fallos, Fallo 2 (*"el nodo queda satélite irreversible sin intervención exógena…"*). No hay definición formal de "satélite" como sustantivo teórico distinto de "nodo sombra". No redefine nada; sin colisión.

### 3.15 TONO — dos acepciones sin desambiguar (conflicto BAJO, solo de lectura)

- Hallazgo de la inspección del espacio en vivo: "tono" tiene dos acepciones en el espacio sin desambiguación explícita: (1) tono-φ como variable de clasificación LOO en v2.7.1 (*"66.2% por tono… El tono φ no se distingue de permutar tonos entre dominios (p = 0.39)"*); (2) tono periodístico en Ueno §6 Datasets, Medios (*"Atención y tono por medio: hub (ABC, Nación, canal grande) contra réplicas sin firma"*). "Tono" no está definido formalmente en el núcleo, así que no afecta a ninguna definición nuclear; el riesgo es solo de lectura. En el repo, "tono" es canónico solo en el sentido (1) (tela LOO tono 66.2%).

### 3.13 Sin conflicto detectado

- **Tono (φ):** canónico (tela LOO tono 66.2%).
- **Kaggle genómico:** 0 ocurrencias de luz/flujo/puente en `kaggle-genomico-informe.md` y `genomico-agent-core.py`. El agente genómico no usa la plantilla.
- **`snt-taxonomia/DOMINIOS.md`:** copia byte-idéntica del repo (`diff` sin diferencias). Sin contaminación.
- **ASI, ACO-A, Muro de 5 eventos, leapfrog, tela, eje u:** usos derivados revisados coinciden con las definiciones del repo en lo verificado (sin perjuicio de la nota de φ en §3.11 y de Roche en §3.9).

---

## 4. Cadena de propagación (cómo se extendió la plantilla)

1. **2026-11-06 — `taxonomia-por-dominio.md`:** nace el esqueleto *"flujo, luz, hub, sombra, puente"* + la ficha por nodo. Fuente declarada: *"repo v2.7.5.1 + definiciones de Elán en chat 2026-11-06"*. La mitad "repo" no contiene "luz", "puente"-rol ni "ficha" (verificado §1.1).
2. **2026-11-07 — Espacio SNT §9 (respaldo `:1211`):** *"El esqueleto — flujo, luz, hub, sombra, puente — se mantiene… la sombra se define por lo que cuesta la luz en ese dominio."* La plantilla entra al espacio como si fuera el esqueleto de la teoría.
3. **2026-11-07 — `snt_agent.py:71-76`:** la plantilla se codifica como `DOMAIN_SPECS` (*"definiciones de Elán + repo v2.7.5.1"*), con umbrales de luz y puerta de suficiencia.
4. **2026-11-07 — `finanzas-mundo-snt.md:12` y `estado-snt.md:12`:** se aplica a dominios nuevos ("somete … a la SNT con la plantilla…").
5. **2026-11-08 — Salidas del agente Kaggle:** "Señales luz", fichas con *"Naturaleza: parásito (por observables: luz no pagada)"*.
6. **2026-11-07 — `linkedin-estrategia-reels.md:26`:** plan de comunicar *"qué es la luz"* en público (reel concepto, en espera por decisión de Elán).
7. **Memoria del proceso (`~/memory/2026-11-07.md:81, 349`):** para el 2026-11-06 ~23:58 las definiciones de luz ya se trataban como *"already defined"*; el 2026-11-07 ~06:25 se lanzó el análisis pesado aplicando *"the per-domain SNT template (flujo/luz/hub/sombra/puente)"*.

## 5. Limitaciones de esta auditoría

- **El chat 2026-11-06 no se revisó** (no disponible en archivos). La atribución "definiciones de Elán" solo se verificó contra el repo, no contra el chat. No se afirma qué dijo Elán en ese chat; se afirma qué contiene y qué no contiene el repo.
- **Espacio en vivo:** la evidencia del espacio es el respaldo `2026-11-07` (§1–§15) más la inspección del espacio en vivo (`artifact.inspect`, ID `594ee4d2-9151-4031-b94a-0bca4e4adee9`, resultado recibido 2026-11-09 ~10:33), que confirma la localización de "luz"/"puente"/"ficha" en Ueno y añade los hallazgos de "satélite" (2 ocurrencias) y "tono" (dos acepciones, §3.14–§3.15). La inspección del artefacto no hizo conteo exacto por grep de los términos ubicuos (citas representativas, no cifras) ni comparó contra el repo — esa comparación es este archivo. El artefacto es estático (sin app.db; `inspect_data` falló por ello) y `list_actions` devolvió 405: la evidencia es el HTML/texto renderizado.
- **Recomendación del inspector (registrada, NO aplicada):** sin tocar el espacio hasta que Elán confirme, acotar solo la frase del esqueleto en Ueno §1 y las filas Luz/Puente por dominio — distinguir esqueleto nuclear (flujo, hub, sombra) de instrumentos operativos del caso Ueno, o moverlos a un glosario "Vocabulario del caso Ueno — no forma parte del marco v01–v34", declarando fecha de entrada (6 nov 2026) y estatus si se integran. Esta recomendación queda registrada como evidencia, no como decisión: **no se aplicó ninguna edición al espacio** (inspección solo de lectura, `repair_authorized: false`).
- **Conteos:** `grep -ciE` por palabra; incluyen usos genéricos. Las citas son la evidencia; los conteos, orientación.
- **Alcance:** no se revisaron los notebooks de Kaggle subidos ni el contenido del chat de la raíz; no se auditó si "luz" aparece en otros derivados fuera de la lista del §0 (p. ej. `efipem-snt/` (archivo local de trabajo), podcast/video de Ueno, `muro-5-eventos/`).
- **Sin veredicto:** este archivo no decide qué se remueve ni qué se integra. Esa decisión es del agente principal con Elán.
