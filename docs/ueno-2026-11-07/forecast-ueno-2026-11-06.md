# COPIA DE REGISTRO — Ueno v3 (corrección 2026-11-09)
# Archivo original: docs/ueno-2026-11-07/forecast-ueno-2026-11-06.md
# Versión: sin número de versión declarado; punto de partida v2
# Estado: archivo de registro — SIN CAMBIOS respecto al original. Cuerpo intacto; solo se añadió esta cabecera.
# Fecha de la copia: 2026-11-09
# md5 original: d1260013838662e8b7309b43dcc7510a
# sha256 original: af753b3717af9cf8c8a93fb4c8a56f6b50faace16da74351e87e992f4a166fca
#
# Forecast — caso Ueno Bank: qué va a pasar desde el 2 nov 2026

**Fecha:** 2026-11-06/07. **Punto de partida:** `modelo-ueno-resultados-v2.md` (backcast v2, verificado) + `ueno-acoa-tela-cimatica-incertidumbre.md` (forma y tendencia en la tela) + parteaguas v2. **Método:** escenarios con sus condiciones, no predicciones. Cada escenario lleva su etiqueta: **documentado** (fecha/monto en fuente), **proyección** (depende de una condición declarada) o **hueco** (no se puede fechar ni cuantificar con los datos disponibles). **Script:** `/tmp/forecast_ueno.py` + `/tmp/forecast_csv.py` (stdlib; saldos por banco del MEF Informe de Bancos sep 2026, cifras preliminares). **Valores:** `forecast-ueno-valores.csv` (md5 `cce53a6cbdbe53e425779633743958af`).

## Guardas

- **Malversación presunta, denunciada e investigada** (denuncia MEF 5 nov 2026; imputación a 27 personas 4 nov 2026), no sentenciada. El trigger oficial fue insuficiencia de solvencia.
- **El 2 nov 2026 es reconocimiento/trigger, no inicio del fallo.** El forecast arranca ahí.
- **Estimaciones marcadas ESTIMADO.** Lo no calculable se marca como **hueco**, nunca se rellena.
- **Leapfrog NO redefinido**: sigue siendo el salto por b < 0 al Nivel Exógeno (README Módulo 0). El muro en reversa (§7.2) es una pregunta, no una redefinición.
- **u sigue NULL** (tela de incertidumbre: el eje u no tiene definición operativa en ningún dominio). La incertidumbre se muestra con lo empírico: residuos del ajuste (±14,1% en R, 1 sd en log), sensibilidad al FX (0,0002) y huecos registrados.
- **R(t) de Ueno termina en τ=1.** El hub muere; ya no hay balance de Ueno que medir. La tendencia hacia adelante no es una prolongación de R(t): es la **redistribución** (tela §3.3).
- No se usan los números v1 retirados (b 0,356; cruce nov 2024).

## 0. Punto de partida (v2, verificado)

| Magnitud | Valor |
|---|---|
| R(t) sep 2026 (último observable) | **0,2395** (Ueno USD 834,8M equiv; sistema USD 4.320,4M equiv) |
| b ventana dic 2024–nov 2025 | extremo **0,383** / OLS **0,436** (R² = 0,873, n=12) |
| Meseta dic 2025–sep 2026 | b ≈ **+0,031** (R² = 0,011) — sin tendencia medible |
| Roche-R | cruce **dic 2024** (0,1021) |
| Roche-C | **1,08** dic 2024 · **1,89** dic 2025 · **≈2,08** mar 2026 (fondos totales) |
| Roche-S | **0,463** el 2 nov 2026 (5,56% / 12%) |
| ASI | jubilados **0/5**, ahorristas **0/4** (+1 sin datos), OEEs **0/5** |
| Muro | **5 negativos / 0 positivos** |
| Tendencia en la tela | **Saturación, no aceleración.** La subida se detuvo en nov 2025; el trigger llega un año después, en la meseta. |

## 1. Pagos del FGD — calendario documentado y escala

### 1.1 Calendario (documentado)

| Fecha | Hito | Fuente |
|---|---|---|
| 2 nov 2026 | Resolución BCP; se dispara la garantía | BCP / parteaguas v2 §1.4 |
| **5 nov 2026** | Límite de las 72 h para el anticipo (Ley 7745/2026) | 2 nov + 72 h (cálculo) |
| **17 nov 2026** | **Primer pago a jubilados** (32.000 a reasignar) | Parteaguas v2 §3.2 [8] |
| **17 nov 2026** | **Plazo máximo del balance de exclusión** (15 días) | 2 nov + 15 días; parteaguas v2 §9.1 [7] |

Las dos fechas del 17 nov son independientes y caen el mismo día: el primer pago a jubilados y el cierre del balance de exclusión. Eso hace del 17 nov el primer hito observable del forecast: si el balance no cierra ese día, la absorción se retrasa; si cierra, la A(τ) empieza a medirse.

