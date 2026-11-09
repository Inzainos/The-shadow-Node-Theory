# COPIA DE REGISTRO — Ueno v3 (corrección 2026-11-09)
# Archivo original: docs/ueno-2026-11-07/finanzas-mundo-snt.md
# Versión: sin número de versión declarado (2026-11-07)
# Estado: archivo de registro — SIN CAMBIOS respecto al original. Cuerpo intacto; solo se añadió esta cabecera.
# Fecha de la copia: 2026-11-09
# md5 original: f26ef328d479325173e7d491aa2bf24b
# sha256 original: b10a89897c1f09b1f1b97c203f9bc49d27c2d4c817569d8dbd8f758dab56a978
#
# Finanzas-mundo: la Teoría del Nodo Sombra aplicada al sistema bancario mundial

**Fractal Core Research** — Primera aplicación SNT a un dominio nuevo después de Ueno
**Fecha:** 2026-11-07 · **Fuentes:** Banco Mundial, API v2 (WDI + GFDD), 24 indicadores, descargados 2026-11-07 · **Licencia:** CC BY 4.0
**Archivos:** `datasets-nuevos-dominios/finanzas/banco-mundial-finanzas-limpio.csv` (216 países, 11,948 filas país-año, 1960–2024), `datasets-nuevos-dominios/finanzas/banco-mundial-decaimiento-metricas.csv` (métricas por país), `finanzas-mundo-snt-valores.csv` (R-análogo por país), `aplicar_snt_finanzas_mundo.py` (script de esta aplicación), `finanzas-mundo-snt-verificacion.json` (verificación)
**Documento base:** `banco-mundial-decaimiento-paises.md` (análisis de decaimiento y acumuladores, verificado)

**Principio (Elán):** la teoría es invariante de escala y universal; misma aritmética, datos distintos por dominio. La taxonomía es PER DOMINIO: cada país se mide con su propia serie y su propio umbral, normalizado dentro de su dominio. **Países y agregados ÚNICAMENTE, cero personas** (regla de nombres de Elán). Todo lo estimado va etiquetado **ESTIMADO**; nunca es fecha de quiebra. b es descriptor de deriva, no prueba de mecanismo; b ≥ 1 es banda descriptiva sin clasificar, NUNCA prueba de superlinealidad.

## 0. Qué es esto y qué no es

Este documento somete Finanzas-mundo a la SNT con la plantilla por dominio (flujo, luz, hub, sombra, puente) y la ficha por nodo (origen, posición, naturaleza, patrón), usando como molde el caso Ueno (`modelo-ueno-resultados-v2.md`, `rastro-del-dinero-ueno.md`). Es la primera vez que un dominio nuevo se somete completo a la SNT después de Ueno.

**Lo que SÍ hace:** define el flujo, la luz, el hub y la sombra del sistema bancario mundial con los indicadores del Banco Mundial; construye el análogo de R(t) por país; define bandas tipo Roche desde la serie propia de cada país; identifica los nodos sombra por observables; lee la red mundial como red micelial con competencia entre países.

**Lo que NO hace:** no prueba mecanismos (la deriva describe, no explica); no predice fechas de falla (los tiempos son ESTIMADOS por extrapolación lineal, con la condición de que la tendencia siga); no ve el hub a nivel de entidad (el Banco Mundial agrega por país — ver §9, gap 1); no mide ASI (sin datos de eventos conductuales) ni u (NULL en todos los dominios).

**El caso plantilla (Ueno) como referencia:** R(t) = fondos públicos en el hub / fondos públicos en el resto del sistema. Cruce Roche-R (0.10) en dic 2024 (R = 0.1021); b = 0.383/0.436 (dic 2024–nov 2025); Roche-C = 1.08 (dic 2024); Roche-S = 0.463 (2 nov 2026); ACO-A con resolución BCP 2 nov 2026 y absorción por 7 bancos. La lección metodológica que se traslada: el hub se ve a nivel de entidad, la deriva se mide con ventana + origen de t + n, y el umbral no se transfiere mecánicamente de un sistema a otro.

## 1. La plantilla aplicada a Finanzas-mundo

| Elemento | Finanzas-mundo (este documento) | Ueno (molde) |
|---|---|---|
| **Flujo** | Dinero y crédito entre países y dentro de cada sistema bancario: crédito al sector privado (% PIB), crédito/depósitos, morosidad (la parte dañada del flujo), reservas totales (el stock acumulado) | Dinero y crédito; fondos públicos en Ueno |
| **Luz** | Capital regulatorio (Basilea 8%), capital/activos, provisiones/morosidad, Z-score (distancia a la insolvencia) | Capital, provisión, auditoría, cuota al FGD, límite a partes relacionadas |
| **Hub** | Los acumuladores de reservas (Nivel 0: China 23.25% del mundo; Nivel 1: Japón, Suiza, EE. UU., India, Rusia, Arabia Saudita) | Continental, Itaú, Ueno (híbrido) |
| **Sombra** | Los sistemas bancarios con señales de decaimiento (92 países con ≥1 señal; 19 con ≥3): mueven el mismo flujo sin pagar la luz (no provisionan, no capitalizan) | Empresa salvadora, cooperativa fuera de FGD, financiera que presta a su grupo |
| **Puente** | Corresponsalía bancaria, centros offshore, corredores de remesas: conectan hub con sombra y cobran por traducir — **rol definido, NO medido con estos datos** (gap, §9) | Fintech wallet, casa de bolsa que coloca CDA |

