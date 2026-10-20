# FUENTES.md — provenance de datos externos

Este archivo ancla las **fuentes externas** del corpus SNT: de dónde salen, en
qué versión, y el checksum de los archivos derivados que sí viven en el repo.
Nació de un hallazgo de la auditoría integral v32: los resultados no estaban
anclados a una versión de datos, así que dos personas ejecutando el mismo
script en fechas distintas podían obtener cifras distintas sin saberlo.

> Regla del repo (AGENTS.md): **real data first**, reproducibilidad + provenance.
> Este documento es el índice de provenance. Actualízalo cuando cambie una
> fuente.

---

## 1. Fuentes externas (estado por fuente)

### `data/mpd2020.xlsx` — **edición del dominio B, presente en el repo** (descargada 2026-09-27)

- **Qué es:** Maddison Project Database 2020, archivo original de la GGDC (hoja
  "Full data": `countrycode, country, year, gdppc, pop`; 169 países; años
  1–2018; PIB per cápita en dólares internacionales de 2011).
- **Por qué esta edición:** es la que produjo el dominio B publicado. Se
  identificó el 2026-09-27 probándola contra `by_domain/dominio_B_real.csv`: con
  ella, `expand_B_massive.py` regenera los 446 casos **byte a byte** (mismo
  SHA-256, `e0c7738a…`). La edición no estaba fijada en el repo; en Google
  Drive del autor solo había `mpd2023_web.xlsx` (edición 2023, distinta).
- **Quién la usa:** `reconstruction_real/code/build_maddison_mpd2020_csv.py`
  → `data/maddison_mpd2020.csv` (mismos datos con los nombres de país de OWID,
  traducidos por ISO3; "Sudan (Former)" → "Sudan") → `expand_B_massive.py` y
  `prueba_discriminante_dominio_B.py` (por defecto desde 2026-09-27).
- **Peso:** dominio B = **446 casos = 62% del corpus**.
- **Cita:** Bolt, J. & van Zanden, J. L. (2020). *Maddison style estimates of
  the evolution of the world economy. A new 2020 update.* Maddison Project
  Working Paper WP-15, University of Groningen.

| Campo | Valor |
|---|---|
| URL de descarga | <https://www.rug.nl/ggdc/historicaldevelopment/maddison/data/mpd2020.xlsx> |
| Fecha de descarga | 2026-09-27 |
| Tamaño | 1,764,793 bytes |
| Licencia | CC BY 4.0 (citar según la política de citas de la hoja "Notes") |
| SHA-256 `mpd2020.xlsx` | `d20853c2e0930d6855fb6d8138da11f24fcf313d234e2db9773ea1f551adfec3` |
| SHA-256 `maddison_mpd2020.csv` | `1c0b15ae4b78d54134d3c781e361784ee06c8519762ca6ceb45ef65fc31d54c0` |

### `data/owid-maddison.csv` — **presente en el repo** (descargado 2026-07-25)

- **No es la edición del corpus.** Es una edición OWID posterior; con ella el
  dominio B solo se reproduce de forma aproximada (ver la medición abajo).
- **Quién la usa:** la corrida de sensibilidad de
  `reconstruction_real/code/prueba_discriminante_dominio_B.py` (con
  `--maddison data/owid-maddison.csv`; por defecto el script usa MPD2020 desde
  2026-09-27), `reconstruction_real/code/expand_dominio_B.py` (línea 11), la
  medición de sensibilidad a la edición del runner de la auditoría y, solo
  como tabla de nombres Code → Entity, `build_maddison_mpd2020_csv.py`.
- **Fuente primaria:** Maddison Project Database (Bolt & van Zanden), Groningen
  Growth and Development Centre (GGDC), vía Our World in Data.
- **Cuidado — dato vivo:** el Maddison Project **revisa sus estimaciones
  históricas de PIB entre ediciones**. Por eso se fija edición + fecha + SHA-256.

| Campo | Valor |
|---|---|
| Origen | OWID grapher `gdp-per-capita-maddison` (base: Maddison Project Database, cobertura hasta 2022 → release 2023) |
| URL de descarga | <https://ourworldindata.org/grapher/gdp-per-capita-maddison.csv> |
| Fecha de descarga | 2026-07-25 |
| Columnas conservadas | `Entity, Code, Year, GDP per capita` (se descartó la columna vacía de anotaciones) |
| Cobertura | 178 entidades · años 1–2022 · 21,586 filas |
| Licencia | OWID: CC BY 4.0 (atribuir Maddison Project Database + Our World in Data) |
| SHA-256 | `6e905c41324d50f2e4e468bad9d204a1efd44f6f34368c98425e8e0b33d6a4ec` |

