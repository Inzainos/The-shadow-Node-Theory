# Pre-registro — el valor puntual del Dominio B: ¿cuántos de los 156 casos estimables son significativos?

**Fecha:** 2026-10-02 · **Rama:** `claude/charming-brown-w9h8iu` · **Base:** `main` en `676adf4`
· **Autor de la teoría:** Elán Zainos Corona · **Análisis:** Claude Code, a pedido del autor.

## 0. El pendiente, exactamente

El Dominio B son **446 pares de países**, cada uno con
`R(t) = PIBpc_hub / PIBpc_nodo` sobre los años comunes 1900–2018 y un ajuste OLS de
`log R` contra `log t`. Es el **62% del corpus** de 721 casos.

La auditoría v32 encontró que sus residuos son casi de raíz unitaria:
**Durbin-Watson mediana 0.112**, 445 de 446 casos con DW < 1, **ρ AR(1) implícita
mediana 0.944**, y **n efectiva mediana 2.2** contra una n nominal de 69.

Con esa corrección el cuadro publicado quedó así:

| Cifra | Valor | Estado |
|---|---:|---|
| Estimables (`n_eff ≥ 3`) | 156 / 446 | cerrado |
| No estimables (`n_eff < 3`) — no "no significativos" | 290 / 446 | cerrado |
| Significativos entre los estimables, **cota inferior** (SE inflado + gl) | 33 (21.2%) | cerrado |
| Significativos entre los estimables, **cota superior** (solo gl) | 112 (71.8%) | cerrado |
| **Valor puntual** | **abierto** | **lo que resuelve este pre-registro** |

Newey-West con el rezago automático de Bartlett (`floor(4·(n/100)^(2/9))`, que da 4 a
estas n) se calculó el 2026-09-27 y dio **120 de 156**: por encima de la cota
superior. Es decir, **subcorrige** con ρ ≈ 0.94, y por eso se registró como INFO y no
como valor puntual.

**Es el último número abierto de la teoría y no necesita red:** las series del
Dominio B se reconstruyen desde `data/maddison_mpd2020.csv`, ya versionado, y la
auditoría ya verifica que los 446 casos reproducen su `b` publicada con
|Δ| ≤ 1×10⁻⁴.

## 0.1 Ceguera: **parcial**. Declarada

- **Visto:** las cinco cifras cerradas de la tabla de arriba (156, 290, 33, 112) y el
  120 de Newey-West. Son la motivación de este documento. También he leído el código
  que construye las series (`expand_B_massive.py`) y el que calcula las cotas
  (`code/snt_utils_v32.py`), y sé que las series reconstruyen exacto, porque es
  estado previo del repositorio y no un resultado de esta prueba.
- **No visto:** **ningún resultado de GLS ni de bootstrap por bloques**, ni sobre los
  datos reales ni sobre simulación. No existe ninguno en el repositorio.

## 0.2 Reglas generales

1. **Se reporta todo resultado**, incluido "el valor puntual sigue abierto".
2. **α = 0.05**, p de dos colas, en todos los métodos.
3. **Semilla fija:** `20261002`.
4. **Log obligatorio** en `reconstruction_real/logs/`.
5. **Sin descargas.** Única entrada: `data/maddison_mpd2020.csv` y
   `data/by_domain/dominio_B_real.csv`, los dos ya versionados con su SHA-256 en
   `data/FUENTES.md`.
6. **Las series se reconstruyen exactamente como `calc()` de `expand_B_massive.py`**
   (años comunes 1900–2018, `t = 1..n`, sin reindexar), y se verifica caso por caso
   contra la `b` publicada antes de correr cualquier prueba. Si no reproducen, el
   análisis se detiene y se reporta eso.

---

## 1. El giro del diseño: no discutir qué corrección es la correcta, **medirla**

La tentación aquí es elegir un método por autoridad —"GLS es lo correcto con AR(1)"—
y reportar su número. Eso es exactamente lo que falló con Newey-West: es el método
estándar y dio una cifra imposible.

Así que el criterio no va a ser la autoridad del método, sino **su tasa de error tipo
I medida sobre series sintéticas que imitan al Dominio B**. Un método que a ρ = 0.94
rechaza la hipótesis nula el 40% de las veces no sirve, por canónico que sea; uno que
rechaza el 5% de las veces sirve, aunque sea feo.

Es la misma disciplina que resolvió el caso del rango-tamaño: ahí una prueba de poder
mostró que un p = 0.974 no valía nada. Aquí una prueba de **tamaño** va a mostrar
cuál de las correcciones es creíble.

---

## 2. Punto 1 — Calibración: tasa de falso positivo de cada método

**Construcción de las series sintéticas.** Se generan `N_SIM = 2,000` casos
sintéticos. Cada uno toma, de un caso real del Dominio B elegido al azar con
reemplazo, su terna observada **(n, ρ, σ)**:

- `n` = número de años comunes del caso real,
- `ρ = 1 − DW/2` del caso real, recortada a `[0, 0.995]`,
- `σ` = desviación estándar de los residuos OLS del caso real.

y produce `log R(t) = ε_t`, con `ε` un **AR(1) de parámetro ρ y varianza marginal σ²**
inicializado en su distribución estacionaria. Es decir: **`b` verdadera = 0, sin
tendencia alguna**. Cualquier rechazo es un falso positivo, por construcción.

**Métodos evaluados**, todos sobre `log R` contra `log t`:

| Clave | Método |
|---|---|
| `ols` | OLS ingenuo, el del corpus publicado |
| `ar1_inf` | Cota inferior AR(1): SE inflado por `√((1+ρ)/(1−ρ))` y gl `n_eff − 2` |
| `ar1_sup` | Cota superior AR(1): solo gl `n_eff − 2` |
| `nw_auto` | Newey-West con rezago automático de Bartlett (el que dio 120) |
| `nw_n4` | Newey-West con rezago `round(n/4)`, una banda acorde a ρ ≈ 0.94 |
| `gls_pw` | **Prais-Winsten** (GLS factible AR(1)), ρ estimada de los residuos OLS e iterada hasta `|Δρ| < 1e-6` o 50 iteraciones, conservando la primera observación con el factor `√(1−ρ²)` |
| `boot_b4` | **Bootstrap por bloques móviles** bajo la nula, longitud de bloque `max(2, round(n^(1/3)))` |
| `boot_b8` | Igual, longitud `max(2, round(√n))` |
| `boot_b17` | Igual, longitud `max(2, round(n/4))` |

El bootstrap por bloques se hace **bajo la hipótesis nula**: se remuestrean bloques
móviles de los residuos del ajuste restringido (`b = 0`), se reconstruye
`log R* = a + ε*`, se reajusta por OLS y se toma
`p = (1 + #{|b*| ≥ |b_obs|}) / (B + 1)`. Réplicas: **B = 199** dentro de la
simulación y **B = 999** sobre los datos reales.

**Se reporta, por método:** la tasa de rechazo global sobre los 2,000 casos
sintéticos, y la tasa **dentro del estrato estimable** (`n_eff ≥ 3`), que es el
estrato donde vive la pregunta.

### Regla de admisión, fijada aquí

Un método es **admisible** para producir el valor puntual si su tasa de falso
positivo medida en el estrato estimable cae en **[0.025, 0.075]** — el 5% nominal con
una tolerancia de ±2.5 puntos.

- Si **ningún** método es admisible, **el valor puntual no se declara.** Se reporta la
  tabla de tamaños medidos y se concluye que esta especificación no admite pruebas de
  significancia, lo cual es un resultado más fuerte que cualquier cifra.
- Si **varios** son admisibles, el valor puntual lo produce el de **mayor poder** en el
  punto 2. Se reportan todos.

---

## 3. Punto 2 — Poder: que un método sea conservador no lo vuelve útil

Un método que nunca rechaza tiene tamaño 0% y es inservible. Así que sobre la misma
construcción del punto 1, pero con una tendencia verdadera añadida
(`log R(t) = b·log t + ε_t`), se mide el poder de cada método en dos puntos:

- **b = −0.30**, un efecto moderado dentro del rango del corpus;
- **b = −0.60**, el `b̄` del dominio ACO, un efecto grande.

Se reporta el poder de los nueve métodos en los dos puntos, en el estrato estimable y
en total. **Sin esta tabla, el valor puntual no se interpreta**: una cifra baja puede
venir de un método riguroso o de un método ciego, y hay que poder distinguirlo.

---

## 4. Punto 3 — El valor puntual sobre los 446 casos reales

Solo con los métodos admisibles del punto 1. Se reporta, por método:

- significativos **entre los 156 estimables** (la cifra que cierra el pendiente),
- significativos **entre los 446** (para comparar con el 374 publicado sin corregir),
- si la cifra cae **dentro de las cotas [33, 112]**.

---

## 5. Qué significa cada desenlace

Escrito **antes** de ver cualquier resultado, para que ninguna lectura se acomode
después.

| Desenlace | Lectura para la SNT |
|---|---|
| Hay método admisible y su cifra cae **dentro de [33, 112]** | El pendiente **se cierra**. El valor puntual se publica con su método, su tamaño medido y su poder medido, y las cotas quedan como lo que son: cotas |
| Hay método admisible y su cifra cae **fuera de [33, 112]** | El valor puntual se publica igual, y **las cotas pasan a estar mal calibradas**: habría que corregir la tabla de la auditoría v32, no el método. Se reporta con esa consecuencia escrita |
| **Ningún método es admisible** | El valor puntual **no se declara, y queda cerrado como indecidible**: con ρ ≈ 0.94 y n ≈ 69 esta especificación no admite pruebas de significancia. La cota inferior de 33 queda como la cifra conservadora a citar, y el Dominio B pasa a ser descriptivo, no inferencial |
| Los métodos admisibles **discrepan entre sí** fuera de un margen razonable | Se reportan todos sin elegir, y el pendiente se reformula: el valor puntual depende del método incluso entre los bien calibrados |

**Lo que este pre-registro NO hace.** No vuelve a estimar ninguna `b`, no cambia
ninguna serie, no toca el eje de satelización ni la capa ACO-A, y **no modifica el
corpus**. Mide una sola cosa: cuántos de los 156 casos estimables del Dominio B
soportan una afirmación de significancia cuando la autocorrelación se trata con un
método cuya tasa de error está medida y no supuesta.

Tampoco resuelve el otro pendiente del Dominio B: el discriminante
acoplamiento-contra-convergencia, que sigue inconcluso por razones ajenas a esta
prueba (`audits/DISCRIMINANTE_DOMINIO_B.md`).

---

## 6. Salidas previstas

- `reconstruction_real/code/dominio_B_valor_puntual.py` (con log).
- `reconstruction_real/data/dominio_B_calibracion.csv` — tamaño y poder por método.
- `reconstruction_real/data/dominio_B_valor_puntual.csv` — una fila por caso real con
  el p de cada método admisible.
- `reconstruction_real/audits/RESULTADOS_DOMINIO_B_PUNTUAL_2026-10-02.md`, con la
  tabla hipótesis → resultado → decisión y la sección **Desviaciones**.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
