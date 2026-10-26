# ADENDA al preregistro prospectivo — receta exacta de b y Δ (post-backcast)

**Fecha:** 2026-10-26 · **Se añade a:** `PREREGISTRO_PROSPECTIVA_CRIPTO_2026-10-26.md`
(commit `df888d0`). Se committea ANTES de que exista cualquier dato del
periodo prospectivo (2026-08-31 → 2027-08-31) — la ventana aún no ha
ocurrido.

## Motivo

El backcast de validación (`BACKCAST_PROSPECTIVA_2026-10-26.md`) aplicó la
receta del preregistro a la ventana pasada 2025-08-31 → 2026-08-31 y expuso
una ambigüedad: el preregistro decía "desde su fecha_ath hasta el fin de la
ventana" para Δ, y no fijaba filtro de madurez. Con esa lectura, P3 fallaba
(|ρ| = 0.435, n = 89) por artefacto: sin madurez, entran subidas degeneradas
(b < 0, pares que nunca subieron) y el Δ hasta-fin-de-ventana arrastra el
valle. Con la receta del test histórico (`orthogonality_test.py`), las tres
predicciones pasan. Esta adenda fija la receta DEFINITIVA para la
evaluación prospectiva.

## Receta definitiva (la del test histórico, sin cambios)

Para cada par colapsado en la ventana prospectiva:

1. **Madurez (filtro):** ≥ 120 días de serie antes del ATH y ≥ 120 días de
   datos después del ATH. Sin madurez: el caso se reporta como colapso
   (cuenta para P1) pero queda FUERA de P2/P3.
2. **b:** ajuste log-log (≥ 20 puntos) sobre nacimiento → ATH, con x =
   días desde el nacimiento (receta `orthogonality_test.py`).
3. **Δ:** ajuste log-log (≥ 20 puntos) sobre **ATH → siguiente valle**
   (argmin post-ATH), NO hasta el fin de la ventana.
4. **P2 (banda):** la mediana de los Δ medibles cae dentro de
   [−3.270, −0.115] — sin cambio.
5. **P3 (ortogonalidad):** |ρ(b, Δ)| < 0.3 sobre los colapsos con ambos
   medibles y madurez — sin cambio.

## Veredicto del backcast (window 2025-08-31 → 2026-08-31, con esta receta)

- P1: 89 colapsos de 389 candidatos → ✓
- P2: mediana Δ = −0.944, dentro de banda → ✓
- P3: ρ(b, Δ) = −0.191 (p = 0.26), n = 36 → ✓

El backcast es validación del DISEÑO con datos ya versionados; la
prospectiva sellada se evalúa en 2027-08-31 y su veredicto es el que cuenta.