### 1.2 Escala (documentado)

| Magnitud | Valor |
|---|---|
| Tope por depositante | **Gs 228.300.000** (75 SM; SM implícito Gs 3.044.000) — Ley 2334/03 |
| Tope en USD equiv | **USD 38.050** (a FX 6.000) |
| Anticipo máximo | **Gs 10.000.000** (USD 1.667) = **4,38% del tope**, en 72 h — Ley 7745/2026 |
| Tope / exposición del IPS (Gs 2,03 billones) | **0,011%** |
| Tope / fondos de Ueno en sep 2026 (Gs 5,009 billones, CSV) | **0,0046%** |
| Tope / fondos de Ueno en sep 2026 (Gs 5,13 billones, ABC) | **0,0045%** |

**Lectura:** el FGD cubre al ahorrista minorista hasta su tope, pero es cinco órdenes de magnitud menor que la exposición institucional. El FGD no es el mecanismo que resuelve el caso: es el mecanismo que paga al pequeño mientras el resto se resuelve por exclusión y compensación. Esa es la misma lectura de v2 (§11.5): una absorción ordenada puede dejar ASI bajo.

### 1.3 Lo que NO se puede calcular (huecos)

- **Monto total que pagará el FGD: hueco.** Requiere el número de depositantes de Ueno y la distribución de sus saldos — ninguno está documentado en las fuentes. Sin eso no hay total, solo tope por persona.
- **Recursos totales del FGD: hueco.** El fondo total no está documentado. El comparador es Banco Master (Brasil, 2025): el FGC pagó R$ 41.000M y el Banco Central endureció los criterios después (parteaguas v2 §6). Si el FGD paraguayo se agota, el pago se escalona más allá del calendario — es el riesgo principal del calendario, y no es cuantificable hoy.
- **Haberes mensuales de los 32.000 jubilados: hueco.** Sin el total mensual no se puede calcular cuánto mueve la reasignación por mes.
- **Los depósitos de OEE/IPS ¿entran al FGD?** La evaluación documental de v2 (§7) los pone en recuperación **vía proceso de exclusión**, no vía FGD. El FGD protege depósitos; la exposición del IPS es mayoritariamente CDA. La cobertura exacta de cada instrumento es una cuestión legal — **hueco**, no se afirma aquí.

**Escenario 1 (condición: el FGD tiene recursos y el balance cierra el 17 nov).** Anticipo en 72 h, primer pago a jubilados el 17 nov, pagos escalonados hasta el tope por depositante. La condición es el balance de exclusión: sin él no hay lista de saldos que pagar. **Escenario 1b (condición: el balance se retrasa o el FGD se tensiona).** Los pagos se escalonan más allá del 17 nov y el anticipo de Gs 10M se vuelve el único cobro inmediato para muchos. El indicador para distinguirlos es público: si el 17 nov hay primer pago, es el escenario 1; si no, es el 1b.

## 2. Absorción — el cierre del ACO-A

### 2.1 Estado al 2 nov 2026 (documentado)

- **Criterio ACO-A cumplido** (v2 §8): extinción funcional (resolución 2 nov, solvencia 5,56%) + absorción identificable (7 bancos presentaron propuestas al IPS; receptores documentados: **BNF, Itaú, GNB, Continental, Sudameris** — 5 nombrados; **los otros 2 oferentes no están nombrados en las fuentes: hueco**).
- **Balance de exclusión: plazo máximo 15 días** (17 nov 2026). 120 funcionarios del BCP desplegados a sucursales para conciliar activos y pasivos.
- **Δ NO estimable** (v2 §8): no hay serie A(τ) para Ueno. La serie A(τ) **empieza ahora**: los montos por receptor y por fecha, cuando se publiquen, son el primer dato de la absorción. Hasta entonces la absorción está **censurada** (estándar ADENDA 5: seguimiento incompleto = censura a la derecha, no evento ni no-evento).
- **Modo:** Acantilado Catastrófico con rasgos de Craquelado (descriptivo). La tela lo matiza: el acantilado está en Roche-S (13,85% → 5,56% en ~1 mes), no en R(t) (subida + meseta).

### 2.2 Base de la redistribución: saldos OEE por banco, sep 2026 (MEF PDF, cifras preliminares)

Total del sistema: **USD 4.320.353.015 equiv** (USD 1.021.087.504 + Gs 19.795.593.071.022 / 6.000). Ueno: **USD 834.825.625 equiv** (19,32% del sistema; R = 0,2395 — reproduce el CSV exacto).

