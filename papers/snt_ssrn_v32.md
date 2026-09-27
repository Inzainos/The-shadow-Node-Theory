# Shadow Node Theory v2.6.0 (manuscrito r32):
## Invarianza de escala en el algoritmo de satelización de nodos — y una Capa Universal de Colapso Orbital Acoplado (ACO-A)

*Verificación empírica en 721 casos reales, cinco pruebas pre-registradas y evidencia de colapso en cinco dominios*

**Elán Zainos Corona**  
Fractal Core Research · Tlaxcala, México · elan.zainos.corona@gmail.com  
DOI: https://doi.org/10.5281/zenodo.19446521 · SSRN: https://ssrn.com/abstract=6418778  
GitHub: https://github.com/Inzainos/The-shadow-Node-Theory  
Pre-print, revisión del manuscrito r32 (2026-09-27; sustituye a la v30 publicada el 2026-06-28 e incorpora la r31, una revisión intermedia preparada el mismo día y no publicada) — release del repositorio v2.6.0 — no arbitrado. Datos y metodología disponibles para revisión. Versión en español de `snt_ssrn_v32_EN.md`; ante cualquier discrepancia rige la versión en inglés enviada a SSRN.

| Campo | Contenido |
|---|---|
| Clasificación JEL | O18 · O33 · D85 · C63 · O11 · R11 · C22 |
| Palabras clave | Shadow Node Theory · invarianza de escala · ley de potencia · satelización · fricción institucional · colapso orbital acoplado (ACO-A) · función de hazard · pre-registro · leapfrog · Índice de Soberanía Atómica |
| Datos principales | Corpus real de 721 casos (`reconstruction_real/`) · Maddison Project Database 2020 · INEGI y US Census · Correlates of War Trade v4.0 · OWID / JHU CSSE (COVID-19) · Open Exoplanet Catalogue · HackerEarth 2026 (propietario) · Yahoo Finance, NOAA GOES, NASA/ZTF, CoV-Spectrum (capa de colapso) · pruebas pre-registradas: ONU WUP 2018, OWID COVID-19 y mpox, StatCounter, archivo público de Binance, FDIC BankFind |
| Código | Scripts públicos del repositorio (`reconstruction_real/code/`); auditoría integral v32 y resultados del pre-registro en `reconstruction_real/audits/`; pre-registro en `reconstruction_real/preregistro/` |
| Zenodo DOI | https://doi.org/10.5281/zenodo.19446521 (paquete v2.5.0; repositorio activo en release v2.6.0) |
| Conflicto de intereses | El autor es ciudadano de Tlaxcala, nodo sombra del caso mesoamericano analizado. El sesgo potencial se mitiga con el uso exclusivo de fuentes cuantitativas externas verificables. |

> **Nota de revisión (r32, 2026-09-27).** Se **pre-registraron** cinco pruebas —
> hipótesis, codificación de fricción, listas de casos y reglas de decisión subidas
> al repositorio público antes de descargar cualquier dato nuevo
> (`reconstruction_real/preregistro/PREREGISTRO_2026-09-27.md`) — y se corrieron
> con datos públicos nuevos. Se reporta todo resultado, favorable o no: (1)
> *disparadores codificados a ciegas:* **respaldada** — en 8 de 8 ciudades
> favorecidas por un decreto abrupto (cuatro traslados de capital, cuatro zonas
> económicas especiales de China), la retadora gana terreno sobre la incumbente más
> rápido que ciudades con la misma razón inicial de tamaño (Wilcoxon de una cola
> p = 0.0039; §5); sustituye al 5.9× retirado con un diseño limpio, n chico y una
> salvedad de supervivencia; (2) *fricción con dominios nuevos sin COVID:* **no
> respaldada** — ρ(fricción, b medio del dominio) = −0.131 en siete dominios,
> permutación exacta p = 0.39 (§12); (3) *series crudas de COVID-19:* el dominio E3
> se reproduce desde los datos crudos (233 de 234 casos) y su significancia
> sobrevive la corrección por autocorrelación (cota AR(1) conservadora: 176 de 198
> casos estimables); el dominio E1 (4 casos) no es reproducible (§3.3, §9); (4)
> *hub comercial variable en el tiempo para pares de países:* **no respaldada**
> (diferencia mediana −0.009, p = 0.95), y a 30 años el efecto es el opuesto (§12);
> (5) *cohortes ampliadas de ACO-A:* ortogonalidad b ⊥ Δ **respaldada por
> equivalencia** en 242 pares cripto (ρ = −0.119, IC 95% [−0.241, +0.007]);
> h(τ) > 0 **respaldada** en 663 pares cripto y 27,771 bancos de EE. UU.; un hazard
> que crece con la edad aparece solo en cripto, donde está confundido con el
> calendario, mientras que los bancos muestran forma de bañera (§13). La
> significancia del dominio B corregida por autocorrelación sigue siendo una cota
> (33–112 de 156 casos estimables): los errores Newey-West estándar dan 120 de 156,
> por encima de la cota superior, porque subcorrigen con residuos tan persistentes.
> La nota de la r31 se conserva abajo; la r31 no se publicó por separado.

> **Nota de revisión (r31, 2026-09-27).** Una auditoría interna integral (v32)
> recalculó cada cifra publicada a partir de los datos versionados, y los datos del
> dominio B se volvieron a verificar. La aritmética del corpus se replica con
> exactitud; la capa de inferencia no. Por eso esta revisión **retira** o
> **corrige** las siguientes afirmaciones de la v30, cada una con la evidencia de la
> sección citada: (1) se **retira** el resultado "los disparadores abruptos son 5.9×
> más rápidos que los graduales": la razón proviene de una tabla de 2 casos
> abruptos contra 2 graduales (5.87×, p = 0.33), la prueba reportada (U = 24,802,
> n = 486) no corresponde a ningún conjunto de datos del repositorio y el corpus
> activo no tiene una variable de disparador utilizable (§5, §12); (2) el ROC-AUC =
> 0.9994 del modelo de abandono de HackerEarth estaba afectado por fuga de datos; el
> valor corregido, de primera sesión, es **0.715 ± 0.019** (§6.3); (3) se **retira
> por tautológica** la "precisión = 1.0, cero falsos positivos" del ASI: se midió
> contra una etiqueta definida por el mismo umbral ASI > 1 (§6.6); (4) el hallazgo
> de fricción conserva su dirección, pero su p-value por caso está inflado por la
> autocorrelación serial y por tratar como independientes 714 casos agrupados
> (ρ por cluster = −0.56, p = 0.25; §12); (5) el polo sin fricción del contraste de
> regímenes son datos de COVID-19 (§12); (6) el dominio B (62% del corpus) ahora se
> reproduce byte a byte desde la Maddison Project Database **2020**, pero una
> prueba discriminante no lo respalda ni como acoplamiento SNT ni como
> β-convergencia, y reconstruirlo con hubs tomados del comercio bilateral, en vez
> de asignados por PIB, no recupera una señal de acoplamiento (§12). La nota de la
> v30 se conserva abajo como registro.

> **Nota de versión (v30).** Esta revisión sustituyó al preprint SNT v2.3.1
> (corpus de 502 casos). Una auditoría de junio de 2026 encontró que ese corpus
> contenía ~188 valores de b generados sintéticamente (`np.random.normal()`) y una
> columna de R² con valores imposibles (hasta −7.332); fue **retirado**. Esta versión
> usa un **corpus de 721 casos reconstruido íntegramente desde fuentes primarias
> verificables** (R² ∈ [0,1] en todos los casos; reproducible desde
> `reconstruction_real/`) e integra una nueva **Capa de Colapso Orbital Acoplado
> (ACO-A)**. La hipótesis de la razón áurea (H-φ) se puso a prueba y se **refutó en
> cuatro rondas** (con control placebo) y queda excluida de las afirmaciones
> principales.

---

## Resumen

Este trabajo presenta la Shadow Node Theory (SNT), un modelo formal de
satelización de nodos que opera en tres escalas de resolución sistémica — Micro
(Nodo Atómico / individuo), Meso (Red Fúngica intra-nacional) y Macro (colisión de
superorganismos entre naciones y plataformas digitales). La hipótesis central
sostiene que, cuando dos nodos de poder orbitan en proximidad crítica, el nodo con
mayor ventaja acumulada sateliza al nodo históricamente dominante mediante un
algoritmo cuya dinámica sigue una ley de potencia invariante a la escala temporal y
al sustrato: R(t) = a·t^b, donde b es el parámetro de velocidad de satelización.

La SNT aporta cuatro contribuciones empíricas: (1) la formalización del Modelo de
Triple Resolución Sistémica, con condiciones de aplicabilidad distintas por
escala; (2) la verificación de una matriz de N-cuerpos con datos de INEGI para
México (32 entidades federativas, b = −0.473, R² = 0.838, p < 0.001), que revela
que el modelo binario subestimaba 9.3× el gradiente de satelización de Tlaxcala;
(3) la operacionalización del Índice de Soberanía Atómica (ASI) con datos de
comportamiento de 4,774 usuarios y 409,287 eventos (HackerEarth 2026; su modelo de
abandono con datos de primera sesión alcanza ROC-AUC = 0.715 ± 0.019 tras corregir
una fuga de datos); y (4) un corpus de **721 casos reconstruidos desde fuentes
primarias verificables** que abarca dominios históricos, económicos, biológicos,
astronómicos y digitales.

