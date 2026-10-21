# Capa Exógena de la Tela — Series Reales y Estadística Dirección→Destino

**Fecha:** 2026-10-21
**Script:** `code/tela_exogena.py`
**Salidas:** `data/tela_exogena_series.csv` (50,813 puntos, 699 casos),
`data/tela_exogena_casos.csv`, `data/tela_exogena_estadisticas.csv`,
`data/tela_exogena_probabilidad.csv`
**Motivación:** la prueba dirección→destino tenía solo 18 casos exógenos
(ACO); las sombras dan Spearman +1.000 por determinismo del modelo. Con
esta capa la tela pasa de 18 a **699 series reales**.

## Reconstrucción y verificación

| Dominio | Fuente versionada | Receta | Casos | Puntos | b verificado |
|---------|-------------------|--------|-------|--------|--------------|
| E3 | `data/owid_covid_casos_totales.csv.gz` | casos acumulados desde primer día con ≥100, 60 días (receta re-identificada: 233/234 dentro de ±0.01) | 234 | 14,040 | 99.6% (solo E3_060, NA conocido del corpus v6) |
| B | `data/maddison_mpd2020.csv` | R = PIB_pc_hub/PIB_pc_nodo, t = posición 1..n (`expand_dominio_B.py`) | 446 | 36,661 | **446/446, 100%** |
| ACO | `snt_corpus_aco_timeseries_v29.csv` | serie tal cual (v29) | 18 | 109 | 18/18, 100% |
| G | `snt_corpus_dominio_G_timeseries.csv` | serie tal cual | 1 | 3 | sin b publicado — declarado |
| **Total** | | | **699** | **50,813** | |

**Lección Regla Cero del proceso:** la primera corrida usó
`data/owid-maddison.csv` (extracto OWID, 21,586 filas) y 45 casos de B
fallaban la verificación con desviaciones de hasta 0.31 en b. El panel
correcto es `data/maddison_mpd2020.csv` (19,706 filas) — el mismo de la
recalibración auditada 2026-10-03. Con el panel correcto: 446/446. Un
5% de "no reproduce" era síntoma de fuente equivocada, no de corpus
roto.

## Estadística por dominio (datos reales, no sombras)

| Dominio | n | b media | b mediana | b moda* | Spearman(dirección temprana → destino) |
|---------|---|---------|-----------|---------|----------------------------------------|
| ACO | 18 | 0.602 | 0.342 | 0.173 | +0.413 (p=0.089 — no significativo, n chico) |
| B | 446 | 0.092 | 0.058 | 0.008 | **+0.224 (p=1.7×10⁻⁶)** |
| E3 | 234 | 0.910 | 0.846 | 0.833 | **+0.823 (p=7.3×10⁻⁵⁹)** |

\* moda por histograma de 20 bins.

**Lectura honesta:** la dirección temprana predice el destino con fuerza
donde la trayectoria es suave (E3: +0.82), débilmente donde la razón
fluctúa (B: +0.22, significativo pero ruido dominante), y sigue sin
decidir en ACO (n=18). El principio de mínima fricción se sostiene
direccionalmente en los tres, con potencia real en dos.

## Probabilidad P(régimen | dirección temprana)

Dirección = tercil de la pendiente de log₁₀R en τ ∈ [0, 0.25]
(calibrado con datos: Q⅓ = 0.074, Q⅔ = 0.927 décadas/fase; regla 9: sin
umbrales inventados). Régimen = bandas declaradas de la SNT. n = 698.

| Dirección temprana | b<0 convergencia | 0≤b<0.5 incipiente | 0.5≤b<1 gradual | b≥1 superlineal/ACO |
|--------------------|------------------:|-------------------:|----------------:|--------------------:|
| Tercil bajo | **0.425** | 0.536 | 0.039 | **0.000** |
| Tercil medio | 0.267 | 0.629 | 0.078 | 0.026 |
| Tercil alto | **0.039** | 0.223 | 0.335 | **0.403** |

**El operador lo dice así:** viendo la dirección, ya sabes el final.

- Un caso que arranca lento: **96%** termina en b<0.5 (convergencia o
  satelización incipiente) y **0%** llega a superlineal.
- Un caso que arranca rápido: **74%** termina en b≥0.5 y **40%** en
  superlineal/ACO.
- Convergencia (b<0) es **11× más probable** con dirección lenta (42.5%
  vs 3.9%); superlineal es **infinitamente más probable** con rápida
  (40.3% vs 0%).

**Advertencia de composición:** la matriz agrupa dominios — el tercil
alto lo dominan los E3 (fase de crecimiento, selección con sesgo
positivo por diseño del dominio) y el bajo los B. Si se conoce el
dominio, use la fila por dominio; la matriz es la respuesta operacional
agrupada para un caso de dominio desconocido.

## Limitaciones

- E3 es un corpus seleccionado por "fase de crecimiento 2020": sesgo
  estructural hacia dirección positiva (declarado, no corregible sin
  redefinir el dominio).
- ACO sigue con n=18: la estadística descriptiva se reporta, la
  inferencia no concluye.
- G: 1 caso, descriptivo.
- La pendiente temprana usa el primer 25% de la ventana de cada caso:
  ventana y fase son por construcción del dominio, no tiempo absoluto.

## Reproducir

```bash
python reconstruction_real/code/tela_exogena.py   # ~8 s, sin descargas
```

Log: `logs/tela_exogena_log.txt`.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-21*