| Banco | Total USD equiv | Participación | R_X = X / (sistema − X) |
|---|---|---|---|
| BNF | 1.169.674.306 | 27,07% | **0,3712** |
| Ueno | 834.825.625 | 19,32% | **0,2395** |
| Continental | 714.868.006 | 16,55% | **0,1983** |
| Itaú | 368.916.236 | 8,54% | **0,0934** |
| Sudameris | 278.324.243 | 6,44% | **0,0689** |
| BASA | 265.749.393 | 6,15% | 0,0655 |
| ZETA | 170.491.507 | 3,95% | 0,0411 |
| BANCOP | 126.274.474 | 2,92% | 0,0301 |
| Citibank | 106.825.814 | 2,47% | 0,0254 |
| GNB | 87.681.024 | 2,03% | **0,0207** |
| Interfisa | 75.365.667 | 1,74% | 0,0178 |
| Familiar | 65.503.727 | 1,52% | 0,0154 |
| Atlas | 46.950.431 | 1,09% | 0,0110 |
| Solar | 6.353.349 | 0,15% | 0,0015 |
| Nación Arg. | 2.414.859 | 0,06% | 0,0006 |
| Do Brasil | 134.353 | 0,00% | 0,0000 |

**Dos lecturas previas a los escenarios.** Primera: **BNF (0,3712) y Continental (0,1983) ya están por encima de 0,10** — el umbral Roche-R no es una línea de peligro absoluta que se transfiera mecánicamente a otros bancos: BNF es el banco estatal y su participación alta es estructural. Lo que el umbral marca en Ueno es la **deriva** (b > 0 sostenida), no el nivel. Segunda: los fondos de Ueno son **19,32% del sistema** — la masa que se redistribuye es casi un quinto de los fondos públicos del sistema.

### 2.3 Escenarios de redistribución (proyección)

**Supuesto común (declarado):** los fondos públicos se conservan dentro del sistema (no hay salida neta) y el total del sistema se mantiene en USD 4.320,4M equiv. Los escenarios reparten los USD 834,8M equiv de Ueno entre receptores. La corriente IPS (Gs 2,03 billones, 41,7% de Ueno) y la corriente OEE/Tesoro (resto) pueden repartirse distinto — el reparto del total como bloque es una aproximación de primer orden, no una medición. Los escenarios se distinguen cuando se publique el reparto real (balance de exclusión + MEF oct/nov 2026).

**Escenario A — reparto igual entre los 7 oferentes** (cada uno recibe USD 119,3M equiv). Condición: el proceso competitivo divide por igual.

| Receptor | R antes | R después | Participación después |
|---|---|---|---|
| BNF | 0,3712 | **0,4252** | 29,83% |
| Continental | 0,1983 | **0,2393** | 19,31% |
| Itaú | 0,0934 | **0,1274** | 11,30% |
| Sudameris | 0,0689 | **0,1014** | 9,20% |
| GNB | 0,0207 | **0,0503** | 4,79% |

**Escenario A5 — reparto igual entre los 5 nombrados** (cada uno USD 167,0M equiv). Sensibilidad si los 2 oferentes no nombrados no reciben fondos públicos.

| Receptor | R antes | R después | Participación después |
|---|---|---|---|
| BNF | 0,3712 | **0,4480** | 30,94% |
| Continental | 0,1983 | **0,2565** | 20,41% |
| Itaú | 0,0934 | **0,1416** | 12,40% |
| Sudameris | 0,0689 | **0,1149** | 10,31% |
| GNB | 0,0207 | **0,0626** | 5,89% |

**Escenario B — proporcional a la participación actual entre los 5 nombrados.** Condición: el reparto sigue la capacidad instalada (el más grande absorbe más).

| Receptor | Peso | Recibe (USD equiv) | R después | Participación después |
|---|---|---|---|---|
| BNF | 44,65% | 372.776.321 | **0,5553** | 35,70% |
| Continental | 27,29% | 227.829.118 | **0,2791** | 21,82% |
| Itaú | 14,08% | 117.573.958 | **0,1269** | 11,26% |
| Sudameris | 10,63% | 88.702.203 | **0,0928** | 8,50% |
| GNB | 3,35% | 27.944.026 | **0,0275** | 2,68% |

**Escenario C — un solo receptor toma todo (el "nuevo hub").** Condición: falla la división competitiva.

| Receptor | R después | Participación después |
|---|---|---|
| BNF toma todo | **0,8656** | 46,40% |
| Continental toma todo | **0,5593** | 35,87% |

