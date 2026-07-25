# Prueba discriminante del dominio B — ¿acoplamiento o convergencia?

**Fecha:** 2026-07-25 · **Script:** `reconstruction_real/code/prueba_discriminante_dominio_B.py`

## La pregunta

El exponente `b` del dominio B (446 de 721 casos = **62% del corpus**), ¿mide
**acoplamiento hub-satélite** (la lectura SNT) o **β-convergencia** de PIB per
cápita (Barro & Sala-i-Martin)? Las dos hipótesis hacen predicciones separables:

| Hipótesis | `b` crece con… | Correlato de prueba |
|---|---|---|
| **H-ACOPLAMIENTO** (SNT) | intensidad del vínculo estructural | comercio bilateral |
| **H-CONVERGENCIA** (economía) | brecha inicial de PIB per cápita | `log(PIB_hub / PIB_nodo)` inicial |

**Si gana H-CONVERGENCIA, el dominio B no es evidencia de SNT.**

## Bloque 0 — diagnóstico estructural (corre sin datos externos) — ⚠️ resultado

El motivo de la prueba: el "hub" se asigna por **mayor PIB per cápita** dentro de
un bucket geográfico, no por topología de red. Consecuencia medida sobre el
corpus real:

```
países en rol de hub          : 91
países en rol de satélite     : 89
países en AMBOS roles         : 77  (85% de los hubs)

Casos más contradictorios (mucho satélite, poco hub):
  Italy           hub=3   satélite=12
  France          hub=1   satélite=10
  Mexico          hub=1   satélite=9
  Spain           hub=6   satélite=9
  United Kingdom  hub=2   satélite=9
```

**El rol de hub es una propiedad del PAR, no del país.** Que el 85% de los "hubs"
también aparezcan como satélites es incompatible con una lectura estructural de
red: si el rol fuera estructural, un país no aparecería en ambos roles dentro del
mismo sistema regional. Lo fija un operador de comparación sobre PIB per cápita.

Además, `b` **depende fuertemente de la región** (Kruskal-Wallis H=63.5,
p=1.2×10⁻⁸), con un gradiente coherente con convergencia: negativo en regiones ya
convergidas (Europa Occidental −0.018, Sudamérica −0.051, Oceanía −0.110) y
positivo en regiones rezagadas (África Norte +0.284, Asia Sudeste +0.240):

```
b<0 (convergencia): 170 / 446 (38.1%)
b>0 (divergencia) : 276 / 446
```

Este gradiente regional es **compatible** con β-convergencia, pero no es prueba:
`b` puede variar por región por muchas razones. La prueba formal es el Bloque 1
— y una vez comparado contra su nulo correcto (1b), **no** respalda convergencia
(ver abajo). Lo que sí queda firme del Bloque 0 es la **dualidad de rol del hub**,
que no depende de ningún ajuste.

## Bloque 1 — H-CONVERGENCIA — CORRIDO (2026-07-25) — **INCONCLUSO (confundido)**

> **⚠️ Corrección de una versión previa de este documento.** Un commit anterior
> reportó el Bloque 1 como *"H-CONVERGENCIA RESPALDADA"* comparando el ρ observado
> contra **cero**. Ésa era la comparación equivocada. La brecha inicial y `b`
> salen del **mismo ajuste OLS** (la brecha es casi el intercepto; `b` la
> pendiente) y el hub se asigna por **PIB promedio de toda la serie**. Eso
> anticorrelaciona pendiente y brecha **por construcción, antes de cualquier
> economía**. El nulo correcto (Bloque 1b) lo demuestra sobre los datos reales.

Sobre **441 de 446 pares**:

```
Spearman b vs brecha inicial log(PIB_hub/PIB_nodo):
   rho = -0.4725   p = 6.6e-26   n = 441   (vs CERO — comparación incorrecta)
```

### Bloque 1b — nulo por remuestreo (500 iter, `owid-maddison.csv` real)

Re-empareja países al azar **dentro de región** y corre el pipeline completo,
incluida la asignación de hub por PIB promedio. Es la distribución nula correcta
del ρ:

```
media del nulo = -0.5732
IC95           = [-0.6435, -0.5046]
```

