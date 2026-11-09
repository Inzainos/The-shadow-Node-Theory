# COPIA DE REGISTRO — Ueno v3 (corrección 2026-11-09)
# Archivo original: docs/ueno-2026-11-07/modelo-ueno-resultados.md
# Versión: v1
# Estado: archivo de registro — SIN CAMBIOS respecto al original. Cuerpo intacto; solo se añadió esta cabecera.
# Fecha de la copia: 2026-11-09
# md5 original: 61d0497454d5ab7c068e7834ae17195c
# sha256 original: 1f49836f7167ad29ef6ec8ad685dfdb9c70584033116bb7c7aa4f882f5c202c8
#
# Inyección al modelo SNT — caso Ueno Bank: resultados

**Fecha:** 2026-11-06/07. **Tabla:** `tabla-maestra-ueno-mef.csv` (45 filas, ene 2023 – sep 2026), **aprobada por Elán tal como está, sin correcciones** (2026-11-06 ~21:27). **Marco:** SNT v2.7.5.1 (README del repo, marco v34). **Método:** Python stdlib, script `/tmp/modelo_ueno.py` (reproducible; cada cálculo verificado dos veces). **Fuentes:** tabla maestra + NOTAS (§§1–11), documento base de adquisición, parteaguas v2, backcast Roche, notas de trabajo (parteaguas, backcast-Roche, taxonomía por dominio).

## Reglas aplicadas

- **b es descriptor de deriva dentro de una ventana**, nunca prueba de mecanismo ni de φ→b. Se reporta siempre con ventana + método + origen de t + n.
- **b ≥ 1 es banda descriptiva no clasificada**, NO prueba de superlinealidad.
- La malversación es **presunta, denunciada e investigada** (denuncia MEF 5 nov 2026, Gs 250,000M Caja Fiscal + Gs 123,838M intereses; imputación a 27 personas 4 nov 2026), no hecho declarado por sentencia. El trigger oficial fue **insuficiencia de solvencia**. El colapso es evento **exógeno** por clasificación de Elán; la deriva fue **endógena**.
- El **2 nov 2026 es fecha de detonante/reconocimiento, NO inicio del fallo**.
- Series MEF / ABC / IPS en columnas separadas, sin mezclar definiciones; FX 6,000 por fila; discrepancias como incertidumbre, nunca corregidas en silencio.
- Lo no calculable se marca como **hueco**, nunca se rellena.

## 1. R(t) — re-verificación desde las columnas del CSV

Definición: R(t) = fondos públicos en Ueno / fondos públicos en el resto del sistema (total MEF − Ueno), en USD equivalentes a FX 6,000 por fila (nov 2024: ancla del documento, FX implícito 6,696).

Recomputada fila por fila como `ueno_total_usd_equiv / (total_sistema_usd_equiv − ueno_total_usd_equiv)`:

| Fecha | R(t) CSV | R(t) recalculada | Diferencia | Fuente |
|---|---|---|---|---|
| 2024-02 | 0.0284 | 0.0284 | −0.0000 | MEF PDF |
| 2024-03 | 0.0319 | 0.0319 | +0.0000 | MEF PDF |
| 2024-04 | 0.0332 | 0.0332 | −0.0000 | MEF PDF |
| 2024-05 | 0.0346 | 0.0346 | −0.0000 | MEF PDF |
| 2024-06 | 0.0338 | 0.0338 | +0.0000 | MEF PDF |
| 2024-07 | 0.0610 | 0.0610 | −0.0000 | MEF PDF |
| 2024-09 | 0.0777 | 0.0777 | +0.0000 | MEF PDF |
| 2024-11 | 0.1100 | 0.1098 | −0.0002 | ancla-documento |
| 2025-04 | 0.1396 | 0.1396 | −0.0000 | MEF PDF |
| 2025-05 | 0.1628 | 0.1628 | −0.0000 | MEF PDF |
| 2025-06 | 0.1706 | 0.1706 | −0.0000 | MEF PDF |
| 2025-07 | 0.2079 | 0.2079 | −0.0000 | MEF PDF |
| 2025-08 | 0.2457 | 0.2457 | −0.0000 | MEF PDF |
| 2025-09 | 0.2467 | 0.2467 | +0.0000 | MEF PDF |
| 2025-10 | 0.2670 | 0.2670 | +0.0000 | MEF PDF |
| 2025-11 | 0.2643 | 0.2643 | −0.0000 | MEF PDF |
| 2025-12 | 0.2280 | 0.2280 | −0.0000 | MEF PDF |
| 2026-02 | 0.2357 | 0.2357 | −0.0000 | MEF PDF |
| 2026-04 | 0.2543 | 0.2543 | −0.0000 | MEF PDF |
| 2026-05 | 0.2254 | 0.2254 | −0.0000 | MEF PDF |
| 2026-06 | 0.2246 | 0.2246 | −0.0000 | MEF PDF |
| 2026-07 | 0.2306 | 0.2306 | −0.0000 | MEF PDF |
| 2026-08 | 0.2161 | 0.2161 | −0.0000 | MEF PDF |
| 2026-09 | 0.2395 | 0.2395 | −0.0000 | MEF PDF |

