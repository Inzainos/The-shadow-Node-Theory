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
Fuente: **Maddison Project Database 2020** (Bolt & van Zanden 2020; cobertura
1–2018), en `data/mpd2020.xlsx`. Sin datos sintéticos. Reproducción, desde la
raíz del repo:

```bash
python reconstruction_real/code/build_maddison_mpd2020_csv.py  # xlsx -> data/maddison_mpd2020.csv
python reconstruction_real/code/expand_B_massive.py            # -> data/dominio_B_real.csv
```

**Reproducción exacta (verificada 2026-09-27):** los 446 casos salen **byte a
byte** iguales a `by_domain/dominio_B_real.csv` (mismo SHA-256, las 19 columnas
idénticas). La edición del corpus no estaba fijada en el repo; se identificó
probando la edición 2020 contra lo publicado. Con la edición OWID posterior
(`data/owid-maddison.csv`) solo se obtiene una reproducción aproximada (441 vs
446 casos, corr(b) = 0.979), porque Maddison revisa el PIB histórico entre
ediciones y el hub se asigna por PIB medio. `expand_dominio_B.py` es una
expansión anterior (254 casos) y no reproduce los 446. El runner
`snt_auditoria_integral_v32.py` repite la verificación en cada ejecución.
