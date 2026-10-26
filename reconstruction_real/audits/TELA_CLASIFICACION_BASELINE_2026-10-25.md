# Tela integrada v2 — línea base, exactitud balanceada, permutación y leave-one-domain-out

**Fecha:** 2026-10-25 · **Script:** [`../code/tela_clasificacion_baseline.py`](../code/tela_clasificacion_baseline.py)
· **Semilla:** 20261025 · **Permutaciones:** 5 000 · **Determinista:** sí.

**Salidas:** `data/tela_clasificacion_baseline.csv`, `data/tela_clasificacion_lodo.csv`,
`data/tela_clasificacion_lodo_resumen.csv`.

**Cómo regenerar** (≈2,5 min):

```sh
python reconstruction_real/code/tela_clasificacion_baseline.py
```

## Por qué existe

[`TELA_V2_INTEGRADA_2026-10-21.md`](TELA_V2_INTEGRADA_2026-10-21.md) reporta la
exactitud leave-one-out (LOO) por centroide: 50,7 % por dominio y 66,2 % por
tono φ. Ese informe ya advierte que no es un clasificador calibrado, pero no
compara contra ninguna referencia. En un corpus donde B aporta 446 de 740
trayectorias, la referencia importa. Esta auditoría agrega cuatro cosas, sin
modificar `tela_cimatica.py`:

1. línea base mayoritaria (siempre predecir la clase más frecuente);
2. exactitud balanceada (recall medio por clase);
3. nulo de permutación de etiquetas;
4. leave-one-domain-out (LODO) para el tono φ.

**Control de consistencia:** la implementación vectorizada reproduce al
decimal las cuatro cifras publicadas (50,7 / 41,9 / 66,2 / 58,6 %) y coincide
con `tela_cimatica.clasificacion_loo` con tolerancia 1e-12.

## Resultados (todos los casos)

| Tarea | Rasgos | n eval | Exactitud | Línea base mayoritaria | Balanceada | Azar balanceada | Nulo filas (bal., media) | p perm. filas | Nulo dominios (bal., media) | p perm. dominios |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Dominio | todos | 737 | 50,7 % | **60,5 %** | 55,6 % | 11,1 % | 7,3 % | 0,0002 | n/a | n/a |
| Dominio | solo-forma | 737 | 41,9 % | **60,5 %** | 51,7 % | 11,1 % | 7,3 % | 0,0002 | n/a | n/a |
| Tono φ | todos | 740 | 66,2 % | 63,8 % | 61,4 % | 20,0 % | 20,1 % | 0,0002 | 57,7 % | **0,39** |
| Tono φ | solo-forma | 740 | 58,6 % | **63,8 %** | 54,0 % | 20,0 % | 20,1 % | 0,0002 | 53,5 % | **0,49** |

`p` es unilateral superior con corrección (1 + k)/(1 + N). «Nulo filas» permuta
las etiquetas caso a caso; «nulo dominios» permuta la asignación tono ← dominio
entre los 12 dominios.

## Lectura

1. **Dominio.** La exactitud cruda (50,7 %) queda *por debajo* de la línea base
   mayoritaria (60,5 %). Sin embargo, la exactitud balanceada (55,6 %) es muy
   superior al azar (11,1 %) y al nulo de permutación (7,3 %; p = 0,0002). La
   forma de la trayectoria **sí contiene información de dominio**; lo que no
   corresponde es presentar 50,7 % como «mejor que el azar» sin la referencia.
   La información está concentrada: E3 acierta 219/234 (94 %), B 137/446 (31 %),
   ACO 4/18, C 3/24.
2. **Sin E3.** Al retirar el dominio cuya receta de selección fija el
   nacimiento de la trayectoria, la exactitud balanceada por dominio baja a
   52,3 % (todos) y 46,1 % (solo-forma), aún sobre el azar (12,5 %). No hay
   colapso, pero el 94 % de E3 no es una medida de dinámica.
3. **Tono φ.** La exactitud (66,2 %) supera a la línea base (63,8 %) por 2,4
   puntos, y en solo-forma queda por debajo (58,6 % frente a 63,8 %). El nulo
   por filas da p = 0,0002, pero **no es el nulo apropiado**: φ es constante
   dentro de cada dominio, por lo que permutar filas rompe esa estructura. Con
   el nulo por dominios, que sí la conserva, el resultado es
   indistinguible de asignar tonos al azar entre dominios (p = 0,39 todos los
   rasgos; p = 0,49 solo-forma). Un agrupamiento arbitrario de dominios en
   «tonos» da una exactitud balanceada media de 57,7 %. Es decir: la figura
   identifica el *dominio*, y el tono hereda esa identificación porque es una
   etiqueta de dominio. Esto no refuta φ; muestra que esta prueba no puede
   distinguirla de cualquier otra agrupación.

## Leave-one-domain-out (tono φ en un dominio no visto)

Cada dominio se retira completo; los centroides por tono se estiman solo con
los demás y la estandarización también. Se evalúan únicamente filas cuyo tono
existe en el entrenamiento (A y ACO quedan fuera: su tono —«media» y
«variable»— no aparece en ningún otro dominio).

| Rasgos | n eval | Exactitud | Azar uniforme | Balanceada | Azar balanceada | Nulo dominios (bal., media) | p perm. dominios (bal.) |
|---|---:|---:|---:|---:|---:|---:|---:|
| todos | 718 | 47,9 % | 20,0 % | 36,4 % | 33,3 % | 18,9 % | **0,13** |
| solo-forma | 718 | 38,9 % | 20,0 % | 31,9 % | 33,3 % | 18,9 % | **0,21** |

Por dominio retenido (todos los rasgos): B 253/446 (56,7 %), E3 79/234
(33,8 %), C 6/24, E1 3/4, E2 2/2, F1 1/2; D, F2, F3 y G no se acertaron (D 0/3,
F2 0/1, F3 0/1, G 0/1).

**Lectura.** La exactitud supera al azar uniforme (47,9 % frente a 20 %), pero
esa comparación es generosa: la exactitud balanceada (36,4 %) apenas rebasa el
azar balanceado (33,3 %) y no se distingue de asignaciones aleatorias de tono a
dominio (p = 0,13). La base mayoritaria del entrenamiento (3,6 %) no es una
referencia informativa aquí, porque al retener B o E3 la clase mayoritaria
restante es la contraria. La parte del acierto que existe viene de B (clasificado
como «alta» por su parecido con C, otra serie económica hub–nodo), lo que es
semejanza de familia de datos y no evidencia de fricción.

## Qué sobrevive y qué no

- **Sobrevive:** la forma de la trayectoria identifica el dominio por encima
  del azar balanceado, también sin E3 y sin τ = 0.
- **No sobrevive como afirmación:** que la figura «identifique el tono φ» más
  allá de lo que ya identifica el dominio. Con el nulo por dominios y con
  LODO, el resultado no se distingue del azar.
- **Cambio de reporte recomendado:** citar siempre exactitud, línea base
  mayoritaria y exactitud balanceada juntas; para φ, citar el resultado de
  LODO y el nulo por dominios, no el LOO por filas.

## Limitaciones

- La estandarización usa todos los casos del conjunto evaluado (igual que
  `tela_cimatica.py`), salvo en LODO.
- Con 12 dominios, el nulo por dominios tiene poca resolución; no puede
  detectar efectos pequeños.
- Los dominios F1–F3, G, A y D tienen entre 1 y 4 casos: sus porcentajes por
  dominio no son estimaciones.
- Es un clasificador de centroides con 8 rasgos (m en 5 fases y 3 armónicos);
  otro clasificador o rasgos distintos podrían dar otro resultado.
