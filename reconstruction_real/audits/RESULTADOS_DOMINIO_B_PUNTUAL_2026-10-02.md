# Resultados — el valor puntual del Dominio B

**Pre-registro:** [`../preregistro/PREREGISTRO_DOMINIO_B_PUNTUAL_2026-10-02.md`](../preregistro/PREREGISTRO_DOMINIO_B_PUNTUAL_2026-10-02.md)
(commit `05bc9ee`, subido antes de correr el script).
**Script:** `code/dominio_B_valor_puntual.py` (con log).
**Datos:** `data/maddison_mpd2020.csv` y `data/by_domain/dominio_B_real.csv`, ya
versionados. **Sin descargas.**
**Salidas:** `data/dominio_B_calibracion.csv`, `data/dominio_B_valor_puntual.csv`.

Cierra el **último número abierto de la teoría**, y lo cierra en la dirección que
menos se esperaba: **el valor puntual no existe.**

---

## Tabla de decisiones

| Punto | Pregunta | Resultado | Decisión |
|---|---|---|---|
| **0** | ¿Las 446 series reconstruyen la `b` publicada? | **446 / 446** con \|Δb\| ≤ 1×10⁻⁴ | **CORRECTO**, se procede |
| **P1** | ¿Algún método alcanza el 5% nominal de falso positivo? | El mejor es **11.7%** (cota inferior AR(1)); el resto va de 17.1% a 67.0% | **NINGUNO ES ADMISIBLE** |
| **P2** | ¿El fallo es por exceso de conservadurismo? | Poder de **74% a 98%** a b = −0.30 y de **91% a 100%** a b = −0.60 | **NO.** El fallo es de tamaño, no de poder |
| **P3** | ¿Cuántos de los 156 estimables son significativos? | Entre **33 y 134** según el método | **NO SE DECLARA** — regla pre-registrada |

**Veredicto:** el valor puntual del Dominio B queda **cerrado como indecidible**. Con
ρ ≈ 0.94 y n ≈ 69, ninguno de los doce métodos evaluados —incluidos los dos que la
literatura recomienda para este caso— alcanza el tamaño nominal.

---

## 1. P1 — La calibración, que es el punto de todo el diseño

2,000 casos sintéticos con la terna `(n, ρ, σ)` de un caso real del Dominio B elegido
al azar y **`b` verdadera = 0**: cualquier rechazo es un falso positivo por
construcción. De los 2,000, **1,738 caen en el estrato estimable** (`n_eff ≥ 3`), que
es donde vive la pregunta.

| Método | Tasa de falso positivo (estimables) | Pre-registrado | ¿Admisible? |
|---|---:|---|---|
| `ols` — el del corpus publicado | **67.0%** | sí | no |
| `ar1_inf` — cota inferior AR(1) (SE inflado + gl) | **11.7%** | sí | no |
| `ar1_sup` — cota superior AR(1) (solo gl) | 53.1% | sí | no |
| `nw_auto` — Newey-West, rezago automático | 52.3% | sí | no |
| `nw_n4` — Newey-West, rezago `n/4` | 48.4% | sí | no |
| `gls_pw` — **Prais-Winsten GLS** iterado | **17.1%** | sí | no |
| `boot_rb3` — bloques móviles `n^(1/3)`, residuos restringidos | 43.2% | sí | no |
| `boot_rb8` — bloques `√n`, restringidos | 29.5% | sí | no |
| `boot_rb17` — bloques `n/4`, restringidos | **24.1%** | sí | no |
| `boot_ub3` / `boot_ub8` / `boot_ub17` — los mismos con residuos no restringidos | 47.9% / 40.3% / 40.0% | añadido | no |

La regla de admisión, fijada en el pre-registro, era **[2.5%, 7.5%]**. El mejor método
está a **once puntos y medio** del techo de esa banda, y es la cota que ya se usaba
como conservadora. Los dos métodos que uno elegiría por autoridad —GLS para AR(1),
bootstrap por bloques para dependencia serial— quedan en 17.1% y 24.1%: **mejores que
el resto, insuficientes igual.**

> Con los residuos del Dominio B, un contraste al 5% nominal rechaza en realidad
> entre el 12% y el 67% de las veces cuando no hay ningún efecto. No hay forma de
> leer un p de este dominio como un p.

