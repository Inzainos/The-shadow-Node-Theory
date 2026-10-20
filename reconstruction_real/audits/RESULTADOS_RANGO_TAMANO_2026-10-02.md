# Resultados — réplica internacional del ajuste rango-tamaño de N-cuerpos

**Pre-registro:** [`../preregistro/PREREGISTRO_RANGO_TAMANO_2026-10-02.md`](../preregistro/PREREGISTRO_RANGO_TAMANO_2026-10-02.md)
(commit `5b97328`, subido **antes** de descargar un solo dato de Brasil o de la UE).
**Scripts:** `code/rango_tamano_internacional.py` (primaria),
`code/rango_tamano_percapita.py` (secundaria per cápita),
`code/rango_tamano_diagnostico.py` (diagnóstico **post hoc**, no pre-registrado).
**Salidas:** `data/rango_tamano_internacional.csv`, `data/rango_tamano_poder.csv`,
`data/rango_tamano_percapita.csv`, `data/rango_tamano_diagnostico.csv`. Los tres
con log.

Pregunta que motivó la réplica: el 2026-10-02 se retiró la lectura de apego
preferencial del Módulo de N-cuerpos porque la lognormal le gana a la ley de
potencia en la curva rango-tamaño de las 32 entidades mexicanas (ΔAIC = 65.04).
Con n = 32 y 0.81 órdenes de magnitud de rango, **México no podía decir si eso
era un hecho general o una peculiaridad suya**. Seis niveles territoriales de
Brasil y la Unión Europea, de 27 a 5,570 unidades, sí pueden.

---

## Tabla de decisiones

| Punto | Hipótesis pre-registrada | Resultado | Decisión |
|---|---|---|---|
| **P1** | **H1.** La lognormal gana en todos los niveles | Gana en **5 de 6**; pierde en los 5,570 municipios de Brasil (ΔAIC = −914.6) | **H1 NO se cumple** |
| **P2** | **H2.** La tasa de falso "sobrevive" decrece conforme n crece | 96.8% → 42.6% de n = 27 a n = 5,570, monótona salvo el primer par | **H2 se cumple** |
| **P2** | Umbral de interpretabilidad: tasa < 20% | **Ningún nivel lo alcanza.** El mejor, con 5,570 unidades, se queda en 42.6% | **P3 no es interpretable en ningún nivel** |
| **P3** | **H3.** Donde haya poder, la potencia se descarta | No hay ningún nivel con poder suficiente | **No evaluable.** No se corrió, por regla pre-registrada |
| **Secundaria** | Repetir con per cápita para medir cuánto depende de la cantidad | La lognormal gana en **4 de 4** niveles per cápita | El veredicto **sí depende de la cantidad** |
| Control | México con `pib_pc` debe reproducir el ΔAIC publicado | **ΔAIC = 65.04**, b = −0.4732, R² 0.8705 / 0.8377 | **Reproduce exacto** |

---

## 1. P1 — La curva rango-tamaño: cinco niveles a la lognormal, uno a la potencia

Año 2021 en todas las fuentes. Cantidad: **PIB total** (México por su columna
`pct_pib`, proporcional al PIB total). "Órdenes" es el rango dinámico
log₁₀(máx/mín), que es la magnitud que Clauset, Shalizi y Newman (2009) señalan
como decisiva. σ es la desviación estándar de los logaritmos.

| Nivel | n | órdenes | σ | b | R² log pot. | R² log logn. | R² crudo pot. | R² crudo logn. | ΔAIC | Veredicto |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Brasil, estados | 27 | 2.17 | 1.227 | −1.3735 | 0.8874 | 0.9833 | 0.5972 | 0.9376 | **+51.5** | LOGNORMAL (fuerte) |
| México, entidades | 32 | 1.47 | 0.824 | −0.9240 | 0.9219 | 0.9782 | 0.7428 | 0.9633 | **+40.9** | LOGNORMAL (fuerte) |
| UE, NUTS1 | 111 | 2.75 | 1.185 | −1.0933 | 0.7411 | 0.9759 | −6.34 | 0.5092 | **+263.5** | LOGNORMAL (fuerte) |
| UE, NUTS2 | 293 | 3.58 | 1.134 | −1.0244 | 0.7605 | 0.9852 | −9.03 | 0.8926 | **+815.0** | LOGNORMAL (fuerte) |
| UE, NUTS3 | 1,327 | 3.11 | 1.122 | −1.0466 | 0.8494 | 0.9962 | −30.58 | 0.9236 | **+4,868.5** | LOGNORMAL (fuerte) |
| **Brasil, municipios** | **5,570** | **4.66** | **1.421** | −1.3940 | **0.9545** | 0.9464 | −177.58 | 0.2183 | **−914.6** | **POTENCIA (fuerte)** |

