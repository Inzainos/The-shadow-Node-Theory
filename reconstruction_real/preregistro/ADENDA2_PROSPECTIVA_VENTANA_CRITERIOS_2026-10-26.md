# ADENDA 2 al preregistro prospectivo — ventana, sellado y criterios recalibrados

**Fecha:** 2026-10-26 (tarde) · **Responde a:** `observaciones.md` del
operador (puntos 2, 3 y 4 — aceptados en su totalidad).

---

## 1. La ventana estaba mal anclada (observación 2)

**Reconocimiento:** el preregistro decía "los datos de la ventana NO
existen al escribir esto" — falso: el corte del archivo versionado es
2026-08-31 y el congelamiento se hizo el 2026-10-26; entre ambas fechas
hay ~8 semanas de datos reales ya existentes en Binance (no en el repo,
pero sí en el mundo).

**Corrección:** la ventana prospectiva se re-ancla al congelamiento REAL:
**2026-10-26 → 2027-10-26** (12 meses desde la fecha del congelamiento).
Todo lo anterior a 2026-10-26 es estado congelado; la ventana empieza en
la fecha del sellado de esta adenda. El preregistro original y la adenda 1
conservan su texto (append-only); esta adenda los sustituye en lo que
contradicen.

## 2. El sellado estaba mal afirmado (observación 3)

**Reconocimiento:** el DOI `10.5281/zenodo.23653089` se selló a las 01:33;
el preregistro prospectivo y la adenda 1 se escribieron después (03:02+).
Ese DOI NO contiene este preregistro, y el texto original no debía
insinuarlo.

**Estado real del sellado:** el commit git de esta adenda (con fecha
verificable por terceros) es el registro vigente del contenido completo:
preregistro df888d0 + adenda 1 (6b6324d) + esta adenda 2. El archivo
versionado de Zenodo pendiente es el del **release 2.7.1** (creado hoy,
contiene todo lo anterior); cuando Zenodo lo procese (o el autor lo suba),
ese DOI reemplaza al 23653089 como sello de ESTE preregistro. Hasta
entonces, la afirmación honesta es: **sellado por git, sellado externo
pendiente de Zenodo.**

## 3. Criterios recalibrados (observación 4)

### P1 — dividida en P1a (firma) y P1b (banda falsable)

**Reconocimiento:** con tasa de colapso ~23%/año medida en el backcast,
"≥1 colapso en 409 candidatos" es prácticamente infalsable
(P(0) ≈ 0.77⁴⁰⁹ ≈ 10⁻⁴³). Como criterio de h(τ) > 0 tiene peso casi nulo.

**P1a (firma):** al menos 1 colapso crudo en la ventana — se reporta pero
se declara de **bajo peso evidencial**.
**P1b (banda, falsable en ambos sentidos):** la fracción de colapsos
crudos de la cohorte (409 candidatos) cae en **[10%, 60%]**. Debajo de 10%
o encima de 60% falsa P1b. Banda fijada desde el backcast (22.9% en el año
bajista) y la vaga histórica del hazard.

### P3 — criterio de equivalencia en lugar del umbral puntual

**Reconocimiento:** con ρ verdadero = 0, el criterio |ρ̂| < 0.3 "falsa" por
azar 37% de las veces con n = 11 y 7.6% con n = 36; y con el IC95 del
backcast [−0.489, +0.146] (n = 36) NO se demuestra |ρ| < 0.3. El umbral
puntual confunde "no detecté" con "demostré ausencia".

**P3 recalibrado (TOST por IC):** la ortogonalidad queda demostrada solo
si el **IC95 de ρ(b, Δ)** cabe entero dentro de (−0.3, +0.3). Si el IC
cruza ±0.3: **inconcluso a ese n** — no falso, no demostrado.
**Nota de potencia (pre-declarada):** con n = 36 el IC ya mide ±0.32 de
ancho; se necesita n ≳ 50 para que la demostración sea alcanzable si el
ρ verdadero es ~0. Si la ventana produce menos colapsos maduros, P3 se
declarará inconcluso por diseño — eso también es un resultado.

## 4. Consecuencia para el backcast ya publicado

Bajo los criterios recalibrados, el backcast 2025-08-31 → 2026-08-31
re-clasifica como: **P1a ✓ · P1b ✓ (22.9% en banda) · P2 ✓ · P3
inconcluso** (IC [−0.489, +0.146] cruza −0.3; n = 36 insuficiente para
demostrar equivalencia). El informe original reportó P3 ✓ bajo el umbral
puntual; esa lectura queda corregida aquí.


## Nota de versión (CORREGIDA 2026-10-26, validación del operador)

Versión original de esta adenda: Δ = −0,944; ρ = −0,191; IC95
[−0,489, +0,146] (archivo con corte en el fin de la ventana). Tras la
re-descarga el número se movió a −0,947/−0,195 y lo atribuí a los
datos nuevos. **Era un error de diagnóstico del operador confirmado:
la causa era una fuga del valle** — el script buscaba el mínimo de Δ y
el ATH en la serie COMPLETA (incluidos los datos posteriores al fin de
la ventana), así que el resultado dependía de cuándo se descargara el
archivo. Corregido el truncado (fit dentro de la ventana): sobre el
archivo completo el backcast da **otra vez −0,944 / −0,191 /
IC [−0,489, +0,146] — versión VIGENTE**, idéntica a la original. Los
números intermedios (−0,947/−0,195) quedan como artefacto documentado
del bug, no como versión.