**Lectura de los escenarios.** En **todos** los escenarios BNF queda como el mayor receptor de fondos públicos del sistema (29,8%–46,4%). En el escenario B su R llega a 0,5553; en el C a 0,8656 con 46,4% del sistema — eso es un nuevo hub por absorción, exactamente lo que ACO-A debe evitar (parteaguas v2 §9.2). El escenario A es el que más dispersa (máximo 29,8%). **Sudameris cruza 0,10 en los escenarios A (0,1014) y A5 (0,1149)** — pero el cruce es marginal: está dentro de la banda de incertidumbre empírica (±14,1% en R) y de la sensibilidad al FX, así que se registra como **cruce marginal, no como entrada firme a Roche-R**. Itaú cruza 0,10 en A, A5 y B (0,127–0,142) — cruce más sólido, pero Itaú es un banco grande con solvencia AAApy: el nivel no es la deriva. **La vigilancia no es el nivel, es la deriva:** si en los MEF de oct–dic 2026 algún receptor muestra b > 0 sostenido en su R_X, esa es la señal de un nuevo drift, no el salto de un mes por absorción.

**Escenario D — reparto aleatorio/competitivo por tipo de cuenta (propuesta del parteaguas).** No calculable: requiere datos por cuenta (tipo de depositante e instrumento), que no están publicados. Es la propuesta de Fassil (1.200.000 cuentas y 90.000 préstamos a 9 bancos con selección aleatoria) adaptada a Ueno — pero en Ueno la selección no puede ser aleatoria pura porque jubilados y fondos públicos tienen requisitos operativos distintos (parteaguas v2 §9.3).

### 2.4 Qué observar para saber en qué escenario estamos

- **MEF Informe de Bancos oct 2026** (cuando se publique): primer saldo post-resolución por banco. Si Ueno sigue con saldo (congelado pero reportado), la R(t) de Ueno tiene una cola; si desaparece, R(t) termina en sep 2026.
- **MEF nov–dic 2026:** la R_X de cada receptor. Un salto de un mes = absorción; una subida sostenida de 3+ meses = deriva.
- **Balance de exclusión (17 nov):** qué activos se declaran realizables y cuáles no. Las megacuentas (177,5% del patrimonio neto) son el cuello de botella de la valuación.

## 3. Activos — embargo, fideicomiso y salvadoras

### 3.1 Embargo (documentado, 3 nov 2026)

| Componente | Monto |
|---|---|
| USD | USD 70.000.000 |
| Gs | Gs 1.621.853.458.972 |
| Costas | Gs 58.639.000.000 |
| **Total Gs equiv (a FX 6.000)** | **Gs 2,1005 billones** (USD 350,1M equiv) |
| vs Derechos Fiduciarios (Gs 2,1057 billones) | **−0,25%** — coincidencia numérica, registrada como tal (v2 §8) |
| vs exposición del IPS (USD 348,5M) | **+0,45%** (350,08M / 348,5M) — otra coincidencia numérica, registrada como tal |

Contra: U Paraguay S.A., U Holdings S.A.R.L., Grupo Vázquez S.A.E., Federico Miguel Vázquez Villasanti, Juan Manuel Gustale, Diana Leticia Mongelós González y cuatro directores. Juzgado en lo Civil y Comercial del Octavo Turno, a solicitud del BCP.

**Proyección:** el embargo congela, no cobra. La recuperación depende de la realización de los bienes embargados — su valuación y su liquidez **no están documentadas (hueco)**. Los Derechos Fiduciarios (Gs 2,1057 billones, 99,44% del patrimonio neto) son el activo más grande y el menos líquido: un fideicomiso de gastos de fusión activados, no un activo realizable en mercado. Si el balance de exclusión los clasifica como no realizables, el embargo cubre en papel más de lo que se recupera en efectivo. **El monto embargado no es el monto recuperable** — confundirlos sería el error simétrico al de confundir la solvencia reportada con la real.

### 3.2 Salvadoras y vinculadas (documentado)

- **Deudas de las salvadoras:** Gs 905.825M ≈ **USD 151,0M** (a FX 6.000; el documento dice USD 153M a otro tipo de cambio) = 35% del patrimonio efectivo → PE implícito Gs 2,588 billones (+4,9% sobre el ancla abr 2026 — tensión reducida, no resuelta, v2 §8).
- **USD 146M a vinculadas** (Mowi, Grupo Hendy, Grupo M, sep 2025–may 2026): **39,8%** del PE cierre 2025 y **35,5%** del PE abr 2026 — ≈1,8–2× el tope del 20%.
- **Circuito 29 abr 2026** (Sagas → Kasas → Vinanzas → Itti → Grupo M): la circularidad ya ocurrió; lo que queda es la deuda.

**Proyección:** las salvadoras deben a Ueno, y Ueno ya no existe como acreedor operativo — sus créditos pasan al proceso de exclusión/compensación. La recuperación de esos Gs 905.825M depende de la capacidad de pago de firmas cuya deuda con Ueno es 800–3.000× su deuda con el resto del sistema (Sagas 3.000×, Kasas 800×). **Condición:** si las salvadoras no tienen activos realizables fuera de Ueno, esa cartera se provisiona como pérdida y el hueco lo absorbe el FGD (hasta su tope), la compensación entre activos y pasivos, o el fisco. **El monto en riesgo no es cuantificable sin la valuación del balance de exclusión (hueco).**