Convención de signo: ΔAIC > 0 favorece a la lognormal, ΔAIC < 0 a la potencia.
El umbral habitual de "evidencia fuerte" es 10; los seis niveles lo superan, en
un sentido o en el otro.

**H1 no se cumple y se reporta sin maquillaje.** Yo escribí en el pre-registro
"la lognormal gana en todos los niveles" y la predicción falla en el nivel más
grande del diseño.

Dos matices que van aquí y no en una nota al pie:

1. **En Brasil municipios la potencia gana por poco en escala logarítmica**
   (R² 0.9545 contra 0.9464). Lo que vuelve aplastante el ΔAIC es n = 5,570, que
   amplifica una diferencia pequeña de suma de residuos. En **escala cruda** la
   lognormal le sigue ganando con holgura (0.2183 contra −177.58).
2. **Los R² crudos negativos de la UE no son un error.** La curva lognormal es
   una curva de cuantiles con μ y σ de máxima verosimilitud, no un ajuste por
   mínimos cuadrados en escala cruda; cuando los primeros rangos valen cientos
   de miles de millones, cualquier desajuste en la cabeza domina la suma. El
   estadístico de decisión pre-registrado es el ΔAIC sobre los residuos
   logarítmicos, y se reportan las dos escalas por separado precisamente porque
   mezclarlas fue uno de los defectos que la auditoría v32 documentó.

---

## 2. P2 — El resultado más fuerte de toda la réplica: la prueba de Clauset nunca llega a tener poder

Por nivel, se simulan **500 muestras lognormales** del mismo n con los
parámetros estimados de los datos reales de ese nivel, y a cada una se le corre
el procedimiento completo de Clauset (MLE con `x_min` por KS, bondad de ajuste
por bootstrap paramétrico de 100 réplicas). La tasa de falso "sobrevive" es la
fracción de esas muestras —que por construcción **no** son leyes de potencia— en
las que la ley de potencia resulta "no descartable".

| Nivel | n | Falso "sobrevive" | ¿Poder suficiente (< 20%)? |
|---|---:|---:|---|
| Brasil, estados | 27 | 96.8% | insuficiente |
| México, entidades | 32 | 97.0% | insuficiente |
| UE, NUTS1 | 111 | 88.4% | insuficiente |
| UE, NUTS2 | 293 | 77.8% | insuficiente |
| UE, NUTS3 | 1,327 | 64.0% | insuficiente |
| Brasil, municipios | 5,570 | **42.6%** | **insuficiente** |

**H2 se cumple:** la tasa decrece con n, de 96.8% a 42.6%. Pero decrece
despacio, y el nivel más grande que existe con datos subnacionales abiertos
—los 5,570 municipios de Brasil, que son **todos** los municipios del país— se
queda al doble del umbral.

> Con 5,570 unidades, la prueba de bondad de ajuste de Clauset todavía deja
> pasar la ley de potencia en **4 de cada 10 muestras que son lognormales por
> construcción**. No hay ningún nivel territorial, en ningún país de este
> diseño, donde un "no se descarta la ley de potencia" signifique algo.

Esto es **más fuerte que lo previsto, y en otra dirección**: el problema nunca
fue que a México le faltaran datos. El problema es que **la prueba de
distribución de Clauset apenas distingue estas dos distribuciones a cualquier
tamaño realista de este tipo de datos.** El 96.4% de falsos que se midió con
n = 32 no era una limitación mexicana; era la curva de poder del método, que a
n = 5,570 sigue en 42.6%.

Consecuencia operativa, y es la regla que yo mismo fijé antes de ver nada: **P3
no se corre.** No se calculó ningún α, ningún `x_min`, ninguna bondad de ajuste
ni ningún Vuong sobre datos reales en esta réplica, porque el pre-registro dice
que solo se interpretan los niveles con tasa < 20% y no hay ninguno. Un resultado
que no se puede interpretar no se publica como si se pudiera.

