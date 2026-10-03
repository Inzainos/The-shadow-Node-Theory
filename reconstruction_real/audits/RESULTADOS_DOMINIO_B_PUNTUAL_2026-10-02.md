# Resultados — el valor puntual del Dominio B

**Pre-registro:** [`../preregistro/PREREGISTRO_DOMINIO_B_PUNTUAL_2026-10-02.md`](../preregistro/PREREGISTRO_DOMINIO_B_PUNTUAL_2026-10-02.md)
(commit `05bc9ee`, subido antes de correr el script).
**Script:** `code/dominio_B_valor_puntual.py` (con log).
**Datos:** `data/maddison_mpd2020.csv` y `data/by_domain/dominio_B_real.csv`, ya
versionados. **Sin descargas.**
**Salidas:** `data/dominio_B_calibracion.csv`, `data/dominio_B_valor_puntual.csv`.

Cierra el **último número abierto de la teoría**. El valor puntual es **33 de 156
estimables (21.2%)**, producido por el único método de doce cuya tasa de falso
positivo medida cae en la banda de admisión pre-registrada — y con **tres reservas
explícitas** que la §6.1 detalla, porque la admisión es marginal.

---

## ⚠ Nota de corrección — 2026-10-03

**Este informe reemplaza una versión anterior cuya conclusión era la opuesta.** La
primera corrida concluyó que *ningún* método era admisible y que el valor puntual
quedaba "cerrado como indecidible". Esa conclusión **era un artefacto de un defecto
en el código de calibración**, detectado en la revisión automatizada del PR #54 y
corregido aquí.

**El defecto.** En la simulación, el estrato de estimabilidad se clasificaba por la
**realización simulada** —se recomputaba `n_eff` de la serie sintética— en vez de por
el **caso real de origen** del que se tomaba la terna `(n, ρ, σ)`. Con `b = 0` los
residuos simulados son el propio ruido AR(1), y `ρ` se subestima sistemáticamente en
series cortas, así que `n_eff` salía inflada: **1,738 de 2,000 simulaciones (86.9%)
caían en el estrato "estimable"**, cuando en los 446 casos reales ese estrato es
**156 de 446 (35.0%)**. El estrato medido contenía casos de `ρ` alta que el estrato
real no contiene, y esos son precisamente los casos donde todo contraste se rompe.
**Resultado: todas las tasas de falso positivo salían demasiado pesimistas.**

**La corrección.** El perfil que alimenta cada simulación ahora carga si su caso real
de origen es estimable, y el estrato lo fija ese indicador. El estrato simulado pasa
a **733 de 2,000 (36.7%)**, consistente con el 35.0% real, como debe ser al muestrear
uniformemente los 446 perfiles.

**Qué cambió, método por método** (tasa de falso positivo en el estrato estimable):

| Método | Primera corrida (defectuosa) | Corrida corregida | Δ |
|---|---:|---:|---:|
| `ols` | 67.0% | **59.5%** | −7.6 |
| `ar1_inf` | 11.7% | **7.1%** | **−4.6** |
| `ar1_sup` | 53.1% | 48.6% | −4.6 |
| `nw_auto` | 52.3% | 40.8% | −11.5 |
| `nw_n4` | 48.4% | 38.1% | −10.4 |
| `gls_pw` | 17.2% | **11.3%** | −5.8 |
| `boot_rb3` | 43.1% | 30.3% | −12.9 |
| `boot_ub3` | 47.9% | 34.8% | −13.1 |
| `boot_rb8` | 29.5% | 17.1% | −12.4 |
| `boot_ub8` | 40.3% | 27.3% | −13.0 |
| `boot_rb17` | 24.1% | 15.6% | −8.5 |
| `boot_ub17` | 40.0% | 27.6% | −12.4 |
| **n del estrato** | **1,738 / 2,000** | **733 / 2,000** | — |

**Todas** bajaron, en la dirección que el diagnóstico del defecto predice. Una sola
cruzó la banda de admisión `[2.5%, 7.5%]`: `ar1_inf`, de 11.7% a **7.1%**. Por eso la
conclusión se invierte: hay método admisible, y el desenlace pre-registrado que
aplica pasa del tercero al primero.

