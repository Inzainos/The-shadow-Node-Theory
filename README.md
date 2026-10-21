# Shadow Node Theory

Shadow Node Theory (SNT) estudia relaciones de satelización de escala
`R(t) = a·t^b` y la capa de colapso orbital acoplado (ACO-A),
`A(τ) = c·τ^Δ`. Este repositorio contiene teoría, datos versionados, scripts y
auditorías. El estado que sigue prioriza resultados empíricos auditados; el
corpus consolidado reúne 721 casos, pero **no** equivale a 721 réplicas
independientes ni todos sus dominios son reproducibles.

## Hallazgos empíricos

| Área | Resultado observado | Alcance y límite | Informe |
|---|---|---|---|
| **Dominio B — satelización histórica** | Las 446 pendientes se reproducen byte a byte con MPD2020. El 99.8% de las series presenta autocorrelación severa; 290/446 no son estimables bajo el criterio de tamaño efectivo. | En una recalibración de 200,000 simulaciones, ninguno de los 12 métodos queda dentro de la banda de falsos positivos predefinida `[2.5%, 7.5%]`. El valor puntual es **indecidible**; no se debe citar la proporción nominal como conclusión inferencial. | [Recalibración de B](reconstruction_real/audits/RESULTADOS_RECALIBRACION_DOMINIO_B_2026-10-03.md) · [Auditoría v32](reconstruction_real/audits/AUDITORIA_INTEGRAL_v32.md) |
| **Dominio B — hub comercial** | Con un hub definido por comercio bilateral, `ρ(b, brecha) = −0.153` (`p=0.125`); la comparación hub–control no detecta diferencia (`p=0.78`). | La reconstrucción con hub emergente no rescata evidencia de acoplamiento SNT por encima del nulo calibrado. | [Reconstrucción de B con comercio](reconstruction_real/audits/RECONSTRUCCION_DOMINIO_B_HUB_COMERCIO.md) |
| **RC1 — exponentes `b ≥ 1`** | El error de selección AIC es 80.3% en E3, 96.8% en B, 48.9% en ACO, 22.6% en C y 94.0% en el único caso E2_01 calibrable. | Ningún dominio calibrado supera la compuerta pre-registrada del 20%; por tanto, la etiqueta de régimen superlineal no se interpreta con AIC. Una exponencial verdadera produce `b ≥ 1` con frecuencia en E3/B/ACO, pero solo 0.7% en C: el artefacto no es universal y la calibración debe ser específica por dominio. | [RC1 en dominios restantes](reconstruction_real/audits/RESULTADOS_RC1_DOMINIOS_RESTANTES_2026-10-17.md) · [RC1 superlineal](reconstruction_real/audits/RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md) |
| **Reproducibilidad por dominio** | C reproduce 23/23 casos con una receta preespecificada; A reproduce 1/4 (coincidencia espuria por usar una ventana incompatible); E2 reproduce 1/2. | D depende de datos propietarios; E1 no se reproduce; F1–F3 no contienen trayectorias temporales `R(t)` equivalentes. Un caso o dominio no reproducible no se presenta como replicado. | [Matriz de resultados RC1](reconstruction_real/audits/RESULTADOS_RC1_DOMINIOS_RESTANTES_2026-10-17.md) |
| **HackerEarth — evaluación temporal** | Con etiqueta temporal de 30 días y validación cruzada de cinco pliegues, el AUC es **0.836 ± 0.038** (`n=2,058`); en usuarios con antigüedad ≥7 días, **0.893 ± 0.041** (`n=137`). | Una ventana y un corte; hay censura a la derecha y la cohorte tiene alta dormancia. Las métricas antiguas basadas en etiquetas definidas por engagement eran circulares y no son evidencia predictiva. El dataset crudo propietario no se redistribuye. | [Auditoría HackerEarth](reconstruction_real/audits/REVISION_REPORTE_HACKEREARTH_2026-10-18.md) · [Números reales](data/hackerearth_zerve/NUMEROS_REALES_2026-10-18.md) |
| **N-cuerpos — rango-tamaño** | Para las 32 entidades mexicanas, la lognormal mejora el AIC frente a la potencia en 65.04 puntos. La réplica internacional favorece la lognormal en 5/6 niveles y la potencia en los municipios brasileños. | La prueba de Clauset no alcanza la tasa de error requerida en ningún nivel: incluso en Brasil (`n=5,570`) deja pasar una ley de potencia en 42.6% de muestras lognormales. No es evidencia general de apego preferencial. | [Comparación lognormal](reconstruction_real/audits/RESULTADOS_LOGNORMAL_2026-10-02.md) · [Réplica internacional](reconstruction_real/audits/RESULTADOS_RANGO_TAMANO_2026-10-02.md) |
| **ACO-A — disparadores** | En 18 casos, la media descriptiva de `b` es +0.400 para abruptos y +0.854 para graduales (`p=0.101`); en la permutación intra-dominio, `p=0.938`. | La comparación no es concluyente y el disparador está confundido con el dominio. Un seguimiento de fricción→Δ encontró `ρ=−0.377`, `p=0.121` en ACO (`n=18`, post-hoc). | [Desbloqueos con datos](reconstruction_real/audits/RESULTADOS_DESBLOQUEOS_2026-10-18.md) |
| **ACO-A — paquetes npm** | En 450 paquetes, la asociación de subida y caída es pequeña (`ρ=+0.114`, IC95 `[+0.016,+0.209]`); el hazard observado decrece con la edad (`ρ=−0.716`, `p=0.013`, dos colas). | La ortogonalidad es respaldada por el criterio de equivalencia preespecificado; el hazard decreciente requiere cautela por censura reciente y mezcla edad-periodo-cohorte. | [Resultados npm](reconstruction_real/audits/RESULTADOS_NPM_2026-10-02.md) |
| **Fricción→Δ — npm** | En la cohorte de 450 paquetes, `ρ=+0.163`, `p=0.0005`. | Seguimiento post-hoc con grupos de tamaño desigual; es una asociación local que requiere réplica pre-registrada en otro ecosistema, no una regla general. | [Desbloqueos con datos](reconstruction_real/audits/RESULTADOS_DESBLOQUEOS_2026-10-18.md) |
| **Eje `u`** | La propuesta `u^H` no supera la compuerta de invariancia ni en el Dominio B ni en cripto. | `u` no tiene definición operativa admitida; no se incorpora como eje medido. | [Prueba de transiciones](reconstruction_real/audits/RESULTADOS_EJE_U_TRANSICIONES_2026-10-17.md) |

