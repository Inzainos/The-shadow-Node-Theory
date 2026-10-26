# PREREGISTRO — Cointegración hub–nodo antes de interpretar R(t) y b

**Fecha:** 2026-10-26 · **Commit de este preregistro:** anterior a todo script,
dato o resultado. **Origen:** pendiente 5.2 de `PENDIENTES_SNT.md`.

---

## Pregunta

`R(t) = hub(t)/nodo(t)` y el ajuste `b` presuponen una relación de largo
plazo entre las dos series. Si `hub` y `nodo` son I(1) **no cointegrados**,
`log R = log hub − log nodo` es I(1) y cualquier regresión de tendencia
sobre `R(t)` es **espuria** (Granger–Newbold): `b` describiría la deriva
del ratio, no una relación de equilibrio. ¿Cuántos casos B tienen componentes
cointegrados y cuántos no?

## Alcance honesto (fijado antes de correr)

- **B (446 pares, era estable):** es el único dominio con AMBOS componentes
  versionados (`maddison_mpd2020.csv`, receta de `tela_exogena.py`: ventana
  `year_min..year_max` por caso, merge por año, `t = 1..n`). Engle–Granger
  aplicable por caso.
- **E3 (234) y ACO (18):** los componentes (hub y nodo por separado) NO
  están versionados — solo existe `R(t)`. Engle–Granger es imposible sin
  ellos. Se reporta ADF sobre `log R` como control descriptivo de la
  estacionariedad del ratio, sin interpretarlo como test de cointegración.

## Receta exacta

Por caso B (era estable):

1. `h_t = log(PIBpc_hub)`, `n_t = log(PIBpc_nodo)` sobre la ventana del caso.
2. ADF sobre cada componente (`statsmodels.tsa.stattools.adfuller`,
   `trend='c'`, `autolag='AIC'`): `p_h`, `p_n`. Ambos-I(1) ⟺ `p_h > 0.05`
   y `p_n > 0.05`.
3. Engle–Granger (`statsmodels.tsa.stattools.coint(h, n, trend='c',
   autolag='AIC')`) → `p_coint` (p-values MacKinnon). Cointegrado ⟺
   `p_coint < 0.05`.
4. ADF sobre `log R` del caso → `p_R` (¿el ratio es estacionario?).

Por caso E3/ACO: solo paso 4 sobre su `R(t)` crudo.

## Veredictos pre-especificados

Sobre los casos B con **ambos** componentes I(1):

1. **≥ 50% cointegrados** → "los pares B con tendencia común tienen relación
   de largo plazo; los ajustes de R(t) sobre ellos no son espurios como
   relaciones — b queda descriptivo del ratio hacia su equilibrio."
2. **< 50% cointegrados** → "los pares B I(1) mayoritariamente NO están
   cointegrados: el ajuste de potencia sobre R(t) es en general espurio
   como estimación de equilibrio; b es descriptivo de la deriva del ratio.
   Esto es consistente con el hallazgo de convergencia del test de comercio
   (RESULTADOS: hub comercial)."

El porcentaje de casos con ratio estacionario (`p_R < 0.05`) se reporta
siempre, en los tres dominios, como descriptivo. **No se agrupa entre
dominios ni se ordena.**

## Qué NO afirma esta prueba

- No "salva" ni "mata" el corpus B: acota la interpretación de `b` en
  presencia de tendencias. Los casos con componentes I(0) (estacionarios
  de por sí) no necesitan cointegración y se reportan aparte.
- E3/ACO quedan fuera del test de cointegración por datos (componentes no
  versionados), no por elección.

## Salidas

- Script: `reconstruction_real/code/cointegracion_hub_nodo.py`
  (determinista: ADF/EG no usan RNG).
- Datos: `reconstruction_real/data/cointegracion_b_por_caso.csv`,
  `cointegracion_ratio_adf.csv` (E3/ACO), `cointegracion_resumen.csv`.
- Informe: `reconstruction_real/audits/COINTEGRACION_HUB_NODO_2026-10-26.md`.
