# COPIA DE REGISTRO — Ueno v3 (corrección 2026-11-09)
# Archivo original: snt-taxonomia/ueno-acoa-tela-cimatica-incertidumbre.md
# Versión: sin número de versión v1/v2; marco SNT v2.7.5.1 / marco v34
# Estado: archivo de registro — SIN CAMBIOS respecto al original. Cuerpo intacto; solo se añadió esta cabecera.
# Fecha de la copia: 2026-11-09
# md5 original: 8eca6f13c5a299108056227cf2f7fb19
# sha256 original: 07ed9e840f7107ba13fbf619e924413121e06a266e4176f86987978a02bebac5
#
# La forma de Ueno en el ACO-A y las telas (cimática + incertidumbre)

**Fecha:** 2026-11-07. **Caso:** Ueno Bank, Paraguay. **Marco:** SNT v2.7.5.1 (README del repo, marco v34).
**Datos de Ueno:** `tabla-maestra-ueno-mef.csv` CORREGIDA (45 filas, 30 meses con R, todos PDF) + `modelo-ueno-resultados-v2.md`.
**Método:** procedimientos VERBATIM de `reconstruction_real/code/tela_cimatica.py`
(`trayectorias` / `espectro` / `rasgos` / `clasificacion_loo`) y de
`tela_de_incertidumbre.py` (m = R, τ = (t−t_min)/(t_max−t_min), u = NULL).
Script: `/tmp/ueno_tela.py` (numpy/pandas/matplotlib/scipy; dos corridas
idénticas). **Nada de esto toca el repo**: los archivos del repo se leen,
no se modifican; todas las salidas están en `~/workspace/snt-taxonomia/`.

## 0. Lo que se verificó en el repo ANTES de calcular

Las tres cosas que Elán nombró por micrófono existen en el repo, con estos
contenidos exactos (no se inventa ninguna definición):

| Lo nombrado | Dónde está | Qué es, según el repo |
|---|---|---|
| **ACO-A** | `README.md` Módulo 1; `reconstruction_real/audits/BACKCAST_PROSPECTIVA_2026-10-26.md`; `preregistro/ADENDA5_PROSPECTIVA_DELISTADOS_Y_HASH_2026-10-27.md` | Capa 2, Colapso orbital acoplado. Criterio: (1) extinción funcional del hub o nodo, (2) absorción de recursos por nodo específico identificable. `A(τ) = c·τ^Δ`. Modos: Regulado, Craquelado, Caída a piso, Acantilado Catastrófico, Barrido Logístico (descriptivos, sin prueba de n grande). Prueba prospectiva: cohorte v2 congelada (491 pares vivos al corte 2026-09-30, 440 candidatos), ventana **2026-09-30 → 2027-09-30**; P1a ✓ (53/389 colapsos observados), P2 ✓ (mediana Δ = −0.961, n=22 maduros), P3 INCONCLUSO (ρ = +0.189, IC95 [−0.253, +0.566]). ADENDA 5: sin imputación; delisting ≠ colapso; seguimiento incompleto = censura a la derecha, no evento ni no-evento. |
| **Tela cimática** | `reconstruction_real/audits/TELA_CIMATICA_2026-10-21.md`; `code/tela_cimatica.py`; `figures/tela_simática.png` | La tela es la placa de Chladni, los 7,306 puntos son la arena, φ es el tono. Piezas: placa (densidad continua τ × log₁₀ m), figura (trayectoria mediana log₁₀ m(τ) por dominio), tonos (FFT armónicos 1–16), huellas (m en τ=0/0.25/0.5/0.75/1, A1/A2/A3, m máx), prueba leave-one-out. Veredictos de la auditoría: la figura sola **NO identifica el dominio (21.2%)**; el tono φ se identifica **parcialmente (53.7%)**; la figura revela el régimen de fricción, no la etiqueta del instrumento; ACO real 13/18 = 72%. |
| **Tela de incertidumbre (Axioma 0)** | `reconstruction_real/audits/TELA_DE_INCERTIDUMBRE_2026-10-21.md`; `code/tela_de_incertidumbre.py`; marco v33/v34 | Cubo 𝒞(u, m, τ). **m = R** (la razón medida, proxy declarado del dominio) — DEFINIDO. **τ = fase temporal normalizada** — DEFINIDO. **u = apertura de posibilidades — NO DEFINIDO en ningún dominio — NULL** (0/7,306 puntos en la auditoría; **0/51,210 en la tela actual**, verificado). φ es campo escalar **postulado** (categórico por dominio, no medido). La sombra de cada caso es Π_θ(𝒞) con marco θ = (B, V, ρ, W, λ) declarado. El volumen opera en (m, τ). |

