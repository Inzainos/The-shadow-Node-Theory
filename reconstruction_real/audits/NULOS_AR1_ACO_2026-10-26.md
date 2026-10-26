# Nulos AR(1) para la convergencia ACO-A — Resultados

**Fecha:** 2026-10-26
**Preregistro:** [`../preregistro/PREREGISTRO_NULOS_AR1_ACO_2026-10-26.md`](../preregistro/PREREGISTRO_NULOS_AR1_ACO_2026-10-26.md) (commit `a253b15`, ANTES del script y de los datos).
**Script:** `code/nulos_ar1_aco.py` (semilla 20261026, M=2 000 réplicas/caso).
**Salidas:** `data/nulos_ar1_aco.csv` (por caso), `data/nulos_ar1_resumen.csv`.

## Pregunta

¿La convergencia de `|log₁₀ m|` hacia 0 en las 18 series reales de ACO
(mediana de inicio 0.2917 → final **0.0712**, serie cruda) es una firma del
colapso o es explicable por regresión a la media de un proceso AR(1) cuya
media empírica es ≈ 0, más la regla de selección de las ventanas?

## Resultados

| Cantidad | Valor |
|---|---|
| S_obs (mediana de \|log₁₀ R_T\|, 18 casos) | **0.0712** |
| Mediana de inicio (referencia) | 0.2917 |
| N1 — nulo AR(1) propio: mediana [p5, p95] | 0.1021 [0.0804, 0.1347] |
| **p_N1 = P(S\* ≤ S_obs), una cola inferior** | **0.0130** |
| Contraste B (n=446, terminan en 2018 por ventana) | mediana final **0.2069** (inicio 0.1742) |

**Veredicto pre-especificado 2** (el que salió): la convergencia observada
es **más cerrada que la dinámica propia** de las series — S_obs queda por
debajo del percentil 5 del nulo. Se reporta como desviación del nulo y NO
se interpreta como "firma del colapso" por sí sola.

## Lectura honesta

1. **No es pura regresión a la media.** El nulo N1 replica la dinámica
   AR(1) de cada caso (su μ, su φ, su σ, anclado al inicio observado) y
   produce terminales con mediana 0.102 — el 0.071 observado es
   significativamente MÁS cerrado (p = 0.013). Una reversión mecánica al
   μ ≈ 0 de cada serie NO alcanza para explicar la mediana observada.
2. **El contraste B señala la regla de selección.** Las ventanas B —
   idéntica construcción salvo que NO terminan en un evento — NO convergen
   (0.207, por encima de su propio inicio 0.174). La convergencia
   terminal está ligada a ventanas que se cierran EN el evento de
   absorción/colapso. Eso es consistente con dos mecanismos no
   distinguibles con estos datos: (a) las ventanas ACO se cortan en
   momentos en que la razón está en paridad (la absorción ocurre cerca
   de R ≈ 1 — p. ej. la vía FDIC de WaMu), o (b) la dinámica final
   acelera hacia 1 justo antes del evento. Esta prueba no las separa.
3. **La convergencia es una afirmación de MEDIANA, no universal.** Por
   caso, la tabla muestra casos que terminan lejos de 1 (MySpace
   \|log R_T\| = 1.079, Azteca 0.908, Nokia 0.914) junto a los que
   terminan en paridad (Sun 0.009, PanAm 0.013). La mediana converge;
   la cola no.
4. **Nota de medida:** la mediana final cruda (0.0712) coincide con la
   publicada desde la retícula interpolada (0.071) — la medida no depende
   de la interpolación.

## Qué NO afirma esta prueba

- No refuta ni confirma ACO-A: acota cuánto de la convergencia es mecánico.
  El residuo (0.071 vs 0.102 del nulo) queda atribuido a la regla de
  selección y/o a dinámica terminal real — la prueba los agrupa, no los
  separa.
- No se ordena nada entre dominios (regla del repo): B se reporta como
  contraste descriptivo, no como test ACO-vs-B.

## Sensibilidad a φ (observación 5 del operador, 2026-10-26)

16/18 series tienen n < 8 puntos: φ estimado es ruidoso. Re-corrido el
nulo perturbando φ por caso en ±0.05 y ±0.15 (`code/sensibilidad_nulos_ar1.py`,
semilla 20261026):

| Perturbación | p_N1 |
|---|---|
| φ − 0.15 | 0.0055 |
| φ − 0.05 | 0.0120 |
| φ (original) | 0.0130 |
| φ + 0.05 | 0.0130 |
| φ + 0.15 | 0.0040 |

**Robusto en todo el rango** (0.004–0.013, todos < 0.05): la conclusión
"más cerrada que la dinámica propia" NO depende de la precisión de φ.

## Cómo regenerar

```sh
python reconstruction_real/code/nulos_ar1_aco.py   # ~7 s, determinista
```

---

*Fractal Core Research · Tlaxcala, México · 2026-10-26*
