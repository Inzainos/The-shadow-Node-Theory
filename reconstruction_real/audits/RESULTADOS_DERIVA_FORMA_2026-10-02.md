# Resultados — ¿deriva el exponente a lo largo de la vida de un caso?

**Pre-registro:** [`../preregistro/PREREGISTRO_DERIVA_FORMA_2026-10-02.md`](../preregistro/PREREGISTRO_DERIVA_FORMA_2026-10-02.md)
(commit `e9a152c`, subido antes de escribir el script).
**Script:** `code/deriva_forma_friccion.py` (con log). **Sin descargas.**
**Entradas, todas versionadas:** `data/maddison_mpd2020.csv`,
`data/binance_cierres_diarios.csv.gz` y
`data/npm_descargas_mensuales_deriva.csv.gz` (agregado mensual de los 450 paquetes de
la cohorte, añadido el 2026-10-03 para que el brazo npm sea reproducible sin el crudo
de 15 MB; SHA-256 en `data/FUENTES.md`, y con él las dos salidas reproducen su hash
registrado al bit).
**Salidas:** `data/deriva_forma_por_caso.csv`, `data/deriva_forma_resumen.csv`.

Prueba de la hipótesis del autor: que la forma no es una etiqueta por caso sino una
**trayectoria dentro del caso** —potencia → lineal → colapso—, y que esa trayectoria
**requiere fricción** para existir, de modo que los ambientes digitales (fricción ≈ 0)
no la tendrían.

**Resultado: la hipótesis no recibe respaldo donde la prueba tiene poder para
evaluarla —el Dominio B— y queda sin probar en los otros dos brazos, cuyo poder no
permite interpretar un negativo. El único brazo que parecía respaldarla, cripto,
resultó ser un artefacto de selección.**

---

## ⚠ CORRECCIÓN DEL 2026-10-02, POSTERIOR A LA PRIMERA VERSIÓN DE ESTE INFORME

**El contraste entre dominios de este diseño es inadmisible y se retira.** Lo detectó
el autor al señalar que el marco establece que cada dominio tiene sus propios valores,
y cada área dentro de un dominio también, y cada una es independiente. Auditoría
completa: [`AUDITORIA_REGLA_POR_DOMINIO_2026-10-02.md`](AUDITORIA_REGLA_POR_DOMINIO_2026-10-02.md).

**Axioma 0.1:** *"obliga a que cada eje tenga definición operativa **por dominio**. Un
eje sin definición operativa en un dominio no se grafica, no se interpreta y **no entra
en ningún ajuste para ese dominio**"*, y *"`m` está definido: es `R` con el **proxy
declarado de cada dominio**"*. **Axioma 2:** cada cavidad *"responde con **modos
propios, no con una frecuencia universal idéntica para todo**"*.

Tres consecuencias, en orden de gravedad:

1. **El estadístico principal —"Dominio B 10.1% − Cripto 55.5% = −45.4 puntos"— no
   mide la fricción y se retira.** No está mal calculado: compara tres proxies
   distintos en tres cavidades distintas, y esa diferencia no es una medición de la
   variable con la que se las etiquetó. Donde este informe decía "CONTRARIO A LA
   PREDICCIÓN", lo correcto es **"comparación no admisible"**.
2. **El papel de npm como "control de fricción cero" se retira**, porque depende de esa
   misma escala.
3. **Había evidencia previa en el repositorio que no se citó.** La nota del Axioma 5
   ya registraba que el ordenamiento de dominios por fricción se probó pre-registrado
   el 2026-09-27 y **falló en las cinco variantes** (ρ de −0.581 a +0.112, todas NO
   RESPALDADA). Y el dominio digital **ya estaba codificado** en ese eje como *"D2
   cuotas digitales — baja (1)"*: la afirmación de que faltaba ubicarlo era falsa, y la
   ubicación a priori de este pre-registro (≈ 0) contradice la del repositorio (1) sin
   decirlo.

**Lo que sobrevive, y es la mayor parte de los números de este informe:** cada brazo
contra **su propio nulo**, que es lo que la regla sí licencia. El resultado del Dominio
B (`b` constante, con el mejor poder de los tres), el artefacto de listado de Binance
(propiedad de esa fuente, no afirmación entre dominios) y el nulo simulado por caso
quedan en pie sin cambio.

