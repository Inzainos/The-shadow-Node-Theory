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
> economía**. El nulo correcto es un **nulo sintético calibrado** (Bloque 1d),
> no la comparación contra cero ni el re-emparejamiento del 1b.

Sobre **441 de 446 pares**:

```
Spearman b vs brecha inicial log(PIB_hub/PIB_nodo):
   rho = -0.4725   p = 6.6e-26   n = 441   (vs CERO — comparación incorrecta)
```

### Bloque 1d — nulo sintético calibrado (el correcto) ✅

Genera series **sintéticas sin ninguna economía** (paseos aleatorios), con la
**misma estructura de regiones y el mismo n**, y con deriva, volatilidad y
dispersión de niveles **calibradas al Maddison real**. Corre el pipeline completo
(hub por PIB promedio) y produce el nulo para el ρ del test completo **y** del
partido. Calibración extraída de `owid-maddison.csv`:

```
deriva anual (media Δlog) = +0.0215
volatilidad (sd Δlog)     =  0.0647
nivel inicial log         =  media 7.804 · sd 0.670
años por serie            =  119        (n=446, semilla 20260725)
```

| Test | Observado | Nulo calibrado (media, IC95) | Veredicto |
|---|---:|---:|---|
| **Bloque 1** (serie completa) | −0.4725 | −0.4244, [−0.5796, −0.2608] | **DENTRO — compatible con puro artefacto** |
| **Bloque 1c** (muestra partida) | −0.3676 | −0.2465, [−0.4132, −0.0902] | **DENTRO — compatible con puro artefacto** |

**Los dos observados caen dentro del intervalo del nulo. No hay señal por encima
del artefacto de asignación de hub — ni en el test completo ni en el de datos
disjuntos.** (Ejecutando el script se reproducen estas cifras dentro del ruido
Monte Carlo, p.ej. full −0.42 [−0.57, −0.25], split −0.25 [−0.42, −0.08].)

El punto clave del 1c: rompe el acoplamiento mecánico por construcción, y **aun
así su nulo calibrado es −0.2465**. Es decir, la regla `pib_avg` inyecta
correlación espuria **incluso cuando la brecha y la pendiente vienen de mitades
disjuntas de la serie**, porque el rol de hub se sigue decidiendo con información
de todo el periodo. Ése era el punto que faltaba en la versión anterior de este
documento (que reportaba el 1c como "sugestivo").

### Bloque 1b — re-emparejamiento — NO es un nulo válido

El 1b (media −0.5704) re-empareja países al azar dentro de región, pero eso
**conserva el mecanismo que se quiere aislar** y además añade la estructura común
de las series reales (shocks globales, tendencias compartidas); mide artefacto +
covarianza real, no artefacto puro. Se conserva en el script como **observación
aparte**, no como nulo: los pares reales están *menos* anticorrelacionados que
pares arbitrarios de la misma región, lo cual apunta —si acaso— en dirección
**contraria** a la convergencia. No se mezcla con el veredicto.

> **Matiz (Quah / Friedman):** el residual es indistinguible de **regresión a la
> media** (Galton), la crítica clásica a la β-convergencia. En ningún caso es
> **acoplamiento estructural** — lo único que sostendría la lectura SNT.

Salidas por par: `discrim_bloque1_convergencia.csv`, `discrim_bloque1c_split.csv`.

## Bloques 2–3 — NO se corren todavía (decisión deliberada)

Con el Bloque 1 confundido por el artefacto de asignación, **traer la matriz de
comercio bilateral es prematuro**. La pregunta ya no es "¿convergencia o
acoplamiento?" sino "¿existe acoplamiento medible con un hub que **emerja** de la
red en vez de asignarse?". Es **reconstruir** el dominio, no rescatarlo.

| Bloque | Prueba | Estado |
|---|---|---|
| **2** H-ACOPLAMIENTO | `b` vs comercio bilateral (nodo→hub) | pendiente — requiere matriz direccional (IMF DOTS / CEPII BACI / UN Comtrade) **y** hub emergente de la red |
| **3** modelo conjunto | R² parcial de cada regresor | requiere 1 (bien especificado) y 2 |

## Estado del dominio B — cierre

Tres problemas independientes, **ninguno resuelto a favor de la teoría**:

1. **Autocorrelación serial.** DW mediana 0.112, ρ AR(1) 0.944. **290/446 casos no
   estimables** (`n_eff < 3`); entre los 156 estimables, significativos entre 33
   (21.2%) y 112 (71.8%) según variante; cifra puntual pendiente de Newey-West.
   *Cerrado en concepto, cuantificado.*
2. **Validez de constructo.** El rol de hub se asigna por PIB per cápita promedio;
   **77/91 países (85%) son hub y satélite a la vez** (Italia hub en 3 / satélite
   en 12; México 1/9). El rol es propiedad del par, no de una posición en red.
   *Sin resolver. El más firme — sale de contar filas.*
3. **Artefacto en el estadístico usado para evaluarlo.** La regla `pib_avg` acopla
   mecánicamente la pendiente con la brecha inicial; contra el nulo calibrado, la
   relación observada **no se distingue del artefacto** (Bloque 1d). *Cerrado.*

**Conclusión:** el dominio B —446 de 721 casos, **62% del corpus**— **no queda
respaldado ni como β-convergencia ni como acoplamiento SNT**. Lo único que
sobrevive sin supuestos, sin nulos y sin parámetros es el **Bloque 0**: el rol de
hub no es estructural.

> **Redacción para el corpus/README (estado metodológico).** El exponente `b` del
> dominio B presenta tres problemas independientes. (i) Las series subyacentes
> tienen autocorrelación severa (DW mediana 0.112); tras corrección AR(1), 290 de
> 446 casos quedan por debajo del mínimo estimable y se reportan como no
> estimables. (ii) El rol de hub se asigna por PIB per cápita promedio, y 85% de
> los países aparecen en ambos roles, por lo que no representa una posición
> estructural en una red. (iii) Esa misma regla de asignación acopla mecánicamente
> la pendiente `b` con la brecha inicial de PIB; contra un nulo sintético
> calibrado sobre los datos reales (deriva +0.0215, volatilidad 0.0647, n=446), la
> correlación observada (ρ=−0.4725) cae dentro del intervalo del nulo
> ([−0.5796, −0.2608]), al igual que la versión con muestra partida (ρ=−0.3676 vs
> nulo [−0.4132, −0.0902]). El dominio B no queda respaldado ni como
> β-convergencia ni como acoplamiento estructural.

### Consecuencia para el corpus

Si el dominio B no mide lo que la teoría dice, el argumento de **invariancia de
escala del v31 se sostiene sobre los dominios restantes**, que son bastante más
chicos. Esa consecuencia hay que verla de frente — no la resuelve este documento.

## Cómo correrlo

```sh
python reconstruction_real/code/prueba_discriminante_dominio_B.py \
    --corpus reconstruction_real/data/by_domain/dominio_B_real.csv \
    --maddison data/owid-maddison.csv \
    --comercio data/comercio_bilateral.csv
```

Bloques 0, 1, 1b, 1c y 1d corren con `owid-maddison.csv` (ya en el repo). El
Bloque 2 requiere además la matriz de comercio bilateral. `--n-placebo` controla
las iteraciones de los nulos (1b y 1d).

## Lo que queda abierto

1. **Newey-West** sobre los residuos crudos para fijar la cifra puntual de
   significancia AR(1) dentro de [33, 112]. El Maddison ya está en el repo, así
   que está **desbloqueado**.
2. **Bloque 2 (comercio bilateral)** — sigue teniendo sentido, pero como pregunta
   distinta: no "¿convergencia o acoplamiento?" sino "¿existe acoplamiento
   medible, con un hub que emerja de la red en vez de asignarse?". Es reconstruir
   el dominio, no rescatarlo.
3. **Composición del corpus** — si el dominio B (62%) no mide lo que la teoría
   dice, la invariancia de escala del v31 se sostiene sobre los dominios
   restantes, más chicos.

## Lectura para el track de la auditoría

Esto **no reemplaza** la corrección por autocorrelación (dominio B: 290/446 no
estimables tras AR(1)); es una pregunta distinta y anterior. Son **problemas
independientes que se acumulan** sobre el mismo 62% del corpus. Ambos apuntan en
la misma dirección: el dominio B no puede tratarse como evidencia limpia de SNT.