## 2. FLUJO: qué se mide y por qué

El flujo es dinero y crédito. Los indicadores elegidos, con su justificación:

| Indicador | Qué mide del flujo | Cobertura |
|---|---|---|
| `FS.AST.PRVT.GD.ZS` — crédito al sector privado (% PIB) | El tamaño del flujo de crédito en la economía | 234 países, 1960–2024, 9,876 celdas |
| `GFDD.SI.04` — crédito / depósitos (%) | Cuánto del flujo prestado se fondea con depósitos (apalancamiento del hub) | 185 países, 1960–2021, 8,553 celdas |
| `FB.AST.NPER.ZS` / `GFDD.SI.02` — morosidad (% de la cartera) | La parte dañada del flujo: lo que dejó de volver | 154 / 144 países, 2000–2024 / 1998–2020 |
| `FI.RES.TOTL.CD` — reservas totales (USD corrientes) | El stock acumulado: dónde termina el flujo cuando se guarda | 183 países, 1960–2024, 9,382 celdas |
| `GFDD.DI.02` — activos de bancos / PIB (%) | El tamaño del sistema bancario (el hub como institución) | 186 países, 1960–2021, 8,656 celdas |
| `GFDD.DI.05` — pasivos líquidos / PIB (%) | Los depósitos: la base del fondeo | 185 países, 1960–2021, 8,531 celdas |

Las dos series de morosidad (WDI y GFDD) son la misma serie en dos vintages: correlación 0.9349 sobre 1,443 pares país-año, diferencia absoluta media 0.424 pp (verificado en el análisis de decaimiento). Donde difieren se registra (p. ej. Gabón 2015–2016). **No se usó** `FS.AST.DOMS.GD.ZS` (crédito del sector financiero, solo 78 países) como comparador global: serie rala.

**La morosidad es el flujo dañado, no el flujo.** La R-análogo (§6) se construye sobre ella porque es el único indicador con serie corriente hasta 2024 en 154 países y con el que se puede fechar un cruce.

## 3. LUZ: qué cuesta estar en regla, y quién la paga

La luz en Finanzas-mundo es el capital, las provisiones y la distancia a la insolvencia. Lo que cuesta, por indicador (umbrales de trabajo del análisis de decaimiento; Basilea donde se indica):

| Luz | Umbral alerta | Umbral crisis | Quién NO la paga (último dato) |
|---|---|---|---|
| Capital regulatorio / activos ponderados (GFDD.SI.05) | 8% (Basilea) | 6% | **1 país:** Chad 5.97% (2020) — el único bajo el mínimo de Basilea |
| Capital / activos (GFDD.SI.03) | 5% | 3% (Basilea, apalancamiento) | **4 países:** Bangladesh 4.77%, Canadá 4.95%, Japón 4.86%, Macao 4.49% (todos 2020) |
| Provisiones / morosidad (GFDD.SI.07) | 40% | 25% | **22 países** bajo 40%; **5** bajo 25%: Australia 18.1% (2020), Azerbaiyán 0.9% (2015), Etiopía 20.3% (2020), Israel 24.3% (2020), Vanuatu 22.1% (2018) |
| Z-score bancario (GFDD.SI.01) | 5 | 3 | **6 países** bajo 5: Azerbaiyán 4.74, Colombia 4.32, Islandia 1.28, Kazajistán 2.95, Santa Lucía 4.90, Eslovenia 4.49; **2** bajo 3: Islandia, Kazajistán (2021) |

**Lectura:** el capital es la luz que casi todos pagan — solo Chad está bajo el mínimo de Basilea, y ningún país está bajo el 3% de capital/activos. **La luz que se deja de pagar es la provisión:** 22 países provisionan menos del 40% de su morosidad, y 5 menos del 25% (Azerbaiyán provisiona 0.9%: casi nada). No provisionar es moverse en sombra dentro del sistema formal: el flujo sigue, pero sin el colchón que la regla exige. Islandia (Z-score 1.28 en 2021) y Kazajistán (2.95) son los sistemas más cerca de la insolvencia por distancia estadística — con la advertencia de que el Z-score es GFDD y termina en 2021.

**Caveat de fecha (importante):** todo el panel de luz es GFDD y termina en 2020/2021. La luz post-COVID no se ve en estos datos. La morosidad WDI (hasta 2024) es la única serie bancaria corriente — por eso el R-análogo (§6) se construye sobre morosidad, no sobre capital.

## 4. HUB: quiénes concentran el flujo

Los hubs del sistema-mundo son los acumuladores de reservas. Niveles por cuota de reservas mundiales 2024 (misma aritmética de niveles del repo, con los cortes declarados aquí):

