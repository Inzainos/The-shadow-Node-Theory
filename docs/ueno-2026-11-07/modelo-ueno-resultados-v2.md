# COPIA DE REGISTRO — Ueno v3 (corrección 2026-11-09)
# Archivo original: snt-taxonomia/modelo-ueno-resultados-v2.md
# Versión: v2
# Estado: archivo de registro — SIN CAMBIOS respecto al original. Cuerpo intacto; solo se añadió esta cabecera.
# Fecha de la copia: 2026-11-09
# md5 original: 986d79b469c031dc345638347b5bb616
# sha256 original: 1fb86198531f4a5cd7cf86f768528879f540601be62564dd3251d399406697e1
#
# Inyección al modelo SNT — caso Ueno Bank: resultados v2 (BACKCAST)

**Fecha:** 2026-11-06/07. **Tabla:** `tabla-maestra-ueno-mef.csv` CORREGIDA (45 filas, ene 2023 – sep 2026; 38 PDFs), **adoptada tras verificación independiente de Mole**. **Marco:** SNT v2.7.5.1 (README del repo, marco v34). **Método:** Python stdlib, script `/tmp/modelo_ueno_v2.py` (reproducible; dos corridas idénticas, misma salida y mismo CSV de valores). **Fuentes:** tabla maestra corregida + NOTAS corregidas (§§1–12), documento base de adquisición, parteaguas v2, backcast Roche (tres ratios), notas de trabajo (parteaguas, backcast-Roche, taxonomía por dominio). **Versión v1:** `modelo-ueno-resultados.md` — queda intacta como registro; sus números quedan RETIRADOS donde esta versión los cambia (ver tabla abajo).

## Tabla de cambios v1 → v2 (lo que cambia, con el motivo)

