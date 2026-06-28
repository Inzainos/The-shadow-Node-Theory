# Shadow Node Theory — Marco Teórico v30

**Elán Zainos Corona** · Fractal Core Research, Tlaxcala, México
ORCID: 0009-0009-9125-253X · Junio 2026

SSRN 6418778 · Zenodo 10.5281/zenodo.19446521 · github.com/Inzainos/The-shadow-Node-Theory

---

## Nota sobre esta versión (v30)

La v30 consolida la v29 (corpus de 721 casos reales, junio 2026) e **integra
como capa central** el desarrollo teórico más reciente: la **Arquitectura de
Colapso Orbital Acoplada (ACO-A)**, reformulada como una **capa universal y
transversal** del marco, no como un módulo aparte. Cambios respecto a la v29:

- **Nueva Parte IV — Capa de Colapso Orbital Acoplado.** El colapso pasa de ser
  un módulo de 18 casos socioeconómicos a un **eje ortogonal (Δ)** acoplado a
  toda la SNT, con evidencia en **cinco dominios** (finanzas, historia, cripto,
  biología, astronomía) usando datos reales.
- **Ley de Inevitabilidad del Colapso** en forma falsable: `h(τ) > 0`.
- **Taxonomía de modos de colapso** gobernada por *fricción × trigger ×
  (piso/techo)*, y el **Principio de Mínima Fricción** como unificador.
- **Cuatro resultados de la hoja de ruta** ya ejecutados con datos reales
  (fricción operacionalizada, ortogonalidad b⊥Δ, biología sin techo, hazard).
- **Hipótesis φ actualizada:** cerrada tras **4 rondas** (la 4ª con control
  placebo); sigue refutada y ahora metodológicamente más sólida.

> Nota de obsolescencia (heredada de v29): el marco v28 y los documentos que
> citan 502 casos deben considerarse **versión obsoleta** en sus cifras
> estadísticas. El corpus de 502 contenía ~188 valores de `b` sintéticos
> (`np.random.normal()`) y R² imposibles (hasta −7.332). Esos valores nunca se
> publicaron como definitivos. La v29/v30 documenta la reconstrucción completa
> con datos primarios reales.

---

## Resumen ejecutivo del cambio

|                         | v28 (obsoleta) | v29           | v30 (actual)                     |
|-------------------------|----------------|---------------|----------------------------------|
| Casos (eje b)           | 502            | 721           | 721                              |
| Datos                   | sintéticos     | REALES        | REALES                           |
| Significativos          | 31%            | 89%           | 89%                              |
| R² corruptos            | ~99            | 0             | 0                                |
| Spearman ρ (fricción→b) | −0.74 (inflado)| −0.68 (n=714) | −0.68 (n=714), p=2.5×10⁻⁹⁷       |
| Test central            | no verificable | p=2.4×10⁻⁷⁴   | p=2.4×10⁻⁷⁴                      |
| Capa de colapso (Δ)     | módulo aparte  | módulo aparte | **eje ortogonal, 5 dominios**    |
| Hazard h(τ)             | —              | —             | **estimado (cripto, n=41)**      |
| H-φ                     | sin probar     | refutada (3)  | **refutada (4 rondas + placebo)**|
| Trazable a fuente       | NO             | SÍ            | SÍ (GitHub público)              |

---

# PARTE I — Fundamentos teóricos

## 1.0 Afirmación central

El universo opera como una red de redes a escala macro, meso y micro, regida por
el mismo algoritmo organizador. Los sistemas complejos a todas las escalas
comparten la topología de red libre de escala, lo que sugiere un principio físico
subyacente común. La Shadow Node Theory demuestra este principio con datos
cuantitativos verificables.

**Niveles de certeza:**

| Nivel | Contenido | Estado |
|-------|-----------|--------|
| 1 | Topología compartida a múltiples escalas (Barabási, IllustrisTNG, SDSS) | DEMOSTRADO |
| 2 | SNT: satelización como ley de potencia; fricción predice b (p=2.4×10⁻⁷⁴); corpus 100% real y reproducible | VERIFICADO (721 casos) |
| 2★ | **Colapso como capa transversal (eje Δ): modos regulares en 5 dominios** | **VERIFICADO / HIPÓTESIS FUERTE (Parte IV)** |
| 3 | Sincronización inter-cerebral como campo colectivo (BrainNet, Waseda, Dartmouth) | HIPÓTESIS ACTIVA |
| 3 | Microtúbulos como decodificadores de información (Penrose-Hameroff, Orch-OR) | HIPÓTESIS ACTIVA |
| 4 | Materia oscura como sustrato conectivo universal | FRONTERA ABIERTA |

