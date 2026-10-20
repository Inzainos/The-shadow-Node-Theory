# Pre-registro — ¿el exponente deriva a lo largo de la vida de un caso, y esa deriva depende de la fricción?

**Fecha:** 2026-10-02 · **Rama:** `claude/charming-brown-w9h8iu` · **Base:** `main` en `676adf4`
· **Autor de la teoría:** Elán Zainos Corona · **Análisis:** Claude Code, a pedido del autor.

## 0. De dónde sale esta prueba

La SNT ajusta la satelización con una sola forma funcional, `R(t) = a·t^b`, y trata el
régimen superlineal (`b ≥ 1`, el "radio de Roche") como un régimen físico distinto. La
capa de colapso, en cambio, **sí** admite una taxonomía: cinco modos determinados por
fricción × disparador × piso.

**Esa asimetría es el punto de partida.** El autor planteó que un mismo caso podría
empezar como ley de potencia, volverse lineal con el tiempo, y solo después entrar en
colapso — es decir, que la forma no es una etiqueta por caso sino una **trayectoria
dentro del caso**. Y añadió una restricción que vuelve la hipótesis mucho más fuerte:
los ambientes digitales no se comportan así, porque **o acaban abruptos o se
mantienen**.

Esa restricción es el eje de fricción de la propia teoría. Un ambiente digital es
fricción ≈ 0: sin planta física, sin contratos laborales, sin rezago regulatorio, sin
capital hundido. Si no hay nada que frene, no hay con qué estirar una fase intermedia.
**La fase lineal necesita fricción para existir.**

De ahí sale una predicción **diferencial**, que es la que se pre-registra:

> La deriva del exponente a lo largo de la vida de un caso **existe en dominios de
> fricción alta y está ausente en dominios de fricción ≈ 0.**

Una predicción que dice "aquí sí y allá no" es mucho más difícil de satisfacer por
accidente que una que solo predice presencia. Es lo que convierte a los dominios
digitales en **control** y no en prueba.

## 0.1 Ceguera: **ninguna**. Declarada

El autor reportó haber observado (a) tendencia a la linealidad en series largas y
(b) bimodalidad en ambientes digitales. El analista, además, ya vio:

- **npm:** `b_subida` mediana +0.516 (369 positivos, 81 negativos), R² mediana 0.3415
  (135 casos con R² < 0.1, 170 con R² > 0.5); `delta_caida` mediana −0.808, R² mediana
  0.5193; 41 de 450 extinciones funcionales (9.1%); hazard decreciente con la edad
  (ρ = −0.716, p = 0.013).
- **Fricción por dominio:** la tabla de 2,600 casos en 11 dominios con sus `b` y `n`
  medianos por nivel de fricción 0–3.
- **Dominio B:** DW mediana 0.112, ρ AR(1) mediana 0.944, `n_eff` mediana 2.2, y la
  tasa de falso positivo del OLS medida hoy, 67.0%.
- **ACO:** AIC sobre 18 series crudas — potencia 13/18, exponencial 4/18, lineal 1/18,
  con los 4 ganadores de la exponencial en b medio +1.54. **Advertencia: ese es el
  exponente de absorción, no el de satelización.** Se anota porque en una conversación
  previa el analista los confundió.

**No visto, y no existe en el repositorio:** ninguna estimación de `b` en ventana
móvil, ningún estadístico de deriva, ningún análisis dentro de caso, en ningún dominio.

Este documento fija **qué se mide y con qué reglas de decisión antes de ver un solo
resultado**, no simula una ceguera que no hubo.

## 0.2 Reglas generales

1. **Se reporta todo resultado**, incluida la ausencia de deriva.
2. **α = 0.05**; cola según se especifique en cada punto.
3. **Semilla fija:** `20261002`.
4. **Log obligatorio** en `reconstruction_real/logs/`.
5. **Sin descargas.** Todas las entradas están ya en disco o versionadas.
6. **Nada se recorta por su valor.** Las exclusiones son solo por longitud insuficiente
   y se cuentan y reportan.

---

## 1. Los tres brazos, y por qué son tres

El confundido que casi arruina este diseño: el Dominio B mide un **cociente** hub/nodo
y npm mide un **nivel** de descargas. Si solo se comparan esos dos, una diferencia
podría venir de la fricción **o** de que una cantidad es cociente y la otra no. Cripto
resuelve eso: un precio **es** un cociente, y cripto es fricción ≈ 0.

| Brazo | Fricción | Cantidad | Casos | Serie cruda |
|---|---|---|---:|---|
| **Dominio B** (países) | **alta (3)** — codificada en `data/friccion_dominios_nuevos_casos.csv` | **cociente** PIBpc hub / PIBpc nodo | 446 | `data/maddison_mpd2020.csv` |
| **Cripto** (moneda / BTC) | **≈ 0** — ubicación a priori, fijada aquí | **cociente** precio moneda / precio hub | hasta 662 | `data/binance_cierres_diarios.csv.gz` |
| **npm** (descargas) | **≈ 0** — ubicación a priori, fijada aquí | **nivel** mensual de descargas | 450 | `data/raw_npm/descargas.jsonl.gz` |