**El ρ observado (−0.4725) NO es más extremo que el nulo — es *menos* negativo que
su media (−0.57), y queda por fuera del IC95 por el lado menos negativo.** Es
decir: la regla de asignación de hub, aplicada a pares **aleatorios**, produce una
anticorrelación **más fuerte** que la de los pares reales. El −0.4725 **no supera
el artefacto de asignación**; por sí solo no aporta evidencia de convergencia.

### Bloque 1c — muestra partida (test limpio)

Rompe el acoplamiento mecánico: brecha medida en la **1ª mitad** de la serie, `b`
ajustado en la **2ª mitad** (datos disjuntos → la brecha deja de ser el intercepto
del ajuste que produce `b`):

```
Spearman b(2a mitad) vs brecha(1a mitad):  rho = -0.3676   p = 1.5e-15   n = 441
```

Sobre datos disjuntos **sobrevive una relación más débil** (−0.37 vs −0.47). Eso
indica que hay *algo* real bajo el artefacto — pero **vs cero**, no vs su propio
nulo split. Sin un nulo para la versión partida no se puede separar
convergencia-económica de **regresión a la media** residual del cociente. Queda
como **sugestivo, no concluyente**.

> **Matiz (Quah / Friedman):** aun el residual del 1c puede ser regresión a la
> media (Galton), la misma crítica clásica a la β-convergencia. En ninguno de los
> casos es **acoplamiento estructural** — que es lo único que sostendría la
> lectura SNT del dominio B.

Salidas por par: `discrim_bloque1_convergencia.csv`, `discrim_bloque1c_split.csv`.

## Bloques 2–3 — NO se corren todavía (decisión deliberada)

Con el Bloque 1 confundido por el artefacto de asignación, **traer la matriz de
comercio bilateral es prematuro**: primero hay que decidir si `b` mide algo más
que la aritmética de dividir dos tendencias suaves con un rol asignado post hoc.

| Bloque | Prueba | Estado |
|---|---|---|
| **2** H-ACOPLAMIENTO | `b` vs comercio bilateral (nodo→hub) | pendiente — requiere matriz direccional (IMF DOTS / CEPII BACI / UN Comtrade) **y** que el hub **emerja** de la red, no se asigne por PIB |
| **3** modelo conjunto | R² parcial de cada regresor | requiere 1 (bien especificado) y 2 |

## Lectura combinada — qué se puede afirmar hoy

1. **Bloque 0 (firme, sin supuestos):** el rol de hub **no es estructural** — 85%
   de los países son hub y satélite a la vez. Sale de contar filas; no depende de
   nulos ni aproximaciones. Es el hallazgo más sólido.
2. **Bloque 1 (confundido):** el ρ=−0.4725 **no supera el nulo del artefacto de
   asignación** (−0.57). No establece convergencia. La versión limpia (1c, −0.37)
   deja un residuo sugestivo pero no concluyente.
3. **Conclusión honesta:** no se puede afirmar "el dominio B mide β-convergencia"
   —eso invalidaría el 62% del corpus y **no está demostrado**—. Pero **tampoco se
   sostiene la lectura SNT**: el constructo de hub es post hoc (Bloque 0) y el
   estadístico que se usó para defenderlo está dominado por un artefacto de
   asignación (Bloque 1b). El dominio B queda **bajo sospecha metodológica seria,
   sin veredicto positivo para ninguna de las dos hipótesis** hasta reconstruir la
   prueba con un hub que emerja de datos independientes (comercio) y un nulo
   propio.

## Cómo correrlo

```sh
python reconstruction_real/code/prueba_discriminante_dominio_B.py \
    --corpus reconstruction_real/data/by_domain/dominio_B_real.csv \
    --maddison data/owid-maddison.csv \
    --comercio data/comercio_bilateral.csv
```

Bloque 0 corre siempre. Los bloques 1–3 se activan al aparecer las fuentes
(fijar edición + SHA-256 en `data/FUENTES.md` antes de correr: el Maddison
Project revisa sus estimaciones entre ediciones).

## Lectura para el track de la auditoría

Esto **no reemplaza** la corrección por autocorrelación (dominio B: 290/446 no
estimables tras AR(1)); es una pregunta distinta y anterior. Si el bloque 1
confirma H-CONVERGENCIA, el problema del dominio B no es solo de *precisión
estadística* (autocorrelación) sino de *qué está midiendo el exponente*. Ambas
apuntan en la misma dirección: tratar el dominio B con cautela como evidencia de
SNT hasta que aparezcan las series fuente.
