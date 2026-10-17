# Pre-registro — eje `u`: ¿la entropía condicional de transiciones admite "apertura de posibilidades" como coordenada?

**Fecha:** 2026-10-17 · **Rama:** `local/preregistro-eje-u-v2.6.1` · **Base:**
`main` en `368e4b6` · **Autor de la teoría:** Elán Zainos Corona · **Análisis:**
Copilot, a pedido del autor.

Este documento se compromete antes de calcular una entropía, resumen o correlación
del candidato `u`. El commit fechado fija el diseño. Cualquier cambio posterior se
anota en la sección **Desviaciones** del informe de resultados, con motivo, y nunca
en silencio.

## 0. El pendiente, exactamente

El Axioma 0.1 define `𝒞(u, m, τ)`, donde `u` es apertura de posibilidades o
incertidumbre. Hoy `m` es `R` con el proxy declarado de cada dominio y `τ` es la fase
temporal normalizada, pero `u` no tiene definición operativa en ningún dominio.

Este pre-registro no instala una proxy por decreto. Prueba un candidato acotado:

> **`u^H(t)` = número efectivo de estados sucesores empíricamente accesibles, dado el
> estado reciente de una serie `R(t)`.**

`u^H` mide diversidad condicional de transiciones observadas. No mide alternativas
no observadas, libertad ontológica ni causalidad. Solo puede llamarse definición
operativa de `u` si pasa las compuertas de admisión de este documento en dos dominios
independientes. Si no las pasa, conserva el nombre descriptivo de *entropía
condicional de transiciones* y el eje `u` sigue vacío.

La prueba no propone relación direccional entre `u^H` y `m`, `τ`, `b`, `Δ` o `φ`.
No usa `b`, `Δ`, fricción, modos de colapso ni etiquetas de resultado para construir
el descriptor.

## 0.1 Ceguera declarada

El analista revisó los esquemas de los archivos, sus rutas, los cargadores existentes
del Dominio B y de cripto, y resultados ya publicados de otras pruebas del repositorio.
No calculó ni inspeccionó valores, resúmenes, gráficos, correlaciones o trayectorias
de `u^H`, de sus incrementos discretizados, ni de las compuertas definidas abajo.

## 0.2 Reglas generales

1. **Se reporta todo resultado**, incluida la no admisión de `u^H`.
2. **Sin descargas.** Solo se usan archivos versionados al momento de este commit.
3. **Sin imputación.** Valores faltantes, ceros no positivos, series cortas y empates
   que impidan formar estados se excluyen con motivo y se cuentan.
4. **Sin aleatoriedad.** El cálculo es determinista; no se añaden bootstrap,
   simulaciones ni ajustes posteriores sin una adenda pre-registrada.
5. **Por dominio.** Dominio B y cripto se evalúan por separado. No se promedian,
   ordenan ni convierten en un estadístico entre dominios.
6. **Proyección explícita.** Cada cálculo declara `θ = (B, V, ρ, W, λ)` como exige
   el Axioma 0.2.
7. **Log obligatorio.** El script deja un log en `reconstruction_real/logs/` y
   registra los SHA-256 de sus entradas y salidas.

## 1. Dominios y datos fijados

Ambos brazos son cocientes positivos, por lo que comparten una construcción de
`R(t)` sin convertir niveles y cocientes en la misma cosa.

| Dominio | Casos | `R(t)` | Archivos fijados | Inclusión mínima |
|---|---:|---|---|---:|
| **B — pares de países** | pares publicados | PIBpc_hub / PIBpc_nodo | `data/maddison_mpd2020.csv`, `reconstruction_real/data/by_domain/dominio_B_real.csv` | 40 años comunes entre 1900 y 2018 |
| **Cripto — moneda/BTC** | pares Binance | cierre_moneda / cierre_BTCUSDT | `data/binance_cierres_diarios.csv.gz` | 200 días comunes con BTCUSDT |

### Dominio B