Del corpus real emergen dos hallazgos, ambos con salvedades de inferencia
explícitas. Primero, **la fricción institucional se asocia negativamente con la
velocidad de satelización** en todas las variantes de análisis: por caso, Spearman
ρ = −0.68 (n = 714); como los 714 casos están agrupados en seis dominios y los
ajustes por caso del dominio B están autocorrelacionados, el p-value por caso
(2.5×10⁻⁹⁷) está inflado — a nivel de cluster de dominio ρ = −0.56 (p = 0.25,
n = 6) y el intervalo del bootstrap por cluster es [−0.72, −0.01]; una prueba
pre-registrada que agrega siete dominios nuevos o sin COVID no respalda el orden
por fricción (ρ = −0.131, permutación exacta p = 0.39): fuera de las epidemias,
ciudades y países convergen (b < 0) y los mercados digitales quedan cerca de cero.
Segundo,
**separación de regímenes**: los dominios sin fricción (b̄ ≈ +0.95) satelizan más
rápido que los dominios económicos con fricción (b̄ ≈ +0.09); el polo sin fricción
está formado por completo por datos de propagación de COVID-19 (238 casos), y
quitar sus 234 casos de E3 reduce la correlación de fricción a ρ = −0.12
(n = 480). El polo es real en sus datos: E3 se regenera desde las series crudas y
su significancia sobrevive una corrección por autocorrelación (cota conservadora:
176 de 198 casos estimables), y una segunda epidemia (mpox 2022) da b̄ = +0.43. Un
tercer hallazgo reportado antes — disparadores abruptos 5.9× más rápidos que los
graduales — descansaba en 2 contra 2 casos y se **retira**; lo sustituye una
prueba pre-registrada con disparadores codificados a ciegas: en 8 de 8 ciudades
favorecidas por un decreto abrupto, la retadora gana terreno sobre la incumbente
más rápido que ciudades con la misma razón inicial (p = 0.0039). El dominio B (pares de países, 62% del corpus) se reproduce con
exactitud desde la Maddison Project Database 2020, pero una prueba discriminante
(nulo calibrado más comercio bilateral del Correlates of War) no lo respalda ni
como acoplamiento hub–nodo ni como β-convergencia; reconstruido con el principal
destino de exportación de cada país como su hub, dos de cada tres países
convergen hacia ese hub, y el hub no se separa más que un socio con la misma
brecha inicial; una prueba pre-registrada con un hub que cambia década por década
tampoco recupera el acoplamiento (p = 0.95). Por lo tanto, la afirmación de que la
soberanía política frena la
satelización como lo hace la interdependencia ecológica se conserva solo como
hipótesis.

Esta revisión añade una **Capa de Colapso Orbital Acoplado (ACO-A)**: el colapso
se reformula como un eje ortogonal (Δ), con una capa de hazard falsable h(τ) > 0
("ningún sistema es eterno"), una taxonomía de modos de colapso de tres factores
(fricción × disparador × piso/techo) y un Principio de Mínima Fricción que los
unifica, demostrado con datos reales en cinco dominios (finanzas, historia, cripto,
biología, astronomía). Cohortes pre-registradas respaldan la ortogonalidad (242
pares cripto, prueba de equivalencia) y h(τ) > 0 (663 pares cripto; 27,771 bancos
de EE. UU.); la forma del hazard depende del dominio. El modelo se acompaña de ocho
criterios de refutación (RC1–RC8) más los criterios del eje de colapso, un
protocolo de diagnóstico de cuatro pasos, un paquete público de replicación y un
pre-registro público.

**Palabras clave:** sistemas complejos, ley de potencia, satelización, invarianza
de escala, apego preferencial, fricción institucional, colapso orbital acoplado,
función de hazard, pre-registro, leapfrog, Índice de Soberanía Atómica, orquestación de IA,
ecosistemas digitales, desigualdad regional, Tlaxcala, México.

**JEL:** O18, O33, D85, C63, O11, R11, C22.

---

## 1. Introducción

### 1.1 El problema de la invarianza de escala

¿Por qué algunas regiones siguen siendo pobres pese a décadas de intervención
pública? ¿Por qué algunas naciones convergen hacia los líderes globales mientras
otras divergen de forma irreversible? Estas preguntas comparten un rasgo
estructural que los modelos agregados no logran capturar: la dinámica de
extracción de recursos entre nodos próximos que operan en niveles jerárquicos
distintos. La economía del desarrollo estándar modela la trampa de pobreza como un
problema de acumulación insuficiente de capital. La Shadow Node Theory propone un
mecanismo distinto: la satelización — la extracción progresiva de energía
productiva residual de un nodo periférico por parte de un hub dominante — cuya
dinámica sigue una ley de potencia invariante a la escala temporal y al sustrato.

### 1.2 Antecedentes teóricos

El mecanismo de apego preferencial (Barabási & Albert, 1999) establece que las
redes libres de escala emergen de forma inevitable cuando las nuevas conexiones se
forman con probabilidad proporcional al grado existente. La SNT formaliza el flujo
direccional de recursos dentro de esas redes y cuantifica la tasa de divergencia
entre el hub y el nodo sombra mediante el exponente b de la ley de potencia. La
teoría del leapfrogging (Brezis & Krugman, 1993) identifica las condiciones en que
un nodo periférico puede rebasar a uno dominante invirtiendo en una dimensión
ortogonal. La SNT lo extiende a tres escalas y formaliza las condiciones de fracaso
que el modelo original no desarrolló.

### 1.3 La brecha en la literatura

Tres brechas motivan este trabajo. Primero, ningún modelo existente cuantifica la
dinámica de satelización en ciudades históricas, Estados nación, regiones
intra-nacionales y plataformas digitales dentro de un marco formal unificado.
Segundo, la taxonomía de disparadores de la teoría del leapfrogging reúne los
tipos de evento en una sola categoría y pasa por alto una posible distinción entre
disparadores abruptos y graduales (retirada como afirmación del corpus en la r31
y puesta a prueba por primera vez con disparadores codificados a ciegas en la r32;
ver §5). Tercero, no existe un índice operativo de
soberanía cognitiva para el Nodo Atómico (individuo) calculable desde datos de
comportamiento observables, sin autorreporte. Una cuarta brecha, que atiende esta
revisión, es la ausencia de una explicación unificada y falsable de cómo
**colapsan** los sistemas una vez que termina la relación de satelización — la
Capa de Colapso Orbital Acoplado (Sección 13).

---

## 2. Marco teórico formal

### 2.1 Definiciones

Un **Nodo Sombra** (o Nodo Periférico) es cualquier componente de un sistema cuya
producción es extraída sistemáticamente por un hub dominante a lo largo del
tiempo, lo que produce una divergencia progresiva de capacidad productiva. Un
**Nodo Hub** es el componente dominante que absorbe la energía productiva residual
de los nodos sombra y aumenta su propia ventaja de masa gravitacional. La
**Proximidad Crítica** es el umbral de proximidad espacial, institucional o
digital por debajo del cual el hub puede extraer recursos a tasas mayores que la
capacidad de regeneración del nodo sombra.

La razón de satelización R(t) = producción_hub(t) / producción_sombra(t) es el
observable central. Cuando R(t) sigue una ley de potencia R(t) = a·t^b con b > 0,
la satelización está activa. Cuando b < 0, ocurre convergencia o leapfrog. El
exponente b es el parámetro de velocidad: b > 0.45 indica satelización acelerada;
0.1 < b < 0.45, satelización gradual; −0.1 < b < 0.1, estado aproximadamente
estacionario; b < −0.1, convergencia o leapfrog. (La v30 vinculaba la banda
acelerada a una "clase de disparador abrupto"; ese vínculo se retira en la r31. La
banda superlineal b ≥ 1 puede reflejar en parte una mala especificación del
modelo — ver el Hallazgo 5 en §12.)

### 2.2 Hipótesis central

Cuando dos nodos orbitan en proximidad crítica dentro del mismo sistema, la razón
de satelización R(t) = producción_hub(t) / producción_sombra(t) sigue una ley de
potencia R(t) = a·t^b, donde b > 0 representa la velocidad de satelización y t es
el tiempo transcurrido desde el evento disparador. Esta relación es invariante a:
(a) la escala temporal — se sostiene desde pares de ciudades medievales hasta
rivalidades entre plataformas digitales; (b) el sustrato productivo — se sostiene
para población, PIB per cápita, conteos de eventos de comportamiento y
participación de mercado; y (c) el nivel del sistema — se sostiene para
individuos, ciudades, regiones, naciones y ecosistemas digitales.

### 2.3 Criterios de refutación

RC1 — Velocidad Escalar: se refuta si una tecnología es adoptada sistemáticamente
más rápido por instituciones que por individuos (RC1a), o si surge una tecnología
sin acceso individual que invierta la jerarquía TC_micro < TC_meso < TC_macro
(RC1b). RC2 — Respuesta Inmune: se refuta si los hubs se adaptan sistemáticamente
hacia las capacidades del nodo periférico en lugar de suprimirlas. RC3 —
Inextraibilidad Cualitativa: se refuta si un hub neutraliza sistemáticamente el
diferencial de conocimiento de un nodo mediante fuga de cerebros, ingeniería
inversa o saturación deliberada. RC4 — Umbral Mínimo Dual: se refuta si un
leapfrog se sostiene con RQ o RL por debajo del mínimo operativo. RC5 — Secuencia
de Expansión: se refuta si la expropiación directa produce resultados más estables
que la absorción silenciosa para la misma clase de nodo. RC6 — Irreversibilidad:
se refuta si un Nodo Sombra revierte la satelización desde dentro del sistema, sin
disparador exógeno y con el hub operando con normalidad.

---

## 3. Metodología

### 3.1 Diseño general

El estudio sigue un diseño cuantitativo mixto que combina análisis de casos
históricos, modelación de una matriz de N-cuerpos para el sistema regional
mexicano, validación con aprendizaje automático sobre datos digitales de
comportamiento y análisis de supervivencia para la capa de colapso. El pipeline
analítico común consiste en: (1) construir la serie temporal de la razón de
satelización R(t) para cada par de casos; (2) linealizar en log-log; (3) estimar
los parámetros a y b por mínimos cuadrados ordinarios; (4) usar la correlación de
Pearson en espacio logarítmico como prueba de significancia; y (5) interpretar con
la taxonomía SNT.