| Nivel | Corte (cuota reservas 2024) | Países | Cuota conjunta |
|---|---|---|---|
| **Nivel 0 — Macro-Hub** | ≥10% | 1: **China 23.25%** (USD 3.456 billones) | 23.25% |
| **Nivel 1 — Atractores** | 3–10% | 6: Japón 8.28%, EE. UU. 6.12%, Suiza 6.12%, India 4.33%, Rusia 4.09%, Arabia Saudita 3.12% | 32.05% |
| **Nivel 2 — Bypass** | 1–3% | 14: Alemania, Francia, Reino Unido, Corea, Brasil, México, Singapur, EAU, Indonesia, Tailandia, Turquía, Italia, Polonia, Israel | 24.98% |
| **Nivel 3 — Nodos** | <1% | 143 países | 19.71% |

**Los 6 primeros concentran el 52.18% de las reservas mundiales** (China + Japón + EE. UU. + Suiza + India + Rusia). Las reservas mundiales (suma de países con dato; el BM no publica el agregado WLD) pasaron de **USD 10.133 billones (2010) a USD 14.867 billones (2024)**: el mundo acumuló ~USD 4.7 billones en 14 años.

**Los acumuladores más rápidos (CAGR 2010–2024, reservas 2024 > USD 10 mil M):** Emiratos Árabes Unidos **15.21%/año** (USD 32.8 mil M → 237.9 mil M, superávit comercial medio +20.77% del PIB); Eslovaquia 14.56%, Vietnam 14.51%, Irlanda 13.66% (superávit +28.54%, inflado por multinacionales), Camboya 13.51%, **Nepal 12.62%** (ver §8, la tensión), Guatemala 10.61%, República Dominicana 9.31%, Chequia 9.23%, España 9.09%, **Suiza 9.05%/año** (USD 270.5 mil M → 909.4 mil M — la acumulación del Banco Nacional Suizo tras el piso del franco 2011–2015).

**El nivel no es la salud (otra vez):** China lleva el crédito/depósitos por encima de 200% desde 2010 (235% → 366% en 2021) y tiene 1 señal por ese indicador (ya en umbral de alerta), pero sin deriva de morosidad (NPL 1.13% → 1.51% en 2024) y con provisiones de 185%: su fondeo no es depósitos, el nivel alto no es una crisis. Igual que en el forecast de Ueno (BNF 0.3712 y Continental 0.1983 ya estaban por encima de 0.10 sin estar en colapso): se vigila la deriva, no el nivel.

**GAP 1 — el hub es un banco, no un país.** El Banco Mundial agrega por país. La concentración que importa (qué banco concentra los depósitos públicos, qué banco presta a su grupo) se ve a nivel de entidad, como en Ueno. Sin dato por banco, el hub aquí es el sistema bancario del país, no el nodo. La lección de Ueno es justamente esa: el país (Paraguay) puede verse sano en agregado mientras su hub (Ueno) se rompe por dentro (ver ficha de Paraguay, §5).

## 5. SOMBRA: fichas por nodo

La sombra en Finanzas-mundo es el sistema bancario que mueve el mismo flujo sin pagar la luz: no provisiona, no capitaliza, deja que la morosidad crezca. **92 países tienen ≥1 señal de decaimiento; 19 tienen ≥3.** Las fichas se hacen por observables (qué dice la serie), no por lo que el país dice de su banca. **Todos los nodos sombra con ≥3 señales son Nivel 3** (<1% de las reservas mundiales): la deriva se concentra en los nodos chicos; los hubs (N0–N2) tienen como máximo 1 señal cada uno (ver §8).

### Chad (TCD) — 6 señales, el más deteriorado

- **Origen:** sistema bancario petrolero; el choque del petróleo 2014–2016 sin recuperación.
- **Posición:** Nivel 3 (0.01% de las reservas mundiales). Centro de su propio sistema, borde del sistema-mundo.
- **Naturaleza:** extrae y no repone. **Patrón: extrae + hiberna.**
- **Números:** morosidad 9.9% (2010) → **31.5% (2023)**, pendiente +2.00 pp/año, R²=0.822; capital regulatorio 12.5% → **6.0% (2020), bajo el mínimo de Basilea 8%** — el único país del mundo bajo el mínimo; capital/activos 11.3% → 9.9%; reservas líquidas 27.1% (2010) → **6.2% (2016, mínimo)** → 15.5% (2021); provisiones 81% → 66%; crédito/depósitos 80% → 94%. R_NPL 0.110 (2010) → 0.460 (2023), b_R = 0.751 (R²=0.766, n=14). Cruce de alerta 2010 (ya estaba), cruce de crisis **2016**. Tiempo restante: **YA EN UMBRAL**.
- **Lectura:** 6 de 9 señales. El sistema no se recupera: la morosidad sigue subiendo después del choque y el capital se comió el colchón. Sin Z-score después de 2016, sin GFDD después de 2020/2021: falta todo lo posterior a 2021 para confirmar si la morosidad 31.5% sigue subiendo.

### Congo, Rep. (COG) — 5 señales, la deriva más rápida

