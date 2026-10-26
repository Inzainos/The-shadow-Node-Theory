# PREREGISTRO — Prueba prospectiva ACO-A: cohorte cripto congelada

**Fecha de congelamiento:** 2026-10-26 · **Committeado ANTES de cualquier
dato del periodo de evaluación.** **Origen:** pendiente 5.4 de
`PENDIENTES_SNT.md`. **Sellado externo:** Zenodo (DOI 10.5281/zenodo.23653089
para el estado actual; este preregistro queda sellado en el próximo release
o carga que haga el autor).

---

## Qué se congela

- **Cohorte:** los **472 pares** de `data/binance_cierres_diarios.csv.gz`
  vivos al corte de datos **2026-08-31**, con su ATH y precio de congelamiento
  versionados en
  `reconstruction_real/data/cohorte_congelada_cripto_2026-10-26.csv`
  (columnas: par, n_obs, fecha_nacimiento, ath_corte, fecha_ath,
  precio_corte, dd_pct_vs_ath). De ellos, **409** tienen dd < 99% al
  congelar (los otros 63 ya cumplieron el umbral contra su ATH histórico
  pero siguen listados — se reportan aparte).
- **Ventana de evaluación:** **2026-08-31 → 2027-08-31** (12 meses desde el
  corte del congelamiento). Los datos de la ventana NO existen al escribir
  esto.

## Definición de colapso (fijada AHORA, no se toca)

Un par **colapsa** en la ventana si su precio cae por debajo del **1 % de
su `ath_corte`** (drawdown ≥ 99 % contra el ATH congelado) y **no se
recupera** por encima de ese umbral al final de la ventana (extinción
funcional — el mismo criterio de `hazard_crypto.py`).

## Predicciones escritas (falsables, una por afirmación ACO-A)

**P1 — h(τ) > 0 ("ningún sistema es eterno"):** al menos **1 de los 409
candidatos** colapsa dentro de la ventana. Falsación: 0 colapsos.

**P2 — Δ medible y en banda histórica:** para cada par colapsado, la
ventana de caída post-ATH (desde su `fecha_ath` hasta el fin de la ventana,
ajuste log-log con ≥ 20 puntos, receta de `aco_cohortes_ampliadas.fit`)
produce un Δ finito. Predicción de banda: la **mediana de los Δ
prospectivos cae dentro de [−3.270, −0.115]** (p5–p95 del histórico
cripto, `orthogonality_crypto_v25.csv`, n=11, mediana histórica −0.330).
Falsación: mediana fuera de la banda, o Δ no medible en ≥ la mitad de los
colapsos con ≥ 20 puntos disponibles.

**P3 — Ortogonalidad b ⊥ Δ:** para los colapsos con b (subida pre-ATH,
misma receta) y Δ ambos medibles, el Spearman ρ(b, Δ) prospectivo cae
dentro de **|ρ| < 0.3** (criterio pre-registrado del test original;
histórico: ρ = +0.009, n = 11). Falsación: |ρ| ≥ 0.3 con n ≥ 5.

**Nota honesta de alcance:** la convergencia a m ≈ 1 no se predice aquí —
un par de precios no es una razón hub/nodo, y la prueba 5.1 dejó la
convergencia ligada a ventanas de evento sin separar selección de dinámica.
Esta prospectiva prueba hazard, forma de absorción y ortogonalidad — no
convergencia.

## Criterios de evaluación (no se cambian después)

1. Los datos de la ventana se obtienen con `descargar_binance_klines.py`
   o los deja el operador en Descargas (patrón CSV) — sin redefinir la
   cohorte congelada.
2. Colapsos, Δ, b y ρ se calculan con la receta anterior, sin ajustes.
3. El informe se escribe en `audits/RESULTADOS_PROSPECTIVA_CRIPTO.md` con
   la fecha real de evaluación, favorable o desfavorable.
4. Evaluación interina permitida (p. ej., a los 6 meses) SIN cambiar
   criterios; la evaluación final es al cierre de la ventana.

## Qué NO afirma esta prueba

- No predice QUÉ par colapsa ni cuándo — solo las propiedades del conjunto.
- No usa la cohorte para predicción de mercado; es la prueba falsable de
  ACO-A que el corpus histórico no puede dar (todos sus casos son
  retrospectivos).

## Salidas al congelar (HOY)

- `data/cohorte_congelada_cripto_2026-10-26.csv` (472 pares, versionada).
- Este preregistro (fecha de git verificable + sellado Zenodo en el
  próximo release).