## 1.1 Definición formal

Para dos entidades acopladas con un hub dominante y un nodo periférico, la ratio
de dominancia en el tiempo t es:

    R(t) = métrica_hub(t) / métrica_nodo(t)

La SNT postula que, en ausencia de fricción institucional, esta ratio sigue una
ley de potencia:

    R(t) = a · t^b   ⟺   log R(t) = log a + b · log t

donde **b** es el exponente de satelización.

**Interpretación del exponente b:**

- b < 0 → convergencia (el nodo gana terreno relativo)
- b ≈ 0 → equilibrio dinámico
- 0 < b < 1 → satelización sublineal (gradual)
- b ≥ 1 → satelización superlineal (acelerada)

**Roche Radius (b = 1.0):** umbral crítico. Un nodo con b ≥ 1 está en absorción
acelerada — análogo al radio de Roche astronómico (distancia dentro de la cual
las fuerzas de marea superan la cohesión del satélite).

**Nota (v29):** el exponente b es una **métrica descriptiva** de la velocidad y
dirección de satelización, no la afirmación de que la ley de potencia sea el
único modelo generativo en todos los dominios. En sistemas con alta fricción
institucional (economías nacionales), los modelos exponencial y lineal compiten
con la ley de potencia a escala de 100 años. La ley de potencia emerge como mejor
descripción donde la fricción es baja (epidemias, invasiones biológicas).

---

# PARTE II — Corpus v30 (721 casos reales)

## 2.0 Metodología de reconstrucción

Para cada caso: (1) obtener series temporales primarias de fuentes documentadas;
(2) calcular R(t) = métrica_hub(t)/métrica_nodo(t); (3) ajuste OLS en log-log;
(4) registrar b, R² real ∈ [0,1], p-value, IC 95%, Durbin-Watson; (5) verificar
que ningún R² sea negativo ni mayor que 1. Todo el corpus es reproducible desde
`reconstruction_real/`.

## 2.1 Corpus por dominio

| Dominio | Fricción | Casos | Sig. | b̄ | R̄² | Fuente |
|---------|----------|-------|------|------|------|--------|
| A  | media | 4   | 0%   | +0.082 | 0.18 | UN Demographic Yearbook |
| B  | alta  | 446 | 84%  | +0.092 | 0.35 | Maddison 2020 |
| C  | alta  | 24  | 100% | +0.091 | 0.53 | INEGI + US Census |
| D  | baja  | 3   | 100% | −1.364 | 0.87 | HackerEarth 2026 |
| E1 | nula  | 4   | 100% | +2.891 | 0.81 | OWID COVID (spatial) |
| E2 | alta  | 2   | 50%  | +0.145 | 0.12 | MacLulich/Elton |
| E3 | nula  | 234 | 100% | +0.912 | 0.85 | JHU COVID-19 |
| F1 | media | 2   | 100% | −1.807 | 0.40 | Open Exoplanet Catalogue |
| F2 | media | 1   | 100% | +1.273 | 0.48 | Open Exoplanet Catalogue |
| F3 | baja  | 1   | 100% | +1.264 | 0.90 | Open Exoplanet Catalogue |
| **TOTAL** | | **721** | **89%** | **+0.366** | **0.58** | |

Integridad: R²<0: 0 casos · R²>1: 0 casos · p inválidos: 0 casos · cada b
reproducible desde scripts públicos.

## 2.2 Índice de fricción institucional

Escala ordinal 0–3, asignada a priori (antes de calcular los b):

- **3 — Alta:** economías nacionales (B), jerarquías subnacionales (C), sistemas
  depredador-presa (E2, interdependencia mutua).
- **2 — Media:** ciudades históricas (A), sistemas planetarios/estelares (F1, F2;
  resonancia orbital / límites radiativos).
