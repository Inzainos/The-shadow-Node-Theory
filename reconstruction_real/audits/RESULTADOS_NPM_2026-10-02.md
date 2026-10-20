# Resultados del pre-registro npm 2026-10-02 — capa ACO-A en software libre

**Pre-registro:** [`../preregistro/PREREGISTRO_NPM_2026-10-02.md`](../preregistro/PREREGISTRO_NPM_2026-10-02.md)
(commit `3ff9fca`, subido antes de descargar cualquier dato de análisis).
**Rama:** `claude/charming-brown-w9h8iu` · **Base:** `main` en `4cdee3b`.

Aplicación independiente de la capa ACO-A a un dominio nuevo, **fuera del corpus de
721 casos**. No modifica el corpus ni ninguna cifra publicada.

Scripts: `code/npm_cohorte_aco.py` (construcción, con log) y `code/npm_pruebas_aco.py`
(las tres pruebas, con log). Cohorte: `data/npm_cohorte_aco.csv.gz`
(SHA-256 `c4bfbf05…`, 450 paquetes). Bandas: `data/npm_hazard_bandas.csv`.

## Tabla de decisiones

| Punto | Hipótesis | Resultado principal | Decisión pre-registrada |
|---|---|---|---|
| **1a.** Positividad del hazard | Toda banda de edad con ≥ 30 en riesgo tiene fines | 8 de 11 bandas con fines; las bandas 8, 9 y 10 años (n = 106, 71, 32) no tienen ninguno | **NO RESPALDADA** |
| **1b.** Forma del hazard | El hazard crece con la edad (afirmación v30) | Spearman(edad, h) = **−0.716**; p 1 cola = 0.99; **p 2 colas = 0.013** | **NO RESPALDADA**, y significativamente **decreciente** |
| **2.** Ortogonalidad b ⊥ Δ | IC 95% de ρ dentro de [−0.3, +0.3] | 450 pares: ρ = **+0.114**, IC **[+0.016, +0.209]** | **RESPALDADA** (equivalencia) |
| **3.** Abrupto contra anunciado | Δ mayor en magnitud en los abruptos | La regla selecciona **1 solo caso abrupto** | **NO EVALUABLE** |

---

## 0. Construcción de la cohorte y atrición

Del marco de **4,446,361** paquetes se tomó una de cada 370 filas (muestreo
sistemático, semilla 20261002, desplazamiento 172) → **12,017 nombres**.

| Paso | Caen | Quedan |
|---|---:|---:|
| Muestreados | — | 12,017 |
| Sin metadatos recuperables | 23 | 11,994 |
| Nacidos fuera de 2015-07-01 .. 2024-10-02 | 3,940 | 8,054 |
| Despublicados | 2 | **8,052** |
| Sin serie de descargas | 0 | 8,052 |
| **< 1,000 descargas en los primeros 180 días** | **6,618** | 1,434 |
| Serie con < 24 meses | 1 | 1,433 |
| Máximo a menos de 6 meses de algún extremo | 884 | 549 |
| Ajuste imposible (< 6 puntos útiles) | 99 | **450** |

**El filtro dominante es el de actividad: elimina el 82% de los candidatos.** Es el
precio de muestrear al azar en un registro donde la enorme mayoría de los paquetes
no tiene uso real. Está fijado de antemano y sobre una ventana temprana, así que no
condiciona el resultado, pero sí define la población: **la cohorte son paquetes que
arrancaron con uso apreciable**, no paquetes cualesquiera.

**Extinciones funcionales: 41 de 450 (9.1%).**

### Composición por fricción a priori — inservible en esta cohorte

| Fricción | Criterio | n |
|---|---|---:|
| nula (0) | usuario individual o sin repositorio | 139 |
| baja (1) | cualquier otra organización | 308 |
| media (2) | organización corporativa de la lista | **3** |
| alta (3) | organización de fundación de la lista | **0** |

Un muestreo aleatorio del registro completo está dominado por la cola larga: no cayó
**ni un solo** paquete de fundación y apenas tres corporativos. La codificación de
fricción, que el pre-registro ya declaraba **solo descriptiva**, no da aquí ninguna
información aprovechable. Para usarla haría falta un marco de muestreo distinto
(por ejemplo, estratificado por organización), y eso sería otro pre-registro.

---

## 1. Hazard h(τ)

| Banda (años) | En riesgo | Fines | h (por año) |
|---:|---:|---:|---:|
| 0 | 450 | 16 | **0.0356** |
| 1 | 434 | 7 | 0.0161 |
| 2 | 426 | 4 | 0.0094 |
| 3 | 395 | 4 | 0.0101 |
| 4 | 330 | 3 | 0.0091 |
| 5 | 291 | 1 | 0.0034 |
| 6 | 232 | 4 | 0.0172 |
| 7 | 160 | 2 | 0.0125 |
| 8 | 106 | **0** | 0.0000 |
| 9 | 71 | **0** | 0.0000 |
| 10 | 32 | **0** | 0.0000 |
| 11 | 7 | 0 | — (n < 30) |