---

## 3. La secundaria per cápita, y el control que valida toda la tubería

La sección 1 del pre-registro compromete repetir el análisis con cantidades per
cápita donde existan, *"para medir cuánto del veredicto depende de la cantidad
elegida"*. Brasil queda fuera porque la tabla 5938 del IBGE no publica per
cápita, como ya estaba anotado. Quedan los tres niveles NUTS con `EUR_HAB` y
México con `pib_pc`.

| Nivel | n | órdenes | σ | b | ΔAIC per cápita | ΔAIC PIB total | Veredicto |
|---|---:|---:|---:|---:|---:|---:|---|
| México, entidades | 32 | 0.81 | 0.434 | −0.4732 | **+65.0** | +40.9 | LOGNORMAL (fuerte) |
| UE, NUTS1 | 110 | 1.47 | 0.734 | −0.6689 | **+235.0** | +263.5 | LOGNORMAL (fuerte) |
| UE, NUTS2 | 285 | 1.61 | 0.723 | −0.6205 | **+600.7** | +815.0 | LOGNORMAL (fuerte) |
| UE, NUTS3 | 1,300 | 1.82 | 0.721 | −0.5967 | **+2,548.7** | +4,868.5 | LOGNORMAL (fuerte) |

Tres cosas se leen aquí:

1. **Per cápita la lognormal gana 4 de 4, sin excepción.** La cantidad elegida
   importa: el per cápita recorta el rango dinámico a la mitad o menos (de 2.75
   a 1.47 en NUTS1, de 3.11 a 1.82 en NUTS3) y con él desaparece cualquier
   asomo de ley de potencia.
2. **El poder per cápita es igual de malo o peor:** 93.8% de falsos en México,
   89.4% en NUTS1, 79.2% en NUTS2, 60.8% en NUTS3. Ningún nivel alcanza el
   umbral, así que P3 tampoco se interpreta aquí.
3. **El control de consistencia pasa exacto.** México con `pib_pc` es
   literalmente la serie que ajusta `nbody_lognormal_clauset.py`, y la tubería
   nueva devuelve **b = −0.4732, ΔAIC = 65.04, R² log 0.8705, R² crudo 0.8377**:
   las cifras publicadas en
   [`RESULTADOS_LOGNORMAL_2026-10-02.md`](RESULTADOS_LOGNORMAL_2026-10-02.md),
   dígito por dígito. Dos implementaciones independientes sobre la misma serie
   coinciden; el código de la réplica no tiene un sesgo que explique nada de lo
   anterior.

---

## 4. Diagnóstico exploratorio: ¿es n o es el rango dinámico?

> **No está pre-registrado.** Se escribió **después** de ver los resultados de
> P1 y se reporta como análisis post hoc, nunca como confirmación. Existe porque
> el pre-registro dejaba una lectura ambigua y los datos sí permiten cerrarla.

El pre-registro fija, por anticipado, qué significaría el desenlace observado:
*"La lognormal gana con n chico y la potencia con n grande → el hallazgo de
México sería un **artefacto de n**, y habría que revisar la retirada del
2026-10-02"*. El problema es que el único nivel que se voltea, Brasil
municipios, es **a la vez** el de mayor n (5,570) y el de mayor rango dinámico
(4.66 órdenes): los dos factores están confundidos.

Que n solo no explica nada ya se ve en la tabla de P1: UE NUTS3 tiene n = 1,327
y da **el mayor margen a favor de la lognormal de toda la réplica** (+4,868),
mayor que NUTS2 con n = 293 (+815). Si el veredicto siguiera a n, el margen
tendría que moverse hacia la potencia conforme n crece, y se mueve al contrario.

Para separarlos se trabaja **dentro de Brasil municipios**, moviendo un factor a
la vez, con 200 réplicas por celda (`rango_tamano_diagnostico.py`):

### A. n variable, rango libre (submuestra aleatoria simple)

Al bajar n el rango se encoge solo, porque los extremos se pierden. Es la línea
base donde ambos factores se mueven juntos.