- **Origen:** sistema bancario petrolero, mismo choque 2014–2016.
- **Posición:** Nivel 3 (0.01% de las reservas mundiales).
- **Naturaleza:** extrae. **Patrón: acumula morosidad.**
- **Números:** morosidad **0.96% (2010) → 15.2% (2023)**, pendiente +1.80 pp/año; GFDD 0.96% → 24.8% (2020); reservas líquidas 51.7% → 26.4% (2023); provisiones **105% → 42%** (pendiente −6.99 pp/año, R²=0.903); crédito/depósitos 35% → 84%. R_NPL 0.0097 → 0.180, **b_R = 1.597 (R²=0.808, n=14) — la deriva más rápida del mundo en el R-análogo**, banda descriptiva b ≥ 1, sin clasificar. Cruce de alerta **2017**, cruce de crisis **2018**. Tiempo restante: **YA EN UMBRAL**.
- **Tensión registrada:** el capital SUBIÓ mientras el flujo se pudría — capital regulatorio 13.1% → 24.9%, capital/activos 8.2% → 17.0% (2020). La luz se pagó en capital y no en provisiones. El nodo capitaliza y no provisiona a la vez: la ficha es por momento, no por nombre.

### Argelia (DZA) — 5 señales, el que hiberna

- **Origen:** sistema bancario estatal con morosidad estructuralmente alta.
- **Posición:** Nivel 3 (0.56% de las reservas mundiales).
- **Naturaleza:** hiberna. **Patrón: hiberna.**
- **Números:** morosidad 18.3% (2010) → **20.7% (2024)** — ya alta al inicio, deriva lenta: b_R = 0.138 (R²=0.115, ajuste débil: no hay deriva clara, hay un problema de nivel); reservas líquidas **86.0% (2010) → 14.6% (2020) → 22.1% (2024)**, pendiente −4.53 pp/año, R²=0.662; activos líquidos 60.5% → 32.7% (2020); provisiones 73.5% → 50.1% (2018); Z-score 19.2 → 24.8 (2020, alto). R_NPL 0.224 (2010) → 0.261 (2024). Cruce de alerta 2010 (ya estaba), cruce de crisis **2023**. Tiempo restante: **1.6 años ESTIMADO** (reservas líquidas, umbral 15%).
- **Contraseñal registrada:** las reservas líquidas se recuperaron parcialmente de 14.6% (2020) a 22.1% (2024). Si la recuperación sigue, el ESTIMADO de 1.6 años no se cumple. Es el único de los tres peores con tiempo estimado mayor que cero.

### Guinea Ecuatorial (GNQ) — 4 señales, el salto

- **Origen:** sistema bancario petrolero, choque 2014–2016.
- **Posición:** Nivel 3 (0.01% de las reservas mundiales).
- **Naturaleza:** extrae. **Patrón: extrae.**
- **Números:** morosidad **4.7% (2010) → 31.1% (2023)**, pendiente +3.91 pp/año, R²=0.786; GFDD 4.7% → 48.8% (2019) y 55.4% (2022); provisiones **112% → 34%**; crédito/depósitos 62% → **157%**; reservas líquidas 76.9% → 24.7% (2023, pendiente −4.12 pp/año pero R²=0.239, sin señal por R²). R_NPL 0.0495 → 0.452, **b_R = 1.366 (R²=0.849, n=14)**, banda descriptiva b ≥ 1. Cruce de alerta **2013** y de crisis **2013** (el mismo año: el salto fue de 5.8% a 20.1% en un año). Tiempo restante: **YA EN UMBRAL**.
- **Lectura:** el salto de 2013 es un cambio de nivel, no una deriva lenta. El b alto lo mide como deriva porque la serie sube sostenida después del salto.

### Ucrania (UKR) — exógeno (guerra)

- **Origen:** exógeno — la guerra, no una deriva bancaria endógena.
- **Posición:** Nivel 3 (0.29% de las reservas mundiales).
- **Naturaleza:** exógeno. **Patrón: contrae.**
- **Números:** morosidad 15.3% (2010) → **30.3% (2024)**; GFDD 15.3% → 41.0% (2020); Z-score 4.66 → 5.18 (2021, bajo); reservas líquidas **6.3% → 46.6%** (2024, el sistema acumuló liquidez); crédito/depósitos **164% → 65%** (el sistema se contrajo). R_NPL 0.180 → 0.435, b_R = 0.629 (R²=0.555, n=15). Cruce de alerta 2010 (ya estaba), cruce de crisis **2012**. Tiempo restante: **YA EN UMBRAL** (por GFDD).
- **Lectura:** la morosidad es de guerra. La liquidez subió y el crédito se contrajo: el sistema no se pudrió por dentro, se achicó por fuera. No se lee como deriva endógena.

### Ghana (GHA) — exógeno (default soberano 2022)

- **Origen:** exógeno — el default soberano de 2022.
- **Posición:** Nivel 3 (0.05% de las reservas mundiales).
- **Naturaleza:** exógeno. **Patrón: salto de nivel.**
- **Números:** morosidad 18.1% (2010) → **21.8% (2024)**; reservas líquidas **23.3% → 70.7%**; Z-score 12.1 → 13.9; capital regulatorio 19.1% → 19.8%. **0 señales de decaimiento** (la pendiente de morosidad es +0.34 pp/año, R²=0.207: no hay deriva que medir). R_NPL 0.221 → 0.279, b_R = 0.094 (R²=0.091, sin ajuste). Cruce de alerta 2010 (ya estaba), cruce de crisis **2017**. Sin tiempo estimado.
- **Lectura y límite del método (registrado):** Ghana es el caso que la regla de señales NO caza: el nivel es alto y el salto de 2023–2024 (14.8% → 20.6% → 21.8%) es un salto de nivel post-default, no una deriva. La SNT aquí describe el nivel, no lo explica; el método de señales detecta deriva, no saltos.

