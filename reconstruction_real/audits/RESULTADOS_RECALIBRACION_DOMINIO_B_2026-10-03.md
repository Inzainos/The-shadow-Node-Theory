# Resultados — recalibración de alta precisión del valor puntual del Dominio B

**Adenda (subida antes de correr):** [`../preregistro/ADENDA_RECALIBRACION_DOMINIO_B_2026-10-03.md`](../preregistro/ADENDA_RECALIBRACION_DOMINIO_B_2026-10-03.md)
(commit `8952d59`, 14:34:56 UTC).
**Script:** `code/dominio_B_recalibracion.py` (commit `f160ed1`, con log).
**Corrida:** 14:36:16 → 14:47:04 UTC del 2026-10-03.
**Datos:** `data/maddison_mpd2020.csv`, ya versionado. **Sin descargas.**
**Salida:** `data/dominio_B_recalibracion.csv`.

---

## El resultado, en una línea

**`ar1_inf` mide 7.96% de falso positivo, no 7.1%. Queda fuera de la banda de admisión
`[2.5%, 7.5%]`, y con él ninguno de los doce métodos es admisible. El valor puntual del
Dominio B vuelve a NO declararse y se cierra como indecidible.**

Es el desenlace que la adenda declaró por anticipado como el que obliga a revertir, y se
publica igual que se habría publicado el que confirmaba el cierre.

| | Corrida pre-registrada | Recalibración | Veredicto |
|---|---:|---:|---|
| `N_SIM` (tamaño) | 2,000 | **200,000** | — |
| Estrato estimable | 733 | **69,827** | — |
| Tasa de `ar1_inf` | 7.1% | **7.962%** | — |
| IC95 de Wilson | [5.47%, 9.21%] | **[7.76%, 8.17%]** | — |
| Techo de la banda | 7.5% | 7.5% | **sin cambio** |
| ¿Admisible? | sí, por 0.4 puntos | **NO, por 0.46 puntos** | **revertido** |

El intervalo nuevo **no toca** la banda: su extremo inferior, 7.76%, ya está por encima
del techo de 7.5%. Con 69,827 casos en el estrato el semiancho es de 0.20 puntos, así
que esto no es una decisión al filo del ruido — es la respuesta.

---

## 1. Las doce tasas, con las dos mediciones lado a lado

Escenario de tamaño (`b` verdadera = 0, donde todo rechazo es un falso positivo por
construcción), tasa en el estrato estimable:

| Método | Tasa (200,000) | IC95 Wilson | Tasa (2,000) | ¿Admisible? |
|---|---:|---:|---:|---|
| `ar1_inf` — cota inferior AR(1) | **7.962%** | **[7.76%, 8.17%]** | 7.1% | **no** |
| `gls_pw` — Prais-Winsten GLS | 12.909% | [12.66%, 13.16%] | 11.3% | no |
| `boot_rb17` — bloques `n/4`, restringidos | 14.734% | [14.47%, 15.00%] | 15.6% | no |
| `boot_rb8` — bloques `√n`, restringidos | 17.714% | [17.43%, 18.00%] | 17.1% | no |
| `boot_ub8` — bloques `√n`, no restringidos | 26.422% | [26.10%, 26.75%] | 27.3% | no |
| `boot_ub17` — bloques `n/4`, no restringidos | 27.660% | [27.33%, 27.99%] | 27.6% | no |
| `boot_rb3` — bloques `n^(1/3)`, restringidos | 28.632% | [28.30%, 28.97%] | 30.3% | no |
| `boot_ub3` — bloques `n^(1/3)`, no restringidos | 33.513% | [33.16%, 33.86%] | 34.8% | no |
| `nw_n4` — Newey-West, rezago `n/4` | 37.637% | [37.28%, 38.00%] | 38.1% | no |
| `nw_auto` — Newey-West, rezago automático | 40.696% | [40.33%, 41.06%] | 40.8% | no |
| `ar1_sup` — cota superior AR(1) | 47.445% | [47.07%, 47.82%] | 48.6% | no |
| `ols` — **el del corpus publicado** | **57.999%** | [57.63%, 58.36%] | 59.5% | no |

**Ninguno cae en `[2.5%, 7.5%]`.** El más cercano, `ar1_inf`, se queda a **0.46 puntos**
por encima del techo. El segundo, `gls_pw`, a 5.4 puntos.

---

## 2. Las dos corridas no se contradicen. La primera era imprecisa, no errónea

Esto es lo que vuelve interpretable el cambio, y hay que decirlo con cuidado porque es
fácil leerlo mal. **Las doce estimaciones de 200,000 caen dentro del IC95 de la corrida
de 2,000:**

