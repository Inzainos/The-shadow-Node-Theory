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

## Evolución: de una hipótesis de escala a una teoría que declara sus límites

La evolución de SNT no es una acumulación lineal de confirmaciones. Cada etapa
añadió una pregunta o una capa de análisis; las auditorías también retiraron
interpretaciones que no sobrevivieron a la reconstrucción, a los controles de
dependencia o a las pruebas de falsabilidad. Esta síntesis conserva los
resultados vigentes y distingue el marco conceptual de lo que está medido.

### 1. La pregunta inicial: relación entre hub y nodo

Las primeras versiones formularon una comparación relativa: cómo cambia la
escala de un nodo respecto de un hub que lo domina o condiciona. La razón
`R(t)` permite comparar trayectorias dentro de una ventana y `b` resume una
parte de su forma. La hipótesis de escala fue útil para hacer comparables
casos de distintas magnitudes, pero la expansión del marco también trajo
ejemplos, mecanismos y generalizaciones que no tenían todos el mismo tipo de
respaldo.

Por eso, el estado actual no trata el linaje narrativo completo como evidencia.
El corpus antiguo de 502 casos fue retirado: la auditoría halló valores de `b`
sintéticos y métricas de ajuste imposibles. El corpus real consolidado de 721
casos lo sustituyó. La cifra 721 describe el inventario, no el número de
réplicas independientes ni una validación global de la teoría. El linaje
detallado del marco —incluidas las propuestas históricas que ya no se usan
como hallazgos— está en [CHANGELOG del marco](papers/CHANGELOG_marco.md).

### 2. El corpus reproducible y la corrección de la inferencia

La reconstrucción del corpus hizo que la pregunta dejara de ser solo si una
pendiente podía calcularse y pasara a ser si podía interpretarse. La auditoría
integral mostró con especial claridad el problema en el Dominio B: la
reconstrucción con Maddison Project Database 2020 es reproducible, pero 445 de
446 series tienen autocorrelación severa; en 290, el tamaño efectivo no permite
estimar la pendiente bajo el criterio aplicado. Una corrección posterior con
200.000 simulaciones encontró que ninguno de los 12 métodos evaluados cumplía
la banda de falsos positivos predefinida. Así, el valor puntual de inferencia
para B quedó **indecidible**, en lugar de convertir significancia nominal en
evidencia.

El mismo cambio de estándar afectó a la relación entre fricción y `b`. La
correlación por fila, aunque numéricamente fuerte en el corpus, no equivale a
714 observaciones independientes: filas del mismo dominio comparten estructura
y recetas. Al resumir por dominios, el resultado no fue concluyente
(`ρ = −0.556`, `p = 0.253`); la prueba pre-registrada con dominios nuevos
tampoco respaldó una relación general (`ρ = −0.131`, permutación exacta
`p = 0.39`). El polo de baja fricción observado en E3 puede describirse con
sus series disponibles, pero no rescata una ley general fricción→`b`.

La reproducción también es específica por dominio. B reproduce 446/446
pendientes desde su fuente versionada; E3 reproduce 233/234 dentro de ±0,01.
En otros dominios, la disponibilidad de series crudas y la compatibilidad de
las recetas varían. Por ello, un ajuste reproducido valida esa reconstrucción
concreta; no valida automáticamente el mecanismo, el valor p ni una
generalización entre dominios.

### 3. La banda `b ≥ 1` deja de ser un diagnóstico

En versiones anteriores, `b ≥ 1` se interpretaba como régimen superlineal. La
calibración RC1 puso esa etiqueta a prueba comparando modelos sobre series
observadas. El error de selección AIC superó el máximo pre-registrado de 20%
en todos los dominios calibrados: E3 80,3%, B 96,8%, ACO 48,9%, C 22,6% y
E2_01 94,0%. Además, una exponencial ajustada como potencia puede producir
`b ≥ 1`, pero con frecuencia distinta según el dominio.

