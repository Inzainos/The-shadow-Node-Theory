# Auditoría integral v32 — recorrido completo de las cifras del repo

**Fecha:** 2026-07-24 · **Datos:** `Inzainos/The-shadow-Node-Theory@main`, sin datos externos
**Scripts:** `snt_utils_v32.py` (extiende `code/snt_utils.py`) + `snt_auditoria_integral_v32.py`

Se recorrieron 33 cifras publicadas. **14 replican exacto. 19 cambian o no son verificables.**

---

## Resultado en una línea

La aritmética del repo está limpia — todas las cifras de `MASTER_cifras_v5.json` y las 40
celdas de `MASTER_resumen_v5.csv` replican al decimal. **Lo que falla es la capa de
inferencia**, en cuatro puntos independientes que se acumulan.

---

## Lo que cambia

### 1. Autocorrelación serial — el hallazgo mayor

`expand_dominio_B.py` **ya calculaba** Durbin-Watson y luego se perdía al consolidar el corpus.
Lo recuperé de `by_domain/dominio_B_real.csv`:

| | Valor |
|---|---|
| DW mediana (446 casos) | **0.112** |
| Casos con DW < 1 (autocorrelación severa) | **445 / 446 = 99.8%** |
| ρ AR(1) implícito, mediana | **0.944** |
| n nominal mediano | 69 |
| **n efectivo mediano** | **2.2** |
| Factor de reducción | **31×** |
| Casos con n_eff < 3 (no ajustables con 2 parámetros) | **290 / 446** |

Consecuencia sobre la significancia:

| | Publicado | Corregido AR(1) |
|---|---|---|
| Significativos dominio B | 374 (83.9%) | **145 (32.5%)** |
| **pct_sig del corpus completo** | **89.3%** | **57.6%** |

Ese 57.6% es corrigiendo **solo B**. E3 (234 casos COVID) no trae DW, pero series de casos
acumulados son igual o más autocorrelacionadas. La cifra real será más baja.

> **Caveat honesto:** `n_eff = n(1−ρ)/(1+ρ)` es la aproximación de Bartlett, derivada para la
> media de un AR(1), no para la pendiente de una regresión. Sirve para dimensionar el orden de
> magnitud, **no como corrección final**. Para publicar: errores estándar Newey-West o GLS con
> estructura AR(1). Pero el orden de magnitud no está en duda: 31× es 31×.

### 2. El régimen superlineal b≥1 puede ser artefacto de modelo — hallazgo nuevo

RC1 ("la ley de potencia no ajusta mejor que lineal/exponencial") figura como NOT REFUTED en el
README, pero **no hay ningún script en el repo que la pruebe**. La probé por AIC sobre las 18
series crudas del ACO (las únicas disponibles):

```
potencia gana: 13/18    exponencial: 4/18    lineal: 1/18
```

RC1 aguanta en mayoría. Pero al cruzar con b apareció esto:

| Modelo ganador | n | b medio | rango |
|---|---:|---:|---|
| potencia | 13 | +0.324 | [+0.009, +1.244] |
| **exponencial** | **4** | **+1.541** | [+0.349, +2.195] |
| lineal | 1 | +0.453 | — |

```
Spearman b vs ΔAIC_potencia:  rho = +0.657   p = 0.0031
b>=1 x gana ley de potencia:  Fisher OR = 0.056   p = 0.0441
                              (3 de 4 casos superlineales son exponenciales)
```

**A mayor b, peor ajusta la ley de potencia.** La banda de clasificación de `snt_utils.py`
—"Satelización rápida sin fricción" (b>1), "Roche Radius"— podría estar etiquetando como
**régimen físico** lo que es **mala especificación de modelo**: curvas exponenciales forzadas a
ley de potencia.

El corpus reporta `pct_b_super = 14.1%` (102 de 721 casos). Si el patrón generaliza, ese 14.1%
está mal clasificado. **No se puede confirmar sin las series crudas de los otros dominios** —
n=18 es poca base para extrapolar. Pero es la hipótesis a probar primero.

Nota de coherencia interna: el propio ACO ya clasifica el modo "Catastrophic Cliff" como
*super-exponential*. O sea, el marco ya sabe que algunos colapsos no son leyes de potencia. El
eje b no había aplicado ese mismo criterio.

### 3. Hallazgo central: dirección aguanta, p no

Confirmado lo del informe anterior, ahora integrado al runner:

```
Por fila    : rho = -0.6782   p = 2.504e-97   n = 714     <- replica exacto
Por cluster : rho = -0.5555   p = 0.2525      n = 6 dominios
Bootstrap   : rho = -0.4337   IC95 = [-0.7219, -0.0063]
sin E3      : rho = -0.1162
sin E3 y B  : rho = -0.4264   p = 0.0119   n = 34
```