| Método | IC95 de la corrida de 2,000 | Punto de 200,000 | ¿Consistente? |
|---|---:|---:|---|
| `ols` | [55.91%, 63.00%] | 57.999% | sí |
| **`ar1_inf`** | **[5.47%, 9.19%]** | **7.962%** | **sí** |
| `ar1_sup` | [44.99%, 52.22%] | 47.445% | sí |
| `nw_auto` | [37.30%, 44.40%] | 40.696% | sí |
| `nw_n4` | [34.66%, 41.67%] | 37.637% | sí |
| `gls_pw` | [9.21%, 13.80%] | 12.909% | sí |
| `boot_rb3` | [27.08%, 33.72%] | 28.632% | sí |
| `boot_ub3` | [31.44%, 38.32%] | 33.513% | sí |
| `boot_rb8` | [14.55%, 20.00%] | 17.714% | sí |
| `boot_ub8` | [24.20%, 30.64%] | 26.422% | sí |
| `boot_rb17` | [13.15%, 18.41%] | 14.734% | sí |
| `boot_ub17` | [24.49%, 30.95%] | 27.660% | sí |

**Doce de doce.** Son dos mediciones independientes —semillas `20261002` y `20261003`—
de la misma cantidad, y concuerdan. **El 7.1% no era un error ni un defecto de código:
era el mismo número medido con 1/10 de la precisión, y cayó del lado bajo de su propio
intervalo.** Lo bastante bajo como para cruzar el techo de la banda por 0.4 puntos.

Y es exactamente lo que la reserva 1 del informe advertía, escrita antes de medir esto:

> *"Con otra semilla el método podría medir 7.6% y quedar fuera."*

Midió **7.96%**. La reserva no era una formalidad: era el riesgo real, cuantificado, y
se materializó.

### Por qué esto NO es un tercer error

Conviene separar tres cosas que ocurrieron en este bloque en dos días:

1. **La primera corrida concluyó "indecidible" por un defecto de código real** (la
   estratificación por la realización simulada). **Eso fue un error mío**, y la
   corrección fue obligada.
2. **La segunda corrida concluyó "33 de 156" aplicando la regla pre-registrada a la
   tasa medida de 7.1%.** Eso **no fue un error**: fue la regla aplicada correctamente
   a la mejor medición disponible, con su imprecisión declarada en el mismo documento
   como la reserva 1.
3. **Esta recalibración mide la misma cantidad con error diez veces menor y la regla da
   el resultado contrario.** Tampoco es un error: es la reserva cerrándose en la
   dirección desfavorable, que es una de las dos direcciones que podía tomar y estaba
   escrita como tal.

El defecto de procedimiento, si hay que nombrar uno, es del **pre-registro base**: fijó
`N_SIM = 2,000` para una decisión cuya banda tiene 5 puntos de ancho, cuando con 733
casos en el estrato el error Monte Carlo es de ±1.9. **La precisión de la simulación
debió dimensionarse contra el ancho de la banda, no elegirse por convención.** Queda
como regla de operación.

---

## 3. El poder, que reproduce y confirma que se mide lo mismo

| Método | Poder a b = −0.30 (200k/20k) | IC95 | Poder a b = −0.30 (2,000) | A b = −0.60 (20k) | (2,000) |
|---|---:|---:|---:|---:|---:|
| `ols` | 98.63% | [98.33%, 98.87%] | 98.4% | 99.99% | 100.0% |
| **`ar1_inf`** | **84.03%** | [83.15%, 84.87%] | 84.1% | **94.00%** | 95.6% |
| `ar1_sup` | 96.37% | [95.90%, 96.78%] | 96.1% | 98.61% | 99.4% |
| `nw_auto` | 97.80% | [97.43%, 98.12%] | 97.7% | 99.90% | 100.0% |
| `nw_n4` | 97.48% | [97.08%, 97.82%] | 97.3% | 99.86% | 100.0% |
| `gls_pw` | 97.77% | [97.40%, 98.09%] | 97.4% | 99.97% | 100.0% |
| `boot_rb3` | 97.32% | [96.92%, 97.67%] | 97.1% | 99.86% | 100.0% |
| `boot_ub3` | 97.49% | [97.10%, 97.83%] | 97.4% | 99.85% | 100.0% |
| `boot_rb8` | 96.37% | [95.91%, 96.78%] | 96.3% | 99.78% | 100.0% |
| `boot_ub8` | 96.94% | [96.51%, 97.32%] | 96.3% | 99.80% | 100.0% |
| `boot_rb17` | 95.62% | [95.12%, 96.07%] | 96.0% | 99.70% | 99.9% |
| `boot_ub17` | 96.80% | [96.36%, 97.18%] | 96.6% | 99.80% | 100.0% |

`ar1_inf` da **84.03%** contra el 84.1% de la corrida anterior: coinciden a la décima.
Eso es la prueba de que las dos corridas montan el mismo experimento y que la diferencia
del escenario de tamaño es precisión y nada más.

**El fallo sigue siendo de tamaño, no de conservadurismo.** Ningún método está
cambiando poder por tamaño: todos detectan un efecto real sin dificultad y todos
rechazan de más bajo la nula.

---

## 4. Dos validaciones del propio diseño