### 3.2 Criterios de selección de casos

Se incluyeron los casos que cumplen cuatro condiciones: (a) dos nodos en
proximidad crítica dentro del mismo sistema; (b) un evento o proceso disparador
identificable; (c) datos de producción o población en al menos cuatro puntos
temporales que abarquen al menos 50 años (o 5 años para los casos digitales); y
(d) un proceso de satelización concluido o en curso. No se excluyó ningún caso por
la dirección del resultado — se incluyen tanto casos de satelización (b > 0) como
de convergencia/leapfrog (b < 0), para evitar el sesgo de confirmación.

### 3.3 Fuentes de datos (corpus real, v30)

El corpus de 721 casos se reconstruye íntegramente desde fuentes primarias
verificables: Maddison Project Database 2020 (pares de países; la edición
versionada reproduce byte a byte los 446 casos del dominio B), INEGI y US Census
(regiones intra-nacionales), Our World in Data / Johns Hopkins CSSE (series de
COVID-19 de propagación espacial y parásito-huésped), el Open Exoplanet Catalogue
(planetario/estelar/multiplanetario), MacLulich (1937) y Elton & Nicholson (1942)
(depredador-presa), y el conjunto HackerEarth 2026 (digital; N = 4,774 usuarios,
409,287 eventos, 141 tipos de evento; propietario, solo resultados agregados).
Integridad: R² ∈ [0,1] en todos los casos (ninguno negativo, ninguno mayor que 1).
El 89% de los casos es significativo de forma **nominal** (p < 0.05, MCO en
log-log sin corrección por autocorrelación); tras una corrección AR(1), solo 156
de los 446 casos del dominio B son estimables (n efectivo ≥ 3) y de ellos siguen
siendo significativos entre 33 y 112 (los errores Newey-West estándar dan 120, por
encima de la cota superior: subcorrigen con residuos tan persistentes, así que rige
la cota). Para el dominio E3, reconstruido desde las series crudas en la r32, 198 de
234 casos son estimables y de ellos siguen siendo significativos entre 176 y 196.
Reproducibilidad: el dominio B se regenera con exactitud desde el archivo Maddison
2020 versionado; el dominio E3 se regenera desde las series crudas de Our World in
Data (casos confirmados acumulados, 60 días desde el primer día con ≥ 100 casos;
233 de 234 b publicados dentro de ±0.01); los cuatro casos de E1 no se pudieron
reproducir con ninguna construcción natural y se declaran no reproducibles; los
datos de HackerEarth son propietarios.

### 3.4 Pipeline de análisis

Para cada par de casos se calcula R(t) en cada punto de observación. El tiempo t se
mide en años (o días en los casos digitales) transcurridos desde el disparador. La
transformación log-log log(R) = log(a) + b·log(t) permite estimar por MCO. Se
reporta (a) el exponente b; (b) el R² del ajuste log-log; (c) el coeficiente de
correlación de Pearson y su p-value; y (d) la clasificación SNT. Para la matriz de
N-cuerpos de México se calcula además el gradiente compuesto — la fuerza total de
satelización sobre cada nodo considerando todos los hubs de nivel superior.

### 3.5 Pruebas estadísticas

Efecto de la fricción institucional: correlación de Spearman entre un índice de
fricción a priori (ordinal 0–3) y b por caso (dominios sociales/biológicos).
Separación de regímenes: U de Mann-Whitney entre los dominios sin fricción y los
dominios económicos con fricción. Como los casos están agrupados dentro de
dominios, la r31 añade el Spearman por cluster (medias de dominio), un bootstrap
por cluster y variantes con exclusión de dominios (sin E3; sin E3 ni B); la
autocorrelación serial de los ajustes del dominio B se trata con una corrección de
n efectivo AR(1) (Durbin-Watson). El efecto del tipo de disparador (abrupto vs
gradual) se recalculó en todos los conjuntos del repositorio con etiqueta de
disparador (§5). El constructo del dominio B se examina con una prueba
discriminante: la correlación de b con la brecha inicial de PIB se compara contra
un nulo sintético calibrado con los datos de Maddison (el hub se asigna por PIB
medio, lo que acopla por construcción la brecha y la pendiente), y se mide la
correlación de b con la participación del comercio bilateral (Correlates of War
Trade v4.0). El dominio B también se reconstruye con un hub que emerge del
comercio (el mayor destino de exportación de cada país en su primera década de
datos), con el mismo ajuste, y el hub comercial se compara con socios emparejados
por brecha inicial. Capa de colapso: Spearman ρ(b, Δ) para la ortogonalidad y
supervivencia de Kaplan-Meier para el hazard. Umbral de significancia α = 0.05;
todas las pruebas en Python 3.11 (scipy.stats); scripts en el repositorio público.

**Pruebas pre-registradas (r32).** Antes de descargar cualquier dato nuevo, las
hipótesis, la codificación de fricción, las listas de casos, las reglas de decisión
y la semilla aleatoria de cinco pruebas se subieron al repositorio público; la
fecha del commit es el sello de tiempo, y toda desviación se reporta con su motivo
(`reconstruction_real/audits/RESULTADOS_PREREGISTRO_2026-09-27.md`). Fuentes
públicas nuevas, cada una archivada con su SHA-256: ONU World Urbanization
Prospects 2018 (aglomeraciones urbanas ≥ 300 mil, anual 1950–2018), Our World in
Data COVID-19 y mpox, cuotas de mercado mundiales de StatCounter (2009–2024),
Correlates of War Trade v4.0 por década, el archivo público de Binance (cierres
diarios de 663 pares spot, 2017–2026) y FDIC BankFind (27,834 instituciones
aseguradas). La unidad de inferencia es siempre la unidad independiente más gruesa
(dominio, nodo, hub o caso). Pruebas: permutación exacta del Spearman a nivel de
dominio (fricción); Wilcoxon de rangos con signo de una cola sobre diferencias
emparejadas (hubs, disparadores); equivalencia con IC 95% dentro de ±0.3
(ortogonalidad); hazard por bandas de edad con entrada tardía (supervivencia).

---

## 4. Resultados — estudios de caso históricos

*Nota (r31): los cuatro casos históricos que siguen provienen del estudio original
v1.0. Son estudios de caso ilustrativos, no forman parte del corpus activo de 721
casos, y sus valores se reportan tal como se estimaron originalmente.*

### 4.1 Brujas → Amberes (1300–1560)

Mecanismo: colapso de infraestructura física (sedimentación del canal del Zwin,
c. 1490). R(t) = población de Amberes / población de Brujas sigue una ley de
potencia con b = +0.739 (R² = 0.868). Se clasifica como satelización acelerada con
disparador abrupto. Brujas fue el hub comercial dominante del norte de Europa
durante dos siglos antes de que la sedimentación del canal le cortara el acceso
marítimo; Amberes, con acceso abierto por el Escalda, absorbió la red comercial en
dos generaciones.

### 4.2 Toledo → Madrid (1528–1787)

Mecanismo: decreto político puro (traslado de la corte imperial por Felipe II,
1561). R(t) = población de Madrid / población de Toledo: b = +0.694 (R² = 0.924),
el mejor ajuste del conjunto. Toledo era la ciudad más grande de Castilla; Madrid,
una villa de menos de 4,000 habitantes en 1528. A 40 años del traslado de la corte,
Madrid ya había superado a Toledo — el decreto político por sí solo, sin ventaja
geográfica, basta para generar satelización de alta velocidad.

### 4.3 Portugal frente al noroeste de Europa (1535–1980)

Mecanismo: Unión Ibérica (1580) combinada con la ventaja atlántica acumulada de las
potencias del noroeste de Europa. Disparador clasificado como híbrido. R(t) = PIB
per cápita del noroeste de Europa / PIB per cápita de Portugal: b = +0.060,
R² = 0.123 — el ajuste bajo refleja un proceso oscilatorio (el oro brasileño causó
recuperaciones parciales entre 1700 y 1750). La tendencia de largo plazo es
inequívocamente divergente (la brecha se multiplicó 3.5× entre 1535 y 1913).

### 4.4 Tlaxcala → Puebla (1550–2022)

Mecanismo: extracción colonial acumulada + industrialización diferencial. R(t) =
PIB per cápita de Puebla / PIB per cápita de Tlaxcala: b = +0.184 (R² = 0.567),
satelización gradual. Un punto crítico: el modelo binario subestima la
satelización real de Tlaxcala porque mide solo el gradiente Tlaxcala–Puebla; la
matriz de N-cuerpos (Sección 8) revela que el 89.2% de la extracción fluye
directamente hacia la Ciudad de México, lo que hace al gradiente compuesto real
9.3× mayor.

---

## 5. Discusión: la taxonomía de dos velocidades

### 5.1 El hallazgo central

Los casos históricos sugieren dos clases de dinámica de satelización. Los casos
con disparador abrupto (Brujas-Amberes, Toledo-Madrid) generan exponentes en el
rango b = 0.69–0.74; los casos graduales/híbridos (Portugal, Tlaxcala) generan
b = 0.06–0.18; la razón entre las medias de clase es 5.87×. **Es una hipótesis, no
un resultado confirmado** (revisado en la r31). Con 2 casos por clase la prueba de
Mann-Whitney no puede alcanzar significancia (p = 0.33, su valor mínimo posible).
La v30 afirmaba que el orden estaba "confirmado a escala" en el corpus de 721 casos
(U = 24,802, p = 1.91×10⁻⁵, n = 486); la auditoría encontró que n = 486 no
corresponde a ningún conjunto de datos del repositorio y que el corpus activo no
tiene variable de disparador utilizable (los 446 casos del dominio B están
codificados todos como "gradual" por asignación), así que esa afirmación se
retira. Un corpus histórico de 57 casos da una razón de 6.3 (p = 0.053), pero es
anterior al corpus verificado y contiene valores de R² imposibles, por lo que no es
citable. Los únicos datos activos con etiqueta de disparador son los 18 casos de la
capa de colapso, que miden otro exponente (absorción tras la extinción funcional
del hub); ahí gradual ≥ abrupto (razón 0.47, p = 0.10), con el disparador
confundido con el dominio. Poner a prueba la hipótesis de dos velocidades requiere
un corpus de satelización con disparadores codificados de forma independiente.