> **Nota de reproducibilidad:** esta es la edición **vigente** de OWID/Maddison
> al 2026-07-25, no necesariamente la que se usó para construir
> `dominio_B_real.csv` originalmente. Para la prueba discriminante (b vs brecha
> inicial) eso no importa —testea una correlación, no reproduce el ajuste—, pero
> re-generar el dominio B con esta edición puede dar cifras algo distintas a las
> publicadas (el Maddison revisa el PIB histórico entre ediciones). Cobertura
> sobre el corpus: 102/103 países (falta "Sudan"), 441/446 pares con `year_min`
> disponible.
>
> **Medición (2026-09-27):** regenerado con `expand_B_massive.py` sobre esta
> edición, el dominio B da 441 casos vs 446 publicados; 408 pares comunes,
> corr(b) = 0.979, signo coincide 396/408 y solo 12/408 b idénticos. La
> diferencia confirma que la edición original no es esta: resultó ser el
> Maddison Project Database 2020 (sección anterior), con el que la
> reproducción es exacta. El runner `snt_auditoria_integral_v32.py` repite ambas
> mediciones en cada ejecución.

### `data/COW_Trade_4.0.zip` — **comercio bilateral, presente en el repo** (descargado 2026-09-27)

- **Qué es:** Correlates of War (COW) Trade Data Set v4.0 (Barbieri, K. & Keshk,
  O. M. G.), comercio diádico 1870–2014 y totales nacionales, en millones de USD
  corrientes. Contiene `Dyadic_COW_4.0.csv`, `National_COW_4.0.csv` y el codebook.
- **Definiciones verificadas en el codebook:** `flow1` = importaciones del país A
  (`importer1`) desde B; `flow2` = importaciones de B desde A; `-9` = faltante.
- **Quién la usa:** `reconstruction_real/code/build_comercio_bilateral_cow.py`
  → `data/comercio_bilateral.csv` → Bloques 2–3 de
  `prueba_discriminante_dominio_B.py`.
- **Reglas de entidad** (no se sustituyen Estados; esos años cuentan en los
  totales de los socios pero no se asignan al corpus): URSS 1917–1991 bajo
  "Russia"; Yugoslavia 1918–2005 bajo el código de Serbia; Vietnam del Norte
  < 1976; Pakistán con Pakistán Oriental < 1972; Czechia solo desde 1993.
- **Cita:** Barbieri, K. & Keshk, O. M. G. (2016). *Correlates of War Project
  Trade Data Set Codebook, Version 4.0.* Online: <https://correlatesofwar.org>.
  Barbieri, K., Keshk, O. M. G. & Pollins, B. (2009). Trading Data: Evaluating
  our Assumptions and Coding Rules. *Conflict Management and Peace Science*
  26(5), 471–491.

| Campo | Valor |
|---|---|
| URL de descarga | <https://correlatesofwar.org/wp-content/uploads/COW_Trade_4.0.zip> |
| Fecha de descarga | 2026-09-27 |
| Tamaño | 12,383,657 bytes |
| SHA-256 `COW_Trade_4.0.zip` | `c44c4b5ce62e68865368482c428306df4624d3a39edec29adc1aa2c0928f7cc7` |
| SHA-256 `comercio_bilateral.csv` | `9625f8403800f6834c5ebd03a5ab7c094d9be603c4954561de6be66ce7eea6cb` |

### Fuente de E3 (COVID-19) — series crudas **recuperadas** (2026-09-27)

- **Quién la usa:** el dominio E3 (234 casos) y el dominio nuevo E4 (mpox) del
  pre-registro 2026-09-27.
- **Archivo:** Our World in Data, `owid-covid-data.csv` (repositorio
  owid/covid-19-data), descargado el 2026-09-27 de
  <https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv>.
  El archivo completo (98 MB) no se versiona (`data/raw_covid/`, en .gitignore);
  se versiona el subconjunto `data/owid_covid_casos_totales.csv.gz`
  (iso_code, continent, location, date, total_cases).
- **Receta de E3 identificada** (`reconstruction_real/code/covid_E3_series_crudas.py`):
  casos acumulados, 60 días desde el primer día con ≥ 100 casos; reproduce 233/234
  b publicados dentro de ±0.01 (Timor Oriental no). E1 no es reproducible con las
  construcciones naturales.

| Campo | Valor |
|---|---|
| Fecha de descarga | 2026-09-27 |
| SHA-256 `owid-covid-data.csv` | `8473d0f0fdf962e1ffbd5b85b18726fc96a49bab109e271186c339725a12b10c` |
| SHA-256 subconjunto `owid_covid_casos_totales.csv.gz` | `21869b75d0e466f3e4a7d1bfc370fa1705e64e51bfb8739d561efaaa62e1473d` |

### Fuentes del pre-registro 2026-09-27 (puntos 2, 4 y 5)

Descargadas el 2026-09-27, **después** de subir el pre-registro
(`reconstruction_real/preregistro/PREREGISTRO_2026-09-27.md`, commit `c319fac`).
Los crudos grandes no se versionan (`data/raw_*`, en .gitignore); se versionan
subconjuntos derivados, y cada script verifica el SHA del crudo cuando está
presente.