### 3.3 Megacuentas (documentado)

Derechos Fiduciarios Gs 2,1057 billones + Intangibles Gs 761.444M + Participación en otras sociedades Gs 891.586M = **Gs 3,7588 billones (177,5% del patrimonio neto)**. La Participación subió +8.000% en 2025 (Red Digital de Procesamientos Gs 640.468M; Red Digital Gs 236.231M). **Proyección:** estas tres cuentas son el núcleo no realizable del balance. El balance de exclusión las separará; lo que se transfiera a los receptores será el resto. **Si el resto no cubre los pasivos transferidos, la diferencia es el costo fiscal de la resolución — no documentado, no estimable hoy (hueco).**

## 4. Proceso legal — línea de tiempo documentada y huecos

| Fecha | Hecho | Estado |
|---|---|---|
| 3 nov 2026 | Detención de 8 directivos | Documentado |
| 3 nov 2026 | Embargo preventivo | Documentado |
| 4 nov 2026 | Imputación a 27 personas (lesión de confianza, tentativa de estafa, violación de llevar libros de comercio, conducta indebida en situaciones de crisis) | Documentado |
| 5 nov 2026 | Denuncia penal del MEF: presunta malversación de **Gs 250.000M** de la Caja Fiscal + **Gs 123.838M** en intereses (depositados jul 2025) | Documentado; presunta, no sentenciada |
| Sin fecha documentada | **Nota BCP/P N.° 019**: el directorio del BCP entregó la denuncia a Fiscalía con un informe de ~200 fojas | **Hueco** (existe; fecha no documentada en las fuentes) |
| Sin fecha documentada | **Informe sellado de 31 fojas al Senado** (respuesta a cinco pedidos de informes) que **NO precisa la fecha ni el monto total del exceso** en el límite de préstamos vinculados | **Hueco** (existe; fecha no documentada) |
| — | Audiencias, formalización, juicio, sentencia, montos recuperados | **Hueco** — no se inventan fechas ni desenlaces |

**Proyección:** el proceso penal avanza en tres carriles separados: (a) la imputación a 27 personas por los delitos de gestión (4 nov); (b) la denuncia del MEF por presunta malversación de la Caja Fiscal (5 nov); (c) la denuncia del BCP vía Nota 019 con el informe de ~200 fojas. **Condición:** el avance depende de la Fiscalía y del juzgado, no del calendario financiero. El único hito fechable hoy es hacia atrás: la denuncia dice que los Gs 250.000M se depositaron en **jul 2025**, cuando la entidad presentaba una situación patrimonial que luego resultó sustancialmente distinta — ese es el ancla temporal de la denuncia, no una fecha de delito probado.

**Advertencia sobre el Informe 016:** el backcast v2 (§12) registra que aunque apareciera el Informe BCP/P N.° 016, es posible que tampoco fechara la malversación — el informe de 31 fojas al Senado no precisa fecha ni monto del exceso. El forecast no depende del 016: el inicio del delito sigue sin fecha en todos los escenarios.

## 5. Cadena política (documentado, sin desenlace)

Documentado (parteaguas v2 §1.4 [21], vía El Cronista): **renuncia presidencial + juicio político** (Santiago Peña) como parte de la cadena posterior al 2 nov. **Desenlace: hueco.** No se documenta en las fuentes quién sucede, en qué fecha, ni qué medidas adopta el sucesor. **Condición:** la cadena política es la variable que más puede mover el forecast — un sucesor puede restaurar el límite de patrimonio efectivo, publicar R(t) por banco, o no hacer nada — pero su desenlace no es proyectable con los datos disponibles. Se registra como la incertidumbre de mayor peso, no como un escenario con fecha.

## 6. IPS — reubicación de la cartera

### 6.1 El stock que se mueve (documentado)

| Magnitud | Valor |
|---|---|
| Exposición total del IPS en Ueno, sep 2026 | **Gs 2,03 billones (USD 348,5M)** — 41,7% de los fondos de Ueno (CSV) |
| CDA en Gs, 2025 | Gs 1,602 billones — 19,7% del inventario CDA Gs |
| CDA en USD, cierre 2025 | USD 27,427M — 19,95% del inventario CDA USD |
| Bonos, 2025 | Gs 250.000M |
| Caja y Equivalentes, 2024 | Gs 665.685M + USD 12.241.088 |
| Posición al 30 oct 2026 | **9,70% de la cartera** (tope 10%); sin nuevas colocaciones en 2026 |

### 6.2 Derivados (ESTIMADO, con la derivación declarada)

