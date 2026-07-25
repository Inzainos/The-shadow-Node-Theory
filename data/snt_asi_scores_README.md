# snt_asi_scores.csv — diccionario de datos y advertencia de circularidad

Companion de `data/snt_asi_scores.csv`. Un CSV no puede llevar metadatos
inline, así que la advertencia vive aquí. **Léelo antes de usar la columna
`soberania` como target de cualquier modelo.**

## Columnas

| Columna | Definición |
|---|---|
| `delta_H` | δH — término de entropía/heterogeneidad |
| `alpha` | α — exponente de absorción |
| `F` | F — fricción |
| `ASI_raw` | **δH · α / F** (verificado, error máx ~2e-14) |
| `ASI` | ASI normalizado |
| `soberania` | booleano — ver advertencia abajo |
| `CSI_V3` | índice CSI v3 |
| `cohort` | cohorte asignada |

## ⚠️ `soberania` NO es una variable independiente — es un umbral de ASI

La auditoría integral v32 verificó que `soberania` es una **función escalón de
ASI**, no una etiqueta observada de forma independiente:

```
ASI de soberano (True)  mínimo = 1.0874
ASI de no-soberano      máximo = 0.9126
                        -> separación PERFECTA (soberania == ASI > ~1)
```

**Consecuencia:** cualquier estadístico del tipo *"ASI predice soberanía"* sería
**circular por construcción** — se estaría prediciendo un umbral de X con la
propia X. No uses `soberania` como variable dependiente contra `ASI`, `ASI_raw`,
`delta_H`, `alpha` o `F`.

Además, la base positiva es diminuta: **13 soberanos de 4,774 = 0.27%**.
Cualquier clasificador entrenado sobre 13 positivos es frágil, independientemente
de la circularidad.

## Uso correcto

- `soberania` sirve como **etiqueta de corte** descriptiva (¿ASI cruza el umbral?),
  no como fenómeno a predecir.
- Si se necesita un target de "soberanía" real, debe provenir de una medición
  **externa a ASI** (p.ej. retención observada), y esa columna hoy **no está** en
  este archivo (ver el hallazgo ROC-AUC 0.715 de la auditoría v32).
