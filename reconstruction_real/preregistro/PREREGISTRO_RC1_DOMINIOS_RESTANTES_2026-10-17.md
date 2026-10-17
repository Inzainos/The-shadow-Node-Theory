# Pre-registro — RC1 en los dominios restantes: ¿el veredicto sobre `b ≥ 1` se replica en A, E2 y C?

**Fecha:** 2026-10-17 · **Rama:** `local/rc1-dominios-restantes-v2.6.1` · **Base:** `main` en `1488144`
· **Autor de la teoría:** Elán Zainos Corona · **Análisis:** opencode, a pedido del autor.

Este documento se compromete **antes de descargar un solo byte de datos nuevos y
antes de escribir el script**. El commit fechado es el sello de tiempo. Todo lo que
se reporte después debe seguir estas reglas; cualquier cambio se declara en la
sección **Desviaciones** del informe, con motivo, y nunca en silencio.

## 0. El pendiente, exactamente

El README arrastra desde la auditoría v32 el pendiente *"Test b ≥ 1 on the other
domains' raw series"*. RC1 (2026-10-02, `audits/RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md`)
cerró la pregunta sobre los tres dominios que entonces tenían serie cruda — E3
(234), B (446) y ACO (18) — con dos resultados: (i) el AIC no es admisible en la
banda `b ≥ 1` en ninguno (error de selección 80.3% / 96.8% / 48.9%, umbral 20%), y
(ii) una exponencial verdadera ajustada como ley de potencia cae en `b ≥ 1` casi
siempre en las bandas altas, por lo que la etiqueta "Roche Radius" quedó retirada.

**Lo que RC1 no probó:** los demás dominios del corpus. Este pre-registro extiende
la misma maquinaria a los tres que sí tienen serie cruda reconstruible desde
fuentes públicas:

| Dominio | Casos | b máximo publicado | Serie cruda | Papel |
|---|---:|---:|---|---|
| **A** — ciudades | 4 | +0.2384 | Candidata: `data/wup2018_aglomeraciones_1950_2018.csv.gz` (ya versionado); UN Demographic Yearbook si hace falta | **Primario** |
| **E2** — lince-liebre | 2 | +0.5483 | Elton & Nicholson 1942 (R `lynx`, Rdatasets) y MacLulich 1937 | Secundario |
| **C** — regiones | 23 (el C_001 México es rango-tamaño, sin serie temporal) | +0.8914 | US Census, población estatal anual 1900-2025 (descarga) | **Primario** |
| D — digital | 3 | — | Propietaria (HackerEarth) | **Excluido y contado** |
| E1 — invasión | 4 | +2.89 | Declarado no reproducible el 2026-09-27 | **Excluido y contado** |
| F1-F3 | 4 | +1.27 | Los ajustes publicados son relaciones masa/órbita, no trayectorias R(t) en el tiempo | **Excluidos y contados** |
| E3, B, ACO | — | — | Ya probados en RC1 | **No se repiten** |

**Nota honesta sobre el alcance:** A, E2 y C no tienen ni un caso con `b ≥ 1`
publicado (el máximo es +0.8914). Por eso aquí la pregunta RC1 no puede ser "¿son
los casos superlineales de este dominio mala especificación?" — no existen. La
pregunta que sí se puede responder por dominio, y es la que este diseño fija:

> **(P0) Con la estructura de ruido `(n, ρ AR(1), σ)` real de cada dominio, ¿el
> AIC de `comparar_modelos` discriminaría a `b ≥ 1` si ahí existiera un caso
> así? Y (P5) ¿una exponencial verdadera con el ruido de este dominio produciría
> una `b` aparente ≥ 1?**

Eso mide si el veredicto de RC1 —"no decidible por AIC; la etiqueta es un
renombre del desajuste"— es una propiedad del estimador a secas o depende de la
estructura de serie del dominio. C es el caso de prueba más informativo: sus
series son las más largas del corpus (n = 126 contra 69 de B y 60 de E3) y su
autocorrelación es hoy desconocida.