- **1 — Baja:** ecosistemas digitales (D), jerarquías multiplanetarias (F3).
- **0 — Nula:** invasión biológica (E1), crecimiento epidémico (E3).

---

# PARTE III — Hallazgos principales (eje de satelización)

**Hallazgo 1 — La fricción predice la satelización.** Correlación de Spearman
entre índice de fricción y b por caso (dominios sociales/biológicos, n=714):
**ρ = −0.68, p = 2.5×10⁻⁹⁷.** A mayor fricción institucional, menor exponente.

**Hallazgo 2 — Separación de regímenes.** Bio sin fricción (E1+E3): b̄ = +0.95.
Económico con fricción (A+B+C): b̄ = +0.09. **Mann-Whitney U = 103,538,
p = 2.4×10⁻⁷⁴.** Los sistemas sin freno institucional se satelizan ~10× más rápido.

**Hallazgo 3 — Equivalencia mecanística.** Soberanía política (B: b̄=+0.09) y
interdependencia ecológica mutua (E2: b̄=+0.14) son estadísticamente
indistinguibles: dos mecanismos distintos operan como frenos equivalentes.

**Hallazgo 4 — Regímenes de modelado.** El power-law es la mejor descripción
donde la fricción es baja (E3: 6/8 casos; E1: b>1 consistente). En alta fricción
(B): power-law mejor solo ~8%, exponencial ~49%, lineal ~35%. El régimen de ley
de potencia emerge donde la teoría predice satelización libre.

**Hallazgo 5 — Índice de Soberanía Atómica (ASI).** Validación en HackerEarth
2026 (n=4,771 usuarios reales): ROC-AUC train=0.719, test=0.697 (sin
sobreajuste); 5-Event Wall: churn 93% (1 tipo) → 74% (≥5 tipos); zona de
absorción (<0.10) 88% churn; paridad (0.10–1.0) 73%; soberana (≥1.0) 34%.

---

# PARTE IV — Capa de Colapso Orbital Acoplado (ACO-A)

*El colapso como eje ortogonal universal. Evidencia en 5 dominios con datos reales.*

## 4.0 Tesis

La Arquitectura de Colapso Orbital deja de ser un módulo aparte (18 casos
socioeconómicos) y se reformula como una **capa universal y transversal** de la
SNT: el colapso es un **eje ortogonal** que puede activarse en cualquier sistema,
de cualquier dominio, en cualquier punto de su trayectoria. **Un solo principio
(mínima fricción)** genera **distintos modos de colapso** según las condiciones
de frontera.

## 4.1 Espacio de estados: dos ejes ortogonales (b ⊥ Δ)

Cada sistema = par de coordenadas **independientes**:

- **Eje 1 — Satelización:** `R(t) = a·t^b`, `R = m_hub / m_node`. **b** = cómo
  evoluciona la dominancia *mientras la relación acoplada corre*.
- **Eje 2 — Colapso:** `A(τ) = c·τ^Δ`, `A = m_absorbente / m_hub^pico`,
  `τ = tiempo desde la extinción funcional`. **Δ** = velocidad/forma de la
  absorción *una vez que el hub colapsa*.

**Por qué ortogonal (no una 5ª fase):** el colapso no espera a que termine el
ciclo de satelización. Un hub en plena Dependencia o Acumulación puede colapsar
de golpe. Reloj distinto (τ ≠ t), razón distinta, exponente distinto.

**Predicción falsable de ortogonalidad:** entre casos con b *y* Δ medidos,
`corr(b, Δ) ≈ 0`. La ortogonalidad es **b ⊥ Δ**.

**Primer test (cripto, n=11).** Como el corpus de satelización y los casos de
colapso son disjuntos, se usa un dataset emparejado dentro de un dominio:
criptomonedas, donde la misma moneda tiene subida (b_subida) y caída (Δ_caída).
Resultado: **Spearman ρ(b_subida, Δ_caída) = +0.009 (p = 0.98)** — sin relación,
**consistente con la ortogonalidad** (RC-Δ1 no refutado). Reproducible en
`reconstruction_real/code/orthogonality_test.py`. *Caveats:* un solo dominio;
b_subida es un exponente de ascenso de precio (análogo de satelización, no el b
canónico hub/nodo); la ortogonalidad cross-dominio sigue sin testearse.