**Prueba pre-registrada con disparadores codificados a ciegas (r32).** Se
codificaron doce casos abruptos, por decreto, antes de ver cualquier serie de
población: ocho traslados de capital y cuatro zonas económicas especiales de China
(1980). Los datos son las series anuales de aglomeraciones de la ONU, World
Urbanization Prospects 2018 (1950–2018). En cada caso, R = población de la retadora
/ población de la incumbente desde el año efectivo hasta 2018, ajustada como el
corpus; su b se compara con el de hasta cinco ciudades de control del mismo país (o
de cualquier país si hay menos de tres) emparejadas por razón inicial. Tres casos
quedan fuera porque una ciudad no está en el archivo (Dodoma, Yamoussoukro, Zomba) y
Berlín/Bonn no tiene controles emparejados; quedan ocho:

| Caso | Año | b (caso) | b medio (controles) | d |
|---|---:|---:|---:|---:|
| Brasília / Río de Janeiro | 1960 | +0.740 | +0.456 | +0.284 |
| Islamabad / Karachi | 1967 | +0.396 | +0.066 | +0.331 |
| Abuja / Lagos | 1991 | +0.391 | −0.089 | +0.480 |
| Astaná / Almaty | 1997 | +0.259 | −0.081 | +0.340 |
| Shenzhen / Cantón | 1980 | +1.241 | +0.003 | +1.238 |
| Zhuhai / Cantón | 1980 | +0.665 | +0.167 | +0.499 |
| Shantou / Cantón | 1980 | +0.200 | −0.324 | +0.524 |
| Xiamen / Fuzhou | 1980 | +0.192 | −0.064 | +0.256 |

d > 0 en 8 de 8 casos (d mediana = +0.410; Wilcoxon de una cola p = 0.0039), y lo
mismo con el año de decisión en lugar del año efectivo. La hipótesis pre-registrada
queda **respaldada**: una ciudad favorecida por un decreto abrupto gana terreno sobre
la incumbente más rápido que ciudades comparables. Solo con las cuatro capitales,
4 de 4 (p = 0.0625, el mínimo posible con n = 4) y la razón de b medios es 5.1×,
cercana al 5.9× de la v1.0, pero con cuatro casos. Dos salvedades acotan el
resultado: el archivo lista solo aglomeraciones con ≥ 300 mil habitantes en 2018,
así que quedan fuera los traslados que crecieron poco (Dodoma, Yamoussoukro) y la
muestra de casos se inclina hacia los exitosos; y la prueba compara un decreto
abrupto con la dinámica basal de ciudades con la misma razón inicial, no
disparadores abruptos contra graduales en el sentido de la v1.0.

### 5.2 Interpretación cualitativa (hipótesis)

La distinción teórica clave no es la magnitud del disparador sino su
reversibilidad. Un disparador abrupto — colapso de infraestructura, decreto
político — produce un cambio estructural irreversible que el nodo sombra no puede
compensar movilizando recursos internos. Un disparador gradual — industrialización
diferencial, difusión tecnológica lenta — permite respuestas adaptativas
temporales que comprimen el exponente b sin revertir la dinámica de fondo.

### 5.3 Implicaciones para la intervención temprana

El exponente b tiene implicaciones directas de política pública. Un nodo con
b = 0.70 enfrenta un horizonte de satelización del orden de décadas antes de que la
brecha se vuelva estructuralmente irreversible. Un nodo con b = 0.18 tiene una
ventana más larga, pero el mismo desenlace terminal si no hay intervención. El
protocolo de diagnóstico SNT (Sección 11) ofrece un procedimiento de cuatro pasos
para estimar el b actual, identificar el horizonte de eventos y diseñar
intervenciones en dimensiones ortogonales que puedan generar b < 0 (convergencia)
sin activar la respuesta inmune del hub.

---

## 6. Validación digital: HackerEarth 2026

### 6.1 El experimento

El conjunto HackerEarth 2026 ofrece un registro de eventos de comportamiento de
4,774 usuarios de la plataforma de ciencia de datos Zerve durante una ventana de 98
días: 409,287 eventos, 141 tipos de evento. Constituye un sistema cerrado de nivel
Meso: la plataforma (hub) y sus usuarios (nodos), con flujos de recursos medidos
como métricas de participación.

### 6.2 El Fractal Gap

El Composite Success Index v3 (CSI_V3), una combinación ponderada de diversidad de
herramientas (0.40), vida en la plataforma (0.30) y Velocity of Diversification
Rate (VDR, 0.30), revela una discontinuidad fractal. La cohorte Elite (0.5%
superior, n = 24) muestra un VDR 7,478× mayor que la mediana de la cohorte Basic
(93.1% inferior, n = 4,444). No es la cola de una ley de potencia — es una
discontinuidad fractal consistente con la predicción SNT de una separación
Hub–Nodo Sombra que sigue un apego preferencial.

### 6.3 El Muro de los 5 Eventos

Un Gradient Boosting Classifier que predice el abandono a partir de variables de
**primera sesión** alcanza ROC-AUC = 0.715 ± 0.019 (validación cruzada de 5
pliegues). *Corrección (r31):* la v30 reportó ROC-AUC = 0.9994 (1.0000 en
validación cruzada); ese modelo usaba variables acumuladas en toda la trayectoria de
cada usuario, incluida la actividad posterior al abandono — una fuga de datos que
ya estaba corregida en el script de validación del repositorio. Los usuarios que
ejecutan menos de cinco tipos distintos de evento abandonan con mucha más
frecuencia — el Muro de los 5 Eventos —, detectable dentro de la primera sesión.
Estas cifras provienen del registro de eventos propietario y no pueden
recalcularse desde el repositorio público (la variable de retención no se
distribuye).

### 6.4 Ranking SHAP y el leapfrog cognitivo

El predictor con mayor ranking SHAP es la orquestación de agentes de IA
(agent_accept_suggestion, proxy SHAP ~0.5). Los usuarios que delegan la ejecución
al agente de IA en lugar de ejecutar de forma lineal son el predictor más fuerte
de una trayectoria Elite — el leapfrog cognitivo: pasar de la ejecución lineal a la
orquestación de agentes, una dimensión donde la ventaja acumulada del hub no aplica
y que hoy está al alcance de los recién llegados.

### 6.5 Extensión al dominio empresarial

El caso HackerEarth es la primera demostración empírica de la SNT aplicada a un
ecosistema empresarial cerrado. La condición de aplicabilidad no es el sector ni el
tamaño, sino la disponibilidad de datos estructurados de eventos de comportamiento
que midan los flujos de recursos entre nodos. Cinco métricas del Índice Compuesto
de Soberanía Empresarial (CSIE) — volumen de eventos por nodo, actividad sostenida,
tiempo de respuesta, diversidad funcional y resiliencia ante fallas — identifican
la satelización dentro de estructuras organizacionales antes de que se vuelva
estructuralmente irreversible.

### 6.6 El Índice de Soberanía Atómica (ASI) — estado (r31)

ASI = δH · α / F se puede calcular desde datos de comportamiento (la fórmula se
replica a partir de los puntajes publicados con precisión numérica), y el umbral
ASI > 1 distingue a 13 de 4,774 usuarios (0.27%). La v30 reportó que el ASI
clasifica la soberanía con "precisión = 1.0, cero falsos positivos". Esa cifra se
**retira**: la etiqueta de soberanía contra la que se evaluó está definida como
ASI > 1, así que la clasificación es tautológica. Una prueba válida requiere un
desenlace medido de forma independiente del ASI (por ejemplo, la retención
observada); el modelo de abandono de primera sesión corregido (§6.3) es la única
verificación externa disponible hasta ahora, y no es reproducible con datos
públicos.

---

## 7. Modelo de Triple Resolución Sistémica SNT

El modelo extiende el modelo binario original a tres escalas con dinámicas,
actores y reglas competitivas incompatibles entre sí. La taxonomía de cinco
niveles y la verificación con INEGI 2022 son consistentes con que el sistema
nacional mexicano opere bajo apego preferencial (un ajuste rango-tamaño; ver la
salvedad en §8); la vectorización de trayectorias de ocho entidades (1940–2022)
documenta los primeros casos de leapfrog exitoso dentro del sistema: Querétaro
(b = −0.155, p < 0.01) y Nuevo León (b = −0.058, p < 0.001).

**7.1 Resolución Micro — el Sistema Atómico.** La escala base de procesamiento y
supervivencia. Los recursos se dividen en Cuantitativos (RQ, extraíbles: capital,
tiempo, infraestructura) y Cualitativos (RL, inherentes: conocimiento, habilidades,
madurez cognitiva). RL no puede extraerse de forma directa, pero se degrada por
desuso cuando la escasez de RQ impide su mantenimiento. El leapfrog requiere dos
dimensiones paralelas: Intrapersonal (DI, base obligatoria) y Profesional (DP,
salto visible).

**7.2 Resolución Meso — la Red Fúngica intra-nacional.** Un ecosistema cerrado
delimitado por una jurisdicción geopolítica o institucional. El Hub Central
administra la red mediante la extracción continua de energía residual de los Nodos
Sombra. El hub es prácticamente inamovible desde dentro; su respuesta inmune se
activa según la dirección del crecimiento, no según el tamaño. El hub se expande
por absorción silenciosa, acuerdo pacífico o expropiación — en ese orden de
preferencia por costo energético.

