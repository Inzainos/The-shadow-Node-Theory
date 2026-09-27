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

## ⚠️ Re-corrida con la edición del corpus (MPD2020) — 2026-09-27

La corrida original (2026-07-25, secciones siguientes) usó `data/owid-maddison.csv`,
una edición OWID **posterior** a la que produjo el corpus: por eso solo encontró
441 de 446 pares (faltaba Sudán). El 2026-09-27 se identificó la edición real del
corpus, el **Maddison Project Database 2020** (`data/mpd2020.xlsx` →
`data/maddison_mpd2020.csv`; reproduce el dominio B byte a byte), y se re-corrió
la prueba con ella. Nulos con **5000 iteraciones** (semilla 20260725), para que
el IC95 sea estable (con 500, su borde variaba ~0.014 entre corridas):

| | OWID (edición posterior) | **MPD2020 (edición del corpus)** |
|---|---:|---:|
| Pares | 441 / 446 | **446 / 446** |
| Calibración 1d: deriva · volatilidad · nivel log | 0.02153 · 0.06473 · 7.804 (sd 0.670) | 0.02170 · 0.06522 · 7.847 (sd 0.693) |
| **Bloque 1** ρ observado | −0.4725 | **−0.4893** |
| Nulo 1d: media [IC95] | −0.4239 [−0.5787, −0.2434] | −0.4226 [−0.5765, −0.2418] |
| Posición · p empírico (nulo ≤ obs) | DENTRO · 0.287 | **DENTRO · 0.213** |
| **Bloque 1c** ρ observado (datos disjuntos) | −0.3676 | **−0.3846** |
| Nulo 1c: media [IC95] | −0.2526 [−0.4068, −0.0810] | −0.2508 [−0.4050, −0.0788] |
| Posición · margen al borde · p empírico | DENTRO · 0.039 · 0.080 | **DENTRO · 0.020 · 0.050** |

**Veredicto con el criterio preestablecido (IC95 del nulo calibrado): sigue
INCONCLUSO.** Los dos ρ observados caen dentro del nulo; el Bloque 0 no cambia
(no depende de Maddison). **Matiz:** con la edición correcta, el test limpio
(1c, datos disjuntos) queda **en el límite**: p empírico de una cola = 0.050 y a
0.020 del borde del intervalo. Es una señal débil de convergencia por encima del
artefacto de asignación de hub, **no concluyente**; no cambia el veredicto, pero
el dominio B queda más cerca de la lectura β-convergencia que en la corrida
original (p 0.080 → 0.050).

El script calcula ahora este veredicto por sí mismo (`veredicto_nulo_calibrado`)
y ya no imprime "RESPALDADA" por la comparación contra cero. Salidas:
`reconstruction_real/data/discrim_bloque1_convergencia.csv` y
`discrim_bloque1c_split.csv` (ahora con MPD2020, 446 pares).

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

## Bloques 2–3 — CORRIDOS (2026-09-27) — acoplamiento **no respaldado**

**Datos:** Correlates of War Trade v4.0 (comercio diádico 1870–2014, millones de
USD corrientes; `data/COW_Trade_4.0.zip`). `build_comercio_bilateral_cow.py`
arma las exportaciones direccionales por espejo de importaciones (flow1 =
importaciones de A desde B; flow2 = de B desde A; −9 = faltante), recorta cada
par a su ventana `[year_min, year_max]` y aplica reglas de entidad: no asigna al
corpus los años en que COW agrupa otro Estado (URSS 1917–1991 bajo "Russia",
Yugoslavia 1918–2005 bajo el código de Serbia, Vietnam del Norte < 1976,
Pakistán con Pakistán Oriental < 1972; Czechia solo desde 1993). Salida
`data/comercio_bilateral.csv`: flujos nodo→hub + una fila "RESTO_DEL_MUNDO" por
país-año, con control exacto de que la suma es el total de exportaciones. Se
descartan 177 filas de años con exportaciones totales = 0 (share indefinido,
sobre todo 1941–1945). **432 de 446 pares** tienen comercio nodo→hub.

**Bloque 2 — H-ACOPLAMIENTO** (predicción SNT: ρ(b, share) **positivo**). Share =
exportaciones nodo→hub / exportaciones totales del nodo; 5000 permutaciones,
semilla 20260725:

| Regresor | ρ por fila (n = 432) | Cluster por nodo (88) | Cluster por región (14) | Permutación intra-región |
|---|---:|---:|---:|---:|
| share media | −0.043 (p = 0.37) | +0.024 (p = 0.83) | −0.147 (p = 0.62) | p = 0.72 |
| share inicial | **−0.185** (p = 1.1×10⁻⁴) | **−0.245 (p = 0.022)** | −0.222 (p = 0.45) | **p = 0.026** |

- **El acoplamiento SNT no se sostiene.** La participación media del comercio
  nodo→hub no se relaciona con `b` en ningún nivel.
- **La única señal robusta tiene el signo OPUESTO al predicho:** cuanto mayor la
  integración comercial inicial del nodo con el hub, **menor** `b` (más
  convergencia). Sobrevive a la permutación intra-región y al cluster por nodo;
  por región no alcanza (14 clusters, baja potencia). Es correlacional y
  compatible con la literatura de convergencia por integración comercial; no
  prueba causalidad.