### Paraguay (PRY) — el caso plantilla, el control

- **Origen:** sistema bancario paraguayo; el caso Ueno vive dentro de él.
- **Posición:** Nivel 3 (0.06% de las reservas mundiales).
- **Naturaleza:** simbionte en agregado, con un hub parásito dentro (Ueno). **Patrón: distribuye.**
- **Números:** **2 señales, las dos de liquidez:** reservas líquidas 28.9% (2010) → 18.3% (2024), pendiente −0.52 pp/año, R²=0.48; activos líquidos 34.3% → 23.1% (2021). **Sin señal de solvencia:** morosidad **2.27% (2024, baja)**, Z-score 17.1 (2021, alto), capital/activos 8.47% (2020), capital regulatorio 13.0% → 19.1%. R_NPL 0.0142 → 0.0233, b_R = 0.217 (R²=0.653, n=15). **Sin cruces de banda.** Sin tiempo estimado. Reservas totales USD 9.6 mil M, CAGR 6.12%/año; balanza comercial media +1.71% del PIB.
- **Lectura (la más importante de este documento):** el hub Ueno cayó (resolución BCP 2 nov 2026, solvencia 5.56%) y el agregado del país apenas se movió. La caída de reservas líquidas 2023→2024 (24.3% → 18.3%, −6 pp en un año) es un movimiento de un año, no una tendencia: hay que ver 2025 antes de leerlo como deriva. **El caso Paraguay prueba el gap 1: el Banco Mundial no ve el hub.** El nodo que se rompió era un banco, no el país.

### Bangladesh (BGD) — 4 señales, el sinceramiento

- **Origen:** revelación de morosidad oculta tras el cambio de gobierno (2024).
- **Posición:** Nivel 3 (0.14% de las reservas mundiales).
- **Naturaleza:** extrae. **Patrón: acumula morosidad.**
- **Números:** morosidad **1.9% (2010) → 19.0% (2024)**, con el salto en 2024 (9.57% en 2023 → 18.96% en 2024); Z-score **20.1 → 12.8** (2021); capital/activos 6.89% → **4.77% (2020, bajo el 5% de alerta)**; reservas líquidas 9.7% → 7.5% (2024, ya bajas). R_NPL 0.0194 (2011) → 0.234 (2024), b_R = 0.685 (R²=0.612, n=14). Cruce de alerta **2014**, sin cruce de crisis (todavía). Tiempo restante: **13.4 años ESTIMADO** (Z-score, umbral 5).
- **Advertencia registrada:** el ESTIMADO de 13.4 años es conservador: si el salto de morosidad 2024 es estructural y no un sinceramiento de un año, el tiempo es menor.

### Nepal (NPL) — 3 señales, la tensión

- **Origen:** sistema bancario pequeño con morosidad en subida y reservas que crecen por remesas, no por superávit.
- **Posición:** Nivel 3 (0.11% de las reservas mundiales).
- **Naturaleza:** simbionte del flujo de remesas. **Patrón: acumula reservas + acumula morosidad a la vez.**
- **Números:** morosidad 1.68% → 4.64% (2024), pendiente +0.32 pp/año, R²=0.563; reservas líquidas 10.7% → 8.2% (2024); crédito/depósitos 88.7% → 96.2%; Z-score 27.1 → 28.9 (alto). R_NPL 0.0171 (2016) → 0.0486 (2024), **b_R = 1.152 (R²=0.416, n=9)**, banda descriptiva b ≥ 1. Sin cruces de banda. Tiempo restante: **YA EN UMBRAL** (reservas líquidas). Reservas totales: CAGR **+12.62%/año** (2010–2024) con balanza comercial media **−29.58% del PIB**.
- **Lectura:** acumular reservas no es estar sano. El b ≥ 1 aquí es sobre una base chica (NPL 1.7% → 4.6%) con R²=0.416: banda descriptiva, nunca prueba de superlinealidad. La tensión es el caso (ver §8).

### Mozambique (MOZ) — 1 señal, el b ≥ 1 con contraseñal

- **Origen:** morosidad en subida desde base baja.
- **Posición:** Nivel 3 (0.03% de las reservas mundiales).
- **Naturaleza:** extrae. **Patrón: acumula morosidad.**
- **Números:** morosidad 2.66% → 9.21% (2024), pendiente +0.58 pp/año, R²=0.40; Z-score 4.27 → 7.06 (2021). R_NPL 0.0273 → 0.101, **b_R = 1.055 (R²=0.653, n=12)**, banda descriptiva b ≥ 1. Cruce de alerta 2024 (recién). **1 señal** de decaimiento.
- **Contraseñal registrada:** las reservas líquidas SUBIERON de 11.6% a **106.5%** (2024), pendiente +5.84 pp/año, R²=0.803. El R-análogo dice deriva, la liquidez dice lo contrario. Se registra la tensión, no se resuelve: la morosidad sube y la liquidez también.

## 6. R(t) ANÁLOGO POR PAÍS