## 4.2 Capa de hazard h(τ): la inevitabilidad, en forma falsable

Si todo sistema con dinámica tiende al colapso (§4.3), la mayoría de los sistemas
observados **aún no colapsan** → datos censurados por la derecha → marco de
**análisis de supervivencia / función de hazard h(τ)**.

> "Ningún sistema es eterno" = **h(τ) > 0 para todo sistema** (probabilidad de
> colapso nunca cero). Refutable si se halla un sistema con hazard = 0.

| Capa | Variable | Mide |
|------|----------|------|
| Satelización | b | dominancia mientras corre |
| Riesgo de colapso | h(τ) | inevitabilidad + tiempo hasta la extinción |
| Absorción | Δ | velocidad/forma de captura tras la extinción |

`F` (fricción) modula las tres.

**Primer hazard estimado (cripto, n=41).** Supervivencia sobre una cohorte de
criptomonedas (Yahoo); extinción funcional = precio < 1% del máximo histórico
(≥99% de caída sin recuperación). 15 extinciones; **muertes en todo el rango de
edad (0.27 → 8.6 años), sin periodo libre de muerte**; Kaplan-Meier cae sostenido
a ~0.60; hazard positivo y creciente con la edad → **consistente con h(τ)>0**.
Reproducible en `reconstruction_real/code/hazard_crypto.py`. *Caveats:* (1) sesgo
de supervivencia (solo monedas listadas = sobrevivientes → hazard real *mayor*);
(2) confound edad/calendario (casi todas nacidas 2017-18; el pico a ~8 años
refleja en parte el bear market 2022-25); (3) la positividad estricta por-bin
está limitada por n.

## 4.3 Ley de Inevitabilidad del Colapso

> Todo sistema con dinámica tiende a un **punto de colapso**. "Colapso" NO es
> muerte: es un **punto de reorganización crítica** (bifurcación).

Al colapsar, el sistema **decae** (absorción terminal, lo mide Δ) o **da el brinco
/ leapfrog** (renovación, reingreso al ciclo — el Uroboro). El colapso es el
momento donde se decide entre ambos; el camino depende de las reservas del nodo
(criterio RC4, umbral dual RQ/RL). Testigos de brinco: Querétaro (b=−0.155),
Nuevo León (b=−0.058). El "tiempo medio hasta el colapso" es **descriptivo, no
predictivo** para un caso individual.

## 4.4 Taxonomía de modos de colapso (tres factores)

El modo lo gobiernan **fricción × trigger × (¿hay piso/techo en la magnitud?)**:

| Modo | Condición | Forma | Testigo (dato real) |
|------|-----------|-------|---------------------|
| **Decaimiento Orbital Regulado** | fricción alta (física o institucional) | ley de potencia suave **o** exponencial (no acelera) | 2008 (R²=0.85–0.99), Roma/URSS, astro, epidemia |
| **Decaimiento Craquelado** | fricción≈0 + gradual | fragmentación errática (red de grietas) | EOS (R²=0.10–0.70) |
| **Caída-a-piso** | fricción≈0 + abrupto + **con piso** | ley de potencia a un piso residual | FTX (PL R²=0.875) |
| **Acantilado Catastrófico** | fricción≈0 + abrupto + **sin piso** | super-exponencial acelerante | LUNA (5.6 OOM / 11 d) |
| **Barrido logístico** | magnitud **acotada** (frecuencia) | S-curve | Delta→Ómicron (k=0.22/d) |

Anclajes físicos: *Acantilado Catastrófico* → catástrofe de pliegue (Thom).
*Decaimiento Craquelado* → agrietamiento por desecación (craquelure): pérdida de
cohesión que fragmenta por una red de grietas.

**Refinamiento clave (§4.6.2):** el *Decaimiento Orbital Regulado* es
suave / no-acelerante y puede ser **ley de potencia** (scale-free: finanzas,
astro) **o exponencial** (tasa constante: epidemias). Lo que lo separa del
*Acantilado Catastrófico* no es la forma exacta sino que **la tasa NO acelera** —
solo el acantilado es super-exponencial.

## 4.5 Principio de Mínima Fricción (unificador)

