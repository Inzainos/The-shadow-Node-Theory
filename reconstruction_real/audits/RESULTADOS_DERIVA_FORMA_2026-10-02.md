# Resultados — ¿deriva el exponente a lo largo de la vida de un caso?

**Pre-registro:** [`../preregistro/PREREGISTRO_DERIVA_FORMA_2026-10-02.md`](../preregistro/PREREGISTRO_DERIVA_FORMA_2026-10-02.md)
(commit `e9a152c`, subido antes de escribir el script).
**Script:** `code/deriva_forma_friccion.py` (con log). **Sin descargas.**
**Salidas:** `data/deriva_forma_por_caso.csv`, `data/deriva_forma_resumen.csv`.

Prueba de la hipótesis del autor: que la forma no es una etiqueta por caso sino una
**trayectoria dentro del caso** —potencia → lineal → colapso—, y que esa trayectoria
**requiere fricción** para existir, de modo que los ambientes digitales (fricción ≈ 0)
no la tendrían.

**Resultado: la hipótesis no recibe respaldo en ninguno de los tres brazos, y el único
brazo que parecía respaldarla resultó ser un artefacto de selección.**

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

**Veredicto:** con el poder disponible, **`b` se comporta como constante dentro de cada
caso** en los tres dominios. La trayectoria de formas no está respaldada, y el régimen
superlineal **no** es "un caso atrapado temprano".

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

## 6. Qué significa para la SNT

| Afirmación | Estado anterior | Estado ahora |
|---|---|---|
| La forma es una trayectoria dentro del caso (potencia → lineal) | Hipótesis del autor, 2026-10-02 | **No respaldada.** `b` se comporta como constante en los tres dominios al poder disponible |
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
   nominal — en el mismo régimen donde el OLS del Dominio B tiene 67.0%. La
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

## Validación del código

- **A `b` constante con ruido blanco:** 5.3% de falso descendente (nominal 5%).
- **A `b` constante con AR(1) ρ = 0.94:** **4.7%** de falso descendente. El nulo por
  caso absorbe la autocorrelación en el régimen donde el OLS tiene 67%.
- **Con deriva real 1.5 → 0.5:** detectada en 60.7% con ruido blanco, 14.7% con
  ρ = 0.94, y **0.0% en dirección ascendente** — el detector no se equivoca de signo.
- **Con deriva real ascendente 0.5 → 1.5:** 66.0% ascendente, 0.0% descendente.
- **446/446 series del Dominio B** reproducen su `b` publicada con |Δ| ≤ 1×10⁻⁴.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
