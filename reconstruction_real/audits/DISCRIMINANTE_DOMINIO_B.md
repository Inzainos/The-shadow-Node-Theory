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

## Bloques 1–3 — BLOQUEADOS por datos ausentes

| Bloque | Prueba | Estado |
|---|---|---|
| **1** H-CONVERGENCIA | `b` vs brecha inicial `log(PIB_hub/PIB_nodo)` | **BLOQUEADO** — falta `data/owid-maddison.csv` (hallazgo #7 de la auditoría v32) |
| **2** H-ACOPLAMIENTO | `b` vs share de comercio bilateral (nodo→hub) | **BLOQUEADO** — falta matriz de comercio bilateral (IMF DOTS / CEPII BACI / UN Comtrade) |
| **3** modelo conjunto | R² parcial de cada regresor | **BLOQUEADO** — requiere 1 y 2 |

El bloque 2 impone además el requisito correcto: el hub debe **emerger** de la red
(centralidad direccional del comercio), no asignarse por PIB per cápita.

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