**Los dos problemas se suman:** el p-value por caso ya estaba inflado por autocorrelación
(punto 1), y encima se agregan 714 casos no independientes como si lo fueran (punto 3). No es
un error, son dos.

### 4. Defectos de reporte

| Hallazgo | Detalle |
|---|---|
| **p truncados** | 557 de 721 casos tienen `p == 0.0` exacto, por `round(p, 6)`. Impide FDR exacto, meta-análisis y combinación de p-values |
| **Dos definiciones de R²** | Dominio B (62% del corpus) usa `r_pearson²` = escala **log**. Los demás usan `1−SSres/SStot` = escala **cruda**. `r2_mean` promedia las dos juntas. No son la misma cantidad |
| **`trigger` hardcodeado** | `expand_dominio_B.py` línea 74: `r['trigger'] = 'gradual'` para los 446 casos, sin condición. El comentario anuncia una heurística que el código no implementa |

### 5. Cifras no verificables con lo que hay en el repo

| Cifra | Por qué |
|---|---|
| **5.9× abrupto/gradual, U=24,802, n=486** | El corpus v5 no tiene variable de trigger utilizable (446/446 = 'gradual' por asignación). n=486 no corresponde a ningún subconjunto de 721. **Parece heredado del corpus v28/502 marcado OBSOLETE** |
| **ROC-AUC 0.715 (ASI)** | El target es retención y no está en `snt_asi_scores.csv` |
| **RC9: ρ=+0.009 crypto n=11** | El corpus ACO (18 casos, tiene b) y el de colapso (14 casos, tiene Δ) **no comparten casos**. No hay pares (b, Δ) en el repo |

### 6. ASI — circularidad latente

```
ASI = δH·α/F   verificado, error máx 2.13e-14
soberania: ASI(False) máx = 0.9126 | ASI(True) mín = 1.0874   -> separación perfecta
```

**`soberania` es un umbral de ASI (ASI > ~1), no una variable independiente.** Cualquier
estadístico del tipo "ASI predice soberanía" sería circular por construcción. No encontré que
el README lo afirme — pero la trampa está armada en el CSV y conviene marcarla antes de que
alguien la pise.

Además: 13 soberanos de 4,774 = **0.27%**. Cualquier clasificador sobre 13 positivos es frágil.

---

## Lo que aguanta

| Bloque | Resultado |
|---|---|
| `MASTER_cifras_v5.json` | **8/8 replican exacto** (n_total, n_sig, pct_sig, b_mean, b_median, pct_b_pos, pct_b_super, r2_sig) |
| `MASTER_resumen_v5.csv` | **40/40 celdas, 0 discrepancias** |
| **N-cuerpos México** | b = **−0.4732** (pub. −0.473) · R²_raw = **0.8377** (pub. 0.838) · p = 7.47e-15. **Replica exacto** |
| ACO 18 casos | b̄ = +0.60 ✓ · 17/18 significativos ✓ |
| Piso de R² en ACO | **No enmascara nada**: 0/18 con R² crudo negativo. Sospecha descartada |
| H-φ | 26.6% cerca de φ en el corpus de 188. Consistente con refutada |

Sobre el N-cuerpos, una advertencia y no un error: un ajuste rank-size sobre 32 entidades
ordenadas produce R² alto casi por construcción. No es evidencia de *preferential attachment*
sin comparar contra lognormal (Clauset et al. 2009).

---

## Qué se agregó a los scripts

Se extendió lo existente en vez de duplicar, como pediste.

### `snt_utils_v32.py` — extiende `code/snt_utils.py`

Retrocompatible: `ajustar_ley_potencia()` devuelve las mismas claves más las nuevas. Ningún
script existente se rompe al cambiar el import.

| Se agregó | Por qué |
|---|---|
| `dw` para **todos** los ajustes | Solo lo tenía B y se perdía al consolidar |
| `rho_ar1`, `n_eff`, `p_ar1` | La corrección del punto 1 |
| `r2_log` **y** `r2_raw` separados | El repo mezclaba dos definiciones |
| `p_exacto` sin `round(,6)` | 557 p truncados a 0 |
| `se_b`, `ci_lo`, `ci_hi` | Solo los tenía B |
| `comparar_modelos()` | Prueba RC1 por AIC. Nunca se había probado |
| `ajustar_mle_clauset()` | El pendiente MLE+KS desde v2.2 |
| `spearman_cluster()` | Generaliza la corrección de rc12 |
| `corregir_corpus()` | Post-hoc sobre CSV ya ajustados, sin reajustar |
| `fdr_bh()` | Comparaciones múltiples sobre 721 |
| `plegado_trigger()` | Detecta el bug de `t = \|año − trigger\| + 1e-6` |

