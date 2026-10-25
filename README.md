# Shadow Node Theory (SNT) · v2.7.1

[![Release](https://img.shields.io/badge/release-v2.7.1-6f42c1)](CHANGELOG.md)
[![Marco teórico](https://img.shields.io/badge/marco-v34-0e8a8a)](papers/marco_teorico.md)
[![Python CI](https://github.com/Inzainos/The-shadow-Node-Theory/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/Inzainos/The-shadow-Node-Theory/actions/workflows/python-package-conda.yml)

**Shadow Node Theory** estudia trayectorias relativas entre un hub y un nodo.
Su objeto empírico es la razón `R(t) = métrica_del_hub / métrica_del_nodo`,
resumida —cuando los datos lo permiten— por `R(t) = a·t^b`. El marco también
incluye ACO-A, una descripción separada de la absorción posterior a ciertos
colapsos, y una capa de incertidumbre que distingue observaciones, proyecciones
y reconstrucciones.

SNT es un marco de análisis, no una ley universal ni un predictor validado.
Los resultados dependen del dominio, la ventana, las variables y la calidad de
reconstrucción. La autocorrelación y la selección de casos limitan la
inferencia; 721 registros no equivalen a 721 réplicas independientes.

## La idea y sus límites

`R(t)` compara la escala del hub con la del nodo. El exponente `b` describe la
trayectoria dentro de la ventana observada:

| `b` | Lectura descriptiva |
|---|---|
| `b < 0` | La razón disminuye: el nodo gana terreno relativo. |
| `b ≈ 0` | La razón permanece aproximadamente estable. |
| `0 < b < 1` | La razón crece de forma sublineal en el ajuste de potencia. |
| `b ≥ 1` | Banda descriptiva no clasificada; no prueba un régimen superlineal. |

Un ajuste de potencia no demuestra causalidad ni identifica por sí solo el
mecanismo del sistema. En la calibración RC1, el error de selección AIC excedió
el umbral preespecificado del 20% en todos los dominios calibrados. Por ello,
`b ≥ 1` no se interpreta como prueba de aceleración o como régimen físico
confirmado. Véanse [RC1 — superlineal](reconstruction_real/audits/RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md)
y [RC1 — dominios restantes](reconstruction_real/audits/RESULTADOS_RC1_DOMINIOS_RESTANTES_2026-10-17.md).

## Evolución del marco

1. **SNT: razón y trayectoria.** La pregunta inicial es cómo cambia `R(t)`
   entre un hub y un nodo. `b` resume esa forma local; no se presupone que una
   misma interpretación sea válida en todos los dominios.
2. **ACO-A: otra pregunta y otro reloj.** Para colapsos con extinción funcional
   y sucesor identificable, `A(τ) = c·τ^Δ` describe la absorción de actividad o
   masa tras el evento. `Δ` no es `b`: usa otra magnitud y otro origen temporal.
   La relación entre ambos se contrasta empíricamente; no se trata como una ley
   universal.
3. **Marco teórico v34: incertidumbre y proyección.** El cubo estructural
   `𝒞(u, m, τ)` distingue el estado propuesto de su observación. En la
   implementación, `m` corresponde a `R` con el proxy declarado y `τ` es la
   fase temporal normalizada. `u` no tiene definición operativa admitida y
   permanece `NULL`; por ahora el análisis opera en `(m, τ)`. Cada observación
   debe declarar su marco `θ = (B, V, ρ, W, λ)`. Una proyección es parcial: no
   permite reconstruir un único estado sin justificarlo.
4. **Tela integrada: datos reales donde existen; sombras donde faltan.** La
   versión integrada reemplaza la antigua lectura de origen común en `m=1`,
   que provenía de sombras modeladas. Las series reales nacen en escalas
   distintas; las sombras siguen identificadas como tales y no se cuentan como
   observaciones nuevas.

Las numeraciones son independientes: **v2.7.1** es la versión del repositorio,
**v6** identifica el corpus consolidado y **v34** el marco teórico.

## Hallazgos que sobreviven a la auditoría

El corpus consolidado contiene **721 casos**. La tela integrada contiene
**740 trayectorias**: **699 series reales versionadas** (B 446, E3 234, ACO 18,
G 1) y **41 sombras** para casos sin serie temporal cruda versionada. Son dos
conjuntos con propósitos distintos; las sombras no amplían el corpus de casos
reales.

| Dominio / capa | Resultado reproducible o medido | Qué permite concluir |
|---|---|---|
| **B — países (446)** | La reconstrucción de las pendientes reproduce MPD2020. Hay autocorrelación severa en 445/446 series; 290/446 no son estimables bajo el criterio de tamaño efectivo. Ninguno de los 12 métodos recalibrados quedó dentro de la banda de falsos positivos predefinida. | La reconstrucción es reproducible; la inferencia puntual sobre B queda **indecidible**. El contraste con un hub de comercio tampoco detectó asociación ni diferencia hub–control. |
| **E3 — expansión epidemiológica (234)** | 233/234 pendientes se reproducen desde la serie OWID versionada dentro de ±0,01. | Confirma la reconstrucción de esta selección de trayectorias; no valida una alerta predictiva ni una regla general para epidemias. |
| **ACO-A (18)** | Hay 18 trayectorias crudas versionadas. La mediana de `|log₁₀ m|` baja de 0,292 a 0,071 entre inicio y final. | Es una convergencia descriptiva hacia `m≈1` en esta muestra. El tamaño y las pruebas disponibles no demuestran un atractor universal ni permiten predecir el momento del colapso. |
| **G — Bennu (1)** | Un caso con tres puntos versionados. | Sirve como ejemplo exploratorio; no permite generalizar a cuerpos celestes. |
| **Tela cimática** | En la clasificación exploratoria leave-one-out de la tela integrada: 50,7% por dominio y 66,2% por tono `φ`. | Son mediciones de una clasificación por centroide, no un clasificador calibrado ni evidencia de que la forma identifique con fiabilidad el dominio o la fricción. |

La tela corregida conserva una distribución inicial abierta: el origen único
en `m=1` de la primera versión era un artefacto de las sombras. En la versión
integrada, el abanico entre trayectorias se amplía durante la fase observada;
la convergencia terminal de ACO se mantiene como resultado descriptivo de sus
18 series reales. Las formas agregadas y sus métricas cimáticas deben leerse
con la composición de dominios y las 41 sombras explícitas en mente.

### Lo que no se presenta como hallazgo establecido

- Los valores p por caso no son pruebas independientes: existe dependencia
  temporal y agrupación por dominio.
- `b ≥ 1` no identifica por sí solo superlinealidad ni aceleración.
- La fricción `φ` está postulada por dominio, no medida como campo continuo.
- El eje `u` no tiene definición operativa y no se rellena con un proxy.
- Las sombras generadas a partir de ajustes no son series observadas ni nuevas
  réplicas; una forma en la tela tampoco demuestra un mecanismo causal.
- La asociación descriptiva entre variables, la clasificación exploratoria y
  la convergencia de ACO no establecen capacidad predictiva ni universalidad.

## Fuentes, datos y auditorías

- [Estado empírico y reproducibilidad por dominio](reconstruction_real/README.md)
- [Corpus consolidado v6](reconstruction_real/data/snt_corpus_REAL_v6.csv)
- [Tela integrada v2](reconstruction_real/audits/TELA_V2_INTEGRADA_2026-10-21.md)
- [Implementación de la capa de incertidumbre](reconstruction_real/audits/TELA_DE_INCERTIDUMBRE_2026-10-21.md)
- [Resultados de la capa cimática](reconstruction_real/audits/TELA_CIMATICA_2026-10-21.md)
- [Marco teórico v34](papers/marco_teorico.md)
- [Fuentes, ediciones y checksums](data/FUENTES.md)
- [Auditorías y preregistros](reconstruction_real/audits/README.md) ·
  [casos de uso externos](CASOS_DE_USO.md)

Las fuentes propietarias o no redistribuibles se identifican en sus informes.
Los valores ausentes permanecen ausentes; no se imputan como cero.

## Reproducir

Usa el entorno local descrito en [AGENTS.md](AGENTS.md). Desde la raíz:

```bash
flake8 .
python -m compileall -q code reconstruction_real dashboard delta
python reconstruction_real/code/build_aco_v29.py
pytest reconstruction_real/tests
```

La prueba del corpus B y las auditorías completas pueden requerir más tiempo.
Consulta las instrucciones de cada informe antes de descargar datos o
regenerar resultados.

## Estructura

- `reconstruction_real/` — corpus, metodología, código, auditorías y pruebas.
- `papers/` — marco teórico v34 y documentos de investigación.
- `code/` — utilidades y scripts activos compartidos.
- `data/` — datos versionados y procedencia.
- `figures/` — figuras de resultados vigentes.
- `delta/` — motor independiente de señales de cripto y bolsa.
- `dashboard/` — dashboard Streamlit.
- `Legacy/` y `archive/` — material histórico supersedido; no citar como
  evidencia vigente.
- El **Genomic Topologic Analyzer** tiene repositorio propio desde 2026-10-20:
  `/home/deamon/genomic_agent`.

## Marco y cita

El marco activo es **v34**; la información de cita está en
[`CITATION.cff`](CITATION.cff). Contribuye mediante una rama y un pull request;
no hagas commits directamente a `main`. Cada resultado nuevo debe incluir
fuente, receta reproducible y límites de inferencia; registra los cambios en
[`CHANGELOG.md`](CHANGELOG.md).