La conclusión que sobrevivió es metodológica: el exponente no clasifica por sí
solo el mecanismo. En esta versión `b ≥ 1` es una banda descriptiva no
clasificada, no prueba de aceleración, transición inminente ni régimen físico
universal. Una clasificación más fuerte requeriría series suficientes,
comparación de modelos calibrada para el dominio y validación independiente.

### 4. ACO-A separa el colapso de la satelización

La capa **Arquitectura de Colapso Orbital Acoplada (ACO-A)** amplió la pregunta
sin redefinir `b`: para un caso con extinción funcional y un sucesor
identificable, describe cómo se absorbe masa o actividad después del evento,
mediante `A(τ) = c·τ^Δ`. `τ` comienza en el evento de referencia y `Δ` resume
esa trayectoria; no son la misma razón, ventana o variable que `R(t)` y `b`.
La separación evita tratar toda pendiente extrema como colapso y permite
contrastar empíricamente la relación entre los dos ejes.

En las 18 series crudas ACO versionadas, la distancia mediana
`|log₁₀ m|` respecto de `m=1` baja de 0,292 a 0,071. Es una descripción de esa
cohorte, no evidencia suficiente de un atractor universal. La comparación de
disparadores abruptos y graduales tampoco fue concluyente (`p = 0.101`; la
permutación intra-dominio dio `p = 0.938`). Una aplicación externa a 450
paquetes npm halló una asociación pequeña entre `b` y `Δ`
(`ρ = +0.114`, IC95 `[+0.016, +0.209]`), compatible con el criterio de
equivalencia preespecificado en esa prueba; no establece ortogonalidad
universal. El hazard observado decreciente requiere cautela por censura y
mezcla edad-periodo-cohorte.

ACO-A conserva preguntas falsables —por ejemplo, si un sucesor captura
actividad medible y cómo evoluciona esa absorción—, no una predicción validada
de cuándo ocurrirá el colapso. Los resultados de otras cohortes y pruebas
externas están enlazados en [auditorías](reconstruction_real/audits/README.md)
y [casos de uso](CASOS_DE_USO.md).

### 5. De una teoría conceptual a un marco con estatus y proyecciones

El marco teórico evolucionó junto al corpus, pero mantiene numeración propia.
La v30 restauró el texto completo del marco anterior y añadió ACO-A; la v31
desarrolló propuestas de trayectorias y mecanismos a escala micro y macro; la
v32 reunió el marco conceptual de doce axiomas. Esas formulaciones no se
convierten en evidencia solo por estar formalizadas. La v33 hizo explícita esa
diferencia al etiquetar el estatus de los axiomas y añadir la **tela de
incertidumbre** como capa conceptual fundamental, no como variable empírica de
SNT.

La v34 desarrolló el paso siguiente: separar el estado propuesto de lo que el
instrumento observa. Su cubo estructural `𝒞(u, m, τ)` define `m` como la
magnitud/razón con proxy declarado y `τ` como fase temporal normalizada.
`u`, apertura de posibilidades, no tiene definición operativa aceptada en
ningún dominio y permanece `NULL`; no se inventa un sustituto para completar
la geometría. Por tanto, la implementación actual trabaja con `(m, τ)`, no con
un cubo tridimensional medido.

La observación se expresa como una sombra o proyección `Π_θ(𝒞)`, con
`θ = (B, V, ρ, W, λ)`: base, variables y proxies, resolución, ventana y
umbral de corte. Como distintas estructuras pueden producir la misma sombra,
la reconstrucción puede ser un conjunto de posibilidades y no un estado único.
El criterio de invarianza exige contrastar marcos de medición independientes;
no se declara satisfecho cuando la evidencia disponible no permite ese
contraste. Esto convierte la incertidumbre en una regla de reporte y de
admisión de afirmaciones, no en una cifra adicional que el corpus no mide.

En el mismo marco, `φ` se formula como campo escalar de fricción, pero su
estatus sigue siendo **postulado, no medido**: los valores actuales son
categóricos por dominio o provienen de cohortes pequeñas, no una medición
continua a lo largo de las trayectorias. La cimática del colapso conserva
estatus conceptual y una cláusula anti-metáfora; las figuras no son evidencia
de vibración física ni identifican por sí solas un modo.

