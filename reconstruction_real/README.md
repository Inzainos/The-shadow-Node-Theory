# SNT Corpus -- Reconstruccion con Datos Reales (v5 / release v2.6.0; corpus sin cambios desde v2.5.2)

## Estado: 721 casos REALES en 11 dominios

| Dominio | Casos | Sig. | b mean | R2 mean | Fuente |
|---------|-------|------|--------|---------|--------|
| A -- Ciudades | 4 | 0% | +0.08 | 0.18 | UN Demographic Yearbook |
| B -- Paises | 446 | 84%† | +0.09 | 0.35 | Maddison Project Database 2020 |
| C -- Regiones | 24 | 100% | +0.09 | 0.53 | US Census historico (23) + INEGI 2022 (1) |
| D -- Digital | 3 | 100% | -1.36 | 0.87 | HackerEarth 2026 |
| E1 -- Invasion (expansion territorial) | 4 | 100% | +2.89 | 0.81 | OWID COVID-19 (spatial spread, 2020) |
| E2 -- Depred-presa | 2 | 50% | +0.15 | 0.12 | MacLulich 1937 / Elton & Nicholson 1942 |
| E3 -- Parasito-huesped | 234 | 100% | +0.91 | 0.85 | OWID COVID-19 (JHU CSSE) |
| F1 -- Planetario | 2 | 100% | -1.81 | 0.40 | Open Exoplanet Catalogue + NASA fact sheet |
| F2 -- Estelar | 1 | 100% | +1.27 | 0.48 | Open Exoplanet Catalogue |
| F3 -- Multiplanet | 1 | 100% | +1.26 | 0.90 | Open Exoplanet Catalogue |
| ACO -- Colapso Acoplado | 18 | 94% | +0.60 | 0.87 | ver build_aco_v29.py |

**Total: 721 casos satelizacion + 18 casos ACO | 89% significativos (nominal†) | CERO R2 corruptos**

† Significancia **nominal** por caso (OLS log-log, sin corregir autocorrelacion).
Tras la correccion AR(1) de la auditoria v32, el dominio B tiene **156/446
casos estimables** (`n_eff >= 3`) y **290/446 no estimables**; entre los
estimables, los significativos caen a **33-112 (21.2%-71.8%)** segun la
variante analitica. Ver `audits/`.

## Hallazgo central (datos reales)

A nivel de casos individuales en dominios sociales/biologicos (n=714):
**Spearman rho = -0.68, p = 2.5x10^-97**

**Tal como se publico (v30):** la friccion institucional predice la
satelizacion: dominios con alta friccion (paises, regiones: b~0.09) vs sin
friccion (epidemias: b~+0.95). **Estado en v2.6.0:** la direccion se mantiene
en el corpus, pero no es significativa a nivel de dominio y la prueba
pre-registrada con dominios nuevos no la respalda (ver abajo).

**Mann-Whitney p = 2.4x10^-74**

**Auditoria v32 — la direccion aguanta, el p no.** La cifra por fila replica
exacto, pero trata 714 casos agrupados en 6 dominios como independientes.
Recalculado desde el corpus versionado (2026-09-26, `code/snt_utils_v32.py`):

| Analisis | rho | p | n |
|---|---:|---:|---:|
| Por fila (publicado) | -0.678 | 2.5x10^-97 | 714 |
| Por cluster (medias por dominio) | -0.556 | 0.25 | 6 dominios |
| Bootstrap por cluster | -0.434 | IC95 [-0.722, -0.006] | 6 dominios |
| Sin E3 | -0.116 | 0.011 | 480 |
| Sin E3 ni B | -0.426 | 0.012 | 34 |

El polo "sin friccion" del contraste (E1 + E3 = 238 casos) es integramente
dato COVID-19 de OWID/JHU. Ademas, la prueba discriminante del dominio B
(`audits/DISCRIMINANTE_DOMINIO_B.md`) quedo **inconclusa**: `b` en B no queda
respaldado ni como acoplamiento SNT ni como beta-convergencia, y las
reconstrucciones con hub de comercio (fijo y variable en el tiempo) muestran
convergencia, no acoplamiento.

