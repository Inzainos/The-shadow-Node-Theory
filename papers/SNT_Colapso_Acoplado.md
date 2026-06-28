# Arquitectura de Colapso Orbital Acoplada (ACO-A)
## Una capa universal de colapso para la Shadow Node Theory

**Elán Zainos Corona** · Fractal Core Research, Tlaxcala, México
SSRN 6418778 · Zenodo 10.5281/zenodo.19446521 · github.com/Inzainos/The-shadow-Node-Theory

*Documento teórico — borrador integrado. Evidencia en 5 dominios con datos reales.*

---

## 0. Tesis

La Arquitectura de Colapso Orbital (ACO) deja de ser un módulo aparte (18 casos
socioeconómicos) y se reformula como una **capa universal y transversal** de la
SNT: el **colapso** es un eje ortogonal que puede activarse en cualquier sistema,
de cualquier dominio, en cualquier punto de su trayectoria. Lo demostramos con
datos reales en **cinco dominios** — finanzas, historia/economía, cripto,
biología y astronomía — y mostramos que **un solo principio (mínima fricción)**
genera **distintos modos de colapso** según las condiciones de frontera.

---

## 1. Espacio de estados: dos ejes ortogonales (b ⊥ Δ)

Cada sistema = par de coordenadas **independientes**:

- **Eje 1 — Satelización:** `R(t) = a · t^b`, `R = m_hub / m_node`.
  **b** = cómo evoluciona la dominancia *mientras la relación acoplada corre*.
- **Eje 2 — Colapso:** `A(τ) = c · τ^Δ`, `A = m_absorbente / m_hub^pico`,
  `τ = tiempo desde la extinción funcional`.
  **Δ** = velocidad/forma de la absorción *una vez que el hub colapsa*.

**Por qué ortogonal (no una 5ª fase):** el colapso no espera a que termine el
ciclo de satelización. Un hub en plena Dependencia o Acumulación puede colapsar
de golpe. Reloj distinto (τ ≠ t), razón distinta, exponente distinto.

**Predicción falsable de ortogonalidad:** entre casos con b *y* Δ medidos,
`corr(b, Δ) ≈ 0`. (Δ y su propio *tiempo de absorción* sí correlacionan: ambos
viven en el eje de colapso. La ortogonalidad es **b ⊥ Δ**.)

**Primer test (cripto, n=11).** El corpus de satelización y los casos de colapso
son entidades disjuntas, así que el test usa un dataset emparejado dentro de un
dominio: criptomonedas, donde la misma moneda tiene subida (exponente b_subida,
ascenso al máximo histórico) y caída (Δ_caída, colapso desde el máximo).
Resultado: **Spearman ρ(b_subida, Δ_caída) = +0.009 (p = 0.98)** — sin relación,
**consistente con la ortogonalidad** (RC-Δ1 no refutado). Reproducible en
`reconstruction_real/code/orthogonality_test.py`; datos en
`reconstruction_real/data/orthogonality_crypto_v25.csv`. *Caveats:* un solo
dominio; b_subida es un exponente de ascenso de precio (análogo de satelización,
no el b canónico hub/nodo); la ortogonalidad cross-dominio sigue sin testearse.

---

## 2. Capa de hazard h(τ): la inevitabilidad, en forma falsable

Si todo sistema con dinámica tiende al colapso (§3), la mayoría de los sistemas
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
edad (0.27 → 8.6 años), sin periodo libre de muerte**; Kaplan-Meier cae de forma
sostenida a ~0.60; hazard positivo y creciente con la edad → **consistente con
h(τ)>0**. Reproducible en `reconstruction_real/code/hazard_crypto.py`; tabla en
`reconstruction_real/data/hazard_crypto_v25.csv`. *Caveats:* (1) sesgo de
supervivencia (solo monedas listadas = sobrevivientes → hazard real *mayor*);
(2) confound edad/calendario (casi todas nacidas 2017-18; el pico a ~8 años
refleja en parte el bear market 2022-25); (3) la positividad estricta por-bin
está limitada por n.