**Lectura conjunta:** los resultados apoyan descripciones locales y
reproducibles allí donde las recetas y fuentes están disponibles; no establecen
una ley universal de SNT. La autocorrelación, la selección de casos, la
reproducibilidad desigual y las pruebas con potencia insuficiente limitan las
inferencias. Las cifras por caso y sus valores p no deben agregarse como si los
721 casos fueran observaciones independientes.

## Corpus y procedencia

- Corpus consolidado: [`reconstruction_real/data/snt_corpus_REAL_v6.csv`](reconstruction_real/data/snt_corpus_REAL_v6.csv).
- Descripción, métodos y estado de reproducibilidad:
  [`reconstruction_real/README.md`](reconstruction_real/README.md).
- Fuentes, ediciones y checksums: [`data/FUENTES.md`](data/FUENTES.md).
- Auditorías y pre-registros: [`reconstruction_real/audits/`](reconstruction_real/audits/)
  y [`reconstruction_real/preregistro/`](reconstruction_real/preregistro/).
- Los datos fuente propietarios o que no pueden redistribuirse se identifican
  en su informe; los valores ausentes permanecen ausentes, no se imputan como
  cero.

## Reproducir

Usa el entorno local documentado en [AGENTS.md](AGENTS.md). Desde la raíz:

```bash
flake8 .
python -m compileall -q code reconstruction_real dashboard delta
python reconstruction_real/code/build_aco_v29.py
pytest reconstruction_real/tests
```

La prueba del corpus B y las auditorías completas pueden requerir más tiempo.
Consulta las instrucciones de cada informe antes de volver a descargar datos o
regenerar salidas.

## Estructura

- `reconstruction_real/` — corpus, metodología, scripts, auditorías y pruebas.
- `papers/` — marco teórico y preprints; marco v34.
- `code/` — utilidades y scripts activos compartidos.
- `data/` — datos fuente/versionados y procedencia.
- `Legacy/` — archivos heredados listados abajo.
- `figures/` — figuras de resultados vigentes.
- `delta/` — motor independiente de señales de cripto y bolsa.
- `dashboard/` — dashboard Streamlit.
- `archive/` — documentos históricos.

### Legacy — nombres de archivos

- `Legacy/data/dataset_completo_v2.csv`
- `Legacy/data/shadow_node_maddison_resumen.csv`
- `Legacy/data/snt_corpus_50_resultados_v2.csv`
- `Legacy/code/generate_publication_figures.py`
- `Legacy/code/snt_corpus_astronomical.py`
- `Legacy/code/snt_corpus_biological.py`
- `Legacy/figures/fig1_corpus_distribution.png`
- `Legacy/figures/fig1_corpus_distribution.svg`
- `Legacy/hackerearth_zerve/canvas.yaml`
- `Legacy/hackerearth_zerve/Development/FRACTAL CORE — Master Narrative.md`

## Marco y cita

El marco teórico activo es **v34** (`papers/marco_teorico.md`); la numeración
del marco y la del corpus son independientes. Las afirmaciones conceptuales y
los criterios de falsabilidad se encuentran en
[`papers/`](papers/) y [`reconstruction_real/`](reconstruction_real/).
La información para citar el trabajo está en [`CITATION.cff`](CITATION.cff).

## Mantenimiento

Contribuye mediante una rama y un pull request; no hagas commits directamente a
`main`. Cada resultado debe incluir su script, fuente, versión y límites de
inferencia. Registra los cambios relevantes en [`CHANGELOG.md`](CHANGELOG.md).