**Pre-registro 2026-09-27** (`preregistro/`, `audits/RESULTADOS_PREREGISTRO_2026-09-27.md`):
el n = 714 publicado **excluye el dominio D** (exponentes de distribucion; con
D, sin E3 ni B, rho = -0.145, p = 0.39, n = 37); con 7 dominios nuevos sin
COVID (mpox, StatCounter, ciudades ONU, hub de comercio) rho(friccion, b media
del dominio) = -0.131, permutacion exacta p = 0.39 -> **no respaldada**. El
polo sin friccion si es real: E3 reconstruido desde series crudas sigue
significativo tras corregir la autocorrelacion, y mpox tambien da b alto
(+0.43).

## Integridad
- Todos los R2 in [0,1] -- verificado
- Todos los p in [0,1] -- verificado, pero redondeados a 6 decimales: **557/721
  leen exactamente `0.0`** (impide FDR exacto y meta-analisis)
- Dos definiciones de R2 conviven: B usa r de Pearson al cuadrado (escala log),
  el resto 1 - SSres/SStot (escala cruda); `r2_mean` las promedia juntas
- `trigger` esta fijo en `'gradual'` para los 446 casos de B (en ambos constructores:
  `expand_B_massive.py` y `expand_dominio_B.py`)
- Sin datos sinteticos
- Checksums SHA-256 de los archivos del corpus anclados en `../data/FUENTES.md`
  (re-verificados 2026-09-26)

## Reproducibilidad
- **Dominio B: reproduccion exacta** (verificada 2026-09-27). El dominio se
  construyo con el **Maddison Project Database 2020** (cobertura 1-2018), ahora
  en el repo como `../data/mpd2020.xlsx`. `code/build_maddison_mpd2020_csv.py`
  lo convierte a `../data/maddison_mpd2020.csv` y `code/expand_B_massive.py`
  regenera los 446 casos **byte a byte** (SHA-256 identico al de
  `data/by_domain/dominio_B_real.csv`).
- Con la edicion OWID posterior (`../data/owid-maddison.csv`, 2026-07-25) B solo
  se reproduce aproximado: 441 vs 446 casos, corr(b) = 0.979, 12/408 b
  identicos (Maddison revisa el PIB historico entre ediciones y el hub se asigna
  por PIB medio). `code/expand_dominio_B.py` es una expansion anterior (254
  casos) y **no** reproduce el dominio.
- **Dominio E3 (COVID-19): reproduccion verificada** (2026-09-27): 233/234
  casos desde la serie cruda de OWID (subconjunto versionado
  `../data/owid_covid_casos_totales.csv.gz`; receta: casos acumulados, 60 dias
  desde el primer dia con >= 100 casos). Correccion AR(1): 198/234 estimables y
  176-196 de esos 198 siguen significativos (cota conservadora: 176;
  `code/covid_E3_series_crudas.py`). Newey-West con rezago estandar da 233/234,
  pero subcorrige con residuos tan persistentes.
- **Dominio E1 (4 casos): no reproducible** desde las series crudas con ninguna
  construccion natural.
- **Auditoria completa:** `python reconstruction_real/code/snt_auditoria_integral_v32.py`
  (salida en `data/auditoria_integral_v32_resultados.csv`) y
  `pytest reconstruction_real/tests`.

## Cambio de v4 a v5
- Dominio B expandido: 258 -> 446 pares de paises (Maddison completo)
- Dominio E3 expandido: 15 -> 234 casos (COVID-19 JHU, 234 paises)
- Spearman actualizado: rho=-0.39 (v4, n=307) -> rho=-0.68 (v5, n=714)

## Notas de honestidad metodologica
- **Dominio A**: solo datos UN modernos (2000-2024), pocos puntos -> no
  significativo. Requiere Bairoch 1988 para casos historicos largos.
- **E1/E3**: modelados como expansion territorial/epidemica (COVID-19, OWID/JHU),
  matematicamente equivalentes a invasion. Datos GBIF de especies bloqueados.
  E1 **no** son invasiones biologicas de especies.
- **Regimen superlineal b >= 1**: por AIC sobre las 18 series crudas ACO, la ley
  de potencia gana 13/18 y la exponencial 4/18; los ganadores exponenciales
  tienen b medio +1.54. El 14.1% del corpus etiquetado como superlineal puede
  ser mala especificacion de modelo. Desde 2026-09-27 la serie cruda de E3 esta
  en el repo (94 de los 102 casos con b >= 1 son E1 + E3), asi que la prueba ya
  es posible para E3 (pendiente).
