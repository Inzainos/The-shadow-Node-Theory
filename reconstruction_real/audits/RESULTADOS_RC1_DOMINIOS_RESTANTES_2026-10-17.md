# Resultados — RC1 en los dominios restantes (A, E2, C)

**Pre-registro:** [`../preregistro/PREREGISTRO_RC1_DOMINIOS_RESTANTES_2026-10-17.md`](../preregistro/PREREGISTRO_RC1_DOMINIOS_RESTANTES_2026-10-17.md)
(commit `4e9cb9e`, subido antes de descargar un solo byte de datos nuevos).
**Script:** `code/rc1_dominios_restantes.py` (con log).
**Semilla:** `20261017` · `N_CAL = 200` · umbral de admisión 20% (el de RC1).

Cierra, hasta donde hoy es cerrable, el pendiente del README *"Test b ≥ 1 on the
other domains' raw series"*: RC1 (2026-10-02) probó E3, B y ACO; aquí se intenta
con **todos** los dominios restantes, con receta o con veredicto de por qué no.

## Tabla de decisiones

| Punto | Dominio | Resultado | Decisión |
|---|---|---|---|
| Fase 0 | **A** (4) | 1/4 reproduce la `b` publicada desde WUP — y la única coincidencia (A_001, receta 1950-2018) es espuria: n=69 contra n=7 publicado | **NO REPRODUCIBLE** → no se calibra |
| Fase 0 | **E2** (2) | E2_01 reproduce **exacto** (b, R² y DW: 0.5371 vs 0.537 publicado); E2_02 no reproduce con ninguna de las 4 recetas (todas dan −0.1072 vs −0.2592) | **Parcial**: se calibra solo E2_01, rotulado como caso único |
| Fase 0 | **C** (23) | **23/23 reproducen** (receta: R = pob_hub/pob_node, anual 1900-2025, US Census vía FRED) | **REPRODUCIBLE** → se calibra |
| P0 | C | Error de selección AIC en la banda contrafactual `b ≥ 1`: **22.6%** (1.0–1.5: 33.3%; ≥1.5: 11.9%) | **NO INTERPRETABLE** por AIC a `b ≥ 1` (umbral 20%) — pero muy lejos de E3/B |
| P5 | C | Exponencial verdadera → `b` aparente ≥ 1: **0.7%** (control ≥ 0.5: 8.8%) | **LA TAUTOLOGÍA NO SE REPLICA**: en la estructura de C, una `b ≥ 1` observada no sería un mero renombre del desajuste |
| P0 | E2_01 | Error en banda contrafactual `b ≥ 1`: **94.0%** | **NO INTERPRETABLE** — replica el patrón de RC1 en series cortas |
| P5 | E2_01 | Exponencial verdadera → `b ≥ 1`: 11.0% | Sin la tautología masiva de E3/B/ACO, pero n=1 caso |
| P1-P4 | C | Ganadores en casos reales: potencia 8 / exponencial 7 / lineal 8; P2 Spearman(b, ΔAIC) = −0.045, p una cola 0.42 | Se reportan, no se interpretan (P0 no admite) |
| P3/P4 | ambos | 0 casos superlineales observados en A/C/E2 | **No evaluables por diseño** — declarado, no omitido |

---

## 1. Fase 0 — qué es testeable hoy y qué no

| Dominio | Casos | Veredicto | Motivo |
|---|---:|---|---|
| A | 4 | **No reproducible** | El WUP (aglomeraciones ONU) no reproduce las `b` del corpus: A_003 Paris→Lyon da −0.02 contra +0.2384 publicado en todas las recetas; A_002 carece de Yokohama (está dentro de la M.M.A. de Tokyo en WUP); A_001 sólo "coincide" con una receta de n=69 que contradice el n=7 publicado. El corpus usó el *Demographic Yearbook* (ciudad, no aglomeración), que no tiene fuente pública legible por máquina al alcance de este diseño |
| E2 | 2 | Parcial (1/2) | E2_01 (tabla lince-liebre 1900-1920, dsem/CRAN ← Gotelli 2008 ← MacLulich 1937) reproduce b, R² **y Durbin-Watson** al decimal. E2_02 ("Lynx vs equilibrio 1821-1850") no reproduce con ninguna receta de normalización — todas comparten pendiente (−0.1072) y la publicada es −0.2592; queda declarado **no reproducible**, como E1 |
| C | 23 | **Reproducible 23/23** | Receta única pre-especificada (anual 1900-2025) reproduce todas las `b` dentro de ±0.01 — la mayoría al 4º decimal. C_001 (México) excluido por diseño (rango-tamaño, no R(t)) |
| D | 3 | No testeable | HackerEarth propietario |
| E1 | 4 | No testeable | Declarado no reproducible el 2026-09-27 |
| F1-F3 | 4 | No testeable | Los ajustes publicados son relaciones masa/órbita, no trayectorias R(t) en el tiempo |