**Bloque 3 — modelo conjunto** (432 pares):
`b = +0.139 − 0.259·brecha_log + 0.309·share_media`; **R² = 0.290**; solo brecha
0.286; **solo share 0.0001**. El comercio no añade poder explicativo. La R² de la
brecha no es evidencia limpia de convergencia: el Bloque 1d muestra que buena
parte de esa relación es el artefacto de asignación de hub.

**Alcance:** esta prueba usa el hub **asignado por PIB medio** (la definición del
dominio). La pregunta de fondo — ¿hay acoplamiento con un hub que **emerja** de
la red de comercio? — sigue abierta y equivale a reconstruir el dominio.

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
   Con la edición del corpus (MPD2020) el test limpio 1c queda en el límite
   (p empírico 0.050): señal débil de convergencia, no concluyente.
4. **Acoplamiento medido con comercio bilateral (Bloques 2–3, 2026-09-27).** La
   participación del comercio nodo→hub **no explica `b`** (R² parcial 0.0001) y
   la única señal robusta (share inicial) tiene el **signo opuesto** al predicho
   por SNT. *Cerrado para el hub asignado.*

**Conclusión:** el dominio B —446 de 721 casos, **62% del corpus**— **no queda
respaldado como acoplamiento SNT** (el Bloque 2 lo evalúa directamente y no lo
encuentra; la señal comercial va en sentido contrario) **ni queda probado como
β-convergencia** (Bloque 1 inconcluso contra el nulo calibrado, aunque tanto el
1c como el share inicial se inclinan hacia convergencia). Lo único que
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
> calibrado sobre los datos reales (Maddison Project Database 2020; deriva
> +0.0217, volatilidad 0.0652, n=446, 5000 iteraciones), la correlación observada
> (ρ=−0.4893) cae dentro del intervalo del nulo ([−0.5765, −0.2418]), al igual
> que la versión con muestra partida (ρ=−0.3846 vs nulo [−0.4050, −0.0788]; p
> empírico 0.050, en el límite). (iv) Medido con comercio bilateral (COW Trade
> 4.0), el acoplamiento hub-nodo no explica `b` (ρ = −0.043 con la participación
> media; R² parcial 0.0001), y la integración comercial inicial se asocia con
> **menor** `b` (ρ = −0.185; permutación intra-región p = 0.026), en sentido
> contrario al predicho por SNT. El dominio B no queda respaldado como
> acoplamiento estructural ni probado como β-convergencia.

### Consecuencia para el corpus

Si el dominio B no mide lo que la teoría dice, el argumento de **invariancia de
escala del v31 se sostiene sobre los dominios restantes**, que son bastante más
chicos. Esa consecuencia hay que verla de frente — no la resuelve este documento.

## Cómo correrlo

```sh
python reconstruction_real/code/prueba_discriminante_dominio_B.py \
    --corpus reconstruction_real/data/by_domain/dominio_B_real.csv \
    --maddison data/maddison_mpd2020.csv \
    --comercio data/comercio_bilateral.csv \
    --n-placebo 5000 --omitir-1b
```

Bloques 0, 1, 1b, 1c y 1d corren con la edición del corpus (`maddison_mpd2020.csv`,
ya en el repo). `--maddison data/owid-maddison.csv` reproduce la corrida de
sensibilidad con la edición OWID posterior. Los Bloques 2–3 usan
`data/comercio_bilateral.csv` (en el repo; se regenera con
`python reconstruction_real/code/build_comercio_bilateral_cow.py` desde
`data/COW_Trade_4.0.zip`). `--n-placebo` controla las iteraciones de los
nulos (1b y 1d); `--omitir-1b` salta el 1b (no es un nulo válido y es el paso
más lento) sin cambiar 1, 1c, 1d ni el veredicto.

## Lo que queda abierto

1. **Newey-West** sobre los residuos crudos para fijar la cifra puntual de
   significancia AR(1) dentro de [33, 112]. El Maddison ya está en el repo, así
   que está **desbloqueado**.
2. **Hub emergente.** El Bloque 2 ya corrió con el hub asignado (2026-09-27; no
   respalda acoplamiento). Queda la pregunta distinta: "¿existe acoplamiento
   medible con un hub que **emerja** de la red de comercio en vez de asignarse
   por PIB?". Es reconstruir el dominio, no rescatarlo; la matriz de comercio ya
   está en el repo.
3. **Composición del corpus** — si el dominio B (62%) no mide lo que la teoría
   dice, la invariancia de escala del v31 se sostiene sobre los dominios
   restantes, más chicos.

## Lectura para el track de la auditoría

Esto **no reemplaza** la corrección por autocorrelación (dominio B: 290/446 no
estimables tras AR(1)); es una pregunta distinta y anterior. Son **problemas
independientes que se acumulan** sobre el mismo 62% del corpus. Ambos apuntan en
la misma dirección: el dominio B no puede tratarse como evidencia limpia de SNT.

## Seguimiento — reconstrucción con hub emergente del comercio (2026-09-27)

La pregunta que este informe dejó abierta (¿aparece el acoplamiento si el hub
**emerge** de la red de comercio en lugar de asignarse por PIB?) se contestó en
[`RECONSTRUCCION_DOMINIO_B_HUB_COMERCIO.md`](RECONSTRUCCION_DOMINIO_B_HUB_COMERCIO.md):
**no**. Con el mayor destino de exportación de cada país como hub, el hub no se
separa del nodo más que un país con la misma brecha inicial (d mediana −0.014,
p = 0.78), y 62 de 95 nodos convergen hacia su hub.