**Lo que NO cambió.** El punto 3 —los doce métodos sobre los 446 casos reales— es
cálculo sobre datos reales y **no toca la simulación**: sus doce cifras son idénticas
al dígito en las dos corridas (§3). El defecto afectaba *qué método tiene permiso de
hablar*, no *qué dice*. Tampoco cambió la partición 156/290, ni ninguna `b`, ni la
reproducción 446/446.

**Declaración de corrida doble.** Se corrió el script, se vieron los resultados, se
encontró el defecto en revisión, se corrigió y se volvió a correr. Eso es la
secuencia que puede sesgar un resultado, así que queda escrita y **las dos tablas de
números están arriba**: el lector puede verificar que el cambio es uniforme en los
doce métodos y no una selección. La semilla (`20261002`) y todos los demás
parámetros son los mismos; el único cambio de código es la línea de estratificación.

---

## Tabla de decisiones

| Punto | Pregunta | Resultado | Decisión |
|---|---|---|---|
| **0** | ¿Las 446 series reconstruyen la `b` publicada? | **446 / 446** con \|Δb\| ≤ 1×10⁻⁴ | **CORRECTO**, se procede |
| **P1** | ¿Algún método alcanza el 5% nominal de falso positivo? | **`ar1_inf`: 7.1%**, dentro de `[2.5%, 7.5%]`. El resto va de 11.3% a 59.5% | **UNO ES ADMISIBLE** |
| **P2** | ¿El método admisible lo es por ser ciego? | `ar1_inf` tiene **84.1%** de poder a b = −0.30 y **95.6%** a b = −0.60 | **NO.** Es el menos potente de doce, pero no es ciego |
| **P3** | ¿Cuántos de los 156 estimables son significativos? | **33 (21.2%)** por `ar1_inf`. Los doce métodos dan de 33 a 134 | **SE DECLARA 33**, con las reservas de §6.1 |

**Veredicto:** el valor puntual del Dominio B es **33 de 156 estimables (21.2%)**, lo
que sobre los 446 casos del dominio son **33 de 446 (7.4%)** — contra los **374 de
446 (83.9%)** del corpus publicado sin corregir. El procedimiento que produjo ese 374
rechaza la nula el **59.5%** de las veces cuando no hay nada que rechazar.

---

## 1. P1 — La calibración, que es el punto de todo el diseño

2,000 casos sintéticos con la terna `(n, ρ, σ)` de un caso real del Dominio B elegido
al azar y **`b` verdadera = 0**: cualquier rechazo es un falso positivo por
construcción. De los 2,000, **733 provienen de un caso real estimable** (`n_eff ≥ 3`),
que es el estrato donde vive la pregunta.

El intervalo de Wilson al 95% se reporta porque con 733 casos la precisión Monte
Carlo **no es despreciable frente al ancho de la banda de admisión**, y eso es parte
de la lectura, no una nota al pie.

| Método | Tasa de falso positivo (estimables) | IC 95% (Wilson) | Pre-registrado | ¿Admisible? |
|---|---:|---:|---|---|
| `ols` — el del corpus publicado | **59.5%** | [55.9%, 63.0%] | sí | no |
| `ar1_inf` — cota inferior AR(1) (SE inflado + gl) | **7.1%** | **[5.5%, 9.2%]** | sí | **SÍ** |
| `ar1_sup` — cota superior AR(1) (solo gl) | 48.6% | [45.0%, 52.2%] | sí | no |
| `nw_auto` — Newey-West, rezago automático | 40.8% | [37.3%, 44.4%] | sí | no |
| `nw_n4` — Newey-West, rezago `n/4` | 38.1% | [34.6%, 41.6%] | sí | no |
| `gls_pw` — **Prais-Winsten GLS** iterado | **11.3%** | [9.2%, 13.8%] | sí | no |
| `boot_rb3` — bloques móviles `n^(1/3)`, residuos restringidos | 30.3% | [27.1%, 33.7%] | sí | no |
| `boot_rb8` — bloques `√n`, restringidos | 17.1% | [14.5%, 19.9%] | sí | no |
| `boot_rb17` — bloques `n/4`, restringidos | **15.6%** | [13.1%, 18.4%] | sí | no |
| `boot_ub3` — bloques `n^(1/3)`, no restringidos | 34.8% | [31.4%, 38.3%] | añadido | no |
| `boot_ub8` — bloques `√n`, no restringidos | 27.3% | [24.2%, 30.6%] | añadido | no |
| `boot_ub17` — bloques `n/4`, no restringidos | 27.6% | [24.4%, 30.9%] | añadido | no |