**El pendiente del README queda cerrado en lo cerrable:** con esto los siete
dominios satelización del corpus tienen veredicto — E3, B, ACO (RC1), C, E2_01
(aquí), y A, E2_02, D, E1, F1-F3 con causa documentada de por qué no.

## 2. C — el hallazgo doble

### 2.1 La compuerta se replica (por poco): el AIC sigue sin ser admisible a `b ≥ 1`

Con la `(n, ρ, σ)` real de cada uno de los 23 casos y bandas contrafactuales
`b = 1.25` y `b = 1.75`:

| Banda contrafactual | Error de selección AIC |
|---|---:|
| 1.0 ≤ b < 1.5 (b=1.25) | 33.3% |
| b ≥ 1.5 (b=1.75) | **11.9%** |
| **b ≥ 1 agregada** | **22.6% → NO INTERPRETABLE** (umbral 20%) |

La compuerta de RC1 se vuelve a activar, pero **por 2.6 puntos**, no por 60-77
como en E3 (80.3%) y B (96.8%). Las 126 observaciones de C dan al AIC más
margen del que nunca tuvo en este repo — la banda alta (≥1.5) queda incluso por
debajo del umbral. Por la regla pre-registrada, la banda agregada decide: **C no
es interpretable por AIC a `b ≥ 1`**.

### 2.2 La tautología NO se replica — y eso es lo informativo

RC1 retiró la etiqueta "Roche Radius" porque una exponencial verdadera ajustada
como ley de potencia cae en `b ≥ 1` en el **99.9%** de las réplicas (banda alta
de E3), 70.6% en B y 98-100% en ACO. En C:

| | E3 | B | ACO | **C** | E2_01 |
|---|---:|---:|---:|---:|---:|
| Exponencial verdadera → `b` aparente ≥ 1 | 69.7–99.9% | 70.6% | 98–100% | **0.7%** | 11.0% |
| (control: `b` aparente ≥ 0.5) | — | — | — | 8.8% | 47.0% |

**En la estructura de series de C, una `b ≥ 1` observada no sería un renombre
del desajuste exponencial.** La tautología que RC1 midió es una propiedad de las
cavidades E3/B/ACO (series de 60-69 puntos, ρ≈0.94), no del estimador a secas.
Por la regla por dominio esto no reabre nada — C no tiene casos superlineales
que reclasificar, y el retiro de la etiqueta queda intacto — pero **la razón del
retiro queda acotada**: la etiqueta se retiró donde se midió; si algún día
aparece un caso `b ≥ 1` en un dominio de series largas como C, no podrá
descartarse como desajuste con el argumento de RC1, sino que exigirá la
calibración de ese dominio.

### 2.3 Lo que las series de C revelan de paso: autocorrelación peor que B

Las series recién recuperadas traen su propio diagnóstico — el mismo que la
auditoría v32 aplicó a B, calculado aquí de forma descriptiva:

| | Dominio B (auditoría v32) | **Dominio C (recuperado hoy)** |
|---|---:|---:|
| n nominal mediano | 69 | **126** |
| DW mediana | 0.112 | **0.032** |
| ρ AR(1) mediana | 0.944 | **0.970** [0.814, 0.995] |
| No estimables (`n_eff < 3`) | 290/446 (65%) | **12/23 (52%)** |

Las series de población de C son **más autocorrelacionadas que las de Maddison**:
sus 23 casos figuran en el corpus como 23/23 significativos (p truncados a 0.0),
y bajo el marco v32 **12 de 23 ni siquiera son estimables**. Esto no cambia
ninguna `b` — son descripciones válidas — pero la significancia por caso del
dominio C hereda exactamente la salvedad del dominio B, y el E2_01 recuperado
resulta marginalmente estimable (`n_eff = 3.10`). Queda registrado para el
pendiente de reporte del corpus (p exactos + `r2_log`/`r2_raw`).