---

## 3. Ley de Inevitabilidad del Colapso

> Todo sistema con dinámica tiende a un **punto de colapso**. "Colapso" NO es
> muerte: es un **punto de reorganización crítica** (bifurcación).

Al colapsar, el sistema **decae** (absorción terminal, lo mide Δ) o **da el
brinco / leapfrog** (renovación, reingreso al ciclo — el Uroboro). El colapso es
el momento donde se decide entre ambos; el camino depende de las reservas del
nodo (criterio RC4, umbral dual RQ/RL). Testigos de brinco: Querétaro
(b=−0.155), Nuevo León (b=−0.058).

---

## 4. Taxonomía de modos de colapso (tres factores)

El modo lo gobiernan **fricción × trigger × (¿hay piso/techo en la magnitud?)**:

| Modo | Condición | Forma | Testigo (dato real) |
|------|-----------|-------|---------------------|
| **Decaimiento Orbital Regulado** | fricción alta (física o institucional) | ley de potencia suave | 2008 (R²=0.85–0.99), Roma/URSS, **astro** |
| **Decaimiento Craquelado** | fricción≈0 + gradual | fragmentación errática (red de grietas) | EOS (R²=0.10–0.70) |
| **Caída-a-piso** | fricción≈0 + abrupto + **con piso** | ley de potencia a un piso residual | FTX (PL R²=0.875) |
| **Acantilado Catastrófico** | fricción≈0 + abrupto + **sin piso** | super-exponencial acelerante | LUNA (5.6 OOM / 11 d) |
| **Barrido logístico** | magnitud **acotada** (frecuencia) | S-curve | Delta→Ómicron (k=0.22/d) |

Anclajes físicos de los nombres: *Acantilado Catastrófico* → catástrofe de
pliegue (Thom). *Decaimiento Craquelado* → agrietamiento por desecación
(craquelure): pérdida de cohesión que fragmenta por una red de grietas.

---

## 5. Principio de Mínima Fricción (unificador)

> Todo colapso sigue la **trayectoria que minimiza la fricción integrada**. Las
> grietas fractales del craquelado son la solución visible a esa optimización:
> el camino por donde el sistema pierde cohesión gastando lo menos posible.

Familia variacional: Fermat, mínima acción, mínima disipación, el rayo, el río.
Aquí la magnitud minimizada es la **fricción**. **El principio = flujo gradiente
sobre un paisaje de estabilidad** (ver §7).

**Unifica los tres modos** — misma ley sobre campos de fricción distintos:

| Campo de fricción | Camino de mínima fricción | Modo |
|---|---|---|
| Alta y homogénea | sin grieta fácil → drena suave | Regulado |
| ≈0 y heterogénea | muchos canales erráticos → red de grietas | Craquelado |
| ≈0 con un canal único | todo se vacía de golpe | Acantilado Catastrófico |

**Versión falsable:** el colapso realizado tiene menor fricción integrada que
las trayectorias contrafactuales. (WaMu por vía FDIC pre-arreglada = mínima
fricción → 21 h; Lehman sin esa vía → fragmentación lenta, 30,681 h.)

**Caveat:** para volverlo medible hay que **operacionalizar "fricción a lo largo
de un camino"** por dominio. Trabajo pendiente.

---

## 6. Evidencia empírica — 5 dominios, datos reales

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
(Spearman ρ = −0.68, p = 2.5×10⁻⁹⁷, n=714). Ahora mostramos que **la fricción
también gobierna la forma de Δ** (el modo de colapso). La fricción es la palanca
de los dos ejes.

### 6.4 Fricción operacionalizada (primer resultado)

Test controlado dentro del cohorte financiero 2008 (mismo dominio y unidades).
Fricción = grado documentado de **pre-arreglo regulatorio del canal de
resolución**, ordinal 1–6 (6 = FDIC receivership/P&A; 5 = Fed-brokered;
4 = gobierno/TARP §363; 3 = FDIC-asistido open-bank; 2 = fusión privada
presionada; 1 = quiebra desordenada sin resolución). La escala se construye del
*mecanismo institucional*, no de Δ.