La regla de admisión, fijada en el pre-registro, es **[2.5%, 7.5%]** sobre la tasa
medida. `ar1_inf` mide **7.1%** y entra. El segundo mejor, `gls_pw`, mide 11.3% y
queda a **3.8 puntos** del techo. Los dos métodos que uno elegiría por autoridad
—GLS para AR(1), bootstrap por bloques para dependencia serial— quedan en 11.3% y
15.6%: **mejores que el resto, insuficientes igual.**

> Con los residuos del Dominio B, un contraste al 5% nominal rechaza en realidad
> entre el 11% y el 60% de las veces cuando no hay ningún efecto — con una única
> excepción medida. No hay forma de leer un p de este dominio como un p **salvo por
> esa excepción.**

### El número que más duele: 59.5%

`ols` es el procedimiento con el que se construyó el corpus publicado. Su tasa de
falso positivo medida es **59.5%**: rechaza la nula **tres veces de cada cinco cuando
no hay nada que rechazar.** Eso pone una cifra a la "doble inflación" que la auditoría
v32 describió en palabras, y explica el 374 de 446 "significativos" del corpus sin
necesidad de suponer nada.

---

## 2. P2 — El método admisible no lo es por ser ciego

Un método puede pasar la calibración por no rechazar casi nunca. **Hay que medirlo**,
y por eso el punto 2 estaba en el pre-registro.

| Método | Poder a b = −0.30 | Poder a b = −0.60 |
|---|---:|---:|
| `ols` | 98.4% | 100.0% |
| **`ar1_inf`** | **84.1%** | **95.6%** |
| `ar1_sup` | 96.1% | 99.4% |
| `nw_auto` | 97.7% | 100.0% |
| `nw_n4` | 97.3% | 100.0% |
| `gls_pw` | 97.4% | 100.0% |
| `boot_rb3` | 97.1% | 100.0% |
| `boot_rb8` | 96.3% | 100.0% |
| `boot_rb17` | 96.0% | 99.9% |
| `boot_ub3` / `boot_ub8` / `boot_ub17` | 97.4% / 96.3% / 96.6% | 100.0% / 100.0% / 100.0% |

`ar1_inf` es **el menos potente de los doce**, lo cual es exactamente lo que se espera
del único que está bien calibrado: los otros once compran poder gastando tamaño. Pero
**84.1% a b = −0.30 y 95.6% a b = −0.60 no es un método ciego**: detecta un efecto
moderado cinco veces de cada seis. La regla pre-registrada —"si varios son admisibles,
el valor puntual lo produce el de mayor poder"— no necesita desempate: hay uno solo.

---

## 3. P3 — El valor puntual

Los doce métodos sobre los 446 casos reales. **Estas doce filas son idénticas al
dígito en la primera corrida y en la corregida**, porque no dependen de la simulación:

| Método | sig / 156 estimables | sig / 446 | ¿En [33, 112]? | ¿Admisible? |
|---|---:|---:|---|---|
| `ols` | 134 | **374** | NO | no |
| **`ar1_inf`** | **33** | **33** | sí (en el borde) | **SÍ** |
| `ar1_sup` | 113 | 115 | NO | no |
| `nw_auto` | **120** | 326 | NO | no |
| `nw_n4` | 109 | 279 | sí | no |
| `gls_pw` | **57** | 111 | sí | no |
| `boot_rb3` | 109 | 302 | sí | no |
| `boot_ub3` | 114 | 314 | NO | no |
| `boot_rb8` | 88 | 248 | sí | no |
| `boot_ub8` | 104 | 283 | sí | no |
| `boot_rb17` | 72 | 187 | sí | no |
| `boot_ub17` | 99 | 274 | sí | no |