### El número que más duele: 67.0%

`ols` es el procedimiento con el que se construyó el corpus publicado. Su tasa de
falso positivo medida es **67.0%**: rechaza la nula **dos veces de cada tres cuando no
hay nada que rechazar.** Eso pone una cifra a la "doble inflación" que la auditoría
v32 describió en palabras, y explica el 374 de 446 "significativos" del corpus sin
necesidad de suponer nada.

---

## 2. P2 — El fallo es de tamaño, no de poder, y eso importa

Un método puede fallar la calibración por ser demasiado conservador. **No es el caso
de ninguno aquí**, y por eso el punto 2 estaba en el pre-registro.

| Método | Poder a b = −0.30 | Poder a b = −0.60 |
|---|---:|---:|
| `ols` | 97.8% | 99.9% |
| `ar1_inf` | 74.1% | 90.9% |
| `ar1_sup` | 95.6% | 99.7% |
| `nw_auto` | 96.4% | 99.8% |
| `nw_n4` | 95.9% | 99.7% |
| `gls_pw` | 97.7% | 100.0% |
| `boot_rb3` | 96.3% | 99.8% |
| `boot_rb8` | 95.4% | 99.8% |
| `boot_rb17` | 94.6% | 99.7% |
| `boot_ub3` / `boot_ub8` / `boot_ub17` | 96.4% / 95.5% / 95.6% | 99.8% / 99.8% / 99.8% |

Todos los métodos detectan un efecto real sin dificultad. **El problema es que también
"detectan" efectos que no existen.** Incluso el más conservador de los doce
—`ar1_inf`, con 74.1% de poder a b = −0.30— rechaza el 11.7% de las veces bajo la
nula. Ninguno está intercambiando tamaño por poder: todos están anti-conservadores.

---

## 3. P3 — El valor puntual, y por qué no se declara

Los doce métodos sobre los 446 casos reales:

| Método | sig / 156 estimables | sig / 446 | ¿En [33, 112]? |
|---|---:|---:|---|
| `ols` | 134 | **374** | NO |
| `ar1_inf` | **33** | 33 | sí |
| `ar1_sup` | 113 | 115 | NO |
| `nw_auto` | **120** | 326 | NO |
| `nw_n4` | 109 | 279 | sí |
| `gls_pw` | **57** | 111 | sí |
| `boot_rb3` | 109 | 302 | sí |
| `boot_ub3` | 114 | 314 | NO |
| `boot_rb8` | 88 | 248 | sí |
| `boot_ub8` | 104 | 283 | sí |
| `boot_rb17` | 72 | 187 | sí |
| `boot_ub17` | 99 | 274 | sí |

**El rango es de 33 a 134 de 156**, es decir de 21% a 86%. Ese abanico, sobre los
mismos datos y la misma hipótesis, es por sí mismo el argumento: la cifra puntual **es
un artefacto del método elegido**, y por eso el pre-registro prohibía declararla sin
una calibración que la respalde.

Si hubiera que señalar un número —y el pre-registro dice que **no** hay que hacerlo—
sería el 57 del GLS, que es el segundo mejor calibrado y cae dentro de las cotas. Se
anota para que quede constancia de que no se escondió, **no como valor puntual.**

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
   implementaciones independientes coinciden al caso.

### Y una convergencia que vale la pena nombrar

**El método mejor calibrado de los doce es precisamente el que la auditoría ya había
elegido como cifra conservadora, y da exactamente 33.** La elección de la auditoría
—tomada por prudencia, sin medición— queda respaldada por medición. No es que el 33
sea "el valor puntual": es que de los doce candidatos, el menos malo es el que ya se
estaba citando.

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
pre-registrados, y se reportan como tal.)

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
Durbin-Watson—, lo cual refuerza la conclusión principal en vez de contradecirla. La
cota inferior no tiene este problema: da 33 por las dos vías.

---

## 6. Qué significa para la SNT

El pre-registro fija la lectura de cada desenlace. El que aplica es el tercero:

> *"Ningún método es admisible → el valor puntual **no se declara, y queda cerrado
> como indecidible**: con ρ ≈ 0.94 y n ≈ 69 esta especificación no admite pruebas de
> significancia. La cota inferior de 33 queda como la cifra conservadora a citar, y el
> Dominio B pasa a ser descriptivo, no inferencial."*

