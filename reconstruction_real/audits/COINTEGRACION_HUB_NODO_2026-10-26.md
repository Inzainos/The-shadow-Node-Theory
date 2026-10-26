# Cointegración hub–nodo antes de interpretar R(t) y b — Resultados

**Fecha:** 2026-10-26
**Preregistro:** [`../preregistro/PREREGISTRO_COINTEGRACION_2026-10-26.md`](../preregistro/PREREGISTRO_COINTEGRACION_2026-10-26.md) (commit `e76545b`, antes del script).
**Script:** `code/cointegracion_hub_nodo.py` (determinista: ADF/EG sin RNG).
**Salidas:** `data/cointegracion_b_por_caso.csv`, `data/cointegracion_ratio_adf.csv`,
`data/cointegracion_resumen.csv`.

## Resultados

| Cantidad | Valor |
|---|---|
| Casos B (era estable, componentes versionados) | 446 |
| Ambos componentes I(1) (ADF p > 0.05) | **416 (93.3 %)** |
| Cointegrados entre los I(1) (Engle–Granger p < 0.05) | **51/416 (12.3 %)** |
| Ratio estacionario en B (ADF sobre log R) | 39/446 (8.7 %) |
| E3: ratio estacionario (descriptivo) | 3/234 |
| ACO: estimables por longitud (n ≥ 8) | 2/18; 0 estacionarios |

**Veredicto pre-especificado 2** (el que salió): <50 % de los pares B I(1)
están cointegrados (**12.3 %**). El ajuste de potencia sobre R(t) es en
general **espurio como estimación de equilibrio** en B; `b` es descriptivo
de la **deriva del ratio**, no de una relación de largo plazo hacia un hub.

## Lectura honesta

1. **B es el dominio donde el control dolía y el control falló.** Con 93 %
   de componentes I(1) y solo 12.3 % de cointegración entre ellos, para
   ~82 % de los 446 casos `log R = log hub − log nodo` es la diferencia de
   dos paseos aleatorios independientes: la regresión de tendencia sobre
   R(t) reproduce la deriva mecánica del ratio (Granger–Newbold). Esto
   **cuantifica** la cautela que el test de comercio ya había insinuado
   (convergencia, no satelización — `RECONSTRUCCION_DOMINIO_B_HUB_COMERCIO.md`):
   ahora se sabe que tampoco hay relación de equilibrio que estimar en la
   mayoría de los pares.
2. **El 12.3 % que sí cointegra existe** (51 pares): para esos casos, y
   solo esos, el ajuste de R(t) admite lectura de relación de largo plazo.
   La tabla por caso (`cointegracion_b_por_caso.csv`) los identifica.
3. **E3 (descriptivo, sin componentes):** 3/234 ratios estacionarios. Las
   fases de crecimiento epidémico SON tendencias — el `b` de E3 mide el
   exponente de esa tendencia por diseño; la preocupación de spuria aplica
   distinto (la curva no es ratio de dos series) y este test no la evalúa.
4. **ACO:** 16/18 series tienen n < 8 — el ADF no es estimable con
   honestidad. La windows cortas limitan tanto el ajuste como este control.

## Consecuencia para el corpus

- **B:** `b` se reporta como descriptor de deriva. La columna
  `cointegrado` del CSV por caso es el filtro para cualquier lectura de
  equilibrio (51 casos habilitados).
- **E3:** sin cambio — `b` ya se reporta como exponente de fase de
  crecimiento (tendencia), no como relación.
- **ACO:** sin cambio por longitud de datos; el control no es exigible.

## Qué NO afirma esta prueba

- No "mata" el corpus: acota la interpretación de `b` en B, que ya estaba
  bajo cautela por el test de comercio. No toca E1/E2/C (componentes no
  versionados ni series de ratio).
- No evalúa cointegración en E3/ACO (sin componentes); su ADF de ratio es
  descriptivo.

## Cómo regenerar

```sh
python reconstruction_real/code/cointegracion_hub_nodo.py   # ~4 s
```

---

*Fractal Core Research · Tlaxcala, México · 2026-10-26*