### 6. La tela integrada: una corrección que cambia la lectura visual

La implementación de la tela pasó de representar todos los casos con curvas
del modelo a usar series crudas donde existen y sombras explícitas donde no.
La versión integrada reúne 699 series reales versionadas (B, E3, ACO y G) y
41 sombras, para 740 trayectorias y 51.210 puntos. No reemplaza ni aumenta el
corpus de 721 casos.

Esta integración corrigió una interpretación visual importante: en la primera
versión, las 721 sombras se construían desde `m=1`, por lo que la imagen
parecía mostrar un origen común. Esa cabeza común era producto de la
construcción, no una propiedad empírica del conjunto. En la versión integrada,
las series observadas comienzan en escalas distintas. Se conserva la
ampliación del abanico entre trayectorias y, en ACO, la convergencia
descriptiva de la cohorte cruda; las sombras siguen marcadas como modelos.

La clasificación exploratoria leave-one-out de la tela integrada alcanza
50,7% por dominio y 66,2% por tono nominal `φ`. Esas cifras no prueban que la
forma recupere el dominio o mida fricción: el procedimiento es de centroide,
no está calibrado como clasificador y `φ` no es una variable continua
observada. El resultado que sí sobrevive es más acotado: la visualización
permite comparar trayectorias bajo una receta declarada, siempre que se
preserve la distinción entre series observadas, modelos y proyecciones.

### Estado actual en una frase

SNT conserva una herramienta descriptiva para comparar trayectorias
hub–nodo, un eje ACO-A para ciertas absorciones post-colapso y un marco de
proyección que hace explícito qué se observó y qué no. La evidencia respalda
reconstrucciones concretas y algunas descripciones locales; no respalda una
ley universal de satelización, un clasificador cimático validado ni una
predicción general de colapso.

Las numeraciones son independientes: **v2.7.1** es la versión del repositorio,
**v6** identifica el corpus consolidado y **v34** el marco teórico.

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
esa pregunta estrecha, no una reparación de los cuatro casos del corpus. La
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

- **Paquete de replicación en Zenodo:** [DOI 10.5281/zenodo.19446521](https://doi.org/10.5281/zenodo.19446521).
  El registro corresponde a la línea del corpus real de 721 casos (paquete
  v2.5.0); **no es un archivo versionado de la release v2.7.1** ni incluye
  automáticamente las actualizaciones posteriores de la tela. Para el código,
  datos y figuras vigentes, consulta este repositorio.
- **Preprint en SSRN:** [abstract 6418778](https://ssrn.com/abstract=6418778).
  El manuscrito r32 se preparó para reemplazar la revisión v30 alojada allí.
  El estado registrado en este repositorio indica que la carga de r32 estaba
  pendiente de la acción del autor; consulta la página SSRN para confirmar qué
  versión está actualmente disponible. No se presenta el manuscrito como
  arbitrado.
- **Archivos del manuscrito r32:** [inglés (PDF)](papers/snt_ssrn_v32_EN.pdf) ·
  [español (PDF)](papers/snt_ssrn_v32.pdf) ·
  [metadatos y revisión preparada para SSRN](papers/SSRN_revision_v32.md).
  El manuscrito identifica la release v2.6.1 como su base; no incorpora
  automáticamente los cambios v2.7.1.
- **Cita del software:** [`CITATION.cff`](CITATION.cff), que registra ambos
  identificadores y aclara el alcance del DOI de Zenodo.

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
pytest reconstruction_real/tests
```

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
  `/home/deamon/genomic_agent`.

## Marco y cita

El marco activo es **v34**; la información de cita está en
[`CITATION.cff`](CITATION.cff). Contribuye mediante una rama y un pull request;
no hagas commits directamente a `main`. Cada resultado nuevo debe incluir
fuente, receta reproducible y límites de inferencia; registra los cambios en
[`CHANGELOG.md`](CHANGELOG.md).