**Ventana del caso (primaria): dic 2024 → nov 2026** — la ventana del
backcast: τ=0 es dic 2024 (cruce Roche-R, R = 0.1021), τ=1 es el trigger
del 2 nov 2026. R observada dic 2024 → sep 2026 (21 puntos; mar 2026 sin
R); en τ=1, m se sostiene en el último R observado (0.2395, sep 2026) —
**convención, no dato**: los dos meses entre sep y nov 2026 no tienen R
y no se imputan. **Sensibilidad:** ventana observada completa
feb 2024 → sep 2026 (30 puntos), τ sobre la ventana observada — la receta
pura de la tela. Las dos se reportan; donde difieren, se dice.

**Guardas aplicadas:** b descriptiva, nunca prueba de mecanismo; b ≥ 1
banda no clasificada; malversación presunta/denunciada/investigada; 2 nov
2026 = reconocimiento/trigger, no inicio del fallo; Δ de ACO-A NO
estimable (sin serie A(τ)); u no se inventa; la figura no identifica el
dominio. Números de Ueno usados (v2, verificados): R oct 2024 0.0780, nov
0.0963, **dic 2024 0.1021 (cruce Roche-R)**; b ventana dic 2024–nov 2025:
extremo **0.383**, OLS **0.436 (R² = 0.873)**; Roche-C dic 2024 = **1.08**;
Roche-S 2 nov 2026 = **0.463**. NO se usan los números v1 (b 0.356, cruce
nov 2024) — retirados.

## 1. La forma de Ueno en el ACO-A

### 1.1 Criterio ACO: se cumple (v1/v2, sin cambio)

1. **Extinción funcional:** resolución BCP 2 nov 2026 (Ley 2334/03);
   congelamiento de activos y pasivos; imposibilidad de reponer el encaje
   legal USD 70M; solvencia 5.56%.
2. **Absorción identificable:** 7 bancos presentaron propuestas al IPS;
   receptores documentados (BNF, Itaú, GNB, Continental, Sudameris);
   proceso competitivo; balance de exclusión con plazo máximo de 15 días.

**Ueno sería el caso real 19 de la tela, y el primero en vivo**: los 18
ACO son colapsos históricos con serie (t, R) versionada; Ueno es un
colapso observado mientras ocurre, con serie real mensual (30 meses con
R). Es también el primer caso real del **dominio Finanzas** en la tela
(los 18 ACO son F/H/I/T: financiero-histórico, imperios, industria,
tecnología — ninguno es un banco en operación con balances mensuales).

### 1.2 La trayectoria en (τ, log₁₀ m) — figura 1

`ueno-acoa-trayectoria.png`: Ueno (rojo, grueso) frente a las 18
trayectorias ACO reales (gris) y su mediana (negro) con banda IQR, más la
banda de equilibrio m ∈ [0.56, 1.78] (verde).

| τ | log₁₀ m Ueno | m Ueno | log₁₀ m ACO mediana | Lectura |
|---|---|---|---|---|
| 0 (dic 2024) | −0.991 | 0.1021 | −0.292 | Ueno empieza 0.70 décadas por debajo de la mediana ACO |
| ~0.25 | −0.769 | 0.1701 | −0.060 | Sube; ACO ya está casi en 1 |
| ~0.5 | −0.634 | 0.2324 | −0.019 | Ueno se acerca a su techo |
| ~0.75 | −0.647 | 0.2253 | +0.003 | Meseta: deja de subir |
| 1 (trigger) | −0.621 | 0.2395 | +0.040 | Termina 0.66 décadas por debajo de la mediana ACO |

**La diferencia estructural: Ueno NO converge a m ≈ 1.** |log₁₀ m| de
Ueno: **0.991 → 0.621**; ACO mediana: **0.292 → 0.071**. Los colapsos
ACO mueren EN la banda de equilibrio (m ≈ 1: el nodo se iguala con el
hub; colapso = satelización completada). Ueno **nunca entra en la banda
de equilibrio** (m máx 0.267 < 0.56): sube por la estela suave
(0 < b < 1, satelización leve) y se estaciona por debajo de la cabeza.
El colapso de Ueno no es la llegada a m = 1: es el **reconocimiento
legal (Roche-S 0.463) mientras R está estancada en ~0.24**. La forma en
R(t) es subida + saturación, no llegada.