**Lea las secciones siguientes con esa corrección aplicada:** son válidas leídas **por
dominio** e inválidas leídas como contraste entre dominios. El pre-registro **no se
edita** —es un pre-registro—; el defecto queda declarado aquí y en la sección de
Desviaciones.

---

---

## Tabla de decisiones

| Punto | Hipótesis pre-registrada | Resultado | Decisión |
|---|---|---|---|
| **Principal** | La deriva es mayor en fricción alta que en fricción ≈ 0 | Dominio B 10.1% − Cripto 55.5% = −45.4 puntos, IC 95% [−50.5, −40.3] | **COMPARACIÓN NO ADMISIBLE** — se retira, ver la corrección de arriba |
| **Post hoc** | — | **70.1%** de las series de cripto tienen su máximo en el **primer 10%** de la serie. Partiendo por posición del pico: 57.5% descendente con pico temprano contra **0.0%** con pico tardío | **La deriva de cripto es un artefacto del momento de listado** |
| **P1, Dominio B** | Deriva presente | 10.1% descendente contra **11.9% ascendente**; deriva mediana −0.003 | **Sin deriva**, y con el **mejor poder** de los tres (31.7%) |
| **P1, npm** | Deriva ausente | 14.9% descendente contra 10.4% ascendente; poder 6.7% | **No informativo** |
| **S1** | "Potencia → lineal" predice cruzar `b = 1` a la baja | **0.0%** en Dominio B, **0.4%** en cripto, 9.6% en npm | **Tres enunciados por dominio**, no uno general: el cruce no ocurre en el Dominio B ni en cripto; en npm ocurre en 9.6% y su brazo está contaminado por el crecimiento del ecosistema |
| **S3** | ¿La deriva es una firma pre-colapso? | Extinguidos 17.1% contra persistentes 14.7%; los extinguidos con deriva mediana **+0.187** (ascendente) | **No hay firma pre-colapso** |
| **S2** | "O muy abruptos o se mantienen" predice masa en los extremos y hueco en medio | El hueco **no existe**: la banda de en medio sale **más llena** que su propio nulo (+6.4 puntos en cripto, +6.2 en npm), y la banda "se mantiene" está vacía en los datos **y en el nulo** (0.5% / 0.0%) | **Sin respaldo**, y la mitad "se mantienen" no es ni medible |
| **S4** | ¿Los casos con `b ≥ 1` están "atrapados temprano"? | **Tres enunciados por dominio.** Dominio B: lo contrario —`b` de la 1ª ventana 0.007 contra `b` global 1.082, y 0.0% de deriva descendente (n = 6). npm: compatible —1.110 contra 1.300 y 33.3% descendente contra 13.4% del resto (n = 33). Cripto: n = 2, no dice nada | **No se sostiene como enunciado general** |

**Veredicto:** **no se evidenció deriva apreciable de `b` dentro de los casos**, y el
alcance de esa frase es desigual entre los tres brazos, porque el poder lo es:

- **Dominio B, 31.7% de poder contra una deriva 1.5 → 0.5:** es el único brazo donde
  el negativo se interpreta. Detección descendente 10.1% contra ascendente 11.9%, con
  poder suficiente para haber visto ~32% si la deriva existiera. **Resultado negativo
  real, no falta de poder.**
- **Cripto, 11.7%, y npm, 6.7%:** a ese poder **ningún negativo es interpretable**.
  Lo que estos dos brazos aportan no es "`b` es constante" sino "esta prueba no puede
  decirlo aquí". El 55.5% de cripto, además, queda explicado por un artefacto de
  selección (§3) y no por deriva.

Por lo tanto: la trayectoria de formas **no queda respaldada en el Dominio B**, y en
cripto y npm **queda sin probar**, no refutada. Lo mismo aplica a "el régimen
superlineal es un caso atrapado temprano": el cruce del `b = 1` no ocurre en el
Dominio B (0.0%) ni en cripto (0.4%), lo cual **quita el respaldo** a la consecuencia
propuesta sin demostrar su negación.

---

## 1. Los tres brazos y lo que midieron