**7.3 Resolución Macro — la colisión de superorganismos.** Competencia entre redes
fúngicas completas; ningún hub central arbitra. La posición relativa la fija la
Masa Gravitacional (MG: PIB total, densidad de población, nivel tecnológico,
superficie territorial). El freno real a la expansión agresiva es la red interna de
nodos, no los reguladores internacionales. El Nodo Atómico nunca escapa por
completo del sistema Macro: su existencia legal y fiscal está anclada a su
superorganismo de residencia.

**7.4 Principios de interacción entre escalas.** Transmisión en cascada: los
eventos Macro impactan a los tres sistemas en cascada descendente (Macro → Meso →
Micro), a una velocidad que depende de la independencia dimensional de cada nodo.
Velocidad escalar: TC_micro (horas–meses) < TC_meso (meses–años) < TC_macro
(décadas–generaciones), con diferencias de 10–100× por nivel. La velocidad es la
ventaja estructural del Nodo Atómico.

---

## 8. Verificación empírica: matriz de N-cuerpos — México

La taxonomía de cinco niveles se verifica con datos de INEGI 2022–2023 para las 32
entidades federativas. Nivel 0 (Ciudad de México): 14.8% del PIB nacional. Nivel 1
(9 atractores secundarios): 41.0%. Nivel 2 (8 nodos de bypass logístico): 20.2%.
Nivel 3 (11 nodos sombra): 16.8%, con el mayor número de entidades. Nivel E (3
anomalías exógenas): 4.3%. El ajuste de ley de potencia rango-tamaño da
b = −0.473, R² = 0.838, p < 0.001 (recalculado en la auditoría: b = −0.4732,
R² = 0.8377). Un ajuste rango-tamaño sobre 32 entidades ordenadas produce un R²
alto casi por construcción, así que esto es consistente con el apego preferencial,
pero no es por sí mismo evidencia de él; queda pendiente la comparación contra una
alternativa lognormal (Clauset et al., 2009).

El gradiente compuesto de Tlaxcala es el resultado central de los N-cuerpos: el
modelo binario midió w_ij(Tlaxcala→Puebla) = 26.2 mil MXN; la matriz de
N-cuerpos revela w_ij(Tlaxcala→Ciudad de México, largo alcance) = 216.8 mil MXN.
Gradiente compuesto total: 243.0 mil MXN — el modelo binario subestimó 9.3× la
satelización de Tlaxcala; el 89.2% de la extracción fluye directamente hacia la
Ciudad de México y rodea al intermediario. La vectorización de trayectorias de ocho
entidades (1940–2022) revela dos grupos naturales: satelización (b > 0): Chiapas
(+0.229), Oaxaca (+0.176), Guerrero (+0.176), Veracruz (+0.181), Tlaxcala
(+0.147), Puebla (+0.116); convergencia (b < 0): Querétaro (−0.155, R² = 0.782) y
Nuevo León (−0.058, R² = 0.935) — los primeros casos documentados de leapfrog
dentro del sistema nacional (Querétaro vía manufactura aeroespacial, Nuevo León
vía manufactura de exportación independiente).

---

## 9. Limitaciones

Se mantienen las limitaciones del corpus original: incertidumbre de datos (±20%)
en las estimaciones históricas anteriores a 1820, R² bajo en el caso de Portugal
(proceso oscilatorio), posible causalidad inversa en el caso digital, sesgo de
selección en la elección de casos y sensibilidad a la definición del disparador en
los casos graduales. Los módulos Micro y Macro del Modelo de Triple Resolución son
marcos conceptuales con operacionalización parcial; las variables RQ, RL, DI, DP y
MG tienen criterios de medición propuestos que aún no se validan con series de
datos estructuradas. El ASI se puede calcular en HackerEarth 2026, pero su
"precisión = 1.0" de la v30 se retira por tautológica (§6.6); requiere validarse
contra un desenlace independiente. El Factor de Coherencia Ck tiene un mecanismo
neurológico verificado (Friston 2010), pero su operacionalización no se ha puesto a
prueba.

**Sobre el corpus:** esta versión retira el corpus de 502 casos publicado antes,
que contenía valores sintéticos, y lo reemplaza con 721 casos reconstruidos desde
fuentes primarias verificables (R² ∈ [0,1]; 89% significativo de forma nominal).
La capa de colapso (Sección 13) es correlacional; la r32 amplía sus cohortes (242
pares cripto para la ortogonalidad; 663 pares cripto y 27,771 bancos para el
hazard), pero sigue siendo una hipótesis fuerte, no una prueba causal.

**Pruebas pre-registradas (añadido en la r32).** De cinco pruebas pre-registradas,
dos respaldan la teoría (disparadores a ciegas; ortogonalidad b ⊥ Δ y positividad
del hazard), dos no (orden por fricción con dominios nuevos; hub comercial variable
en el tiempo) y una es una corrección de reporte (series crudas de COVID-19). Sus
propios límites: la prueba de disparadores tiene ocho casos y un filtro de
supervivencia; la de fricción tiene siete dominios, así que su potencia es baja (el
p de permutación exacta más chico posible es 12/5040 ≈ 0.002, con un orden
perfecto); los picos de la ortogonalidad cripto se concentran en un ciclo de
mercado (153 de 242 en 2021) y el "nacimiento" es el listado en Binance, no el
origen de la moneda; el hazard cripto creciente está confundido con el calendario
(queda pendiente un modelo edad-periodo-cohorte); el archivo de la FDIC no registra
ningún cierre antes de 1970, así que la entrada pre-registrada en 1934 está sesgada
y la decisión usa la entrada en 1970.

**Auditoría integral v32 y reverificación (añadido en la r31).** (i)
*Autocorrelación serial:* los ajustes del dominio B tienen una mediana de
Durbin-Watson de 0.112 y una mediana de ρ AR(1) de 0.944, es decir, un n efectivo
mediano de 2.2 (nominal 69); 290 de 446 casos no son estimables (n efectivo < 3), y
de los 156 estimables siguen siendo significativos entre 33 y 112 según la variante
de corrección. (ii) *Pseudorreplicación:* los 714 casos detrás del hallazgo de
fricción están agrupados en seis dominios; la prueba por cluster no es
significativa (§12). (iii) *Validez de constructo del dominio B:* el hub se asigna
por PIB medio, y 77 de los 91 países que actúan como hub en algún par (85%) son
satélite en otro, así que el rol es una propiedad del par y no una posición en la
red; reconstruido con hubs que emergen del comercio, solo 9 de 102 pares hub–nodo
comerciales están en el dominio B, y el principal destino de exportación cambia
para 2005–2014 en 77 de 102 países, así que un solo hub fijo durante 50–119 años es
en sí una aproximación fuerte. (iv) *Régimen superlineal:* en las 18 series crudas
de la capa de colapso, el AIC prefiere la ley de potencia en 13, una exponencial en
4 (b media = +1.54) y un modelo lineal en 1; cuanto mayor es b, peor ajusta la ley
de potencia, así que parte de la banda b ≥ 1 (102 de 721 casos) puede ser mala
especificación. (v) *Reporte:* los p-values por caso se redondearon a seis
decimales (557 de 721 aparecen como 0.0) y se promediaron dos definiciones de R²
(escala logarítmica y escala original). (vi) *Composición:* el polo sin fricción
(E1 + E3) son datos de COVID-19; E1 modela propagación territorial, no invasión de
especies. (vii) *Reproducibilidad:* el dominio B se reproduce con exactitud desde
el archivo Maddison 2020 versionado; E3 se reproduce desde las series crudas (233 de
234; r32), E1 no es reproducible y los datos de HackerEarth no se distribuyen.

---

## 10. Criterios de refutación

RC1 — Velocidad Escalar: se refuta si una tecnología es adoptada sistemáticamente
más rápido por empresas que por individuos (RC1a), o si surge una tecnología sin
acceso individual que invierta la jerarquía TC (RC1b). RC2 — Respuesta Inmune: se
refuta si la adaptación del hub hacia el nodo periférico se documenta con más
frecuencia que la supresión. RC3 — Inextraibilidad Cualitativa: se refuta si los
hubs neutralizan sistemáticamente los diferenciales de conocimiento del nodo.
RC4 — Umbral Mínimo Dual: se refuta si un leapfrog se sostiene con alguna de las
dos dimensiones por debajo del mínimo. RC5 — Secuencia de Expansión: se refuta si
la expropiación directa produce estados más estables que la absorción silenciosa.
RC6 — Irreversibilidad: se refuta si un Nodo Sombra revierte la satelización de
forma endógena, sin disparador exógeno. RC7 — Operacionalización del ASI: se
refuta si los usuarios con ASI > 1 muestran un desempeño comparable al de los
usuarios con ASI < 0.5 en tareas que requieren soberanía cognitiva (sin poner a
prueba: la "precisión = 1.0" de la v30 era tautológica, §6.6). RC8 — Freno por
interdependencia mutua: se refuta si sistemas depredador-presa o de Estados
soberanos producen b > 0.5 sostenido sin perturbación exógena.

*Nota de numeración (r31): estos son los criterios conceptuales del marco. El README
del repositorio mantiene una lista empírica aparte con su propia numeración (por
ejemplo, su "RC3" es la prueba abrupto vs gradual, ahora marcada como no
comprobable).*