| Fuente | Crudo (SHA-256) | Subconjunto versionado (SHA-256) | Uso |
|---|---|---|---|
| OWID mpox — `owid-monkeypox-data.csv` (<https://raw.githubusercontent.com/owid/monkeypox/main/owid-monkeypox-data.csv>) | `2764761fd455f9fb295101129b10e37cf1f4e7acf1ae3c779b6f6d2b25b2c927` | `data/owid_mpox_casos_totales.csv.gz` — `bc7d9ca5476448d62fd201e07a2af5e7519cda227730e38c0c0f2bd41b3c41c0` | Dominio E4 (punto 2) |
| StatCounter Global Stats, mundial mensual 2009-01..2024-12 (browser, search_engine, os_combined, social_media: todas las plataformas; vendor: móvil), exportación CSV de <https://gs.statcounter.com> | browser `4811c535…`, search_engine `158017b6…`, os_combined `eb3a5703…`, social_media `1b45289f…`, vendor `d8983f44…` (completos en el script) | `data/statcounter_2009_2024.csv.gz` — `851ed4eedcff152724af3e3c84325810f2211712361ac72b3282c6b9f223a118` | Dominio D2 (punto 2) |
| ONU, World Urbanization Prospects 2018 — `WUP2018-Excel-files.zip` (<https://population.un.org/wup/assets/Download/Archive/WUP2018-Excel-files.zip>), archivo `WUP2018-F22-Cities_Over_300K_Annual.xls` | zip `80eb71bbabb46cb2e1599b51b16133bf28b0a99a541d72de20a1248ec6170a75`; F22 `4366cc15ecdda4d9ab420adfe730da6a7e35a8334615f50172a08d60b121c11c` | `data/wup2018_aglomeraciones_1950_2018.csv.gz` — `8eb47691607e7e9a3cafb0c3049d3dff51b4c6bd8c1927c8eb11398baf2d0665` | Punto 4 (disparadores) y dominio A2 (punto 2) |
| Binance, archivo público de velas diarias spot (<https://data.binance.vision>), todos los pares contra USDT salvo estables/fiat y apalancados | por par en `data/raw_binance/klines_1d/` | `data/binance_cierres_diarios.csv.gz` — `fcb2ad7e34f7b5d0ad3ee4a685f952f3e9391bc9d85212b2eb110428d375915e` (663 pares, 2017-08-17..2026-08-31) | Punto 5 (ortogonalidad y hazard cripto) |
| FDIC BankFind API — instituciones (índice `institutions_20260925090006`) y quiebras (índice `failures_1787667198788`), <https://api.fdic.gov/banks> | institutions `8d410c2583a59d7b4540046f77f28dd6fa6761beb816ec94a7531d4fb4c0003e`; failures `65e727fff36cc9bf86a772e7cec4dd8d0b8368f2990b945742e40f0ddc90161c` | `data/fdic_instituciones_2026-09-25.csv.gz`, `data/fdic_quiebras_2026-08-25.csv.gz` | Punto 5 (hazard bancos) |


### Pre-registro npm 2026-10-02 (capa ACO-A en software libre)

Aplicación independiente, fuera del corpus de 721 casos. Consultadas el 2026-10-02.

| Fuente | Uso |
|---|---|
| `https://replicate.npmjs.com/_all_docs` | Marco de muestreo (4,446,361 paquetes). Paginado con `startkey`, máximo 10,000 filas por petición |
| `https://registry.npmjs.org/{paquete}` | Nacimiento (`time.created`), versiones, `deprecated`, repositorio |
| `https://api.npmjs.org/downloads/range/{inicio}:{fin}/{paquetes}` | Series diarias. Máximo **128 paquetes** por petición y **365 días** en consulta por lote (18 meses si es un solo paquete) |
| `https://api.osv.dev/v1/query` | Avisos de vulnerabilidad con fecha y severidad |

Los crudos quedan en `data/raw_npm/` (no versionado, 15 MB el mayor). **Su hash sí
queda registrado**, para que se pueda verificar que un crudo reconstruido es el mismo
que produjo estos resultados:

| Crudo (no versionado) | SHA-256 |
|---|---|
| `data/raw_npm/descargas.jsonl.gz` (series diarias, 15,486,679 bytes) | `455acba13c8b8d951243bbf3ef23e5ead4bf4a8271ec8e599c74f7a19d31ac71` |

Salidas versionadas:

| Archivo | SHA-256 |
|---|---|
| `reconstruction_real/data/npm_cohorte_aco.csv.gz` (450 paquetes) | `c4bfbf0513954911ad1c6d5e445ec01ff8d6bab47453d90bfc89428672a1c58b` |
| `reconstruction_real/data/npm_hazard_bandas.csv` | `981a0781668a9b9daf68f21e2783e572ffb652dde954e762f97f74f8fa5fe203` |
| `data/npm_descargas_mensuales_deriva.csv.gz` (agregado mensual de los 450; 35,002 filas `nombre,mes,descargas`; 183,179 bytes) | `20fc2f6b6b70796020cd75a182df6de5913ef9942a526ebb71ff77f88338345b` |

El agregado mensual es el **insumo exacto** del brazo npm de la prueba de deriva, y
está versionado precisamente para que esa prueba sea reproducible sin los 15 MB del
crudo. `deriva_forma_friccion.py` lo prefiere si está presente y recae en el crudo si
no, con un `warning` en el log. Verificado: con el derivado, las dos salidas de la
prueba reproducen sus SHA-256 registrados **al bit**. Conserva el orden de paquetes
del crudo, no el alfabético, porque el nulo por caso consume el RNG caso por caso.

Nota de calidad: el muestreo aleatorio del registro completo está dominado por la cola
larga, así que la codificación de fricción a priori resultó degenerada (0 paquetes de
fundación, 3 corporativos) y no es aprovechable en esta cohorte.

Notas de calidad: WUP incluye solo aglomeraciones con ≥ 300 mil habitantes en
2018 (filtro de supervivencia); la base de la FDIC no registra cierres antes de
1970; 41 instituciones tienen fecha de fundación de relleno (01/01/1800).

### Pre-registro rango-tamaño internacional 2026-10-02 (réplica del Módulo de N-cuerpos)

Aplicación independiente, fuera del corpus de 721 casos. Seis niveles territoriales
de Brasil y la Unión Europea, de 27 a 5,570 unidades, más México como referencia.
Año **2021** en todas las fuentes. Consultadas el 2026-10-02.

| Fuente | Uso | Unidades utilizadas |
|---|---|---|
| `https://apisidra.ibge.gov.br/values/t/5938/n3/all/v/37/p/2021` | PIB por estado, en Mil Reais | 27 |
| `https://apisidra.ibge.gov.br/values/t/5938/n6/all/v/37/p/2021` | PIB por municipio, en Mil Reais | 5,570 |
| `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10r_3gdp?format=JSON&time=2021&unit=MIO_EUR` | PIB regional total | 111 NUTS1, 293 NUTS2, 1,327 NUTS3 |
| `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10r_3gdp?format=JSON&time=2021&unit=EUR_HAB` | PIB regional per cápita (secundaria) | 110 NUTS1, 285 NUTS2, 1,300 NUTS3 |
| `data/matriz_mexico_32.csv` | `pct_pib` (primaria) y `pib_pc` (secundaria) | 32 |

Los crudos quedan en `data/raw_rango_tamano/` (no versionado):

| Archivo crudo | Bytes | SHA-256 |
|---|---:|---|
| `ibge_n3_2021.json` | 8,084 | `b60e7b58e17c81a06d12196e37a15539ab27eca1e7fae351c0384b4dbdc88550` |
| `ibge_n6_2021.json` | 1,577,341 | `619f9caf07f59d4f85fdf128389ce001c593199b2d78076f876122ae66d024e3` |
| `eurostat_mio_eur_2021.json` | 98,639 | `bb237abf4695e8e353d60cb4561f0c57be86096d70dcba113c1e58e5dacb27a7` |
| `eurostat_eur_hab_2021.json` | 94,737 | `9f79df345d31300ee828962e4005c2be27f3ce68e402031670e295a981bda251` |

Salidas versionadas:

| Archivo | SHA-256 |
|---|---|
| `reconstruction_real/data/rango_tamano_internacional.csv` | `58392810079966d929d9d6d927c1c5fdb2f127b559777c18c81a6326431b47b5` |
| `reconstruction_real/data/rango_tamano_poder.csv` | `99e424c52328c1b71b0b8ab6a769b925d3f0be5d24a03452a0e5f28fbf4d7c6b` |
| `reconstruction_real/data/rango_tamano_percapita.csv` | `1ecd50e67afbdc12eee5b7998d26d8f7c031025824e779eebdef9e6b9512af9f` |
| `reconstruction_real/data/rango_tamano_diagnostico.csv` | `67854656728ac25326b909600dc6464570107a132b36bb9524b464ad9c90c4cd` |

**Nota de calidad, importante.** Eurostat publica, por país y por nivel, un código
residual etiquetado **"Extra-Regio"** (`BEZ`/`BEZZ`/`BEZZZ`, `FRZ`/`FRZZ`/`FRZZZ`, …)
con la actividad económica que no puede asignarse a ninguna región: embajadas,
plataformas marinas, buques. Son **16 por nivel**, tienen la longitud de código
correcta y por eso pasan cualquier filtro que solo mire la longitud. **No son
unidades territoriales.** Incluirlos ocupa toda la cola baja de los tres niveles
NUTS —desde 22.62 MIO_EUR— e infla el rango dinámico europeo de ~3 a 4.5 órdenes de
magnitud, que es justo la cantidad decisiva del método de Clauset. Se excluyen con
`es_region()`. Quien reutilice `nama_10r_3gdp` para una distribución de tamaños
tiene que descartarlos.

Nota de calidad: la tabla 5938 del IBGE **no publica PIB per cápita**, así que Brasil
no entra en la secundaria. Los datos de Estados Unidos quedan fuera del diseño: la
API del BLS respondió `REQUEST_NOT_PROCESSED` por umbral diario agotado desde esta
dirección, y las de BEA y Census exigen clave.

---

### Valor puntual del Dominio B 2026-10-02 (sin descargas)

No entra ninguna fuente externa nueva. Entradas, ya versionadas y con su SHA-256 más
arriba en este archivo: `data/maddison_mpd2020.csv` (las 446 series del Dominio B se
reconstruyen desde ahí, verificado caso por caso contra la `b` publicada) y
`reconstruction_real/data/by_domain/dominio_B_real.csv`.

| Archivo de salida | SHA-256 |
|---|---|
| `reconstruction_real/data/dominio_B_calibracion.csv` | `c2372a096bdba792b8fbb4728ed709575c1b91435103910b9cffa6d2700659d8` |
| `reconstruction_real/data/dominio_B_valor_puntual.csv` | `0cfb54028790bfb3b38e8a9d13e51031f7c5d7e6ca220e20257ee3dcc0d75c16` |
| `reconstruction_real/data/dominio_B_recalibracion.csv` (recalibración a N = 200,000, 2026-10-03) | `4f1034a34b0bd7bf82f37ae61c20b81bd8db3d1d14359dca1bf0076d4fb045b1` |

Nota de calidad: `dominio_B_valor_puntual.csv` trae el p de los doce métodos por caso.
**Ninguna de ellas es admisible.** La recalibración a `N = 200,000` del 2026-10-03
(`audits/RESULTADOS_RECALIBRACION_DOMINIO_B_2026-10-03.md`, salida
`dominio_B_recalibracion.csv`) midió la banda de admisión [2.5%, 7.5%] contra las doce
tasas y **ninguna entra**: la mejor, `p_ar1_inf`, mide **7.96%** (IC95 Wilson
[7.76%, 8.17%]) y se queda a 0.46 puntos del techo; el resto va de 12.9% a 58.0%.
**Ninguna de las doce columnas debe usarse para contar significativos.** Sobre los
mismos datos la cuenta va de 33 a 134 de 156 según el método, y el 33 de `p_ar1_inf` es
una **cota conservadora, no un valor puntual**.

---

### Deriva del exponente contra fricción 2026-10-02 (sin descargas)

Entradas, todas versionadas: `data/maddison_mpd2020.csv` (Dominio B),
`data/binance_cierres_diarios.csv.gz` (cripto, cocientes moneda/BTC) y
`data/npm_descargas_mensuales_deriva.csv.gz` (npm, agregado mensual de los 450 de la
cohorte, SHA-256 arriba). El crudo `data/raw_npm/descargas.jsonl.gz` sigue sin
versionar por tamaño, pero su SHA-256 está registrado en la sección de npm y el script
recae en él si el derivado no está.

| Archivo de salida | SHA-256 |
|---|---|
| `reconstruction_real/data/deriva_forma_por_caso.csv` | `56eeb28b82605fb4eb106145b1b342cafb12ba9ce433f133eef4ed6d41c9b299` |
| `reconstruction_real/data/deriva_forma_resumen.csv` | `37297b6c331c2759b14d6f836ac36a7b6a917a5039845cf1868c3923afcedddc` |

El hash del resumen cambió el 2026-10-03 al añadirse los puntos secundarios S2 y S4, que faltaban. Cambia **solo por las filas nuevas** `S2_*` y `S4_*`: `deriva_forma_por_caso.csv` conserva su SHA-256 al bit y ninguna cifra de los puntos anteriores se movió. El hash previo del resumen era `848be0936875973c9d5c3e38668ef285aece34117310a79a1fb400742b0070ce`.

**Nota de calidad, de primer orden para cualquiera que use datos de Binance en análisis
temporales.** El momento en que un exchange lista una moneda es un **sesgo de selección
fuerte**: en los 571 cocientes moneda/BTC analizados, **el 70.1% tiene su máximo dentro
del primer 10% de la serie** y el 84.9% dentro del primer 25% (mediana de la posición
del máximo: 0.019). Una serie que empieza en su máximo tiene que bajar, y eso produce
por sí solo un exponente local cada vez más negativo. Partiendo los casos por posición
del pico, la deriva descendente pasa de **57.5%** (pico temprano) a **0.0%** (pico
tardío). Ver `audits/RESULTADOS_DERIVA_FORMA_2026-10-02.md` §3.

Nota de calidad: el brazo de npm mide un **nivel** de descargas, no un cociente, así
que arrastra el crecimiento del ecosistema completo — la mediana del exponente en las
ventanas tardías es 1.858, que es npm creciendo, no el paquete. Por eso entró cripto al
diseño como brazo de cociente.

---

### RC1, régimen superlineal 2026-10-02 (sin descargas)

Entradas, todas versionadas: `data/owid_covid_casos_totales.csv.gz` (E3, receta
verificada: acumulados, inicio en el primer día con ≥ 100 casos, 60 días),
`data/maddison_mpd2020.csv` (B) y
`reconstruction_real/data/snt_corpus_aco_timeseries_v29.csv` (ACO, control).

| Archivo de salida | SHA-256 |
|---|---|
| `reconstruction_real/data/rc1_por_caso.csv` | `066f5fdd9f55018ab553590754ef293a0a110281ebc1e718d543143525e86e82` |
| `reconstruction_real/data/rc1_calibracion.csv` | `29fa46af16fa0777dca5064255df22dc6d16108dddb0f893b65e427b096b97a5` |
| `reconstruction_real/data/rc1_resumen.csv` | `a853282f43b7bed971219ca3174bbf6bcb50d8f8fa287dc6279c469c8ad488f7` |

**Nota de calidad, de primer orden para cualquiera que use `comparar_modelos` o
cualquier AIC sobre residuos crudos.** El criterio supone independencia, y en estos
dominios los residuos están muy autocorrelados. Calibrado contra series simuladas desde
una **ley de potencia conocida**, el AIC elige otro modelo en el **80.3%** de las
réplicas en E3, el **96.8%** en B y el **48.9%** en el ACO, dentro de la banda `b ≥ 1`
— y el error **crece con `b`**. Las columnas `ganador` y `delta_aic_potencia` de
`rc1_por_caso.csv` **no deben usarse para contar formas** sin leer antes
`rc1_calibracion.csv`.

**Segunda nota, independiente del AIC.** Una exponencial verdadera ajustada como ley de
potencia produce `b ≥ 1` en el **99.9%** de las réplicas en la banda alta de E3 y en el
**100%** del ACO, contra **0.0%** donde la `b` real es menor que 0.5. Cualquier umbral
sobre la `b` estimada bajo ley de potencia hereda eso. Ver
`audits/RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md` §2.

---

## 2. Archivos derivados que SÍ están en el repo (checksums)

Checksums SHA-256 al 2026-07-25, **re-verificados el 2026-09-26: los 6 coinciden**.
Sirven para detectar si un archivo cambió sin que se documente. Recalcular con `sha256sum <archivo>`.

| Archivo | SHA-256 |
|---|---|
| `reconstruction_real/data/by_domain/dominio_B_real.csv` | `e0c7738a31b45b913c73d851ac1b81a9d2ea56aef7e9168ae991eda2687ce583` |
| `reconstruction_real/data/by_domain/dominio_E3_real.csv` | `11a99cc42a62a73dbe4b282acd66d48c8e86839e6a0fc8cdddc187f9c70c0e82` |
| `reconstruction_real/data/snt_corpus_REAL_v5.csv` | `6a4a89ed780552facfc0cd77a1abf7ce49b02d73211205d04f51f5eb5d38e9b1` |
| `reconstruction_real/data/snt_corpus_aco_timeseries_v29.csv` | `68c11e95e3b609008820111e303141b2d9391923960a5f7855c074e44512d31c` |
| `data/snt_asi_scores.csv` | `57e38ee9f779efc117b747247cb72ce6f869ae433f885aa116a653b766531fb6` |
| `data/owid-maddison.csv` | `6e905c41324d50f2e4e468bad9d204a1efd44f6f34368c98425e8e0b33d6a4ec` |
| `data/mpd2020.xlsx` | `d20853c2e0930d6855fb6d8138da11f24fcf313d234e2db9773ea1f551adfec3` |
| `data/maddison_mpd2020.csv` | `1c0b15ae4b78d54134d3c781e361784ee06c8519762ca6ceb45ef65fc31d54c0` |
| `data/COW_Trade_4.0.zip` | `c44c4b5ce62e68865368482c428306df4624d3a39edec29adc1aa2c0928f7cc7` |
| `data/comercio_bilateral.csv` | `9625f8403800f6834c5ebd03a5ab7c094d9be603c4954561de6be66ce7eea6cb` |

> Para regenerar la tabla:
> ```sh
> for f in reconstruction_real/data/by_domain/dominio_B_real.csv \
>          reconstruction_real/data/by_domain/dominio_E3_real.csv \
>          reconstruction_real/data/snt_corpus_REAL_v5.csv \
>          reconstruction_real/data/snt_corpus_aco_timeseries_v29.csv \
>          data/snt_asi_scores.csv \
         data/owid-maddison.csv \
         data/mpd2020.xlsx \
         data/maddison_mpd2020.csv \
         data/COW_Trade_4.0.zip \
         data/comercio_bilateral.csv; do
>   sha256sum "$f"
> done
> ```

---

## 3. Pendientes de provenance (heredados de la auditoría v32)

- [x] Descargar `data/owid-maddison.csv`, fijar edición + fecha + SHA-256 arriba.
      **Hecho 2026-07-25** (OWID grapher, cobertura hasta 2022).
- [x] Identificar y fijar la edición exacta de Maddison que produjo el dominio
      B. **Hecho 2026-09-27:** Maddison Project Database 2020
      (`data/mpd2020.xlsx`); reproducción byte a byte de los 446 casos.
- [x] Recuperar las series crudas de E3 (OWID COVID snapshot) para desbloquear
      su corrección AR(1). **Hecho 2026-09-27** (pre-registro, punto 3):
      `owid-covid-data.csv` (SHA arriba); E3 reproducido 233/234; E1 no
      reproducible.
- [x] Conseguir la matriz de comercio bilateral direccional para el bloque 2 de
      la prueba discriminante. **Hecho 2026-09-27:** Correlates of War Trade
      v4.0 (`data/COW_Trade_4.0.zip` → `data/comercio_bilateral.csv`).
- [ ] Opcional: `download_sources.sh` que baje ambas fuentes y verifique los
      checksums, para que el corpus sea regenerable de punta a punta.

---

## Dominio G — provenance (paquetes cósmicos / desempaquetado)

Generado por `reconstruction_real/code/build_dominio_G.py` el 2026-09-11. Bloque para pegar en `data/FUENTES.md`.

> Regla del repo (AGENTS.md): **real data first**. Este dominio se entrega con metadatos y citas primarias. **Estado (v2.5.2):** G03 Bennu tiene la primera serie real poblada (n = 3, Mojarro et al. 2025, PNAS) y está AJUSTADO; los otros cuatro casos siguen con `t`/`R` vacías porque ningún caso publicado ofrece hoy ≥3 puntos de señal orgánica vs tiempo de exposición para un mismo cuerpo. NaN, no cero.

### Casos

| id | tipo_muestra | trigger | cita verificada en sesión | estado |
|---|---|---|---|---|
| `G01_Murchison_1969` | caida | 1969-09-28 | sí | PENDIENTE — sin serie temporal real |
| `G02_Ryugu_Hayabusa2_2020` | retorno_de_muestra | 2020-12-06 | sí | PENDIENTE — sin serie temporal real |
| `G03_Bennu_OSIRISREx_2023` | retorno_de_muestra | 2023-09-24 | sí | AJUSTADO |
| `G04_Orgueil_1864` | caida | 1864-05-14 | sí | PENDIENTE — sin serie temporal real |
| `G05_TagishLake_2000` | caida | 2000-01-18 | NO | PENDIENTE — sin serie temporal real |

### Fuentes primarias por caso

#### `G01_Murchison_1969`

Kvenvolden K. et al. (1970). Evidence for extraterrestrial amino-acids and hydrocarbons in the Murchison meteorite. Nature 228, 923-926. DOI 10.1038/228923a0; Kvenvolden K., Lawless J., Ponnamperuma C. (1971). Nonprotein amino acids in the Murchison meteorite. PNAS 68(2), 486-490; Cronin J.R. & Moore C.B. (1971). Science 172, 1327; Engel M.H. & Macko S.A. (1997). Isotopic evidence for extraterrestrial non-racemic amino acids in the Murchison meteorite. Nature 389, 265; Koga T. et al. (2024). Abundant extraterrestrial purine nucleobases in the Murchison meteorite. Geochim. Cosmochim. Acta 365, 253-265; Glavin D.P. et al. (2018). In: Primitive Meteorites and Asteroids (Abreu N., ed.), Elsevier, 205-271

**Campo candidato para `t`/`R`:** Fracción de aminoácidos no proteinogénicos (AIB, isovalina) sobre el inventario total, o grado de racemización de aminoácidos quirales, medida en alícuotas curadas con historial documentado, en función del tiempo de residencia terrestre desde 1969. Requiere revisión de literatura de re-análisis 1970→2024 con condiciones de almacenamiento registradas.

#### `G02_Ryugu_Hayabusa2_2020`

Oba Y. et al. (2023). Uracil in the carbonaceous asteroid (162173) Ryugu. Nat. Commun. 14, 1292. DOI 10.1038/s41467-023-36904-3; Naraoka H. et al. (2023). Soluble organic molecules in samples of the carbonaceous asteroid (162173) Ryugu. Science 379, abn9033; Parker E. et al. (2023). Extraterrestrial amino acids and amines identified in asteroid Ryugu samples returned by the Hayabusa2 mission. Geochim. Cosmochim. Acta 347, 42-57; Yada T. et al. (2022). Preliminary analysis of the Hayabusa2 samples returned from C-type asteroid Ryugu. Nat. Astron. 6, 214-220; Yokoyama T. et al. (2023). Science 379, eabn7850; Oba Y. et al. (2026). A complete set of canonical nucleobases in the carbonaceous asteroid (162173) Ryugu. Nat. Astron. DOI 10.1038/s41550-026-02791-z

**Campo candidato para `t`/`R`:** Concentración de uracilo (y B3) por muestra en función de la dosis de exposición espacial estimada (superficie vs subsuperficie). Hoy solo existen 2 puntos (A0106, C0107): n=2 < 3, no ajustable. Se necesitan alícuotas adicionales o un proxy de dosis por grano.

#### `G03_Bennu_OSIRISREx_2023`

Mojarro A., Aponte J.C., Dworkin J.P., Elsila J.E., Glavin D.P., Connolly H.C., Lauretta D.S. (2025). Prebiotic organic compounds in samples of asteroid Bennu indicate heterogeneous aqueous alteration. PNAS 122(49), e2512461122. DOI 10.1073/pnas.2512461122 (Table 2; datos en Astromat DOI 10.60707/1k00-p463, 10.60707/sxy1-sq73, 10.60707/kacg-nb16); Glavin D.P., Dworkin J.P. et al. (2025). Abundant ammonia and nitrogen-rich soluble organic matter in samples from asteroid (101955) Bennu. Nat. Astron. DOI 10.1038/s41550-024-02472-9; McCoy T.J. et al. (2025). An evaporite sequence from ancient brine recorded in Bennu samples. Nature 637, 1072-1077; Lauretta D.S. et al. (2024). Asteroid (101955) Bennu in the laboratory. Meteorit. Planet. Sci. 59, 2453-2486; PNAS (2025). Prebiotic organic compounds in samples of asteroid Bennu indicate heterogeneous aqueous alteration. DOI 10.1073/pnas.2512461122

**Campo candidato para `t`/`R`:** POBLADO (n=3, diversidad). Siguiente paso: abundancias absolutas (nmol/g) por piedra con el mismo proxy, o más piedras por litología, para subir n y pasar de conteo a concentración.

#### `G04_Orgueil_1864`

Aponte J. et al. (2023). Organic-soluble compounds in asteroid Ryugu samples A0106 and C0107 and the Orgueil (CI1) meteorite. Earth Planets Space 75, 28; Oba Y. et al. (2026). Nat. Astron. DOI 10.1038/s41550-026-02791-z; Burton A.S. et al. (2014). The effects of parent-body hydrothermal heating on amino acid abundances in CI-like chondrites. Polar Sci. 8, 255-263; Stoks P.G. & Schwartz A.W. (1979). Uracil in carbonaceous meteorites. Nature 282, 709-710

**Campo candidato para `t`/`R`:** Mismo índice que G01 (fracción no proteinogénica o racemización) en alícuotas de distintas colecciones con historial de curación conocido, contra tiempo de residencia. Caso de mayor t disponible (>160 años) pero con provenance de alícuota más incierta.

#### `G05_TagishLake_2000`

Brown P.G. et al. (2000). The fall, recovery, orbit, and composition of the Tagish Lake meteorite: a new type of carbonaceous chondrite. Science 290, 320-325 [POR VERIFICAR — cita de memoria, no confirmada en sesión]

**Campo candidato para `t`/`R`:** Mismo índice que G01/G04. Su valor es de control: caída natural con contaminación cercana a la de un retorno de muestra.

### Relación transversal registrada (no temporal)

`GX01_purina_pirimidina_vs_amoniaco` — Ratio purina/pirimidina correlaciona negativamente con amoníaco entre Ryugu, Bennu y Orgueil (mineralogía y composición elemental similares). Murchison enriquecido en purinas, Ryugu ≈ equilibrado, Bennu y Orgueil enriquecidos en pirimidinas.

Eje: química del entorno receptor (amoníaco) — no tiempo. Valores numéricos: {'purina_sobre_pirimidina': {'Bennu': 0.55, 'Orgueil': 1.1, 'Murchison': 2.8, 'Ryugu': None}, 'amoniaco_nmol_g': {'Bennu': 13600, 'Murchison': '≈1130 (1/12)', 'Ryugu': '≈181 (1/75)', 'Orgueil': None}, 'fuente_cifras': 'Glavin 2025, Nat. Astron. (texto principal y Extended Data Table 6)'}. Puntos limpios con ambas variables: Bennu y Murchison (n=2). Orgueil tiene ratio pero amoníaco discrepante entre extractos; Ryugu tiene amoníaco pero ratio solo cualitativo (≈1, Oba 2026). n limpio = 2 < 3: sigue sin ajustar. Eje 'resonancia del receptor' (Axioma 2), no el eje temporal de ACO-A.

Fuente: Oba Y. et al. (2026). A complete set of canonical nucleobases in the carbonaceous asteroid (162173) Ryugu. Nat. Astron. DOI 10.1038/s41550-026-02791-z