**Definición (misma aritmética que Ueno, datos distintos):** R_NPL(t) = NPL%(t) / (100 − NPL%(t)) — la parte morosa de la cartera sobre la parte sana. Es la misma forma parte/resto que la R(t) de Ueno (fondos públicos en el hub / fondos públicos en el resto del sistema), con la morosidad como "hub" interno de la cartera. **Ventana:** 2010–último dato (WDI, hasta 2024). **t-origen:** 2010 (t = año − 2009). **Ajuste:** log-log R(t) = a·t^b, valores > 0, n ≥ 5 para el ajuste, n ≥ 8 para reportar (mismas convenciones del análisis de decaimiento). **b_deriva del CSV de métricas** (sobre el indicador crudo) se reutiliza tras verificación por recomputación: **42/42 coinciden exactos** (23 de morosidad WDI + 19 de morosidad GFDD, a 3 decimales).

**Resultado (143 países con serie suficiente):**

| Clasificación por b (R-análogo) | Países | Lectura |
|---|---|---|
| b < 0 — convergencia / leapfrog | 81 | La morosidad relativa cae: el sistema se limpia |
| 0 ≤ b < 1 — deriva | 58 | La morosidad relativa crece, sublineal |
| b ≥ 1 — banda descriptiva, sin clasificar | 4 | Congo Rep. 1.597, Guinea Ecuatorial 1.366, Nepal 1.152, Mozambique 1.055 — NUNCA prueba de superlinealidad |

**Los 4 de la banda b ≥ 1** son deriva rápida sobre bases distintas: Congo Rep. (R_NPL 0.0097 → 0.180, R²=0.808) y Guinea Ecuatorial (0.0495 → 0.452, R²=0.849) son deriva real con buen ajuste; Nepal (0.0171 → 0.0486, R²=0.416, n=9) y Mozambique (0.0273 → 0.101, R²=0.653) son deriva sobre base chica. La banda b ≥ 1 no clasifica: no dice superlinealidad, dice "aquí la deriva es la más rápida del dominio, mírala aparte".

**Casos notables (R-análogo completo en `finanzas-mundo-snt-valores.csv`):**

| País | R_NPL primero → último | b_R | R² | n | Cruce alerta | Cruce crisis | Señales |
|---|---|---|---|---|---|---|---|
| Chad | 0.110 (2010) → 0.460 (2023) | 0.751 | 0.766 | 14 | 2010 | 2016 | 6 |
| Congo, Rep. | 0.0097 (2010) → 0.180 (2023) | 1.597 | 0.808 | 14 | 2017 | 2018 | 5 |
| Argelia | 0.224 (2010) → 0.261 (2024) | 0.138 | 0.115 | 15 | 2010 | 2023 | 5 |
| Guinea Ecuatorial | 0.0495 (2010) → 0.452 (2023) | 1.366 | 0.849 | 14 | 2013 | 2013 | 4 |
| Ucrania | 0.180 (2010) → 0.435 (2024) | 0.629 | 0.555 | 15 | 2010 | 2012 | 2 |
| Ghana | 0.221 (2010) → 0.279 (2024) | 0.094 | 0.091 | 15 | 2010 | 2017 | 0 |
| Bangladesh | 0.0194 (2011) → 0.234 (2024) | 0.685 | 0.612 | 14 | 2014 | — | 4 |
| Kenia | 0.0541 (2010) → 0.157 (2024) | 0.501 | 0.771 | 15 | 2017 | — | 3 |
| Nepal | 0.0171 (2016) → 0.0486 (2024) | 1.152 | 0.416 | 9 | — | — | 3 |
| Paraguay (plantilla) | 0.0142 (2010) → 0.0233 (2024) | 0.217 | 0.653 | 15 | — | — | 2 |

**b depende del origen del reloj** — como en Ueno: cada b se reporta con su ventana (2010–último), su t-origen (2010) y su n. Cambiar el origen cambia el b. Por eso el CSV lleva las tres cosas por país.

## 7. BANDAS TIPO ROCHE POR PAÍS

**Definición:** bandas sobre la serie propia de cada país, en forma R, con los umbrales de trabajo del análisis de decaimiento (NPL 10% alerta / 20% crisis, expresados en R): **alerta R_NPL > 0.10** (NPL > 9.09%), **crisis R_NPL > 0.25** (NPL > 20%). **No se transfiere el 0.10 de Ueno mecánicamente:** el 0.10 de Ueno es el cruce de R(t) de fondos públicos; el 0.10 de aquí es el umbral de alerta del propio dominio, expresado en la misma aritmética parte/resto. Lo que se traslada es la forma (bandas sobre la serie propia), no el número.

**Resultado:** de los 143 países con R-análogo, **66 cruzaron la banda de alerta** y **25 cruzaron la banda de crisis** dentro de su ventana 2010–último. Años de cruce de crisis (primer cruce en ventana): 2010, 2011, 2012, 2013, 2015, 2016, 2017, 2018, 2020, 2023.

**Cruces de los casos notables:**