**Resultado: la serie reproduce el CSV.** Diferencia máxima 0.0002 (nov 2024, redondeo del ancla: 271/2,468 = 0.1098 → 0.110 en el CSV). Participación de Ueno reproduce igual (diferencia máxima 0.00005). **24 meses con R calculable** (23 con PDF + 1 ancla). Valores clave confirmados: feb 2024 0.028, jul 2024 0.061, sep 2024 0.078, nov 2024 0.110, nov 2025 0.264, meseta 2026 0.216–0.254.

**Huecos (R no calculable):** oct 2024, dic 2024–mar 2025, ene y mar 2026 (sin total del sistema), todo 2023 (Ueno sin fila individual o dentro de OTROS BANCOS). No se imputa nada.

**Observaciones registradas, no ajustadas:** salto jul 2024 (R 0.034→0.061, +80% en un mes); USD de Ueno feb–mar 2024 casi idéntico (+USD 16) mientras Gs sube — posible cifra arrastrada; caída dic 2025 (Ueno −12.5% en USD, R 0.264→0.228) mientras el sistema sube — el documento no la comenta.

## 2. b — descriptor de deriva por ventana (OLS log-log: log R = log a + b log t)

Tabla de lectura del Módulo 0 (README): b < 0 convergencia / leapfrog; −0.1 < b ≤ 0.05 estado estacionario; 0.05 < b ≤ 0.3 satelización gradual; 0.3 < b < 1 satelización activa; b ≥ 1 banda descriptiva no clasificada.