> Todo colapso sigue la **trayectoria que minimiza la fricción integrada**. Las
> grietas fractales del craquelado son la solución visible a esa optimización: el
> camino por donde el sistema pierde cohesión gastando lo menos posible.

Familia variacional: Fermat, mínima acción, mínima disipación, el rayo, el río.
Aquí la magnitud minimizada es la **fricción**. **El principio = flujo gradiente
sobre un paisaje de estabilidad** (§4.7).

| Campo de fricción | Camino de mínima fricción | Modo |
|---|---|---|
| Alta y homogénea | sin grieta fácil → drena suave | Regulado |
| ≈0 y heterogénea | muchos canales erráticos → red de grietas | Craquelado |
| ≈0 con un canal único | todo se vacía de golpe | Acantilado Catastrófico |

**Versión falsable:** el colapso realizado tiene menor fricción integrada que las
trayectorias contrafactuales. (WaMu por vía FDIC pre-arreglada = mínima fricción
→ 21 h; Lehman sin esa vía → fragmentación lenta, 30,681 h.)

## 4.6 Evidencia empírica — 5 dominios, datos reales

| Dominio | Caso | Fricción | Piso/techo | Modo | Ajuste | Fuente |
|---------|------|----------|------------|------|--------|--------|
| Astro | Fulguración solar M6.9 | física | — | Regulado | PL exp −0.84, R²=0.975 | NOAA GOES |
| Astro | TDE AT2019qiz | física (viscosidad) | — | Regulado | PL exp −1.07, R²=0.843 (teór. −5/3) | NASA IRSA/ZTF |
| Finanzas | Cohorte 2008 (6 casos) | inst. alta | — | Regulado | PL R²=0.85–0.99 | SEC/FDIC/Fed/SIGTARP |
| Historia | Roma, URSS, Azteca, Cartago | inst. | — | Regulado | PL R²=0.77–0.99 | Maddison 2023 |
| Cripto | EOS (gradual) | ≈0 | — | Craquelado | errático R²=0.10–0.70 | Drive + Yahoo |
| Cripto | FTX / FTT (abrupto) | ≈0 | piso ~$1 | Caída-a-piso | PL R²=0.875 | Yahoo Finance |
| Cripto | LUNA / Terra (abrupto) | ≈0 | sin piso | Acantilado Catastrófico | super-exp, acelera | Yahoo Finance |
| Biología | Delta→Ómicron (Sudáfrica) | (acotado) | techo 100% | Barrido logístico | k=0.218/d, R²=0.79 | CoV-Spectrum/LAPIS |

**Detalle financiero (tiempo a 90% de absorción, en horas — ordena por fricción
de resolución):** WaMu (FDIC) 21 h · Bear Stearns (Fed) 626 h · Wachovia 4,140 h
· Merrill 7,122 h · Chrysler 16,071 h · Lehman (quiebra desordenada) 30,681 h.
Rango ~1,460×. WaMu ≈ 21 h valida contra el hecho real (toma del FDIC en ~48 h).

**Conexión con el hallazgo central SNT:** la fricción institucional predice b
(ρ=−0.68, p=2.5×10⁻⁹⁷, n=714). La fricción **también gobierna la forma de Δ** (el
modo de colapso). La fricción es la palanca de los dos ejes.

### 4.6.1 Fricción operacionalizada (hoja de ruta #1)

Test controlado dentro del cohorte financiero 2008 (mismo dominio y unidades).
Fricción = grado documentado de **pre-arreglo regulatorio del canal de
resolución**, ordinal 1–6 (6 = FDIC receivership/P&A; 5 = Fed-brokered;
4 = gobierno/TARP §363; 3 = FDIC-asistido open-bank; 2 = fusión privada
presionada; 1 = quiebra desordenada). La escala se construye del *mecanismo
institucional*, no de Δ.

| Test (n=6) | Resultado |
|---|---|
| Fricción vs Δ (exponente de colapso) | **Spearman ρ = −1.000, p < 0.001** |
| Fricción vs log(tiempo a 90%) | ρ = −0.829, p = 0.042 |