| País | Cruce alerta | Cruce crisis | Qué pasó en el cruce |
|---|---|---|---|
| Chad | 2010 (ya estaba) | 2016 | NPL 18.8% → 22.9%; reservas líquidas en su mínimo 6.2% el mismo año |
| Congo, Rep. | 2017 | 2018 | NPL 16.2% → 22.5% |
| Argelia | 2010 (ya estaba) | 2023 | NPL 19.9% → 20.9% (lento, tras 13 años sobre alerta) |
| Guinea Ecuatorial | 2013 | 2013 | NPL 5.8% → 20.1% en un año (salto) |
| Ucrania | 2010 (ya estaba) | 2012 | NPL 14.7% → 20.4% (pre-guerra; la guerra lo llevó a 54.8% en 2017) |
| Ghana | 2010 (ya estaba) | 2017 | NPL 17.3% → 21.6% (pre-default; el default lo sostuvo arriba) |
| Bangladesh | 2014 | — | NPL cruzó alerta en 2014; la crisis no llegó (todavía) |
| Kenia | 2017 | — | NPL 5.1% → 13.6% (2024) |
| Paraguay | — | — | Nunca cruzó: R_NPL máximo 0.0233 |

**La regla de Ueno, aplicada aquí: mirar la DERIVA, no el nivel.** China con crédito/depósitos >200% no está en crisis; Argelia lleva 14 años sobre la alerta sin colapsar; Ghana cruzó crisis en 2017 y siguió. El cruce de banda fecha la ruptura estructural de la serie propia, no un delito ni una quiebra. Y al revés: un país puede estar sano en nivel y pudriéndose en deriva (Congo Rep. partió de NPL 0.96% en 2010 y cruzó crisis en 2018).

**Comparación con Ueno:** la R(t) de Ueno cruzó 0.10 en dic 2024 (R = 0.1021), un mes después de la Res. 093-046/2024 y en el mes en que empezó la captura masiva de CDA. En Finanzas-mundo no hay un evento fechado equivalente por país: los cruces se fechan, el evento que los explica (choque petrolero, guerra, default, sinceramiento) se registra aparte y no se infiere de la serie.

## 8. LECTURA MUNDO: la red micelial con competencia entre países

**La competencia SÍ aplica entre países** (regla de Elán: en ciudades/municipios la red es micelial sin competencia; entre países, sí). La red mundial es micelial en forma — un nodo central alimenta a los demás — pero los países compiten por el flujo: lo que uno acumula, otro lo deja de tener. Dos ejes, no uno: **acumulación** y **decaimiento**.

**Eje 1 — quién acumula a costa de quién.** Superávit comercial persistente 2015–2024 (% del PIB, años de superávit de 10): Luxemburgo +32.45% (10/10), Singapur +31.92% (10/10), Macao +31.68% (8/10), Gabón +30.02% (10/10), Irlanda +28.54% (10/10), Bermudas +25.71% (10/10), San Marino +25.25% (9/10), Emiratos Árabes Unidos +20.77% (9/10), Qatar +18.10% (8/10), Malta +16.27% (10/10). La lista mezcla centros financieros y ciudades-estado pequeños (el ranking en % del PIB favorece a las economías chicas) con exportadores de hidrocarburos. Los superavitarios grandes en dólares son China (+2.10% sobre un PIB gigante), Alemania (+5.38%) y Corea (+3.57%). El déficit persistente es la cara del drenaje: **Nepal −29.58%**, Líbano, Jordania.

**Eje 2 — la deriva se concentra en los nodos chicos.** Los 19 países con ≥3 señales son TODOS Nivel 3 (<1% de las reservas mundiales). Los hubs (N0–N2) tienen como máximo 1 señal: China 1 (crédito/depósitos >200%, ya en umbral, sin deriva), India 1 (el ESTIMADO de 2.5 años, DESACTUALIZADO), Rusia 1, Emiratos 1, Corea 1, México 1, Singapur 1, Turquía 1; Suiza, Japón, EE. UU. y Arabia Saudita, 0. **La sombra vive abajo, el hub acumula arriba.** No es una ley: es lo que muestran estos datos, con este método, en esta ventana.

**La tensión (Nepal):** acumula reservas a 12.62%/año con balanza comercial −29.58% del PIB — las reservas crecen por remesas, no por superávit (lectura del análisis de decaimiento) — y al mismo tiempo tiene 3 señales de decaimiento bancario. **Acumular reservas no es lo mismo que estar sano.** Suiza acumula a 9.05%/año con banca sana (0 señales); Nepal acumula a 12.62%/año con banca en deriva. El eje de acumulación y el eje de decaimiento son dos ejes.

**Los eventos exógenos son los que revelan.** Como Ueno (evento exógeno — resolución 2 nov 2026 — sobre un hub endógenamente frágil), en el mundo los eventos visibles son la guerra (Ucrania 30.3% de morosidad 2024), el default soberano (Ghana 21.8%) y el choque petrolero 2014–2016 (Chad, Congo, Guinea Ecuatorial, sin recuperación). El resto es deriva lenta, no evento.

