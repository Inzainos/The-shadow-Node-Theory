# Resultados — comparación lognormal del ajuste rango-tamaño de N-cuerpos (México)

**Pre-registro:** [`../preregistro/PREREGISTRO_LOGNORMAL_2026-10-02.md`](../preregistro/PREREGISTRO_LOGNORMAL_2026-10-02.md)
(commit `9718808`). **Script:** `code/nbody_lognormal_clauset.py` (con log).
**Datos:** `data/matriz_mexico_32.csv`, 32 entidades, columna `pib_pc`. Sin descargas.
**Salida:** `data/nbody_lognormal_resultados.csv`.

Cierra el pendiente que el README arrastraba desde la auditoría v32.

## Tabla de decisiones

| Punto | Prueba | Resultado | Decisión |
|---|---|---|---|
| **1** | Bondad de ajuste de la ley de potencia (Clauset, bootstrap paramétrico) | p = 0.974 | No se descarta — **pero ver punto 3** |
| **1** | Vuong, potencia contra lognormal | R = −0.103, p = 0.746 | **Indistinguible** |
| **1** | Vuong, potencia contra exponencial | R = −0.122, p = 0.828 | **Indistinguible** |
| **2** | Curva rango-tamaño, potencia contra lognormal (AIC) | **ΔAIC = 65.04** | **Evidencia fuerte a favor de la LOGNORMAL** |
| **3** | Poder del diseño | **96.4%** de falsos "sobrevive" | **El punto 1 no tiene poder** |

---

## 1. La prueba de distribución no puede decidir, y sabemos exactamente por qué

El ajuste de máxima verosimilitud da α = 4.702 con x_min = 137.8, dejando **13 de 32
entidades** en la cola (41%). La bondad de ajuste da p = 0.974, que por la regla de
Clauset significa "no se descarta la ley de potencia".

**Ese p = 0.974 no vale nada, y el punto 3 lo demuestra con una cifra.**

Se simularon 1,000 muestras de n = 32 extraídas de una **lognormal** con los
parámetros de los datos reales —muestras que por construcción **no** son leyes de
potencia— y se les aplicó el mismo procedimiento. La ley de potencia resultó "no
descartable" en **964 de las 1,000**.

> Con una tasa de falso "sobrevive" del **96.4%**, el procedimiento del punto 1 no
> distingue nada a este tamaño de muestra. Un "no se descarta" aquí significa **falta
> de datos**, no respaldo.

Las dos pruebas de Vuong confirman lo mismo desde otro ángulo: ni contra la lognormal
(p = 0.75) ni contra la exponencial (p = 0.83) hay forma de separar los modelos.

Era lo anticipado en la sección 0.2 del pre-registro: **0.81 órdenes de magnitud** de
rango (factor 6.5, de 43.9 a 285.2) con n = 32, muy por debajo de lo que el método
necesita. Quedó escrito **antes** de correr nada, precisamente para que no se leyera
después como excusa.

---

## 2. En la curva rango-tamaño la lognormal gana, y por mucho

Esta es la prueba que importa, porque la curva rango-tamaño es **lo que la figura del
repositorio muestra y lo que el Módulo de N-cuerpos afirma**.

| Modelo | R² log | R² crudo | AIC |
|---|---:|---:|---:|
| Potencia (`b = −0.4732`) | 0.8705 | 0.8377 | −115.84 |
| **Lognormal** (μ = 4.7775, σ = 0.4340) | **0.9830** | **0.9755** | **−180.88** |

**ΔAIC = 65.04.** La convención habitual llama "evidencia fuerte" a cualquier
diferencia mayor que 10. Esta es seis veces ese umbral.

La lognormal no gana por poco ni por tener más parámetros —ambos modelos tienen dos—:
reduce el error de ajuste de forma masiva, pasando de R² = 0.838 a **0.976** en escala
cruda.

### De paso, una discrepancia del repositorio queda explicada

`mexico_nbody_real.csv` reporta R² = 0.8705 y el README R² = 0.8377. **Son la misma
cifra en dos escalas**: 0.8705 es el R² en escala logarítmica y 0.8377 en escala
cruda. Es exactamente el defecto de reporte que la auditoría v32 documentó para el
corpus (`r2_log` y `r2_raw` promediados juntos), aquí en el módulo de N-cuerpos.

---

## 3. Qué significa para la teoría

El README advertía, correctamente, que un ajuste rango-tamaño sobre 32 entidades
ordenadas da un R² alto *casi por construcción*, y que por eso no era evidencia de
apego preferencial hasta hacer esta comparación. **La comparación está hecha y el
resultado es negativo.**

| Afirmación | Estado anterior | Estado ahora |
|---|---|---|
| b = −0.473, R² = 0.838 replica | Verificado | **Sigue verificado** |
| La distribución sigue una ley de potencia | Pendiente de comparar | **Indecidible con n = 32** |
| Es consistente con **apego preferencial** | "Consistente, pendiente" | **No respaldado**: la lognormal ajusta mucho mejor |
| Gradiente compuesto de Tlaxcala 9.3× | Verificado | **Sin cambio** — no depende de esto |
| Leapfrogs de Querétaro y Nuevo León | Verificado | **Sin cambio** — son ajustes de trayectoria |

**Lo que se cae es la lectura, no la medición.** El exponente b = −0.473 sigue siendo
una descripción válida y reproducible de la jerarquía económica estatal mexicana. Lo
que ya no se puede decir es que esa jerarquía **evidencie apego preferencial**, porque
una lognormal —que es lo que produce un proceso multiplicativo corriente, sin ningún
mecanismo de "el rico se hace más rico"— describe los mismos datos bastante mejor.

Es la misma clase de corrección que el 5.9×, el ROC-AUC de 0.9994 y la precisión = 1.0
del ASI: **la aritmética estaba bien, la interpretación no.**

### Lo que sigue en pie del Módulo de N-cuerpos

El resultado central del módulo **no depende** de la forma de la distribución. El
gradiente compuesto de Tlaxcala —9.3× mayor que el binario, con 89.2% de la extracción
fluyendo hacia la CDMX— es una suma de pesos entre pares, no un ajuste de ley de
potencia. Sigue intacto, y sigue siendo el hallazgo más sólido y más útil del módulo.

---

## Desviaciones respecto al pre-registro

1. **Bootstrap del punto 3.** El pre-registro no fijaba cuántas réplicas usar dentro
   de cada una de las 1,000 simulaciones de poder. Se usan **100** (en lugar de las
   2,000 del punto 1), porque el procedimiento completo serían 2 millones de ajustes.
   Con una tasa observada del 96.4%, muy lejos de cualquier umbral de decisión, la
   precisión del bootstrap corto es más que suficiente.
2. **x_min, candidatos.** Se excluyen los dos valores más altos como candidatos a
   `x_min`, para dejar al menos 3 puntos en la cola. El pre-registro decía "todos los
   valores candidatos de la muestra" sin fijar ese mínimo.

## Validación del código

Antes de correr sobre los datos reales se verificó el estimador contra distribuciones
conocidas:

- Muestras de una ley de potencia con α = 2.5 y α = 3.0 (n = 5,000): el MLE recupera
  **2.508** y **2.970**.
- Muestras lognormales con σ = 0.3 (n = 4,000): el Vuong da **R = −16.62, p = 0.0002**,
  favoreciendo correctamente la lognormal, y pierde poder conforme σ crece, que es el
  comportamiento esperado.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