Más fricción → Δ más pequeño (absorción frontal y ordenada). Operacionaliza "la
fricción gobierna la forma de Δ" como afirmación **medida y falsable**
(RC-Δ2/RC-Δ4). Reproducible en `reconstruction_real/code/friction_operational.py`.
*Caveats:* n=6; el ordinal es un juicio documentado (conviene pre-registrar la
escala antes de ampliar casos).

### 4.6.2 Biología con magnitud sin techo (hoja de ruta #3)

La *frecuencia* de variante está acotada [0,1] → logística por construcción. Para
salir del régimen logístico medimos el colapso de una **ola epidémica en casos
absolutos** (sin techo): ola Ómicron en Sudáfrica (JHU CSSE), pico 14 dic 2021
(~23,437 casos/día), caída a 11% del pico en 49 d.

| Ajuste de la caída | R² |
|---|---|
| Ley de potencia | 0.863 |
| **Exponencial** (e-fold ≈ 22 d) | **0.958** |

La caída es **suave (exponencial), NO acantilado** (los retornos no aceleran).
Aun sin techo, el colapso biológico se mantiene **regulado**: la
retroalimentación epidemiológica (inmunidad, agotamiento de susceptibles,
R_eff<1) es **fricción intrínseca**. Reproducible en
`reconstruction_real/code/bio_unbounded_collapse.py`.

### 4.6.3 Ortogonalidad b⊥Δ (hoja de ruta #2)

Ver §4.1: cripto n=11, **ρ(b_subida, Δ_caída) = +0.009 (p = 0.98)** → consistente
con b⊥Δ. Falta el test cross-dominio con un dataset emparejado.

### 4.6.4 Hazard h(τ) (hoja de ruta #4)

Ver §4.2: cripto n=41, 15 extinciones, **h(τ)>0 en todo el rango de edad**.

## 4.7 El lenguaje visual: paisajes de estabilidad ("gráficas de valles")

El sistema es una bola en un valle (cuenca de atracción) de un paisaje de
potencial; la fricción controla cómo rueda; el colapso es la bola saliendo de su
valle. **Los modos son geometrías distintas del mismo paisaje**
(`figures/fig_paisajes_colapso.{svg,png}`):

- **Regulado:** valle que se inclina/aplana despacio → la bola rueda suave.
- **Acantilado Catastrófico:** catástrofe de pliegue — la pared del valle
  desaparece y la bola cae hasta el fondo (cero, sin piso).
- **Caída-a-piso:** igual, pero un valle intermedio (piso) atrapa la bola.
- **Craquelado:** paisaje rugoso/fractal, muchos canales someros.
- **Barrido logístico:** doble pozo (valle-Delta → valle-Ómicron).
- **Leapfrog:** la bola escapa hacia arriba, a un valle mejor (renovación).

`figures/fig_catastrofe_cuspide.{svg,png}` muestra la catástrofe de pliegue: al
bajar la fricción (parámetro de control), el valle estable y su barrera se
aniquilan y el sistema cae por el acantilado. Anclajes: teoría de catástrofes
(Thom), paisaje epigenético de Waddington, "ball-in-cup" de resiliencia ecológica
(Holling), tipping points climáticos (Lenton).

## 4.8 Conexión con la SNT existente

- **F (fricción)** ya vive en ASI = δH·α/F → Δ se conecta vía F sin fingir que es
  el mismo número que b.
- **Leapfrog / RC4** → la bifurcación del colapso.
- **Ciclo de satelización** → el colapso es ortogonal a sus fases.
- En astronomía **F es literal**: la *dynamical friction* de Chandrasekhar y la
  viscosidad del disco gobiernan la absorción (TDE, fusiones).

## 4.9 Caveats / honestidad metodológica

- Lado cripto = n=2 limpios (EOS + LUNA) + FTX; n chico.
- Es **correlacional**: los dominios difieren en más que la fricción (escala, qué
  es "masa", microestructura). Enmarcar como hipótesis.
- LUNA y la fulguración solar no son ACO de absorción con absorbente único →
  entran como evidencia de *forma/modo de colapso*.
- TDE exp −1.07 vs −5/3 teórico: más somero por banda g + resta de host
  imperfecta; el punto es que es ley de potencia (regulado), no el exponente.
- "Tiempo a 90%" depende del umbral; el **orden** abrupto < gradual es robusto.
- Frecuencias (Ómicron) son acotadas → logístico por construcción.

