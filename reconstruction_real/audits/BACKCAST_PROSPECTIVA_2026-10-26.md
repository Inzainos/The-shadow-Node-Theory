# Backcast de la prueba prospectiva — actualización con censura por seguimiento

**Actualizado:** 2026-10-27
**Preregistro validado:** `../preregistro/PREREGISTRO_PROSPECTIVA_CRIPTO_2026-10-26.md`
(df888d0) + **adenda de receta** (`ADENDA_PROSPECTIVA_RECETA_2026-10-26.md`,
mismo día — la ventana prospectiva aún no existe).
La clasificación de seguimiento incompleto se incorpora con
`../preregistro/ADENDA5_PROSPECTIVA_DELISTADOS_Y_HASH_2026-10-27.md`.
**Datos:** `data/binance_cierres_diarios.csv.gz` (versionados, corte 2026-08-31).
**Receta:** la misma del preregistro, aplicada a la ventana PASADA
**2025-08-31 → 2026-08-31** — congelamiento al 2025-08-31 sin lookahead.
La clasificación de pares sin cierre al fin de ventana se actualiza según
la **ADENDA 5**: se censuran, no se cuentan como colapsos ni supervivientes.

## Resultado vigente (ADENDA 5)

| Predicción | Resultado | Veredicto |
|---|---|---|
| **P1a** — al menos un colapso observado | **53** de 389 candidatos; 55 censurados por falta de seguimiento hasta el fin | ✓ RESPALDADA (peso bajo) |
| **P2** — mediana Δ en banda [−3.270, −0.115] | **mediana Δ = −0.961** (n = 22 maduros) | ✓ RESPALDADA |
| **P3** — equivalencia \|ρ(b, Δ)\| < 0.3 | **ρ = +0.189**, IC95 [−0.253, +0.566] (n = 22) | INCONCLUSO: el IC rebasa +0.3 |

La tasa descriptiva es 53/389 (13,62%). Los 55 censurados permanecen en el
denominador fijado, pero no se clasifican como eventos ni como no-eventos.

## Cambio metodológico

En la versión anterior del backcast, 89 pares se contaron como colapsos
usando el último cierre disponible como si fuera el cierre de fin de
ventana, aunque 55 no tenían seguimiento hasta esa fecha. La ADENDA 5 fija
que ese seguimiento incompleto es censura a la derecha:

- El par conserva sus cierres reales hasta la última fecha observada; no se
  imputan precios después de salir de cotización.
- El delisting por sí solo no cuenta como colapso. Sin observación al fin de
  ventana, el par no puede satisfacer ni refutar el criterio de persistencia.
- La receta de madurez, `b` y `Δ` no cambia. Al aplicarla a los 53 colapsos
  observados, quedan 22 maduros y medibles.

## Lectura honesta

1. **El backcast valida el proceso, no sustituye la prospectiva.** La
   ventana 2025–2026 es histórica; el veredicto que cuenta es el de la
   ventana congelada 2026-09-30 → 2027-09-30.
2. P1a sigue respaldada con peso evidencial bajo. La fracción descriptiva
   no se interpreta como prueba de hazard.
3. P2 permanece dentro de la banda. P3 es inconcluso: el intervalo de
   equivalencia no cabe entero en (−0.3, +0.3).

## Trazabilidad de las versiones

- **Vigente bajo ADENDA 5:** 53 colapsos observados, 55 censurados,
  mediana Δ = −0.9612, ρ = +0.1892, IC95 [−0.2526, +0.5657].
- **Versión previa, supersedida para la clasificación de eventos:** 89
  colapsos, 36 maduros, Δ = −0.9443, ρ = −0.1912, IC95 [−0.4891, +0.1465].
  Usó cierres terminales anteriores al fin como si fueran observaciones al
  cierre. Se conserva aquí para explicar la diferencia, no como resultado
  vigente.
- Los números intermedios (−0,947 / −0,195 / [−0,492, +0,143]) que
  aparecieron tras la re-descarga NO eran un efecto de los datos:
  eran **fuga del valle** — el script buscaba el ATH y el mínimo de Δ
  en la serie completa, incluyendo datos posteriores al fin de la
  ventana (diagnóstico del operador, confirmado al truncar). Bug
  corregido en `backcast_prospectiva.py` y `evaluar_prospectiva.py`
  (truncado en `fin`); el test
  `tests/test_evaluar_prospectiva.py` fija esta validación en CI.
- La mediana Δ y la correlación también cambian porque la muestra de
  colapsos maduros se reduce al censurar seguimientos incompletos.

## Re-clasificación bajo ADENDA 2 (observaciones del operador)

La ADENDA 4 retiró P1b y la fracción permanece descriptiva. Bajo la ADENDA
5, P1a ✓ · P2 ✓ · P3 INCONCLUSO; la conclusión de P3 sigue sin demostrar
equivalencia, ahora con el conjunto de casos que tienen seguimiento completo.

## Cómo regenerar

```sh
python reconstruction_real/code/backcast_prospectiva.py   # ~30 s
```

(script versionado tras la observación 1 del operador; reproduce los
números de arriba exactamente).

---

*Fractal Core Research · Tlaxcala, México · 2026-10-26*

## Nota sobre el sello y las mejoras posteriores (actualizada 2026-10-27)

El DOI 10.5281/zenodo.23678033 (release 2.7.3) contiene el estado sellado
antes de esta actualización y las ADENDA 1–4. La ADENDA 5 y la censura de
casos sin seguimiento completo son criterios **posteriores** a ese sello.
Se publicarán en un release/DOI nuevo antes de evaluar la ventana
2026-09-30 → 2027-09-30; por tanto, el evaluador futuro no será idéntico
al archivo 2.7.3, sino a la versión posterior sellada con la descarga y su
manifiesto de hashes antes de calcular resultados.