| Brazo | Fricción | Cantidad | Casos | Deriva descendente | Deriva ascendente | Deriva mediana |
|---|---|---|---:|---:|---:|---:|
| **Dominio B** (países) | alta (3) | cociente | 446 | **45 (10.1%)** | 53 (11.9%) | −0.003 |
| **Cripto** (moneda/BTC) | ≈ 0 | cociente | 571 | **317 (55.5%)** | 21 (3.7%) | **−0.622** |
| **npm** (descargas) | ≈ 0 | nivel | 450 | **67 (14.9%)** | 47 (10.4%) | −0.003 |

Cero casos excluidos por ventanas insuficientes en los tres brazos. Las 446 series del
Dominio B reprodujeron su `b` publicada con |Δ| ≤ 1×10⁻⁴ antes de correr cualquier
prueba.

**El estadístico principal, que es el que prueba la hipótesis** (los dos brazos son
cocientes, así que la diferencia aísla la fricción):

> **Dominio B 10.1% − Cripto 55.5% = −45.4 puntos, IC 95% [−50.5, −40.3].**

**Este estadístico se retira** (ver la corrección al inicio). El intervalo no roza el
cero, pero lo que separa a los dos brazos no es la fricción: son tres proxies distintos
en tres cavidades distintas, y el Axioma 0.1 no licencia leer esa diferencia como la
medición de la variable con la que se las etiquetó. Se conserva el número por
transparencia y porque la auditoría lo cita, no como resultado.

---

## 2. El poder, que es lo que vuelve legible el resultado negativo

Esta tabla **no estaba pre-registrada** y se añadió porque sin ella el resultado del
Dominio B sería ilegible: una fracción baja puede ser ausencia de deriva o falta de
poder. Es la lección del caso de Clauset.

| Brazo | Poder contra deriva +1.5 → +0.5 | Contra +1.0 → +0.5 |
|---|---:|---:|
| **Dominio B** | **31.7%** | **23.3%** |
| Cripto | 11.7% | 6.7% |
| npm | 6.7% | 5.0% |

Y aquí está el punto que decide la lectura:

- **El Dominio B tiene el mejor poder de los tres (31.7%) y la menor detección (10.1%).**
  Si existiera una deriva de 1.5 → 0.5, se habría detectado en ~32% de los casos. Se
  detectó en 10.1%, prácticamente igual a su tasa ascendente de 11.9%. **El resultado
  negativo del Dominio B es interpretable y real, no falta de poder.**
- **Cripto tiene poco poder (11.7%) y la mayor detección (55.5%)** — cinco veces su
  propio poder contra la deriva simulada. Eso significa que lo que hay en cripto es
  mucho más fuerte que una deriva de 1.5 → 0.5. Demasiado fuerte, de hecho, y la
  sección 3 explica por qué.
- **npm no informa nada**: 6.7% de poder, con fracciones descendente y ascendente
  prácticamente simétricas (14.9% contra 10.4%).

---

## 3. El artefacto que mata el único resultado positivo

> **Diagnóstico post hoc, no pre-registrado.** Se corrió **después** de ver que cripto
> daba 55.5%, precisamente porque esa cifra no cuadraba con su poder.

La sospecha: Binance lista una moneda **cuando está en auge**. Si la serie empieza en
su máximo por construcción de *cuándo arrancan los datos*, entonces tiene que bajar, y
en log-log esa bajada se ve como un exponente que se hace cada vez más negativo. No
sería una ley dinámica: sería el momento del listado.

**Lo que se midió sobre los 571 casos de cripto:**

| Posición relativa del máximo en la serie | |
|---|---:|
| Mediana | **0.019** |
| Máximo dentro del **primer 10%** de la serie | **70.1% de los casos** |
| Máximo dentro del primer 25% | **84.9%** |

Y al partir los casos por esa posición:

| Grupo | Deriva mediana | Descendente significativa |
|---|---:|---:|
| **Pico temprano** (< 0.25 de la serie) | **−0.626** | **57.5%** |
| **Pico tardío** (> 0.75 de la serie) | **+0.153** | **0.0%** |

**Cero por ciento.** Cuando la serie no empieza en su máximo, la deriva descendente
desaparece por completo y el signo de la deriva mediana se invierte.

> La deriva de cripto no es una propiedad del tiempo: es una propiedad de **dónde
> empieza la ventana de observación**. Es el mismo defecto de selección que ya nos
> mordió con el filtro de ciudades ≥ 300 mil habitantes de la WUP, con el ROC-AUC
> filtrado del ASI y con la precisión tautológica. **Es la cuarta vez, y es la primera
> que se detecta antes de publicar.**