| # | Ventana | Método | Origen de t | n | b | a | R² | Lectura (Módulo 0) |
|---|---|---|---|---|---|---|---|---|
| (a) | nov 2024 → nov 2025 | Extremo a extremo, anclajes del documento (R 0.110 → 0.274) | t=1 nov 2024 | 2 | **0.356** | — | — | Satelización activa |
| (a') | nov 2024 → nov 2025 | Extremo a extremo, valores CSV (R 0.110 → 0.2643) | t=1 nov 2024 | 2 | **0.342** | — | — | Satelización activa |
| (b) | abr – nov 2025 | OLS log-log | t=1 nov 2024 (t=6..13) | 8 | **0.906** | 0.0278 | 0.955 | Satelización activa (pendiente local, 2ª mitad) |
| (c) | dic 2025 – sep 2026 (meseta) | OLS log-log | t=1 nov 2024 (t=14..23) | 8 | **−0.046** | 0.2652 | 0.025 | Estado estacionario |
| (d) | feb – jul 2024 (pre-Roche) | OLS log-log | t=1 feb 2024 (t=1..6) | 6 | **0.288** | 0.0262 | 0.503 | Satelización gradual (ajuste débil) |
| (e) | feb 2024 – sep 2026 (completa) | OLS log-log | t=1 feb 2024 | 24 | **0.813** | 0.0165 | 0.911 | Satelización activa (resumen grueso) |
| (e') | feb 2024 – sep 2026 (solo PDF) | OLS log-log | t=1 feb 2024 | 23 | **0.814** | 0.0165 | 0.911 | Idéntica a (e): el ancla no mueve el ajuste |

**Discrepancias con el encargo (reportadas, no corregidas en silencio):** (c) tiene **n=8, no 10** — los meses con R en dic 2025–sep 2026 son dic 2025, feb 2026 y abr–sep 2026 (ene y mar 2026 no tienen total del sistema). (e) tiene **n=24 con el ancla / 23 solo PDF** (el encargo decía 23; coincide con la variante solo PDF).

**Hallazgo de sensibilidad al origen de t (importante):** el mismo ajuste (b) con origen local (t=1 en abr 2025) da **b = 0.344, R² = 0.942**, frente a 0.906 con el reloj del documento (t=1 nov 2024). Y la meseta (c) con origen local da b = −0.012, R² = 0.030 (misma conclusión: sin tendencia). **b depende del reloj elegido**: es un descriptor de la ventana con su origen declarado, no una constante intrínseca del sistema. Por eso cada b aquí lleva su origen. La misma advertencia aplica al b IPS (ver abajo).

**Verificación del b IPS del documento (2.93):** el documento enuncia b = 2.93 para la serie IPS 2023–2025 sin especificar la variable. Verificado: OLS log-log sobre **r_ips** (0.0101, 0.0917, 0.2453; t=1,2,3) da **b = 2.934, R² = 0.995** — reproduce el 2.93. Sobre participaciones (1.0%, 8.4%, 19.7%) da 2.752 (R² = 0.992) y sobre montos en Gs da 2.762 (R² = 0.994). **Conclusión: el 2.93 es el ajuste sobre r_ips (la forma de razón, coherente con R(t)), no sobre participaciones.** En cualquier caso b ≥ 1 es banda descriptiva no clasificada (n=3 puntos anuales); NO es prueba de superlinealidad. El documento ya lo advierte; aquí queda verificado con la variable identificada.

**Lectura conjunta de b:** la deriva no fue uniforme. Antes de Roche (feb–jul 2024) era gradual (b ≈ 0.29, R² = 0.50 — ajuste débil, dominado por el salto de jul 2024). En la ventana completa nov 2024–nov 2025 fue activa (b ≈ 0.35), y dentro de ella la segunda mitad se empinó (b local ≈ 0.91 en el reloj del documento, R² = 0.96). Después de nov 2025 la deriva se detuvo: la meseta tiene b ≈ −0.05 con R² = 0.02, es decir, **sin tendencia medible**. El ajuste de toda la serie (b ≈ 0.81, R² = 0.91) resume tres regímenes distintos en un solo número y no debe usarse solo: esconde el salto, la aceleración y la meseta.

## 3. Roche-R (relativa): R(t) > 0.10

- **Primer mes con R > 0.10: nov 2024 (R = 0.110).** Mes anterior con dato: sep 2024 (0.0777). **Ventana de cruce: sep–nov 2024** (oct 2024 sin PDF; no se interpola a día).
- **Cruce de 0.20:** entre jun 2025 (0.1706) y jul 2025 (0.2079). Interpolación lineal, fracción 0.788: con la convención del documento (valores al inicio del mes) ≈ **24 jun 2025**; con convención de fin de mes ≈ 24 jul 2025. La diferencia es un artefacto de convención, no de los datos. Se adopta ≈24 jun 2025 (misma convención del documento y de la verificación previa).
- R(t) se mantuvo > 0.10 en todos los meses con dato desde nov 2024 hasta sep 2026 (mínimo de la meseta: 0.2161, ago 2026). No hay retorno por debajo de Roche-R en la serie.

## 4. Roche-C (concentración): fondos públicos en Ueno / patrimonio efectivo > 1.0

Valores fechados de los documentos (backcast §5, fuentes ABC/Asoban/EEFF):

| Momento | Fondos en Ueno | Patrimonio efectivo | Roche-C | Fuente |
|---|---|---|---|---|
| Nov 2024 | IPS Gs 1.7 billones | Gs 1.6 billones | **1.06** | ABC 2026-01-28 / 2026-07-12 |
| Dic 2024 | Sector público Gs 1,747 billones | Gs 1.56 billones | **1.12** | Asoban vía ABC 2026-09-21 / EEFF 2024 |
| Cierre 2024 | IPS Gs 1,766 billones | Gs 1.56 billones | **1.13** | ABC 2026-07-12 / 2026-07-14 |
| 31 oct 2025 | IPS Gs 2.1 billones | Gs 1.8 billones | **1.17** | ABC 2025-12-30 |
| Cierre 2025 | IPS Gs 2.24 billones | Gs 2.20 billones | **1.02** | ABC 2026-07-12 |

**Entrada a Roche-C: nov 2024** (1.06), mismo mes que Roche-R. Roche-C se mantuvo > 1.0 en los cinco puntos fechados (máximo 1.17, 31 oct 2025; mínimo 1.02, cierre 2025).

**HUECO: la serie mensual de Roche-C NO es calculable.** El patrimonio efectivo solo existe en cierres (2024: Gs 1.56 billones; 2025: Gs 2.20 billones) y en el punto 31 oct 2025 (Gs 1.8 billones). Sin serie mensual de patrimonio efectivo no se puede fechar el cruce al mes con más precisión que nov 2024, ni calcular su trayectoria entre los puntos.

## 5. Roche-S (solvencia): solvencia reportada / mínimo legal 12% < 0.50

| Fecha | Solvencia reportada | Roche-S | Fuente |
|---|---|---|---|
| Mar 2026 | 15.01% | **1.251** | Parteaguas v2 §1.4 [19][22] |
| Jun 2026 | 14.5% | **1.208** | Parteaguas v2 §1.4 [19][22] |
| Sep 2026 | 13.85% | **1.154** | Parteaguas v2 §1.4 [19][22] |
| 2 nov 2026 | 5.56% | **0.463** | BCP, resolución (Ley 2334/03 art. 13 inc. b) |

La solvencia reportada se mantuvo **por encima del mínimo (Roche-S > 1) hasta sep 2026**. El cruce económico de Roche-S **no es fechable con datos públicos**: entre sep y nov 2026 el reporte pasó de 13.85% a 5.56% tras previsiones > Gs 1.6 billones (inspección 31 oct), pero el reporte estaba sostenido por intangibles (Gs 761,444M), Derechos Fiduciarios (Gs 2,105,743M) y Participaciones (+8,000% en 2025), saldos de cierre 2025 sin fecha mensual. **El 2 nov 2026 es el reconocimiento legal de Roche-S (0.463 < 0.50), no su cruce económico.**

## 6. φ — la secuencia en 5 pasos (observable, fechada)

φ es captura de la gobernanza: la capacidad de modificar la regla que limita. Se detecta por acumulación, no por un solo acto (parteaguas v2 §4.3).

| Paso | Fecha | Acto | Observable |
|---|---|---|---|
| 1 | **9 nov 2023** | Baja el puntaje mínimo para subastas | 65 → 60 (y baja la calificación exigida después) |
| 2 | **12 nov 2024** | Res. IPS C.A. N° 093-046/2024 | Elimina el límite de patrimonio efectivo; baja la calificación exigida de A-Py con tendencia fuerte a A genérica |
| 3 | 2024–2025 (fusión Visión) | Activación de gastos de fusión como activo fiduciario | Derechos Fiduciarios Gs 2,105,743M = 99.44% del patrimonio neto (cierre 2025) |
| 4 | 2024 (Res. SB.SG. N° 00105/2024) | Tolerancia a no desagregar software en la subcuenta de transparencia | Intangibles +Gs 654,799M solo en 2025 (Gs 761,444M total; triplica los intangibles de nueve bancos juntos, Gs 269,233M) |
| 5 | 2024–2026 | Reserva supervisora mantenida | Notificaciones 5 jun y 24 jul 2026 sin acción pública hasta la inspección del 31 oct; memorando Rivarola 10 jul 2026 bajo reserva |

**φ contable (parteaguas v2 §1.2):** balance 2025 con Gs 2.5 billones de gastos en el fideicomiso de fusión con Visión y Gs 2.6 billones de cartera morosa mal clasificada (acta Directorio BCP 19 jun 2026). **Ningún paso, por sí solo, dispara una alarma; juntos eliminan todos los frenos.** φ no se mide como campo continuo (README: postulada por dominio); aquí se presenta como secuencia observable fechada, que es lo que los documentos permiten.

## 7. ASI por unidad atómica — evaluación documental (NO la fórmula del repo)

ASI (v2 §1.3) = Índice de Soberanía Atómica: cuánto control conserva la unidad atómica cuando el hub falla. Condiciones de ASI alto según la v2: (1) puede elegir banco, (2) puede retirar/transferir sin permiso del hub, (3) accede a información veraz, (4) recupera en plazo. Se añade (5) diversifica (no concentra su exposición en un solo hub), criterio del encargo, coherente con la diversidad del muro. Cada condición se evalúa **al momento del fallo del hub** (eso es lo que ASI mide), con su fuente.

**NO se calcula ASI = δH·α/F (fórmula del repo): no hay datos de eventos de comportamiento para Ueno** (δH requiere distribución de problemas, α eventos autónomos/total, F caos interno). El conteo siguiente es la **evaluación documental del ASI**, no la fórmula del repo. Umbral del repo (ASI > 1 define soberanía) no aplicable a un conteo.

| Condición de ASI alto | Jubilados (~32,000) | Ahorristas (depositantes) | OEEs (organismos; documentado vía IPS) |
|---|---|---|---|
| 1. Puede elegir banco | **NO** — reasignación automática sin elección inicial [Infobae; parteaguas §3.2, §9.3] | **NO** — al fallar el hub, fondos congelados y reasignación por proceso, sin elección [§9.3] | **NO** — elección constreñida: Ley 7609/25 art. 79 ordena BNF salvo contratos vigentes/gradualidad; los fondos permanecieron por convenios heredados [§2.1] |
| 2. Puede retirar/transferir sin permiso del hub | **NO** — fondos congelados; pago vía FGD/reasignación [§9.1] | **NO** — fondos congelados mientras se define el balance de exclusión [§9.3] | **NO** — congelados; recuperación vía FGD/proceso competitivo [§9.1] |
| 3. Accede a información veraz | **NO** — la colocación se hizo sobre una situación patrimonial que luego resultó sustancialmente distinta [La Nación, denuncia MEF] | **NO** — el banco presentaba públicamente una situación patrimonial que cumplía, distinta de la constatada [La Nación] | **NO** — balance Gs 3,163,975M vs Tesoro Gs 3,721,013M + USD 235M (discrepancia registrada, no resuelta) [Asoban/ABC]; situación presentada ≠ constatada [La Nación] |
| 4. Recupera en plazo | **NO** — primer pago 17 nov es anticipo (≤ Gs 10M); recuperación total pendiente de balance de exclusión (máx. 15 días) y compensación, sin plazo definido | **NO** — anticipo ≤ Gs 10M en 72 h; cobertura total hasta 75 SM (Gs 228.3M); saldos superiores a compensación sin plazo definido | **NO** — dependen de la denuncia y del proceso penal para intentar recuperar [§9.3]; sin plazo de recuperación total |
| 5. Diversifica | **NO** — cuenta cautiva por convenio/préstamo IPS heredado de Visión [CGR/ABC, §3.2] | **SIN DATO** — no hay catastro de depositantes ni diversificación por ahorrista en los documentos | **NO** — concentración documentada: IPS 19.7% CDA Gs, 19.95% CDA USD, 9.70% de cartera (30 oct); Caja Fiscal Gs 250,000M en una adjudicación; cuota de Ueno en fondos del Estado 18.6% (dic 2025) |
| **Conteo** | **0 / 5** | **0 / 4 evaluables** (1 sin dato) | **0 / 5** |

**Resultado: ASI bajo en las tres unidades atómicas.** Coincide con la evaluación de la v2 (§9.3), ahora verificada condición por condición con fuente. La lección de la v2 se confirma con los números: **una absorción puede ser ordenada en términos sistémicos y, al mismo tiempo, dejar un ASI bajo.**

## 8. ACO-A — colapso y absorción

**Criterio ACO (README, Módulo 1):** (1) extinción funcional del hub o nodo; (2) absorción de recursos por nodo específico identificable. **Ambas se cumplen y son observables:**

1. **Extinción funcional:** resolución BCP 2 nov 2026 (Ley 2334/03); congelamiento de activos y pasivos; cierre de servicios; imposibilidad de reponer encaje legal USD 70M; solvencia 5.56%.
2. **Absorción identificable:** 7 bancos presentaron propuestas al IPS para absorber a los jubilados [Infobae]; receptores documentados: BNF, Itaú, GNB (jubilados y fondos públicos), Continental, Sudameris; proceso competitivo (no un único receptor); balance de exclusión con plazo máximo de 15 días; 120 funcionarios del BCP desplegados para conciliación.

**Sobre Δ (A(τ) = c·τ^Δ): NO estimable con estos datos.** No hay serie temporal de A(τ) (absorción en función del tiempo) en la tabla ni en los documentos: no hay montos absorbidos por fecha ni por receptor. **No se inventa Δ.** Lo que el repo dice de su propio corpus (18 casos: |log₁₀ m| mediano 0.292 → 0.071) no es computable aquí: no hay serie de m para Ueno.

**Modo de colapso (descriptivo, juicio — no medición):** entre los 5 modos del repo (Regulado, Craquelado, Caída-a-piso, Acantilado Catastrófico, Barrido Logístico), el ajuste más cercano es **Acantilado Catastrófico** para el tramo final: la solvencia reportada cae de 13.85% (sep 2026) a 5.56% (2 nov 2026) en ~1 mes tras la inspección del 31 oct — un acantilado contable. Con rasgos de **Craquelado** (quiebres por fricción) en la acumulación: los 5 pasos de φ, las notificaciones de jun/jul 2026, el memorando Rivarola bajo reserva. **Clasificación descriptiva, no medida:** los modos del repo son descriptivos sin prueba de n grande, y aquí no hay serie de A(τ) para clasificar por forma. La entrada al radio de Roche → colapso abrupto, Δ negativo, A(τ) decreciente (README) describe la forma general del caso: entrada a Roche nov 2024, reconocimiento abrupto nov 2026.

**Aritmética de la absorción (todo verificable en los documentos):**

| Magnitud | Valor | Fuente / cálculo |
|---|---|---|
| Cobertura FGD por depositante y por entidad | Gs 228,300,000 (75 salarios mínimos) | Ley 2334/03; parteaguas §3.3, §9.1 |
| Primer pago (anticipo) | Hasta Gs 10,000,000 en 72 h (Ley 7745/2026) | 4.38% del tope de cobertura |
| Cobertura FGD / exposición IPS (sep 2026, Gs 2.03 billones) | **0.011%** | 228.3M / 2,030,000M — el tope cubre una centésima del 1% de la exposición del IPS como depositante único |
| Exposición IPS / fondos públicos en Ueno (sep 2026) | 40.8% (doc, USD 855M) / 41.8% (CSV, USD 834.8M) | USD 348.5M / total Ueno |
| Jubilados a reasignar | ~32,000; primer pago 17 nov | Parteaguas §9.1; [Infobae] |
| Bancos pujantes por los jubilados | 7 | [Infobae] |
| Plazo máximo balance de exclusión | 15 días | BCP vía ABC [7] |
| Embargo preventivo (3 nov 2026) | USD 70M + Gs 1,621,853,458,972 + Gs 58,639,000,000 costas | Juzgado 8° turno, a pedido del BCP |
| Embargo total en Gs equivalentes (FX 6,000) | **Gs 2.1005 billones** | 420,000M + 1,621,853M + 58,639M |
| Embargo total vs Derechos Fiduciarios (Gs 2,105,743M) | **−0.25%** | Observación aritmética: el embargo es casi exactamente del tamaño de los Derechos Fiduciarios. Los componentes son distintos en definición; no se afirma identidad, se registra la coincidencia numérica. |
| Crédito a vinculadas sep 2025–may 2026 | ~USD 146M a Mowi, Grupo Hendy, Grupo M, a sola firma, sin garantías | ABC [17]; por encima del tope 20% |
| USD 146M / patrimonio efectivo (cierre 2025, Gs 2.20 billones ≈ USD 366.7M a FX 6,000) | **39.8%** (≈ 2× el tope del 20% ≈ USD 73.3M) | Cálculo con FX 6,000 y cierre 2025; aproximado |
| Deudas de las salvadoras (ago 2026) | Gs 905,825M ≈ USD 153M = 35% del patrimonio efectivo | Informe supervisión 8 jun 2026 [5] |
| Patrimonio efectivo implícito por ese 35% | **Gs 2.59 billones** | 905,825M / 0.35 — **tensión registrada:** supera los cierres documentados (1.56 billones en 2024; 2.20 en 2025; 1.8 al 31 oct 2025). El 35% del documento implica un patrimonio efectivo mayor que los cierres; posible valor de ago 2026 no documentado. Se registra como incertidumbre, no se resuelve. |
| Fondeo incremental dic 2024–mar 2025 no aplicado a préstamos | **91.75%** (depósitos +Gs 1,755,304M vs crédito neto +Gs 144,737M = 8.25% a préstamos) | Asoban vía ABC [7]; verifica el 92% del documento |

**Lectura:** la absorción existe y es observable, pero sus números no cierran para las unidades grandes: el tope del FGD es 0.011% de la exposición del IPS; el embargo total es del tamaño de una sola megacuenta contable (los Derechos Fiduciarios); y la división entre receptores todavía no tiene montos por receptor (hueco: medir la absorción por banco receptor es el paso siguiente, no asumible como uniforme).

## 9. Five-event-wall-by-phi

**Definiciones vigentes (no se redefinen):** el Muro de 5 eventos del repo es el umbral crítico de diversidad funcional mínima para escapar de la satelización (<5 tipos de evento distintos → >90% de churn en HackerEarth; 2–5% de pacientes con ≥5 eventos hub en TCGA). **Leapfrog = b < 0 (Convergencia/leapfrog, tabla del Módulo 0) y salto directo al Nivel Exógeno sin pasar por los intermedios (espacio).** No se define el leapfrog como "5 eventos positivos".

**Aplicación al caso Ueno (propuesta de Elán, en construcción):**

| Lado del muro | Eventos | Estado en Ueno |
|---|---|---|
| **Negativos (5)** | Los 5 pasos de φ (§6) | **5/5 ocurridos** (9 nov 2023; 12 nov 2024; activación de gastos de fusión; tolerancia a no desagregar software; reserva supervisora mantenida). El muro predice colapso. El colapso ocurrió (resolución 2 nov 2026). |
| **Positivos (5)** | Condiciones de ASI alto cumplidas (§7) | Jubilados **0/5**; ahorristas **0/4** (+1 sin dato); OEEs **0/5**. Ninguna unidad alcanza 5 positivos. Ninguna unidad alcanza el salto bajo el conteo de la propuesta. |

**Convergencia de los dos instrumentos (observación, no prueba):** bajo la definición vigente del repo tampoco hay leapfrog en Ueno: ningún ajuste de b da b < 0 con significación — la única ventana con b negativa es la meseta (b ≈ −0.05, R² = 0.02, indistinguible de cero). El conteo del muro (0 positivos) y la lectura de b (sin convergencia) **coinciden en el resultado: nadie escapó**. La conexión entre ambos —por qué 5 eventos positivos producirían b < 0— sigue siendo **pregunta abierta**.

**HIPÓTESIS de reconciliación (de Mole, NO establecida):** los eventos positivos son acciones que bajan R(t) (diversificar fuera del hub, retirar, elegir otro banco), es decir, empujan b hacia negativo; el salto al Nivel Exógeno es salir de la órbita del hub. Si la hipótesis es correcta, el conteo del muro y el signo de b miden lo mismo por dos vías. **No se escribe como hecho.** Queda para Elán.

## 10. Las bandas determinan el colapso

**Secuencia observada de cruces:**

| Banda | Cruce | Fecha |
|---|---|---|
| Roche-R (R > 0.10) | R = 0.110 | **Nov 2024** |
| Roche-C (> 1.0) | IPS/patrimonio = 1.06 | **Nov 2024** (mismo mes que Roche-R) |
| Roche-S (< 0.50) | 5.56/12 = 0.463 | **Reconocido 2 nov 2026** (cruce económico no fechable) |

**Las tres cruzadas = colapso completo con trigger legal.** La secuencia es: concentración (Roche-R) y capital superado (Roche-C) juntas en nov 2024 → dos años de permanencia más allá de Roche (meseta, sin retorno) → reconocimiento legal de la insolvencia (Roche-S) en nov 2026 → cadena (congelamiento, garantía, reasignación, denuncias, imputaciones, crisis política).

**Contrafactuales (HIPÓTESIS DE TRABAJO, marcadas como tales — no son mediciones):**
- **Solo Roche-R cruzada** (concentración sin brecha de capital): aviso. Reversible restaurando el freno (reimponer el límite de patrimonio efectivo). El sistema aún puede volver.
- **Roche-R + Roche-C sin Roche-S** (ruptura estructural sin trigger legal): el estado de 2025 — frágil pero operando, con el hub absorbiendo sin intermediar (92% del fondeo sin crédito). Ruptura sin reconocimiento.
- **Solo Roche-S** (quiebra de solvencia sin concentración): falla bancaria resoluble sin problema sistémico de absorción — el FGD y los receptores bastarían, porque no habría una masa de fondos públicos que trasladar.
- **Ninguna cruzada:** el sistema dentro del radio — deriva normal, sin ruptura.

La hipótesis de trabajo es que **el número y el orden de las bandas cruzadas determinan la forma del colapso**, y Ueno es el caso de las tres. Verificarla exige otros casos (Master, Fassil, CAME) con las mismas tres bandas — fuera de este encargo.

## 11. Qué muestran los modelos

**R(t) dice:** el hub creció 2.4–2.5 veces más rápido que el resto del sistema en doce meses (nov 2024 → nov 2025) y después dejó de crecer: se quedó en ~1/4 del resto durante 2026. La captura ocurrió en un año, no de a poco. Y el salto que la inicia es de un mes: jul 2024, R de 0.034 a 0.061.

**b dice:** la deriva tuvo tres regímenes, no uno. Gradual antes de Roche (0.29, ajuste débil), activa en la ventana nov 2024–nov 2025 (0.35), más empinada en la segunda mitad (0.91 en el reloj del documento) y detenida después (meseta b ≈ −0.05, R² = 0.02: sin tendencia). El número único de toda la serie (0.81) esconde los tres regímenes. Y b depende del reloj: la misma segunda mitad da 0.91 o 0.34 según el origen de t. b describe; no explica.

**Roche dice:** el sistema entró en zona de ruptura en nov 2024, dos años antes de que alguien actuara. El 2 de noviembre de 2026 no fue la entrada: fue el reconocimiento. Roche-R y Roche-C se cruzaron el mismo mes, juntas, y no hubo retorno: R nunca volvió por debajo de 0.10 en la serie.

**φ dice:** los cinco pasos son fechables y observables, cada uno defendible por separado. Juntos quitaron todos los frenos. φ no es un acto: es una secuencia. El paso 2 (12 nov 2024) es el que habilita el cruce: sin eliminar el límite de patrimonio efectivo, el cruce de nov 2024 habría violado el reglamento vigente.

**ASI dice:** 0/5, 0/4, 0/5. Ninguna unidad atómica conservó soberanía. La absorción puede ser ordenada y, al mismo tiempo, dejar ASI bajo: esa es la lección de la v2, y los números la confirman condición por condición.

**ACO-A dice:** la absorción existe (7 bancos, proceso competitivo, balance de exclusión en 15 días), pero sus números no cierran para las unidades grandes. El tope del FGD cubre el 0.011% de la exposición del IPS. El embargo total es del tamaño de una sola megacuenta contable. Y Δ no se puede estimar: no hay serie de absorción en el tiempo.

**El muro dice:** 5 eventos negativos, 0 positivos. Colapso predicho y ocurrido; nadie con la diversidad para saltar. Y por la definición vigente (b < 0) tampoco hay salto en ninguna ventana: los dos instrumentos coinciden en el resultado, aunque la conexión entre ellos sigue siendo pregunta abierta.

**Qué sorprende:**
- La meseta: la captura se detuvo sola, por saturación del canal (IPS en 9.70% de su cartera, tope 10%, sin nuevas colocaciones en 2026), no por intervención. El hub tocó techo.
- El FX: a 6,000 los totales del sistema reproducen exactos, pero los de Ueno no — los anclajes se publicaron con tipos de cambio distintos por periodo. R(t) apenas se mueve (≤0.010); los totales, hasta 12.9%.
- El b IPS de 2.93 se reproduce en r_ips (2.934), no en participaciones (2.75): la variable elegida, no solo la ventana, cambia b. Otra razón para reportar siempre variable + ventana + origen.
- La caída de dic 2025 (Ueno −12.5%, R 0.264→0.228) no la comenta ningún documento. Queda registrada, sin explicación.

**Qué queda sin resolver:** el inicio de la malversación (solo el Informe BCP/P N.° 016); la serie mensual de patrimonio efectivo (Roche-C al mes); la serie de absorción por receptor y en el tiempo (Δ); la reconciliación entre los 5 eventos positivos y el leapfrog vigente (b < 0); el 35% de las salvadoras, que implica un patrimonio efectivo (Gs 2.59 billones) por encima de los cierres documentados.

## 12. Huecos y límites

- **Malversación:** inicio no fechable con R(t) ni con estos datos. Solo el Informe BCP/P N.° 016 (precintado, Senado).
- **Roche-C mensual:** sin serie mensual de patrimonio efectivo.
- **Roche-S económico:** cruce no fechable con datos públicos (reporte sostenido por intangibles/fideicomiso/participaciones).
- **Δ de ACO-A:** sin serie temporal de A(τ). Sin montos absorbidos por receptor ni por fecha.
- **ASI = δH·α/F:** sin datos de eventos de comportamiento. Solo evaluación documental.
- **Diversificación de ahorristas individuales:** sin catastro de depositantes.
- **PDF MEF faltantes (15):** oct 2024, dic 2024–mar 2025, ene/mar 2026 y 2023. Sin ellos no hay OLS de 13 puntos sobre la ventana completa nov 2024–nov 2025 ni cierre de la meseta 2026.
- **Serie IPS:** solo valores del documento (CDA anual, cortes mar/sep 2026). Sin boletines mensuales descargados.
- **Balances de Ueno:** solo la cifra de mar 2026 del documento. Sin serie de patrimonio efectivo ni de depósitos del sector público según balance.
- **El b es sensible al origen de t y a la variable elegida** (r_ips vs participación; reloj nov 2024 vs reloj local). Todos los b de este informe llevan ventana, método, origen y n. Ningún b aquí prueba mecanismo ni φ→b.

## Apéndice A — Método y reproducibilidad

- **R(t):** recomputada desde `ueno_total_usd_equiv` y `total_sistema_usd_equiv` del CSV (FX 6,000 por fila; nov 2024 ancla del documento). Diferencia máxima con la columna R_t del CSV: 0.0002 (redondeo del ancla).
- **b:** OLS por mínimos cuadrados sobre log R vs log t (stdlib `math`, sin librerías externas). a = exp(intercepto). R² = 1 − SS_res/SS_tot.
- **Origen de t:** ventanas posteriores a nov 2024 usan t=1 en nov 2024 (reloj del documento); ventanas anteriores o que la cruzan usan t=1 en feb 2024 (inicio de la serie). La sensibilidad se reporta con el origen local como variante.
- **Roche-S:** solvencia reportada / 12%.
- **ASI:** evaluación documental condición por condición (5 condiciones × 3 unidades), con fuente por celda. Sin fórmula δH·α/F.
- **Script:** `/tmp/modelo_ueno.py`. Salida completa verificada dos veces (misma salida en ambas corridas; los valores de este informe coinciden con la salida del script).

## Apéndice B — Discrepancias encontradas al calcular (no corregidas en silencio)

1. **(c) meseta: n=8, no 10.** El encargo decía 10 puntos; los meses con R en dic 2025–sep 2026 son 8.
2. **(e) serie completa: n=24 con ancla / 23 solo PDF.** El encargo decía 23; coincide con la variante solo PDF. El ancla no mueve el ajuste (b 0.8133 vs 0.8136).
3. **Cruce de 0.20: ≈24 jun 2025 o ≈24 jul 2025 según convención** (inicio de mes vs fin de mes). Se adopta 24 jun 2025, convención del documento.
4. **b IPS 2.93: se reproduce en r_ips (2.934), no en participaciones (2.752) ni en montos (2.762).** El documento no especificaba la variable; ahora está identificada.
5. **Salvadoras 35% → patrimonio efectivo implícito Gs 2.59 billones**, por encima de los cierres documentados (1.56 en 2024; 2.20 en 2025; 1.8 al 31 oct 2025). Tensión registrada, no resuelta.
6. **Caída dic 2025:** Ueno −12.5% en USD (792.6M → 693.5M), R 0.264→0.228. Ningún documento la comenta.
7. **Embargo total (Gs 2.1005 billones) ≈ Derechos Fiduciarios (Gs 2.1057 billones), diferencia −0.25%.** Coincidencia aritmética registrada; componentes distintos en definición.
8. **(a) extremo a extremo:** 0.356 con anclajes del documento vs 0.342 con valores CSV (diferencia por el FX del ancla nov 2025: R 0.274 doc vs 0.2643 CSV).