**Tiempos restantes (ESTIMADO, nunca fecha de falla):** 63 países tienen estimación por extrapolación lineal; **32 ya están en umbral de alerta** en al menos un indicador. Las más cortas con datos corrientes (WDI hasta 2024): **Argelia 1.6 años ESTIMADO** (reservas líquidas, con la recuperación parcial 2020–2024 como contraseñal) y **Filipinas 2.4 años ESTIMADO** (reservas líquidas). Con datos GFDD hasta 2020/2021 (sin serie gemela corriente): Sierra Leona 1.2, Congo Dem. 1.3, Burundi 1.6, San Marino 4.8 años ESTIMADO. **Las 4 DESACTUALIZADAS se mantienen como tales:** India (2.5 años: morosidad WDI bajó de 7.94% en 2020 a 2.50% en 2024), Guinea (0.9: 9.38% → 6.69%), Gabón (1.7: 8.96% → 7.58%), Bután (3.9: 11.69% → 2.22%). Una estimación con datos hasta 2020 no sobrevive a los datos 2021–2024: se retira y queda la lección metodológica.

**La forma es la misma, el nivel es el proxy.** Cada país dibuja su propia deriva con los mismos indicadores; lo que cambia es el nivel y la velocidad. Chad a 31.5% de morosidad y Suiza a 0.83% no se comparan en nivel: se comparan en deriva dentro de su propio dominio. Normalizado a su propio R-análogo, el patrón es el mismo: la parte dañada crece contra la parte sana.

## 9. GAPS (registrados como gaps, nada inventado)

1. **Dato por banco.** El Banco Mundial agrega por país. La concentración del hub (qué banco concentra los depósitos públicos, qué banco presta a su grupo) se ve a nivel de entidad. Sin eso, el decaimiento es del sistema, no del nodo. El caso Paraguay lo prueba: Ueno cayó y el agregado del país apenas se movió. Fuentes candidatas: Bankscope/Orbis (pago), balances de bancos centrales por entidad, FSI del FMI por país (mismo nivel de agregación, no resuelve).
2. **Flujos entre países.** Quién le presta a quién, dónde se coloca el dinero. El Banco Mundial no lo tiene por país-par; el BIS (estadísticas bancarias locacionales, por país acreedor/deudor) sí. Es el siguiente dataset.
3. **GFDD termina 2020/2021.** No hay Z-score, capital ni liquidez GFDD post-COVID. La morosidad WDI llega a 2024 y es la única serie bancaria corriente. El panel de luz (§3) está congelado en 2020/2021.
4. **Deuda del gobierno central solo 120 países; deuda externa solo 133.** Los acreedores grandes (EE. UU., Japón, Reino Unido, Suiza) no reportan deuda externa en esta serie.
5. **Crédito del sector financiero solo 78 países.** Serie rala; no usarla como comparador global.
6. **Reservas en meses de importaciones** (`FI.RES.TOTL.MO`) está descargada pero no se usó: es el siguiente indicador para la suficiencia de reservas.
7. **Sin serie de fondos públicos por banco.** El análogo global de la R(t) de Ueno no existe en el Banco Mundial: se construye país por país desde los bancos centrales. El R-análogo de este documento (§6) es sobre morosidad, no sobre fondos públicos.
8. **ASI no computable.** Sin datos de eventos conductuales por país (el ASI del repo es δH·α/F, umbral 0.167; aquí no hay δH ni α medibles). **u NULL** (tela de incertidumbre, Axioma 0: u no está definida en ningún dominio).
9. **El puente no está medido.** Corresponsalía, offshore y remesas son el rol puente a escala mundo, pero estos datos no los miden. La única pista medida es indirecta: Nepal acumula reservas con balanza −29.58% (remesas, lectura del análisis de decaimiento).
10. **Límite del método de señales:** detecta deriva, no saltos de nivel (Ghana: 0 señales con NPL 21.8% post-default). Un país puede cruzar crisis sin una sola señal.

## 10. Verificación y reproducibilidad

- **b_deriva verificada por recomputación:** 42/42 coinciden exactos (23 de morosidad WDI + 19 de morosidad GFDD, a 3 decimales, mismo n), recomputadas desde la tabla limpia con la misma fórmula (log-log, t = año − 2009). Detalle en `finanzas-mundo-snt-verificacion.json`.
- **Titulares re-verificados contra los CSV:** reservas mundiales USD 10.133 billones (2010) → 14.867 billones (2024); China 23.25% (USD 3.456 billones); top 6 = 52.18%; mediana de morosidad 3.16% (154 países); 26 países ≥10%, 5 ≥20%; 92 países con ≥1 señal, 19 con ≥3; 63 con tiempo estimado, 32 ya en umbral; 66 cruces de alerta y 25 de crisis en el R-análogo (143 países).
- **Scripts:** `aplicar_snt_finanzas_mundo.py` (esta aplicación: verificación + R-análogo + luz + niveles), `banco-mundial/analizar_decaimiento.py` (métricas y b_deriva), `banco-mundial/limpiar_banco_mundial.py` (tabla limpia), `banco-mundial/descargar_banco_mundial.py` (descarga).
- **Licencia de los datos:** CC BY 4.0 (Banco Mundial). Países y agregados únicamente, cero personas.

---

*Finanzas-mundo es el primer dominio nuevo sometido a la SNT después de Ueno. El siguiente en línea es Estado (DNCP + MEF, el más completo después de Finanzas-mundo). Salud y Energía esperan las definiciones de Elán (hub/sombra en Salud; flujo/hub/sombra/puente en Energía).*