El Spearman entre posición del pico y deriva da +0.035 con p = 0.41, que **no** es
evidencia en contra de lo anterior: la distribución de la posición del pico está tan
degenerada (85% por debajo de 0.25) que casi no hay variación con la que correlacionar.
La partición en grupos es la comparación informativa, y es inequívoca.

---

## 4. El cruce del `b = 1` no ocurre

La hipótesis específica era **potencia → lineal**, y en `R = a·t^b` lineal es `b = 1`.
Entonces el cruce del 1 a la baja es la predicción puntual:

| Brazo | `b` 1ª ventana (mediana) | `b` última ventana (mediana) | Cruzan `b = 1` a la baja |
|---|---:|---:|---:|
| Dominio B | 0.015 | −0.062 | **0 (0.0%)** |
| Cripto | −0.221 | −2.323 | **2 (0.4%)** |
| npm | 0.322 | 1.858 | 43 (9.6%) |

En el Dominio B **ningún caso** cruza el 1, porque sus exponentes ya empiezan cerca de
cero. En cripto tampoco: no se vuelve lineal, se pasa de largo hasta −2.3. Y en npm el
exponente **sube** en la mediana (0.322 → 1.858) en vez de bajar.

**Nota sobre npm, que contamina su propio brazo:** ese `b` de 1.858 en las ventanas
tardías no es dinámica del paquete, es el **crecimiento del ecosistema npm completo**,
que se multiplicó en el periodo. Un nivel de descargas arrastra la tendencia global;
un cociente la cancelaría. Es exactamente la razón por la que cripto entró al diseño, y
confirma que el brazo de nivel es el débil.

---

## 5. Sin firma pre-colapso

El control de supervivencia en npm —el único brazo donde el muestreo no condicionó al
colapso— pregunta si la deriva es una señal previa a la muerte:

| Grupo | n | Descendente significativa | Deriva mediana |
|---|---:|---:|---:|
| Extinguidos | 41 | 7 (17.1%) | **+0.187** |
| Persistentes | 409 | 60 (14.7%) | −0.007 |

17.1% contra 14.7% es indistinguible con esas n, y los extinguidos tienen deriva
mediana **positiva**. **No hay firma de deriva antes del colapso.**

---

## 5.1 S2 — La bimodalidad de los ambientes digitales no aparece

**Este punto estaba pre-registrado y faltaba en la primera versión del informe.** Se
implementó y corrió el **2026-10-03**, a señalamiento de la revisión del PR #54, junto
con S4. La omisión queda declarada en la sección de desviaciones.

Es la mitad **"o muy abruptos o se mantienen"** de la hipótesis del autor: en fricción
≈ 0 no habría trayectoria gradual, sino dos destinos. El pre-registro fijó el punto
—"fracción que persiste contra fracción que cae, y empinamiento de la caída cuando
cae"— pero **no fijó ni el umbral de "cae" ni un estadístico de bimodalidad**, así que
las dos cosas se declaran aquí y van marcadas como operacionalización posterior:

- **Retención** `r` = mediana de la última ventana / máximo de la serie. Se toma la
  mediana de la ventana y no el último punto para que una sola observación rara no
  decida la clasificación.
- **Cae** si `r < 0.10`; **se mantiene** si `r ≥ 0.90`; lo de en medio es la banda
  gradual. La hipótesis predice masa en los extremos y **hueco en medio**.

Y aquí está lo que vuelve legible el resultado: **cada brazo se compara contra su
propio nulo**, nunca contra el otro. El nulo es `b` constante con la ρ y la σ de ese
mismo caso, 299 réplicas. Sin esa referencia el reparto no se puede leer: con `b`
negativa una serie **baja sola**, así que una fracción alta de "colapso" puede ser la
pendiente y no una caída abrupta. (RNG propio, semilla `20261004`, para no alterar las
réplicas de los puntos ya corridos.)

| Brazo | n | Cae: obs. | Cae: nulo | En medio: obs. | En medio: nulo | Se mantiene: obs. | Se mantiene: nulo |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cripto | 571 | 70.1% | **76.7%** | 29.4% | **23.0%** | 0.5% | 0.3% |
| npm | 450 | 43.8% | **50.0%** | 56.2% | **50.0%** | 0.0% | 0.0% |