---

# PARTE V — Hipótesis φ (cerrada)

**ESTADO: REFUTADA tras 4 rondas de validación independiente.**

H-φ postulaba que el exponente b tendería a agruparse cerca de fracciones de la
proporción áurea (φ = 1.618...), conjunto {φ/4, φ/3, φ/2, 2φ/3, 3φ/4, φ} ±0.10.

- **Ronda 1 (crypto):** 0/4 datasets con señal de φ.
- **Ronda 2 (literatura biológica primaria):** 0/6 datasets con señal.
- **Ronda 3 (corpus real, n=188, b>0):** 26.6% cerca de φ vs 27.5% esperado por
  azar (Monte Carlo N=5,000), **p = 0.642 — idéntico al azar.**
- **Ronda 4 (re-test corpus 721 + control placebo):** al re-correr sobre el
  corpus expandido apareció una **señal aparente** que obligó a un análisis más
  riguroso:

| Subconjunto | % cerca de φ | null uniforme | placebo (objetivos aleatorios) |
|---|---|---|---|
| Corpus b>0 (n=534) | 42.3% | p<0.001 (señal) | **p=0.170 — NO especial** |
| Bio sin fricción E1+E3 (n=238) | 60.1% | p<0.001 | p<0.001 (sobrevive) |

Dos trampas identificadas: (1) **cobertura de bandas** — las 6 bandas de φ (±0.10)
tapizan densamente [0.3–1.3], justo donde b se concentra; el null uniforme
sobreestima el azar, y un placebo (6 objetivos *aleatorios* en el mismo rango)
muestra que para el corpus completo φ **no es especial** (p=0.170); (2)
**pseudoreplicación** — el "signal" bio sobrevive el placebo, pero E3 son 234
países midiendo la MISMA pandemia (COVID), no datos independientes; la b
característica de COVID ≈ 0.846 cae a 0.037 de φ/2 = 0.809: una sola coincidencia
replicada 234×, no un atractor.

**Conclusión: H-φ sigue refutada.** El corpus expandido NO la rescata. *Lección
metodológica:* el test de φ requiere **placebo control** (objetivos aleatorios) y
**manejo de no-independencia**, no solo un null uniforme. H-φ se clasifica como
**hipótesis especulativa de segundo orden**; no se incluye en los claims del
paper principal y no afecta la validez del marco SNT general, el exponente b ni
el ASI. Sub-hipótesis H-3 (denominador 3 dominante en b/φ): **descartada**.
Reproducible: `papers/phi_retest.py` + `papers/phi_placebo.py`.

---

# PARTE VI — Módulos teóricos extendidos

Los siguientes módulos del marco v28 se mantienen sin cambios (no contienen
cifras del corpus empírico): Módulo I — Taxonomía de Nodos (5 niveles); Módulo II
— Sistema N-Cuerpos y Nodo Atómico; Módulo III — Dominio Individual; Módulo IV —
Dominio Empresarial; Módulo V — Leapfrog Cognitivo y ASI (conceptual); Módulo VI
— Casos Históricos (Tlaxcala, narrativa); Apéndice A — Sistema Sentinel Omega.

**Nota:** los casos históricos individuales (Brujas→Amberes, Toledo→Madrid, etc.)
son narrativamente correctos como motivación, pero los valores específicos de b
citados en v28 no son verificables desde el corpus v29/v30. Deben citarse como
ilustración cualitativa, no como cifras formales del corpus.

---

# PARTE VII — Estado de publicaciones

- **SSRN (abstract 6418778):** PUBLICADO — preprint activo. Cifras v28; actualizar
  a v30.
- **Zenodo (DOI 10.5281/zenodo.19446521):** PUBLICADO — v2.5.0.
- **PLOS Complex Systems (PCSY-D-26-00059):** REVISIÓN MAYOR — deadline 10 ago
  2026. Cifras actualizadas a v29 (721 casos). Editor: Haroldo V. Ribeiro;
  EIC: Hocine Cherifi.
- **Journal of Complex Networks (COMNET-2026-214):** RECHAZADO sin revisión
  (Yamir Moreno). Acción: re-someter a Scientific Reports / Physica A.
