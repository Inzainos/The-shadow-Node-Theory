# Shadow Node Theory (SNT) · v2.7.1

[![Release](https://img.shields.io/badge/release-v2.7.1-6f42c1)](CHANGELOG.md)
[![Marco teórico](https://img.shields.io/badge/marco-v34-0e8a8a)](papers/marco_teorico.md)
[![Python CI](https://github.com/Inzainos/The-shadow-Node-Theory/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/Inzainos/The-shadow-Node-Theory/actions/workflows/python-package-conda.yml)

**Shadow Node Theory** estudia trayectorias relativas entre un hub y un nodo.
Su objeto empírico es la razón `R(t) = métrica_del_hub / métrica_del_nodo`,
resumida —cuando los datos lo permiten— por `R(t) = a·t^b`. El marco también
incluye ACO-A, una descripción separada de la absorción posterior a ciertos
colapsos, y una capa de incertidumbre que distingue observaciones, proyecciones
y reconstrucciones.

SNT es un marco de análisis, no una ley universal ni un predictor validado.
Los resultados dependen del dominio, la ventana, las variables y la calidad de
reconstrucción. La autocorrelación y la selección de casos limitan la
inferencia; 721 registros no equivalen a 721 réplicas independientes.

**Estado de la evidencia.** Cada cifra citada en este README se verifica contra
los CSV versionados con [`reconstruction_real/claims.yaml`](reconstruction_real/claims.yaml)
(`python reconstruction_real/code/verificar_claims.py`; también corre en CI).

| Afirmación | Estado |
|---|---|
| Las pendientes de B y E3 se reconstruyen desde fuentes versionadas | Reproducible (E3: 233/234) |
| Inferencia sobre `b` en B | Indecidible: 290/446 series no estimables |
| `b` de B como estimación de equilibrio de largo plazo | No confirmado: 93,3% componentes I(1), 12,3% cointegrado detectado — apenas 2–4 pp sobre el tamaño del test (EG sobre-rechaza 8–10% bajo la nula en series cortas, M=3000 versionado). Corregida por tamaño por-n y potencia, la tasa verdadera es ~4–15% (≈9% a la mediana de B con 45,9% de potencia y 9,0% de tamaño a n=69; ponderada por n: 4,2–7,4%). `b` queda como descriptor de deriva ([cointegración](reconstruction_real/audits/COINTEGRACION_HUB_NODO_2026-10-26.md)) |
| `b ≥ 1` como régimen superlineal | No respaldada (error de selección AIC de 22,6% a 96,8%) |
| Relación general fricción `φ` → `b` | No respaldada en tres vías: agrupamiento de dominios (p_perm = 0,053; MixedLM p = 0,57), dominios nuevos pre-registrados (p = 0,39), y por caso dentro de npm (ρ = +0,09, dirección contraria) |
| La forma de la trayectoria identifica el dominio | Sí, en exactitud balanceada; no frente a la línea base cruda |
| La forma de la trayectoria identifica el tono `φ` | No distinguible de asignar tonos al azar entre dominios |
| ACO-A: convergencia descriptiva de `\|log₁₀ m\|` hacia 0 | Más cerrada que la dinámica AR(1) propia (p = 0,013) pero ligada a ventanas acabadas en evento (las de B no convergen) — no interpretada como firma del colapso ([nulos AR(1)](reconstruction_real/audits/NULOS_AR1_ACO_2026-10-26.md)) |
| Prueba prospectiva ACO-A (cripto congelada 2026-10-26) | Sellada por git (sellado externo pendiente); ventana re-anclada 2026-10-26 → 2027-10-26; criterios recalibrados (P1a/P1b falsable, P3 por TOST). Backcast 2025-26 (corte 2026-09-30): P1a/P1b/P2 respaldadas (mediana Δ = −0,944), P3 inconcluso por diseño a n=36 (ρ = −0,191, IC95 [−0,489, +0,146] cruza −0,3) ([backcast](reconstruction_real/audits/BACKCAST_PROSPECTIVA_2026-10-26.md)) |

## La idea y sus límites

`R(t)` compara la escala del hub con la del nodo. El exponente `b` describe la
trayectoria dentro de la ventana observada:

| `b` | Lectura descriptiva |
|---|---|
| `b < 0` | La razón disminuye: el nodo gana terreno relativo. |
| `b ≈ 0` | La razón permanece aproximadamente estable. |
| `0 < b < 1` | La razón crece de forma sublineal en el ajuste de potencia. |
| `b ≥ 1` | Banda descriptiva no clasificada; no prueba un régimen superlineal. |

Un ajuste de potencia no demuestra causalidad ni identifica por sí solo el
mecanismo del sistema. En la calibración RC1, el error de selección AIC excedió
el umbral preespecificado del 20% en todos los dominios calibrados. Por ello,
`b ≥ 1` no se interpreta como prueba de aceleración o como régimen físico
confirmado. Véanse [RC1 — superlineal](reconstruction_real/audits/RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md)
y [RC1 — dominios restantes](reconstruction_real/audits/RESULTADOS_RC1_DOMINIOS_RESTANTES_2026-10-17.md).

## Evolución

La historia completa — de la hipótesis de escala a la teoría que declara
sus límites, con cada auditoría que retiró una interpretación — vive en
[`docs/HISTORIA.md`](docs/HISTORIA.md).

## Desarrollo empírico por dominio

El corpus consolidado contiene **721 casos**. La tela integrada contiene
**740 trayectorias**: **699 series reales versionadas** (B 446, E3 234, ACO 18,
G 1) y **41 sombras** para casos sin serie temporal cruda versionada. Son dos
conjuntos con propósitos distintos; las sombras no amplían el corpus de casos
reales. La tabla siguiente resume **cómo se desarrolló y qué sobrevivió en cada
dominio**, con enlaces a las auditorías y preregistros correspondientes.

### A — Ciudades

El corpus contiene cuatro comparaciones urbanas. La reconstrucción con World
Urbanization Prospects no recupera la receta publicada de forma consistente:
solo 1/4 coincide, y esa coincidencia usa una ventana de 69 observaciones
frente a las siete del caso publicado, por lo que se considera espuria. A no es
un dominio reproducible y no se calibra como tal en RC1.

Un análisis distinto, pre-registrado, contrastó ocho traslados o desarrollos
urbanos con controles de dinámica basal: los ocho mostraron una pendiente
mayor (`d > 0`; Wilcoxon unilateral `p = 0.0039`). El resultado es favorable a
esa pregunta estrecha, no una reparación de los cuatro casos del corpus. Con
`n = 8`, ese `p` es el **mínimo alcanzable** de la prueba unilateral
(1/2⁸ = 0.0039): 8 de 8 es el resultado más extremo posible, así que la
cifra habla de ausencia total de contraejemplos, no de la magnitud del
efecto. La
fuente solo incluye aglomeraciones de al menos 300.000 habitantes, lo que deja
un sesgo de selección/supervivencia y excluye ciudades pequeñas.

**Informes:** [RC1 en dominios restantes](reconstruction_real/audits/RESULTADOS_RC1_DOMINIOS_RESTANTES_2026-10-17.md) ·
[prueba pre-registrada de disparadores urbanos](reconstruction_real/audits/RESULTADOS_PREREGISTRO_2026-09-27.md) ·
[bloqueo de la fuente WUP para ciudades menores](reconstruction_real/audits/RESULTADOS_DESBLOQUEOS_2026-10-18.md).

### B — Países y trayectoria hub–nodo

Las 446 pendientes se reconstruyen desde Maddison Project Database 2020. La
reproducción confirma la receta y los valores descriptivos; no resuelve la
inferencia: 445/446 series presentan autocorrelación severa, el `n_eff` mediano
es 2,2 y 290/446 no son estimables con el criterio aplicado. En la recalibración
pre-registrada de 200.000 simulaciones, la tasa de falsos positivos de la cota
AR(1) fue 7,962% (IC95 `[7,76%, 8,17%]`), fuera de la banda de admisión
`[2,5%, 7,5%]`; ninguno de los 12 métodos la superó. El valor puntual para B
queda **indecidible**.

También se probó si la asignación original del hub por PIB medio creaba parte
de la asociación. Con hubs derivados de comercio, la correlación entre
pendiente y brecha inicial fue `ρ = −0,153` (`p = 0,125`); frente a controles
con brecha comparable no hubo diferencia (mediana `d = −0,014`, Wilcoxon
`p = 0,78`). Esta reconstrucción alternativa no sustituye el corpus B: muestra
que cambiar la definición del hub cambia la pregunta y no recupera evidencia
de acoplamiento comercial.

La tela v2 sí integra las 446 series reales de B. Su pendiente temprana y la
dirección al cierre se asocian débilmente (`ρ = +0,224`, `p = 1,7×10⁻⁶`), pero
la autocorrelación, la selección de pares y la dependencia por dominio impiden
leerlo como predicción validada.

**Informes:** [recalibración B](reconstruction_real/audits/RESULTADOS_RECALIBRACION_DOMINIO_B_2026-10-03.md) ·
[hub comercial](reconstruction_real/audits/RECONSTRUCCION_DOMINIO_B_HUB_COMERCIO.md) ·
[dirección temprana en tela v2](reconstruction_real/audits/TELA_EXOGENA_2026-10-21.md).

### C — Regiones y curva rango–tamaño

La reconstrucción temporal de los 23 casos del corpus reproduce las pendientes
con la receta pre-especificada. Sin embargo, la autocorrelación es incluso más
fuerte que en B (`ρ` AR(1) mediana 0,970); 12/23 casos tienen `n_eff < 3`.
La significancia nominal de las filas no debe interpretarse como evidencia
independiente.

En la prueba RC1, el error AIC para la banda `b ≥ 1` fue 22,6%, sobre el límite
pre-registrado de 20%, de modo que la banda queda **no interpretable por AIC**
para C. En una pregunta distinta —la curva rango–tamaño de las 32 entidades
mexicanas— la lognormal mejoró el AIC en 65,04 puntos; la prueba de Clauset
tuvo 96,4% de falsos “sobrevive” sobre datos lognormales simulados. La
interpretación de apego preferencial no está respaldada por ese ajuste. Una
réplica internacional encontró lognormal en cinco de seis niveles y potencia
en municipios de Brasil; la prueba de Clauset no alcanzó poder suficiente en
ninguno.

**Informes:** [RC1 y autocorrelación de C](reconstruction_real/audits/RESULTADOS_RC1_DOMINIOS_RESTANTES_2026-10-17.md) ·
[comparación lognormal en México](reconstruction_real/audits/RESULTADOS_LOGNORMAL_2026-10-02.md) ·
[réplica internacional de rango–tamaño](reconstruction_real/audits/RESULTADOS_RANGO_TAMANO_2026-10-02.md).

### D — Digital / HackerEarth

Los tres casos del corpus dependen de datos propietarios: D sigue
**no reproducible** desde el repositorio. La auditoría de un reporte posterior
encontró que sus AUC de 0,9994 y 1,0 eran circulares: la etiqueta de retención
se derivaba de la misma puntuación CSI_V3 que aparecía entre las variables de
entrada. Esas cifras no se citan como capacidad predictiva.

Con una etiqueta temporal externa —inactividad en los 30 días posteriores a
un corte—, la evaluación prospectiva sobre los datos disponibles obtuvo AUC
`0,836 ± 0,038` (`n = 2.058`) y `0,893 ± 0,041` para usuarios con antigüedad
de al menos siete días (`n = 137`). Es una medición de una cohorte y un corte,
con censura a la derecha; informa sobre esa evaluación de HackerEarth, no
reproduce ni valida los tres casos D del corpus SNT.

**Informe:** [auditoría y evaluación temporal de HackerEarth](reconstruction_real/audits/REVISION_REPORTE_HACKEREARTH_2026-10-18.md).

### E1 — Expansión territorial

Los cuatro casos no se reproducen desde las series crudas con las
construcciones evaluadas. El resultado vigente es **no reproducible**, no una
confirmación de `R(t)`. La tela usa sombras para representar los casos donde no
hay series verificables; esas curvas son proyecciones del ajuste, no
observaciones territoriales. E1 queda fuera de las conclusiones de
reproducibilidad.

**Informes:** [RC1 en dominios restantes](reconstruction_real/audits/RESULTADOS_RC1_DOMINIOS_RESTANTES_2026-10-17.md) ·
[prueba pre-registrada de series COVID y E1](reconstruction_real/audits/RESULTADOS_PREREGISTRO_2026-09-27.md).

### E2 — Depredador–presa

De los dos casos, E2_01 reproduce `b`, `R²` y Durbin–Watson al decimal;
E2_02 no reproduce con ninguna de las cuatro recetas evaluadas. RC1 se aplica
solo a E2_01: la tasa de error AIC en la banda contrafactual `b ≥ 1` fue 94%.
Al ser un solo caso reproducible, no es una calibración representativa del
dominio ni autoriza generalización biológica.

**Informe:** [RC1 en dominios restantes](reconstruction_real/audits/RESULTADOS_RC1_DOMINIOS_RESTANTES_2026-10-17.md).

### E3 — Expansión epidemiológica

Los 234 casos corresponden a trayectorias de COVID seleccionadas por una
receta de crecimiento. Con OWID versionado, 233/234 pendientes se reproducen
dentro de ±0,01; la única excepción es E3_060, que permanece faltante donde
no se reproduce. De 234 series, 198 son estimables tras el ajuste por
autocorrelación; la cota AR(1) conservadora deja 176 casos significativos
(196 bajo la variante superior). A diferencia de B, la señal descriptiva de
crecimiento sobrevive la cota conservadora en esta cohorte seleccionada.

La calibración RC1 reporta error AIC de 80,3% en la banda `b ≥ 1`, así que
esa banda no clasifica un régimen en E3. En la tela integrada, 233/234 curvas
son series reales; la pendiente temprana y el destino se asocian fuertemente
(`ρ = +0,823`), pero la selección por fase de crecimiento hace que esta
asociación sea descriptiva, no una prueba prospectiva de predicción ni una
regla para otras epidemias.

**Informes:** [reconstrucción y corrección por autocorrelación](reconstruction_real/audits/RESULTADOS_PREREGISTRO_2026-09-27.md) ·
[RC1 por dominio](reconstruction_real/audits/RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md) ·
[series reales de la tela](reconstruction_real/audits/TELA_EXOGENA_2026-10-21.md) ·
[r² crudo actualizado](reconstruction_real/audits/RESULTADOS_DESBLOQUEOS_2026-10-18.md).

### F — Sistemas físicos

Los cuatro registros F1–F3 describen relaciones de masa u órbita, no
trayectorias temporales `R(t)` comparables con las de B o E3. Por esa
diferencia de objeto no se calibran en RC1 como series temporales. En la tela,
sus trayectorias son sombras del modelo y no series físicas observadas; no se
extraen conclusiones de dominio a partir de su forma.

**Referencia:** [RC1 en dominios restantes](reconstruction_real/audits/RESULTADOS_RC1_DOMINIOS_RESTANTES_2026-10-17.md).

### G — Geoquímica de Bennu

G cuenta con un caso y tres puntos versionados para un proxy geoquímico. Es una
trayectoria exploratoria, insuficiente para estimar variabilidad del dominio,
validar una ley de escala o generalizar a otros cuerpos menores. La tela la
incluye como una serie real de un solo caso, no como réplica de una población.

**Referencia:** [capa exógena de la tela v2](reconstruction_real/audits/TELA_EXOGENA_2026-10-21.md).

### ACO-A — Colapso y absorción

ACO-A es un eje complementario a la satelización, no otro nombre para `b ≥ 1`.
Sus 18 casos tienen trayectorias crudas versionadas. En esta muestra,
`|log₁₀ m|` mediano cae de 0,292 a 0,071 desde el inicio hasta el final:
descripción compatible con convergencia hacia `m≈1`, no prueba de atractor
universal. La diferencia entre disparadores abruptos y graduales tampoco fue
concluyente (`p = 0,101`; permutación intra-dominio `p = 0,938`).

La aplicación externa pre-registrada a 450 paquetes npm encontró asociación
pequeña entre `b` y `Δ` (`ρ = +0,114`, IC95 `[+0,016, +0,209]`), compatible con
el criterio de equivalencia de esa prueba. El hazard observado decrece con
edad (`ρ = −0,716`, `p = 0,013`, dos colas), con advertencias por censura y
mezcla edad-periodo-cohorte. No se generaliza desde npm a todos los sistemas.

**Informes:** [ACO-A en npm](reconstruction_real/audits/RESULTADOS_NPM_2026-10-02.md) ·
[cohorte original y hazard](reconstruction_real/audits/RESULTADOS_PREREGISTRO_2026-09-27.md) ·
[tela integrada](reconstruction_real/audits/TELA_V2_INTEGRADA_2026-10-21.md).

### Comparación visual de las trayectorias

La placa y las medianas por dominio resumen la **tela integrada**: las series
reales se incluyen donde existen y las sombras permanecen visibles como
reconstrucciones del modelo. La placa no identifica por sí sola mecanismo,
dominio ni fricción. La figura de tonos es una descripción espectral; `φ`
sigue siendo categórica/postulada, no una variable física medida.

<p align="center">
  <img src="figures/fig_tela_cimatica_chladni.png" alt="Densidad y trayectorias medianas por dominio en la tela integrada" width="100%">
  <br>
  <img src="figures/fig_tela_cimatica_tonos.png" alt="Espectros medianos por dominio en la tela integrada" width="85%">
</p>

En la prueba leave-one-out por centroide, la tela integrada obtiene 50,7% de
clasificación por dominio y 66,2% por tono nominal. Es una evaluación
exploratoria sin calibración de clasificador. El origen único en `m=1` de la
primera versión se retiró: era consecuencia de las sombras, que se construían
con ese punto inicial. En v2 las 699 series reales nacen en escalas distintas;
las 41 sombras mantienen su etiqueta de modelo.

**Informes de las figuras y resultados:** [integración v2](reconstruction_real/audits/TELA_V2_INTEGRADA_2026-10-21.md) ·
[capa cimática](reconstruction_real/audits/TELA_CIMATICA_2026-10-21.md) ·
[proyección y datos](reconstruction_real/audits/TELA_DE_INCERTIDUMBRE_2026-10-21.md).

## Zenodo y SSRN

- **Archivo versionado de v2.7.1 (canónico):**
  [DOI 10.5281/zenodo.23661819](https://doi.org/10.5281/zenodo.23661819) —
  snapshot del release 2.7.1 (2026-10-26), contiene los preregistros de la
  ronda 2026-10-26. El primer archivo del mismo día
  ([10.5281/zenodo.23653089](https://doi.org/10.5281/zenodo.23653089)) quedó
  antes de los preregistros y no los incluye. La línea del corpus de 721
  casos sigue en
  [10.5281/zenodo.19446521](https://doi.org/10.5281/zenodo.19446521).
- **Preprint en SSRN:** [abstract 6418778](https://ssrn.com/abstract=6418778).
  El manuscrito vigente es la **r33** (2026-10-26, base v2.7.1, subida por el
  autor): añade la tela de incertidumbre integrada y los dos controles
  nuevos (nulos AR(1), cointegración) en el Abstract y el §16; el resto es
  r32 sin cambios. No se presenta como arbitrado.
- **Archivos del manuscrito:** r33 [inglés](papers/snt_ssrn_v33_EN.md) ·
  [español](papers/snt_ssrn_v33.md); r32 (histórico):
  [inglés (PDF)](papers/snt_ssrn_v32_EN.pdf) ·
  [español (PDF)](papers/snt_ssrn_v32.pdf).
- **Cita del software:** [`CITATION.cff`](CITATION.cff), con el DOI canónico
  y la historia de identificadores.

### Lo que no se presenta como hallazgo establecido

- Los valores p por caso no son pruebas independientes: existe dependencia
  temporal y agrupación por dominio.
- `b ≥ 1` no identifica por sí solo superlinealidad ni aceleración.
- La fricción `φ` está postulada por dominio, no medida como campo continuo.
- El eje `u` no tiene definición operativa y no se rellena con un proxy.
- Las sombras generadas a partir de ajustes no son series observadas ni nuevas
  réplicas; una forma en la tela tampoco demuestra un mecanismo causal.
- La asociación descriptiva entre variables, la clasificación exploratoria y
  la convergencia de ACO no establecen capacidad predictiva ni universalidad.

## Fuentes, datos y auditorías

- [Estado empírico y reproducibilidad por dominio](reconstruction_real/README.md)
- [Corpus consolidado v6](reconstruction_real/data/snt_corpus_REAL_v6.csv)
- [Tela integrada v2](reconstruction_real/audits/TELA_V2_INTEGRADA_2026-10-21.md)
- [Implementación de la capa de incertidumbre](reconstruction_real/audits/TELA_DE_INCERTIDUMBRE_2026-10-21.md)
- [Resultados de la capa cimática](reconstruction_real/audits/TELA_CIMATICA_2026-10-21.md)
- [Marco teórico v34](papers/marco_teorico.md)
- [Fuentes, ediciones y checksums](data/FUENTES.md)
- [Auditorías y preregistros](reconstruction_real/audits/README.md) ·
  [casos de uso externos](CASOS_DE_USO.md)

Las fuentes propietarias o no redistribuibles se identifican en sus informes.
Los valores ausentes permanecen ausentes; no se imputan como cero.

## Reproducir

Usa el entorno local descrito en [AGENTS.md](AGENTS.md). Desde la raíz:

```bash
flake8 .
python -m compileall -q code reconstruction_real dashboard delta
python reconstruction_real/code/build_aco_v29.py
pytest reconstruction_real/tests          # incluye claims y auditoría integral
python reconstruction_real/code/verificar_claims.py
```

La prueba de línea base y permutación de la tela se regenera con
`python reconstruction_real/code/tela_clasificacion_baseline.py` (≈2,5 min,
semilla fija).

La prueba del corpus B y las auditorías completas pueden requerir más tiempo.
Consulta las instrucciones de cada informe antes de descargar datos o
regenerar resultados.

## Estructura

- `reconstruction_real/` — corpus, metodología, código, auditorías y pruebas.
- `papers/` — marco teórico v34 y documentos de investigación.
- `code/` — utilidades y scripts activos compartidos.
- `data/` — datos versionados y procedencia.
- `figures/` — figuras de resultados vigentes.
- `delta/` — motor independiente de señales de cripto y bolsa.
- `dashboard/` — dashboard Streamlit.
- `Legacy/` y `archive/` — material histórico supersedido; no citar como
  evidencia vigente.
- El **Genomic Topologic Analyzer** tiene repositorio propio desde 2026-10-20:
  `/home/deamon/genomic_agent` (proyecto local independiente, remote de GitHub pendiente de crear; historial completo preservado en la rama `genomic-agent-split` de este repo).

## Marco y cita

El marco activo es **v34**; la información de cita está en
[`CITATION.cff`](CITATION.cff). Contribuye mediante una rama y un pull request;
no hagas commits directamente a `main`. Cada resultado nuevo debe incluir
fuente, receta reproducible y límites de inferencia; registra los cambios en
[`CHANGELOG.md`](CHANGELOG.md).