- **Cartera total del IPS (ESTIMADO): Gs 20,93 billones** = 2,03 billones / 9,70%. Depende de que el 9,70% y los 2,03 billones refieran a la misma base (cartera total) — si la base difiere, el estimado cambia; se marca como tal.
- **Tope del 10% por emisor (ESTIMADO): Gs 2,09 billones.** Consecuencia: **el tope del 10% NO obliga a diversificar** — toda la exposición de Ueno (Gs 2,03 billones) cabría legalmente en un solo emisor. La diversificación real depende del límite de patrimonio efectivo por emisor, que fue eliminado por la Res. 093-046/2024 y cuya restauración es una propuesta (parteaguas §10), no un hecho.
- **Inventario CDA Gs implícito: Gs 8,13 billones** (1,602 / 19,7%). **Inventario CDA USD implícito: USD 137,5M** (27,427M / 19,95%).

### 6.3 El ritmo: hueco

**Cronograma de vencimientos de los CDA del IPS en Ueno: hueco.** Sin vencimientos no hay ritmo de reubicación: si los CDA vencen en semanas, la reubicación es inmediata; si vencen en años, el IPS queda atado a la resolución (y a la compensación) durante años. **La reubicación no es una decisión del IPS sola: es el vencimiento de los instrumentos más la decisión de dónde recolocar.** Los 32.000 jubilados se mueven el 17 nov (pago), pero sus préstamos con descuento de haberes y la caja diaria tienen otro ritmo — tampoco documentado.

**Escenario 6a (condición: vencimientos cortos + restauración del límite de PE).** El IPS recoloca Gs 2,03 billones entre varios bancos con tope por PE; ningún receptor recibe más de ~Gs 400.000M de golpe; la R_X de los receptores sube por absorción y luego se estabiliza. **Escenario 6b (condición: vencimientos largos o sin restauración del límite).** El IPS queda expuesto a la compensación durante meses o años, o recoloca todo en BNF (el tope del 10% lo permite) — escenario C de §2.3. **El indicador que distingue es el primer vencimiento publicado, no una fecha que se pueda adelantar.**

## 7. Lectura SNT del después

### 7.1 Recuperación del ASI — hoja de ruta condicional (sin fechas)

ASI hoy: jubilados 0/5, ahorristas 0/4 (+1 sin datos), OEEs 0/5. Cada condición tiene un trigger observable; ninguno tiene fecha salvo el 17 nov.

| Condición (alto ASI) | Qué la cumpliría | Trigger observable | Fecha |
|---|---|---|---|
| Puede elegir banco | Reasignación **con elección** (hoy automática, sin elección en primera instancia) | Publicación del mecanismo de elección por el IPS/BCP | Hueco |
| Puede retirar/transferir sin permiso del hub | Cuentas operativas en el receptor + fondos descongelados | Primer pago 17 nov (jubilados); descongelamiento de ahorristas | 17 nov (jubilados); resto hueco |
| Tiene información veraz | Publicación de R(t) por banco y de la cartera del IPS | MEF Informe de Bancos oct/nov 2026 con Ueno en cero y receptores desagregados | A observar |
| Puede recuperar a tiempo | FGD hasta el tope + compensación del resto | Balance de exclusión 17 nov; cronograma de compensación | 17 nov (balance); resto hueco |
| Puede diversificar | IPS reparte entre emisores (tope 10% + límite PE restaurado) | Publicación de la nueva cartera del IPS | Hueco |

**Lectura:** la primera condición que puede cumplirse es "recuperar a tiempo" (17 nov, parcialmente: el anticipo y el primer pago). La última es "diversificar": requiere una decisión normativa (restaurar el límite de PE) y una decisión de cartera (repartir). **El ASI no se recupera con el pago: se recupera con la elección.** Un jubilado que cobra en un banco que no eligió sigue en 0/5 en esa condición aunque cobre a tiempo.

### 7.2 El muro en reversa — los 5 eventos positivos (pregunta, no redefinición)

El muro es bipolar por propuesta de Elán: 5 eventos negativos → colapso; 5 positivos → salto de rana. Los 5 φ negativos están fechados (§6 de v2). Los 5 positivos son el espejo — **se formulan como pregunta, no como redefinición del leapfrog** (que sigue siendo b < 0):

1. **Restaurar el límite de patrimonio efectivo** sobre la exposición total por emisor (no por instrumento) — propuesta del parteaguas §10. Espejo del φ paso 2.
2. **Publicar R(t) por banco y por dominio** con la periodicidad del Informe de Bancos del MEF — propuesta del parteaguas §10. Espejo del φ paso 5 (la reserva que ocultaba).
3. **Protocolo de absorción con reparto competitivo y aleatorio por tipo de cuenta** — propuesta del parteaguas §10. Espejo del φ paso 3 (el fideicomiso que sostuvo el balance).
4. **Protocolo de contingencia del IPS** (el que la Contraloría constató que no existe) — espejo de la ausencia de protocolo, el nodo sombra institucional del dominio IPS.
5. **Supervisión que actúa sobre sus propios memorandos** (el memo Rivarola del 10 jul 2026 recomendó no admitir la venta de cartera morosa a Vinanzas; quedó bajo reserva) — espejo del φ paso 4 (la tolerancia).