**Las tres lecturas, y las tres van contra la hipótesis:**

1. **El hueco en medio no existe. Es lo contrario.** La banda gradual sale **más
   llena** que su propio nulo: +6.4 puntos en cripto, +6.2 en npm. Bimodalidad
   predeciría el signo opuesto.
2. **La fracción que "cae" es menor que la del nulo** en los dos brazos (70.1% contra
   76.7%; 43.8% contra 50.0%). Es decir: estos casos caen **menos** de lo que caerían
   por su sola pendiente con ruido. El "muy abrupto" no está ahí.
3. **La mitad "se mantienen" no es medible con esta definición.** 0.5% y 0.0% en los
   datos, pero **0.3% y 0.0% en el nulo**: la banda `r ≥ 0.90` está estructuralmente
   casi vacía —exige terminar prácticamente en el máximo, que con ruido es raro—, así
   que su vacío **no informa nada sobre el mundo**. Es precisamente lo que el nulo
   sirve para detectar, y por eso no se reporta "casi nada persiste" como hallazgo.

**Empinamiento de la caída, cuando cae** (lo otro que pedía el punto):

| Brazo | n que caen | `b` global (mediana) | `b` de la última ventana (mediana) |
|---|---:|---:|---:|
| Cripto | 400 | −0.836 | **−3.474** |
| npm | 197 | −0.556 | **+2.867** |

En cripto la caída sí se empina muchísimo al final (−3.5 contra −0.8 global), pero esa
cifra **no se puede leer como dinámica**: es el mismo brazo cuyo 70.1% de máximos en el
primer 10% de la serie quedó identificado como artefacto de listado en la §3. En npm el
signo se **invierte** —la última ventana sube a +2.9— por el crecimiento del ecosistema
descrito en la §4. Ninguno de los dos empinamientos es interpretable, y por la regla
por dominio tampoco se promedian.

> **Veredicto de S2:** en los dos brazos digitales, el reparto de destinos no se aparta
> de lo que produce un exponente constante con el ruido de cada caso. La predicción de
> bimodalidad **no recibe respaldo**, y su mitad "se mantienen" no llega a ser medible
> bajo esta operacionalización. Como siempre, es un enunciado **de estos dos brazos con
> este proxy**, no de "lo digital".

---

## 5.2 S4 — Los `b ≥ 1` no están "atrapados temprano", y la respuesta es por dominio

**También pre-registrado y también faltante en la primera versión**; corrido el
2026-10-03.

Primero una advertencia que la propia ronda obliga a poner: **`b ≥ 1` se usa aquí como
corte numérico, no como régimen.** RC1 midió el 2026-10-02 que una exponencial
verdadera ajustada como ley de potencia cae en esa banda casi siempre (99.9% en la
banda alta de E3, 100% en ACO, contra 0.0% donde la `b` real es < 0.5), así que el
umbral **no separa satelización rápida de un desajuste de forma**. Ver
[`RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md`](RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md).

La predicción del autor era: un caso con `b ≥ 1` está **atrapado temprano** en su
trayectoria, así que debería tener `b` de la primera ventana **aún mayor** que su `b`
global y deriva descendente. La comparación es **dentro** de cada brazo:

| Brazo | Grupo | n | `b` 1ª ventana (mediana) | `b` global (mediana) | Descendente sig. |
|---|---|---:|---:|---:|---:|
| **Dominio B** | `b ≥ 1` | 6 | **0.007** | 1.082 | **0 (0.0%)** |
| Dominio B | `b < 1` | 440 | 0.015 | 0.057 | 45 (10.2%) |
| **Cripto** | `b ≥ 1` | 2 | −0.260 | 1.825 | 1 (50.0%) |
| Cripto | `b < 1` | 569 | −0.221 | −0.661 | 316 (55.5%) |
| **npm** | `b ≥ 1` | 33 | **1.110** | 1.300 | **11 (33.3%)** |
| npm | `b < 1` | 417 | 0.288 | −0.223 | 56 (13.4%) |

**Tres enunciados, uno por dominio, como manda el Axioma 0.1:**