**Contraste principal: Dominio B contra cripto.** Los dos son cocientes, fricción
opuesta. Es la comparación que prueba la hipótesis.

**Tercer brazo, npm:** mismo nivel de fricción que cripto pero cantidad de otro tipo.
Sirve para saber si la distinción cociente-contra-nivel importa. Si npm y cripto
coinciden, no importa; si difieren, el diseño lo detecta en vez de esconderlo.

**Celda ausente, declarada:** no hay un dominio de fricción alta con cantidad de tipo
nivel y serie cruda disponible. El 2×2 queda incompleto y eso limita la inferencia.

### Ubicación a priori de la fricción para los dos dominios digitales

Se fija **aquí, antes de correr nada**, con criterios estructurales y no por resultado:
ausencia de planta física, de inventario, de contratos laborales, de rezago
regulatorio y de capital hundido; capacidad de cesar la actividad sin costo de
desmantelamiento. Cripto y npm cumplen los cinco → **fricción ≈ 0**. El Dominio B
(economías nacionales) no cumple ninguno y además ya está codificado como fricción 3
en el repositorio.

### Construcción de las series

- **Dominio B:** exactamente como `calc()` de `expand_B_massive.py` — años comunes
  1900–2018, `t = 1..n`. Se verifica caso por caso que la `b` global reproduzca la
  publicada con |Δ| ≤ 1×10⁻⁴ **antes** de cualquier prueba; si no reproduce, el
  análisis se detiene y se reporta eso.
- **Cripto:** `R(t) = close_moneda(t) / close_BTC(t)` en días comunes, con **BTCUSDT
  como hub** y excluyendo al hub de la lista de nodos. Mínimo **200 días** comunes.
- **npm:** descargas agregadas por mes calendario desde el nacimiento del paquete,
  para los 450 de la cohorte. Mínimo **24 meses**.

---

## 2. La medición: exponente local en ventana móvil

Para cada caso, sobre `log R` contra `log t`:

- **Ancho de ventana:** `w = max(8, round(n/4))`.
- **Paso:** `s = max(1, round(w/4))`.
- **Mínimo de ventanas:** **5**. Los casos con menos quedan excluidos, contados y
  reportados por brazo.
- En cada ventana `k` se estima `b_k` por OLS de `log R` contra `log t` **dentro de la
  ventana**. `b_k` es el exponente local, es decir `d(log R)/d(log t)` en ese tramo.

**Estadístico por caso:** `ρ_k` = Spearman entre el índice de ventana y `b_k`. Negativo
= el exponente baja a lo largo de la vida del caso.

Se elige medir `b(t)` directamente, y no competir entre familias funcionales, por una
razón que conviene dejar escrita: en `R = a·t^b`, **`b = 1` ES lineal**. Comparar
"potencia contra lineal" confundiría un cambio de familia con un exponente que se
desplaza. Medir la deriva de `b` y reportar si cruza 1 separa las dos cosas.

---

## 3. El nulo, que aquí es la prueba entera

Un `ρ_k` negativo también lo produce el puro ruido: reversión a la media, la
compresión de `log t` hacia el final de la serie, y sobre todo la autocorrelación. En
el Dominio B, con ρ AR(1) mediana 0.944, **la deriva espuria va a ser grande**. Hoy
mismo medimos que su OLS tiene 67.0% de falso positivo.

Por eso el nulo se simula **por caso**:

- `b` **constante**, igual a la `b` global del caso.
- Ruido AR(1) con la ρ y la σ estimadas de los residuos de ese mismo caso.
- Misma `n`, mismo ventaneo, mismo estadístico.
- **299 réplicas** por caso.

`p_desc` = fracción de réplicas con `ρ_k` ≤ el observado (una cola, descendente).
`p_asc` = la simétrica, ascendente. Las **dos** se reportan: la deriva ascendente es
el falsificador directo.

---

## 4. Estadísticos de decisión

**Por brazo:** fracción de casos con deriva **descendente** significativa
(`p_desc < 0.05`) y fracción con deriva **ascendente** significativa (`p_asc < 0.05`),
sobre los casos con ventanas suficientes.

**Principal:** la **diferencia** de la fracción descendente entre Dominio B y cripto,
con intervalo de confianza del 95% por bootstrap de casos (**1,999 réplicas**).