**1a. Positividad: no respaldada.** Tres bandas con ≥ 30 en riesgo no tienen ningún
fin. Sus cotas superiores (3/n) son 0.028, 0.042 y 0.094 por año: **no demuestran
que el hazard sea cero**, solo que si es positivo es pequeño y esta cohorte no tiene
potencia para detectarlo. Tal como la regla pre-registrada lo define, la hipótesis
no se respalda.

**1b. Forma: no respaldada, y el signo es el contrario.** El hazard **decrece** con
la edad, de 0.036 en el primer año a 0.003 en el sexto, con un repunte menor en el
sexto y séptimo. Spearman(edad, h) = −0.716, significativo a dos colas (p = 0.013).
Es una forma de **mortalidad infantil**: el riesgo se concentra al principio.

### La afirmación de la v30 queda en tres formas distintas

| Cohorte | n | Forma | ρ(edad, h) |
|---|---:|---|---:|
| Cripto (Binance) | 663 | Creciente, **confundida con el calendario** | +0.881 (p = 0.002) |
| Bancos (FDIC) | 27,771 | **Bañera** | +0.050 (p = 0.38) |
| **Paquetes (npm)** | **450** | **Decreciente** (mortalidad infantil) | **−0.716** (p = 0.013 a dos colas) |

Tres dominios, tres formas. **La afirmación de la v30 de que el hazard crece con la
edad no se sostiene en ningún dominio salvo cripto, donde está confundida con el
mercado bajista de 2022–2025.** La lectura del repositorio —que la forma del hazard
es dominio-dependiente— sale reforzada; lo que queda es que h > 0 en el grueso del
rango de edades, no que crezca.

### Salvedad principal: censura por la derecha en las bandas altas

Las bandas 8 a 10 son las de los paquetes nacidos en 2015–2018, y su exposición a
esas edades ocurre justamente en los años recientes. Dos efectos se suman ahí:

1. **El criterio de extinción necesita 6 meses consecutivos** bajo el 1% del máximo,
   así que un paquete que muera en el último medio año antes del corte **no se
   registra**. Eso recorta fines recientes, que son los que poblarían las bandas altas.
2. Las extinciones observadas se concentran en 2023 (8) y 2024 (8) de un total de 41,
   lo que indica que el proceso está lejos de ser estacionario.

El cero de esas tres bandas **no debe leerse como "los paquetes viejos no mueren"**.
Separar edad de periodo requiere un modelo edad-periodo-cohorte, igual que en cripto,
y queda declarado pendiente.

**Año calendario de las 41 extinciones:** 2015: 2 · 2016: 3 · 2017: 1 · 2018: 1 ·
2019: 4 · 2020: 3 · 2021: 5 · 2022: 3 · 2023: 8 · 2024: 8 · 2025: 3.

---

## 2. Ortogonalidad b ⊥ Δ — **respaldada**

| | Cripto (v2.6.0) | **npm (nuevo)** |
|---|---:|---:|
| Pares | 242 | **450** |
| Spearman ρ | −0.119 (p = 0.065) | **+0.114 (p = 0.016)** |
| IC 95% (Fisher) | [−0.241, +0.007] | **[+0.016, +0.209]** |
| Pearson r | −0.103 (p = 0.11) | +0.099 (p = 0.035) |
| Parcial, controlando el tamaño | — | +0.071 |
| Decisión | Respaldada | **Respaldada** |

Distribuciones: b_subida mediana **+0.516** (rango −1.03 a +4.34); Δ_caída mediana
**−0.808** (rango −3.17 a −0.05).

**Lo más informativo no es que el IC entre en la banda, sino que el signo no coincide
entre dominios.** En cripto la asociación era ligeramente negativa (−0.119), aquí es
ligeramente positiva (+0.114), y ambas caen dentro de ±0.3. Dos dominios con relojes,
sustratos y mecanismos distintos dan asociaciones pequeñas y de signo opuesto: es
justo lo que se espera si **no existe relación real** entre la velocidad de subida y
la forma de la caída.

Con 450 pares el ρ = +0.114 alcanza significancia nominal (p = 0.016), pero eso mide
que no es exactamente cero, no que sea grande: controlando el tamaño del paquete baja
a +0.071. **RC9 queda no refutado por segunda vez, ahora fuera de cripto.**

---

## 3. Modos de colapso — **no evaluable**

| Clase | n |
|---|---:|
| Abrupto (aviso OSV con CVSS ≥ 7.0 en [pico−3, pico+6] meses) | **1** |
| Anunciado (campo `deprecated`, sin aviso grave en la ventana) | 33 |
| Sin clasificar | 416 |

