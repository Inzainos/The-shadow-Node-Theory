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

## Potencia del test (observación 6 del operador, 2026-10-26)

"93% I(1)" y "12.3% cointegrado" son fallas en rechazar. Calibración por
simulación bajo cointegración CONOCIDA (`code/potencia_cointegracion.py`,
500 sims/config, semilla 20261026):

| n | ρ_err = 0.5 | ρ_err = 0.8 |
|---|---|---|
| 34 (mín B) | 64.8% | 23.8% |
| 69 (mediana B) | 92.2% | **48.2%** |
| 119 (máx B) | 97.4% | 80.0% |

Tamaño bajo no-cointegración (n=69): 9.8% (algo inflado vs nominal 5%).

**Consecuencia honesta (CORREGIDA 2026-10-26 tarde, observación del
operador):** el cálculo original trató el 12.3% como piso aplicando la
potencia sin descontar el TAMAÑO del test — pero EG sobre-rechaza bajo
la nula (tamaño medido M=3000: 10.2% a n=34, 8.6% a n=69, 6.9% a
n=119 con trend='c'; el nominal es 5%). El 12.3% observado está apenas
2–4 puntos POR ENCIMA del piso de falsos positivos. Corregida por
tamaño — con el TAMAÑO DE CADA n, no un tamaño único (corrección del
operador, segunda ronda) — π = (R − tamaño_n)/(potencia_n,ρ − tamaño_n),
todo desde el CSV M=3000 versionado (reproducible):

| (n, ρ_err) | tamaño | potencia | π |
|---|---|---|---|
| (119, 0.5) | 8.0% | 97.6% | 4.8% |
| (69, 0.5) | 9.0% | 92.6% | 3.9% |
| (119, 0.8) | 8.0% | 82.7% | 5.8% |
| (69, 0.8) — mediana de B | 9.0% | 45.9% | **8.9%** |
| (34, 0.8) | 10.3% | 23.3% | 15.4% |

**Ponderada por la distribución real de n en B** (segunda corrección
del operador: el 12.3% es una tasa agregada; restar un tamaño único a
cada fila es aproximación): tamaño ponderado 8.7% · potencia ponderada
92.6% (ρ=0.5) / 56.7% (ρ=0.8) → **π ponderada = 4.2% (ρ=0.5) /
7.4% (ρ=0.8)**.

**La tasa verdadera de cointegración en B está entre ~4% y ~15%, con
estimación puntual ~9% a la mediana de B y 4–7% ponderada.** El techo
anterior (~25%) era un artefacto de aplicar el tamaño de n=69 a la fila
de n=34. Lectura robusta: el 12.3% apenas supera el ruido del test. La
frase "para ~82% de B, log R es diferencia de paseos independientes"
del informe original queda retirada (ya lo estaba); lo que el dato
permite afirmar es que el equilibrio está **sin confirmar** en B con
este test a este n, y que b queda como descriptor de deriva mientras no
haya confirmación.

**Nota de reproducibilidad (corrección del operador):** los tamaños
citados antes como "estables M=3000" venían de una corrida inline no
versionada; el script tenía M=500. Corregido: `potencia_cointegracion.py`
ahora corre M=3000 (potencias y tamaños) y el CSV versionado es la
fuente única de la tabla de arriba.

**Diagnóstico del sobre-rechazo (a pedido del operador):** EG
sobre-rechaza en series cortas con ambos trends (10.2%/11.1% a n=34;
7.6%/9.2% a n=69) y converge hacia el nominal a n=119 (6.9%/8.5%). No
es el generador (series sin drift) ni específico de trend='c': es
**variedad de muestra corta del ADF de la etapa de residuos** — la
misma familia de problema que RC1 documentó para el AIC. A estos
tamaños, un rechazo individual de EG es evidencia débil.

## Cómo regenerar

```sh
python reconstruction_real/code/cointegracion_hub_nodo.py   # ~4 s
```

---

*Fractal Core Research · Tlaxcala, México · 2026-10-26*