**El test es medible:** si esos 5 eventos ocurren, la prueba es si la exposición de las unidades atómicas a un solo hub cae — su propio b < 0, medible en las publicaciones futuras del MEF y del IPS. Si no ocurren, el muro queda en 5/0 y el próximo hub se forma en otro dominio (parteaguas §10). **No se afirma que 5 positivos = leapfrog**: la conexión muro–b sigue siendo hipótesis (v2 §9).

### 7.3 Las bandas hacia adelante — protocolo de vigilancia, no valores

El hub murió; las bandas se trasladan a los receptores como **protocolo de vigilancia mensual** con el mismo feed (MEF Informe de Bancos):

| Banda | Adelante | Qué se vigila | Dato necesario | Estado |
|---|---|---|---|---|
| Roche-R | R_X de cada receptor, mes a mes | ¿Algún receptor muestra b > 0 sostenido (3+ meses) en su R_X? Un salto de un mes es absorción; una deriva es un nuevo drift | MEF mensual (el feed continúa) | Vigilable desde oct 2026 |
| Roche-C | Fondos públicos del receptor / su PE > 1,0 | ¿Algún receptor cruza 1,0 por la absorción? | **PE por banco receptor** (boletines BCP) | **Hueco** — sin PE por banco no hay Roche-C de receptores |
| Roche-S | Solvencia del receptor / 12% < 0,50 | ¿La absorción deteriora la solvencia de algún receptor? (las megacuentas no realizables son el riesgo) | Solvencia por banco (BCP) | Vigilable cuando se publique |

**Advertencia:** el umbral 0,10 no se aplica mecánicamente a los receptores (BNF y Continental ya están por encima por estructura). La vigilancia es la **deriva**, no el nivel.

### 7.4 La forma en la tela y la dirección del forecast

De `ueno-acoa-tela-cimatica-incertidumbre.md` (§3): la tendencia es **saturación, no aceleración**; R(t) termina en τ=1; la dirección es **de un hub a siete receptores, con la masa de fondos conservada y repartida**. La incertidumbre es empírica (±14,1% en R, residuos del ajuste; FX 0,0002 despreciable; u = NULL). La firma cimática de Ueno (A1 2,065, A2 1,326, bulto en A4 0,717 — firma de la saturación) y su asignación al centroide ACO (distancia 1,24; 0,49 normalizada a R/R_max) dicen que **la forma es ACO**: el forecast es el cierre de esa forma — la absorción. Lo que la tela no da es el número del reparto: eso lo da el balance de exclusión.

## 8. Huecos que más pesan en el pronóstico (ordenados)

| # | Hueco | Por qué pesa | Qué lo cerraría |
|---|---|---|---|
| 1 | **Recursos totales del FGD y número de depositantes de Ueno** | Sin ellos no hay monto total de pagos ni saber si el calendario del 17 nov se sostiene | Publicación del FGD / BCP |
| 2 | **Cronograma de vencimientos de los CDA del IPS** | Sin él no hay ritmo de reubicación de Gs 2,03 billones | Publicación del IPS |
| 3 | **Balance de exclusión (17 nov)** | Sin él no hay reparto real entre receptores ni valuación de lo realizable | El balance mismo |
| 4 | **PE por banco receptor** | Sin él no hay Roche-C de los receptores (la vigilancia del próximo hub) | Boletines del BCP |
| 5 | **Desenlace de la cadena política** | Mueve las decisiones normativas (restaurar el límite, publicar R(t)) | Los hechos |
| 6 | **Valuación de los bienes embargados y de las megacuentas** | El embargo (Gs 2,1005 billones) no es lo recuperable | Balance de exclusión / remates |
| 7 | **Fechas de Nota 019 e informe al Senado; audiencias y sentencia** | Sin ellas el proceso penal no tiene línea de tiempo hacia adelante | Fiscalía / juzgado |
| 8 | **Los 2 oferentes no nombrados** | Sin ellos el reparto igual es entre 5 o entre 7 (escenarios A vs A5) | Publicación del IPS/BCP |
| 9 | **Haberes mensuales de los 32.000 jubilados** | Sin ellos no se cuantifica el flujo mensual de la reasignación | IPS |
| 10 | **MEF oct/nov 2026** | Sin ellos no se observa la primera R_X post-resolución | El feed mensual |

## 9. Qué vigilar (fechas observables)