## 0.1 Regla por dominio, aplicada desde el diseño

Como en RC1: cada dominio se prueba **por separado**, con su serie cruda y su
propio proxy; los resultados se cuentan por dominio, nunca se agrupan ni se
promedian; no se ordena dominios en escala compartida ni se lee su diferencia como
medición (Axiomas 0.1 y 2, `papers/marco_teorico.md:110,163`). Una discrepancia
entre dominios es un resultado, no un problema que resolver.

## 0.2 Ceguera declarada

- **Visto:** los resultados completos de RC1 (tasas de error de selección por banda
  y dominio; fracciones de falsa `b ≥ 1` de P5); los `b`, R², p y `n` publicados de
  A, E2 y C en `by_domain/`; el esquema (columnas, cobertura) del archivo WUP
  versionado; la receta de E3 como precedente de identificación; el docstring de
  `comparar_modelos` con su advertencia de calibración.
- **No visto, y no existe en el repositorio:** ninguna serie cruda de A, E2 o C;
  ningún Durbin-Watson, ρ AR(1) ni σ de estos dominios; ningún resultado de AIC
  sobre ellos.

## 0.3 Reglas generales

1. **Se reporta todo resultado**, por dominio, favorable o no, incluidos los "no
   reproducible" y los "no evaluable" con su motivo.
2. **α = 0.05.** Pruebas de una cola solo donde RC1 fijó la dirección (P2 y P3,
   con la dirección fijada por el resultado previo del ACO); se reporta también el
   p de dos colas.
3. **Semilla fija:** `20261017` en toda aleatoriedad.
4. **Log obligatorio** en `reconstruction_real/logs/` y **SHA-256** de cada
   descarga anotado en `data/FUENTES.md`.
5. **Nada se recorta por su valor.** Las exclusiones son por falta de serie cruda
   o por diseño (rango-tamaño, datos propietarios) y se cuentan.
6. **No se modifica el corpus** ni se reestima ninguna `b` publicada.
7. **Antes de calibrar, reproducir:** cada dominio pasa primero por la
   identificación de receta (Fase 0). Sin reproducción no hay calibración —
   calibrar con una serie equivocada sería afinar el instrumento sobre el sistema
   equivocado.

---

## 1. Fase 0 — Identificación de recetas (exploratoria, con criterio fijado)

Ninguno de los tres dominios tiene la receta documentada en el repo (a diferencia
de E3). Se aplica el método del pre-registro 2026-09-27, punto 3: lista de recetas
**ordenada**, se acepta la primera que reproduzca el `b` publicado dentro de
±0.01 en ≥ 90% de los casos emparejables.

**Regla de decisión, más estricta que la de E3:** si ninguna receta de la lista
alcanza el 90%, el dominio se declara **NO REPRODUCIBLE** y **no se calibra**. En
E3 la receta de máxima coincuencia se usó "rotulada como aproximación" para
corregir por autocorrelación; aquí la salida alimenta una **calibración por
simulación**, y una serie aproximada contamina `(ρ, σ)` — el instrumento mismo. Sin
receta exacta no hay prueba.

### 1.1 Dominio A (4 casos) — sin descargas nuevas

Pares publicados: Tokyo→Osaka (2000-2020, n=7), Tokyo→Yokohama (2000-2020, n=7),
Paris→Lyon (1999-2021, n=6), Madrid→Barcelona (2001-2023, n=15). Recetas
candidatas, en este orden, todas sobre `data/wup2018_aglomeraciones_1950_2018.csv.gz`
(R = pob_hub/pob_node, t = 1..n, ajuste OLS log-log idéntico a `calc()` de
`expand_B_massive.py`):

1. Anual dentro de [año_ini, año_descripción] recortada a 2018 (fin del WUP).
2. Cada 3 años desde año_ini (recortada a 2018).
3. Cada 4 años desde año_ini.
4. Cada 5 años desde año_ini.
5. Anios de censo del país dentro de la ventana (JP 2000/05/10/15/20; FR
   1999/2006/2011/2016/2021(≈2018); ES 2001/2011/2021(≈2018)).