| # | Qué | v1 | v2 | Motivo |
|---|---|---|---|---|
| 1 | R nov 2024 | 0.110 (ancla del documento; R recalculada 0.1098) | **0.0963** (PDF) | El ancla mezclaba tipos de cambio: Ueno ≈6,696, sistema ≈7,793. Con tipo de cambio único, R = 0.0963 (0.0965 a FX 7,793; sensibilidad 0.0002). |
| 2 | Meses con R | 24 (23 PDF + 1 ancla) | **30 (todos PDF)** | Nuevos: oct 2024 (0.0780), dic 2024 (0.1021), ene 2025 (0.1094), feb 2025 (0.1253), mar 2025 (0.1315), ene 2026 (0.2132). La diferencia máxima R_csv vs R_recalculada es ahora 0.0000 (antes 0.0002 por el redondeo del ancla). |
| 3 | Cruce Roche-R (R > 0.10) | Nov 2024 (R = 0.110); ventana sep–nov 2024 (oct sin PDF) | **Dic 2024 (R = 0.1021)**; ventana nov–dic 2024 (ambos meses con PDF) | R nov 2024 corregido a 0.0963 < 0.10. La ventana queda cerrada a un mes exacto, sin interpolación a día. |
| 4 | b (a) extremo a extremo | 0.356 (anclajes doc) / 0.342 (CSV) — **RETIRADO** | **0.383** (R 0.1021 → 0.2643, t=1→12) | El 0.356 era un artefacto del ancla con FX mezclado. Ventana nueva: dic 2024 – nov 2025. |
| 5 | b (a) OLS ventana completa | No existía (el 0.906 era solo el tramo abr–nov) | **0.436** (R² = 0.873, n=12, t=1 dic 2024) | Es el valor que debe citarse para la ventana dic 2024 – nov 2025. |
| 6 | b (a') referencia nov 2024 – nov 2025 corregida | No existía | Extremo **0.394**; OLS **0.451** (R² = 0.855, n=13, t=1 nov 2024) | Ventana de referencia con el ancla corregida. |
| 7 | b (b) local abr–nov 2025 | 0.906 (origen t=1 nov 2024, t=6..13) | **0.802** (origen t=1 dic 2024, t=5..12; R² = 0.957) | El 0.906 era un artefacto del origen de t: el mismo tramo da 0.906 con el origen viejo (reproducido: 0.9058) y 0.802 con el origen consistente de la ventana. Con origen local (t=1 abr 2025): 0.344, sin cambio respecto a v1. |
| 8 | b (c) meseta dic 2025 – sep 2026 | −0.046 (n=8, origen nov 2024, R² = 0.025) | **+0.031** (n=9, origen dic 2024, R² = 0.011); con origen viejo +0.032; con origen local +0.009 | Ene 2026 ahora tiene R (0.2132), n pasa a 9. El cambio de signo es ruido (R² ≈ 0.01 en las tres variantes): la conclusión no cambia — sin tendencia medible. |
| 9 | b (e) serie completa | 0.813 (n=24; variante solo PDF 0.814, n=23) | **0.819** (n=30, R² = 0.909) | 6 meses nuevos + ancla corregida. La variante (e') desaparece: ya no hay ancla, los 30 meses son PDF. |
| 10 | b IPS | 2.934 sobre r_ips | **Sin cambio: 2.934** (R² = 0.995, n=3) | La serie IPS no cambió. |
| 11 | Roche-C, entrada | Nov 2024 (IPS 1.06), mismo mes que Roche-R | **Nov 2024 (base IPS, 1.06)**; Roche-R pasa a dic 2024 | Las dos bandas ya no cruzan el mismo mes: Roche-C (IPS) en nov, Roche-R en dic. Base fondos totales nueva: dic 2024 **1.08**, dic 2025 **1.89**, mar 2026 **≈2.08**. |
| 12 | Roche-S | 1.251 / 1.208 / 1.154 / 0.463 | **Sin cambio** | La solvencia reportada no depende de la tabla. |
| 13 | ACO-A: USD 146M / PE | 39.8% (PE cierre 2025) | **39.8% (dic 2025) + 35.5% (PE abr 2026, nuevo)** | Nueva ancla PE abr 2026 (2,467,235M, implícita por el tope 20%). |
| 14 | ACO-A: salvadoras 35% → PE implícito | Gs 2.59 billones, por encima de los cierres (tensión) | **Gs 2.59 billones; +4.9% sobre el ancla abr 2026** (antes +17.6% sobre cierre 2025) | La tensión se reduce con el ancla nueva, no se resuelve (PE ago 2026 sin documentar). |
| 15 | ACO-A: exposición IPS / fondos Ueno sep 2026 | 41.8% (CSV) | **41.7%** | Corrección de redondeo de v1 (348.5/834.825625 = 0.4175). El 40.8% del documento no cambia. |
| 16 | Backcast: ventana de inicio | jul–nov 2024; mes focal nov 2024 | **jul–dic 2024; mes focal dic 2024** | La entrada a Roche-R es dic 2024. El salto de jul 2024 sigue como peldaño anterior. |
| 17 | Backcast: ventana sin precisar día | sep–nov 2024 (faltaba el PDF de oct 2024) | **Cerrada: oct 2024 tiene PDF (R = 0.0780)** | El cruce queda fechado al mes (nov–dic 2024). Sigue sin interpolarse a día. |
| 18 | Huecos: PDFs MEF faltantes | 15 | **7** (2023-01–05, 2024-08, 2026-03) | Recuperados 8 PDFs. |
| 19 | φ, ASI, muro, FGD 0.011%, embargo −0.25%, fondeo 91.75% | — | **Sin cambio** | Ninguno depende del ancla corregida. |

## Reglas aplicadas

- **b es descriptor de deriva dentro de una ventana**, nunca prueba de mecanismo ni de φ→b. Se reporta siempre con ventana + método + origen de t + n.
- **b ≥ 1 es banda descriptiva no clasificada**, NO prueba de superlinealidad.
- La malversación es **presunta, denunciada e investigada** (denuncia MEF 5 nov 2026, Gs 250,000M Caja Fiscal + Gs 123,838M intereses; imputación a 27 personas 4 nov 2026), no hecho declarado por sentencia. El trigger oficial fue **insuficiencia de solvencia**. El colapso es evento **exógeno** por clasificación de Elán; la deriva fue **endógena**.
- El **2 nov 2026 es fecha de detonante/reconocimiento, NO inicio del fallo**.
- Series MEF / ABC / IPS en columnas separadas, sin mezclar definiciones; FX 6,000 por fila; discrepancias como incertidumbre, nunca corregidas en silencio.
- Lo no calculable se marca como **hueco**, nunca se rellena.
- **Tres definiciones Roche-C/R/S del documento backcast** (la §9 de las NOTAS sigue mostrando la pregunta como abierta; el documento backcast es la autoridad).

## 1. R(t) — re-verificación desde las columnas del CSV

Definición: R(t) = fondos públicos en Ueno / fondos públicos en el resto del sistema (total MEF − Ueno), en USD equivalentes a FX 6,000 por fila. **Ya no hay ancla del documento: los 30 meses con R son PDF.**

Recomputada fila por fila como `ueno_total_usd_equiv / (total_sistema_usd_equiv − ueno_total_usd_equiv)`, con verificación cruzada desde los componentes crudos (USD×6,000 + Gs):

| Fecha | R(t) CSV | R(t) recalculada | Diferencia | Fuente |
|---|---|---|---|---|
| 2024-02 | 0.0284 | 0.0284 | +0.0000 | MEF PDF |
| 2024-03 | 0.0319 | 0.0319 | +0.0000 | MEF PDF |
| 2024-04 | 0.0332 | 0.0332 | +0.0000 | MEF PDF |
| 2024-05 | 0.0346 | 0.0346 | +0.0000 | MEF PDF |
| 2024-06 | 0.0338 | 0.0338 | +0.0000 | MEF PDF |
| 2024-07 | 0.0610 | 0.0610 | +0.0000 | MEF PDF |
| 2024-09 | 0.0777 | 0.0777 | +0.0000 | MEF PDF |
| 2024-10 | 0.0780 | 0.0780 | +0.0000 | MEF PDF (nuevo) |
| 2024-11 | 0.0963 | 0.0963 | +0.0000 | MEF PDF (corregido; v1: ancla 0.110) |
| 2024-12 | 0.1021 | 0.1021 | +0.0000 | MEF PDF (nuevo) |
| 2025-01 | 0.1094 | 0.1094 | +0.0000 | MEF PDF (nuevo) |
| 2025-02 | 0.1253 | 0.1253 | +0.0000 | MEF PDF (nuevo) |
| 2025-03 | 0.1315 | 0.1315 | +0.0000 | MEF PDF (nuevo) |
| 2025-04 | 0.1396 | 0.1396 | +0.0000 | MEF PDF |
| 2025-05 | 0.1628 | 0.1628 | +0.0000 | MEF PDF |
| 2025-06 | 0.1706 | 0.1706 | +0.0000 | MEF PDF |
| 2025-07 | 0.2079 | 0.2079 | +0.0000 | MEF PDF |
| 2025-08 | 0.2457 | 0.2457 | +0.0000 | MEF PDF |
| 2025-09 | 0.2467 | 0.2467 | +0.0000 | MEF PDF |
| 2025-10 | 0.2670 | 0.2670 | +0.0000 | MEF PDF |
| 2025-11 | 0.2643 | 0.2643 | +0.0000 | MEF PDF |
| 2025-12 | 0.2280 | 0.2280 | +0.0000 | MEF PDF |
| 2026-01 | 0.2132 | 0.2132 | +0.0000 | MEF PDF (nuevo; v1: serie ABC sin total) |
| 2026-02 | 0.2357 | 0.2357 | +0.0000 | MEF PDF |
| 2026-04 | 0.2543 | 0.2543 | +0.0000 | MEF PDF |
| 2026-05 | 0.2254 | 0.2254 | +0.0000 | MEF PDF |
| 2026-06 | 0.2246 | 0.2246 | +0.0000 | MEF PDF |
| 2026-07 | 0.2306 | 0.2306 | +0.0000 | MEF PDF |
| 2026-08 | 0.2161 | 0.2161 | +0.0000 | MEF PDF |
| 2026-09 | 0.2395 | 0.2395 | +0.0000 | MEF PDF |

**Resultado: la serie reproduce el CSV exactamente.** Diferencia máxima 0.0000 (v1: 0.0002 por el redondeo del ancla, que ya no existe). Participación de Ueno reproduce igual. **30 meses con R calculable, todos con PDF.** Valores clave confirmados: feb 2024 0.028, jul 2024 0.061, sep 2024 0.078, oct 2024 0.078, nov 2024 0.096, dic 2024 0.102, nov 2025 0.264, meseta 2026 0.213–0.254.

**Huecos (R no calculable):** ene–may 2023 y ago 2024 (sin PDF), mar 2026 (sin total del sistema), todo 2023 (Ueno sin fila individual o dentro de OTROS BANCOS), ene 2024 (USD de Ueno dentro de OTROS BANCOS). No se imputa nada.

**Observaciones registradas, no ajustadas:** salto jul 2024 (R 0.034→0.061, +80.5% en un mes); USD de Ueno feb–mar 2024 casi idéntico (+USD 16) mientras Gs sube — posible cifra arrastrada; caída dic 2025 (Ueno −12.5% en USD, R 0.264→0.228) mientras el sistema sube — el documento no la comenta. **Nuevo:** la planicie feb–jun 2024 (R 0.028–0.035) queda rota en jul 2024 y nunca se recupera; oct 2024 (0.0780) muestra que entre sep y nov la subida fue gradual (0.0777 → 0.0780 → 0.0963), no un salto de un mes: el cruce de 0.10 se preparó en dos meses, no se produjo de golpe.

## 2. b — descriptor de deriva por ventana (OLS log-log: log R = log a + b log t)

Tabla de lectura del Módulo 0 (README): b < 0 convergencia / leapfrog; −0.1 < b ≤ 0.05 estado estacionario; 0.05 < b ≤ 0.3 satelización gradual; 0.3 < b < 1 satelización activa; b ≥ 1 banda descriptiva no clasificada.

| # | Ventana | Método | Origen de t | n | b | a | R² | Lectura (Módulo 0) |
|---|---|---|---|---|---|---|---|---|
| (a) | dic 2024 → nov 2025 | Extremo a extremo, valores CSV (R 0.1021 → 0.2643) | t=1 dic 2024 | 2 | **0.383** | — | — | Satelización activa |
| (a-OLS) | dic 2024 → nov 2025 | OLS log-log | t=1 dic 2024 | 12 | **0.436** | 0.0829 | 0.873 | Satelización activa — **valor a citar para la ventana** |
| (a') | nov 2024 → nov 2025 (corregida) | Extremo a extremo, valores CSV (R 0.0963 → 0.2643) | t=1 nov 2024 | 2 | **0.394** | — | — | Satelización activa |
| (a'-OLS) | nov 2024 → nov 2025 (corregida) | OLS log-log | t=1 nov 2024 | 13 | **0.451** | 0.0749 | 0.855 | Satelización activa |
| (b) | abr – nov 2025 | OLS log-log | t=1 dic 2024 (t=5..12) | 8 | **0.802** | 0.0385 | 0.957 | Satelización activa (pendiente local, 2ª mitad) |
| (b') | abr – nov 2025 | OLS log-log (sensibilidad origen local) | t=1 abr 2025 | 8 | **0.344** | 0.1316 | 0.942 | Satelización activa |
| (b'') | abr – nov 2025 | OLS log-log (origen viejo, reproduce v1) | t=1 nov 2024 (t=6..13) | 8 | **0.906** | 0.0278 | 0.955 | El 0.906 de v1 era el origen, no los datos |
| (c) | dic 2025 – sep 2026 (meseta) | OLS log-log | t=1 dic 2024 (t=13..22) | 9 | **+0.031** | 0.2101 | 0.011 | Estado estacionario |
| (c') | dic 2025 – sep 2026 (meseta) | OLS log-log (sensibilidad origen local) | t=1 dic 2025 | 9 | **+0.009** | 0.2266 | 0.013 | Estado estacionario |
| (c'') | dic 2025 – sep 2026 (meseta) | OLS log-log (origen viejo, compara v1) | t=1 nov 2024 (t=14..23) | 9 | **+0.032** | 0.2088 | 0.011 | Estado estacionario |
| (d) | feb – jul 2024 (pre-Roche) | OLS log-log | t=1 feb 2024 (t=1..6) | 6 | **0.288** | 0.0262 | 0.503 | Satelización gradual (ajuste débil) |
| (e) | feb 2024 – sep 2026 (completa) | OLS log-log | t=1 feb 2024 (calendario) | 30 | **0.819** | 0.0158 | 0.909 | Satelización activa (resumen grueso) |
| (IPS) | 2023 – 2025 (anual) | OLS log-log sobre r_ips (0.0101, 0.0917, 0.2453) | t=1 2023 | 3 | **2.934** | 0.0106 | 0.995 | b ≥ 1 banda descriptiva no clasificada |

**El origen de t sigue siendo la advertencia central (ahora con un caso más):** el mismo tramo abr–nov 2025 da 0.802 (origen dic 2024), 0.906 (origen nov 2024) y 0.344 (origen local abr 2025). Tres números, un tramo, tres relojes. La meseta da +0.031, +0.032 y +0.009 según el origen — todas ≈ 0 con R² ≈ 0.01, así que la conclusión (sin tendencia) no depende del reloj, pero el signo sí: con R² = 0.01 el signo de b en la meseta es ruido, no señal. En v1 la meseta daba −0.046; el cambio de signo al añadir ene 2026 (R = 0.2132, el punto más bajo de la meseta, al inicio de la ventana) confirma que ese número no es estable. **b depende del reloj elegido**: es un descriptor de la ventana con su origen declarado, no una constante intrínseca del sistema.

**Verificación del b IPS del documento (2.93):** sin cambio respecto a v1. OLS log-log sobre **r_ips** (0.0101, 0.0917, 0.2453; t=1,2,3) da **b = 2.934, R² = 0.995** — reproduce el 2.93. Sobre participaciones (1.0%, 8.4%, 19.7%) da 2.752 (R² = 0.992) y sobre montos en Gs da 2.762 (R² = 0.994). **Conclusión: el 2.93 es el ajuste sobre r_ips (la forma de razón, coherente con R(t)), no sobre participaciones.** En cualquier caso b ≥ 1 es banda descriptiva no clasificada (n=3 puntos anuales); NO es prueba de superlinealidad.

**Lectura conjunta de b (corregida):** la deriva no fue uniforme. Antes de Roche (feb–jul 2024) era gradual (b ≈ 0.29, R² = 0.50 — ajuste débil, dominado por el salto de jul 2024). En la ventana dic 2024–nov 2025 fue activa (b ≈ 0.44 por OLS, 0.38 de extremo a extremo), y dentro de ella la segunda mitad se empinó (b local ≈ 0.80 con el origen consistente, R² = 0.96). Después de nov 2025 la deriva se detuvo: la meseta tiene b ≈ +0.03 con R² = 0.01, es decir, **sin tendencia medible**. El ajuste de toda la serie (b ≈ 0.82, R² = 0.91) resume tres regímenes distintos en un solo número y no debe usarse solo: esconde el salto, la aceleración y la meseta. **La corrección suaviza la historia, no la invierte:** la ventana completa pasa de 0.906 (que era solo el tramo abr–nov con otro origen) a 0.436; la deriva sigue siendo satelización activa, pero menos empinada de lo que decía v1.

## 3. Roche-R (relativa): R(t) > 0.10

- **Primer mes con R > 0.10: dic 2024 (R = 0.1021).** Mes anterior con dato: nov 2024 (0.0963); anterior: oct 2024 (0.0780). **Ventana de cruce: nov–dic 2024** — ambos meses tienen PDF; el cruce queda fechado al mes, sin interpolación a día (los datos son mensuales).
- **Variaciones mensuales del cruce:** nov → dic 2024: **+6.0%** (0.0963 → 0.1021); dic 2024 → ene 2025: **+7.1%** (0.1021 → 0.1094). El cruce no fue un salto: fue el tercer mes consecutivo de subida (sep 0.0777 → oct 0.0780 → nov 0.0963 → dic 0.1021).
- **Cruce de 0.20:** entre jun 2025 (0.1706) y jul 2025 (0.2079). Interpolación lineal, fracción 0.788: con la convención del documento (valores al inicio del mes) ≈ **24 jun 2025**; con convención de fin de mes ≈ 24 jul 2025. La diferencia es un artefacto de convención, no de los datos. Se adopta ≈24 jun 2025 (misma convención del documento y de la verificación previa). Sin cambio respecto a v1.
- R(t) se mantuvo > 0.10 en todos los meses con dato desde dic 2024 hasta sep 2026. Mínimo después del mes del cruce: 0.1094 (ene 2025). No hay retorno por debajo de Roche-R en la serie.

## 4. Roche-C (concentración): fondos públicos en Ueno / patrimonio efectivo > 1.0

Dos bases, sin mezclar. La base IPS es la del documento backcast (sin cambio). La base fondos totales es nueva en v2: se calcula desde el CSV (fondos a FX 6,000) y las anclas de patrimonio efectivo de NOTAS §12.

**Base IPS (backcast §5, fuentes ABC/Asoban/EEFF):**

| Momento | Fondos en Ueno | Patrimonio efectivo | Roche-C | Fuente |
|---|---|---|---|---|
| Nov 2024 | IPS Gs 1.7 billones | Gs 1.6 billones | **1.06** | ABC 2026-01-28 / 2026-07-12 |
| Cierre 2024 | IPS Gs 1,766 billones | Gs 1.56 billones | **1.13** | ABC 2026-07-12 / 2026-07-14 |
| 31 oct 2025 | IPS Gs 2.1 billones | Gs 1.8 billones | **1.17** | ABC 2025-12-30 |
| Cierre 2025 | IPS Gs 2.24 billones | Gs 2.20 billones | **1.02** | ABC 2026-07-12 |

**Base fondos públicos totales (CSV a FX 6,000 + anclas PE de NOTAS §12):**

| Momento | Fondos en Ueno (CSV) | Patrimonio efectivo | Roche-C | Nota |
|---|---|---|---|---|
| Dic 2024 | Gs 1.687 billones (USD 281.2M) | Gs 1.56 billones | **1.08** | Mismo mes que Roche-R |
| Dic 2025 | Gs 4.161 billones (USD 693.5M) | Gs 2.20 billones | **1.89** | NOTAS §12 dice 1.91 con 4.2 billones redondeados; aquí 4.161 exactos del CSV |
| Mar 2026 | Gs 5.133 billones (USD 855.6M, Tesoro/ABC) | Gs 2.467 billones (ancla abr 2026) | **≈2.08** | Aproximado: el PE es de abr 2026, no de mar 2026. NOTAS §12 dice ≈2.2 con 5.2/2.4 redondeados |

**Entrada a Roche-C: nov 2024** (base IPS, 1.06). En base fondos totales el primer punto computable es dic 2024 (1.08), mismo mes que Roche-R. Con el PE de dic 2024 como proxy, nov 2024 en base fondos totales daría ≈1.15 (1.792/1.56) — eso es un **supuesto** (PE de dic aplicado a nov), no una medición; se registra como tal y no se usa como fecha de entrada.

**HUECO: la serie mensual de Roche-C NO es calculable.** El patrimonio efectivo solo existe en anclas fechadas (dic 2023: 337,228M; dic 2024: 1.56 billones; oct 2025: 1.8 billones; dic 2025: 2.20 billones; ene 2026: >USD 335M; abr 2026: 2.467 billones implícito por el tope 20%). Sin serie mensual de patrimonio efectivo no se puede fechar el cruce al mes con más precisión que nov 2024 (base IPS), ni calcular su trayectoria entre los puntos. Sigue sin cambio respecto a v1.

**Discrepancia dic 2024 (registrada, no resuelta):** hay cuatro cifras de fondos públicos totales para dic 2024 — PDF a FX 6,000: Gs 1.687 billones → Roche-C 1.08; balance 2024 (sector público): Gs 1.740 billones → 1.12; Asoban vía ABC: Gs 1.747 billones → 1.12; ABC citado: Gs 1.76 billones → 1.13. NOTAS §12 explica que 1.76 es el mismo saldo convertido a otro tipo de cambio (≈6,300), no una cifra distinta del PDF. **Las cuatro dan Roche-C entre 1.08 y 1.13, todas > 1.0: la conclusión (cruce en dic 2024) no depende de cuál se elija.** Se usa 1.08 (PDF a FX 6,000) como valor primario por ser el único con componentes verificables en la tabla.

## 5. Roche-S (solvencia): solvencia reportada / mínimo legal 12% < 0.50

Sin cambio respecto a v1.

| Fecha | Solvencia reportada | Roche-S | Fuente |
|---|---|---|---|
| Mar 2026 | 15.01% | **1.251** | Parteaguas v2 §1.4 [19][22] |
| Jun 2026 | 14.5% | **1.208** | Parteaguas v2 §1.4 [19][22] |
| Sep 2026 | 13.85% | **1.154** | Parteaguas v2 §1.4 [19][22] |
| 2 nov 2026 | 5.56% | **0.463** | BCP, resolución (Ley 2334/03 art. 13 inc. b) |

La solvencia reportada se mantuvo **por encima del mínimo (Roche-S > 1) hasta sep 2026**. El cruce económico de Roche-S **no es fechable con datos públicos**: entre sep y nov 2026 el reporte pasó de 13.85% a 5.56% tras previsiones > Gs 1.6 billones (inspección 31 oct), pero el reporte estaba sostenido por intangibles (Gs 761,444M), Derechos Fiduciarios (Gs 2,105,743M) y Participaciones (+8,000% en 2025), saldos de cierre 2025 sin fecha mensual. **El 2 nov 2026 es el reconocimiento legal de Roche-S (0.463 < 0.50), no su cruce económico.**

## 6. φ — captura normativa en 5 pasos (mecanismo)

Sin cambio respecto a v1. φ no es una métrica con unidad; es la **trazabilidad normativa** del desplazamiento: qué actos retiraron luz, cuándo, con qué observable.

| # | Paso (φ) | Fecha | Observable (fuente) |
|---|---|---|---|
| 1 | Licitación: puntaje mínimo **65 → 60** (v1 decía 70 → 60, sin fecha; v2 lo corrige y fecha) | **9 nov 2023** | ABC 2023-11-10; parteaguas v2 §3.1 [14]. R no se mueve: es pre-condición, no inicio. |
| 2 | IPS Res. C.A. N.° 093-046/2024: **eliminación del límite de patrimonio efectivo** | **12 nov 2024** | Parteaguas v2 §3.2 [15]. Mismo paso también baja la calificación requerida (A-Py strong trend → genérica A). |
| 3 | Gastos de fusión activados como **activo fiduciario**: aumento de Derechos Fiduciarios de Gs 0 a Gs 2.1 billones, 99.44% del patrimonio neto | 2025 | EEFF 2025 (Asoban); parteaguas v2 §3.3 [17]. |
| 4 | **No-desagregación del software** tolerada: activos intangibles +Gs 654,799M (2024–2025) | 2025 | EEFF 2025 (Asoban); parteaguas v2 §3.4 [18]. |
| 5 | **Reserva supervisora mantenida** (solicitud de constituir previsiones no ejecutada) | Jun – oct 2026 | Supervisión (8 jun 2026) [20]; acta BCP (19 jun 2026) [19]; Rivarola (10 jul 2026) [22]. |

Las φ son **causas formales**: cada paso retiró luz. Ninguna es causa mecánica por sí sola, ni una variable continua en una ecuación. **φ no fue cuantificado como campo continuo** (el estado actual del marco lo postula por dominio, no lo mide).

**φ contable (v2):** Gs 2.5 billones de gastos de fideicomiso + Gs 2.6 billones de cartera morosa mal clasificada como vigente. Sin cambio respecto a v1.

## 7. ASI — Índice de Soberanía Atómica (evaluación documental)

Definición (parteaguas v2 §3): ASI designa el Índice de Soberanía Atómica. **No es un seguro ni un mecanismo de absorción.** Mide cuánto control conserva la unidad atómica (depositante, jubilado, organismo) cuando el hub falla. Condiciones (alto ASI): puede elegir banco; puede retirar/transferir sin permiso del hub; tiene información veraz; puede recuperar a tiempo; puede diversificar.

Evaluación documental (sin cambio respecto a v1):

| Condición (alto ASI) | Jubilados (IPS) | Ahorristas (FGD) | OEE (MEF) |
|---|---|---|---|
| Puede elegir banco | **No** — CDA por licitación, sin opción individual | **No** — el banco elegido por el hub fue Ueno | **No** — Tesoro por licitación, sin opción individual |
| Puede retirar/transferir sin permiso del hub | **No** — fondos congelados al 2 nov | **No** — fondos congelados al 2 nov | **No** — fondos congelados al 2 nov |
| Tiene información veraz | **No** — reporte 13.85% ocultaba previsiones | **No** — reporte 13.85% ocultaba previsiones | **No** — reporte 13.85% ocultaba previsiones |
| Puede recuperar a tiempo | **No** — FGD hasta 75 SM, pago escalonado (adelanto Gs 10M en 72h; Ley 7745/2026) | **No** — FGD hasta 75 SM (Gs 228,300,000), pago escalonado | **No** — recuperación vía proceso de exclusión (balance máx. 15 días) |
| Puede diversificar | **No** — CDA concentrado en Ueno (19.7% Gs, 19.95% USD del IPS) | **Sin datos** — diversificación individual no medida | **No** — Tesoro concentrado en Ueno (R 0.24) |

**Conteo: jubilados 0/5, ahorristas 0/4 (+1 sin datos), OEEs 0/5. ASI bajo en las tres unidades.** Sin cambio respecto a v1.

**La fórmula del repo (ASI = δH·α/F, README) NO se calculó**: requiere datos de eventos de comportamiento (δH = cambio de entropía de la distribución de decisiones, α = tasa de adaptación, F = energía libre) y no existe serie de eventos para Ueno. La evaluación documental es un conteo de condiciones, no la fórmula. **No se afirma equivalencia entre la fórmula del repo y el conteo documental**: es una pregunta abierta para Elán.

## 8. ACO-A — absorción por oferta competitiva y adjudicación

**Criterio de ACO-A (README):** extinción funcional de la unidad + absorción identificable por otro proceso. **Criterio cumplido** (sin cambio): 2 nov 2026, resolución de solvencia 5.56% < 12% (Ley 2334/03 art. 13 inc. b); proceso de exclusión con 7 bancos licitantes y balance de exclusión en un plazo máximo de 15 días.

**Δ NO es estimable** (sin cambio): la fórmula requiere A(τ) (masa/actividad de la unidad) en el tiempo y no hay serie temporal de A(τ) para Ueno. Lo que hay son saldos de cierre y anclas.

**Modo de colapso (juicio descriptivo, no medición): Acantilado Catastrófico** con rasgos de **Craquelado** — la solvencia reportada pasó de 13.85% (sep 2026) a 5.56% (2 nov 2026) en ~1 mes, tras una fase de fracturas acumuladas (provisionamiento, reservas mantenidas, fideicomiso). Sin cambio respecto a v1.

**Aritmética (actualizada con las anclas nuevas de NOTAS §12):**

- FGD / exposición IPS (sep 2026): Gs 228,300,000 / Gs 2.03 billones = **0.011%** (sin cambio).
- Anticipo FGD Gs 10,000,000 = **4.38% del tope** (sin cambio).
- **Exposición IPS / fondos Ueno (sep 2026): doc 40.8% (348.5/855); CSV 41.7% (348.5/834.8).** v1 decía 41.8% por redondeo; la corrección es 0.1 pp. La discrepancia doc/CSV (40.8% vs 41.7%) refleja la diferencia de total (855M vs 834.8M a FX 6,000), no un error de cálculo.
- **USD 146M vinculados / patrimonio efectivo: 39.8% con PE cierre 2025 (Gs 2.2 billones = USD 366.7M) y 35.5% con PE abr 2026 (Gs 2,467,235M = USD 411.2M).** El 35.5% es nuevo (ancla abr 2026, más contemporánea al periodo sep 2025–may 2026 del excedente). En ambos casos ≈1.8–2× el tope del 20% (el tope es USD 73M con PE 2025 o USD 82.2M con PE abr 2026; el excedente es USD 146M).
- **Salvadoras:** deudas Gs 905,825M = 35% del patrimonio efectivo → PE implícito **Gs 2.588 billones**. Contra el ancla abr 2026 (Gs 2.467 billones): **+4.9%**. Contra el cierre 2025 (Gs 2.20 billones): +17.6%. **La tensión se reduce con el ancla nueva** (v1 solo tenía el cierre 2025), pero no se resuelve: el PE de ago 2026 (fecha de la cifra de salvadoras) no está documentado, y el PE implícito sigue por encima de todos los cierres conocidos.
- Fondeo dic 2024–mar 2025 no a préstamos: depósitos +Gs 1,755,304M (+17%), crédito neto +Gs 144,737M (+2%) → **91.75% del fondeo incremental no fue a préstamos** (144,737/1,755,304 = 8.25% a préstamos). Sin cambio respecto a v1.
- **Embargo total (Gs equivalente):** USD 70M + Gs 1,621,853,458,972 + Gs 58,639,000,000 = **Gs 2.1005 billones** (a FX 6,000). vs Derechos Fiduciarios Gs 2.105743 billones: **−0.25%**. Coincidencia numérica, registrada como tal (sin cambio).
- **Nuevo dato (NOTAS §12):** la diferencia entre la cifra de fondos totales de dic 2024 y la de mar 2026 (Gs 1.687 → 5.133 billones) es +Gs 3.446 billones en 15 meses, mientras el PE pasó de 1.56 a 2.467 billones: Roche-C en base fondos totales subió de 1.08 a ≈2.08. El hub se endeudó con fondos públicos más rápido de lo que creció su capital.

## 9. El muro de 5 eventos — lectura por φ

**Guarda:** el muro de 5 eventos existe en el repo (v30) como criterio de escape de la satelización (mínima diversidad funcional); el muro-por-φ es una **aplicación de Elán al caso Ueno** y una **propuesta** (lectura bipolar), no una redefinición. **Leapfrog NO se redefine**: sigue siendo el salto por b < 0 al Nivel Exógeno (README Módulo 0: b < 0 = Convergencia / leapfrog).

**Negativos (φ): 5/5.** Los 5 pasos de φ (§6) son los 5 eventos negativos del muro: (1) puntaje 65→60 (9 nov 2023); (2) eliminación del límite de PE (12 nov 2024); (3) gastos de fusión como activo fiduciario; (4) no-desagregación del software; (5) reserva supervisora mantenida. El muro predice colapso; el colapso ocurrió (2 nov 2026).

**Positivos (condiciones de ASI alto): 0/5 (jubilados), 0/4 (ahorristas, +1 sin datos), 0/5 (OEEs).** Ninguna unidad atómica alcanza el salto bajo la definición vigente de leapfrog (b < 0). **Convergencia observada:** ninguna ventana muestra b < 0 significativo — ni la meseta (b ≈ +0.03, R² = 0.01) ni la serie completa (b ≈ 0.82). El muro y b **coinciden en el resultado** (nadie escapó) sin resolver aún la conexión entre ambos: la hipótesis de reconciliación (los eventos positivos son acciones que bajan R(t), es decir, b < 0) sigue siendo **HIPÓTESIS, no establecida**.

## 10. Las bandas determinan el colapso

**Hipótesis de trabajo (Elán):** cuando se cruza el ratio de Roche, las bandas cruzadas — una, dos, tres — determinan cómo se despliega el colapso. En Ueno se cruzaron las tres; el resultado fue colapso total con trigger legal. Las lecturas de una o dos bandas son **hipótesis de trabajo, no mediciones**.

| Banda | Definición | Cruce | Valor |
|---|---|---|---|
| Roche-C | Fondos públicos / PE > 1.0 | **Nov 2024** (base IPS, 1.06); dic 2024 (base fondos totales, 1.08) | 1.06 / 1.08 |
| Roche-R | R(t) > 0.10 | **Dic 2024** (R = 0.1021) | 0.1021 |
| Roche-S | Solvencia / 12% < 0.50 | **2 nov 2026** (reconocimiento legal, 0.463) | 0.463 |

**Corrección clave de v2:** Roche-C y Roche-R **ya no cruzan el mismo mes**. Roche-C (base IPS) cruzó en nov 2024; Roche-R en dic 2024. La entrada a Roche-R coincide con el mes en que empieza la captura masiva en CDA (dic 2024–mar 2025: +Gs 1,755,304M en depósitos con crédito neto +2%). La secuencia corregida es: **nov 2024 — concentración (Roche-C, IPS); dic 2024 — ruptura relativa (Roche-R) + captura masiva; nov 2026 — reconocimiento legal (Roche-S)**. Dos años entre la entrada a Roche (nov–dic 2024) y el reconocimiento (nov 2026).

**Contrafactuales (hipótesis, no mediciones):** con solo Roche-C (concentración sin deriva relativa) el sistema podría haber estabilizado en una captura lenta; con Roche-C + Roche-R (sin Roche-S) la absorción habría sido ordenada pero sin trigger legal; con las tres, el colapso fue total con trigger legal y embargo. Ninguno de estos escenarios es medible con los datos disponibles.

## 11. Qué muestran los modelos (lectura corregida)

1. **La captura ocurrió en un año y luego se detuvo sola por saturación.** R pasó de 0.1021 (dic 2024) a 0.2643 (nov 2025), ×2.6 en 11 meses (b ≈ 0.44 por OLS). Después, b ≈ +0.03 (R² = 0.01): la meseta dic 2025–sep 2026 no tiene tendencia medible. El freno fue el tope del 10% del IPS (9.70% al 30 oct 2025; sin nuevas colocaciones en 2026), no una intervención. **Corrección: la ventana es dic 2024–nov 2025 (b 0.383/0.436), no nov 2024–nov 2025 (0.356 retirado).**
2. **La deriva tuvo tres regímenes y el número único los esconde.** Gradual (feb–jul 2024, b ≈ 0.29, ajuste débil) → activa (dic 2024–nov 2025, b ≈ 0.44; segunda mitad b ≈ 0.80) → meseta (dic 2025–sep 2026, b ≈ +0.03). El ajuste de toda la serie (b ≈ 0.82, R² = 0.91) es un resumen grueso: no debe citarse solo.
3. **El sistema entró en Roche en nov–dic 2024, dos años antes del reconocimiento.** Roche-C (IPS) en nov 2024, Roche-R en dic 2024. El 2 nov 2026 no fue la entrada: fue el reconocimiento legal (Roche-S 0.463). **La corrección separa las dos entradas en un mes; la lectura de fondo no cambia, pero la secuencia es más precisa: la concentración precedió a la ruptura relativa en un mes.**
4. **La entrada a Roche-R coincide con el mes de la captura masiva en CDA.** Dic 2024 es a la vez el mes del cruce (R = 0.1021) y el inicio de la avalancha de fondeo (dic 2024–mar 2025: +Gs 1,755,304M, 91.75% no a préstamos). El mes focal del backcast pasa de nov 2024 a **dic 2024**: un mes después del retoque normativo del 12 nov 2024 (Res. 093-046/2024) y el mes en que la captura se vuelve masiva. La causa formal (paso 2 de φ) precede al cruce en un mes; el cruce y la captura son simultáneos.
5. **Una absorción puede ser ordenada y dejar ASI bajo.** 7 bancos licitantes, balance de exclusión en 15 días, FGD pagando — y ASI 0/5, 0/4, 0/5 en las tres unidades. El orden del proceso no restauró el control atómico: el FGD cubre el 0.011% de la exposición del IPS.
6. **La caída de dic 2025 (Ueno −12.5% en USD, R 0.264→0.228) sigue sin explicación en ningún documento.** Se registra como hueco, no se interpreta.
7. **El b depende del reloj.** El tramo abr–nov 2025 da 0.802, 0.906 o 0.344 según el origen de t. Cualquier b debe citarse con ventana + método + origen + n. **El 0.906 de v1 era un artefacto del origen; el valor consistente con la ventana dic 2024–nov 2025 es 0.802.**

## 12. Huecos y límites (actualizado)

| Hueco | Estado |
|---|---|
| Inicio de la malversación | **Sin fechar.** El Informe BCP/P N.° 016 sigue sin aparecer en abierto. Lo que existe: **Nota BCP/P N.° 019** (directorio del BCP entregó la denuncia a Fiscalía con un informe de ~200 fojas) y un **informe sellado de 31 fojas al Senado** (respuesta a cinco pedidos de informes) que **NO precisa la fecha ni el monto total del exceso** en el límite de préstamos vinculados. Consecuencia: aunque apareciera el 016, es posible que tampoco fechara la malversación. El backcast fecha la **ruptura estructural** (nov–dic 2024), no el delito. |
| Roche-C mensual | **Sin serie.** El patrimonio efectivo solo existe en anclas (dic 2023, dic 2024, oct 2025, dic 2025, ene 2026, abr 2026). Sin serie mensual no hay trayectoria ni cruce al mes en base fondos totales (solo el primer punto computable, dic 2024). |
| ACO-A Δ | **Sin estimar.** No hay serie A(τ) para Ueno. |
| Leapfrog / reconciliación muro-b | **Pregunta abierta.** La hipótesis (eventos positivos = acciones que bajan R(t)) no está establecida. |
| Caída dic 2025 | **Sin explicación.** Ningún documento la comenta. |
| PDFs MEF faltantes | **7 meses:** 2023-01, 02, 03, 04, 05; 2024-08; 2026-03. (v1: 15.) |
| R(t) 2023 | Ueno sin fila individual o dentro de OTROS BANCOS; no se imputa. |
| PE ago 2026 | Sin documentar (fecha de la cifra de salvadoras). La tensión salvadoras se reduce con el ancla abr 2026 (+4.9%) pero no se resuelve. |
| ASI = δH·α/F | **Sin calcular.** Sin serie de eventos de comportamiento para Ueno. Equivalencia con el conteo documental: pregunta abierta para Elán. |
| Cruce económico de Roche-S | **No fechable** con datos públicos (solvencia reportada > 12% hasta sep 2026; salto a 5.56% en nov 2026 tras previsiones). |

## 13. El backcast v2 — la escalera desde el 2 nov 2026

El backcast es el recorrido inverso: desde el cruce del 2 nov 2026 hacia atrás, peldaño por peldaño, por las anomalías fechadas, hasta la ventana de inicio. Cada peldaño es un hecho documentado con fecha; la escalera no interpola entre peldaños.

| Peldaño | Fecha | Hecho | R(t) / ratio | Lectura |
|---|---|---|---|---|
| 12 | 3 nov 2026 | Embargo: USD 70M + Gs 1,621,853,458,972 + Gs 58,639,000,000 (Gs 2.1005 billones) contra U Paraguay S.A., U Holdings S.A.R.L., Grupo Vázquez S.A.E., Federico Miguel Vázquez Villasanti, Juan Manuel Gustale, Diana Leticia Mongelós González + cuatro directores | — | La cadena llega a los beneficiarios finales |
| 11 | 2 nov 2026 | **Resolución BCP: solvencia 5.56% < 12%. Roche-S = 0.463.** Trigger legal, reconocimiento. FGD: adelanto Gs 10M en 72h; IPS primero; ~32,000 jubilados a reubicar; 7 bancos licitan | R sep 2026: 0.2395 | **Punto de llegada del backcast, no su inicio** |
| 10 | 31 oct 2026 | Inspección BCP → previsiones > Gs 1.6 billones → 5.56% | — | La inspección hace visible la fragilidad acumulada |
| 9 | 10 jul 2026 | Memo Rivarola: contra vender cartera morosa a Vinanzas para simular el tope del 20% vinculado | — | φ paso 5 (reserva mantenida) documentado |
| 8 | 19 jun 2026 | Acta BCP: previsiones no ejecutadas | R jun 2026: 0.2246 | φ paso 5 |
| 7 | 8 jun 2026 | Informe de supervisión: solicitud de constituir previsiones | R jun 2026: 0.2246 | φ paso 5 |
| 6 | 29 abr 2026 | **Circuito salvadoras: Sagas → Kasas → Vinanzas → Itti → Grupo M.** Deudas Gs 905,825M ≈ USD 153M = 35% del PE; Sagas 3,000×, Kasas 800× vs resto del sistema | R abr 2026: 0.2543 | La sombra se mueve dentro del hub (fideicomiso interno) |
| 5 | dic 2024 – mar 2025 | **Avalancha de fondeo: depósitos +Gs 1,755,304M (+17%), crédito neto +Gs 144,737M (+2%). 91.75% del fondeo no fue a préstamos** | R dic 2024: 0.1021 → mar 2025: 0.1315 | Comportamiento post-Roche: el hub ya no presta, acumula |
| 4 | 2025 | Derechos Fiduciarios Gs 2,105,743M = 99.44% del patrimonio neto; Participación en otras sociedades +8,000% (Red Digital de Procesamientos Gs 640,468M; Red Digital Gs 236,231M); intangibles +Gs 654,799M | R nov 2025: 0.2643 | φ pasos 3 y 4: el balance se sostiene con saldos no líquidos |
| 3 | **dic 2024** | **Roche-R cruza 0.10 (R = 0.1021). Roche-C (fondos totales) = 1.08. Mes focal del backcast.** | **R = 0.1021** | **Entrada a Roche-R. Coincide con el inicio de la captura masiva en CDA (peldaño 5).** |
| 2 | nov 2024 | **Roche-C (base IPS) cruza 1.0 (1.06).** R = 0.0963 (corregido; antes 0.110) | R = 0.0963 | **Entrada a Roche-C.** La concentración precede a la ruptura relativa en un mes |
| 1 | 12 nov 2024 | **IPS Res. C.A. N.° 093-046/2024: eliminación del límite de patrimonio efectivo** (y baja de calificación requerida A-Py strong trend → genérica A) | R nov 2024: 0.0963 | **φ paso 2: la causa formal que habilita el cruce, un mes antes** |
| 0 | 9 nov 2023 | Licitación: puntaje mínimo 65 → 60 | R no se mueve | φ paso 1: pre-condición, no inicio |
| −1 | jul 2024 | **Salto: R 0.0338 → 0.0610 (+80.5%); Ueno total USD 104.4M → 186.4M (+78.5%). Fusión Visión efectiva 1 jul 2024; facilidades Gs 5.1 billones autorizadas 27 may 2024** | R = 0.0610 | **Peldaño anterior: el primer salto estructural, cinco meses antes de Roche-C** |

**Tres fechas corregidas (A/B/C) respecto al backcast v1:**

- **A — Entrada a Roche-C: nov 2024 (sin cambio).** Base IPS 1.06. Lo que cambia es que ya no comparte mes con Roche-R.
- **B — Entrada a Roche-R: dic 2024 (antes nov 2024).** R = 0.1021, con nov 2024 en 0.0963 y oct 2024 en 0.0780. La ventana de cruce es nov–dic 2024, cerrada al mes.
- **C — Mes focal del backcast: dic 2024 (antes nov 2024).** Es el mes en que (i) Roche-R cruza, (ii) Roche-C en base fondos totales cruza (1.08), (iii) empieza la captura masiva en CDA. Un mes después del retoque normativo del 12 nov 2024.

**Ventana de inicio corregida: jul–dic 2024.** El salto de jul 2024 es el peldaño anterior (cinco meses antes de Roche-C); la entrada a Roche es nov–dic 2024. **La lectura corregida: la entrada a Roche-R coincide con el mes en que empieza la captura masiva en CDA.** No hay interpolación a día: los datos son mensuales y el cruce se fecha al mes (nov–dic 2024), no a un día.

**Qué NO cambia en el backcast:** el 2 nov 2026 sigue siendo reconocimiento/trigger, no inicio; la malversación sigue sin fecha (solo el Informe BCP/P N.° 016 podría fecharla, y ni siquiera es seguro — ver §12); el salto de jul 2024 sigue siendo el primer peldaño estructural; los 5 pasos de φ siguen siendo los 5 eventos negativos del muro.

---

## Apéndice A — Método y reproducibilidad

- **Script:** `/tmp/modelo_ueno_v2.py` (stdlib; sin dependencias externas). Lee `tabla-maestra-ueno-mef.csv` (45 filas), recomputa R(t) desde los componentes (USD×6,000 + Gs) y desde las columnas `ueno_total_usd_equiv` / `total_sistema_usd_equiv`, ajusta b por OLS log-log (log R = log a + b log t) por ventana, calcula Roche-R/Roche-C/Roche-S y la aritmética ACO-A, y escribe `modelo-ueno-valores-v2.csv`.
- **Determinismo verificado:** dos corridas producen salida estándar idéntica y CSV idéntico (md5 `306d4a5cfdefebbadb6c43abb86d8349`).
- **Convención de t:** t es el mes calendario (meses desde el origen, con huecos cuando falta el PDF). **Origen nuevo para las ventanas posteriores a nov 2024: t=1 en dic 2024** (el mes del cruce de Roche-R). Las ventanas anteriores o que cruzan nov 2024 usan t=1 en feb 2024. La ventana de referencia nov 2024–nov 2025 usa t=1 en nov 2024. Cada b se reporta con su origen; la sensibilidad al origen se muestra con las variantes (b', b'', c', c'').
- **R(t) usa FX 6,000 por fila** (convención de la tabla). La sensibilidad a FX es ≤ 0.002 (verificada en la corrección: R nov 2024 = 0.0963 a FX 6,000, 0.0965 a FX 7,793).
- **Roche-C en base fondos totales** usa los fondos del CSV a FX 6,000 y las anclas de PE de NOTAS §12 (única fuente disponible; no hay serie mensual de PE).
- **Roche-S** usa las solvencias reportadas del parteaguas v2 (15.01% mar 2026, 14.5% jun, 13.85% sep, 5.56% 2 nov 2026).
- **b IPS** usa los tres puntos anuales de r_ips (0.0101, 0.0917, 0.2453; t=1,2,3).
- **Archivos v1 intactos:** `modelo-ueno-resultados.md` y `modelo-ueno-valores.csv` no se tocaron. **No se tocó** el espacio, el podcast, el CSV ni las NOTAS.

## Apéndice B — Discrepancias registradas (actualizado)

**Herencia de v1 (se mantienen):**

1. Meseta n=8 en el brief → **n=9 en v2** (ene 2026 ahora tiene R). La cifra de v1 (n=8) era correcta con los datos de v1.
2. Serie completa n=24 en v1 → **n=30 en v2** (6 meses nuevos + ancla corregida). La variante (e') desaparece (ya no hay ancla).
3. Cruce de 0.20: ≈24 jun 2025 (convención inicio de mes) vs ≈24 jul 2025 (fin de mes). Artefacto de convención; se adopta 24 jun 2025.
4. b IPS: 2.934 sobre r_ips vs 2.752 sobre participaciones vs 2.762 sobre montos. El 2.93 del documento es sobre r_ips.
5. Salvadoras 35% → PE implícito Gs 2.588 billones vs anclas conocidas (2.20 dic 2025, 2.467 abr 2026). Tensión reducida (+4.9% vs abr 2026) pero no resuelta.
6. Caída dic 2025 (Ueno −12.5% en USD, R 0.264→0.228): ningún documento la comenta.
7. Embargo Gs 2.1005 billones ≈ Derechos Fiduciarios Gs 2.105743 billones (−0.25%): coincidencia numérica, registrada como tal.
8. (a) 0.356 (anclajes doc) vs 0.342 (CSV) en v1 → **ambos retirados en v2** (artefacto del ancla con FX mezclado). Nuevo (a): 0.383 extremo / 0.436 OLS.

**Nuevas en v2:**

9. **Roche-C dic 2025: 1.89 (componentes exactos del CSV) vs 1.91 (NOTAS §12, con 4.2 billones redondeados).** Se usa 1.89; la diferencia es redondeo de entrada, no de método.
10. **Roche-C mar 2026: ≈2.08 (PE abr 2026 como proxy) vs ≈2.2 (NOTAS §12, con 5.2/2.4 redondeados).** Se usa ≈2.08, marcado como aproximado; la diferencia es redondeo + proxy de PE.
11. **Roche-C nov 2024 en base fondos totales: ≈1.15 con PE dic 2024 como proxy.** Supuesto, no medición; no se usa como fecha de entrada.
12. **Fondos dic 2024: cuatro cifras (PDF 1.687, balance 1.740, Asoban 1.747, ABC 1.76 billones) → Roche-C 1.08–1.13.** Todas > 1.0; la conclusión no depende de cuál se elija. Valor primario: 1.08 (PDF).
13. **Exposición IPS / fondos Ueno sep 2026: v1 decía 41.8% (CSV); v2 corrige a 41.7%** (348.5/834.825625 = 0.4175). Error de redondeo de v1.
14. **Meseta b: −0.046 (v1) → +0.031 (v2).** Cambio de signo con R² ≈ 0.01 en ambas versiones: ruido, no señal. La conclusión (sin tendencia) no cambia.
15. **NOTAS §9 sigue mostrando la pregunta del ratio de Roche como abierta** aunque el documento backcast la resolvió en tres ratios (C/R/S). Se usa el documento backcast como autoridad. NOTAS §12 aparece antes que §§10–11 en la numeración; no afecta los números.
16. **Oct 2024: la etiqueta de procedencia difiere** (el CSV dice archivo_4.pdf; NOTAS §§1/§12 lo atribuyen al patrón con guion bajo). El valor (R = 0.0780) está verificado desde el PDF; la procedencia es un detalle de archivo, no de número.

## Apéndice C — Qué debe cambiar en el espacio y en el podcast v2

> **Para aplicar después, con el visto bueno de Elán. Esta es la lista exacta y completa. No se ha tocado ni el espacio ni el podcast.**

### C.1 Espacio — subsección "Qué muestran los modelos" (sección caso Ueno, subsección 5)

| # | Texto actual (v1) | Texto nuevo (v2) |
|---|---|---|
| 1 | R(t) nov 2024 = 0.110 (ancla del documento) | R(t) nov 2024 = **0.0963** (PDF). El ancla mezclaba tipos de cambio. |
| 2 | "24 meses con R (23 PDF + 1 ancla)" | **"30 meses con R, todos con PDF"** (nuevos: oct 2024 0.0780, dic 2024 0.1021, ene 2025 0.1094, feb 2025 0.1253, mar 2025 0.1315, ene 2026 0.2132). |
| 3 | b (a): "0.356 (anclajes doc) / 0.342 (CSV)" | **b = 0.383 extremo a extremo / 0.436 OLS (R² = 0.873, n=12), ventana dic 2024–nov 2025, t=1 dic 2024.** El 0.356 queda retirado como artefacto de FX mezclado. |
| 4 | b (a') no existía | Añadir: referencia nov 2024–nov 2025 corregida: **0.394 extremo / 0.451 OLS (n=13)**. |
| 5 | b (b) local abr–nov 2025: 0.906 | **0.802** (origen t=1 dic 2024, R² = 0.957). El 0.906 era un artefacto del origen de t (reproducido con el origen viejo: 0.9058). Con origen local: 0.344 (sin cambio). |
| 6 | b (c) meseta: −0.046 (n=8) | **+0.031 (n=9, R² = 0.011)** — sin tendencia medible. El cambio de signo es ruido (R² ≈ 0.01). |
| 7 | b (e) serie completa: 0.813 (n=24) | **0.819 (n=30, todos PDF, R² = 0.909).** La variante (e') desaparece. |
| 8 | "Cruce de Roche-R: nov 2024 (R = 0.110); ventana sep–nov 2024" | **"Cruce de Roche-R: dic 2024 (R = 0.1021); ventana nov–dic 2024"** (nov 0.0963, oct 0.0780; +6.0% nov→dic, +7.1% dic→ene). |
| 9 | "Roche-C y Roche-R cruzaron el mismo mes (nov 2024)" | **"Roche-C (IPS) nov 2024 (1.06); Roche-R dic 2024 (0.1021): un mes aparte."** |
| 10 | Roche-C: solo base IPS | Añadir base fondos totales: **dic 2024 1.08, dic 2025 1.89, mar 2026 ≈2.08** (PE abr 2026 como proxy, aproximado). |
| 11 | Tabla de bandas (§10): "Roche-R nov 2024" | **"Roche-R dic 2024; Roche-C nov 2024 (IPS) / dic 2024 (fondos totales); Roche-S 2 nov 2026 (sin cambio)".** |
| 12 | §11 lectura 1: "la captura ocurrió en un año (nov 2024–nov 2025)" | **"dic 2024–nov 2025 (b 0.383/0.436)"**. |
| 13 | §11 lectura 3: "el sistema entró en zona de ruptura en nov 2024" | **"el sistema entró en Roche en nov–dic 2024: Roche-C (IPS) en nov, Roche-R en dic"**. |
| 14 | §11 lectura 2: regímenes "(0.29 / 0.35 / 0.91 / −0.05)" | **"(0.29 / 0.38–0.44 / 0.80 / +0.03)"**. |
| 15 | ACO-A: "146M/PE 39.8% (PE cierre 2025)" | Añadir: **"35.5% con PE abr 2026 (Gs 2,467,235M)"**. |
| 16 | ACO-A: "salvadoras: PE implícito 2.59 billones, por encima de los cierres" | **"PE implícito 2.59 billones; +4.9% sobre el ancla abr 2026 (antes +17.6% sobre cierre 2025): tensión reducida, no resuelta"**. |
| 17 | ACO-A: "IPS/fondos sep 2026: 41.8% (CSV)" | **41.7%** (corrección de redondeo). |
| 18 | §12 huecos: "15 PDFs faltantes" | **7 PDFs faltantes** (2023-01–05, 2024-08, 2026-03). |
| 19 | §12 huecos: "Informe BCP/P N.° 016 no encontrado" | Añadir: **"existe la Nota BCP/P N.° 019 (denuncia a Fiscalía + informe ~200 fojas) y un informe sellado de 31 fojas al Senado que NO precisa fecha ni monto del exceso"**. |

### C.2 Podcast — episodio v2 (`script-v2.txt`, 53 turnos) y `episodio-v2.mp3`

El guion v2 (3,334 palabras) lleva los números v1 en los turnos del modelo y del cierre. **Cambios exactos por turno (texto hablado, números deletreados):**

| # | Turno / bloque | Texto actual (v1) | Texto nuevo (v2) |
|---|---|---|---|
| 1 | R nov 2024 | "En noviembre de dos mil veinticuatro, la razón era cero punto once, con doscientos setenta y un millones en Ueno y dos mil setecientos treinta y nueve millones en el sistema." | "En noviembre de dos mil veinticuatro, la razón era cero punto cero nueve seis tres, no cero punto once: el ancla mezclaba dos tipos de cambio. Con un solo tipo de cambio, Ueno tenía doscientos noventa y ocho punto siete millones y el sistema tres mil trescientos noventa y ocho punto ocho millones. En diciembre, la razón cruzó cero punto diez, en cero punto uno cero dos uno." |
| 2 | b ventana | "La be, entre noviembre de dos mil veinticuatro y noviembre de dos mil veinticinco, da cero punto tres cinco seis..." | "La be, entre diciembre de dos mil veinticuatro y noviembre de dos mil veinticinco, da cero punto tres ocho tres de extremo a extremo y cero punto cuatro tres seis por mínimos cuadrados. En la ventana completa fue cero punto cuatro tres seis. Y dentro de ella, la segunda mitad, de abril a noviembre de dos mil veinticinco, se empinó hasta cero punto ocho cero dos, no cero punto nueve cero seis: el cero punto nueve cero seis era un artefacto del origen del reloj. Después, la meseta tiene una be de cero punto cero tres uno, sin tendencia medible. El número único de toda la serie, cero punto ocho uno nueve, esconde los tres regímenes." |
| 3 | b depende del reloj | "La be depende del reloj. La misma segunda mitad da cero punto nueve cero seis con el reloj del documento... y cero punto tres cuatro cuatro con un reloj local" | "La be depende del reloj. La misma segunda mitad da cero punto ocho cero dos con el reloj de la ventana, que arranca en diciembre de dos mil veinticuatro, y cero punto tres cuatro cuatro con un reloj local que arranca en abril de dos mil veinticinco. Con el reloj viejo, que arrancaba en noviembre de dos mil veinticuatro, daba cero punto nueve cero seis: mismo tramo, tres números, tres relojes." |
| 4 | Recap Roche | "Roche erre, la razón mayor que cero punto diez, se cruzó en noviembre de dos mil veinticuatro, con la razón en cero punto once. Roche ce, los fondos públicos sobre el patrimonio efectivo mayor que uno, se cruzó el mismo mes, en uno punto cero seis." | "Roche erre, la razón mayor que cero punto diez, se cruzó en diciembre de dos mil veinticuatro, con la razón en cero punto uno cero dos uno; en noviembre estaba en cero punto cero nueve seis tres. Roche ce, los fondos públicos sobre el patrimonio efectivo mayor que uno, se cruzó en noviembre por la base del I P S, en uno punto cero seis, y en diciembre por la base de fondos totales, en uno punto cero ocho. Ya no es el mismo mes para las dos: Roche ce en noviembre, Roche erre en diciembre." |
| 5 | Cierre (zona de ruptura) | "El sistema entró en zona de ruptura en noviembre de dos mil veinticuatro, dos años antes de que alguien actuara" | "El sistema entró en zona de ruptura en diciembre de dos mil veinticuatro, por la razón, y en noviembre por el capital; dos años antes de que alguien actuara" |
| 6 | Cierre (tabla aprobada) | "la tabla ya está aprobada tal como está" | **Sin cambio** (la tabla corregida es la aprobada; la frase sigue siendo válida). |
| 7 | "Cinco cosas abiertas" | "el inicio de la malversación, que solo se puede fechar con el informe B C P P cero dieciséis" | Añadir: "existe la Nota cero diecinueve y un informe de treinta y una fojas al Senado, pero ese informe no precisa ni la fecha ni el monto del exceso, así que ni siquiera es seguro que el cero dieciséis lo fechara". |
| 8 | R(t) serie | "la serie se re-verificó fila por fila" | Añadir: "treinta meses con razón, todos con P D F, y la diferencia máxima es cero". |
| 9 | be del IPS | "La be del I P S, de dos punto nueve tres, se reproduce sobre erre de I P S" | **Sin cambio** (2.934 verificado, sin cambio). |
| 10 | FGD 0.011% / embargo / fondeo 91.75% | — | **Sin cambio** (verificados, sin cambio). |

**Nota de duración:** los cambios añaden ~90 palabras al guion v2 (≈40 s a ~130 palabras/min). El episodio v2 actual dura 19:27; con los cambios quedaría en ~20:05 si no se recorta nada. Si Elán mantiene el objetivo de 15 min, hay que recortar ~5 min en otro bloque (la oferta de dividirlo en dos partes sigue abierta).
