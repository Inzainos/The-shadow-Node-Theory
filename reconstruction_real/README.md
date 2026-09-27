# SNT Corpus -- Reconstruccion con Datos Reales (v5 / v2.5.2)

## Estado: 721 casos REALES en 11 dominios

| Dominio | Casos | Sig. | b mean | R2 mean | Fuente |
|---------|-------|------|--------|---------|--------|
| A -- Ciudades | 4 | 0% | +0.08 | 0.18 | UN Demographic Yearbook |
| B -- Paises | 446 | 84%† | +0.09 | 0.35 | Maddison Project 2023 (via OWID) |
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

La friccion institucional predice la satelizacion: dominios con alta
friccion (paises, regiones: b~0.09) vs sin friccion (invasion, epidemias:
b~+0.95). El gradiente es nitido y altamente significativo.

**Mann-Whitney p = 2.4x10^-74**

**Auditoria v32 — la direccion aguanta, el p no.** La cifra por fila replica
exacto, pero trata 714 casos agrupados en 6 dominios como independientes.
Recalculado desde el corpus versionado (2026-09-26, `code/snt_utils_v32.py`):

| Analisis | rho | p | n |
|---|---:|---:|---:|
| Por fila (publicado) | -0.678 | 2.5x10^-97 | 714 |
| Por cluster (medias por dominio) | -0.556 | 0.25 | 6 dominios |
| Bootstrap por cluster | ~ -0.44 | IC95 [-0.722, -0.006] | 6 dominios |
| Sin E3 | -0.116 | 0.011 | 480 |
| Sin E3 ni B | -0.426 | 0.012 | 34 |

El polo "sin friccion" del contraste (E1 + E3 = 238 casos) es integramente
dato COVID-19 de OWID/JHU. Ademas, la prueba discriminante del dominio B
(`audits/DISCRIMINANTE_DOMINIO_B.md`) quedo **inconclusa**: `b` en B no queda
respaldado ni como acoplamiento SNT ni como beta-convergencia.

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
- **Dominio B:** se regenera **de forma aproximada, no exacta**, desde
  `../data/owid-maddison.csv` (en el repo, descargado 2026-07-25). Medido el
  2026-09-27: `code/expand_B_massive.py` da 441 casos vs 446 publicados (408
  pares comunes, corr(b) = 0.979, signo coincide 396/408, solo 12/408 b
  identicos; agregados casi iguales: b medio +0.088 vs +0.092, 83.7% vs 83.9%
  significativos nominales). La edicion de Maddison usada originalmente no se
  fijo y Maddison revisa el PIB historico entre ediciones; ademas, el hub se
  asigna por PIB medio y la revision puede invertir pares.
  `code/expand_dominio_B.py` produce solo 254 casos: **no** reproduce el dominio.
- **Dominios E1/E3 (COVID-19):** solo estan los resumenes ajustados; las series
  crudas **no** estan en el repo. Esto bloquea la correccion AR(1) de E3.
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
  ser mala especificacion de modelo (sin probar en otros dominios: faltan sus
  series crudas).
- **Dominios fisicos (F)**: siguen ley de potencia pero su "friccion" es
  fisica (Eddington, resonancia orbital), no institucional.

## Fuentes (publicas y verificables, salvo HackerEarth)
- UN Demographic Yearbook (A)
- Maddison Project Database 2023 (Bolt & van Zanden), via OWID (B)
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
- `code/expand_B_massive.py` -- regenera el dominio B de forma aproximada (441 vs 446; lee `../data/owid-maddison.csv`)
- `code/expand_dominio_B.py` -- expansion regional previa (254 casos; no reproduce los 446)
- `code/build_dominio_B.py` -- construye dominio B
- `code/build_aco_v29.py` -- ACO, 18 casos (smoke test del CI)
- `code/build_dominio_G.py` -- Dominio G, 5 casos; G03 Bennu n=3
- `code/snt_auditoria_integral_v32.py` -- runner de la auditoria v32
- `code/prueba_discriminante_dominio_B.py` -- prueba discriminante del dominio B
- `code/recalculo_trigger_abrupto_gradual.py` -- recalculo de abrupto vs gradual (cifra 5.9x); salida en `data/trigger_abrupto_gradual_recalculo.csv`
- `audits/` -- informes de auditoria (`AUDITORIA_INTEGRAL_v32.md`, `DISCRIMINANTE_DOMINIO_B.md`)
- `tests/test_correccion_ar1.py` -- prueba de regresion (156/290/33/112)