| n | órdenes (mediana) | ΔAIC mediano | intervalo 5–95% | gana la potencia |
|---:|---:|---:|---|---:|
| 27 | 2.46 | −7.7 | −49.8 a +39.5 | 56% |
| 111 | 3.08 | −45.3 | −177.1 a +130.9 | 74% |
| 293 | 3.41 | −75.5 | −342.1 a +171.2 | 70% |
| 1,327 | 4.12 | −256.0 | −773.5 a +254.8 | 80% |
| 2,785 | 4.58 | −546.8 | −1,136.3 a +159.2 | 91% |

### B. n variable, rango **fijo** en 4.66 órdenes (forzando máximo y mínimo global)

Lo único que cambia es n.

| n | órdenes | ΔAIC mediano | intervalo 5–95% | gana la potencia |
|---:|---:|---:|---|---:|
| 27 | 4.66 | −22.7 | −41.6 a −9.9 | **99%** |
| 111 | 4.66 | −107.9 | −196.5 a −27.3 | **99%** |
| 293 | 4.66 | −219.8 | −455.7 a −59.4 | **97%** |
| 1,327 | 4.66 | −430.1 | −948.9 a +15.1 | **93%** |
| 2,785 | 4.66 | −642.8 | −1,231.2 a −70.2 | **97%** |

**Con el rango completo de Brasil, la ley de potencia gana en 93–99% de las
réplicas a todos los tamaños, incluido n = 27.** Veintisiete municipios
brasileños que cubran los 4.66 órdenes favorecen a la potencia tan claramente
como los 5,570.

### C. n **fijo** en 1,327 (el de UE NUTS3), tres rangos distintos

| Regla de selección | órdenes | ΔAIC | Veredicto |
|---|---:|---:|---|
| Los 1,327 municipios más grandes | 3.05 | **−2,919.4** | POTENCIA (fuerte) |
| Bloque contiguo del medio | 0.33 | **+2,239.4** | LOGNORMAL (fuerte) |
| Rango máximo (forzando extremos) | 4.66 | **−320.8** | POTENCIA (fuerte) |

### Lo que el diagnóstico establece

**El veredicto no lo decide n.** El experimento B lo muestra con 200 réplicas
por celda: con el rango clavado, el tamaño de muestra no voltea nada entre 27 y
2,785. **La lectura pre-registrada del "artefacto de n" queda descartada, y con
ella desaparece el motivo para revisar la retirada del 2026-10-02.**

El rango dinámico sí mueve el resultado, pero —y esto es importante— **no es
suficiente para explicarlo.** El bloque contiguo del medio, con 0.33 órdenes,
es casi degenerado y su resultado no dice gran cosa; el caso informativo es el
siguiente.

---

## 5. La comparación que descarta las dos explicaciones fáciles

Los 1,327 municipios más grandes de Brasil contra las 1,327 regiones NUTS3 de la
UE. Mismo n, por construcción:

| | n | órdenes | σ | b | R² log pot. | R² log logn. | ΔAIC |
|---|---:|---:|---:|---:|---:|---:|---:|
| Brasil, 1,327 municipios mayores | 1,327 | 3.05 | 1.052 | −1.0574 | **0.9859** | 0.8730 | **−2,919.4** |
| UE, NUTS3 | 1,327 | 3.11 | 1.122 | −1.0466 | 0.8494 | **0.9962** | **+4,868.5** |

Mismo tamaño de muestra. Rango dinámico prácticamente igual (3.05 contra 3.11).
σ prácticamente igual (1.05 contra 1.12). **Exponente prácticamente igual**
(−1.057 contra −1.047, los dos a un paso del −1 de Zipf). Y **veredictos
opuestos, los dos aplastantes.**

Ni n, ni rango dinámico, ni dispersión logarítmica, ni el exponente explican la
diferencia. Lo que difiere es la **curvatura de la curva rango-tamaño**: los
municipios grandes de Brasil son casi perfectamente zipfianos (R² log = 0.9859
sobre una recta), y las regiones NUTS3 europeas no lo son (0.8494 contra 0.9962
de la lognormal).