### 1.3 La diferencia es de normalización, no de forma — sensibilidad clave

El proxy de ACO es **m = masa absorbente / masa pico**: está normalizado
a su propio pico, así que termina en 1 **por construcción**. El proxy de
Ueno es **R = fondos en Ueno / resto del sistema**: una participación del
sistema, sin pico al que normalizar. Si se pone a Ueno en la misma
escala (m = R / R_max, sensibilidad — NO es el proxy declarado):

| | log₁₀ m τ=0 | τ=0.25 | τ=0.5 | τ=0.75 | τ=1 | \|log₁₀ m\| τ=0 → τ=1 |
|---|---|---|---|---|---|---|
| Ueno R/R_max | −0.416 | −0.194 | −0.059 | −0.072 | −0.046 | **0.416 → 0.045** |
| ACO mediana | −0.292 | −0.060 | −0.019 | +0.003 | +0.040 | 0.292 → 0.071 |

Normalizado, Ueno converge a m ≈ 1 igual que los ACO (0.045 vs 0.071 al
final), y su distancia al centroide ACO cae de **1.24 a 0.49** — el
mínimo del rango de los propios ACO ([0.49, 2.74], mediana 0.85), es
decir, tan cerca del centroide ACO como el caso ACO más cercano. **La
forma es ACO; el nivel es el proxy.** La lectura honesta es doble: con
el proxy declarado (participación del sistema), Ueno se queda por debajo
de la cabeza; con la normalización de ACO, su figura es indistinguible
de un colapso ACO. Ninguna de las dos es "la verdadera": son dos
proxies, y la diferencia entre ellos es el hallazgo.

### 1.4 Modo de colapso: el matiz que añade la tela

La clasificación v1 (descriptiva, juicio — no medición) es **Acantilado
Catastrófico con rasgos de Craquelado**. La tela la **matiza, no la
refuta ni la confirma** (sigue sin haber serie A(τ) para medir Δ):

- El **acantilado está en Roche-S, no en R(t)**: la solvencia reportada
  cae de 13.85% (sep 2026) a 5.56% (2 nov 2026) en ~1 mes tras la
  inspección del 31 oct. En R(t) no hay acantilado: hay subida y
  meseta.
- Los **rasgos de Craquelado** (quiebres por fricción) sí están en la
  forma: los 5 pasos de φ, las notificaciones de jun/jul 2026, el
  memorando Rivarola bajo reserva — la acumulación con quiebres antes
  del salto final.
- **Δ sigue NO estimable.** Sin serie temporal de absorción A(τ) no hay
  modo medido. La etiqueta queda descriptiva, como en v1.

### 1.5 El ángulo prospectivo: Ueno cae dentro de la ventana, fuera de la cohorte

La prueba prospectiva ACO-A es la **cohorte v2 de cripto**: 491 pares
vivos al corte 2026-09-30, 440 candidatos, ventana **2026-09-30 →
2027-09-30**, P1a ✓ / P2 ✓ / P3 inconcluso (backcast de la ventana
pasada). **Ueno NO pertenece a esa cohorte** (es un banco, no un par de
Binance) y **no puede confirmar ni refutar P1a/P2/P3**. Su resolución
(2 nov 2026) cae dentro del **calendario** de la ventana, pero fuera de
su cohorte y de su dominio. Eso es todo lo que se puede decir de la
prueba sobre Ueno — y es importante decirlo, porque confundir "cayó
dentro de la ventana" con "cuenta en la prueba" sería un error.

Lo que SÍ se transfiere de la ADENDA 5 como estándar metodológico, y
Ueno lo cumple: **sin imputación** (los 7 PDF MEF faltantes son huecos,
no se rellenan); **censura** (la absorción posterior a nov 2026 aún no
se observa: queda censurada, no asumida); **ausencia ≠ evento** (que
falte un PDF no es un colapso, como un delisting no es un colapso).
Ueno es un caso vivo observado durante la ventana prospectiva, fuera de
la cohorte — un recordatorio de que la prueba cubre solo su cohorte.

