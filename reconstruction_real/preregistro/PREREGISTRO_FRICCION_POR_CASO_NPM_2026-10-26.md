# PREREGISTRO — Fricción por caso vs b: la prueba dentro de un dominio (npm)

**Fecha:** 2026-10-26 · **Committeado ANTES de correr el análisis.**
**Origen:** pendiente 5.5 de `PENDIENTES_SNT.md` ("medir φ por caso") + el
punto 6 de la nota del Axioma 5 ("para reclamar fricción como campo medido
se requiere fricción continua por caso").

---

## Por qué esta prueba es la que faltaba

El ancla fricción → b del Axioma 5 (ρ = −0.68 caso-nivel) quedó hoy medido
como descriptivo del agrupamiento de dominios (nulo por dominios p = 0.053,
MixedLM p = 0.57 — `MODEL_JERARQUICO_B_2026-10-26.md`). La razón de fondo:
la fricción era CONSTANTE por dominio. La cohorte npm es la única del
corpus con **fricción codificada POR CASO y ANTES de ver las series**
(fundación = 3, corporativa = 2, otra organización = 1, individual = 0 —
declarado post-hoc en el follow-up original, pero codificado a priori),
y con n = 450 dentro de UN SOLO dominio. Sin confundido dominio-fricción.

## Receta (fijada antes de correr)

- **Datos:** `npm_cohorte_aco.csv.gz` (450 paquetes con nacimiento,
  b_subida, friccion_a_priori, disparador).
- **Test principal:** Spearman(friccion_a_priori, b_subida), n = 450.
  Reportado a 2 colas SIEMPRE; el test direccional usa 1 cola (p/2) SOLO
  para el veredicto.
- **Por nivel:** mediana de b_subida por nivel de fricción (0..3) con
  p25/p75; Kruskal-Wallis entre niveles con n ≥ 30.
- **Control por disparador** (abrupto / anunciado / sin_clasificar):
  Spearman dentro de cada clase con n ≥ 30, y el test principal controlado
  (diferencia de ρ reportada sin formalizar).

## Predicción direccional (pre-registrada)

Bajo el Axioma 5 ("la fricción limita la velocidad"): a mayor fricción
institucional del paquete, MENOR el exponente de subida b_subida →
**ρ(fricción, b_subida) < 0**. Dirección contraria (ρ ≥ 0) o nula: no
respaldada.

## Alcance honesto (lo que esta prueba NO es)

- `b_subida` es el exponente de crecimiento de las descargas del paquete
  (serie única), NO una razón hub/nodo. La dirección se prueba por analogía
  declarada (fricción limita velocidad), no como el mismo objeto del ancla
  cross-dominio.
- Un dominio (npm), una cohorte (paquetes que colapsaron): no se ordena
  contra otros dominios (regla del repo).
- La fricción aquí es ordinal a-priori 0..3, no un campo continuo medido:
  es lo más cercano a "φ por caso" que el corpus tiene hoy.

## Veredictos pre-especificados

1. **ρ < 0 con p 1 cola < 0.05** → dirección del Axioma 5 respaldada POR
   CASO dentro de npm: primera evidencia estructuralmente limpia de
   fricción → b.
2. **ρ ≥ 0 o p ≥ 0.05** → no respaldada por esta vía; se reporta la cifra
   con su intervalo y NO se interpreta.
3. El Kruskal-Wallis y el control por disparador se reportan SIEMPRE como
   descriptivos.

## Salidas

- Script: `reconstruction_real/code/friccion_por_caso_npm.py`
  (determinista, sin RNG).
- Informe: `reconstruction_real/audits/FRICCION_POR_CASO_NPM_2026-10-26.md`.
- Datos: resumen CSV en `reconstruction_real/data/`.