Sobre ese último: en `snt_utils.py` v28, si la serie cruza el año del trigger, los puntos previos
y posteriores caen en **el mismo t** (plegado por valor absoluto). Y si hay un punto exactamente
en el trigger, `log(1e-6) = −13.8` domina la regresión OLS. No pude confirmar que ocurra —
dominio B no usa esa función (usa su propio `calc()` con `t = arange(1, n+1)`), y no tengo las
series crudas de los demás dominios. **Queda como bandera, no como hallazgo.** La función ahora
avisa cuando pasa.

### `snt_auditoria_integral_v32.py` — nuevo, necesario

No existía nada equivalente en el repo. Absorbe `rc12_friccion_audit.py` y
`rc13_persistencia_nicho.py` (quedan como históricos). 13 bloques, un solo run, salida a CSV.

---

## 7. Reproducibilidad — hallazgo estructural (añadido 2026-07-24)

Rastreé todas las rutas de entrada que referencian los scripts del repo. Solo hay una externa:

```
data/owid-maddison.csv   ->  NO EXISTE en el repositorio
```

`expand_dominio_B.py` la lee en su línea 11. **El dominio B — 446 casos, 62% del corpus — no se
puede regenerar clonando el repo.** Tampoco está la fuente de E3 (COVID).

Proporción justa: el Maddison Project es público y obtenible, así que esto no es irrecuperable.
Pero el repo no fija versión ni checksum, y el Maddison Project **revisa sus estimaciones
históricas de PIB entre ediciones**. Los resultados no están anclados a una versión de datos, así
que dos personas ejecutando el mismo script en fechas distintas pueden obtener cifras distintas
sin saberlo.

Arreglo barato: un `data/FUENTES.md` con URL, fecha de descarga, edición y SHA-256 de cada
archivo fuente. O un `download_sources.sh`.

**Consecuencia para esta auditoría:** tres de los seis pendientes están bloqueados por esta misma
causa — corregir E3 por autocorrelación, extender la prueba de b≥1 a otros dominios, y reajustar
reportando p sin truncar. Los tres necesitan series crudas que no están.

## 8. Rastro del 5.9× en el CHANGELOG

El CHANGELOG v2.4.0 documenta que los datos y papers de la era de 502 casos se movieron a
`archive/`, con nota histórica explícita: contenían valores sintéticos y una columna r² con
valores imposibles, y **no deben citarse en publicaciones académicas**.

No pude localizar el archivo concreto (las rutas que probé bajo `archive/` dan 404, y la API de
GitHub me limitó por tasa antes de poder listar el árbol). Pero la aritmética apunta en una sola
dirección: n=486 es un subconjunto plausible de 502, no lo es de 721, y el corpus v5 no tiene
variable de trigger utilizable. **Verificable en un minuto desde tu clon local**: si el 5.9× sale
del corpus archivado, sale del README o se recalcula.

## 9. Precedente favorable

El CHANGELOG v2.3.1 registra: *"Corrección de fuga de datos en validación HackerEarth (ROC-AUC
corregido)"*. Ya detectaste y corregiste una fuga de datos por iniciativa propia, y lo dejaste
asentado en el registro público.

Eso importa por dos razones. Primero, el ROC-AUC 0.715 **es** el valor ya corregido, así que mi
señalamiento de la circularidad de `soberania` es un riesgo latente distinto, no el mismo que ya
resolviste. Segundo, y más práctico: tienes historial documentado de autocorrección. Eso vuelve
mucho más creíble una nota proactiva al editor que una corrección forzada por un revisor.

---

## Orden sugerido

1. **Corregir por autocorrelación antes que nada.** Es el problema más grande, afecta 62% del
   corpus como mínimo, y `corregir_corpus()` ya lo hace sobre los CSV que tienen `dw`. Lo que
   falta es reajustar E3 y los demás dominios para obtener su `dw`.
2. **Nota al editor de PLOS** cubriendo autocorrelación + cluster juntos. Son dos problemas
   distintos que se acumulan sobre la misma cifra.
3. **Probar b≥1 en las demás series crudas.** Si el patrón de B7b generaliza, hay que reetiquetar
   el 14.1% del corpus. Es el hallazgo con más consecuencias teóricas.
4. **Reportar p sin truncar** y separar `r2_log` de `r2_raw` en el corpus consolidado. Barato.
5. **Localizar el origen del 5.9×.** Si viene de v28/502, sale del README o se recalcula.
6. **Marcar `soberania` como derivada de ASI** en el CSV, para que nadie la use como target.