## 3. E2 — un solo caso, y se comporta como RC1 predijo para series cortas

E2_01 (n=21, ρ=0.743): el AIC se equivoca en el **94.0%** de las réplicas
contrafactuales de la banda `b ≥ 1` — la misma escala de E3/B. Con un solo caso
reproducible no hay dominio que reportar; se reporta el caso, rotulado como tal.

## 4. Qué significa para la SNT

| Afirmación | Estado anterior | Estado ahora |
|---|---|---|
| RC1 no es decidible por AIC a `b ≥ 1` | E3 80.3% / B 96.8% / ACO 48.9% | **Se replica en C (22.6%, al filo) y en E2_01 (94%)**. El veredicto "no decidible" sigue vigente en todos los dominios calibrados |
| Una exponencial verdadera produce `b ≥ 1` casi siempre (base del retiro de la etiqueta) | Medida en E3/B/ACO: 70-100% | **NO es universal**: en C es 0.7%. La tautología es propiedad de la estructura de cada dominio. El retiro de la etiqueta queda intacto (no hay casos superlineales en C/E2 que reclasificar), pero su fundamento queda acotado por dominio |
| Significancia por caso del dominio C | 23/23 significativos (nominal) | **Sus series crudas tienen ρ AR(1) mediana 0.970 y 12/23 casos no estimables** bajo el marco v32. Misma salvedad que B, registrada |
| Pendiente "test b ≥ 1 en los demás dominios" | Abierto desde la auditoría v32 | **Cerrado en lo cerrable**: veredicto para los 7 dominios de satelización (3 en RC1 + C + E2_01 aquí + A/E2_02/D/E1/F con causa documentada) |

**Lo que no cambia:** ninguna `b` publicada, el corpus, la ortogonalidad b ⊥ Δ,
el gradiente de Tlaxcala, la capa ACO-A, y el retiro de la etiqueta "Roche
Radius" del código.

## Desviaciones respecto al pre-registro

1. **C tiene 23 pares, no 22.** El pre-registro (§1.3) escribió "22 pares
   (C_002..C_024)" y umbral "≥ 21 de 22"; C_002..C_024 son 23. La regla general
   (≥ 90% de los casos) era la vinculante y se cumplió 23/23, así que el error
   de conteo no afecta ninguna decisión. Se declara para el registro.
2. **Ruta de descarga del censo:** el pre-registro ordenaba "(a) tablas de
   census.gov; (b) FRED". Se usó la (b) sin intentar la (a): FRED es el espejo
   del Census PEP y la receta identificó 23/23 al primer intento, con lo que
   explorar (a) no podía mejorar la identificación. SHAs de las 32 descargas
   crudas, una por estado, en el log.
3. **E2 tratado por caso, no por dominio.** §1.2 definía listas de recetas
   *distintas* para E2_01 y E2_02; la regla del 90% se aplicó por caso. E2_02 no
   reproduce → el caso queda no reproducible y la "calibración de E2" es en
   realidad un solo caso rotulado como tal en todo el informe. No se presenta
   como representativa del dominio.
3b. **La coincidencia de A_001 es espuria y se ignora.** El único caso de A que
   cruzó la tolerancia (receta 1950-2018, |Δb| = 0.0056) usa n=69 contra n=7
   publicado — la salvedad que el pre-registro declaró ("la receta puede
   reproducir la b por azar aunque sea la equivocada") materializada. El dominio
   exigía 4/4 y quedó 1/4.
4. **Extracción de `hare_lynx.rda`:** la tabla de dsem se versiona como
   `data/hare_lynx_1900_1920.csv` (derivada del `.rda` con `pyreadr`, una sola
   vez y documentada aquí); el script lee el CSV versionado y no depende de
   `pyreadr` ni de red. SHA del `.rda` crudo en `data/FUENTES.md`.

## Reproducción

```bash
python reconstruction_real/code/rc1_dominios_restantes.py
```

Determinista (semilla `20261017`). La primera corrida descarga 32 series de FRED
(~1 min); después usa `data/us_census_poblacion_estatal_1900_2025.csv`.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-17*
