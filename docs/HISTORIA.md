# Historia — SNT: de una hipótesis de escala a una teoría que declara sus límites

> Movida del README (2026-10-26) para dejar arriba solo estado actual,
> tabla de evidencia y cómo reproducir.

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
50,7% por dominio y 66,2% por tono nominal `φ`. Frente a la línea base
mayoritaria (siempre predecir la clase más frecuente), la exactitud por
dominio queda por debajo (60,5%) y la de tono la supera por solo 2,4 puntos
(63,8%). La exactitud balanceada por dominio (55,6%) sí supera ampliamente el
azar (11,1%): la forma contiene información de dominio. Para el tono no hay
evidencia adicional: con un nulo que permuta los tonos entre dominios, el
resultado no se distingue del azar (p = 0,39), y al dejar un dominio fuera
(leave-one-domain-out) la exactitud balanceada es 36,4% contra 33,3% de azar
(p = 0,13). Como `φ` es constante por dominio, identificar el tono equivale a
identificar el dominio. Detalle en
[`TELA_CLASIFICACION_BASELINE_2026-10-25.md`](reconstruction_real/audits/TELA_CLASIFICACION_BASELINE_2026-10-25.md).
Esas cifras no prueban que la forma recupere el dominio por dinámica o mida
fricción: el procedimiento es de centroide, no está calibrado como clasificador
y `φ` no es una variable continua observada. El resultado que sí sobrevive es
más acotado: la visualización permite comparar trayectorias bajo una receta
declarada, siempre que se preserve la distinción entre series observadas,
modelos y proyecciones.

### Estado actual en una frase

SNT conserva una herramienta descriptiva para comparar trayectorias
hub–nodo, un eje ACO-A para ciertas absorciones post-colapso y un marco de
proyección que hace explícito qué se observó y qué no. La evidencia respalda
reconstrucciones concretas y algunas descripciones locales; no respalda una
ley universal de satelización, un clasificador cimático validado ni una
predicción general de colapso.

Las numeraciones son independientes: **v2.7.1** es la versión del repositorio,
**v6** identifica el corpus consolidado y **v34** el marco teórico. El DOI de
Zenodo archiva v2.5.0 y el manuscrito r32 se basa en v2.6.1 (ver «Zenodo y
SSRN»).