## 2. La firma cimática de Ueno

### 2.1 Procedimiento

El mismo de `tela_cimatica.py`, verbatim: log₁₀ m interpolado a la
retícula de 32 fases; FFT real de la trayectoria sin media; rasgos =
[log₁₀ m en τ=0/0.25/0.5/0.75/1] + [A1, A2, A3] (las 3 primeras
amplitudes FFT). Las fases se leen en los índices 0/8/16/23/31 de la
retícula (τ ≈ 0 / 0.258 / 0.516 / 0.742 / 1), como en el código.

### 2.2 La figura y los tonos — figura 2

`ueno-cimatica-tonos.png`: espectro FFT (armónicos 1–16) de Ueno frente
a las medianas por dominio.

| Armónico | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ueno (primaria) | **2.065** | **1.326** | 0.438 | 0.717 | 0.349 | 0.436 | 0.312 | 0.338 |
| ACO mediana | 1.377 | 0.893 | 0.661 | 0.556 | 0.463 | 0.378 | 0.312 | 0.275 |
| Ueno (sensibilidad) | 5.926 | 2.298 | 2.139 | 1.131 | 0.852 | 0.696 | 0.678 | 0.683 |

| Armónico | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|
| Ueno (primaria) | 0.178 | 0.208 | 0.236 | 0.215 | 0.219 | 0.200 | 0.162 | 0.208 |
| ACO mediana | 0.254 | 0.239 | 0.229 | 0.216 | 0.206 | 0.201 | 0.199 | 0.198 |

**Lectura:** A1 domina (subida monótona: el fundamental es la deriva).
A2 es el segundo componente (la curvatura subida-meseta). Hay un
**bulto secundario en A4 (0.717 > A3 0.438)**: la forma
subida-luego-plano tiene contenido en el armónico 4 — es la firma de la
saturación, no del ruido (los armónicos 9–16 quedan planos en ~0.2,
como en ACO). En la ventana de sensibilidad (feb 2024 → sep 2026) A1
salta a 5.93: la subida desde los R bajos de principios de 2024 (0.028)
es el fundamental más fuerte; la figura depende de la ventana, como b
depende del reloj. **No se afirma que el espectro identifique el
dominio**: se reporta la firma, medida.

### 2.3 La huella de Ueno

`ueno-huella-cimatica.csv` — mismo formato que
`reconstruction_real/data/tela_cimatica_huellas.csv`:

| | log₁₀ m τ=0 | τ=0.25 | τ=0.5 | τ=0.75 | τ=1 | log₁₀ m máx | A1 | A2 | A3 |
|---|---|---|---|---|---|---|---|---|---|
| **Ueno (primaria, dic 2024 → nov 2026)** | −0.9910 | −0.7693 | −0.6338 | −0.6471 | −0.6207 | −0.5752 | 2.0653 | 1.3255 | 0.4377 |
| Ueno (sensibilidad, feb 2024 → sep 2026) | −1.5467 | −1.1079 | −0.7680 | −0.6712 | −0.6207 | −0.5735 | 5.9262 | 2.2975 | 2.1394 |
| ACO mediana (18, publicada) | −0.2917 | −0.0600 | −0.0186 | +0.0032 | +0.0402 | +0.0402 | 1.3772 | 0.8930 | 0.6613 |

Comparación directa: la huella de Ueno está **desplazada hacia abajo
~0.6–0.7 décadas** respecto a la mediana ACO en todas las fases (el
nivel del proxy, §1.3), pero con la **misma forma**: subida fuerte en
la primera mitad, plana en la segunda (τ=0.5 → τ=1: −0.634 → −0.621,
casi horizontal). El m máx de Ueno (0.266) es el R de oct 2025 (0.2670).

### 2.4 La prueba leave-one-out, reproducida sobre la tela actual

Se corrió `clasificacion_loo` verbatim sobre la tela actual
(`tela_de_incertidumbre.csv`: 51,210 puntos, **740 casos** — 699 series
reales + 41 sombras). Las huellas medianas por dominio **reproducen
exactas** las publicadas (diferencia 0.0000 en los 12 dominios), así
que los datos son los mismos; lo que cambió respecto a la auditoría es
la composición de la tela (ver abajo).