Con **un solo caso abrupto** no hay emparejamiento 1:1 ni prueba de Wilcoxon posible.

**No se sustituyó la regla ni se amplió la ventana.** Cambiar el criterio después de
ver que selecciona un caso sería elegirlo en función de los datos, que es exactamente
lo que el pre-registro existe para impedir. La prueba queda **no evaluable en esta
cohorte** y la taxonomía de modos de colapso sigue sin una prueba de n grande.

**Por qué falló el diseño, para el próximo intento:** los paquetes con vulnerabilidad
crítica son raros en la cola larga del registro, y la ventana de ±pocos meses alrededor
del máximo es estrecha. Un marco de muestreo **estratificado por presencia de aviso en
OSV** —muestrear a propósito paquetes con y sin vulnerabilidad grave, emparejados—
daría n suficiente. Eso es otro pre-registro, no un ajuste de este.

### Descriptivos (sin valor inferencial, con n = 1 en una celda)

| Clase | n | Δ mediana | R² mediano de la caída |
|---|---:|---:|---:|
| Abrupto | 1 | −0.851 | 0.421 |
| Anunciado | 33 | −1.079 | 0.586 |
| Sin clasificar | 416 | −0.786 | 0.518 |

**Candidatos a "Detenido en Piso":** 265 de 450 (58.9%) tienen el mínimo posterior al
máximo por encima del 1% de ese máximo. La mayoría de los paquetes que caen **no caen
a cero**: se estabilizan en un piso de uso residual, coherente con el modo descrito en
la taxonomía. Es descriptivo, no una prueba.

---

## Desviaciones respecto al pre-registro

1. **Severidad del aviso.** El pre-registro decía "CVSS ≥ 7.0". Se usa como criterio
   primario la **etiqueta de severidad** que OSV replica de GitHub (`HIGH` o
   `CRITICAL`), que por definición corresponde a CVSS ≥ 7.0, y el cálculo del vector
   queda como respaldo cuando la etiqueta falta. Es la misma regla, implementada con
   la fuente más fiable.
2. **Mes del corte.** El pre-registro no fijaba qué hacer con el mes en curso, que
   está incompleto. Se descarta en la agregación mensual.
3. **Ventanas de descarga.** El pre-registro anotaba un límite de 18 meses por
   petición, verificado sobre un paquete. En consultas **en lote** el límite real son
   **365 días** (`exceeded max days of 365 for bulk query`). Se usan dos rejillas: 365
   días para los lotes y 18 meses para los individuales. No afecta los datos
   obtenidos, solo cómo se piden.
4. **Bandas de edad sin mínimo declarado para la forma.** H1b se calcula sobre las
   bandas con ≥ 30 en riesgo, el mismo umbral que H1a; el pre-registro solo lo fijaba
   para H1a.

### Incidente de la primera corrida completa

La primera corrida terminó y produjo una cohorte de **249 paquetes, todos scoped**:
los 5,444 paquetes planos quedaron sin serie. La causa fue la desviación 3 —ventanas
de 18 meses en consultas en lote— combinada con que el código trataba el **HTTP 400
como respuesta vacía sin registrarlo**, de modo que 344 lotes fallaron sin dejar
rastro en el log. Ese resultado **se descartó por completo** y no se reporta aquí. El
código ahora registra todo 400 con el cuerpo de la respuesta. Queda anotado porque un
fallo silencioso que casi produce un resultado falso es parte del registro honesto de
esta prueba.

---

## Lectura

**Lo que aporta esta prueba al repositorio:**

1. **RC9 (ortogonalidad) deja de depender de un solo dominio y un solo ciclo de
   mercado.** 450 pares de un sustrato completamente distinto, con asociación pequeña
   y de signo opuesto a la de cripto. Es la réplica cruzada que la hoja de ruta pedía.
2. **La afirmación "el hazard crece con la edad" queda sin respaldo en tres de tres
   dominios** salvo el caso confundido de cripto. Aquí sale incluso decreciente y
   significativo a dos colas.
3. **La positividad estricta de h(τ) falla en las bandas altas**, igual que en los
   bancos de la FDIC. Dos cohortes de dos dominios con el mismo patrón: la versión
   fuerte de "ningún sistema es eterno" —h > 0 en **toda** banda de edad— no se
   sostiene con estos datos; la versión débil —fines en el grueso del rango— sí.
4. **La taxonomía de modos de colapso sigue sin prueba de n grande.** Era el objetivo
   más ambicioso de este pre-registro y el diseño no alcanzó para probarla.

**Lo que no aporta:** nada sobre fricción, porque el muestreo aleatorio no produjo
paquetes de fundación ni prácticamente corporativos. Y nada sobre satelización (el eje
b como razón hub/nodo): esta prueba mide los dos ejes de ACO-A sobre la trayectoria
propia de cada paquete, igual que la prueba cripto, no sobre un par hub–nodo.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
