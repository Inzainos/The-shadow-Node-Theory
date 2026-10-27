# Shadow Node Theory (SNT) · v2.7.4

[![Release](https://img.shields.io/badge/release-v2.7.4-6f42c1)](CHANGELOG.md)
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

**Estado de la evidencia.** Cada cifra citada en este README se verifica contra
los CSV versionados con [`reconstruction_real/claims.yaml`](reconstruction_real/claims.yaml)
(`python reconstruction_real/code/verificar_claims.py`; también corre en CI).

| Afirmación | Estado |
|---|---|
| Las pendientes de B y E3 se reconstruyen desde fuentes versionadas | Reproducible (E3: 233/234) |
| Inferencia sobre `b` en B | Indecidible: 290/446 series no estimables |
| `b` de B como estimación de equilibrio de largo plazo | No confirmado: 93,3% componentes I(1), 12,3% cointegrado detectado — apenas 2–4 pp sobre el tamaño del test (EG sobre-rechaza 8–10% bajo la nula en series cortas, M=3000 versionado). Corregida por tamaño por-n y potencia, la tasa verdadera es ~4–15% (≈9% a la mediana de B con 45,9% de potencia y 9,0% de tamaño a n=69; ponderada por n: 4,2–7,4%). `b` queda como descriptor de deriva ([cointegración](reconstruction_real/audits/COINTEGRACION_HUB_NODO_2026-10-26.md)) |
| `b ≥ 1` como régimen superlineal | No respaldada (error de selección AIC de 22,6% a 96,8%) |
| Relación general fricción `φ` → `b` | No respaldada en tres vías: agrupamiento de dominios (p_perm = 0,053; MixedLM p = 0,57), dominios nuevos pre-registrados (p = 0,39), y por caso dentro de npm (ρ = +0,09, dirección contraria) |
| La forma de la trayectoria identifica el dominio | Sí, en exactitud balanceada; no frente a la línea base cruda |
| La forma de la trayectoria identifica el tono `φ` | No distinguible de asignar tonos al azar entre dominios |
| ACO-A: convergencia descriptiva de `\|log₁₀ m\|` hacia 0 | Más cerrada que la dinámica AR(1) propia (p = 0,013) pero ligada a ventanas acabadas en evento (las de B no convergen) — no interpretada como firma del colapso ([nulos AR(1)](reconstruction_real/audits/NULOS_AR1_ACO_2026-10-26.md)) |
| Prueba prospectiva ACO-A | Cohorte v2 y ventana 2026-09-30 → 2027-09-30. La ADENDA 5 fija la censura de pares sin seguimiento completo y el manifiesto/hash previo al análisis; es posterior al DOI 23678033 y se sellará en un release nuevo antes de evaluar. El backcast histórico fue actualizado bajo esta regla: P1a/P2 respaldadas, P3 inconcluso ([ADENDA 5](reconstruction_real/preregistro/ADENDA5_PROSPECTIVA_DELISTADOS_Y_HASH_2026-10-27.md); [backcast](reconstruction_real/audits/BACKCAST_PROSPECTIVA_2026-10-26.md)) |

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

## Evolución

La historia completa — de la hipótesis de escala a la teoría que declara
sus límites, con cada auditoría que retiró una interpretación — vive en
[`docs/HISTORIA.md`](docs/HISTORIA.md).

## Desarrollo empírico por dominio

El corpus consolidado contiene **721 casos**. La tela integrada contiene
**740 trayectorias**: **699 series reales versionadas** (B 446, E3 234, ACO 18,
G 1) y **41 sombras** para casos sin serie temporal cruda versionada. Son dos
conjuntos con propósitos distintos; las sombras no amplían el corpus de casos
reales.

El detalle de cada dominio — qué sobrevivió, qué se retiró y las
auditorías correspondientes — vive en
[`docs/DOMINIOS.md`](docs/DOMINIOS.md).

| Dominio | Casos | Estado en una frase |
|---|---:|---|
| A — ciudades | 4 | No reproducible (1/4, espuria); el 8/8 pre-registrado es el mínimo alcanzable (1/2⁸) |
| B — países | 446 | Reproducible byte a byte (Maddison); sin acoplamiento (comercio); sin cointegración mayoritaria (12,3% detectado; potencia 23–98%) |
| C — estados EEUU | 24 | 23/23 reproducibles (anual); autocorrelación severa |
| D — HackerEarth | 3 | No reproducible; circularidad demostrada |
| E1 — territorial | 4 | No reproducible |
| E2 — biológico | 2 | 1/2 reproducible (E2_01) |
| E3 — epidémico | 234 | 233/234 reproducibles (OWID); polo sin fricción robusto; nace por receta (≥100 casos) |
| F — planetario | 4 | Sin trayectorias R(t) equivalentes |
| G — geoquímico | 1 | Sin b publicado que verificar |
| ACO — colapsos | 18 | Serie cruda versionada; convergencia descriptiva, ligada a ventanas de evento (nulos AR(1) p=0,013) |

## Zenodo y SSRN

- **Archivo versionado de v2.7.1 (canónico):**
  [DOI 10.5281/zenodo.23661819](https://doi.org/10.5281/zenodo.23661819) —
  snapshot del release 2.7.1 (2026-10-26), contiene los preregistros de la
  ronda 2026-10-26. El primer archivo del mismo día
  ([10.5281/zenodo.23653089](https://doi.org/10.5281/zenodo.23653089)) quedó
  antes de los preregistros y no los incluye. La línea del corpus de 721
  casos sigue en
  [10.5281/zenodo.19446521](https://doi.org/10.5281/zenodo.19446521).
- El DOI [10.5281/zenodo.23678033](https://doi.org/10.5281/zenodo.23678033)
  corresponde a v2.7.3, anterior a la ADENDA 5. El nuevo archivo que sellará
  v2.7.4 y esta adenda aún no está publicado; su DOI se añadirá al publicarse.
- **Preprint en SSRN:** [abstract 6418778](https://ssrn.com/abstract=6418778).
  El manuscrito vigente es la **r33** (2026-10-26, base v2.7.1, subida por el
  autor): añade la tela de incertidumbre integrada y los dos controles
  nuevos (nulos AR(1), cointegración) en el Abstract y el §16; el resto es
  r32 sin cambios. No se presenta como arbitrado.
- **Archivos del manuscrito:** r33 [inglés](papers/snt_ssrn_v33_EN.md) ·
  [español](papers/snt_ssrn_v33.md); r32 (histórico):
  [inglés (PDF)](papers/snt_ssrn_v32_EN.pdf) ·
  [español (PDF)](papers/snt_ssrn_v32.pdf).
- **Cita del software:** [`CITATION.cff`](CITATION.cff), con el DOI canónico
  del corpus y el historial de identificadores publicados; el DOI de v2.7.4
  se añadirá cuando se publique el nuevo archivo.

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
pytest reconstruction_real/tests          # incluye claims y auditoría integral
python reconstruction_real/code/verificar_claims.py
```

La prueba de línea base y permutación de la tela se regenera con
`python reconstruction_real/code/tela_clasificacion_baseline.py` (≈2,5 min,
semilla fija).

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
  `/home/deamon/genomic_agent` (proyecto local independiente, remote de GitHub pendiente de crear; historial completo preservado en la rama `genomic-agent-split` de este repo).

## Marco y cita

El marco activo es **v34**; la información de cita está en
[`CITATION.cff`](CITATION.cff). Contribuye mediante una rama y un pull request;
no hagas commits directamente a `main`. Cada resultado nuevo debe incluir
fuente, receta reproducible y límites de inferencia; registra los cambios en
[`CHANGELOG.md`](CHANGELOG.md).