| Prueba | Tela actual (740 casos) | Auditoría (tela anterior) | README Módulo 2 |
|---|---|---|---|
| Por dominio, todos los rasgos | **50.7%** (374/737) | 21.2% (156/737) | **50.7%** |
| Por dominio, solo-forma | 41.9% | 19.8% | — |
| Por tono φ, todos los rasgos | **66.2%** (490/740) | 53.7% | **66.2%** |
| Por tono φ, solo-forma | 58.6% | 43.7% | — |

**Por qué cambió el número:** la tela de la auditoría tenía 7,306
puntos (18 series reales + 721 sombras del modelo R = t^b, cuya forma
está determinada por (b, n)); la tela actual tiene 51,210 puntos (699
series reales de la capa exógena + 41 sombras). Con series reales, la
figura separa mejor los dominios — y el README Módulo 2 ya reporta
50.7% / 66.2%: **mi reproducción coincide exacta con el README**. La
prosa de la auditoría dice "739 casos"; sus propios conteos por dominio
suman 740, igual que la tela actual — discrepancia de un caso en la
prosa, no en los datos.

**El veredicto se mantiene en sustancia, con el número actualizado:**
la figura **no identifica el dominio de forma fiable** — la mitad de
los casos se clasifica mal (50.7%), y ACO mismo solo acierta 4/18 en
la tela actual (antes 13/18). Ese 13/18 era en parte un artefacto: en
la tela anterior solo los ACO eran series reales y empezaban por debajo
de m=1, mientras las 721 sombras empezaban exactamente en 1 — el rasgo
τ=0 separaba ACO por construcción, no por forma. Con series reales en
B y E3, ACO ya no se distingue por τ=0 solo. El tono φ se identifica
mejor (66.2%), parcial como decía la auditoría: `nula` 230/241 (95%),
`alta` 248/472 (53%), `variable` (ACO) 7/18 (39%), `fisica` 1/5. La
figura revela el régimen de fricción, no la etiqueta del instrumento —
eso no cambió.

### 2.5 Asignación de Ueno como caso nuevo (centroide cercano)

Ueno no pertenece a ningún dominio del repo (Finanzas no existe en los
11 dominios), así que no se "clasifica": se mide **a qué centroide se
parece**, con la misma estandarización que la prueba LOO. Resultado:
**ACO en dominio y `variable` en tono, en las 4 configuraciones**
(ventana primaria y sensibilidad × todos los rasgos y solo-forma).

| Configuración | Distancias a centroides (menor = más cercano) | Predicho |
|---|---|---|
| Primaria, por dominio, todos | **ACO 1.24** · E2 1.46 · C 1.49 · A 1.51 · B 1.54 · F1 3.96 · E3 6.23 · D 7.89 · E1 11.80 | **ACO** |
| Primaria, por dominio, solo-forma | **ACO 1.08** · E2 1.12 · B 1.14 · C 1.15 · A 1.18 · F1 3.85 · E3 5.40 · D 7.84 · E1 11.76 | **ACO** |
| Primaria, por tono, todos | **variable 1.24** · media 1.51 · alta 1.54 · fisica 3.43 · nula 6.20 | **variable** |
| Primaria, por tono, solo-forma | **variable 1.08** · alta 1.14 · media 1.18 · fisica 3.31 · nula 5.40 | **variable** |
| Sensibilidad, por dominio, todos | **ACO 2.05** · E2 2.35 · B 2.49 · C 2.55 · F1 2.90 · A 2.90 · E3 6.35 · D 6.69 · E1 10.82 | **ACO** |
| Sensibilidad, por tono, todos | **variable 2.05** · alta 2.49 · fisica 2.56 · media 2.90 · nula 6.27 | **variable** |

**Lectura honesta de los márgenes:** ACO es el más cercano en las 4,
pero el margen es **delgado**, sobre todo en solo-forma (1.08 frente a
1.12 de E2 y 1.14 de B). La asignación es **sugestiva, no decisiva**:
la figura de Ueno se parece a un colapso ACO más que a cualquier otro
centroide, sin que eso identifique su dominio (que no existe en el
repo) ni pruebe mecanismo. Dentro del rango ACO: la distancia de Ueno
al centroide ACO (1.24) está dentro del rango de los 18 ACO reales
([0.49, 2.74], mediana 0.85); 4 de los 18 ACO están más lejos de su
propio centroide que Ueno. Normalizado a R/R_max (§1.3), la distancia
cae a **0.49** — el mínimo del rango ACO. La forma es ACO; el margen
depende del proxy.

