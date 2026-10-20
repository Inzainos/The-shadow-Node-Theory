# Pre-registro — comparación lognormal del ajuste rango-tamaño de N-cuerpos (México)

**Fecha:** 2026-10-02 · **Rama:** `claude/charming-brown-w9h8iu` · **Base:** `main` en `8f5f27b`
· **Autor de la teoría:** Elán Zainos Corona · **Análisis:** Claude Code, a pedido del autor.

## 0. Qué resuelve

El README declara, desde la auditoría v32, un pendiente sobre una de las cifras más
citadas del repositorio:

> *"A rank-size fit over 32 ordered entities yields a high R² almost by construction,
> so it is not by itself evidence of preferential attachment until it is compared
> against a lognormal alternative (Clauset et al., 2009)."*

Y lo daba por bloqueado: *"The committed file is a one-row summary; the rank-size
series needed to refit from raw data is not in the repo."*

**Esa segunda afirmación es incorrecta.** La serie sí está versionada, en
`data/matriz_mexico_32.csv` (32 entidades con `pib_pc`). La comparación se puede
hacer sin descargar nada.

## 0.1 Ceguera: **ninguna**. Declarada

A diferencia de los pre-registros anteriores, aquí el analista **ya vio los datos**
antes de escribir este documento. Concretamente, ya verificó que:

- el ajuste publicado **reproduce exacto** desde `pib_pc`: b = −0.4732, p = 7.5×10⁻¹⁵;
- el R² de 0.8705 de `mexico_nbody_real.csv` y el 0.8377 del README son **la misma
  cifra con dos definiciones** (escala logarítmica y escala cruda), el mismo defecto
  de reporte que la auditoría v32 ya documentó para el corpus;
- los 32 valores van de **43.9 a 285.2**, es decir un factor de 6.5 — **0.81 órdenes
  de magnitud**.

Este documento existe para fijar **qué pruebas se corren y con qué reglas de decisión
antes de ver sus resultados**, no para simular una ceguera que no hubo. Las cifras de
arriba son descriptivas del ajuste ya publicado; ninguna prueba de las de abajo se ha
ejecutado.

## 0.2 Límite estructural, anotado de antemano

Clauset, Shalizi y Newman (2009) advierten que distinguir una ley de potencia de una
lognormal exige que la cola abarque **varios órdenes de magnitud** y un n grande; con
n = 32 y 0.81 órdenes de magnitud **se espera que las pruebas no puedan distinguir**.

Eso **no invalida la prueba: es parte del resultado.** Si el veredicto es
"indistinguible", la conclusión no es "la ley de potencia gana por falta de pruebas",
sino que **estos datos no pueden sostener la afirmación**, que es justo lo que el
pendiente del README preguntaba. Queda escrito aquí para que no se lea después como
una excusa construida a posteriori.

## 0.3 Reglas generales

1. **Se reporta todo resultado**, favorable o no.
2. **α = 0.05**; se reportan los p de dos colas.
3. **Semilla fija:** `20261002` en todo bootstrap y simulación.
4. **Log obligatorio** en `reconstruction_real/logs/`.
5. Datos: `data/matriz_mexico_32.csv`, columna `pib_pc`, 32 entidades. Sin descargas.

---

## Punto 1 — Ley de potencia contra lognormal en la **distribución** (método de Clauset)

Es la prueba que el README cita por su nombre.

**Ajuste.** Estimación por máxima verosimilitud del exponente α de la cola continua,
con `x_min` elegido por minimización del estadístico de Kolmogórov-Smirnov sobre todos
los valores candidatos de la muestra. Se reporta α, `x_min` y el n de la cola.

**Bondad de ajuste.** p por **bootstrap paramétrico** con 2,000 réplicas sintéticas:
se simulan muestras del modelo ajustado, se reajusta cada una por el mismo
procedimiento y se mide la fracción cuyo KS supera el observado.

**Decisión (regla de Clauset):** la ley de potencia **se descarta** si p < 0.1. Un
p ≥ 0.1 **no la confirma**: solo indica que no se puede descartar con estos datos.

**Comparación.** Prueba de razón de verosimilitudes de **Vuong** contra una lognormal
ajustada sobre la misma cola (x ≥ `x_min`), con su p de dos colas.

| Resultado | Lectura |
|---|---|
| R > 0 con p < 0.05 | Favorece la **ley de potencia** |
| R < 0 con p < 0.05 | Favorece la **lognormal** |
| p ≥ 0.05 | **Indistinguible** con estos datos |

**Secundaria:** la misma comparación contra una **exponencial**, que es la compañera
habitual de la prueba.

---

## Punto 2 — Ley de potencia contra lognormal en la **curva rango-tamaño**

Es la forma que realmente muestra la figura del repositorio: valor contra rango.

Se ajustan por mínimos cuadrados, sobre los mismos 32 puntos ordenados, dos modelos:

- **Potencia:** log(valor) = log(a) + b·log(rango) — el ajuste publicado.
- **Lognormal:** valor = exp(μ + σ·Φ⁻¹(1 − (rango − 0.5)/n)), la curva de cuantiles
  que predice una lognormal con los μ y σ de máxima verosimilitud de los datos.

**Comparación por AIC**, con la convención habitual:

| ΔAIC a favor del mejor | Lectura |
|---|---|
| < 2 | Indistinguibles |
| 2 a 10 | Evidencia moderada |
| > 10 | Evidencia fuerte |

Se reportan además el R² de cada modelo **en las dos escalas** (logarítmica y cruda),
precisamente porque mezclarlas fue uno de los defectos que la auditoría v32 encontró.

---

## Punto 3 — Hasta dónde alcanza el diseño (potencia)

Para que el resultado del punto 1 sea interpretable hace falta saber si la prueba
podía distinguir algo.

Se simulan 1,000 muestras de n = 32 extraídas de una **lognormal** con los parámetros
estimados de los datos reales, y en cada una se corre el procedimiento completo del
punto 1. **Se reporta qué fracción de esas muestras —que por construcción NO son leyes
de potencia— la prueba clasificaría como "no descartable".**

Esa fracción es la tasa de falsos "la ley de potencia sobrevive". Si es alta, el punto
1 no tiene poder y hay que decirlo con esa cifra en la mano, no como impresión.

---

## Salidas previstas

- `reconstruction_real/code/nbody_lognormal_clauset.py` (con log).
- `reconstruction_real/data/nbody_lognormal_resultados.csv`.
- `reconstruction_real/audits/RESULTADOS_LOGNORMAL_2026-10-02.md`, con la tabla
  hipótesis → resultado → decisión y la sección **Desviaciones**.

## Qué se actualiza según el resultado

Pase lo que pase, el README deja de decir que la serie no está en el repositorio, y
el pendiente de RC5 deja de estar abierto sin cifra.

- Si la ley de potencia **sobrevive y gana**: se registra, con la salvedad del poder.
- Si **gana la lognormal**: la lectura de apego preferencial del Módulo de N-cuerpos
  se corrige, como se corrigieron el 5.9×, el ROC-AUC y la precisión del ASI.
- Si resulta **indistinguible**: se declara que estos datos no pueden sostener ni
  refutar la afirmación, y el b = −0.473 queda como **descriptivo**, no como evidencia
  de apego preferencial.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