- **Dominio B: lo contrario de la predicción.** Sus 6 casos con `b ≥ 1` empiezan con
  `b` de ventana **0.007** —indistinguible del resto del dominio— y terminan con `b`
  global 1.082. No vienen de arriba: su `b` global alta se construye a lo largo de la
  serie. Y **ninguno** tiene deriva descendente significativa, contra 10.2% del resto
  del mismo brazo. Con n = 6 esto no prueba nada por sí solo, pero va en la dirección
  opuesta a la hipótesis, no a su favor.
- **npm: compatible con la predicción, en el brazo más débil.** Ahí sí los `b ≥ 1`
  arrancan alto (1.110) y derivan hacia abajo con más frecuencia que el resto (33.3%
  contra 13.4%). Es el único apoyo que S4 encuentra, y llega con tres descuentos: el
  brazo tiene **6.7% de poder**, es el brazo de **nivel** (contaminado por el
  crecimiento del ecosistema, §4), y son **33 casos**.
- **Cripto: n = 2.** No dice nada y se reporta para que no parezca que se escondió.

> **Veredicto de S4:** la consecuencia "los superlineales son casos atrapados
> temprano" **no se sostiene como enunciado general**. Recibe apoyo en npm y lo
> contrario en el Dominio B, que es justo lo que la regla por dominio predice que
> pasará cuando se intente un enunciado único. Y de todos modos el corte `b ≥ 1` ya no
> designa un régimen desde RC1, así que la pregunta misma quedó reformulada.

---

## 6. Qué significa para la SNT

| Afirmación | Estado anterior | Estado ahora |
|---|---|---|
| La forma es una trayectoria dentro del caso (potencia → lineal) | Hipótesis del autor, 2026-10-02 | **No respaldada en el Dominio B** (31.7% de poder, 10.1% descendente contra 11.9% ascendente). **Sin probar en cripto y npm**, cuyo poder —11.7% y 6.7%— no permite interpretar un negativo |
| La trayectoria requiere fricción; lo digital no la tiene | Predicción diferencial pre-registrada | **No evaluable con este diseño**: el contraste entre dominios es inadmisible (Axioma 0.1) y se retira. Lo que sí queda medido es que el aparente efecto en cripto es un **artefacto de listado**. La formulación admisible —que el dominio digital tiene transiciones más abruptas **contra su propio nulo**— queda sin probar |
| El régimen superlineal es "un caso atrapado temprano" | Consecuencia propuesta para RC1 | **Sin respaldo.** El cruce del 1 ocurre en 0.0% del Dominio B y 0.4% de cripto |
| La deriva como firma pre-colapso | Idea secundaria | **Sin respaldo.** Extinguidos y persistentes indistinguibles |
| Los cinco modos de colapso | Vigentes | **Sin cambio.** Esta prueba no los toca |
| Ortogonalidad b ⊥ Δ, gradiente de Tlaxcala, exponentes publicados | Vigentes | **Sin cambio.** No se reestimó ninguna `b` |

**Lo que sí quedó establecido, y es lo que vale de esta corrida:**

1. **`b` es constante dentro del caso**, hasta donde el poder alcanza. Eso cierra la
   puerta a reinterpretar el régimen superlineal como una fase temprana, y deja el
   pendiente de RC1 donde estaba: si el `b ≥ 1` es mala especificación, no es porque
   sea un tramo de una trayectoria.
2. **El momento de listado de un exchange es un sesgo de selección de primer orden**
   para cualquier análisis de trayectorias en cripto. 70.1% de las series empiezan
   dentro del 10% de su máximo. Quien use datos de Binance para estudiar dinámicas
   temporales hereda esto, y es un hallazgo de instrumento que no depende de la SNT.
3. **El nulo simulado por caso neutraliza la autocorrelación.** A ρ = 0.94, con `b`
   verdaderamente constante, la prueba mantiene 4.7% de falso positivo contra el 5%
   nominal — en el mismo régimen donde el OLS del Dominio B tiene 59.5%. La
   herramienta sirve y es reutilizable.

### Lo que NO se concluye

El poder va de 6.7% a 31.7% según el brazo. Una deriva **de la magnitud simulada**
(1.0 → 0.5 o 1.5 → 0.5) se habría visto en el Dominio B y no se vio. Una deriva
**más pequeña** sigue siendo indetectable con estos datos, y eso no se resuelve aquí.
Así que lo correcto es: *no hay evidencia de deriva de magnitud apreciable*, no *se
demostró que `b` sea exactamente constante*.