Se compara cada brazo **contra su propio nulo simulado**, no contra un 5% teórico. Eso
es lo que vuelve interpretable el Dominio B a pesar de su autocorrelación: no se
pregunta "¿baja `b` en el Dominio B?" en términos absolutos, sino **"¿excede el
Dominio B su propio nulo más de lo que cripto excede el suyo?"**

---

## 5. Puntos secundarios

- **S1 — El cruce del 1.** Distribución de `b_k` en la primera y la última ventana por
  brazo, y fracción de casos que **cruzan `b = 1` a la baja**. "Potencia → lineal"
  predice el cruce, no una bajada cualquiera.
- **S2 — Bimodalidad en fricción 0.** Por brazo digital: fracción que persiste contra
  fracción que cae, y empinamiento de la caída cuando cae. Es la mitad "o muy abruptos
  o se mantienen" de la hipótesis del autor.
- **S3 — Control de supervivencia.** En npm, deriva en los **41 extinguidos** contra
  los **409 persistentes**. Si la deriva aparece solo en los que murieron, es una firma
  pre-colapso y no una trayectoria universal — y eso cambia la lectura por completo.
- **S4 — Relación con RC1.** Bajo la hipótesis, los casos superlineales (`b ≥ 1` global)
  son casos **atrapados temprano** en su trayectoria. Se reporta la `b` de la primera
  ventana contra la `b` global, y qué fracción de los superlineales tiene `b_k`
  descendente.

---

## 6. Qué significa cada desenlace

Escrito **antes** de ver cualquier resultado.

| Desenlace | Lectura |
|---|---|
| Descendente **mayor en el Dominio B que en cripto**, y el Dominio B por encima de su propio nulo | **H1 respaldada.** La deriva existe y depende de la fricción. El régimen de forma pasa a coordenada candidata por las cuatro condiciones del Axioma 12 |
| Descendente **igual en los dos** | La deriva existe pero **no depende de la fricción**. El encuadre de fricción se cae; la trayectoria sobrevive sin él |
| Descendente **en cripto y no en el Dominio B** | **Contrario a la predicción.** El control falla, y la historia de la fricción se retira |
| **Ningún brazo** excede su nulo | No hay deriva medible. La trayectoria queda sin respaldo y `b` se trata como constante. El régimen superlineal se queda como está |
| Deriva **ascendente** significativa en una fracción apreciable de cualquier brazo | **Falsificador directo** de la trayectoria tal como está planteada |
| npm y cripto **difieren entre sí** | La distinción cociente-contra-nivel importa, y el contraste de fricción queda confundido con ella. Se reporta sin elegir |

**Lo que este pre-registro NO hace.** No reestima ninguna `b` publicada, no modifica el
corpus, no toca el gradiente compuesto de Tlaxcala ni la ortogonalidad b ⊥ Δ, y **no
prueba la cláusula "al final todo entra en el colapso"**, que con los datos de npm ya
quedó sin respaldo dentro de la ventana observable (90.9% no colapsó) y que, enunciada
sobre un largo plazo inobservable, no es falsable.

Tampoco resuelve las dos piezas que faltan para el eje de fricción completo —la
codificación formal de los dominios digitales dentro del corpus y las etiquetas de modo
de colapso por caso—. Quedan **para después, por decisión del autor**, y este diseño no
las requiere: usa la codificación de fricción que ya existe para el Dominio B y una
ubicación a priori declarada para los dos digitales.

## 6.1 Limitaciones, declaradas de antemano

1. **Los casos de cripto no son independientes.** El mercado se mueve en bloque. Se
   reporta, además del estadístico principal, una versión con los casos agrupados por
   trimestre de pico, para ver cuánto del resultado sobrevive al agrupamiento.
2. **La ventana de cripto es corta** (2017–2025) comparada con los 119 años del
   Dominio B. La deriva se mide en escala relativa a la vida de cada caso, pero el
   contraste sigue siendo entre dominios con historias de muy distinta duración.
3. **npm mide un nivel, no un cociente.** Por eso está cripto. Si npm y cripto
   discrepan, la lectura se reporta sin elegir.
4. **La celda fricción alta × nivel no existe** en estos datos.
5. **La ubicación a priori de la fricción digital es un juicio**, no una medición. Está
   fijada aquí con criterios explícitos para que se pueda discutir, no para que pase
   inadvertida.

---

## 7. Salidas previstas

- `reconstruction_real/code/deriva_forma_friccion.py` (con log).
- `reconstruction_real/data/deriva_forma_por_caso.csv` — una fila por caso con `ρ_k`,
  `p_desc`, `p_asc`, `b` de la primera y última ventana, número de ventanas.
- `reconstruction_real/data/deriva_forma_resumen.csv` — por brazo y por punto.
- `reconstruction_real/audits/RESULTADOS_DERIVA_FORMA_2026-10-02.md`, con la tabla
  hipótesis → resultado → decisión y la sección **Desviaciones**.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