## 3. La tendencia en la tela de incertidumbre

### 3.1 El camino de Ueno en el plano (m, τ) — figura 3

`ueno-tela-incertidumbre-tendencia.png`: R(t) observado dic 2024 →
sep 2026 sobre τ, con el ajuste de ventana y su banda empírica, y el
trigger en τ=1.

Marco θ declarado (Axioma 0.2): **B = (m, τ)**; **V = R crudo**
(serie real mensual, no sombra del modelo); **ρ = 1 punto por dato**;
**W = ventana dic 2024 → nov 2026**; **λ = sin corte**. **u = NULL**
(0/51,210 puntos definidos en la tela actual — verificado).

| Fase | τ | m = R(t) | Régimen (v2) |
|---|---|---|---|
| dic 2024 | 0 | 0.1021 | Cruce Roche-R; inicio de la ventana |
| ene–jun 2025 | 0.04–0.30 | 0.1094 → 0.1706 | Subida (ajuste b = 0.436) |
| jul–nov 2025 | 0.30–0.48 | 0.2079 → 0.2643 | Subida; R máx 0.2670 (oct 2025) |
| dic 2025–sep 2026 | 0.52–0.91 | 0.2280 → 0.2395 | **Meseta** (b ≈ +0.01–0.03, R² ≈ 0.01) |
| 2 nov 2026 | 1 | 0.2395 (sostenido) | Trigger / reconocimiento; R termina |

**La tendencia es saturación, no aceleración.** La subida se detiene
en nov 2025 y R se queda en ~0.21–0.25 durante 2026: el hub tocó techo
(IPS en 9.70% de su cartera, tope 10%, sin nuevas colocaciones en
2026). El trigger no llega en el pico de la subida: llega **un año
después de que la subida se detuvo**, por inspección y provisiones.
Eso es lo que la tela muestra: el camino sube, se aplana, y el evento
ocurre en la meseta.

### 3.2 La incertidumbre es empírica — no hay banda de la teoría

- **Banda del ajuste (ventana dic 2024–nov 2025):** OLS re-verificado
  aquí: a = 0.0829, **b = 0.436, R² = 0.873, n = 12** (idéntico a v2).
  Desviación típica de los residuos en log: **0.132 → ±14.1% en R**
  (±1 sd). Esa es la banda dibujada en la figura 3: es la dispersión
  de los residuos, no un intervalo de confianza teórico.