1. **El estrato simulado reproduce la proporción real con tres cifras.** 69,827 de
   200,000 = **34.91%**, contra 156 de 446 = **34.98%** en los datos. Con 200,000
   réplicas esa concordancia deja de ser indicativa y pasa a ser una verificación
   estricta de que el muestreo de perfiles y la estratificación por el caso de origen
   están bien. Es la misma comprobación cuya **ausencia** —86.9% contra 35.0%— delató el
   defecto del 2026-10-03.
2. **`ar1_inf` sigue devolviendo 33 de 156 sobre los datos reales.** Recomputado en esta
   corrida de forma determinista (ese estimador no usa el RNG): **33 de 156 (21.2%)**.
   La cifra de la cota inferior no se mueve; lo que se cae es el permiso de llamarla
   valor puntual.

---

## 5. Qué significa para la SNT

Aplica el desenlace que la adenda fijó para este caso:

> *"`ar1_inf` por encima de 7.5% → deja de ser admisible. Como ningún otro método está
> cerca —el segundo mejor midió 11.3%— el valor puntual **vuelve a NO declararse y se
> cierra como indecidible**, por la regla del pre-registro base. El 33 regresa a ser la
> cifra conservadora a citar, y el informe se reescribe otra vez, en esa dirección."*

| Afirmación | Estado del 2026-10-03 (mañana) | Estado ahora |
|---|---|---|
| Estimables / no estimables, 156 / 290 | Cerrado | **Sin cambio.** Sale de `n_eff < 3`, no depende de simulación |
| **Valor puntual** | 33 de 156 (21.2%), con tres reservas | **NO SE DECLARA. Cerrado como indecidible** |
| Cota inferior 33 (21.2%) | Pasaba a ser el valor puntual | **Vuelve a ser cota**: la cifra conservadora a citar, no una estimación |
| Cota superior 112 (71.8%) | Frágil, su método en 48.6% | **Frágil igual**, su método mide 47.4% con IC de 0.4 puntos |
| Los 374/446 del corpus | Inflados, OLS en 59.5% | **Cuantificado con precisión: 58.0%**, IC95 [57.6%, 58.4%] |
| El exponente `b` del Dominio B | Verificado | **Sin cambio.** Nada aquí reestima una `b` |
| Dirección de los hallazgos | Verificada | **Sin cambio.** No depende de la significancia por caso |

**Lo que se cae es la significancia por caso, no la medición.** Las 446 `b` siguen
siendo descripciones válidas y reproducibles de sus pares de países. Lo que no se puede
hacer con ellas es contar cuántas son "significativas": con ρ ≈ 0.94 y n ≈ 69, **ninguno
de los doce contrastes evaluados tiene un tamaño que lo permita**, y ahora eso está
medido con un error de dos décimas de punto en vez de dos puntos. El Dominio B queda
**descriptivo, no inferencial**.

### Alcance de "indecidible", otra vez

Aplica a **esta especificación** —OLS de `log R` contra `log t` con residuos casi de
raíz unitaria a n ≈ 69— y a **estos doce métodos**. No es una afirmación de que ningún
procedimiento podría funcionar. Lo que quedaría por hacer, ahora sin la vía barata:

1. **Cambiar la especificación**, no el contraste: diferencias, o un modelo que no
   suponga residuos estacionarios alrededor de una tendencia logarítmica. Era la opción
   2 de la lista anterior y ahora es la primera, porque la de recalibrar **ya se hizo y
   cerró la puerta**.
2. **Más observaciones por caso**, que con series anuales 1900–2018 no existen.
3. **Un contraste con tamaño verificado** a ρ ≈ 0.95 y n ≈ 69. Si aparece, el banco de
   pruebas es este, y ahora con 200,000 réplicas de referencia.

### La regla por dominio

Todo lo de arriba es del **Dominio B** bajo su proxy declarado
(`R = PIBpc_hub / PIBpc_nodo`). Ni el 7.96%, ni la inadmisibilidad de los doce, ni el
58.0% del OLS se trasladan a otro dominio: las tres cosas se midieron sobre la terna
`(n, ρ, σ)` **de este dominio**, por Axioma 0.1
([`../../papers/marco_teorico.md:110`](../../papers/marco_teorico.md)). Lo transferible
es el procedimiento: **dimensionar la precisión de la simulación contra el ancho de la
regla de decisión, antes de pre-registrarla.**

---

## Desviaciones respecto a la adenda

**Ninguna.** Se corrió lo que la adenda fijó: 200,000 en tamaño, 20,000 en los dos
puntos de poder, los doce métodos, semilla `20261003`, banda `[0.025, 0.075]` sin tocar,
`BOOT_SIM = 199`, estratificación por el caso real de origen, y los mismos datos
versionados sin descargas. El script original y sus salidas no se modificaron: esta
recalibración escribió sus propios archivos.

La función `wilson()` del script nuevo se verificó antes de correr contra la cifra ya
publicada: `wilson(52, 731)` devuelve `[0.0547, 0.0921]`, idéntico al IC95
`[5.5%, 9.2%]` del informe anterior. El intervalo con el que se juzga el resultado nuevo
es el mismo que produjo la reserva.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-03*
