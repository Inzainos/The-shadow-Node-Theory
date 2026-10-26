# Backcast de la prueba prospectiva — Validación del diseño

**Fecha:** 2026-10-26
**Preregistro validado:** `../preregistro/PREREGISTRO_PROSPECTIVA_CRIPTO_2026-10-26.md`
(df888d0) + **adenda de receta** (`ADENDA_PROSPECTIVA_RECETA_2026-10-26.md`,
mismo día — la ventana prospectiva aún no existe).
**Datos:** `data/binance_cierres_diarios.csv.gz` (versionados, corte 2026-08-31).
**Receta:** la misma del preregistro, aplicada a la ventana PASADA
**2025-08-31 → 2026-08-31** — congelamiento al 2025-08-31 sin lookahead.

## Resultado (con la receta histórica exacta — la definitiva tras la adenda)

| Predicción | Resultado | Veredicto |
|---|---|---|
| **P1** — h(τ) > 0: ≥ 1 colapso en la ventana | **89 colapsos** de 389 candidatos (dd < 99% al congelar) | ✓ RESPALDADA |
| **P2** — mediana Δ en banda [−3.270, −0.115] | **mediana Δ = −0.944** (n = 36 medibles con madurez) | ✓ RESPALDADA |
| **P3** — ortogonalidad \|ρ(b, Δ)\| < 0.3 | **ρ = −0.191** (p = 0.26, n = 36) | ✓ RESPALDADA |

**Las tres predicciones de la perspectiva ACO-A pasan el backcast.**

## El hallazgo metodológico (por qué hubo dos corridas)

La primera corrida usó la literal del preregistro ("Δ desde fecha_ath hasta
el fin de la ventana", sin madurez) y P3 FALLÓ: |ρ| = 0.435 (n = 89). La
autopsia mostró que era **artefacto de receta**, no señal real:

1. Sin filtro de madurez entran subidas degeneradas (pares cuyo "ATH" es
   casi su primer precio; b < 0 por construcción).
2. El Δ hasta fin de ventana arrastra el tramo post-valle, contaminando el
   exponente de caída.

Con la receta del test histórico (`orthogonality_test.py`: madurez ≥ 120
días por lado, Δ = ATH → siguiente valle), la ortogonalidad vuelve a \|ρ\| <
0.3. La adenda fija esa receta como la definitiva para la evaluación
prospectiva — **committeada antes de que exista un solo dato de la ventana
2026-08-31 → 2027-08-31**, así que la prospectiva no queda contaminada.

## Lectura honesta

1. **El backcast valida el diseño, no sustituye la prospectiva.** El
   conocimiento de la ventana 2025-2026 existía al diseñar; el veredicto que
   cuenta es el de 2027-08-31 con criterios sellados desde hoy.
2. **La ventana fue dura y las predicciones aguantaron:** 89 colapsos
   (23 % de la cohorte) en un año de mercado bajista — h(τ) > 0 no
   sobrevivió "por poco": sobrevivió masivamente. El Δ mediano (−0.944) es
   más pronunciado que el histórico (−0.330) pero dentro de la banda
   pre-registrada.
3. **P3 con n = 36 es la ortogonalidad mejor medida del corpus cripto**
   (histórica: n = 11). ρ = −0.191 es compatible con cero a este n.
4. **La lección de proceso:** la ambigüedad de receta la cazó el backcast,
   no la prospectiva — para eso se hizo. Sin el backcast, la evaluación de
   2027 habría corrido con la receta literal y quizá reportado una
   "falsación" que era un bug de ventana.

## Re-clasificación bajo ADENDA 2 (observaciones del operador)

Los criterios recalibrados (`ADENDA2_PROSPECTIVA_VENTANA_CRITERIOS_2026-10-26.md`)
re-clasifican este backcast: **P1a ✓ · P1b ✓ (22.9% en banda [10%, 60%])
· P2 ✓ · P3 INCONCLUSO** — el IC95 de ρ ([−0.489, +0.146], n = 36) cruza
−0.3, así que a este n no se DEMUESTRA la ortogonalidad, solo no se
detecta desviación. La lectura original (P3 ✓ bajo umbral puntual) queda
corregida; el umbral puntual confundía "no detecté" con "demostré".

## Cómo regenerar

```sh
python reconstruction_real/code/backcast_prospectiva.py   # ~30 s
```

(script versionado tras la observación 1 del operador; reproduce los
números de arriba exactamente).

---

*Fractal Core Research · Tlaxcala, México · 2026-10-26*