Se reconstruye cada par publicado exactamente como `calc()` de
`expand_B_massive.py`: años comunes, 1900--2018, `R = PIBpc_hub / PIBpc_nodo`.
Antes de calcular `u^H`, el script verifica que la pendiente global reproduce `b`
publicada con `|Δb| <= 1e-4`. Si una serie no reproduce, queda fuera de este análisis
con ese motivo; no se modifica ni se reestima el corpus.

### Cripto

Se reutiliza la regla publicada en `deriva_forma_friccion.py`: BTCUSDT es el hub,
cada par distinto de BTCUSDT es el nodo, y solo se usan cierres diarios positivos en
fechas comunes. No se descargan pares, no se reordenan fechas y no se usa volumen,
capitalización, listados, fricción ni el pico de precio.

## 2. Construcción del candidato `u^H`

Para cada serie elegible:

```text
x_t = log(R_t)
d_t = x_t - x_(t-1)
```

`x_t` es la magnitud logarítmica observada y `d_t` la transición cruda entre
observaciones consecutivas. Los cortes de estado se fijan retrospectivamente con la
serie completa disponible; por tanto `u^H` no es un estimador en tiempo real ni una
prueba de pronóstico. Una vez fijado ese vocabulario, la frecuencia condicional en
una posición `t` cuenta solo transiciones ya ocurridas y nunca `d_(t+1)`.

### Proyección primaria: `θ1`

| Componente | Definición |
|---|---|
| `B` | Serie del cociente `R(t)` |
| `V` | Incremento de un paso `d_t` |
| `ρ` | Tres estados por los terciles empíricos de `d_t`, con `numpy.quantile(..., method="linear")` |
| `W` | Las 12 transiciones históricas más recientes que parten del mismo estado actual |
| `λ` | Se requieren las 12 transiciones; de otro modo `u^H_t` es faltante |

Si `q1` y `q2` son esos terciles, `S_t = -1` si `d_t <= q1`, `S_t = 0` si
`q1 < d_t <= q2`, y `S_t = +1` si `d_t > q2`. Para cada posición válida se toman las
últimas 12 transiciones históricas `(S_j, S_(j+1))` cuyo origen cumple `S_j = S_t`.
Si `p_(t,k)` es la frecuencia del estado sucesor `k` en esas 12 transiciones:

```text
H_t = -Σ_k p_(t,k) log(p_(t,k))
h_t = H_t / log(3)
u^H_t = exp(H_t)
```

`h_t` es la entropía normalizada en `[0, 1]`; `u^H_t` es el número efectivo de
estados sucesores, entre 1 y 3. Si los cortes producen menos de tres estados no
vacíos, el caso no es elegible para `θ1`.

### Proyección de invarianza: `θ2`

| Componente | Definición |
|---|---|
| `B` | Misma serie del cociente `R(t)` |
| `V` | Cambio de dos pasos `g_t = x_t - x_(t-2)` |
| `ρ` | Cinco estados por los quintiles empíricos de `g_t`, con interpolación lineal y cortes cerrados a la derecha |
| `W` | Las 20 transiciones históricas más recientes que parten del mismo estado actual |
| `λ` | Se requieren las 20 transiciones; de otro modo el valor es faltante |

La fórmula es la misma, sustituyendo `k = 1..5`; para comparar proyecciones se usa
solo la entropía normalizada `h_t = H_t / log(5)`. Si los cortes producen menos de
cinco estados no vacíos, el caso no es elegible para `θ2`.

Si `q1, q2, q3, q4` son los quintiles de `g_t`, los estados son, en orden:
`g_t <= q1`, `q1 < g_t <= q2`, `q2 < g_t <= q3`, `q3 < g_t <= q4` y `g_t > q4`.

`θ1` y `θ2` difieren en `V`, `ρ`, `W` y `λ`; no son el mismo corte con otra escala.
Las posiciones temporales se alinean por el índice original de la serie. Un caso
requiere al menos 12 posiciones comunes con `h_t` finita en ambas proyecciones para
entrar a la prueba de invarianza.