**Es una diferencia de forma, real, entre los dos sistemas, y no tengo
identificada su causa.** Lo que sí puedo reportar es la hipótesis que probé y no
pude confirmar: que las unidades NUTS son una **partición administrativa
construida por bandas de población** —el Reglamento (CE) 1059/2003 fija
150,000–800,000 habitantes para NUTS3— mientras que los municipios brasileños
son unidades históricas sin esa restricción. La población derivada por región
(cociente `MIO_EUR`/`EUR_HAB` de las dos descargas de Eurostat) es consistente
con la banda: p25 = 139,921 y p75 = 483,999 habitantes en NUTS3. Pero la
hipótesis **no se sostiene con los estadísticos que estos datos permiten
calcular**: el factor intercuartílico del PIB es comparable en todos los niveles
(4.1 en NUTS3, 6.0 en Brasil municipios, 3.8 en los 1,327 mayores de Brasil), así
que la "compresión" administrativa no aparece donde tendría que aparecer. Queda
como pregunta abierta con un siguiente paso concreto: comparar poblaciones
municipales brasileñas contra poblaciones NUTS3, que exige una descarga que no
está en este diseño.

---

## 6. Qué significa para la SNT

El pre-registro fija, antes de ver nada, la lectura de cada desenlace. El que
aplica es el tercero:

> *"Resultados mezclados entre países → la forma **depende del contexto
> institucional**, que sería un hallazgo propio y obligaría a matizar la
> afirmación de invariancia."*

| Afirmación | Estado anterior | Estado ahora |
|---|---|---|
| La lognormal le gana a la potencia en la jerarquía económica subnacional | Verificado solo en México (n = 32) | **Verificado en 5 de 6 niveles y en 4 de 4 per cápita**, con márgenes de +41 a +4,868 |
| El hallazgo de México es un artefacto de n | Posibilidad abierta por el pre-registro | **Descartado.** Con el rango fijo, n no voltea el veredicto entre 27 y 2,785 (99% → 97%) |
| La forma de la distribución es invariante de escala | Afirmación del Módulo de N-cuerpos | **Hay que matizarla.** Mismo n, mismo rango, mismo σ, mismo b, y veredictos opuestos entre Brasil y la UE |
| Un "no se descarta la potencia" por Clauset significa algo | Se sabía débil con n = 32 | **No significa nada a ningún n de este diseño.** 42.6% de falsos con 5,570 unidades |
| Retirada de la lectura de apego preferencial (2026-10-02) | En pie | **En pie y reforzada** — ver abajo |
| Gradiente compuesto de Tlaxcala, 9.3× | Verificado | **Sin cambio.** No depende de esto |

**Por qué la retirada se refuerza en lugar de debilitarse.** El Módulo de
N-cuerpos usaba la forma de la distribución como evidencia de apego
preferencial. Esta réplica muestra que **la forma depende de cómo se parte el
territorio**: los mismos 5,570 municipios dan "potencia" completos o por su
cola alta, y "lognormal" si se toma un bloque estrecho del medio; y dos
sistemas con n, rango, σ y b casi idénticos dan veredictos opuestos. Si la forma
depende de la partición, **la forma no puede ser evidencia de un mecanismo
generador.** Eso vale igual en el sentido contrario: que los municipios
brasileños salgan zipfianos **tampoco** es evidencia de apego preferencial en
Brasil, porque un Zipf es compatible con varios mecanismos de crecimiento
multiplicativo con barrera inferior —Gabaix (1999)— y la prueba que podría
separarlos es justo la que aquí no tiene poder.

**Lo que esta réplica NO toca,** y conviene repetirlo porque está escrito en el
pre-registro: no mide satelización, no prueba el eje **b** de la SNT, y no toca
la capa ACO-A. Mide la **forma de la distribución de tamaños económicos
subnacionales**, que es lo que el Módulo de N-cuerpos usaba como evidencia. El
exponente de satelización y el gradiente compuesto de Tlaxcala siguen intactos
y siguen siendo el resultado más sólido del módulo.

---

## Desviaciones respecto al pre-registro

Cuatro, todas declaradas:

1. **Códigos extra-regio de Eurostat, excluidos.** El pre-registro fijaba las
   exclusiones como "los códigos agregados que no son del nivel analizado
   (`EU27_2020`, códigos de país de 2 letras, y los niveles superiores)". No
   previó que Eurostat publica, por país y por nivel, un código residual
   etiquetado **"Extra-Regio"** (`BEZ`/`BEZZ`/`BEZZZ`, `FRZ`/`FRZZ`/`FRZZZ`, …)
   con la actividad económica que no puede asignarse a ninguna región:
   embajadas, plataformas marinas, buques. Son **16 por nivel**, tienen la
   longitud de código correcta y por eso pasaban el filtro. **No son unidades
   territoriales y no eran inocuos:** ocupaban toda la cola baja de los tres
   niveles de la UE, desde 22.62 MIO_EUR, e inflaban el rango dinámico europeo a
   4.5 órdenes de magnitud — exactamente la cantidad que el método de Clauset
   considera decisiva. Se excluyen (`es_region()`, commit `4abd8f4`). Conteos
   finales: 111 NUTS1 (contra 127 del pre-registro), 293 NUTS2 (contra 309) y
   1,327 NUTS3 (contra 1,343); la diferencia son los 16 extra-regio menos el
   `HUZ`, que ya caía por valor cero.
2. **Tope de 200 candidatos a `x_min`.** El pre-registro de México decía "todos
   los valores candidatos de la muestra". El barrido exhaustivo es O(n²) y el
   diseño lo invoca ~50,000 veces por nivel: 1.5 billones de operaciones a
   n = 5,570, es decir una corrida que no termina. Por encima de 200 valores
   distintos se recorre un subconjunto espaciado logarítmicamente, que es lo que
   hacen las implementaciones habituales del método; por debajo el barrido sigue
   siendo exhaustivo. **Verificado que México no cambia ni un dígito** (α = 4.702,
   `x_min` = 137.8, cola = 13, KS = 0.0769) y que el estimador sigue recuperando
   α = 2.508 de muestras con α = 2.5 (commit `22f2d24`).
3. **Réplicas del bootstrap de poder: 100, no 2,000.** Igual que en el informe
   de México, y por lo mismo: el procedimiento completo serían 3 millones de
   ajustes por nivel. Con tasas observadas de 42.6% a 97.0%, todas lejísimos del
   umbral del 20%, la precisión del bootstrap corto sobra para la decisión.
4. **Un script adicional no previsto en las salidas.** El pre-registro listaba
   un solo programa. La secundaria per cápita se implementó aparte
   (`rango_tamano_percapita.py`) para no tocar la tubería de la corrida
   principal, y el diagnóstico de n contra rango
   (`rango_tamano_diagnostico.py`) es **post hoc y así está etiquetado** en su
   encabezado, en su log y en la sección 4 de este informe.

## Corrida descartada

La corrida del 2026-10-02 a las 15:25 **se descarta completa** por el defecto 1.
Sus niveles europeos estaban contaminados con los 16 extra-regio por nivel. Se
detuvo antes de que escribiera ningún CSV; su log se conservó fuera del árbol
como evidencia y no quedó ningún artefacto versionado proveniente de ella. Las
cifras de poder de Brasil y México de esa corrida coincidían con las de la
corrida válida (96.8% y 97.0%), lo que confirma que la contaminación afectaba
solo a la UE.

## Incidente de registro, resuelto

`nbody_lognormal_clauset.py` llamaba a `logging.basicConfig` al importarse, así
que al reutilizarlo desde la réplica el módulo se adueñaba del logger raíz y el
log de la réplica sobrescribía `nbody_lognormal_log.txt`. Se corrigió moviendo
la configuración dentro de `main()` (commit `4aab3fc`), y después el mismo
patrón se aplicó a `rango_tamano_internacional.py` para que la secundaria pudiera
importarlo sin repetir la falla (commit `4abd8f4`). El log de México se
**regeneró** re-corriendo el script, y reproduce las cifras publicadas con
`nbody_lognormal_resultados.csv` idéntico bit por bit al versionado. El
incidente fue estrictamente local: `reconstruction_real/logs/` está en
`.gitignore` y nunca tocó un artefacto versionado.

## Validación del código

- **Dos implementaciones independientes, una serie:** México `pib_pc` da
  ΔAIC = 65.04 y b = −0.4732 tanto en `nbody_lognormal_clauset.py` como en la
  tubería nueva de `rango_tamano_percapita.py`.
- **Estimador contra distribuciones conocidas** (de la ronda anterior, mismo
  código): α = 2.508 y 2.970 recuperados de muestras con α = 2.5 y 3.0; Vuong
  favorece correctamente la lognormal (R = −16.62, p = 0.0002) en muestras
  lognormales con σ = 0.3.
- **Esquema de las fuentes verificado contra las etiquetas de Eurostat**, que es
  cómo se encontró el defecto de los extra-regio.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
