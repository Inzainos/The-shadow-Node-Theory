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

Este gradiente regional es **exactamente lo que β-convergencia predice** y no lo
que un mecanismo de acoplamiento estructural requeriría. No es prueba definitiva
—para eso están los bloques 1–3— pero mueve el *prior* con fuerza.

## Bloque 1 — H-CONVERGENCIA — ✅ CORRIDO (2026-07-25) — **RESPALDADA**

Con `data/owid-maddison.csv` ya en el repo (Maddison Project Database vía OWID,
cobertura hasta 2022; ver `data/FUENTES.md`), el bloque corre sobre **441 de 446
pares** (`year_min` disponible para hub y nodo):

```
Spearman  b vs brecha inicial log(PIB_hub / PIB_nodo):
   rho = -0.4725   p = 6.6e-26   n = 441
PREDICCION H-CONVERGENCIA : rho NEGATIVO y significativo
VEREDICTO                 : RESPALDADA
```

La predicción de convergencia —brecha inicial grande → el rezagado alcanza → el
cociente hub/nodo cae → `b` menor— se cumple con fuerza. Y **sobrevive el control
por región** (Spearman intra-región), así que no es un artefacto de mezclar
regiones:

| Región | n | ρ intra | p |
|---|---:|---:|---:|
| Europa_Occidental | 66 | **−0.920** | <1e-4 |
| Europa_Nordica | 10 | −0.709 | 0.022 |
| Africa_Sub | 91 | −0.689 | <1e-4 |
| Africa_Norte | 10 | −0.685 | 0.029 |
| Sudamerica | 45 | −0.672 | <1e-4 |
| Europa_Sur | 18 | −0.664 | 0.003 |
| Asia_Sur | 15 | −0.443 | 0.098 |
| Medio_Oriente | 45 | −0.387 | 0.009 |
| Europa_Este | 55 | −0.201 | 0.141 |
| Centroamerica | 36 | −0.116 | 0.501 |
| Asia_Oriental | 10 | −0.091 | 0.803 |
| Asia_Sudeste | 36 | +0.165 | 0.337 |

Negativo en 11 de 12 regiones; solo Asia_Sudeste sale débilmente positivo y no
significativo. Salida por par en `reconstruction_real/data/discrim_bloque1_convergencia.csv`.

> **Matiz honesto (Quah / Friedman):** una correlación negativa entre la pendiente
> de `log R` y su nivel inicial es también la firma de la **regresión a la media**
> (Galton) — el mismo fenómeno que la crítica clásica a la β-convergencia. No es
> necesario decidir si es "convergencia real" o regresión a la media: en ninguno
> de los dos casos es **acoplamiento estructural**. El hallazgo que importa para
> SNT es el signo y la fuerza, no la etiqueta económica.

## Bloques 2–3 — BLOQUEADOS por datos ausentes

| Bloque | Prueba | Estado |
|---|---|---|
| **2** H-ACOPLAMIENTO | `b` vs share de comercio bilateral (nodo→hub) | **BLOQUEADO** — falta matriz de comercio bilateral (IMF DOTS / CEPII BACI / UN Comtrade) |
| **3** modelo conjunto | R² parcial de cada regresor | **BLOQUEADO** — requiere 1 y 2 |

El bloque 2 impone además el requisito correcto: el hub debe **emerger** de la red
(centralidad direccional del comercio), no asignarse por PIB per cápita.

## Lectura combinada (Bloque 0 + Bloque 1)

Dos evidencias independientes, ambas sobre datos reales, apuntan en la misma
dirección: (a) el rol de hub **no es estructural** (85% de dualidad de rol), y
(b) el exponente `b` está **fuertemente explicado por la brecha inicial de PIB**
(ρ=−0.47 global, hasta −0.92 dentro de una región). El bloque 2 (comercio
bilateral) decidiría si el acoplamiento estructural **añade** algo sobre la
convergencia; hasta entonces, la lectura honesta es que **el dominio B —62% del
corpus— es, en lo que se puede medir hoy, consistente con β-convergencia y no
con acoplamiento SNT**. No es refutación cerrada de SNT en B, pero sí desplaza
la carga de la prueba: hace falta el bloque 2 para sostener la lectura SNT.

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