**El valor puntual es 33 de 156 (21.2%)**, por `ar1_inf`, el único método admisible.

**El rango de los doce es de 33 a 134 de 156**, es decir de 21% a 86%. Ese abanico,
sobre los mismos datos y la misma hipótesis, sigue siendo el argumento central del
diseño: la cifra puntual **sería un artefacto del método elegido** si el método se
eligiera por autoridad. Lo que la calibración hace es quitar la elección de las manos
de quien reporta y ponerla en una medición.

### La coincidencia con la cota, que no es confirmación

`ar1_inf` **es el mismo estimador** que produjo la cota inferior publicada: "SE
inflado + gl", `snt_auditoria_integral_v32.py:144`. Por lo tanto el chequeo
pre-registrado "¿cae dentro de `[33, 112]`?" **se satisface por construcción y en el
borde exacto**, no de forma independiente. Decirlo al revés —"el valor puntual cae
dentro de las cotas, lo que valida las cotas"— sería circular, y aquí no se dice.

Lo que sí se puede afirmar, y es distinto: **la cota inferior deja de ser una elección
por prudencia y pasa a ser la única de doce cuya tasa de error está medida y cerca de
la nominal.** La cota pasa de "cifra conservadora que decidimos citar" a "estimación
puntual con tamaño y poder medidos". No cambia el número; cambia su estatus.

---

## 4. Tres validaciones que salieron del propio diseño

No son adornos: son lo que permite creer el resto de la tabla.

1. **Las 446 series reconstruyen exacto.** `|b − b_publicada| ≤ 1×10⁻⁴` en los 446
   casos, desde `data/maddison_mpd2020.csv`. DW mediana 0.1120, ρ mediana 0.9440,
   `n_eff` mediana 2.20, estimables 156/446: las cuatro cifras de la auditoría v32,
   reproducidas.
2. **`nw_auto` devuelve 120 de 156**, exactamente la cifra que la auditoría registró
   el 2026-09-27 como INFO. La tubería nueva reproduce el número que motivó este
   pre-registro.
3. **`ar1_inf` devuelve 33 de 156**, exactamente la cota inferior publicada. Dos
   implementaciones independientes del mismo estimador coinciden al caso — lo cual
   valida **la implementación**, no la cota (§3).

### Y una cuarta, que salió de la corrección

4. **El estrato simulado reproduce la proporción real.** Con la estratificación
   corregida, 733 de 2,000 simulaciones (36.7%) provienen de casos estimables, contra
   156 de 446 (35.0%) en los datos. Esa concordancia es la prueba de que el muestreo
   de perfiles está bien, y su ausencia —86.9% contra 35.0%— era el síntoma que
   delató el defecto.

---

## 5. Dos correcciones a la lectura previa

### 5.1 Newey-West no "subcorrige con ρ ≈ 0.94". Está mal calibrado a estas n

La auditoría anotó que Newey-West subcorrige *por la ρ alta*. La validación del código
muestra que el diagnóstico es incompleto: con **ruido blanco puro** (ρ = 0, n = 69,
b = 0), `nw_auto` rechaza el **12.2%** y `nw_n4` el **25.2%**, contra un 5% nominal.
El estimador HAC sobre-rechaza **sin autocorrelación alguna**, por tamaño de muestra.
La ρ alta empeora el cuadro; no lo causa. Por eso el 120 no era un síntoma de ρ, era
un síntoma de n.

(Las cifras de ruido blanco vienen de la validación del código, no de los puntos
pre-registrados, y se reportan como tal. No dependen de la estratificación: con ρ = 0
todas las series son estimables.)

### 5.2 La cota superior es 112 o 113, según el redondeo. Caso `B042`

Recomputada desde las series crudas, la cota superior da **113** y no el 112
publicado. La diferencia es **un solo caso**, `B042` (Belgium→Spain), y su causa está
identificada al dígito:

| Fuente de `dw` | `dw` | gl = `n_eff` − 2 | p (solo gl) | Veredicto |
|---|---:|---:|---:|---|
| CSV publicado, redondeada a 3 decimales | 0.104 | 1.17659 | **0.050252** | no significativo |
| Serie cruda, sin redondear | 0.104437 | 1.19030 | **0.048964** | significativo |

Ni el 112 ni el 113 están mal: uno sale del resumen versionado tal como está
documentado, el otro de la serie cruda. Lo que muestra el caso es que **la cota
superior es frágil en el margen** —un caso se voltea por el tercer decimal de un
Durbin-Watson— y además su método mide **48.6%** de falso positivo. La cota inferior
no tiene este problema: da 33 por las dos vías.

---

## 6. Qué significa para la SNT

El pre-registro fija la lectura de cada desenlace. El que aplica es el **primero**:

> *"Hay método admisible y su cifra cae **dentro de [33, 112]** → el pendiente **se
> cierra**. El valor puntual se publica con su método, su tamaño medido y su poder
> medido, y las cotas quedan como lo que son: cotas."*

| Afirmación | Estado anterior | Estado ahora |
|---|---|---|
| Estimables / no estimables, 156 / 290 | Cerrado | **Sin cambio.** Sale de `n_eff < 3`, no depende de convenciones ni de métodos |
| Cota inferior 33 (21.2%) | Cerrada, elegida por prudencia | **Pasa a ser el valor puntual**: único método de doce con tasa de error medida en la banda nominal (7.1%), poder 84.1% / 95.6% |
| Cota superior 112 (71.8%) | Cerrada | **Frágil**: 112 o 113 según el redondeo de un `dw`; y su método mide 48.6% de falso positivo. Queda como cota, no como estimación |
| **Valor puntual** | Abierto | **CERRADO: 33 de 156 estimables (21.2%)**, con las tres reservas de §6.1 |
| Los 374/446 significativos del corpus | Sabidos inflados | **Cuantificado:** el procedimiento que los produjo rechaza el **59.5%** de las veces bajo la nula |
| El exponente `b` del Dominio B | Verificado | **Sin cambio.** Esta prueba no reestima ninguna `b` |
| Dirección de los hallazgos del dominio | Verificada en todas las variantes | **Sin cambio.** La dirección no depende de la significancia por caso |

**Lo que se cae es el 374, no la medición.** Las 446 `b` siguen siendo descripciones
válidas y reproducibles de sus pares de países. Lo que no se puede sostener es que 374
de ellas sean "significativas": con el único contraste de tamaño medido, son **33**.
El Dominio B conserva capacidad inferencial, pero **reducida en un factor de 11** con
respecto a lo publicado.

Es la misma clase de corrección que el 5.9×, el ROC-AUC filtrado, la precisión
tautológica del ASI y la lectura de apego preferencial del Módulo de N-cuerpos: **la
aritmética estaba bien, la inferencia no.** Cinco veces el mismo patrón.

### 6.1 Las tres reservas, escritas junto al número y no después

El valor puntual se declara porque la regla pre-registrada lo manda, y la regla se
aplica como está escrita —sobre la tasa medida— sin ajustarla después de ver el
resultado. Pero el número **no es robusto**, y las tres razones van aquí:

1. **La admisión es marginal.** 7.1% está dentro de `[2.5%, 7.5%]` por **0.4 puntos**.
   El intervalo de Wilson al 95% es **[5.5%, 9.2%]**, que **no está contenido en la
   banda**: su extremo superior la rebasa. Con otra semilla el método podría medir
   7.6% y quedar fuera. La regla pre-registrada no previó la precisión Monte Carlo, y
   no se la añade ahora para cambiar el desenlace; se reporta. **Para cerrar esta
   reserva habría que recalibrar con N ≫ 2,000** y el pre-registro no lo fijó.
2. **El chequeo de cotas es tautológico para este método.** El 33 coincide con la
   cota inferior porque `ar1_inf` **es** el estimador de la cota inferior (§3). El
   desenlace pre-registrado se satisface en el borde exacto y por construcción, no por
   evidencia independiente.