| Test (n=6) | Resultado |
|---|---|
| Fricción vs Δ (exponente de colapso) | **Spearman ρ = −1.000, p < 0.001** |
| Fricción vs log(tiempo a 90%) | ρ = −0.829, p = 0.042 |

Más fricción → Δ más pequeño (absorción frontal y ordenada). Esto operacionaliza
"la fricción gobierna la forma de Δ" como afirmación **medida y falsable**
(RC-Δ2/RC-Δ4). Reproducible en `reconstruction_real/code/friction_operational.py`.
*Caveats:* n=6; el ordinal de fricción es un juicio documentado (no circular,
pero conviene pre-registrar la escala antes de ampliar casos).

### 6.5 Biología con magnitud sin techo (epidemia, casos absolutos)

La *frecuencia* de variante está acotada [0,1] → logística por construcción
(§6 Delta→Ómicron). Para salir del régimen logístico medimos el colapso de una
**ola epidémica en casos absolutos** (sin techo): ola Ómicron en Sudáfrica
(JHU CSSE), pico 14 dic 2021 (~23,437 casos/día), caída a 11% del pico en 49 d.

| Ajuste de la caída | R² |
|---|---|
| Ley de potencia | 0.863 |
| **Exponencial** (e-fold ≈ 22 d) | **0.958** |

La caída es **suave (exponencial), NO acantilado** (los retornos no aceleran).
Aun sin techo, el colapso biológico se mantiene **regulado**: la
retroalimentación epidemiológica (inmunidad, agotamiento de susceptibles,
R_eff<1) es **fricción intrínseca**. Reproducible en
`reconstruction_real/code/bio_unbounded_collapse.py`.

**Refinamiento de la taxonomía:** el modo *Decaimiento Orbital Regulado* es
suave / no-acelerante, y puede ser **ley de potencia** (scale-free: finanzas,
astro) **o exponencial** (tasa constante: epidemias). Lo que lo separa del
*Acantilado Catastrófico* no es la forma exacta sino que **la tasa NO acelera**
— solo el acantilado es super-exponencial.

---

## 7. El lenguaje visual: paisajes de estabilidad ("gráficas de valles")

El sistema es una bola en un valle (cuenca de atracción) de un paisaje de
potencial; la fricción controla cómo rueda; el colapso es la bola saliendo de su
valle. **Los modos son geometrías distintas del mismo paisaje** (ver
`figures/fig_paisajes_colapso.{svg,png}`):

- **Regulado:** valle que se inclina/aplana despacio → la bola rueda suave.
- **Acantilado Catastrófico:** catástrofe de pliegue — la pared del valle
  desaparece y la bola cae a un valle hasta el fondo (cero, sin piso).
- **Caída-a-piso:** igual, pero un valle intermedio (piso) atrapa la bola.
- **Craquelado:** paisaje rugoso/fractal, muchos canales someros.
- **Barrido logístico:** doble pozo (valle-Delta → valle-Ómicron).
- **Leapfrog:** la bola escapa hacia arriba, a un valle mejor (renovación).

`figures/fig_catastrofe_cuspide.{svg,png}` muestra la **catástrofe de pliegue**:
al bajar la fricción (parámetro de control), el valle estable y su barrera se
aniquilan y el sistema cae por el acantilado.

Anclajes establecidos: teoría de catástrofes (Thom), paisaje epigenético de
Waddington (biología), "ball-in-cup" de resiliencia ecológica (Holling), tipping
points climáticos (Lenton). La gráfica de valles es el lenguaje común que une la
SNT con estos marcos.

---

## 8. Caveats / honestidad metodológica