## 3. Compuertas de admisión

Estas reglas se aplican por separado en B y cripto.

### A. Cobertura

Un dominio solo se evalúa si al menos 30 casos cumplen todos los requisitos de datos
y producen las 12 posiciones comunes entre `θ1` y `θ2`. Si no los alcanza, el
dominio se declara **sin cobertura suficiente**, no negativo.

### B. Invarianza de proyección

Para cada caso se calcula Spearman entre sus `h_t` de `θ1` y `θ2` en posiciones
comunes. El dominio pasa esta compuerta solo si:

1. la mediana de esas correlaciones es `>= 0.60`, y
2. al menos dos tercios de los casos tienen correlación `>= 0.30`.

Una Spearman indefinida por una serie constante se registra como no evaluable y no
cuenta como cumplimiento. La mediana solo se calcula si al menos 90% de los casos
elegibles son evaluables; si no, la compuerta falla.

Si falla, el candidato depende del corte y no define un eje observable estable.

### C. Variación efectiva

Para cada caso se calcula el rango intercuartílico de `h_t` bajo `θ1`. El dominio
pasa solo si la mediana de los IQR es `>= 0.05`. Un descriptor esencialmente
constante no añade una coordenada temporal.

### D. No colapso a magnitud o dispersión

Para cada posición de `θ1` se calculan:

- `m_t = x_t`, la magnitud logarítmica observada;
- `v_t`, la desviación absoluta mediana de los incrementos de las 12 transiciones
  históricas que forman su `W`.

Por caso se calculan `|Spearman(h_t, m_t)|` y `|Spearman(h_t, v_t)|`. El dominio
falla esta compuerta si, en 75% o más de sus casos, alguna de las dos correlaciones
es `>= 0.90`. En ese desenlace `u^H` se reporta como transformación casi monótona de
magnitud o dispersión, no como coordenada adicional. Una correlación indefinida se
registra como no evaluable; la compuerta falla si menos de 90% de los casos elegibles
es evaluable para ambas comparaciones.

## 4. Decisión pre-especificada

| Resultado | Decisión |
|---|---|
| B y cripto pasan A--D | `u^H` queda admitido como **definición operativa candidata** de `u` en dos dominios. Solo entonces puede entrar como coordenada de `𝒞` en análisis posteriores. |
| Solo un dominio pasa A--D | `u^H` queda como descriptor de ese dominio; por la regla de admisión del Axioma 0.1 no entra a `𝒞`. |
| Ningún dominio pasa o falta cobertura | El eje `u` sigue sin definición operativa. No se sustituye por otra proxy en esta corrida. |
| Alguna compuerta muestra dependencia de la proyección, magnitud o dispersión | Se conserva el resultado descriptivo, pero se rechaza la interpretación de apertura de posibilidades. |

No se publican p-valores, causalidad ni una comparación B contra cripto. El requisito de
dos dominios es una regla de admisión de eje, no una prueba agrupada.

## 5. Salidas previstas

- `reconstruction_real/code/eje_u_transiciones.py`, con log y sin llamadas de red.
- `reconstruction_real/data/eje_u_transiciones_por_caso.csv`: elegibilidad, cobertura,
  invarianza, IQR y diagnósticos de no colapso por caso.
- `reconstruction_real/data/eje_u_transiciones_resumen.csv`: una fila por dominio y
  compuerta, sin estadístico combinado.
- `reconstruction_real/audits/RESULTADOS_EJE_U_TRANSICIONES_2026-10-17.md`, con tabla
  diseño → resultado → decisión y sección **Desviaciones**.

`papers/marco_teorico.md` no cambia antes de la corrida ni cambia si el candidato no
supera las compuertas. El resultado se integra al marco solo después de publicar las
salidas, su procedencia y la auditoría correspondiente.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-17*