6. Serie completa WUP 1950-2018.

Si ninguna reproduce 4/4 (el 90% de 4 casos son 4 casos), se declara no
reproducible. **Salvedad pre-declarada:** con n = 6-7 puntos, la receta puede
reproducir el `b` por azar aunque sea la equivocada; la Fase 1 reportará este
riesgo junto a los resultados de A.

### 1.2 Dominio E2 (2 casos)

- **E2_01** (Lynx→Hare, Hudson Bay 1900-1920, n=21, b=+0.5483): la serie de
  liebres de MacLulich 1937. Lista de fuentes candidatas: (a) Rdatasets/CRAN si
  existe un dataset público con la tabla lince-liebre de MacLulich; (b) la tabla
  reproducida en publicaciones de acceso abierto que citen a MacLulich 1937 con
  los datos. Recetas: R = liebre/lince y R = lince/liebre, anual 1900-1920, t=1..21.
  Si no se localiza la tabla pública, se declara no reproducible.
- **E2_02** (Lynx vs equilibrio 1821-1850, n=30, b=−0.2592, "Elton & Nicholson
  1942 (Rdatasets)"): serie R `lynx` (Elton & Nicholson; anual 1821-1934).
  Recetas candidatas, en orden: R = x_t / media(x en 1821-1850); R = x_t / media(x
  en 1821-1934); R = x_t / mediana(x en 1821-1850); R = x_t / x_1821; todas con
  t=1..30 sobre la ventana 1821-1850. Se acepta la primera que reproduzca b
  dentro de ±0.01.

### 1.3 Dominio C (23 casos; C_001 excluido por diseño)

22 pares de estados EEUU (C_002..C_024, n=126, 1900-2025) + exclusión contada de
C_001 (México, ajuste rango-tamaño sobre 32 entidades, sin serie temporal R(t)).

Fuente: población estatal anual 1900-2025 del US Census Bureau (Population
Estimates Program / tablas históricas). Rutas de acceso candidatas, en orden:
(a) tablas descargables de census.gov (popest/históricas estatales); (b) FRED
`fredgraph.csv` por estado (serie anual Census-based, sin API key). Se registra
URL, fecha y SHA-256 de lo descargado en `data/FUENTES.md`.

Receta única pre-especificada: R = pob_hub/pob_node, anual 1900-2025, t=1..126,
OLS log-log. Aceptación: ≥ 21 de 22 casos (90%) dentro de ±0.01 del `b`
publicado. Si la fuente sólo cubre 1900-2024 (n=125) se declara la desviación y
el umbral se mantiene sobre los casos emparejables.

---

## 2. Fase 1 — La maquinaria RC1, por dominio

Solo para los dominios cuya receta pasó la Fase 0. Para cada caso: ajuste OLS
log-log sobre la serie identificada, verificación contra el `b` publicado, y
extracción de la terna **(n, ρ AR(1), σ)** — ρ de los residuos del caso, σ su
desviación estándar — exactamente como RC1.

### P0 — Compuerta: error de selección del AIC, por banda de b

Para cada caso y cada banda de `b` — observada si hay casos, y **contrafactual**
para las bandas sin casos — se simulan series desde una **ley de potencia
conocida** (la `b` de la banda) con la σ y la ρ del caso real y su misma n;
`N_CAL = 200` réplicas por caso-banda. Todo lo que el AIC elija que no sea
"potencia" es error por construcción. Bandas y centros contrafactuales:

| Banda | Centro simulado | Uso |
|---|---:|---|
| `b < 0.5` | b del caso real (si el caso está en la banda) | observada |
| `0.5 ≤ b < 1.0` | b del caso real (si aplica) | observada |
| **`1.0 ≤ b < 1.5`** | **b = 1.25** con la (n, ρ, σ) de cada caso | **contrafactual** |
| **`b ≥ 1.5`** | **b = 1.75** con la (n, ρ, σ) de cada caso | **contrafactual** |

**Umbral de admisión (el mismo de RC1):** la banda `b ≥ 1` de un dominio es
interpretable solo si su tasa de error de selección es **< 20%**.

### P5 — Prueba de tautología (no usa el AIC; no cae con la compuerta)

Para cada caso se simula desde una **exponencial conocida** — ajustada al rango
de la serie real — con la σ y la ρ del caso y su misma n, y se ajusta como ley de
potencia. Se reporta la fracción de réplicas con `b` aparente ≥ 1 (y, como
control, la fracción con `b` aparente ≥ 0.5).

### P1-P4 — Se reportan, se interpretan solo si P0 admite

P1: conteo de ganadores AIC por caso (potencia/exponencial/lineal). P2: Spearman
`(b, ΔAIC_potencia)` dentro del dominio (una cola, dirección negativa fijada por
el ACO). P3: Fisher exacto (b≥1 × gana potencia) — **no evaluable** en dominios
sin casos superlineales; se declara. P4: fracción de superlineales que ajustan
mejor con otra forma — ídem, no evaluable; se declara.

---

## 3. Qué significa cada desenlace (escrito antes de ver nada)

Por dominio, sin agrupar:

| Desenlace | Lectura |
|---|---|
| P0 ≥ 20% en la banda contrafactual `b ≥ 1` | **El dominio no es interpretable por AIC a `b ≥ 1`.** El veredicto de RC1 se replica en su estructura de ruido. Se reporta la tasa exacta, que puede diferir de 80-97%: es la medida de este dominio |
| P0 < 20% en `b ≥ 1` | **El dominio SÍ discriminaría a `b ≥ 1`.** El "no decidible por AIC" de RC1 es dominio-dependiente, no universal — y se reporta como tal, sin agrupar con los otros tres |
| P5 alto (≥ 50% de falsa `b ≥ 1`) en las bandas altas | La etiqueta `b ≥ 1` sería tautológica también aquí: un desajuste exponencial se disfraza de superlineal con el ruido de este dominio |
| P5 bajo (< 10%) | En este dominio una `b ≥ 1` observada **no** sería mero renombre del desajuste; el umbral discriminaría. Se reporta junto al P0 correspondiente |
| Receta no identificada (Fase 0 < 90%) | El dominio se declara **no reproducible desde fuentes públicas al alcance**, sus casos se cuentan, y queda registrado que el pendiente del README no es cerrable hoy para ese dominio |
| ρ AR(1) cercana a cero en C (series largas de población) | Resultado en sí mismo: documentaría que el defecto de B (ρ≈0.94) no es universal y que la inferencia por caso de C es otra cosa |

**Lo que este pre-registro NO hace.** No reestima ninguna `b` publicada, no
modifica el corpus, no toca la ortogonalidad b ⊥ Δ, el gradiente de Tlaxcala ni la
capa ACO-A, no reabre el retiro de la etiqueta "Roche Radius" (los dominios sin
casos superlineales no pueden reabrirlo por sí solos), y **no compara dominios
entre sí** más allá de contar sus resultados independientes.

## 4. Salidas previstas

- `reconstruction_real/code/rc1_dominios_restantes.py` (con log).
- `reconstruction_real/data/rc1_resto_recetas.csv` — Fase 0 por caso.
- `reconstruction_real/data/rc1_resto_por_caso.csv` — una fila por caso con b, dw,
  ρ, σ, n, y las tasas P0/P5 del caso.
- `reconstruction_real/data/rc1_resto_calibracion.csv` — P0 y P5 por dominio y banda.
- `reconstruction_real/audits/RESULTADOS_RC1_DOMINIOS_RESTANTES_2026-10-17.md`,
  con tabla diseño → resultado → decisión por dominio y sección **Desviaciones**.
- `data/FUENTES.md` (descargas nuevas) y `CHANGELOG.md`.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-17*
