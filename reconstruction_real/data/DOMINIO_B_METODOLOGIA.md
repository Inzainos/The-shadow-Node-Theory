# Dominio B (Países) — Reconstrucción con Datos Reales

## Fuente de datos
**Maddison Project Database** (Bolt & van Zanden 2023), vía Our World in Data.
PIB per cápita real (constant 2011 international $), series 1-2018.

## Metodología
Para cada par hub-nodo:
1. R(t) = PIB_pc_hub(t) / PIB_pc_nodo(t)
2. Linealización log-log: log R(t) = log a + b·log t
3. Estimación OLS de b (exponente de satelización)
4. R² real (coeficiente de determinación, siempre ∈ [0,1])
5. Durbin-Watson para autocorrelación
6. 95% CI vía error estándar de la pendiente

## Criterio de selección de pares
- Pares dentro de la misma región económica
- Hub = país con mayor PIB per cápita promedio histórico (criterio objetivo)
- Mínimo 8 observaciones temporales por par
- Período base: 1900-2018 (ajustado por disponibilidad)

## Resultados (446 casos)
- Significativos (p<0.05): 220 (85.3%)
- b medio: +0.076, mediano: +0.033
- R² medio (significativos): 0.41
- **Cero valores de R² corruptos** (vs ~46 en versión sintética anterior)

## Hallazgo central (verificable)
La satelización (b) varía sistemáticamente por región según fricción institucional:
- Convergencia (b<0): Europa, Sudamérica (integración regional, instituciones fuertes)
- Satelización (b>0): África Subsahariana, Asia Sudeste (mayor divergencia)

## Trazabilidad
Los valores de b y R² se regeneran ejecutando `expand_B_massive.py` (desde la
raíz del repo) sobre `data/owid-maddison.csv`. Sin datos sintéticos.

**Alcance de la reproducción (medido 2026-09-27):** la regeneración es
**aproximada, no exacta**. Con la edición de Maddison/OWID versionada
(descargada 2026-07-25) se obtienen 441 casos vs 446 publicados: 408 pares
comunes, corr(b) = 0.979, signo de b coincide en 396/408 y solo 12/408 valores
de b idénticos. La edición usada al construir el dominio no se fijó y Maddison
revisa el PIB histórico entre ediciones; como el hub se asigna por PIB medio,
la revisión puede invertir el orden de un par. `expand_dominio_B.py` es una
expansión anterior (254 casos) y no reproduce los 446. El runner
`snt_auditoria_integral_v32.py` repite esta medición en cada ejecución.
