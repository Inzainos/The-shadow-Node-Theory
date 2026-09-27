# Pre-registro — cinco pruebas de la Shadow Node Theory

**Fecha:** 2026-09-27 · **Rama:** `claude/charming-brown-w9h8iu` · **Base:** `main` en `28eabb1`
(merge del PR #45) · **Autor de la teoría:** Elán Zainos Corona · **Análisis:** Claude Code
(sesión del repositorio), a pedido del autor.

Este documento se sube al repositorio **antes** de descargar los datos nuevos y de correr
cualquiera de las pruebas. El commit y su fecha en GitHub son el sello de tiempo. Todo lo que
se reporte después debe seguir estas reglas; cualquier cambio se anota en la sección
**Desviaciones** del informe de resultados, con motivo, y nunca en silencio.

## 0. Reglas generales

1. **Se reporta todo resultado**, favorable o no, con el mismo detalle.
2. **α = 0.05.** Cuando la hipótesis tiene dirección pre-especificada, la prueba principal es
   de una cola en esa dirección; también se reporta el p de dos colas.
3. **Unidad de inferencia:** la unidad independiente más gruesa disponible (dominio, nodo,
   hub o caso), nunca la fila cuando las filas comparten estructura.
4. **Ajuste de b:** el mismo de todo el corpus — MCO de log R contra log t con t = 1..n
   (`calc()` de `expand_B_massive.py`), salvo que la prueba diga otra cosa.
5. **Semillas fijas:** 20260927 en toda aleatoriedad.
6. **Logs obligatorios** en `reconstruction_real/logs/` y SHA-256 de cada archivo fuente
   descargado, anotado en `data/FUENTES.md`.
7. **Ceguera declarada.** Punto 1: el analista ya vio la reconstrucción estática del dominio B
   con hub de comercio (PR #45), así que ese punto **no es ciego** respecto a la fuente; sí lo
   es respecto al nuevo diseño. Puntos 2, 3, 4 y 5: los datos nuevos (mpox, StatCounter, WUP
   2018, OWID COVID, Binance, FDIC) **no** se han descargado ni visto al escribir esto.
8. **Hallazgo previo que condiciona el punto 2** (verificado hoy, antes de este documento): la
   prueba publicada de fricción (n = 714) **excluye el dominio D** (digital, 3 casos). D mide
   exponentes de distribución de actividad (tipo rango-tamaño), no una trayectoria R(t), lo
   que justifica excluirlo, pero el preprint no lo dice. Con D: sin E3 ni B, ρ = −0.145
   (p = 0.39, n = 37); sin D: ρ = −0.426 (p = 0.012, n = 34).

---

## Punto 1 — Hub variable en el tiempo (pares de países)

**Pregunta.** ¿El país diverge de su hub comercial *vigente* más que de un país con la misma
brecha con el que casi no comercia?

**Datos.** Maddison 2020 (`data/maddison_mpd2020.csv`, población de `data/mpd2020.xlsx`) y COW
Trade v4.0 (`data/COW_Trade_4.0.zip`), con las mismas reglas de entidad y de mapeo de socios de
`reconstruccion_B_hub_comercio.py`. Nodos: los 103 países del dominio B.

**Diseño.**
- Arranques s ∈ {1900, 1910, …, 1990}. Para cada nodo y arranque, **hub_s** = socio con mayor
  suma de exportaciones del nodo en la ventana previa [s − 4, s] (COW desde 1870). El hub se
  fija con información anterior a la trayectoria que se mide.
- Trayectoria: R(t) = PIBpc_hub / PIBpc_nodo en [s, s + H − 1], H = **20** años; se exige
  ≥ 15 observaciones Maddison en la ventana.
- Controles: socios con serie Maddison que **no** estén entre los 5 principales destinos del
  nodo en [s − 4, s], misma ventana (n ≥ 90% de la del hub), |Δg| ≤ 0.25 (g = media de log R
  en las 5 primeras observaciones), los K = 5 más cercanos en g.
- d = b_hub − media(b_controles).
- Marcas: la de cobertura CMEA dudosa (miembros del CMEA con arranque en 1949–1991 cuyas
  exportaciones a la URSS en la ventana previa son faltantes o cero en ≥ 3 de 5 años).

**Hipótesis SNT (H1).** d > 0: el hub vigente se separa más del nodo.

**Prueba principal.** Media de d por nodo → Wilcoxon de una cola (d > 0) sobre nodos.
**Secundarias.** (a) Media de d por hub → Wilcoxon sobre hubs. (b) Solo espacios con hub más rico
al inicio (g > 0). (c) Sin marcas CMEA. (d) Sensibilidad H = 10 y H = 30. (e) Descriptivo:
fracción de espacios con b > 0 cuando el hub es más rico; número de cambios de hub.

**Decisión.** *Respaldada* si la principal da p < 0.05 **y** la mediana por hub es > 0.
*No respaldada* si p ≥ 0.05. *Contraria* si la prueba de dos colas da p < 0.05 con d < 0.

---

## Punto 2 — Fricción con dominios nuevos, sin COVID

**Pregunta.** ¿La relación negativa entre fricción a priori y b se sostiene a nivel de dominio
cuando se agregan dominios nuevos que no son COVID?

**Codificación de fricción (fijada aquí, antes de ver los datos; misma escala que el corpus:
nula 0, baja 1, media 2, alta 3).**

| Dominio nuevo | Datos | Fricción | Criterio |
|---|---|---|---|
| **E4** mpox 2022 | OWID monkeypox (casos por país) | nula (0) | misma clase que E1/E3: propagación epidémica |
| **D2** cuotas digitales | StatCounter, mundial, mensual 2009-01 a 2024-12 | baja (1) | misma clase que D: competencia entre plataformas digitales |
| **A2** ciudades | ONU WUP 2018, archivo anual de aglomeraciones ≥ 300 mil, 1950–2018 | media (2) | misma clase que A: pares de ciudades de un país |
| **B-comercio** | Reconstrucción del dominio B con hub de comercio (PR #45) | alta (3) | misma clase que B: pares de Estados soberanos |

**Construcción de R(t).**
- **E4:** la receta de E3 identificada en el punto 3, aplicada a mpox. Si el punto 3 no la
  identifica: casos confirmados acumulados en los primeros 60 días desde el primer día con
  ≥ 10 casos acumulados; países con ≥ 100 casos acumulados al día 60.
- **D2:** categorías browser, search engine, OS, social media y mobile vendor (todas las
  plataformas, mundial). Hub = entidad con mayor cuota media en los primeros 12 meses;
  nodos = entidades con cuota media ≥ 1% en esos 12 meses (se excluyen "Other" y "Unknown").
  R = cuota_hub / cuota_nodo; t = mes 1..n; ≥ 24 meses con cuota > 0.
- **A2:** por país, hub = mayor aglomeración en 1950; nodos = las demás aglomeraciones del
  país en el archivo. R = pob_hub / pob_nodo, 1950–2018 (sin proyecciones).
- **B-comercio:** los b de `dominio_B_hub_comercio.csv` tal como están.

**Hipótesis SNT (H2).** A mayor fricción, menor b: ρ(fricción, b̄ del dominio) < 0.

**Prueba principal.** Nivel dominio, **sin COVID**: A, A2, B-comercio, C, D2, E2, E4
(7 dominios). Spearman entre fricción y la media de b por dominio; p por **permutación exacta**
de las etiquetas de fricción entre los 7 dominios (una cola, ρ < 0).
**Secundarias.** (a) Mediana de b por dominio en lugar de media. (b) Con B publicado en lugar
de B-comercio. (c) Agregando E1 y E3 (todos los dominios). (d) Agregando D (exponentes de
distribución). (e) Por caso, solo como descriptivo (no inferencial).

**Decisión.** *Respaldada* si ρ < 0 y p de permutación < 0.05 en la principal. *No
respaldada* en otro caso. *Contraria* si ρ > 0 con p de dos colas < 0.05.

---

## Punto 3 — Series crudas de COVID (E3, E1) y autocorrelación

**Pregunta.** ¿Cuántos de los 234 casos de E3 siguen siendo significativos al corregir la
autocorrelación serial, y se puede reproducir E3 desde datos crudos?

**Datos.** OWID COVID-19 (archivo completo de OWID; SHA anotado).

**Identificación de la receta (exploratoria, con criterio fijado).** Se prueban, en este orden,
las recetas: variable ∈ {casos confirmados acumulados, casos nuevos suavizados a 7 días};
inicio ∈ {primer caso, primer día con ≥ 10 acumulados, primer día con ≥ 100 acumulados};
ventana de 60 días; t = 1..60. Se **acepta** la primera receta que reproduzca el b publicado
dentro de ±0.01 en ≥ 90% de los países emparejados. Si ninguna lo logra se reporta que E3 no es
reproducible y se usa la receta con mayor coincidencia, rotulada como aproximación.

**Corrección.** Por caso: Durbin-Watson, ρ AR(1) de los residuos, n efectivo
n·(1 − ρ)/(1 + ρ), estimable si n_eff ≥ 3; p con error estándar Newey-West (rezagos
floor(4·(n/100)^(2/9))). Se reporta cuántos quedan con p < 0.05.
**E1** (4 casos): mismo procedimiento si se identifica su construcción; si no, se declara no
reproducible.

Sin hipótesis direccional: es una corrección de reporte.

---

## Punto 4 — Corpus de disparadores codificados a ciegas

**Pregunta.** ¿Un disparador abrupto por decreto produce una satelización más rápida que la
dinámica basal de ciudades con la misma razón inicial de tamaño?

**Casos abruptos codificados ahora, antes de ver las series** (año efectivo; entre paréntesis
el año de decisión, usado como sensibilidad):

| Caso | Retador → incumbente | Año |
|---|---|---|
| Brasil, traslado de capital | Brasília / Rio de Janeiro | 1960 (1956) |
| Pakistán, traslado de capital | Islamabad / Karachi | 1967 (1959) |
| Nigeria, traslado de capital | Abuja / Lagos | 1991 (1976) |
| Kazajistán, traslado de capital | Astana / Almaty | 1997 (1994) |
| Tanzania, traslado de capital | Dodoma / Dar es Salaam | 1996 (1973) |
| Costa de Marfil, traslado de capital | Yamoussoukro / Abidjan | 1983 (1983) |
| Alemania, traslado de capital | Berlín / Bonn | 1999 (1991) |
| Malawi, traslado de capital | Lilongwe / Zomba | 1975 (1965) |
| China, Zona Económica Especial | Shenzhen / Guangzhou | 1980 (1979) |
| China, Zona Económica Especial | Zhuhai / Guangzhou | 1980 (1979) |
| China, Zona Económica Especial | Shantou / Guangzhou | 1980 (1979) |
| China, Zona Económica Especial | Xiamen / Fuzhou | 1980 (1979) |

**Regla de inclusión.** Entran los casos cuyas dos ciudades estén en el archivo WUP 2018 de
aglomeraciones (1950–2018) con ≥ 15 observaciones desde el año efectivo. Los que no cumplan se
listan como excluidos por datos.

**Diseño.** R = pob_retador / pob_incumbente, t = 1..n desde el año efectivo hasta 2018.
Controles: otras aglomeraciones del mismo país (excluidos retadores codificados e incumbente),
R = pob_control / pob_incumbente en la misma ventana, emparejadas por razón inicial
(|Δ log R| ≤ 0.25 en la media de las 5 primeras observaciones), K = 5 más cercanas; si hay
menos de 3 en el país, se completan con aglomeraciones de cualquier país (misma ventana, mismo
emparejamiento, R contra el incumbente de su propio país = su mayor aglomeración en el año
efectivo). d = b_caso − media(b_controles).

**Hipótesis SNT (H4).** d > 0: el retador abrupto gana terreno más rápido. (La v1.0 decía que
los abruptos son ~5.9× más rápidos.)

**Prueba principal.** Wilcoxon de una cola (d > 0) sobre los casos incluidos.
**Secundarias.** (a) Rango percentil de b_caso en su grupo de control; media de percentiles
contra 0.5 (prueba de signo). (b) Solo traslados de capital. (c) Con el año de decisión.
(d) Razón b̄_casos / b̄_controles.

**Decisión.** *Respaldada* si p < 0.05 y mediana de d > 0. *No respaldada* en otro caso.
*Contraria* si p de dos colas < 0.05 con d < 0. Con pocos casos la potencia es baja; un "no
respaldada" con n chico no equivale a refutación y se reporta así.

**Segunda codificación (opcional).** El autor puede codificar la lista por su cuenta sin ver
los resultados; si lo hace se reporta el acuerdo entre ambas codificaciones.

---

## Punto 5 — Ampliar las cohortes de ACO-A

**5a. Ortogonalidad b ⊥ Δ (cripto).** Datos: archivo público de Binance
(`data.binance.vision`, klines diarias spot, todos los pares contra USDT, incluidos
retirados; se excluyen stablecoins, tokens apalancados UP/DOWN/BULL/BEAR y pares de monedas
fiat). Método idéntico a `orthogonality_test.py`: serie ≥ 200 días, pico con ≥ 120 días antes
y después, b_subida = ajuste log-log del precio contra días desde el primer dato hasta el
máximo, Δ_caída = ajuste desde el máximo hasta el mínimo posterior; ≥ 20 puntos por ajuste.
Nota: el "nacimiento" es el listado en Binance, no el origen de la moneda.
**H5a:** ortogonalidad. **Criterio de equivalencia:** respaldada si el IC 95% de Spearman
(Fisher) cae dentro de [−0.3, +0.3]; refutada si |ρ| ≥ 0.3 con p < 0.05; indeterminada en otro
caso.

**5b. Hazard h(τ) > 0.** Dos cohortes.
- **Cripto (Binance):** nacimiento = primera vela diaria; extinción funcional = criterio ACO
  (último cierre < 1% del máximo histórico, fecha = último día sobre el umbral); censura al
  último dato. Secundaria: retiro del par cuenta como extinción.
- **Bancos (FDIC, API pública):** todas las instituciones aseguradas; nacimiento = fecha de
  establecimiento; fin = institución inactiva (cualquier causa: fusión, adquisición, quiebra);
  secundaria: solo quiebras (lista de quiebras de la FDIC). **Entrada tardía:** las
  instituciones establecidas antes de 1934 entran al riesgo a la edad que tenían en 1934.
  Censura: 2026-09-27.

**H5b-i (positividad):** en toda banda de edad con ≥ 30 en riesgo hay al menos un fin
(bandas de 1 año en cripto, 5 años en bancos). Una banda con 0 fines no refuta por sí sola
(se reporta su cota superior 3/n) pero cuenta como "sin evidencia de positividad" en esa banda.
**H5b-ii (forma, afirmación de la v30):** el hazard crece con la edad — Spearman entre edad
de la banda y hazard > 0 (una cola). Respaldada si p < 0.05.

**5c. Fricción → Δ.** No se amplía: no hay series públicas de absorción post-quiebra
comparables a las de la cohorte 2008 (n = 6). Se declara como pendiente.

---

## Salidas previstas

`reconstruction_real/code/` (un script por punto, con log), `reconstruction_real/data/`
(resultados por caso) y un informe `reconstruction_real/audits/RESULTADOS_PREREGISTRO_2026-09-27.md`
con una tabla hipótesis → resultado → decisión y la sección **Desviaciones**.