| Fecha | Qué se observa | Qué decide |
|---|---|---|
| 5 nov 2026 | Anticipo FGD en 72 h (hasta Gs 10M) | Si se paga, el FGD opera; si no, escenario 1b |
| **17 nov 2026** | Primer pago a jubilados + cierre del balance de exclusión | El hito doble: pago y reparto |
| Cuando se publique | MEF Informe de Bancos **oct 2026** | Primera R_X post-resolución; ¿Ueno sigue con saldo o desaparece? |
| Cuando se publique | MEF Informe de Bancos **nov–dic 2026** | Deriva o solo absorción en los receptores |
| Cuando se publique | Nueva cartera del IPS | ¿Diversifica o concentra en un receptor? |
| Sin fecha | Nota 019, informe al Senado, audiencias | Línea de tiempo penal |

## Apéndice A — Método y reproducibilidad

- **Script:** `/tmp/forecast_ueno.py` (aritmética) y `/tmp/forecast_csv.py` (CSV). Stdlib. Saldos por banco leídos del `MEF_Informe_Bancos_2026-09.txt` (pdftotext del PDF, cifras preliminares según el propio informe).
- **Verificación de la base:** el total del sistema calculado desde los saldos por banco (USD 4.320.353.015 equiv) reproduce el R(t) de Ueno del CSV corregido (0,2395) exacto; la participación de Ueno (19,32%) y los totales por moneda reproducen los del PDF.
- **Convenciones:** FX 6.000 por fila (misma convención de la tabla maestra). "Billones" = 10¹². Los escenarios suponen conservación de la masa de fondos públicos dentro del sistema y total constante.
- **Corrección registrada:** en el script de trabajo, dos cocientes se calcularon primero con 2,03 billones como 2,03×10⁹ (error de unidades ×1.000); se detectaron antes de escribir cualquier entregable y se corrigieron: FGD/exposición IPS = **0,011%** (no 11,24%), cartera IPS implicita = **Gs 20,93 billones** (no 20,93 mil millones). Ningún valor erróneo llegó al documento ni al CSV.
- **Archivos v2 y telas intactos:** no se tocó `modelo-ueno-resultados-v2.md`, `ueno-acoa-tela-cimatica-incertidumbre.md`, el CSV ni las NOTAS.

## Apéndice B — Qué necesitarían el espacio y el podcast si se actualizan con el forecast

> Para aplicar después, con el visto bueno de Elán. No se ha tocado ni el espacio ni el podcast.

**Espacio — sección caso Ueno (nueva subsección "6 · Qué va a pasar" o cierre del caso):**

1. FGD: tope Gs 228,3M por depositante (0,011% de la exposición del IPS); anticipo Gs 10M en 72 h; primer pago a jubilados **17 nov 2026**; monto total del FGD **hueco** (sin número de depositantes ni fondo total).
2. Absorción: 7 oferentes (5 nombrados: BNF, Itaú, GNB, Continental, Sudameris); balance de exclusión **17 nov 2026**; escenarios de reparto con la R_X posterior por receptor (A: BNF 0,4252; B: BNF 0,5553; C: BNF 0,8656 con 46,4% del sistema — el nuevo hub que ACO-A debe evitar); Δ sigue no estimable hasta que se publique A(τ).
3. Embargo Gs 2,1005 billones (USD 350,1M equiv) — congela, no cobra; −0,25% vs Derechos Fiduciarios (coincidencia); +0,45% vs exposición del IPS (coincidencia).
4. IPS: Gs 2,03 billones a reubicar; cartera implicita **Gs 20,93 billones (ESTIMADO)**; tope 10% = Gs 2,09 billones (ESTIMADO) — **no obliga a diversificar**; vencimientos **hueco**.
5. ASI: hoja de ruta condicional (primero "recuperar a tiempo" el 17 nov; último "diversificar"); el ASI no se recupera con el pago sino con la elección.
6. Muro en reversa: los 5 eventos positivos como pregunta (restaurar límite PE; publicar R(t); protocolo de absorción; protocolo de contingencia del IPS; supervisión que actúa) — sin redefinir leapfrog.
7. Vigilancia: Roche-R por receptor (deriva, no nivel), Roche-C de receptores **hueco** (sin PE por banco), Roche-S de receptores; hitos observables 5 nov, 17 nov, MEF oct/nov 2026.

**Podcast — si se graba un episodio forecast (no existe guion; sería nuevo):** los números hablados serían: tope FGD doscientos veintiocho millones trescientos mil guaraníes por depositante, cero punto cero once por ciento de la exposición del I P S; primer pago diecisiete de noviembre; siete bancos oferentes, cinco nombrados; balance de exclusión diecisiete de noviembre; embargo dos coma uno cero cero cinco billones de guaraníes; exposición del I P S dos coma cero tres billones; cartera implicita veinte coma noventa y tres billones, estimado. Duración estimada: un episodio de cierre de ~10–12 min, separado del backcast (el v2 ya dura 19:27 y con los cambios ~20:05).