**Criterios del eje de colapso (nuevos).** RC-Δ1 — Ortogonalidad: se refuta si
corr(b, Δ) es significativamente distinta de cero en casos pareados (primera
prueba: cripto n = 11, ρ = +0.009; prueba pre-registrada en la r32: 242 pares,
ρ = −0.119, IC 95% [−0.241, +0.007] dentro de la banda de equivalencia ±0.3 — no
refutado). RC-Δ2 — La fricción gobierna la forma del colapso: se refuta si la
fricción de resolución no predice Δ (primera prueba: cohorte 2008 n = 6,
ρ = −1.000; no se amplía en la r32 por falta de datos públicos comparables). RC-Δ3 —
Positividad del hazard: se refuta si se encuentra un sistema con hazard = 0 (r32:
toda banda de edad con ≥ 30 en riesgo tiene fines en 663 pares cripto y 27,771
bancos — no refutado).

---

## 11. Protocolo de diagnóstico

La SNT es prescriptiva además de descriptiva. Cuatro pasos para aplicar el modelo a
cualquier sistema real. **Paso 1 — Clasificación de nivel:** recolectar datos de
producción de los nodos; verificar si la distribución sigue una ley de potencia
(ajuste log-log, R² > 0.7, p < 0.05); clasificar en la taxonomía de cinco niveles.
**Paso 2 — Cálculo del gradiente:** calcular w_ij para cada hub que extrae del
nodo; calcular el gradiente compuesto si hay varios hubs (el caso Tlaxcala muestra
que el gradiente de largo alcance puede ser 8.3× mayor que el directo). **Paso 3 —
Estimación del horizonte de eventos:** ajustar la trayectoria histórica; si b > 0,
estimar t_horizonte; si b < 0, identificar el mecanismo y verificar que sea
sostenible. **Paso 4 — Identificación de la dimensión ortogonal:** buscar
dimensiones en las que el hub no haya invertido en 5–10 años, en las que el nodo
tenga una ventaja inicial medible y que tengan potencial de apego preferencial;
verificar que no requieran infraestructura controlada por el hub; después diseñar
la intervención (atender la deficiencia crítica al mínimo, construir capacidad sin
activar la respuesta inmune, ejecutar el leapfrog cuando la ventana esté abierta).

---

## 12. Corpus de 721 casos reales — hallazgos

El corpus empírico comprende 721 casos reconstruidos íntegramente desde fuentes
primarias verificables, y reemplaza al corpus previo de 502 casos (retirado tras
una auditoría que encontró ~188 valores de b sintéticos y una columna de R²
imposible). Distribución por dominio (fricción, n, b̄): A Ciudades (media, 4); B
Pares de países, Maddison 2020 (alta, 446, +0.092); C Regiones US Census + INEGI
(alta, 24, +0.091); D Digital (baja, 3, −1.364); E1 Propagación territorial,
COVID-19 (nula, 4, +2.891); E2 Depredador-presa (alta, 2, +0.145); E3
Parásito-huésped, COVID-19 (nula, 234, +0.912); F1–F3 Astronómicos (media/baja, 4).
Total 721, b̄ global = +0.366; integridad R² ∈ [0,1] en todos; 89% significativo de
forma nominal (ver §3.3 y §9 para las cifras corregidas).

**Hallazgo 1 — La fricción institucional se asocia negativamente con la
satelización (resultado central, con salvedades de inferencia).** Correlación de
Spearman entre el índice de fricción a priori y b (dominios sociales/biológicos):

| Análisis | ρ | p | n |
|---|---:|---:|---:|
| Por caso | −0.678 | 2.5×10⁻⁹⁷ | 714 |
| Por cluster de dominio (medias por dominio) | −0.556 | 0.25 | 6 dominios |
| Bootstrap por cluster | −0.434 | IC 95% [−0.722, −0.006] | 6 dominios |
| Sin E3 (COVID-19) | −0.116 | 0.011 | 480 |
| Sin E3 ni B | −0.426 | 0.012 | 34 |

El signo negativo sobrevive en todas las variantes; el p-value por caso no, porque
trata como independientes casos agrupados y autocorrelacionados. El n = 714 excluye
el dominio D (3 casos de HackerEarth), que mide exponentes de distribución de
actividad y no trayectorias R(t); la exclusión es razonable, pero pesa: sin E3 ni B,
incluir D da ρ = −0.145 (p = 0.39, n = 37).

*Prueba pre-registrada con dominios nuevos (r32).* La codificación de fricción de
cuatro dominios nuevos se fijó antes de ver sus datos, y la prueba se corrió a nivel
de dominio y sin COVID-19:

| Dominio | Fricción | n | b medio |
|---|---:|---:|---:|
| E4 mpox 2022 (nuevo) | nula (0) | 59 | +0.425 |
| D2 cuotas digitales, StatCounter (nuevo) | baja (1) | 18 | +0.018 |
| A ciudades (corpus) | media (2) | 4 | +0.082 |
| A2 ciudades, ONU WUP 1950–2018 (nuevo) | media (2) | 1,704 | −0.315 |
| B pares de países, hub de comercio | alta (3) | 102 | −0.074 |
| C regiones (corpus) | alta (3) | 24 | +0.091 |
| E2 depredador-presa (corpus) | alta (3) | 2 | +0.145 |

ρ(fricción, b medio del dominio) = −0.131 en los siete dominios sin COVID-19,
permutación exacta p = 0.39: **no respaldada**, y tampoco en ninguna variante (b
mediana: ρ = −0.430, p = 0.17; con el dominio B publicado: ρ = +0.112; agregando E1
y E3: ρ = −0.581, p = 0.055; agregando D: ρ = +0.049). El polo sin fricción se
repite con una segunda epidemia (mpox, b̄ = +0.43), pero fuera de las epidemias no
hay orden: ciudades y países (fricción media y alta) convergen, y los mercados
digitales (fricción baja) quedan cerca de cero. La relación fricción → b del corpus
descansa, por lo tanto, en el contraste entre epidemias y todo lo demás. El
resultado es una dirección consistente en el corpus original, sin respaldo
inferencial fuera de ese contraste.

**Hallazgo 2 — Separación de regímenes.** Los dominios sin fricción (E1+E3)
producen b̄ ≈ +0.95; los dominios económicos con fricción (A+B+C) producen
b̄ ≈ +0.09. U de Mann-Whitney = 103,538, p = 2.4×10⁻⁷⁴ (por caso; sujeto a la
misma salvedad de agrupamiento). Los 238 casos sin fricción son todos datos de
propagación de COVID-19 (E1 propagación territorial, E3 curvas por país), así que
el contraste compara una epidemia con series económicas; es sugerente, no una ley
general. El lado epidémico es robusto: E3 se regenera desde las series crudas (233
de 234) con una mediana de Durbin-Watson de 0.431 y un n efectivo mediano de 7.25
(nominal 60), y de sus 198 casos estimables siguen siendo significativos entre 176 y
196 tras la corrección AR(1), a diferencia del dominio B (33–112 de 156); mpox 2022
(59 países, b̄ = +0.43) reproduce el polo con un segundo patógeno.

**Hallazgo 3 — Disparadores abruptos vs graduales: retirado (r31), sustituido por
una prueba pre-registrada (r32).** La v30
reportó una razón de 5.9× (U = 24,802, p = 1.91×10⁻⁵, n = 486) "estable en 57 →
114 → 721 casos". Recalculado en todos los conjuntos con etiqueta de disparador: la
razón proviene de 2 vs 2 casos históricos (5.87×, p = 0.33); n = 486 no
corresponde a ningún conjunto; el corpus activo de 721 casos no tiene variable de
disparador utilizable; el corpus no citable de 57 casos da 6.3× (p = 0.053); los
casos de la capa de colapso (otro exponente) dan 0.47× (p = 0.10). La afirmación se
retira. Su sustituta, pre-registrada con disparadores codificados a ciegas sobre
datos de ciudades de la ONU, queda **respaldada**: d > 0 en 8 de 8 ciudades
favorecidas por decreto frente a controles emparejados (Wilcoxon de una cola
p = 0.0039; solo capitales 5.1× con cuatro casos), con una salvedad de
supervivencia (§5).

**Hallazgo 4 — La soberanía política como freno: hipótesis (revisado en la r31).**
Los pares de países soberanos (b̄ ≈ +0.09) y los sistemas depredador-presa (E2,
b̄ = +0.145, n = 2) tienen exponentes medios similares, lo que la v30 leyó como dos
mecanismos que anclan b cerca de cero porque la extinción completa del nodo
destruiría al hub. Esa lectura descansa en el dominio B, cuyo constructo no valida
una prueba discriminante: (a) la correlación de b con la brecha inicial de PIB
(ρ = −0.489, n = 446) cae dentro de un nulo sintético calibrado con los datos de
Maddison (intervalo 95% [−0.577, −0.242]; versión con muestra dividida ρ = −0.385,
p empírico = 0.050, en el límite); (b) con comercio bilateral del Correlates of War
(432 pares), la participación de las exportaciones del nodo hacia su hub no
predice b (ρ = −0.043; permutación intra-región p = 0.72; R² parcial = 0.0001), y la
participación inicial va con un b **menor** (ρ = −0.185; cluster por nodo
p = 0.022), en sentido opuesto a la predicción de acoplamiento. Por lo tanto, el
dominio B no se respalda ni como acoplamiento hub–nodo ni como β-convergencia. (c)
Reconstruido con un hub que emerge del comercio — el mayor destino de exportación
de cada país en su primera década de datos COW (102 de 103 países; 19 hubs
distintos, sobre todo Reino Unido y Estados Unidos) —, solo 9 de los 102 pares
hub–nodo comerciales existen en el dominio B, 62 de los 95 nodos cuyo hub era más
rico convergen hacia él (b < 0), y el hub comercial no se separa más que hasta
cinco socios con la misma brecha inicial que no son socios comerciales importantes
(diferencia mediana −0.014; 45/102 positivas; Wilcoxon p = 0.78; por cluster de
hub, p = 0.62). Una comparación dentro de cada país, entre sus socios, da una
asociación positiva débil y no robusta entre la participación de exportaciones y b
(ρ parcial mediana = +0.115; permutación de signos p = 0.15). (d) Una prueba
pre-registrada con un hub que cambia en el tiempo (r32) — para cada uno de los 103
países del dominio B y cada década de 1900 a 1990, el hub es el principal destino de
exportación en los cinco años previos — compara la trayectoria del país contra ese
hub con hasta cinco socios con la misma brecha inicial que no son socios
comerciales importantes: diferencia mediana −0.009 por nodo, 38 de 96 positivas,
Wilcoxon de una cola p = 0.95 a 20 años (**no respaldada**); a 30 años la
diferencia es significativamente negativa (dos colas p = 0.0002): los países
convergen más hacia su principal socio comercial que hacia un país igual de lejano
con el que casi no comercian. El hub cambia 185 veces entre décadas, y 78 de 96
países cambian de hub al menos una vez. La afirmación de la soberanía como freno se
conserva como hipótesis. La v30 cerraba este hallazgo con
el contraste de que, cuando la transferencia de recursos es directa y sin
mediación (un banco de arenques no puede negociar con un cardumen de caballas; un
Júpiter caliente no pide autorización regulatoria), b supera 1 sin importar el
sustrato. En el corpus, 94 de los 102 casos con b ≥ 1 son series de propagación de
COVID-19 (E1 + E3), y la banda puede reflejar en parte una mala especificación
(Hallazgo 5), así que la r31 lo plantea como conjetura.