| Afirmación | Estado anterior | Estado ahora |
|---|---|---|
| Estimables / no estimables, 156 / 290 | Cerrado | **Sin cambio.** Sale de `n_eff < 3`, no depende de convenciones ni de métodos |
| Cota inferior 33 (21.2%) | Cerrada, elegida por prudencia | **Respaldada por medición**: es el método mejor calibrado de doce |
| Cota superior 112 (71.8%) | Cerrada | **Frágil**: 112 o 113 según el redondeo de un `dw`; y su método tiene 53.1% de falso positivo |
| Valor puntual | Abierto | **Cerrado como indecidible.** Último número abierto de la teoría, y la respuesta es que no hay número |
| Los 374/446 significativos del corpus | Sabidos inflados | **Cuantificado:** el procedimiento que los produjo rechaza el **67.0%** de las veces bajo la nula |
| El exponente `b` del Dominio B | Verificado | **Sin cambio.** Esta prueba no reestima ninguna `b` |
| Dirección de los hallazgos del dominio | Verificada en todas las variantes | **Sin cambio.** La dirección no depende de la significancia por caso |

**Lo que se cae es la significancia por caso, no la medición.** Las 446 `b` siguen
siendo descripciones válidas y reproducibles de sus pares de países. Lo que no se puede
hacer con ellas es contar cuántas son "significativas", porque ningún contraste
disponible a esta ρ y esta n tiene un tamaño que lo permita. El Dominio B queda
**descriptivo**.

Es la misma clase de corrección que el 5.9×, el ROC-AUC filtrado, la precisión
tautológica del ASI y la lectura de apego preferencial del Módulo de N-cuerpos: **la
aritmética estaba bien, la inferencia no.** Cinco veces el mismo patrón, y esta es la
primera en la que la respuesta es explícitamente "no se puede saber".

### Alcance de la palabra "indecidible"

Honestidad sobre lo que esto no dice. "Indecidible" aplica a **esta especificación**
—OLS de `log R` contra `log t` con residuos casi de raíz unitaria a n ≈ 69— y a **estos
doce métodos**. No es una afirmación de que ningún procedimiento podría funcionar
nunca. Lo que haría falta para reabrirlo, en orden de viabilidad:

1. **Cambiar la especificación**, no el contraste: trabajar en diferencias o con un
   modelo que no suponga residuos estacionarios alrededor de una tendencia
   logarítmica. Es el camino que la literatura de raíz unitaria señalaría.
2. **Más observaciones por caso**, que con series anuales 1900–2018 no existen.
3. **Un contraste con tamaño verificado** a ρ ≈ 0.95 y n ≈ 69. Si aparece, la prueba
   de calibración de este informe es el banco donde debe pasar antes de usarse.

---

## Desviaciones respecto al pre-registro

Dos, las dos declaradas:

1. **Tres métodos de bootstrap añadidos.** El pre-registro fijaba el remuestreo sobre
   los residuos del ajuste **restringido** (`b = 0`). Al implementarlo quedó claro que
   la variante **no restringida** no arrastra la señal al ruido y por tanto no pierde
   poder cuando `b ≠ 0`. En vez de cambiar lo pre-registrado en silencio se
   implementaron **las dos**, y las tres añadidas van marcadas como `añadido` en el
   log, en la columna `preregistrado` del CSV y en las tablas de este informe. No
   altera ninguna conclusión: las seis variantes quedan igual de lejos de la banda de
   admisión.
2. **Réplicas de bootstrap: 199 en la simulación, 999 sobre los datos reales.** Estaba
   fijado así en el pre-registro y se cumple; se repite aquí porque es la clase de
   parámetro que conviene tener a la vista. Con tasas observadas de 24% a 48%, muy
   lejos del techo del 7.5%, la precisión del bootstrap corto sobra para la decisión.

Lo que **no** se desvió: la regla de admisión [2.5%, 7.5%], los dos puntos de poder,
la semilla `20261002`, y la prohibición de declarar un valor puntual sin método
admisible — que es la regla que gobierna el resultado y se respetó aunque el GLS
ofreciera una cifra cómoda dentro de las cotas.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
