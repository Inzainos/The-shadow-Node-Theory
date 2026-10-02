# Auditoría — todas las afirmaciones de la ronda 2026-10-02 contra la regla por dominio

**Motivo:** el autor detuvo el trabajo al advertir que el marco teórico establece que
**cada dominio tiene sus propios valores, y cada área dentro de un dominio también, y
cada una es independiente.** Una de las pruebas de esta ronda —la deriva del exponente
contra la fricción— violó esa regla. Esta auditoría revisa **todas** las afirmaciones
de la ronda, no solo la señalada.

## 0. La regla, citada del marco

**Axioma 0.1** (`papers/marco_teorico.md:110`):

> *"Esa lectura tiene un precio explícito: obliga a que **cada eje tenga definición
> operativa por dominio**. Un eje sin definición operativa en un dominio no se grafica,
> no se interpreta y **no entra en ningún ajuste para ese dominio**."*

Y en el mismo axioma: *"`m` está definido: es `R` con el **proxy declarado de cada
dominio**."*

**Axioma 2** (`papers/marco_teorico.md:163`):

> *"Cada sistema recorta el fondo del Axioma 0 como una cavidad... y responde con
> **modos propios, no con una frecuencia universal idéntica para todo**. ... Schumann
> es un modo del telar, no el lienzo."*

**Axioma 9:** *"En lugar de una cúspide única, se asume un paisaje con **múltiples
óptimos locales**."*

## 0.1 Evidencia previa que se debió citar y no se citó

La nota de auditoría del **Axioma 5, punto 3** ya registraba que el ordenamiento de
dominios por fricción **había sido probado y había fallado**:

> *"Prueba pre-registrada con dominios nuevos (2026-09-27; hipótesis y codificación de
> fricción fijadas antes de ver los datos). Con 7 dominios sin COVID, ρ(fricción,
> b̄ del dominio) = −0.131, p por permutación exacta = 0.39: **no respaldada**. ...
> **entre fricción baja, media y alta no aparece ningún orden**."*

Y falló en las cinco variantes (`data/friccion_dominios_nuevos_resumen.csv`):
−0.131, −0.430, +0.112, −0.581, +0.049 — **NO RESPALDADA** en todas.

Además, el dominio digital **ya estaba en ese eje**: el encabezado de
`code/prueba_friccion_dominios_nuevos.py` lo declara como *"D2 cuotas digitales —
baja (1). StatCounter mundial mensual 2009-01..2024-12"*. La afirmación de que faltaba
ubicarlo era **falsa**, y la ubicación a priori que se fijó en el pre-registro de la
deriva (≈ 0) contradice la que el repositorio ya tenía (1) sin decirlo.

---

## 1. La distinción que decide cada caso

No toda mención de dos dominios es una violación. Lo que la regla prohíbe es un tipo
concreto de inferencia:

**Permitido entre dominios:**

1. **Réplica independiente** de una prueba hecha dentro de un dominio, con su propio
   proxy y su propio nulo. No se agrupa nada; se repite el procedimiento y se compara
   el veredicto.
2. **Refutación de una afirmación universal** por un contraejemplo. Si la teoría dice
   "para todo sistema", un dominio que falle la refuta. Eso es lógica, no agrupamiento.
3. **Conteo de resultados independientes** sin convertirlos en un estadístico único
   ("gana en 5 de 6 niveles" como tally, nunca como una prueba con n = 6).

**Prohibido:**

4. **Ordenar dominios en una escala compartida** y esperar una ley común. Es lo que
   hizo la prueba de fricción del 2026-09-27 (y falló) y lo que repitió la prueba de
   deriva de esta ronda sobre otra cantidad.
5. **Leer la diferencia entre dominios como medición** de la variable que los
   distingue. Dos cavidades con proxies distintos difieren por construcción; esa
   diferencia no mide la variable que uno eligió para etiquetarlas.

---

## 2. Veredicto por afirmación

### 2.1 Capa ACO-A en npm — `RESULTADOS_NPM_2026-10-02.md`

| Afirmación | Tipo | Veredicto |
|---|---|---|
| Positividad del hazard **no respaldada** (3 bandas sin fines) | Dentro de npm | **VÁLIDA** |
| Hazard **decreciente**, ρ = −0.716, p = 0.013 (11 bandas) | Dentro de npm | **VÁLIDA** |
| "La afirmación de un hazard universalmente creciente no se sostiene" | Refutación de universal por contraejemplo (permitido 2) | **VÁLIDA** |
| Ortogonalidad b ⊥ Δ **respaldada**, ρ = +0.114, IC [+0.016, +0.209] | Dentro de npm, 450 pares | **VÁLIDA** |
| "RC9 deja de depender de un solo dominio" | Réplica independiente (permitido 1) | **VÁLIDA** |
| "El signo no coincide entre dominios... dos dominios con relojes, sustratos y mecanismos distintos" | Comparación de dos réplicas independientes, y el texto **ya razona por dominio** | **VÁLIDA** |
| Fricción a priori degenerada (0 fundación, 3 corporativos) | Dentro de npm | **VÁLIDA** |

**Sin cambios.** Este bloque se construyó por dominio desde el principio.

### 2.2 Réplica internacional del rango-tamaño — `RESULTADOS_RANGO_TAMANO_2026-10-02.md`