**Hallazgo 5 — Regímenes de modelación.** La ley de potencia es la mejor
descripción donde la fricción es baja (propagación epidémica, E1 y E3); con
fricción alta (países) compiten los modelos exponencial y lineal. En las 18 series
crudas de la capa de colapso, el AIC prefiere la ley de potencia en 13, la
exponencial en 4 (b media = +1.54) y el modelo lineal en 1: cuanto mayor es b, peor
ajusta la ley de potencia. El exponente b es una métrica descriptiva y comparable
entre dominios — no la afirmación de que la ley de potencia sea el único modelo
generador en todos los dominios —, y la banda superlineal b ≥ 1 debe volver a
probarse contra modelos alternativos.

---

## 13. Capa de Colapso Orbital Acoplado (ACO-A)

La Arquitectura de Colapso Orbital deja de ser un módulo separado y se reformula
como una **capa universal y transversal** de la SNT: el colapso es un **eje
ortogonal** que puede activarse en cualquier sistema, en cualquier dominio y en
cualquier punto de su trayectoria. Un solo principio (mínima fricción) genera
modos de colapso distintos según las condiciones de frontera, demostrado con datos
reales en cinco dominios.

**13.1 Dos ejes ortogonales (b ⊥ Δ).** Cada sistema es un par de coordenadas
independientes. Eje 1 — Satelización: R(t) = a·t^b, cómo evoluciona la dominancia
mientras corre la relación acoplada. Eje 2 — Colapso: A(τ) = c·τ^Δ, con τ = tiempo
desde la extinción funcional; Δ mide la velocidad/forma de la absorción una vez que
el hub colapsa. El colapso no espera a que termine el ciclo de satelización (otro
reloj, τ ≠ t). Predicción falsable: corr(b, Δ) ≈ 0. Primera prueba (cripto
pareado, n = 11): Spearman ρ(b_subida, Δ_caída) = +0.009 (p = 0.98) — consistente
con la ortogonalidad. Ampliación pre-registrada (r32), mismo método sobre el archivo
público de Binance (664 pares spot contra USDT tras excluir stablecoins, monedas
fiat y tokens apalancados; 663 con velas diarias): 242 pares cumplen las reglas,
Spearman ρ = −0.119 (p = 0.065), IC 95% [−0.241, +0.007], dentro de la banda de
equivalencia ±0.3 — **respaldada**. Si hay asociación, es débil y negativa (a mayor
subida, caída algo más pronunciada). Salvedades: 153 de los 242 máximos ocurrieron
en 2021 (un solo ciclo de mercado), y el "nacimiento" es el listado en Binance.

**13.2 Capa de hazard h(τ).** "Ningún sistema es eterno" = h(τ) > 0 para todo
sistema (refutable si se encuentra un sistema con hazard = 0). Primera estimación
(cohorte cripto, n = 41; extinción funcional = precio < 1% del máximo histórico): 15
extinciones en todo el rango de edad (0.27–8.6 años), sin una era libre de muertes;
Kaplan-Meier decreciente; hazard positivo y creciente con la edad — consistente con
h(τ) > 0. Salvedades: sesgo de supervivencia (el hazard real es mayor), confusión
entre edad y calendario, n limitado. Ampliación pre-registrada (r32), dos cohortes
independientes: (a) 663 pares de Binance, 124 extinciones funcionales: toda banda de
edad de un año con ≥ 30 en riesgo tiene extinciones (8 de 8), y el hazard sube de
0.007 por año en el primer año a 0.18–0.20 por año entre los 4 y los 6 años
(ρ = +0.881, p de una cola = 0.002), pero los pares listados en 2017–2020 llegan a
esas edades durante el mercado bajista de 2022–2025, así que edad y calendario
están confundidos; (b) FDIC BankFind, 27,771 instituciones aseguradas de EE. UU.,
cualquier fin (fusión, adquisición o quiebra), entrada en 1970 porque el archivo no
registra ningún cierre antes de ese año: toda banda de cinco años con ≥ 30 en riesgo
tiene fines (39 de 39), pero el hazard tiene **forma de bañera** (0.04–0.06 por año
en los primeros 35 años, ~0.02–0.03 entre los 35 y los 125, y vuelve a subir en
edades muy altas; ρ = +0.050, p = 0.38); las quiebras solas bajan con la edad y no
aparecen en cuatro bandas de más de 155 años. h(τ) > 0 se sostiene en ambas
cohortes grandes, con fines en todas las edades; la afirmación de la v30 de que el
hazard crece con la edad aparece solo en cripto, donde está confundida con el
calendario, y no se cumple en bancos. La forma del hazard depende del dominio.

**13.3 Taxonomía de modos de colapso (tres factores).** Gobernada por fricción ×
disparador × (piso/techo de la magnitud): Decaimiento Orbital Regulado (fricción
alta → ley de potencia suave o exponencial, sin aceleración; cohorte 2008
R² = 0.85–0.99, Roma/URSS, fulguración solar R² = 0.975, TDE R² = 0.84);
Decaimiento Craquelado (fricción ≈ 0 + gradual → fragmentación errática; EOS
R² = 0.10–0.70); Detenido en Piso (fricción ≈ 0 + abrupto + piso → ley de potencia
hasta un piso residual; FTX R² = 0.875); Precipicio Catastrófico (fricción ≈ 0 +
abrupto + sin piso → super-exponencial; LUNA, 5.6 órdenes de magnitud en 11 días);
Barrido Logístico (magnitud acotada → curva S; Delta→Ómicron k = 0.22/d).

**13.4 Principio de Mínima Fricción (unificador).** Todo colapso sigue la
trayectoria que minimiza la fricción integrada (familia variacional: Fermat, mínima
acción, mínima disipación) — un flujo gradiente sobre un paisaje de estabilidad.
Versión falsable: el colapso realizado tiene menor fricción integrada que las
trayectorias contrafactuales (WaMu por el canal prearreglado de la FDIC = mínima
fricción → 21 h; Lehman sin él → fragmentación lenta, 30,681 h; rango ~1,460×,
monótono con el grado de intervención regulatoria).

**13.5 Resultados con datos reales (cuatro puntos de la hoja de ruta).** (1)
Fricción operacionalizada: dentro de la cohorte financiera de 2008 (n = 6), la
fricción del canal de resolución (ordinal 1–6) contra Δ: Spearman ρ = −1.000,
p < 0.001 — más fricción, absorción más frontal y ordenada. (2) Ortogonalidad
b ⊥ Δ: cripto n = 11, ρ = +0.009 (§13.1). (3) Biología sin cota: la ola de Ómicron
en conteos absolutos (Sudáfrica, JHU) decae de forma exponencial suave (R² = 0.96,
e-fold ~22 d), NO como precipicio — la retroalimentación epidemiológica es
fricción intrínseca. (4) Hazard h(τ) > 0 (§13.2). Conexión con el hallazgo
central: la fricción se asocia negativamente con b (ρ = −0.68 por caso; dirección
robusta, significancia no, y sin respaldo de la prueba pre-registrada con dominios
nuevos — §12) y, en la cohorte 2008 (n = 6), con la forma de Δ — una palanca
candidata para el eje de colapso, que todavía debe ponerse a prueba en cohortes más
grandes.

---

## 14. Diálogo con la literatura

**Barabási & Albert (1999):** la SNT extiende el apego preferencial al cuantificar
la velocidad de satelización con el exponente b y proponer una taxonomía funcional
de cinco niveles. Los datos de INEGI son consistentes con la distribución
rango-tamaño predicha (b = −0.473, R² = 0.838), pendiente de una comparación
lognormal (§8). **Watts & Strogatz (1998):** la SNT añade al coeficiente de
agrupamiento la dimensión direccional del flujo de recursos — dos nodos pueden
estar cerca en distancia de conexión pero en niveles jerárquicos radicalmente
distintos. **Holland (1995):** la SNT especifica la satelización como una dinámica
emergente recurrente, con trayectoria matemáticamente predecible, dentro de los
Sistemas Adaptativos Complejos. **Friston (2010):** la SNT extiende el Principio de
Energía Libre más allá del cerebro individual hacia los sistemas sociales; la
respuesta inmune del hub y el Factor de Coherencia Ck son manifestaciones del mismo
principio en escalas distintas. **Brezis & Krugman (1993):** la SNT extiende el
leapfrogging tecnológico a tres escalas y formaliza las condiciones de fracaso que
el modelo original no desarrolló. **Teoría de catástrofes y resiliencia (Thom 1972;
Waddington 1957; Holling 1973; Lenton et al. 2008):** el lenguaje de paisaje de
estabilidad de la capa de colapso conecta a la SNT con las catástrofes de pliegue,
el paisaje epigenético, la resiliencia ecológica de "bola en copa" y los puntos de
inflexión climáticos.

