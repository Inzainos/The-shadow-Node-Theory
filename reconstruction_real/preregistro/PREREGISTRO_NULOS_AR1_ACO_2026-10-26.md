# PREREGISTRO — Nulos AR(1) para la convergencia ACO-A

**Fecha:** 2026-10-26 · **Commit de este preregistro:** anterior a todo script,
dato o resultado de la prueba. **Autor de la decisión estadística:** pendiente
5.1 de `PENDIENTES_SNT.md`, redactado antes de ejecutar nada.

---

## Pregunta

¿La convergencia de `|log₁₀ m|` hacia 0 en las 18 series reales de ACO
(mediana de inicio ≈ 0.29 → mediana final ≈ 0.05-0.07 según agregación) es
una **firma del colapso** o es explicable por **regresión a la media de un
proceso AR(1) cuya media empírica es ≈ 0, más la regla de selección de las
ventanas** (terminan en la fecha del evento de absorción)?

## Datos y medida exacta (fijada ANTES de correr)

- Serie por caso: `snt_corpus_aco_timeseries_v29.csv`, puntos con `t > 0` y
  `R > 0`, ordenados por `t`. n = 18 casos.
- Por caso: `x_t = log₁₀(R_t)`; `d_ini = |x_0|`, `d_fin = |x_T|` (T = último
  punto del caso). **Sin retícula interpolada**: inicio y fin crudos.
- Estadístico global: `S_obs = mediana de d_fin sobre los 18 casos`.
  Referencia descriptiva: mediana de `d_ini`.

## Nulos pre-especificados

### N1 — Dinámica propia (AR(1) por caso, anclado al inicio)

Por caso, ajustar por OLS sobre SU serie:

```
x_t = μ + φ·(x_{t-1} − μ) + ε_t,   ε ~ N(0, σ_ε²)
```

con `μ = media muestral de x`, `φ = autocorrelación lag-1 de (x − μ)`
(lag-1 de los valores, no de residuos — AR(1) nivel), `σ_ε = std muestral
de los incrementos × sqrt(1 − φ²)/... ` — NO: se fija explícitamente
`σ_ε = std(ddof=1) de (x_t − μ − φ·(x_{t-1} − μ))`. Clamp `φ ∈ [0, 0.995]`.

Réplicas: M = 2 000 por caso, semilla global 20261026, generador
`numpy.random.default_rng(20261026)`. Cada réplica: longitud = n del caso,
`x*_0 = x_0` observado (anclado), ruido iid gaussiano.

Distribución nula de S: por réplica r, `S*_r = mediana sobre los 18 casos de
|x*_{T(c)}|`. **p_N1 = P(S* ≤ S_obs)** (una cola inferior: ¿es la
convergencia observada MÁS cerrada de lo que la propia dinámica produce?).

### Contraste B — ventanas que NO terminan en evento (regla de selección)

Las series B (PIBpc hub/nodo, era estable, del paquete de la tela v2) NO
terminan en un evento de colapso: terminan en 2018 por decisión de ventana.
Medir el MISMO estadístico: `S_B = mediana de |log₁₀(R_{2018}/1)|` sobre los
casos B. Si `S_B ≫ S_obs`, la convergencia terminal está ligada a ventanas
acabadas en evento (regla de selección), no solo a la dinámica.

## Veredictos pre-especificados (se reporta el que salga, sin re-interpretar)

1. **p_N1 > 0.05** → "la convergencia observada está DENTRO de lo que la
   dinámica AR(1) de las propias series produce": explicada por regresión a
   la media hacia μ ≈ 0. La convergencia no aporta evidencia adicional de
   'firma' más allá de la dinámica ya medida.
2. **p_N1 ≤ 0.05** → la convergencia observada es MÁS cerrada que la dinámica
   propia: hay estructura adicional (p. ej. la selección del endpoint). NO se
   interpretará como 'firma del colapso' por sí sola; se reporta como
   desviación del nulo y qué la explicaría.
3. El contraste B se reporta SIEMPRE como descriptivo del rol de la regla
   de selección, sin test de hipótesis entre dominios (regla del repo: no
   se ordena entre dominios).

## Qué NO afirma esta prueba

- No refuta ni confirma ACO-A: acota CUÁNTO de la convergencia reportada es
  mecánica (regresión a la media + selección de ventana).
- No usa la retícula interpolada de la tela (los 0.292/0.071 publicados
  salen de la retícula de fase; aquí se mide sobre serie cruda — la
  diferencia se reporta, no se reconcilia a la fuerza).

## Salidas

- Script: `reconstruction_real/code/nulos_ar1_aco.py` (semilla 20261026).
- Datos: `reconstruction_real/data/nulos_ar1_aco.csv` (por caso: n, φ, μ,
  σ_ε, d_ini, d_fin, cuantiles del nulo) + resumen global.
- Informe: `reconstruction_real/audits/NULOS_AR1_ACO_2026-10-26.md`.