- Lado cripto = n=2 limpios (EOS + LUNA) + FTX; n chico.
- Es **correlacional**: los dominios difieren en más que la fricción (escala,
  qué es "masa", microestructura). Enmarcar como hipótesis.
- LUNA y la fulguración solar no son ACO de absorción con absorbente único →
  entran como evidencia de *forma/modo de colapso*.
- TDE exp −1.07 vs −5/3 teórico: más somero por banda g + resta de host
  imperfecta; el punto es que es ley de potencia (regulado), no el exponente.
- "Tiempo a 90%" depende del umbral (scale-free); el **orden** abrupto < gradual
  es robusto a 0.5/0.9/0.95.
- Frecuencias (Ómicron) son acotadas → logístico por construcción; la taxonomía
  cliff/craquelado/regulado aplica a magnitudes sin techo.

---

## 9. Conexión con la SNT existente

- **F (fricción)** ya vive en ASI = δH·α/F → Δ se conecta vía F sin fingir que
  es el mismo número que b.
- **Leapfrog / RC4** → la bifurcación del colapso.
- **Ciclo de satelización** → el colapso es ortogonal a sus fases.
- En astronomía **F es literal**: la *dynamical friction* de Chandrasekhar y la
  viscosidad del disco gobiernan la absorción (TDE, fusiones).

---

## 10. Hoja de ruta

1. **Operacionalizar la fricción** a lo largo de un camino, por dominio.
2. Más casos por modo (n=3+ cripto; más TDEs; bio sin techo: carga viral
   absoluta, no frecuencia).
3. Test de ortogonalidad `corr(b, Δ) ≈ 0` — primer resultado (cripto, n=11,
   ρ=+0.009; ver §1). Falta el test cross-dominio.
4. Formalizar h(τ) con datos de supervivencia de poblaciones de sistemas.
5. Reestructurar el repo: ACO de módulo paralelo → capa transversal; renombrar
   exponente de absorción a **Δ**.

---

## 11. Conclusiones

1. **El colapso es universal y tiene estructura.** Demostrado con datos reales
   en 5 dominios independientes (finanzas, historia, cripto, biología,
   astronomía): la absorción post-extinción sigue formas funcionales regulares
   y clasificables, no es ruido idiosincrático.
2. **La fricción es la palanca de los dos ejes.** Gobierna **b** (velocidad de
   satelización, ρ=−0.68, n=714) y la **forma de Δ** (el modo de colapso). Una
   sola variable une "cómo dominas" y "cómo colapsas".
3. **Un solo principio genera todos los modos.** Mínima fricción = flujo
   gradiente sobre un paisaje de estabilidad; la geometría del campo de fricción
   (× trigger × piso) decide si el colapso es regulado, craquelado, caída-a-piso
   o acantilado catastrófico.
4. **Colapso ≠ muerte.** Es una bifurcación: decaer o brincar (leapfrog). La
   extinción del hub genera los recursos del siguiente nivel (Uroboro).

## 12. Hallazgos concretos

- **Orden por fricción de resolución (finanzas 2008):** WaMu 21 h → Lehman
  30,681 h, rango ~1,460×, monotónico con el grado de intervención regulatoria.
- **La fricción regulariza la forma:** con fricción → ley de potencia suave
  (R²=0.85–0.99 en finanzas e historia; **R²=0.975 fulguración solar; 0.84
  TDE**). Sin fricción → la regularidad se rompe (EOS errático R²=0.10–0.70).
- **Acantilado catastrófico verdadero requiere ausencia de piso:** LUNA (sin
  piso) → 5.6 órdenes de magnitud en 11 días, super-exponencial; FTX (con piso
  ~$1) → caída-a-piso tipo ley de potencia. Mismo trigger, distinto resultado.
- **En magnitudes acotadas el modo es logístico siempre:** Delta→Ómicron
  k=0.218/día (odds se duplican cada 3.2 días), R²=0.79.
- **En astronomía la fricción es literal** (viscosidad de disco, fricción
  dinámica de Chandrasekhar) y produce el caso regulado más limpio y con
  exponente derivable de primeros principios (TDE ~ t^(−5/3)).