---

## 15. Conclusiones

**15.1 Lo que la SNT demuestra.** La SNT propone que el ciclo de satelización — de
nodo hijo dependiente a par y a hub de nuevos hijos — opera entre dominios; el
corpus documenta trayectorias de tipo ley de potencia en todos los dominios que
cubre, con las salvedades de inferencia de §9 y §12. La taxonomía de cinco niveles
es consistente con una ley de potencia rango-tamaño en los datos de INEGI
(pendiente la comparación lognormal); el modelo binario subestimaba 9.3× la
satelización de Tlaxcala; se verifican los primeros casos documentados de
leapfrog dentro del sistema nacional mexicano (Querétaro b = −0.155, Nuevo León
b = −0.058); el ASI se puede calcular desde el comportamiento de 4,774 usuarios (su
validación sigue abierta, §6.6). Con el corpus real de 721 casos, **la fricción
institucional se asocia negativamente con b en todas las variantes de análisis**
(ρ = −0.68 por caso; no significativa a nivel de cluster de dominio, ρ = −0.56,
p = 0.25) y, en la cohorte 2008, con la forma del colapso (Δ). La hipótesis de la
razón áurea (H-φ) se puso a prueba y se refutó en cuatro rondas, y el orden abrupto
vs gradual reportado en la v30 se retira (§5); ambos quedan excluidos de las
afirmaciones. Cinco pruebas pre-registradas (r32) aportan la primera evidencia con
diseño limpio: las ciudades favorecidas por un decreto abrupto ganan terreno sobre
la incumbente más rápido que ciudades emparejadas (8 de 8, p = 0.0039);
satelización y colapso son ortogonales dentro de ±0.3 (242 pares cripto); toda
banda de edad tiene fines en 663 pares cripto y 27,771 bancos (h(τ) > 0); y el polo
epidémico (E3) sobrevive una corrección por autocorrelación sobre las series
crudas.

**15.2 Lo que la SNT no demuestra.** Que el leapfrog sea siempre posible para
cualquier nodo. El modelo formaliza condiciones de viabilidad y mecanismos de
fracaso, pero no garantiza el éxito. Los módulos Micro y Macro requieren validación
empírica independiente; el ASI requiere validarse contra un desenlace
independiente de su propio umbral; la capa de colapso es correlacional y requiere
cohortes más grandes y pruebas entre dominios. La SNT no demuestra que el dominio B
mida un acoplamiento hub–nodo: una prueba discriminante con nulo calibrado y datos
de comercio bilateral no respalda esa lectura, y tampoco una reconstrucción con
hubs tomados del comercio, fijos o cambiantes por década (§12, Hallazgo 4). No
demuestra que la fricción ordene b entre dominios: la prueba pre-registrada con
dominios nuevos no lo respalda fuera del contraste epidemias contra el resto
(ρ = −0.131, p = 0.39), ni que el hazard crezca con la edad en general (los bancos
muestran forma de bañera).

**15.3 Líneas de investigación futura.** Validar el Módulo Micro con datos
longitudinales de trayectorias individuales; operacionalizar el ASI en otras
plataformas; extender la matriz de N-cuerpos a otros sistemas nacionales; prueba de
ortogonalidad b ⊥ Δ entre dominios; cohortes más grandes y sin sesgo de
supervivencia para h(τ); pre-registro antes de afirmar causalidad. De la r31,
resuelto en la r32: recuperar las series crudas de COVID-19 (E3 reproducido; E1 no
reproducible), un corpus de satelización con disparadores codificados de forma
independiente (respaldada, n = 8) y una definición de hub variable en el tiempo (no
respaldada). Sigue abierto: estimación GLS o bootstrap por bloques para fijar la
significancia del dominio B corregida por autocorrelación (Newey-West estándar
subcorrige); volver a probar la banda superlineal contra modelos exponencial y
lognormal; un corpus de disparadores más grande y sin filtro de supervivencia; un
modelo edad-periodo-cohorte para el hazard cripto; fricción → Δ más allá de la
cohorte 2008; y una segunda codificación, independiente, de disparadores y
fricción.

**15.4 La implicación mayor.** No es teórica sino práctica. Si la satelización
sigue un algoritmo predecible con una taxonomía de fracaso identificable, es
intervenible. Para Tlaxcala: el 89.2% del gradiente no viene de Puebla sino de la
Ciudad de México — cualquier estrategia que apunte solo a la relación
Tlaxcala–Puebla resuelve el 10.8% del problema. Para el Nodo Atómico: el leapfrog
cognitivo — orquestar agentes de IA en lugar de ejecutar tareas de forma lineal — es
la primera dimensión en la historia reciente en la que la ventaja acumulada de los
nodos dominantes no aplica de forma directa, y la evidencia de HackerEarth 2026
sugiere que esa ventana está abierta ahora.

> *"El algoritmo de satelización es predecible. La taxonomía de fracaso del
> leapfrog es conocida. Lo que sigue es una decisión que ningún modelo puede tomar
> por el nodo."*

---

## Referencias

Avey, J.B., Reichard, R.J., Luthans, F. & Mhatre, K.H. (2011). Meta-analysis of the
impact of positive psychological capital on employee attitudes, behaviors, and
performance. *Human Resource Development Quarterly*, 22(2), 127–152.

Barabási, A.L. & Albert, R. (1999). Emergence of scaling in random networks.
*Science*, 286(5439), 509–512.

Barbieri, K. & Keshk, O.M.G. (2016). *Correlates of War Project Trade Data Set
Codebook, Version 4.0.* En línea: http://correlatesofwar.org.

Barbieri, K., Keshk, O.M.G. & Pollins, B. (2009). Trading data: Evaluating our
assumptions and coding rules. *Conflict Management and Peace Science*, 26(5),
471–491.

Bolt, J. & van Zanden, J.L. (2020). Maddison style estimates of the evolution of
the world economy. A new 2020 update. Maddison Project Working Paper WP-15,
University of Groningen. [Maddison Project Database 2020; la edición que reproduce
el dominio B.]

Brezis, E.S. & Krugman, P.R. (1993). Leapfrogging in international competition.
*American Economic Review*, 83(5), 1211–1219.

Clauset, A., Shalizi, C.R. & Newman, M.E.J. (2009). Power-law distributions in
empirical data. *SIAM Review*, 51(4), 661–703.

Dong, E., Du, H. & Gardner, L. (2020). An interactive web-based dashboard to track
COVID-19 in real time. *The Lancet Infectious Diseases*, 20(5), 533–534. [JHU CSSE]

Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature
Reviews Neuroscience*, 11(2), 127–138.

Holland, J.H. (1995). *Hidden Order: How Adaptation Builds Complexity.*
Addison-Wesley.

Holling, C.S. (1973). Resilience and stability of ecological systems. *Annual
Review of Ecology and Systematics*, 4, 1–23.

INEGI (2022). PIB per cápita por entidad federativa. Sistema de Cuentas Nacionales
de México.

Lenton, T.M. et al. (2008). Tipping elements in the Earth's climate system. *PNAS*,
105(6), 1786–1793.

Thom, R. (1972). *Stabilité structurelle et morphogénèse.* [catástrofe de pliegue]

Waddington, C.H. (1957). *The Strategy of the Genes.* [paisaje epigenético]

Watts, D.J. & Strogatz, S.H. (1998). Collective dynamics of small-world networks.
*Nature*, 393(6684), 440–442.

Zainos Corona, E. (2026). Shadow Node Theory — Replication Package v2.5.0
(721-case real corpus + Coupled Collapse layer ACO-A). Zenodo.
https://doi.org/10.5281/zenodo.19446521. Repositorio actual (release v2.6.0,
auditoría integral v32, prueba discriminante y reconstrucción del dominio B,
pre-registro del 2026-09-27 y sus resultados):
https://github.com/Inzainos/The-shadow-Node-Theory

United Nations, Department of Economic and Social Affairs, Population Division
(2018). *World Urbanization Prospects: The 2018 Revision*, File 22 (población anual
de las aglomeraciones urbanas con ≥ 300 mil habitantes en 2018, 1950–2018).

Mathieu, E. et al. (2020–2024). Coronavirus (COVID-19) and mpox data. *Our World
in Data*. https://ourworldindata.org

StatCounter Global Stats (2009–2024). Cuotas de mercado mundiales mensuales de
navegador, buscador, sistema operativo, redes sociales y fabricante de móviles.

Federal Deposit Insurance Corporation (2026). BankFind Suite API: instituciones
(índice del 2026-09-25) y quiebras (índice del 2026-08-25),
https://api.fdic.gov/banks (consultado el 2026-09-27).

Binance (2017–2026). Archivo público de datos de mercado, velas diarias spot,
https://data.binance.vision (consultado el 2026-09-27).

Fuentes de datos de la capa de colapso: Yahoo Finance (LUNA, FTT, EOS); NOAA SWPC
GOES (rayos X solares); NASA IRSA / ZTF (TDE AT2019qiz); CoV-Spectrum / LAPIS
(variantes de SARS-CoV-2); SEC, FDIC, Federal Reserve, SIGTARP (cohorte 2008).

---

*— Fractal Core Research — Pre-print, revisión del manuscrito r32 (2026-09-27), release del repositorio v2.6.0 — Tlaxcala, México — 2026 —*
