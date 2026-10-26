# Fricción por caso vs b (npm, n=450) — Resultados

**Fecha:** 2026-10-26
**Preregistro:** [`../preregistro/PREREGISTRO_FRICCION_POR_CASO_NPM_2026-10-26.md`](../preregistro/PREREGISTRO_FRICCION_POR_CASO_NPM_2026-10-26.md) (commit `df888d0`, antes del script).
**Script:** `code/friccion_por_caso_npm.py` (determinista, sin RNG).
**Salida:** `data/friccion_por_caso_resumen.csv`.

## Pregunta

El ancla fricción → b del Axioma 5 quedó hoy medido como descriptivo del
agrupamiento de dominios (nulo por dominios p = 0.053, MixedLM p = 0.57).
La cohorte npm es la única con **fricción por caso** (0..3 a priori) dentro
de **un solo dominio** — la estructura que faltaba. ¿Sobrevive ahí la
dirección "más fricción → menor b"?

## Resultados

| Medida | Valor |
|---|---|
| Spearman(fricción, b_subida), n=450 | **+0.0932** (p 2 colas 0.048; p 1 cola dirección ρ<0 = **0.976**) |
| b mediana, fricción 0 (individual, n=139) | +0.441 |
| b mediana, fricción 1 (org, n=308) | +0.541 |
| b mediana, fricción 2 (corporativa, n=3) | +1.408 (n demasiado chico) |
| Control anunciado (n=33) | ρ = −0.070 (p = 0.70) |
| Control sin_clasificar (n=416) | ρ = +0.115 (p = 0.019) |

**Veredicto pre-especificado 2** (el que salió): NO respaldada por esta vía.
La correlación observada es **positiva** — la dirección OPUESTA a la
pre-registrada (ρ<0). Con el test direccional del preregistro, p = 0.976.

## Lectura honesta

1. **La vía por caso existe y quedó probada — y salió negativa.** Esta era
   la estructura limpia que el ancla cross-dominio no tenía: fricción por
   caso, un dominio, n = 450. La dirección del Axioma 5 no se sostiene
   aquí; el signo observado (+0.09) apunta, si acaso, al lado contrario
   (paquetes de organizaciones crecen un poco más rápido que los
   individuales — plausible por recursos, no por "protección").
2. **El estado del ancla fricción → b queda triplemente negativo:**
   (i) cross-dominio caso-nivel: artefacto del agrupamiento (p_perm =
   0.053; MLM p = 0.57); (ii) dominios nuevos pre-registrados: ρ = −0.131,
   p = 0.39; (iii) por caso dentro de npm: ρ = +0.09, dirección contraria.
   El estatus ANCLADO del Axioma 5 descansa, como su propia nota ya decía,
   en fricción → Δ (cohorte 2008, n = 6) y en la fricción física
   astronómica — no en fricción → b.
3. **Nota de alcance (del preregistro, no añadida después):** b_subida es
   el exponente de crecimiento de descargas (serie única), no una razón
   hub/nodo. La analogía estaba declarada; si aún con esa generosidad la
   dirección no aparece, el resultado es informativo.

## Cómo regenerar

```sh
python reconstruction_real/code/friccion_por_caso_npm.py   # < 1 s
```

---

*Fractal Core Research · Tlaxcala, México · 2026-10-26*
