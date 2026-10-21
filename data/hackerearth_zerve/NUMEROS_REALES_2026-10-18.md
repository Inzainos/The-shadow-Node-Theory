# Números reales — proyecto HackerEarth/Zerve (2026-10-18)

**Qué es esto:** la entrega corregida del proyecto de retención de usuarios
HackerEarth ("Fractal V3"). Sustituye las cifras principales del reporte PDF
del 18-oct-2026 (ROC-AUC 0.9994, ROC-AUC 1.0, precision 1.0), que la
verificación con los propios datos del proyecto demostró **circulares por
construcción** (ver `../../reconstruction_real/audits/REVISION_REPORTE_HACKEREARTH_2026-10-18.md`).

**Cómo se producen estos números:** modelo de churn con **etiqueta temporal**
— features de eventos antes del corte 2025-11-08, etiqueta = inactividad los
30 días siguientes; 5-fold CV. Score de los 4,774 usuarios con sus features al
fin de los datos (2025-12-08). Scripts:
`reconstruction_real/code/hackerearth_verificacion.py` (verificación) y
`hackerearth_entrega_honesta.py` (entrega). Datos: eventos PostHog
2025-09-01 → 2025-12-08, 409,287 eventos, 4,774 usuarios (SHAs en
`data/FUENTES.md`).

## Los números reales

| Cifra del reporte | Número real | Diferencia |
|---|---:|---|
| ROC-AUC 0.9994 (churn, "284 features") | **0.836 ± 0.038** (CV 5-fold, etiqueta temporal) | la brecha es la circularidad removida |
| ROC-AUC 1.0, precision 1.0, recall 1.0 (retención) | **No es un modelo**: la etiqueta era la cohorte (definida por CSI_V3) y CSI_V3 era feature → separación garantizada por definición | — |
| "Exceptional predictive accuracy" | **Señal honesta y modesta**: la dormancia a 30 días se predice sobre todo por **antigüedad (25%) + recencia (23%) + días activos (16%)** — no por "anchor events" | los "churn lifts" del reporte eran re-descripciones de la definición de cohorte |
| 2,108 "Intervene Now" (matriz 2×2) | Ver matriz honesta abajo | las dos dimensiones ahora son distintas de verdad |

**Calibración:** probabilidad media predicha 0.920 vs tasa real de la ventana
0.927 — el modelo no miente sobre la base: **el 92.7% de la base está
dormante**; ésa es la historia real del producto, no un logro del modelo.

## Matriz 2×2 honesta (4,774 usuarios)

Probabilidad de churn 30d > 0.5 × engagement ≥ 3 eventos totales:

| Cuadrante | Usuarios | % |
|---|---:|---:|
| Reactivar (riesgo alto, engagement bajo) | 2,334 | 48.9% |
| Intervenir ya (riesgo alto, engagement alto) | 2,259 | 47.3% |
| Cuidar (riesgo bajo, engagement alto) | 179 | 3.7% |
| Vigilar (riesgo bajo, engagement bajo) | 2 | 0.0% |

**Cómo usarla:** con una base 92.7% dormante, el umbral 0.5 separa poco — lo
accionable es el **ranking** dentro de cada cuadrante (`entrega_scores_honestos.csv`
lleva `prob_churn_30d` por usuario): los CSM priorizan los "Intervenir ya" con
mayor probabilidad (usuarios activos con señal de salida) y el cuadrante
"Cuidar" (179) es el activo sano a proteger.

## La segmentación descriptiva se mantiene

La segmentación CSI_V3 (Elite 24 / Intermediate 306 / Basic 4,444) es válida
**como descripción** del snapshot y reproduce exacto. Lo que no es válido es
usarla como etiqueta de un modelo que la lleva como feature. La lectura de
negocio del reporte (activar cómputo en los "Likely Retained", funnels de
agente) sigue siendo razonable **como estrategia sobre la segmentación
descriptiva** — no como predicción.

## Caveats (declarados, no opcionales)

1. **Censura a la derecha**: el dato termina 2025-12-08; un "churned" pudo
   volver después. Una sola ventana de 30 días, un solo corte.
2. **La base es 92.7%**: el AUC 0.836 es sobre una clase mayoritaria enorme; en
   la subpoblación establecida (antigüedad ≥ 7 días, n=137) el AUC es
   0.893 ± 0.041 y la recencia sola ya da 0.907 — la mayor parte de la señal
   es "días sin actividad", y eso es lo que hay.
3. **Horizonte**: las probabilidades son de inactividad en los 30 días desde
   2025-12-08. Si se usan más adelante, re-entrenar con datos frescos.

## Archivos

| Archivo | Contenido |
|---|---|
| `entrega_scores_honestos.csv` | 4,774 usuarios: features al corte, prob_churn_30d, cuadrante |
| `entrega_matriz_accion.csv` | conteos del 2×2 |
| `entrega_resumen.csv` | números clave en una tabla |
| `metricas_fractal_v3.csv` | métricas descriptivas por usuario (válidas como descripción) |
| `docu_*.csv` | salidas del proyecto original (conservadas como registro; sus AUC no citables) |

---

*Fractal Core Research · 2026-10-18 · Sustituye al PDF "Fractal V3 Insights"*