| Afirmación | Tipo | Veredicto |
|---|---|---|
| ΔAIC por nivel, cada uno ajustado aparte | Dentro de cada nivel | **VÁLIDA** |
| Curva de poder por nivel, con los parámetros de ese nivel | Dentro de cada nivel | **VÁLIDA** |
| "La lognormal gana en 5 de 6 niveles" | Conteo de resultados independientes (permitido 3) | **VÁLIDA** como tally. **No** es una prueba con n = 6, y el informe no la usa como tal |
| "La prueba de Clauset no alcanza poder a ningún n de este diseño" | Conteo de resultados independientes por nivel | **VÁLIDA** |
| Brasil top-1,327 contra UE NUTS3: mismo n, mismo rango, misma σ, mismo b, veredictos opuestos | Comparación entre cavidades | **VÁLIDA, y refuerza la regla.** La conclusión fue que la forma **no** es invariante, es decir que cada sistema responde con sus propios modos. Es exactamente lo que el Axioma 2 predice |
| "Hay que matizar la afirmación de invariancia" | Consecuencia de lo anterior | **VÁLIDA** |
| Diagnóstico A/B/C de n contra rango | **Dentro** de Brasil municipios | **VÁLIDA** |

**Sin cambios.** Paradójicamente, este bloque es el que más apoya la regla por dominio.

### 2.3 Valor puntual del Dominio B — `RESULTADOS_DOMINIO_B_PUNTUAL_2026-10-02.md`

Entero dentro de un solo dominio, con un solo proxy: 12 métodos, calibración por
simulación con la terna `(n, ρ, σ)` de casos reales **de ese dominio**, valor puntual
declarado indecidible.

**VÁLIDO sin cambios.** Cero afirmaciones entre dominios.

### 2.4 Deriva del exponente — `RESULTADOS_DERIVA_FORMA_2026-10-02.md`

| Afirmación | Tipo | Veredicto |
|---|---|---|
| **"Dominio B 10.1% − Cripto 55.5% = −45.4 puntos" como prueba de fricción** | **Ordenar cavidades en una escala compartida (prohibido 4 y 5)** | **SE RETIRA** |
| Framing de npm como "control de fricción cero" | Depende de la ubicación en la escala, que es inadmisible y además contradice la codificación del repo | **SE RETIRA** |
| Dominio B: 10.1% descendente contra 11.9% ascendente, poder 31.7% → `b` constante | Dentro de un dominio, contra su propio nulo | **VÁLIDA** |
| Cripto: 55.5% descendente, y el artefacto de listado (70.1% con pico en su primer 10%; 57.5% contra **0.0%** al partir) | Dentro de un dominio; el artefacto es propiedad de esa fuente | **VÁLIDA** |
| npm: 14.9% contra 10.4%, poder 6.7% | Dentro de un dominio | **VÁLIDA, y no informa nada** |
| "El cruce de `b = 1` no ocurre" como enunciado general | Mezcla tres cavidades en una frase | **SE REFORMULA** a tres enunciados por dominio: 0.0% en B, 0.4% en cripto, 9.6% en npm |
| Nulo por caso: 4.7% de falso positivo a ρ = 0.94 | Herramienta, por caso | **VÁLIDA** |

### 2.5 `CASOS_DE_USO.md`

| Fila de la tabla §4 | Veredicto |
|---|---|
| Ortogonalidad respaldada en npm | **VÁLIDA** (réplica) |
| Hazard creciente no sobrevive — "tercer dominio, tercera forma" | **VÁLIDA** (refutación de universal, y la frase ya es por dominio) |
| Positividad del hazard no respaldada | **VÁLIDA** |
| Apego preferencial retirado y reforzado | **VÁLIDA** (tally) |
| Invariancia de la forma hay que matizarla | **VÁLIDA** (es la regla afirmándose) |
| Gradiente de Tlaxcala sin cambio | **VÁLIDA** |

**Sin cambios en las filas.** Se añade la regla como sexto criterio de admisión para
casos de uso nuevos.

---

## 3. Resumen del daño

| Bloque | Afirmaciones | Se retiran | Se reformulan | Sobreviven |
|---|---:|---:|---:|---:|
| npm ACO-A | 7 | 0 | 0 | **7** |
| Rango-tamaño internacional | 7 | 0 | 0 | **7** |
| Valor puntual del Dominio B | todas | 0 | 0 | **todas** |
| Deriva del exponente | 7 | **2** | **1** | 4 |
| `CASOS_DE_USO.md` §4 | 6 | 0 | 0 | **6** |

**Se retiran dos afirmaciones, se reformula una, y el resto del trabajo de la ronda se
sostiene.** La razón no es suerte: los otros tres bloques se construyeron como pruebas
independientes por dominio, con nulo por dominio, que es justo lo que la regla exige.
El bloque que falla es el único que se diseñó como contraste **entre** cavidades.

## 4. Lo que el autor señaló y cómo se formula bien

El autor sostiene que **el dominio digital es especial porque sus cambios de fase
tienden a ser más abruptos**. Bajo la regla por dominio eso **no** es una posición en
una escala universal de fricción: es una propiedad de los **modos propios de esa
cavidad** (Axioma 2).

Formulación admisible, para la prueba siguiente:

> Dentro del dominio digital, y contra su propio nulo, las transiciones de fase son más
> abruptas de lo que su propio nulo produce.

Eso se mide **sin comparar con ningún otro dominio**: se define abruptez sobre la serie
cruda de ese dominio, se simula el nulo con la estructura de ruido de ese dominio, y se
contrasta. Si el mismo procedimiento se repite después en otro dominio, es **réplica
independiente** (permitido 1), no ordenamiento.

## 5. Causa de raíz del error, para que no se repita

El pre-registro de la deriva se escribió **antes** de leer el marco teórico y **antes**
de revisar los logs y los informes de las pruebas anteriores del repositorio. Si el
orden hubiera sido el inverso, el Axioma 0.1 y la nota del Axioma 5 habrían bastado
para descartar el diseño entre dominios desde la primera línea.

Queda como regla de operación: **antes de pre-registrar, leer el marco y los
resultados previos del eje que se va a tocar.**

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
