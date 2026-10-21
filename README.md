# Shadow Node Theory · v2.7.1

### Satelización de escala · colapso orbital acoplado · tela de incertidumbre

[![Release](https://img.shields.io/badge/release-v2.7.1-6f42c1)](CHANGELOG.md)
[![Marco teórico](https://img.shields.io/badge/marco-v34-0e8a8a)](papers/marco_teorico.md)
[![Series reales en la tela](https://img.shields.io/badge/tela-699%20series%20reales-2ea44f)](reconstruction_real/audits/TELA_EXOGENA_2026-10-21.md)
[![Python CI](https://github.com/Inzainos/The-shadow-Node-Theory/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/Inzainos/The-shadow-Node-Theory/actions/workflows/python-package-conda.yml)

**Shadow Node Theory (SNT)** estudia la evolución de relaciones entre nodos y
hubs mediante `R(t) = a·t^b`; **ACO-A** añade un eje ortogonal para el colapso,
`A(τ) = c·τ^Δ`. La **tela de incertidumbre** incorpora esas trayectorias como
proyecciones observables en `𝒞(u, m, τ)`: series reales donde están versionadas,
y sombras del modelo solo donde todavía faltan.

<p align="center">
  <img src="figures/fig_tela_cimatica_chladni.png" alt="Placa cimática continua de la tela de incertidumbre" width="48%">
  <img src="figures/fig_tela_cimatica_tonos.png" alt="Firmas de tono y espectro por dominio" width="48%">
</p>

> **Qué contiene esta versión:** el corpus SNT de **721 casos** permanece
> separado de la tela integrada, que reúne **740 trayectorias y 51.210 puntos**:
> 699 series reales reconstruidas desde fuentes versionadas y 41 sombras
> explícitamente identificadas. No son 740 nuevas réplicas independientes ni
> una afirmación de ley universal.

## La tela de incertidumbre, integrada

La capa conecta SNT + ACO-A con mediciones temporales trazables: magnitud
`m = R`, fase normalizada `τ` y marco de observación declarado
`θ = (B, V, ρ, W, λ)`. El eje `u` sigue **sin definición operativa** y se
conserva como `NULL`; la fricción `φ` es postulada por dominio, no una medición
continua.

| Capa | Qué integra | Resultado auditado |
|---|---|---|
| **Series exógenas** | E3 (234), B (446), ACO (18) y G (1); 50.813 puntos reconstruidos desde datos versionados | B reproduce 446/446; E3 reproduce 233/234 dentro de ±0,01 en `b`; ACO 18/18. |
| **Cubo v2** | Series reales donde existen y 41 sombras donde faltan | 740 trayectorias / 51.210 puntos; las sombras no se presentan como observaciones reales. |
| **Capa cimática** | Placa continua, figura por dominio, espectros, huellas y prueba leave-one-out | Identificación LOO: 50,7% por dominio y 66,2% por tono `φ`; resultado exploratorio, no clasificador calibrado. |
| **Dirección → destino** | Relación entre dirección en el primer 25% y régimen final | Spearman: E3 `+0,823`, B `+0,224`, ACO `+0,413` (`n=18`, `p=0,089`, no concluyente). Asociación descriptiva, no causalidad. |

La matriz agrupada sugiere que la dirección temprana contiene información
sobre el régimen final, pero su composición está dominada por E3 en el tercil
rápido y B en el lento; debe leerse conociendo ese sesgo. La capa cimática
identifica mejor tonos que etiquetas de dominio; **no** identifica de forma
fiable el dominio por la figura. ACO converge hacia `m≈1` en la muestra
disponible (`n=18`), sin inferencia concluyente.

### Casos de uso: qué pregunta responde la tela

La tela no es solo una imagen: es una forma común de **seguir una razón a lo
largo de una trayectoria**, distinguir observaciones de sombras y preguntar
qué rasgos aparecen al principio, al final o en distintos regímenes. Estos
ejemplos vienen de las series que ya están integradas:

| Caso | Pregunta práctica | Qué muestra la tela | Qué no permite concluir |
|---|---|---|---|
| **Países (B): PIB per cápita hub/nodo** | ¿Se reconstruyó fielmente la trayectoria relativa a través del tiempo? | Las 446 series reales reproducen `b` publicado (446/446) usando MPD2020. La curva permite inspeccionar la razón `R` y su evolución normalizada. | La reproducción no prueba por sí sola acoplamiento hub-nodo ni significancia: la autocorrelación es severa y la inferencia puntual de B sigue indecidible. |
| **Epidemias (E3): crecimiento de casos COVID-19** | ¿La forma temprana de la curva está asociada con su estado al cierre de la ventana? | 233/234 pendientes reproducen dentro de ±0,01; en esta selección de trayectorias de crecimiento, la asociación entre pendiente temprana y destino es `ρ=+0,823`. | No es una alerta anticipada validada ni una regla general para epidemias: la cohorte se seleccionó por fase de crecimiento y eso condiciona el resultado. |
| **Colapsos ACO-A** | ¿La trayectoria real se acerca o se aleja de la banda `m≈1`? | En los 18 casos, la mediana de `|log₁₀ m|` baja de 0,292 a 0,071: descriptivamente, las trayectorias terminan más cerca de `m=1`. | Con `n=18`, no demuestra un atractor universal ni permite predecir cuándo ocurrirá un colapso (`ρ=+0,413`, `p=0,089`). |
| **Bennu (G): proxy geoquímico** | ¿Puede visualizarse una trayectoria real de un dominio distinto? | La fuente versionada aporta un caso y tres puntos, mostrado como serie real; sirve para inspección y para definir qué datos faltarían para una prueba. | Un caso no permite estimar distribución, clasificación ni generalizar a cuerpos celestes. |

**Cómo leer la placa:** el eje horizontal `τ` lleva cada ventana desde el inicio
(0) hasta el final (1); el vertical `log₁₀ m` muestra la razón `m=R` en escala
logarítmica. La densidad indica dónde pasan más trayectorias; la figura resume
la mediana por dominio y su banda IQR. Una curva que termina más cerca de cero
termina más cerca de `m=1`. Las trayectorias de datos reales y las sombras se
identifican por separado en los datos; una forma visual parecida no las vuelve
la misma clase de evidencia.

**¿Cómo se aplicaría a otro caso?** El apartado
[Casos de uso de SNT](CASOS_DE_USO.md) documenta pruebas externas como la
cohorte de 450 paquetes npm: allí se evaluó ACO-A y se encontró
`ρ(b, Δ)=+0,114` (IC95 `[+0,016, +0,209]`). Es un ejemplo de cómo una aplicación
puede respaldar una parte de la teoría y contradecir otra; **npm todavía no
forma parte de la tela integrada**. Para añadirlo haría falta construir y
auditar su serie `R(t)`, declarar el marco `θ` y repetir el análisis sin
confundirlo con validación ya hecha.

**Explora la capa:** [auditoría de la tela integrada](reconstruction_real/audits/TELA_V2_INTEGRADA_2026-10-21.md) ·
[serie real y capa exógena](reconstruction_real/audits/TELA_EXOGENA_2026-10-21.md) ·
[resultados cimáticos](reconstruction_real/audits/TELA_CIMATICA_2026-10-21.md) ·
[implementación del cubo](reconstruction_real/audits/TELA_DE_INCERTIDUMBRE_2026-10-21.md).

**Figuras:** [placa continua (PNG)](figures/fig_tela_cimatica_chladni.png) ·
[placa vectorial (SVG)](figures/fig_tela_cimatica_chladni.svg) ·
[tonos (PNG)](figures/fig_tela_cimatica_tonos.png) ·
[tonos vectoriales (SVG)](figures/fig_tela_cimatica_tonos.svg).

> **Versionado independiente:** v2.7.1 es la versión del paquete del
> repositorio; el marco teórico activo sigue en v34 y el corpus SNT en 721
> casos. La tela añade una capa de trayectorias y análisis, no cambia el tamaño
> del corpus consolidado.

El estado que sigue prioriza resultados empíricos auditados. El corpus de
721 casos **no equivale a 721 réplicas independientes**, y la reproducibilidad
varía entre dominios.

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
- Datos de la tela: [`reconstruction_real/data/tela_de_incertidumbre.csv`](reconstruction_real/data/tela_de_incertidumbre.csv) (740 trayectorias, 51.210 puntos); series exógenas: [`tela_exogena_series.csv`](reconstruction_real/data/tela_exogena_series.csv) (699 series reales).
- Código reproducible: [`tela_exogena.py`](reconstruction_real/code/tela_exogena.py) → [`tela_de_incertidumbre.py`](reconstruction_real/code/tela_de_incertidumbre.py) → [`tela_cimatica.py`](reconstruction_real/code/tela_cimatica.py).
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
- `figures/` — figuras de resultados vigentes, incluidas la placa cimática y
  las firmas de tono de la tela.
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