- **MIT GCFP 13th Annual Conference:** EN PREPARACIÓN — deadline 17 jul 2026.
  Tesis: la fricción institucional regulariza la *forma* del colapso.
- **Papers sin liberar (requieren actualización a v30):** J. Theoretical Biology,
  Astrophysical Journal, Investigación Económica.

---

# Hoja de ruta (estado actualizado)

1. **Operacionalizar la fricción** a lo largo de un camino, por dominio.
   *PRIMER RESULTADO (§4.6.1): fricción de resolución vs Δ, ρ=−1.000, n=6.* Falta
   extender a más casos/dominios con escala pre-registrada.
2. **Test de ortogonalidad** `corr(b,Δ)≈0`. *PRIMER RESULTADO (§4.1/§4.6.3):
   cripto n=11, ρ=+0.009.* Falta test cross-dominio.
3. **Más casos por modo** (n=3+ cripto; varios TDEs). *Biología sin techo: PRIMER
   RESULTADO (§4.6.2) — Ómicron en casos absolutos decae exponencial suave
   (R²=0.96), no acantilado.* Falta buscar un colapso biológico SIN fricción
   intrínseca (shock externo abrupto).
4. **Formalizar h(τ).** *PRIMER RESULTADO (§4.2/§4.6.4): cripto n=41, h(τ)>0 en
   todo el rango de edad.* Falta cohorte más grande sin sesgo de supervivencia y
   desenredar edad vs calendario.
5. **Definir el "piso" con rigor** y decidir si se folda en la fricción o es un
   tercer eje independiente.
6. **Validación independiente / pre-registro** antes de afirmar causalidad (hoy
   todo es correlacional y descriptivo).

---

# Referencias

- Bolt, J. & van Zanden, J.L. (2020). *Maddison Project Database 2020.* Maddison
  Project Working Paper 15. University of Groningen.
- INEGI (2022). *PIB per cápita por entidad federativa.* Sistema de Cuentas
  Nacionales de México.
- US Census Bureau (2023). *Historical state population estimates.*
- Dong, E., Du, H. & Gardner, L. (2020). An interactive web-based dashboard to
  track COVID-19 in real time. *The Lancet Infectious Diseases*, 20(5), 533–534.
  [Johns Hopkins CSSE]
- MacLulich, D.A. (1937). Fluctuations in the numbers of the varying hare.
  *University of Toronto Studies*, Biol. Ser. 43.
- Elton, C. & Nicholson, M. (1942). The ten-year cycle in numbers of the lynx in
  Canada. *Journal of Animal Ecology*, 11(2), 215–244.
- Open Exoplanet Catalogue (2024).
- Thom, R. (1972). *Stabilité structurelle et morphogénèse.* [catástrofe de pliegue]
- Waddington, C.H. (1957). *The Strategy of the Genes.* [paisaje epigenético]
- Holling, C.S. (1973). Resilience and stability of ecological systems. *Annual
  Review of Ecology and Systematics*, 4, 1–23.
- Lenton, T.M. et al. (2008). Tipping elements in the Earth's climate system.
  *PNAS*, 105(6), 1786–1793.
- NOAA SWPC GOES X-ray flux; NASA IRSA / ZTF (TDE AT2019qiz); CoV-Spectrum / LAPIS.

---

# Repositorio y datos

GitHub: github.com/Inzainos/The-shadow-Node-Theory · Corpus v5 (721 casos):
`reconstruction_real/data/snt_corpus_REAL_v5.csv`. Capa de colapso:
`papers/SNT_Colapso_Acoplado.md`; scripts en `reconstruction_real/code/`
(`friction_operational.py`, `orthogonality_test.py`, `bio_unbounded_collapse.py`,
`hazard_crypto.py`, `collapse_multidomain.py`, `make_collapse_landscapes.py`);
hipótesis φ: `hypotheses/snt_phi_hypothesis.md` + `papers/phi_retest.py` +
`papers/phi_placebo.py`.

SSRN: https://ssrn.com/abstract=6418778 · Zenodo:
https://doi.org/10.5281/zenodo.19446521

---

*Fractal Core Research — Tlaxcala, México · Marco Teórico v30 · Junio 2026*
*"Verdad técnica por encima de impresión numérica."*
