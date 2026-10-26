# ADENDA 4 — La banda P1b queda RETIRADA: la fracción de colapso mide el régimen del mercado, no h(τ)

**Fecha:** 2026-10-26 (cierre) · **Responde a:** `PENDIENTES_SNT.md`
post-línea-185 ("P1b con banda [10%, 60%], muy ancha") — la observación
del operador resultó subestimar el problema.

## La medición que decide

Fracción de colapsos por ventana (misma receta del backcast, congelar
sin lookahead y evaluar 12 meses):

| Ventana | Colapsos/candidatos | Fracción |
|---|---|---|
| 2022-08-31 → 2023-08-31 | 6/321 | **1.9%** |
| 2023-08-31 → 2024-08-31 | 4/339 | **1.2%** |
| 2024-08-31 → 2025-08-31 | 24/363 | **6.6%** |
| 2025-08-31 → 2026-08-31 | 89/389 | **22.9%** |

**La banda P1b [10%, 60%] habría FALSADO en 3 de las 4 ventanas
históricas** (1.9%, 1.2% y 6.6% quedan debajo del piso). Y no porque
h(τ) fallara — el hazard siguió positivo (hubo colapsos todos los
años) — sino porque la FRACCIÓN la domina el régimen del mercado
(alcista/bajista), no la ley de mortalidad. La banda fue calibrada
sobre el año más extremo del historial reciente (2025-26, año bajista)
— error mío de calibración, captado primero por el ojo del operador
("muy ancha") y confirmado al medir la dispersión.

## La corrección

- **P1b queda RETIRADA como criterio.** Una banda de fracción no es un
  test de h(τ) a esta escala: es un test del ciclo del mercado con
  n=1.
- **P1a se mantiene** (≥ 1 colapso crudo = firma de h(τ) > 0) con su
  peso evidencial BAJO ya declarado en la ADENDA 2.
- **El contenido real de la prospectiva son P2 (Δ en banda) y P3 (TOST
  de ortogonalidad)** — ambos independientes del régimen (miden la
  FORMA de los colapsos, no cuántos).
- La fracción de colapso de la ventana 2026-09-30 → 2027-09-30 se
  REPORTARÁ siempre como descriptiva del régimen, sin compuerta.

## Qué NO cambia

La cohorte congelada v2, la ventana (2026-09-30 → 2027-09-30), P2, P3
y sus criterios de la ADENDA 2. Esta adenda solo retira P1b y declara
la fracción como descriptiva.