- **Dominios fisicos (F)**: siguen ley de potencia pero su "friccion" es
  fisica (Eddington, resonancia orbital), no institucional.

## Fuentes (publicas y verificables, salvo HackerEarth)
- UN Demographic Yearbook (A)
- Maddison Project Database 2020 (Bolt & van Zanden 2020) (B)
- US Census Bureau (estados) + INEGI 2022 (Mexico) (C)
- HackerEarth 2026 (D; propietario, solo resultados agregados)
- OWID COVID-19 dataset, JHU CSSE (E1, E3)
- MacLulich 1937 / Elton & Nicholson 1942 (lince-liebre) (E2)
- Open Exoplanet Catalogue + NASA planetary fact sheet (F1-F3)

## Archivos
- `data/snt_corpus_REAL_v5.csv` -- corpus consolidado (721 casos)
- `data/MASTER_cifras_v5.json` -- todas las cifras del paper (8/8 replican)
- `data/MASTER_resumen_v5.csv` -- resumen por dominio (40/40 celdas replican)
- `data/by_domain/` -- CSV individual por dominio con metadatos y fuente declarada
- `data/snt_corpus_aco_v29.csv` + `data/snt_corpus_aco_timeseries_v29.csv` -- ACO (18 casos + series crudas)
- `data/snt_corpus_dominio_G*.csv` + `data/snt_corpus_dominio_G_fuentes.md` -- Dominio G (v2.5.2)
- `data/auditoria_integral_v32_resultados.csv` -- salida de la auditoria v32
- `data/dominio_B_corregido_ar1_v32.csv` -- dominio B con correccion AR(1) por caso
- `code/build_maddison_mpd2020_csv.py` -- convierte `../data/mpd2020.xlsx` en `../data/maddison_mpd2020.csv` (verifica SHA-256)
- `code/expand_B_massive.py` -- construye el dominio B (446 casos; reproduccion byte a byte desde `../data/maddison_mpd2020.csv`)
- `code/expand_dominio_B.py` -- expansion regional previa (254 casos; no reproduce los 446)
- `code/build_dominio_B.py` -- construye dominio B
- `code/build_aco_v29.py` -- ACO, 18 casos (smoke test del CI)
- `code/build_dominio_G.py` -- Dominio G, 5 casos; G03 Bennu n=3
- `code/snt_auditoria_integral_v32.py` -- runner de la auditoria v32
- `code/prueba_discriminante_dominio_B.py` -- prueba discriminante del dominio B
- `code/recalculo_trigger_abrupto_gradual.py` -- recalculo de abrupto vs gradual (cifra 5.9x); salida en `data/trigger_abrupto_gradual_recalculo.csv`
- `code/build_comercio_bilateral_cow.py` -- COW Trade v4.0 -> `../data/comercio_bilateral.csv` (bloque 2 de la prueba discriminante)
- `code/comercio_maddison.py` -- funciones compartidas COW/Maddison (reglas de entidad y mapeo de socios)
- `code/reconstruccion_B_hub_comercio.py` -- dominio B con hub emergente de comercio (fijo)
- `code/prueba_hub_temporal.py` -- pre-registro punto 1: hub variable en el tiempo
- `code/prueba_friccion_dominios_nuevos.py` -- pre-registro punto 2: friccion con dominios nuevos (E4, D2, A2, B-comercio)
- `code/covid_E3_series_crudas.py` -- pre-registro punto 3: E3 desde series crudas + correccion de autocorrelacion
- `code/prueba_disparadores_ciudades.py` -- pre-registro punto 4: disparadores codificados a ciegas (ONU WUP 2018)
- `code/descargar_binance_klines.py` + `code/aco_cohortes_ampliadas.py` -- pre-registro punto 5: ortogonalidad y hazard (Binance, FDIC)
- `code/generate_readme_figures.py` -- figuras del README (v2.6.0, clara y oscura)
- `preregistro/PREREGISTRO_2026-09-27.md` -- pre-registro (subido antes de correr las pruebas)
- `audits/` -- informes: `AUDITORIA_INTEGRAL_v32.md`, `DISCRIMINANTE_DOMINIO_B.md`, `RECONSTRUCCION_DOMINIO_B_HUB_COMERCIO.md`, `RESULTADOS_PREREGISTRO_2026-09-27.md`
- `tests/test_correccion_ar1.py` -- prueba de regresion (156/290/33/112)