---

## Desviaciones respecto al pre-registro

**Defecto de diseño, detectado después de correr y declarado antes que cualquier
desviación menor:** el pre-registro fijó un contraste **entre dominios** que el marco
teórico no licencia (Axioma 0.1, Axioma 2), y no citó que ese mismo ordenamiento por
fricción ya se había probado pre-registrado el 2026-09-27 y había fallado en cinco
variantes. La causa de raíz: el pre-registro se escribió **antes** de leer el marco y
los resultados previos del eje. Queda como regla de operación — antes de pre-registrar,
leer el marco y los resultados previos del eje que se va a tocar.

**Segunda falta, corregida el 2026-10-03:** la primera versión de este informe
**omitió dos de los cuatro puntos secundarios pre-registrados** —S2 (bimodalidad en
fricción 0) y S4 (relación con RC1)— sin declararlo. Lo detectó la revisión del PR #54.
Están implementados y corridos en las §5.1 y §5.2, y ninguno de los dos cambia el
resultado principal: los dos van en contra de la hipótesis del autor. Omitir puntos
pre-registrados sin declararlo es el defecto que el pre-registro existe para impedir,
así que queda escrito aquí y no en una nota al pie. **El pre-registro de S2 fijó el
punto pero no su definición operativa ni un estadístico de bimodalidad**; las dos cosas
se declaran en la §5.1 y van marcadas como operacionalización posterior a los datos.

Y tres desviaciones menores, todas declaradas:

1. **Brazo de poder añadido.** El pre-registro fijó el nulo pero no el poder. La
   validación del código mostró que con ruido AR(1) fuerte el poder cae a 14.7%, así
   que una fracción baja podría ser falta de poder y no ausencia de deriva. Va marcado
   como `PODER_anadido` en el CSV de resumen y como "añadido, no pre-registrado" en el
   log y en este informe. **Sin esa tabla el resultado del Dominio B no sería legible.**
2. **Diagnóstico post hoc del momento de listado.** No estaba previsto. Se corrió
   después de ver que el 55.5% de cripto no cuadraba con su poder de 11.7%, y está
   etiquetado como post hoc en la sección 3. Es el que cambia la conclusión, así que su
   condición de no pre-registrado es lo primero que se declara.
3. **Cripto quedó en 571 casos y no en los 662 posibles.** El filtro pre-registrado de
   200 días comunes con el hub excluyó el resto. Estaba fijado de antemano; se anota la
   cifra por transparencia.

Lo que **no** se desvió: las ventanas (`w = max(8, n/4)`, paso `w/4`, mínimo 5), las 299
réplicas del nulo por caso, las 1,999 del bootstrap, la semilla `20261002`, la
ubicación a priori de la fricción digital, y el reporte obligatorio de la deriva
ascendente — que fue la que mostró que el Dominio B es simétrico y por tanto nulo.

**Nota de reproducibilidad de la corrida del 2026-10-03.** S2 usa un generador propio
(semilla `20261004`) precisamente para no desplazar el consumo del RNG de los puntos
que ya se habían corrido y publicado. Verificado: `deriva_forma_por_caso.csv` conserva
su SHA-256 **al bit** (`56eeb28b…c9b299`). El único archivo que cambia es
`deriva_forma_resumen.csv`, y cambia **solo por las filas nuevas** `S2_*` y `S4_*`; su
hash actualizado está en `data/FUENTES.md`. Ninguna cifra de P1, del estadístico
principal, de S1, de S3 ni de la tabla de poder se movió.

## Validación del código

- **A `b` constante con ruido blanco:** 5.3% de falso descendente (nominal 5%).
- **A `b` constante con AR(1) ρ = 0.94:** **4.7%** de falso descendente. El nulo por
  caso absorbe la autocorrelación en el régimen donde el OLS tiene 59.5%.
- **Con deriva real 1.5 → 0.5:** detectada en 60.7% con ruido blanco, 14.7% con
  ρ = 0.94, y **0.0% en dirección ascendente** — el detector no se equivoca de signo.
- **Con deriva real ascendente 0.5 → 1.5:** 66.0% ascendente, 0.0% descendente.
- **446/446 series del Dominio B** reproducen su `b` publicada con |Δ| ≤ 1×10⁻⁴.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