## 13. Utilidades (para qué sirve)

- **Política de resolución / estabilidad financiera:** Δ como diagnóstico
  *ex post* de si los regímenes de resolución ordenada (Title II, FDIC SPOE)
  cumplen su promesa de transferencia rápida; medición temporal de la
  concentración "too-big-to-fail".
- **Alerta temprana sistémica:** un campo de fricción que se erosiona predice
  *qué modo* de colapso viene (riesgo de acantilado vs decaimiento manejable).
- **Epidemiología / genómica:** la velocidad logística de reemplazo de variantes
  como métrica de ventaja selectiva — alimenta directamente el SNT Genomic
  Analyzer (una sucesión de variantes es colapso orbital con captura de nicho).
- **Ecología y resiliencia:** distinguir sistemas frágiles (baja fricción →
  acantilado) de sistemas con decaimiento amortiguado; dónde intervenir.
- **Lenguaje común:** el paisaje de estabilidad ("gráficas de valles") permite
  hablar de colapso con el mismo vocabulario en finanzas, biología, ecología y
  física — y conecta la SNT con teoría de catástrofes, Waddington, Holling y
  tipping points.
- **Marco falsable y transferible:** un mismo kit de diagnóstico (b, Δ, h(τ), F,
  modos) aplicable y refutable en cualquier dominio.

## 14. Qué nos faltaría

- **Operacionalizar la fricción a lo largo de un camino**, por dominio — es lo
  que vuelve el Principio de Mínima Fricción medible y no poético. *(Prioridad 1
  — PRIMER RESULTADO en §6.4: fricción de resolución vs Δ, ρ=−1.000, n=6. Falta
  extender a más casos y otros dominios, con escala pre-registrada.)*
- **Más casos por modo:** n=3+ cripto; varios TDEs. *Biología sin techo: PRIMER
  RESULTADO (§6.5) — ola Ómicron en casos absolutos decae exponencial suave
  (R²=0.96), no acantilado; la biología tiene fricción intrínseca.* Falta:
  buscar algún colapso biológico SIN fricción intrínseca (¿extinción abrupta
  por shock externo?) para ver si ahí sí aparece el acantilado.
- **Test de ortogonalidad** `corr(b, Δ) ≈ 0` — PRIMER RESULTADO (cripto, n=11,
  ρ=+0.009, p=0.98 → consistente con b⊥Δ). Falta un test cross-dominio con un
  dataset emparejado (misma entidad con b y Δ).
- **Formalizar h(τ)** — PRIMER RESULTADO (§2: cripto, n=41, h(τ)>0 en todo el
  rango de edad). Falta: cohorte más grande sin sesgo de supervivencia (incluir
  monedas muertas no listadas) y desenredar edad vs calendario; extender a otros
  dominios (longevidad de empresas, imperios).
- **Definir el "piso" con rigor** y decidir si se folda en la fricción o es un
  tercer eje independiente (hoy es factor, no variable medida).
- **Reestructurar el repo:** ACO de módulo paralelo → capa transversal;
  renombrar el exponente de absorción a **Δ** de forma consistente.
- **Validación independiente / pre-registro** antes de afirmar causalidad (hoy
  todo es correlacional y descriptivo).

---

## Fuentes de datos de esta versión
- Cripto: CSVs propios (EOS, ETH) + Yahoo Finance (LUNA1-USD, FTT-USD).
- Biología: CoV-Spectrum / LAPIS open (GenBank), Sudáfrica.
- Astronomía: NOAA SWPC GOES (rayos X), NASA IRSA / ZTF (TDE AT2019qiz).
- Socioeconómico: corpus ACO v2.4.0 (`reconstruction_real/`), Maddison, SEC,
  FDIC, Federal Reserve, SIGTARP.

*Fractal Core Research · Tlaxcala, México · 2026*
*"Verdad técnica sobre impresión numérica."*