- **Meseta:** sd residual (log) 0.057 (±5.9%), b = +0.009 (origen
  local, n=9) — coincide con v2 (c').
- **Sensibilidad al tipo de cambio:** R nov 2024 es 0.0963 a FX 6,000
  y 0.0965 a FX 7,793 — **0.0002**, despreciable frente al ±14.1% de
  los residuos. El FX no mueve la tendencia.
- **u = NULL.** No hay banda de confianza sacada de la teoría, porque
  el eje u no tiene definición operativa en ningún dominio y φ es
  postulada, no medida. La incertidumbre que se muestra es la medida
  (residuos + sensibilidad FX + huecos registrados), no la del cubo.

### 3.3 Hacia adelante: la dirección del forecast

**R(t) de Ueno termina en τ=1.** El hub muere; ya no hay balance de
Ueno que medir. La tendencia hacia adelante no es una prolongación de
R(t): es la **redistribución** — los fondos públicos salen de Ueno y
entran en los 7 bancos receptores, el FGD paga (primer pago 17 nov,
hasta Gs 10M; tope Gs 228.3M por depositante), el balance de exclusión
cierra en 15 días, el embargo (Gs 2.1005 billones) se ejecuta y el
proceso penal avanza. La dirección es: **de un hub a siete receptores**,
con la masa de fondos conservada y repartida — no con R(t) siguiendo
su curva.

**Lo que el forecast refinará** (aún no está; se marca aquí, no se
adivina): la R(t) posterior de los receptores (¿alguno de los 7 muestra
un salto en su participación de fondos públicos?); la línea de tiempo
de la absorción A(τ) y su Δ (hoy no estimable: faltan los montos por
receptor y por fecha); y la recuperación del ASI (¿cuándo vuelven los
jubilados/ahorristas/OEEs a cumplir las 5 condiciones? hoy 0/5, 0/4,
0/5). Nada de eso se proyecta aquí con banda: la tela da la dirección
(redistribución), no el número.

## 4. Limitaciones y huecos (registrados, no rellenados)

1. **u = NULL** en todos los dominios (0/51,210 puntos). El cubo opera
   en (m, τ). No se inventa definición operativa para u.
2. **φ postulada, no medida** (categórica por dominio). La asignación
   de Ueno a `variable` es por parecido de figura, no una medición de
   fricción. Calibrar φ por caso (no por dominio) es el paso siguiente
   natural que la propia auditoría señala.
3. **Δ de ACO-A no estimable** (sin serie A(τ)). El modo de colapso
   queda descriptivo.
4. **La figura no identifica el dominio** (LOO 50.7% en la tela actual;
   ACO 4/18). La asignación ACO de Ueno es por cercanía con margen
   delgado, no una identificación.
5. **La ventana manda en la figura:** la huella cambia con la ventana
   (A1 2.07 primaria vs 5.93 sensibilidad). Como b, la firma lleva su
   ventana declarada.
6. **Mar 2026 sin R; 7 PDF MEF faltantes** (2023-01–05, 2024-08,
   2026-03). La interpolación a la retícula de 32 fases une dic 2025–
   ene 2026 y feb–abr 2026 por encima del hueco de mar 2026 — el hueco
   no se imputa, pero la interpolación lo cruza; la huella en τ≈0.6
   depende de esa interpolación lineal.
7. **τ=1 es el trigger con m sostenido**, no una observación. Los dos
   meses sep→nov 2026 no tienen R.
8. **La comparación de nivel con ACO depende del proxy** (§1.3). Con el
   proxy declarado Ueno queda bajo la cabeza; normalizado a su pico,
   converge a 1 como los ACO. Las dos lecturas están en el informe.
9. **La prueba prospectiva no cubre a Ueno** (§1.5). No se usa para
   validar ni refutar nada de este caso.
10. **La prosa de la auditoría cimática dice 739 casos**; sus conteos
    por dominio suman 740. Discrepancia de un caso en la prosa, no en
    los datos (las huellas reproducen exactas).

## 5. Reproducibilidad

- **Script:** `/tmp/ueno_tela.py` — funciones `trayectorias`,
  `espectro`, `rasgos`, `clasificacion_loo` copiadas verbatim de
  `reconstruction_real/code/tela_cimatica.py`; definiciones de
  `tela_de_incertidumbre.py`. Log completo en `/tmp/ueno_tela_log3.txt`.
- **Verificaciones hechas en esta corrida:** OLS ventana dic 2024–nov
  2025 reproduce b = 0.436, R² = 0.873 (v2); huellas medianas por
  dominio reproducen exactas las publicadas (12/12, diferencia 0.0000);
  LOO sobre la tela actual reproduce el README Módulo 2 (50.7% dominio,
  66.2% tono).
- **Salidas:**
  - `ueno-acoa-tela-cimatica-incertidumbre.md` (este informe)
  - `ueno-huella-cimatica.csv` (huella de Ueno, 2 filas: ventana
    primaria + sensibilidad, mismo formato que
    `tela_cimatica_huellas.csv`)
  - `ueno-acoa-trayectoria.png` (figura 1)
  - `ueno-cimatica-tonos.png` (figura 2)
  - `ueno-tela-incertidumbre-tendencia.png` (figura 3)
- **Fuentes:** `snt-repo` (HEAD a3cd14c): `reconstruction_real/audits/
  TELA_CIMATICA_2026-10-21.md`, `TELA_DE_INCERTIDUMBRE_2026-10-21.md`,
  `BACKCAST_PROSPECTIVA_2026-10-26.md`,
  `preregistro/ADENDA5_PROSPECTIVA_DELISTADOS_Y_HASH_2026-10-27.md`,
  `README.md` (Módulos 1–2), `code/tela_cimatica.py`,
  `code/tela_de_incertidumbre.py`, `data/tela_de_incertidumbre.csv`
  (51,210 puntos, 740 casos), `data/tela_cimatica_huellas.csv`,
  `data/snt_corpus_aco_timeseries_v29.csv` (18 casos). Ueno:
  `tabla-maestra-ueno-mef.csv` (corregida),
  `modelo-ueno-resultados-v2.md`, `modelo-ueno-resultados.md` (§§7–9:
  ASI, ACO-A, muro).