3. **Es el método menos potente de los doce.** 84.1% de poder a b = −0.30 significa
   que **uno de cada seis efectos moderados reales se le escapa**. El 33 es por tanto
   una estimación **conservadora** del número de casos con tendencia real, no una
   estimación central. La lectura correcta es "al menos 33 de 156", no "exactamente
   33 de 156".

### 6.2 Alcance

Honestidad sobre lo que esto no dice. El cierre aplica a **esta especificación**
—OLS de `log R` contra `log t` con residuos casi de raíz unitaria a n ≈ 69— y a
**estos doce métodos**. Lo que queda por hacer, en orden de viabilidad:

1. **Recalibrar `ar1_inf` con más réplicas** para cerrar la reserva 1. Es lo más
   barato y lo único que puede volver firme o tumbar el 33.
2. **Cambiar la especificación**, no el contraste: trabajar en diferencias o con un
   modelo que no suponga residuos estacionarios alrededor de una tendencia
   logarítmica. Es el camino que la literatura de raíz unitaria señalaría, y el único
   que podría dar una estimación central en vez de una cota.
3. **Más observaciones por caso**, que con series anuales 1900–2018 no existen.
4. **Un contraste con tamaño verificado** a ρ ≈ 0.95 y n ≈ 69 y más poder que 84%. Si
   aparece, la prueba de calibración de este informe es el banco donde debe pasar
   antes de usarse.

### 6.3 La regla por dominio

Este resultado es del **Dominio B** bajo su propio proxy declarado
(`R = PIBpc_hub / PIBpc_nodo`), y nada de él se traslada a otro dominio. Ni el 21.2%,
ni la admisibilidad de `ar1_inf`, ni la inadmisibilidad de los otros once: las tres
cosas se midieron sobre la terna `(n, ρ, σ)` **de este dominio**. Otro dominio con
otra ρ y otra n necesita su propia calibración, por Axioma 0.1
([`../../papers/marco_teorico.md:110`](../../papers/marco_teorico.md)). Lo que **sí**
es transferible es el procedimiento, no el número.

---

## Desviaciones respecto al pre-registro

Tres, las tres declaradas:

1. **Tres métodos de bootstrap añadidos.** El pre-registro fijaba el remuestreo sobre
   los residuos del ajuste **restringido** (`b = 0`). Al implementarlo quedó claro que
   la variante **no restringida** no arrastra la señal al ruido y por tanto no pierde
   poder cuando `b ≠ 0`. En vez de cambiar lo pre-registrado en silencio se
   implementaron **las dos**, y las tres añadidas van marcadas como `añadido` en el
   log, en la columna `preregistrado` del CSV y en las tablas de este informe. No
   altera ninguna conclusión: las seis variantes quedan lejos de la banda de admisión.
2. **Réplicas de bootstrap: 199 en la simulación, 999 sobre los datos reales.** Estaba
   fijado así en el pre-registro y se cumple; se repite aquí porque es la clase de
   parámetro que conviene tener a la vista. Con tasas observadas de 15.6% a 34.8%, muy
   lejos del techo del 7.5%, la precisión del bootstrap corto sobra para **esa**
   decisión. No sobra para la de `ar1_inf`, que no usa bootstrap.
3. **Corrida doble por corrección de un defecto.** Declarada arriba con las dos tablas
   de números. El pre-registro no contempla recorrer el script después de ver
   resultados; se hizo porque la revisión encontró un defecto que invalidaba la
   calibración, y la alternativa —publicar un "indecidible" que se sabe producto de un
   error— no es una opción. El cambio de código es una línea de estratificación, la
   semilla es la misma, y el efecto es uniforme en los doce métodos.

Lo que **no** se desvió: la regla de admisión [2.5%, 7.5%], los dos puntos de poder,
la semilla `20261002`, y la obligación de declarar el valor puntual cuando hay método
admisible dentro de las cotas — que es la regla que gobierna el resultado y se
respetó, con sus reservas escritas, aunque la admisión quedara a 0.4 puntos del borde.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02, corregido 2026-10-03*
