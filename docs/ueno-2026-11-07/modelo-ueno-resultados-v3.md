# Inyección al modelo SNT — caso Ueno Bank: resultados v3

**Fecha:** 2026-11-09. **Tabla:** `tabla-maestra-ueno-mef.csv` VIGENTE (45 filas, ene 2023 – sep 2026; **07 nov 10:48, posterior al v2**), adoptada tras verificación independiente. **Marco:** SNT v2.7.5.1 (README del repo, marco v34). **Método:** Python stdlib, script `verificar_v3.py` (en este mismo directorio de staging; reproducible; lee la tabla vigente, recomputa R(t) desde los componentes y desde las columnas de equivalentes, ajusta b por OLS log-log por ventana con origen de t declarado, y calcula (c′) en calendario y en secuencial). **Fuentes:** tabla maestra vigente + auditoría `REVISION_DOCUMENTOS_UENO.md` (2026-11-09, 564 líneas) + modelo v2 (`modelo-ueno-resultados-v2.md`, 370 líneas) + NOTAS. **Versión v2:** `modelo-ueno-resultados-v2.md` — queda intacta como registro; sus números quedan RETIRADOS o DESACTUALIZADOS donde esta versión los cambia (ver tabla abajo). **Versión v1:** `modelo-ueno-resultados.md` — queda intacta como registro.

**Alcance de esta v3:** solo el modelo de resultados. No se tocó el espacio SNT, no se tocó el podcast, no se subió nada a GitHub, no se modificó ningún otro documento de Ueno. Los cambios pendientes para el espacio y el podcast siguen siendo los del Apéndice C de v2 (19 + 10 cambios), sin aplicar en este pase; esta v3 no los sustituye, solo actualiza los números que esos cambios deberán llevar cuando Elán dé el visto bueno.

## Tabla de cambios v2 → v3 (lo que cambia, con el motivo y la cita)

| # | Qué | v2 | v3 | Motivo / cita |
|---|---|---|---|---|
| 1 | Meses con R | 30 (todos PDF) | **31 (todos PDF)** | Mar 2026 recuperado con PDF y R calculable. `tabla-maestra-ueno-mef.csv:40` (R = 0.2662, participación 0.2103); auditoría §2.1. |
| 2 | R mar 2026 | Sin R ("sin total del sistema"; hueco) | **0.2662** (participación 0.2103) | PDF recuperado 2026-11-07 y verificado en local (Ueno USD 235,381,762 y Gs 3,721,013,013,754 exactos del PDF). `tabla-maestra-ueno-mef.csv:40`; auditoría §2.1. |
| 3 | Máximo de la meseta | Nov 2025, 0.2643 (máximo de la serie hasta entonces) | **Mar 2026, 0.2662 — supera nov 2025 (0.2643)** | Consecuencia no calculada en ningún documento anterior. Auditoría §2.1. |
| 4 | Rango de la meseta dic 2025–sep 2026 | 0.213–0.254 (v2 §1 y §11) | **0.2132–0.2662** | Entra mar 2026 (0.2662, máximo) y el mínimo sigue siendo ene 2026 (0.2132). Auditoría §2.1. |
| 5 | b (c) meseta dic 2025–sep 2026 | +0.031 (n=9, origen dic 2024, R² = 0.011) | **−0.0101 (n=10, origen dic 2024, a = 0.2397, R² = 0.0007)** | Entra mar 2026; n pasa a 10. El signo vuelve a negativo; con R² ≈ 0.001 el signo es ruido. La conclusión ("sin tendencia medible") se mantiene; el número v2 queda desactualizado. Auditoría §2.2. |
| 6 | b (c′) meseta local, t=1 dic 2025 | +0.009 (n=9, R² = 0.013) — valor **secuencial** | **+0.0065 (n=10, a = 0.2306, R² = 0.0048), en CALENDARIO** | Corrección H-1: v2 declaraba calendario (Ap. A, v2:290-299) pero publicaba secuencial. En v3 la ventana ya no tiene huecos (mar 2026 presente), así que calendario y secuencial coinciden en +0.0065. Los valores publicados antes eran secuenciales: v1 −0.0120, v2 +0.0086; con calendario daban v1 −0.0046, v2 +0.0104. Auditoría §2.2, H-1 (`REVISION_DOCUMENTOS_UENO.md:115`, `:124`). |
| 7 | b (c′′) meseta, origen nov 2024 (sensibilidad) | +0.032 (n=9, R² = 0.011) | **−0.0114 (n=10, a = 0.2407, R² = 0.0008)** | Misma ventana con el origen viejo; el signo también se invierte. Auditoría §2.2 (valores vigentes). |
| 8 | b (e) serie completa | 0.819 (n=30, a = 0.0158, R² = 0.909) | **0.8234 (n=31, a = 0.0157, R² = 0.9108)**, origen feb 2024 calendario | Entra mar 2026. Auditoría §2.2. |
| 9 | PDFs MEF faltantes | 7 (2023-01–05, 2024-08, 2026-03) | **6 (2023-01–05, 2024-08)** | Mar 2026 ya tiene PDF. Auditoría §2.9. |
| 10 | Conteo de PDFs (H-5) | 38 PDFs en disco; 38 filas MEF PDF en la tabla de v2 | **38 archivos en disco, pero 39 filas marcadas "MEF PDF"** | Dic 2023 está contado dos veces: su fila figura como "MEF PDF" con totales del sistema (`tabla-maestra-ueno-mef.csv:13`), pero el PDF NO está en el directorio local (NOTAS §2 lo admite; el log lo marca MISSING). Además el "38" de v2 no es el mismo "38" actual: el de v2 incluía dic 2023 y no mar 2026; el actual incluye mar 2026 y no dic 2023. Ningún documento advertía esta coincidencia. Auditoría §2.9, H-5 (`REVISION_DOCUMENTOS_UENO.md:179`). |
| 11 | Discrepancia mar 2026 (balance vs Tesoro) | **No mencionada en ningún punto de v2** (grep "3,163,975" en v2 = 0) | **Registrada en v3: Gs 557.038M solo en Gs; USD 235.381.762 sin conciliar aparte** | Balance Gs 3,163,975M vs Tesoro Gs 3,721,013M + USD 235M; diferencia Gs 557,038,013,754 verificada. A FX 6.000, el USD serían +Gs 1,412,290,572,000, así que la discrepancia total en equivalentes sería Gs 1,969,328,585,754. GAP de definición, no error aritmético: la cifra citada (557.038M) no es la discrepancia total en equivalentes. Auditoría §2.8 (`REVISION_DOCUMENTOS_UENO.md:173`); `tabla-maestra-ueno-mef.csv:40`. |
| 12 | φ paso 1 (C-16) | 65 → 60, 9 nov 2023, con paréntesis "(v1 decía 70 → 60, sin fecha; v2 lo corrige y fecha)" (v2:163) | **65 → 60, 9 nov 2023 — igual en v1 y en v2; la "corrección" que v2 se atribuye NO existe** | v1 YA decía 65 → 60 CON fecha (`modelo-ueno-resultados.md:114`). La atribución a v1 es falsa contra el propio archivo v1. Además el encabezado del §6 de v2 decía "Sin cambio respecto a v1" y a la vez afirmaba corregir: autocontradicción interna de v2. El valor 65 → 60 en sí es el mismo en ambas versiones. Auditoría §5.3, C-16 (`REVISION_DOCUMENTOS_UENO.md:422`). |
| 13 | φ pasos 3–5: fechas (C-17) | Paso 3: 2025; paso 4: 2025; paso 5: jun–oct 2026, sin la notificación del 24 jul 2026 (v2:157-171). Tabla de cambios #19 de v2 decía "φ, ASI, muro… Sin cambio" | **Se lista el cambio, no se esconde: paso 3 2024–2025 → 2025; paso 4 2024 → 2025; paso 5 2024–2026 → jun–oct 2026, sin la notificación del 24 jul 2026** | Cambio no listado en v2: las fechas se estrechan y desaparece la notificación del 24 jul 2026, sin motivo registrado. El contenido (montos) es el mismo. Auditoría §5.3, C-17 (`REVISION_DOCUMENTOS_UENO.md:423`). |
| 14 | φ paso 4: periodo del incremento de intangibles (C-18) | "+Gs 654.799M (2024–2025)" (v2:157-171) | **"+Gs 654.799M — periodo POR CONFIRMAR: v1 dice solo en 2025; v2 dice 2024–2025"** | El mismo incremento se atribuye a "solo 2025" en v1 y a "2024–2025" en v2. El total (Gs 761.444M) es el mismo. No se inventa un periodo: queda marcado así hasta verificarlo contra los EEFF. Auditoría §5.3, C-18 (`REVISION_DOCUMENTOS_UENO.md:424`). |
| 15 | IPS 9.70%: año (C-30) | "30 oct 2025" (v2:234, lectura 1) | **30 oct 2026** | Las fuentes del parteaguas (F5 `:47` y `:262`, F6 `:28`) dicen 30 oct 2026; también el forecast .md:209 y backcast-roche-notas:21. El valor 9.70% no está en disputa, solo el año. El v2 trae el año mal (2025 por 2026). Auditoría §3.7 (`REVISION_DOCUMENTOS_UENO.md:269`) y §5.3, C-30 (`REVISION_DOCUMENTOS_UENO.md:436`). |
| 16 | Secuencia de bandas | Nov 2024 Roche-C → dic 2024 Roche-R → 2 nov 2026 Roche-S | **SIN CAMBIO con mar 2026** | Mar 2026 (R = 0.2662) no cruza ninguna banda nueva: cae dentro de la meseta, entre Roche-R (ya cruzada en dic 2024) y Roche-S (2 nov 2026). Auditoría §6 y §8. |

**Sin cambio v2 → v3 (verificado en la auditoría):** R 0.0963 (nov 2024), cruce Roche-R dic 2024 (0.1021), Roche-C 1.06 / 1.08 / 1.89 / ≈2.08, Roche-S 0.463, b 0.383 / 0.436, 0.802, 0.344 (origen local), 0.288, b IPS 2.934, FGD 0.011%, anticipo 4.38%, IPS/fondos 41.7%, USD 146M / PE 39.8% / 35.5%, salvadoras Gs 2.59 billones, fondeo 91.75%, embargo Gs 2.1005 billones, −0.25%. Auditoría §5.3 ("Sin cambio v1→v2 (verificado)") y §8.

## Tabla de cambios v1 → v2 (registro histórico, sin cambios)

Se reproduce íntegra la tabla de v2, porque es el registro de lo que v2 corrigió respecto a v1. Nada de esta tabla se vuelve a cambiar en v3; solo se añade la tabla v2 → v3 de arriba.

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
- **(Nuevo en v3, H-1):** la convención de t declarada en el Apéndice A — t es el mes calendario, con huecos cuando falta el PDF — se aplica también a la variante local (c′). En v1 y v2 (c′) se publicó con numeración secuencial; en v3 se publica con calendario. En la ventana v3 ambas numeraciones coinciden (no hay huecos entre dic 2025 y sep 2026), así que el valor +0.0065 es a la vez calendario y secuencial.

## 1. R(t) — re-verificación desde las columnas del CSV

Definición: R(t) = fondos públicos en Ueno / fondos públicos en el resto del sistema (total MEF − Ueno), en USD equivalentes a FX 6,000 por fila. **Ya no hay ancla del documento: los 31 meses con R son PDF.**

Recomputada fila por fila como `ueno_total_usd_equiv / (total_sistema_usd_equiv − ueno_total_usd_equiv)`, con verificación cruzada desde los componentes crudos (USD×6,000 + Gs). Ver `VERIFICACION_V3.md`: diferencia máxima 0.00005 en valor absoluto (0.0000 a 4 decimales, puro redondeo de la columna R_t del CSV).

| Fecha | R(t) CSV | R(t) recalculada | Diferencia | Fuente |
|---|---|---|---|---|
| 2024-02 | 0.0284 | 0.0284 | +0.0000 | MEF PDF |
| 2024-03 | 0.0319 | 0.0319 | +0.0000 | MEF PDF |
| 2024-04 | 0.0332 | 0.0332 | +0.0000 | MEF PDF |
| 2024-05 | 0.0346 | 0.0346 | +0.0000 | MEF PDF |
| 2024-06 | 0.0338 | 0.0338 | +0.0000 | MEF PDF |
| 2024-07 | 0.0610 | 0.0610 | +0.0000 | MEF PDF |
| 2024-09 | 0.0777 | 0.0777 | +0.0000 | MEF PDF |
| 2024-10 | 0.0780 | 0.0780 | +0.0000 | MEF PDF |
| 2024-11 | 0.0963 | 0.0963 | +0.0000 | MEF PDF (corregido en v2; v1: ancla 0.110) |
| 2024-12 | 0.1021 | 0.1021 | +0.0000 | MEF PDF |
| 2025-01 | 0.1094 | 0.1094 | +0.0000 | MEF PDF |
| 2025-02 | 0.1253 | 0.1253 | +0.0000 | MEF PDF |
| 2025-03 | 0.1315 | 0.1315 | +0.0000 | MEF PDF |
| 2025-04 | 0.1396 | 0.1396 | +0.0000 | MEF PDF |
| 2025-05 | 0.1628 | 0.1628 | +0.0000 | MEF PDF |
| 2025-06 | 0.1706 | 0.1706 | +0.0000 | MEF PDF |
| 2025-07 | 0.2079 | 0.2079 | +0.0000 | MEF PDF |
| 2025-08 | 0.2457 | 0.2457 | +0.0000 | MEF PDF |
| 2025-09 | 0.2467 | 0.2467 | +0.0000 | MEF PDF |
| 2025-10 | 0.2670 | 0.2670 | +0.0000 | MEF PDF |
| 2025-11 | 0.2643 | 0.2643 | +0.0000 | MEF PDF |
| 2025-12 | 0.2280 | 0.2280 | +0.0000 | MEF PDF |
| 2026-01 | 0.2132 | 0.2132 | +0.0000 | MEF PDF |
| 2026-02 | 0.2357 | 0.2357 | +0.0000 | MEF PDF |
| 2026-03 | **0.2662** | **0.2662** | +0.0000 | **MEF PDF (nuevo en v3; participación 0.2103)** |
| 2026-04 | 0.2543 | 0.2543 | +0.0000 | MEF PDF |
| 2026-05 | 0.2254 | 0.2254 | +0.0000 | MEF PDF |
| 2026-06 | 0.2246 | 0.2246 | +0.0000 | MEF PDF |
| 2026-07 | 0.2306 | 0.2306 | +0.0000 | MEF PDF |
| 2026-08 | 0.2161 | 0.2161 | +0.0000 | MEF PDF |
| 2026-09 | 0.2395 | 0.2395 | +0.0000 | MEF PDF |

**Resultado: la serie reproduce el CSV exactamente.** Diferencia máxima 0.0000 a 4 decimales (v1: 0.0002 por el redondeo del ancla, que ya no existe). Participación de Ueno reproduce igual. **31 meses con R calculable, todos con PDF.** Valores clave confirmados: feb 2024 0.028, jul 2024 0.061, sep 2024 0.078, oct 2024 0.078, nov 2024 0.096, dic 2024 0.102, nov 2025 0.264, **mar 2026 0.266**, meseta 2026 **0.2132–0.2662**.

**Nuevo en v3 — mar 2026 es el máximo de la meseta y supera nov 2025:** R mar 2026 = 0.2662 > R nov 2025 = 0.2643. Ningún documento anterior calculó esta consecuencia. La meseta dic 2025–sep 2026 ya no tiene como máximo nov 2025 ni como techo 0.254: su rango es 0.2132 (ene 2026, mínimo) a 0.2662 (mar 2026, máximo).

**Huecos (R no calculable):** ene–may 2023 y ago 2024 (sin PDF), todo 2023 (Ueno sin fila individual o dentro de OTROS BANCOS), ene 2024 (USD de Ueno dentro de OTROS BANCOS). Mar 2026 **sale** de la lista de huecos. No se imputa nada.

**Observaciones registradas, no ajustadas:** salto jul 2024 (R 0.034→0.061, +80.5% en un mes); USD de Ueno feb–mar 2024 casi idéntico (+USD 16) mientras Gs sube — posible cifra arrastrada; caída dic 2025 (Ueno −12.5% en USD, R 0.264→0.228) mientras el sistema sube — el documento no la comenta. **Nuevo:** la planicie feb–jun 2024 (R 0.028–0.035) queda rota en jul 2024 y nunca se recupera; oct 2024 (0.0780) muestra que entre sep y nov la subida fue gradual (0.0777 → 0.0780 → 0.0963), no un salto de un mes: el cruce de 0.10 se preparó en dos meses, no se produjo de golpe.

### 1.1 Discrepancia mar 2026 (balance vs Tesoro) — GAP de definición, no error aritmético

Esta discrepancia **está en el CSV sí, en el v2 no**: v2 no la menciona en ningún punto (grep "3,163,975" en v2 = 0). Se registra aquí por primera vez en el modelo (auditoría §2.8, `REVISION_DOCUMENTOS_UENO.md:173`; `tabla-maestra-ueno-mef.csv:40`; NOTAS §7).

- Balance Gs 3,163,975M vs Tesoro Gs 3,721,013M (+ USD 235M): diferencia en guaraníes **Gs 557,038,013,754** — verificada (3,721,013,013,754 − 3,163,975,000,000).
- **Matiz no advertido en los documentos:** los Gs 557,038M son diferencia **solo en Gs**; el componente USD queda "sin conciliar" aparte y no se suma. El USD de Ueno de mar 2026, exacto en el CSV, es **USD 235,381,762**; a FX 6,000 serían **+Gs 1,412,290,572,000**.
- Discrepancia total en equivalentes (Gs + USD×6,000): **Gs 1,969,328,585,754**. Es decir, la cifra citada habitualmente (Gs 557,038M) **no es la discrepancia total en equivalentes**: es solo la parte en guaraníes.
- Estado: **GAP de definición, no error aritmético.** La discrepancia sigue registrada como no resuelta. No se corrige nada en silencio: no se sabe si el USD 235M debe sumarse al Gs 557,038M (son dos mediciones distintas — balance vs Tesoro — y el propio CSV las registra por separado), así que se presentan ambas cifras y su suma en equivalentes, marcadas como lo que son.

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
| (c) | dic 2025 – sep 2026 (meseta) | OLS log-log | t=1 dic 2024 (t=13..22) | 10 | **−0.0101** | 0.2397 | 0.0007 | Estado estacionario |
| (c') | dic 2025 – sep 2026 (meseta) | OLS log-log (origen local, **calendario**) | t=1 dic 2025 (t=1..10) | 10 | **+0.0065** | 0.2306 | 0.0048 | Estado estacionario |
| (c'') | dic 2025 – sep 2026 (meseta) | OLS log-log (origen viejo, compara v1/v2) | t=1 nov 2024 (t=14..23) | 10 | **−0.0114** | 0.2407 | 0.0008 | Estado estacionario |
| (d) | feb – jul 2024 (pre-Roche) | OLS log-log | t=1 feb 2024 (t=1..6) | 6 | **0.288** | 0.0262 | 0.503 | Satelización gradual (ajuste débil) |
| (e) | feb 2024 – sep 2026 (completa) | OLS log-log | t=1 feb 2024 (calendario) | 31 | **0.8234** | 0.0157 | 0.9108 | Satelización activa (resumen grueso) |
| (IPS) | 2023 – 2025 (anual) | OLS log-log sobre r_ips (0.0101, 0.0917, 0.2453) | t=1 2023 | 3 | **2.934** | 0.0106 | 0.995 | b ≥ 1 banda descriptiva no clasificada |

**La meseta cambia de signo otra vez — y eso es lo que hay que leer:** en v1 daba −0.046 (n=8), en v2 +0.031 (n=9), en v3 −0.0101 (n=10, origen dic 2024). Con R² ≈ 0.001 en v3 (0.0007 con origen dic 2024, 0.0008 con origen nov 2024, 0.0048 con origen local), el signo de b en la meseta es ruido, no señal. La conclusión no cambia en ninguna versión: **sin tendencia medible**. Lo que cambia es el número, y el número v2 (+0.031) queda desactualizado por mar 2026. Con origen local la meseta v3 da +0.0065: el signo depende del origen, igual que en v2 (+0.031 / +0.032 / +0.009). Ninguna de las tres variantes es significativa.

**Corrección H-1 — (c′) ahora es calendario, como se declaraba (auditoría §2.2, H-1):** v2 Apéndice A (v2:290-299) establece: "t es el mes calendario (meses desde el origen, con huecos cuando falta el PDF)". Pero los valores publicados de (c′) correspondían a **numeración secuencial 1..n**: v1 (c′) −0.0120 / R² 0.0296 = secuencial exacto; con calendario da −0.0046 / R² 0.005. v2 (c′) +0.0086 / R² 0.0132 = secuencial exacto; con calendario da +0.0104 / R² 0.0226. Los ajustes principales (c), (e), (a-OLS), (b) sí usan calendario y reproducen. En v3 la (c′) se publica con calendario: **+0.0065 / R² 0.0048, n=10**. Y en esta ventana el calendario y el secuencial **coinciden** (t = 1..10 en ambos, porque dic 2025–sep 2026 ya no tiene huecos con mar 2026 presente), así que el valor +0.0065 es a la vez calendario y secuencial. Los cuatro valores de control (v1 secuencial −0.0120, v1 calendario −0.0046, v2 secuencial +0.0086, v2 calendario +0.0104) se reproducen exactos con `verificar_v3.py` — ver `VERIFICACION_V3.md`. La diferencia es pequeña y no cambia ninguna conclusión (R² ≈ 0.01), pero el método declarado y el aplicado ya no difieren en (c′).

**El origen de t sigue siendo la advertencia central:** el mismo tramo abr–nov 2025 da 0.802 (origen dic 2024), 0.906 (origen nov 2024) y 0.344 (origen local abr 2025). Tres números, un tramo, tres relojes. La meseta da −0.010, −0.011 y +0.007 según el origen — todas ≈ 0 con R² ≈ 0.001–0.005, así que la conclusión (sin tendencia) no depende del reloj, pero el signo sí. **b depende del reloj elegido**: es un descriptor de la ventana con su origen declarado, no una constante intrínseca del sistema.

**Verificación del b IPS del documento (2.93):** sin cambio respecto a v1 y v2. OLS log-log sobre **r_ips** (0.0101, 0.0917, 0.2453; t=1,2,3) da **b = 2.934, R² = 0.995** — reproduce el 2.93. Sobre participaciones (1.0%, 8.4%, 19.7%) da 2.752 (R² = 0.992) y sobre montos en Gs da 2.762 (R² = 0.994). **Conclusión: el 2.93 es el ajuste sobre r_ips (la forma de razón, coherente con R(t)), no sobre participaciones.** En cualquier caso b ≥ 1 es banda descriptiva no clasificada (n=3 puntos anuales); NO es prueba de superlinealidad.

**Lectura conjunta de b (corregida en v3 solo en la meseta y en la serie completa):** la deriva no fue uniforme. Antes de Roche (feb–jul 2024) era gradual (b ≈ 0.29, R² = 0.50 — ajuste débil, dominado por el salto de jul 2024). En la ventana dic 2024–nov 2025 fue activa (b ≈ 0.44 por OLS, 0.38 de extremo a extremo), y dentro de ella la segunda mitad se empinó (b local ≈ 0.80 con el origen consistente, R² = 0.96). Después de nov 2025 la deriva se detuvo: la meseta tiene b ≈ −0.01 con R² = 0.001, es decir, **sin tendencia medible**. El ajuste de toda la serie (b ≈ 0.82, R² = 0.91) resume tres regímenes distintos en un solo número y no debe usarse solo: esconde el salto, la aceleración y la meseta. Además es un descriptor de una serie acumulativa con autocorrelación fuerte: sin n_eff ni comparación contra un nulo, es un descriptor, no una prueba. **La corrección de v3 no invierte la historia de v2, la precisa:** la ventana completa pasa de 0.819 (n=30) a 0.823 (n=31); la meseta pasa de +0.031 (n=9) a −0.010 (n=10); la deriva sigue siendo satelización activa hasta nov 2025 y meseta después.

## 3. Roche-R (relativa): R(t) > 0.10

Sin cambio respecto a v2.

- **Primer mes con R > 0.10: dic 2024 (R = 0.1021).** Mes anterior con dato: nov 2024 (0.0963); anterior: oct 2024 (0.0780). **Ventana de cruce: nov–dic 2024** — ambos meses tienen PDF; el cruce queda fechado al mes, sin interpolación a día (los datos son mensuales).
- **Variaciones mensuales del cruce:** nov → dic 2024: **+6.0%** (0.0963 → 0.1021); dic 2024 → ene 2025: **+7.1%** (0.1021 → 0.1094). El cruce no fue un salto: fue el tercer mes consecutivo de subida (sep 0.0777 → oct 0.0780 → nov 0.0963 → dic 0.1021).
- **Cruce de 0.20:** entre jun 2025 (0.1706) y jul 2025 (0.2079). Interpolación lineal, fracción 0.788: con la convención del documento (valores al inicio del mes) ≈ **24 jun 2025**; con convención de fin de mes ≈ 24 jul 2025. La diferencia es un artefacto de convención, no de los datos. Se adopta ≈24 jun 2025 (misma convención del documento y de la verificación previa). Sin cambio respecto a v1 y v2.
- R(t) se mantuvo > 0.10 en todos los meses con dato desde dic 2024 hasta sep 2026. Mínimo después del mes del cruce: 0.1094 (ene 2025). No hay retorno por debajo de Roche-R en la serie. Mar 2026 (0.2662) no cambia esto: es el máximo de la meseta, no un cruce nuevo.

## 4. Roche-C (concentración): fondos públicos en Ueno / patrimonio efectivo > 1.0

Sin cambio respecto a v2. Dos bases, sin mezclar. La base IPS es la del documento backcast (sin cambio). La base fondos totales es nueva en v2: se calcula desde el CSV (fondos a FX 6,000) y las anclas de patrimonio efectivo de NOTAS §12.

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

**HUECO: la serie mensual de Roche-C NO es calculable.** El patrimonio efectivo solo existe en anclas fechadas (dic 2023: 337,228M; dic 2024: 1.56 billones; oct 2025: 1.8 billones; dic 2025: 2.20 billones; ene 2026: >USD 335M; abr 2026: 2.467 billones implícito por el tope 20%). Sin serie mensual de patrimonio efectivo no se puede fechar el cruce al mes con más precisión que nov 2024 (base IPS), ni calcular su trayectoria entre los puntos. Sigue sin cambio respecto a v1 y v2.

**Discrepancia dic 2024 (registrada, no resuelta):** hay cuatro cifras de fondos públicos totales para dic 2024 — PDF a FX 6,000: Gs 1.687 billones → Roche-C 1.08; balance 2024 (sector público): Gs 1.740 billones → 1.12; Asoban vía ABC: Gs 1.747 billones → 1.12; ABC citado: Gs 1.76 billones → 1.13. NOTAS §12 explica que 1.76 es el mismo saldo convertido a otro tipo de cambio (≈6,300), no una cifra distinta del PDF. **Las cuatro dan Roche-C entre 1.08 y 1.13, todas > 1.0: la conclusión (cruce en dic 2024) no depende de cuál se elija.** Se usa 1.08 (PDF a FX 6,000) como valor primario por ser el único con componentes verificables en la tabla.

## 5. Roche-S (solvencia): solvencia reportada / mínimo legal 12% < 0.50

Sin cambio respecto a v1 y v2.

| Fecha | Solvencia reportada | Roche-S | Fuente |
|---|---|---|---|
| Mar 2026 | 15.01% | **1.251** | Parteaguas v2 §1.4 [19][22] |
| Jun 2026 | 14.5% | **1.208** | Parteaguas v2 §1.4 [19][22] |
| Sep 2026 | 13.85% | **1.154** | Parteaguas v2 §1.4 [19][22] |
| 2 nov 2026 | 5.56% | **0.463** | BCP, resolución (Ley 2334/03 art. 13 inc. b) |

La solvencia reportada se mantuvo **por encima del mínimo (Roche-S > 1) hasta sep 2026**. El cruce económico de Roche-S **no es fechable con datos públicos**: entre sep y nov 2026 el reporte pasó de 13.85% a 5.56% tras previsiones > Gs 1.6 billones (inspección 31 oct), pero el reporte estaba sostenido por intangibles (Gs 761,444M), Derechos Fiduciarios (Gs 2,105,743M) y Participaciones (+8,000% en 2025), saldos de cierre 2025 sin fecha mensual. **El 2 nov 2026 es el reconocimiento legal de Roche-S (0.463 < 0.50), no su cruce económico.**

## 6. φ — captura normativa en 5 pasos (mecanismo)

**Corrección de la atribución (C-16) y precisión de fechas (C-17/C-18).** El paso 1 es 65 → 60 el 9 nov 2023 **en v1 y en v2**: la "corrección" que v2 se atribuía no existe, y el encabezado de este §6 en v2 ("Sin cambio respecto a v1") contradecía su propio paréntesis. En v3 el encabezado es: pasos 1, 2 y montos sin cambio respecto a v1; **fechas de los pasos 3–5 estrechadas respecto a v1 (se listan, no se esconden)**; periodo del incremento de intangibles del paso 4 por confirmar. φ no es una métrica con unidad; es la **trazabilidad normativa** del desplazamiento: qué actos retiraron luz, cuándo, con qué observable.

| # | Paso (φ) | Fecha | Observable (fuente) |
|---|---|---|---|
| 1 | Licitación: puntaje mínimo **65 → 60** (igual en v1 y en v2; v2 decía corregir el "70 → 60" de v1, pero v1 ya decía 65 → 60 con fecha — C-16) | **9 nov 2023** | ABC 2023-11-10; parteaguas v2 §3.1 [14]. R no se mueve: es pre-condición, no inicio. |
| 2 | IPS Res. C.A. N.° 093-046/2024: **eliminación del límite de patrimonio efectivo** | **12 nov 2024** | Parteaguas v2 §3.2 [15]. Mismo paso también baja la calificación requerida (A-Py strong trend → genérica A). |
| 3 | Gastos de fusión activados como **activo fiduciario**: aumento de Derechos Fiduciarios de Gs 0 a Gs 2.1 billones, 99.44% del patrimonio neto | **2025** (v1 decía 2024–2025 — C-17) | EEFF 2025 (Asoban); parteaguas v2 §3.3 [17]. |
| 4 | **No-desagregación del software** tolerada: activos intangibles +Gs 654,799M (**periodo POR CONFIRMAR: v1 dice solo en 2025; v2 dice 2024–2025** — C-18) | **2025** (v1 decía 2024 — C-17; el periodo del incremento queda por confirmar, ver nota) | EEFF 2025 (Asoban); parteaguas v2 §3.4 [18]. |
| 5 | **Reserva supervisora mantenida** (solicitud de constituir previsiones no ejecutada) | **Jun – oct 2026** (v1 decía 2024–2026 — C-17) | Supervisión (8 jun 2026) [20]; acta BCP (19 jun 2026) [19]; Rivarola (10 jul 2026) [22]. |

**Nota C-17 (paso 5):** la notificación del **24 jul 2026** que v1 citaba en el paso 5 no aparece en la tabla de v2, y no hay motivo registrado para su desaparición. No se restablece aquí como hecho del paso 5: queda como GAP de traslado, pendiente de verificar contra parteaguas v2 §1.4 (que sí registra notificaciones 5 jun / 24 jul 2026). Las fechas 5 jun / 15 jun / 24 jul 2026 son NO VERIFICABLES contra v2 (auditoría §3.5); su fuente es parteaguas v2 [18][21].

**Nota C-18 (paso 4):** el incremento es +Gs 654,799M y el total es Gs 761,444M en ambas versiones; lo que cambia es el periodo al que se atribuye el incremento ("solo en 2025" en v1, "2024–2025" en v2). No se elige un periodo en v3: se marca POR CONFIRMAR hasta verificarlo contra los EEFF. El comparador "triplica la suma de intangibles de nueve bancos (Gs 269,233M)" que aparece en parteaguas-notas es aritméticamente incorrecto (654,799/269,233 = 2.43×, no 3×) y no está en v2: no se usa aquí (auditoría §3.5, C-29).

Las φ son **causas formales**: cada paso retiró luz. Ninguna es causa mecánica por sí sola, ni una variable continua en una ecuación. **φ no fue cuantificado como campo continuo** (el estado actual del marco lo postula por dominio, no lo mide).

**φ contable (v2, sin cambio):** Gs 2.5 billones de gastos de fideicomiso + Gs 2.6 billones de cartera morosa mal clasificada como vigente. Sin cambio respecto a v1.

## 7. ASI — Índice de Soberanía Atómica (evaluación documental)

Sin cambio respecto a v1 y v2.

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

Sin cambio respecto a v2.

**Criterio de ACO-A (README):** extinción funcional de la unidad + absorción identificable por otro proceso. **Criterio cumplido** (sin cambio): 2 nov 2026, resolución de solvencia 5.56% < 12% (Ley 2334/03 art. 13 inc. b); proceso de exclusión con 7 bancos licitantes y balance de exclusión en un plazo máximo de 15 días.

**Δ NO es estimable** (sin cambio): la fórmula requiere A(τ) (masa/actividad de la unidad) en el tiempo y no hay serie temporal de A(τ) para Ueno. Lo que hay son saldos de cierre y anclas.

**Modo de colapso (juicio descriptivo, no medición): Acantilado Catastrófico** con rasgos de **Craquelado** — la solvencia reportada pasó de 13.85% (sep 2026) a 5.56% (2 nov 2026) en ~1 mes, tras una fase de fracturas acumuladas (provisionamiento, reservas mantenidas, fideicomiso). Sin cambio respecto a v1.

**Aritmética (actualizada con las anclas nuevas de NOTAS §12, sin cambio en v3):**

- FGD / exposición IPS (sep 2026): Gs 228,300,000 / Gs 2.03 billones = **0.011%** (sin cambio).
- Anticipo FGD Gs 10,000,000 = **4.38% del tope** (sin cambio).
- **Exposición IPS / fondos Ueno (sep 2026): doc 40.8% (348.5/855); CSV 41.7% (348.5/834.8).** v1 decía 41.8% por redondeo; la corrección es 0.1 pp. La discrepancia doc/CSV (40.8% vs 41.7%) refleja la diferencia de total (855M vs 834.8M a FX 6,000), no un error de cálculo.
- **USD 146M vinculados / patrimonio efectivo: 39.8% con PE cierre 2025 (Gs 2.2 billones = USD 366.7M) y 35.5% con PE abr 2026 (Gs 2,467,235M = USD 411.2M).** El 35.5% es nuevo en v2 (ancla abr 2026, más contemporánea al periodo sep 2025–may 2026 del excedente). En ambos casos ≈1.8–2× el tope del 20% (el tope es USD 73M con PE 2025 o USD 82.2M con PE abr 2026; el excedente es USD 146M).
- **Salvadoras:** deudas Gs 905,825M = 35% del patrimonio efectivo → PE implícito **Gs 2.588 billones**. Contra el ancla abr 2026 (Gs 2.467 billones): **+4.9%**. Contra el cierre 2025 (Gs 2.20 billones): +17.6%. **La tensión se reduce con el ancla nueva** (v1 solo tenía el cierre 2025), pero no se resuelve: el PE de ago 2026 (fecha de la cifra de salvadoras) no está documentado, y el PE implícito sigue por encima de todos los cierres conocidos.
- Fondeo dic 2024–mar 2025 no a préstamos: depósitos +Gs 1,755,304M (+17%), crédito neto +Gs 144,737M (+2%) → **91.75% del fondeo incremental no fue a préstamos** (144,737/1,755,304 = 8.25% a préstamos). Sin cambio respecto a v1.
- **Embargo total (Gs equivalente):** USD 70M + Gs 1,621,853,458,972 + Gs 58,639,000,000 = **Gs 2.1005 billones** (a FX 6,000). vs Derechos Fiduciarios Gs 2.105743 billones: **−0.25%**. Coincidencia numérica, registrada como tal (sin cambio).
- **Dato de NOTAS §12 (v2):** la diferencia entre la cifra de fondos totales de dic 2024 y la de mar 2026 (Gs 1.687 → 5.133 billones) es +Gs 3.446 billones en 15 meses, mientras el PE pasó de 1.56 a 2.467 billones: Roche-C en base fondos totales subió de 1.08 a ≈2.08. El hub se endeudó con fondos públicos más rápido de lo que creció su capital.

## 9. El muro de 5 eventos — lectura por φ

Sin cambio de fondo respecto a v2; solo se actualiza la referencia a la meseta.

**Guarda:** el muro de 5 eventos existe en el repo (v30) como criterio de escape de la satelización (mínima diversidad funcional); el muro-por-φ es una **aplicación de Elán al caso Ueno** y una **propuesta** (lectura bipolar), no una redefinición. **Leapfrog NO se redefine**: sigue siendo el salto por b < 0 al Nivel Exógeno (README Módulo 0: b < 0 = Convergencia / leapfrog).

**Negativos (φ): 5/5.** Los 5 pasos de φ (§6) son los 5 eventos negativos del muro: (1) puntaje 65→60 (9 nov 2023); (2) eliminación del límite de PE (12 nov 2024); (3) gastos de fusión como activo fiduciario; (4) no-desagregación del software; (5) reserva supervisora mantenida. El muro predice colapso; el colapso ocurrió (2 nov 2026).

**Positivos (condiciones de ASI alto): 0/5 (jubilados), 0/4 (ahorristas, +1 sin datos), 0/5 (OEEs).** Ninguna unidad atómica alcanza el salto bajo la definición vigente de leapfrog (b < 0). **Convergencia observada:** ninguna ventana muestra b < 0 significativo — ni la meseta (b ≈ −0.01 con origen dic 2024, R² = 0.001; b ≈ +0.007 con origen local, R² = 0.005) ni la serie completa (b ≈ 0.82). El muro y b **coinciden en el resultado** (nadie escapó) sin resolver aún la conexión entre ambos: la hipótesis de reconciliación (los eventos positivos son acciones que bajan R(t), es decir, b < 0) sigue siendo **HIPÓTESIS, no establecida**.

## 10. Las bandas determinan el colapso

**Guarda v3.1 (lectura descriptiva, Claude 2026-11-09):** todo lo que sigue en esta sección es una lectura descriptiva de un solo caso, leída a posteriori sobre un caso ya ocurrido. No hay grupo de comparación, ni nulo, ni preregistro: las bandas y el backcast describen, no validan. La meseta (n=10, R² = 0.0007) solo respalda "sin tendencia", no una estructura. El b = 0.8234 de la serie completa es un descriptor de una serie acumulativa con autocorrelación fuerte, no una prueba.

**Hipótesis de trabajo (Elán):** cuando se cruza el ratio de Roche, las bandas cruzadas — una, dos, tres — determinan cómo se despliega el colapso. En Ueno se cruzaron las tres; el resultado fue colapso total con trigger legal. Las lecturas de una o dos bandas son **hipótesis de trabajo, no mediciones**.

| Banda | Definición | Cruce | Valor |
|---|---|---|---|
| Roche-C | Fondos públicos / PE > 1.0 | **Nov 2024** (base IPS, 1.06); dic 2024 (base fondos totales, 1.08) | 1.06 / 1.08 |
| Roche-R | R(t) > 0.10 | **Dic 2024** (R = 0.1021) | 0.1021 |
| Roche-S | Solvencia / 12% < 0.50 | **2 nov 2026** (reconocimiento legal, 0.463) | 0.463 |

**Corrección clave de v2 (se mantiene en v3):** Roche-C y Roche-R **ya no cruzan el mismo mes**. Roche-C (base IPS) cruzó en nov 2024; Roche-R en dic 2024. La entrada a Roche-R coincide con el mes en que empieza la captura masiva en CDA (dic 2024–mar 2025: +Gs 1,755,304M en depósitos con crédito neto +2%). La secuencia corregida es: **nov 2024 — concentración (Roche-C, IPS); dic 2024 — ruptura relativa (Roche-R) + captura masiva; nov 2026 — reconocimiento legal (Roche-S)**. Dos años entre la entrada a Roche (nov–dic 2024) y el reconocimiento (nov 2026).

**La secuencia NO cambia con mar 2026 (nuevo en v3):** mar 2026 (R = 0.2662) es el máximo de la meseta, pero no cruza ninguna banda nueva: Roche-R ya estaba cruzada desde dic 2024, Roche-C desde nov/dic 2024, y Roche-S se reconoce el 2 nov 2026. La secuencia nov 2024 → dic 2024 → 2 nov 2026 queda intacta (auditoría §6 y §8).

**Contrafactuales (hipótesis, no mediciones):** con solo Roche-C (concentración sin deriva relativa) el sistema podría haber estabilizado en una captura lenta; con Roche-C + Roche-R (sin Roche-S) la absorción habría sido ordenada pero sin trigger legal; con las tres, el colapso fue total con trigger legal y embargo. Ninguno de estos escenarios es medible con los datos disponibles.

## 11. Qué muestran los modelos (lectura corregida en v3)

**Guarda v3.1 (lectura descriptiva, Claude 2026-11-09):** todo lo que sigue en esta sección es una lectura descriptiva de un solo caso, leída a posteriori sobre un caso ya ocurrido. No hay grupo de comparación, ni nulo, ni preregistro: las bandas y el backcast describen, no validan. La meseta (n=10, R² = 0.0007) solo respalda "sin tendencia", no una estructura. El b = 0.8234 de la serie completa es un descriptor de una serie acumulativa con autocorrelación fuerte, no una prueba.

1. **La captura ocurrió en un año y luego se detuvo sola por saturación.** R pasó de 0.1021 (dic 2024) a 0.2643 (nov 2025), ×2.6 en 11 meses (b ≈ 0.44 por OLS). Después, b ≈ −0.01 (n=10, R² = 0.001): la meseta dic 2025–sep 2026 no tiene tendencia medible. El freno fue el tope del 10% del IPS (9.70% al **30 oct 2026** — año corregido en v3, v2 decía 2025; sin nuevas colocaciones en 2026), no una intervención. **Corrección: la ventana es dic 2024–nov 2025 (b 0.383/0.436), no nov 2024–nov 2025 (0.356 retirado).**
2. **La deriva tuvo tres regímenes y el número único los esconde.** Gradual (feb–jul 2024, b ≈ 0.29, ajuste débil) → activa (dic 2024–nov 2025, b ≈ 0.44; segunda mitad b ≈ 0.80) → meseta (dic 2025–sep 2026, b ≈ −0.01, n=10). El ajuste de toda la serie (b ≈ 0.82, n=31, R² = 0.91) es un resumen grueso: no debe citarse solo.
3. **El sistema entró en Roche en nov–dic 2024, dos años antes del reconocimiento.** Roche-C (IPS) en nov 2024, Roche-R en dic 2024. El 2 nov 2026 no fue la entrada: fue el reconocimiento legal (Roche-S 0.463). **La corrección separa las dos entradas en un mes; la lectura de fondo no cambia, pero la secuencia es más precisa: la concentración precedió a la ruptura relativa en un mes.** Mar 2026 no mueve esta secuencia.
4. **La entrada a Roche-R coincide con el mes de la captura masiva en CDA.** Dic 2024 es a la vez el mes del cruce (R = 0.1021) y el inicio de la avalancha de fondeo (dic 2024–mar 2025: +Gs 1,755,304M, 91.75% no a préstamos). El mes focal del backcast pasa de nov 2024 a **dic 2024**: un mes después del retoque normativo del 12 nov 2024 (Res. 093-046/2024) y el mes en que la captura se vuelve masiva. La causa formal (paso 2 de φ) precede al cruce en un mes; el cruce y la captura son simultáneos.
5. **Una absorción puede ser ordenada y dejar ASI bajo.** 7 bancos licitantes, balance de exclusión en 15 días, FGD pagando — y ASI 0/5, 0/4, 0/5 en las tres unidades. El orden del proceso no restauró el control atómico: el FGD cubre el 0.011% de la exposición del IPS.
6. **La caída de dic 2025 (Ueno −12.5% en USD, R 0.264→0.228) sigue sin explicación en ningún documento.** Se registra como hueco, no se interpreta.
7. **El b depende del reloj.** El tramo abr–nov 2025 da 0.802, 0.906 o 0.344 según el origen de t. La meseta da −0.010, −0.011 o +0.007 según el origen. Cualquier b debe citarse con ventana + método + origen + n. **El 0.906 de v1 era un artefacto del origen; el valor consistente con la ventana dic 2024–nov 2025 es 0.802. Y los valores publicados de (c′) en v1/v2 eran secuenciales, no calendario (H-1, corregido en v3).**

## 12. Huecos y límites (actualizado en v3)

| Hueco | Estado |
|---|---|
| Inicio de la malversación | **Sin fechar.** El Informe BCP/P N.° 016 sigue sin aparecer en abierto. Lo que existe: **Nota BCP/P N.° 019** (directorio del BCP entregó la denuncia a Fiscalía con un informe de ~200 fojas) y un **informe sellado de 31 fojas al Senado** (respuesta a cinco pedidos de informes) que **NO precisa la fecha ni el monto total del exceso** en el límite de préstamos vinculados. Consecuencia: aunque apareciera el 016, es posible que tampoco fechara la malversación. El backcast fecha la **ruptura estructural** (nov–dic 2024), no el delito. Procedencia de la Nota 019 / informe de 31 fojas: GAP en la auditoría (C-37) — ese dato de v2 no proviene de ninguna de las 7 fuentes verificadas. |
| Roche-C mensual | **Sin serie.** El patrimonio efectivo solo existe en anclas (dic 2023, dic 2024, oct 2025, dic 2025, ene 2026, abr 2026). Sin serie mensual no hay trayectoria ni cruce al mes en base fondos totales (solo el primer punto computable, dic 2024). |
| ACO-A Δ | **Sin estimar.** No hay serie A(τ) para Ueno. |
| Leapfrog / reconciliación muro-b | **Pregunta abierta.** La hipótesis (eventos positivos = acciones que bajan R(t)) no está establecida. |
| Caída dic 2025 | **Sin explicación.** Ningún documento la comenta. |
| PDFs MEF faltantes | **6 meses:** 2023-01, 02, 03, 04, 05; 2024-08. (v2: 7, incluía 2026-03, ya recuperado.) **H-5:** hay 38 archivos en disco pero 39 filas marcadas "MEF PDF": dic 2023 está contado dos veces (su fila lleva totales del sistema pero el PDF no está en el directorio local). El "38" de v2 incluía dic 2023 y no mar 2026; el "38" actual incluye mar 2026 y no dic 2023. |
| Clasificación de oct 2024 (H-6) | **Detalle de archivo, no de número.** NOTAS §1 clasifica oct 2024 en el patrón "guion bajo", pero su URL real es del patrón genérico (`archivo_4.pdf`, según `download_log.csv` y el CSV). Con la corrección, el reparto real sería 16 estándar + 6 guion bajo + 16 genéricos = 38, no 16+7+15. R oct 2024 = 0.0780, verificado desde el PDF; el valor no cambia. |
| Discrepancia mar 2026 | **GAP de definición (nuevo en v3, §1.1).** Gs 557,038M solo en Gs; USD 235,381,762 sin conciliar aparte (+Gs 1,412,290,572,000 a FX 6,000); total en equivalentes Gs 1,969,328,585,754. No resuelta. |
| Periodo del incremento de intangibles (C-18) | **POR CONFIRMAR.** v1: solo en 2025; v2: 2024–2025. Monto (+Gs 654,799M) y total (Gs 761,444M) iguales en ambas. |
| Notificación 24 jul 2026 en φ paso 5 (C-17) | **GAP de traslado.** v1 la citaba; v2 la omitió sin motivo registrado. Pendiente de verificar contra parteaguas v2 §1.4. |
| R(t) 2023 | Ueno sin fila individual o dentro de OTROS BANCOS; no se imputa. |
| PE ago 2026 | Sin documentar (fecha de la cifra de salvadoras). La tensión salvadoras se reduce con el ancla abr 2026 (+4.9%) pero no se resuelve. |
| ASI = δH·α/F | **Sin calcular.** Sin serie de eventos de comportamiento para Ueno. Equivalencia con el conteo documental: pregunta abierta para Elán. |
| Cruce económico de Roche-S | **No fechable** con datos públicos (solvencia reportada > 12% hasta sep 2026; salto a 5.56% en nov 2026 tras previsiones). |

## 13. El backcast v3 — la escalera desde el 2 nov 2026

**Guarda v3.1 (lectura descriptiva, Claude 2026-11-09):** todo lo que sigue en esta sección es una lectura descriptiva de un solo caso, leída a posteriori sobre un caso ya ocurrido. No hay grupo de comparación, ni nulo, ni preregistro: las bandas y el backcast describen, no validan. La meseta (n=10, R² = 0.0007) solo respalda "sin tendencia", no una estructura. El b = 0.8234 de la serie completa es un descriptor de una serie acumulativa con autocorrelación fuerte, no una prueba.

El backcast es el recorrido inverso: desde el cruce del 2 nov 2026 hacia atrás, peldaño por peldaño, por las anomalías fechadas, hasta la ventana de inicio. Cada peldaño es un hecho documentado con fecha; la escalera no interpola entre peldaños. **Sin cambio de peldaños respecto a v2.** Mar 2026 (R = 0.2662) no añade peldaño: cae dentro de la meseta, no cruza ninguna banda y no es un hecho fechado nuevo de la escalera; la secuencia de bandas no cambia con él (ver §10).

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
| 4 | 2025 | Derechos Fiduciarios Gs 2,105,743M = 99.44% del patrimonio neto; Participación en otras sociedades +8,000% (Red Digital de Procesamientos Gs 640,468M; Red Digital Gs 236,231M); intangibles +Gs 654,799M (periodo por confirmar, C-18) | R nov 2025: 0.2643 | φ pasos 3 y 4: el balance se sostiene con saldos no líquidos |
| 3 | **dic 2024** | **Roche-R cruza 0.10 (R = 0.1021). Roche-C (fondos totales) = 1.08. Mes focal del backcast.** | **R = 0.1021** | **Entrada a Roche-R. Coincide con el inicio de la captura masiva en CDA (peldaño 5).** |
| 2 | nov 2024 | **Roche-C (base IPS) cruza 1.0 (1.06).** R = 0.0963 (corregido; antes 0.110) | R = 0.0963 | **Entrada a Roche-C.** La concentración precede a la ruptura relativa en un mes |
| 1 | 12 nov 2024 | **IPS Res. C.A. N.° 093-046/2024: eliminación del límite de patrimonio efectivo** (y baja de calificación requerida A-Py strong trend → genérica A) | R nov 2024: 0.0963 | **φ paso 2: la causa formal que habilita el cruce, un mes antes** |
| 0 | 9 nov 2023 | Licitación: puntaje mínimo 65 → 60 | R no se mueve | φ paso 1: pre-condición, no inicio |
| −1 | jul 2024 | **Salto: R 0.0338 → 0.0610 (+80.5%); Ueno total USD 104.4M → 186.4M (+78.5%). Fusión Visión efectiva 1 jul 2024; facilidades Gs 5.1 billones autorizadas 27 may 2024** | R = 0.0610 | **Peldaño anterior: el primer salto estructural, cinco meses antes de Roche-C** |

**Tres fechas (A/B/C) respecto al backcast v1 — sin cambio en v3:**

- **A — Entrada a Roche-C: nov 2024 (sin cambio).** Base IPS 1.06. Lo que cambia es que ya no comparte mes con Roche-R.
- **B — Entrada a Roche-R: dic 2024 (antes nov 2024).** R = 0.1021, con nov 2024 en 0.0963 y oct 2024 en 0.0780. La ventana de cruce es nov–dic 2024, cerrada al mes.
- **C — Mes focal del backcast: dic 2024 (antes nov 2024).** Es el mes en que (i) Roche-R cruza, (ii) Roche-C en base fondos totales cruza (1.08), (iii) empieza la captura masiva en CDA. Un mes después del retoque normativo del 12 nov 2024.

**Ventana de inicio corregida: jul–dic 2024.** El salto de jul 2024 es el peldaño anterior (cinco meses antes de Roche-C); la entrada a Roche es nov–dic 2024. **La lectura corregida: la entrada a Roche-R coincide con el mes en que empieza la captura masiva en CDA.** No hay interpolación a día: los datos son mensuales y el cruce se fecha al mes (nov–dic 2024), no a un día.

**Qué NO cambia en el backcast:** el 2 nov 2026 sigue siendo reconocimiento/trigger, no inicio; la malversación sigue sin fecha (solo el Informe BCP/P N.° 016 podría fecharla, y ni siquiera es seguro — ver §12); el salto de jul 2024 sigue siendo el primer peldaño estructural; los 5 pasos de φ siguen siendo los 5 eventos negativos del muro.

---

## Apéndice A — Método y reproducibilidad

- **Script:** `verificar_v3.py` (stdlib; sin dependencias externas; en este mismo directorio de staging). Lee `tabla-maestra-ueno-mef.csv` (45 filas), recomputa R(t) desde los componentes (USD×6,000 + Gs) y desde las columnas `ueno_total_usd_equiv` / `total_sistema_usd_equiv`, ajusta b por OLS log-log (log R = log a + b log t) por ventana, calcula (c′) en calendario y en secuencial (incluidos los controles v1/v2 que reproducen los valores de la auditoría), y verifica la aritmética de la discrepancia mar 2026.
- **Determinismo verificado:** la salida del script está guardada en `VERIFICACION_V3.md` (mismo directorio). Los valores v3 que este documento publica son los que el script recomputa; ningún número de v3 se corrigió inventando: lo que no reproduce se habría marcado GAP (no fue necesario: todo lo publicado en v3 reproduce).
- **Convención de t:** t es el mes calendario (meses desde el origen, con huecos cuando falta el PDF). **Origen nuevo para las ventanas posteriores a nov 2024: t=1 en dic 2024** (el mes del cruce de Roche-R). Las ventanas anteriores o que cruzan nov 2024 usan t=1 en feb 2024. La ventana de referencia nov 2024–nov 2025 usa t=1 en nov 2024. Cada b se reporta con su origen; la sensibilidad al origen se muestra con las variantes (b', b'', c', c''). **Nuevo en v3:** la variante (c′) también usa calendario (H-1 corregido); en la ventana v3 calendario y secuencial coinciden.
- **R(t) usa FX 6,000 por fila** (convención de la tabla). La sensibilidad a FX es ≤ 0.002 (verificada en la corrección: R nov 2024 = 0.0963 a FX 6,000, 0.0965 a FX 7,793).
- **Roche-C en base fondos totales** usa los fondos del CSV a FX 6,000 y las anclas de PE de NOTAS §12 (única fuente disponible; no hay serie mensual de PE).
- **Roche-S** usa las solvencias reportadas del parteaguas v2 (15.01% mar 2026, 14.5% jun, 13.85% sep, 5.56% 2 nov 2026).
- **b IPS** usa los tres puntos anuales de r_ips (0.0101, 0.0917, 0.2453; t=1,2,3).
- **Archivos v1 y v2 intactos:** `modelo-ueno-resultados.md` y `modelo-ueno-resultados-v2.md` no se tocaron. **No se tocó** el espacio, el podcast, el CSV ni las NOTAS.

## Apéndice B — Discrepancias registradas (actualizado en v3)

**Herencia de v1/v2 (se mantienen):**

1. Meseta n=8 en el brief → **n=10 en v3** (ene 2026 y mar 2026 ahora tienen R). La cifra de v1 (n=8) era correcta con los datos de v1; la de v2 (n=9) era correcta con los datos de v2.
2. Serie completa n=24 en v1 → n=30 en v2 → **n=31 en v3** (mar 2026). La variante (e') desaparece desde v2 (ya no hay ancla).
3. Cruce de 0.20: ≈24 jun 2025 (convención inicio de mes) vs ≈24 jul 2025 (fin de mes). Artefacto de convención; se adopta 24 jun 2025.
4. b IPS: 2.934 sobre r_ips vs 2.752 sobre participaciones vs 2.762 sobre montos. El 2.93 del documento es sobre r_ips.
5. Salvadoras 35% → PE implícito Gs 2.588 billones vs anclas conocidas (2.20 dic 2025, 2.467 abr 2026). Tensión reducida (+4.9% vs abr 2026) pero no resuelta.
6. Caída dic 2025 (Ueno −12.5% en USD, R 0.264→0.228): ningún documento la comenta.
7. Embargo Gs 2.1005 billones ≈ Derechos Fiduciarios Gs 2.105743 billones (−0.25%): coincidencia numérica, registrada como tal.
8. (a) 0.356 (anclajes doc) vs 0.342 (CSV) en v1 → **ambos retirados en v2** (artefacto del ancla con FX mezclado). Nuevo (a): 0.383 extremo / 0.436 OLS.

**De v2 (se mantienen):**

9. **Roche-C dic 2025: 1.89 (componentes exactos del CSV) vs 1.91 (NOTAS §12, con 4.2 billones redondeados).** Se usa 1.89; la diferencia es redondeo de entrada, no de método.
10. **Roche-C mar 2026: ≈2.08 (PE abr 2026 como proxy) vs ≈2.2 (NOTAS §12, con 5.2/2.4 redondeados).** Se usa ≈2.08, marcado como aproximado; la diferencia es redondeo + proxy de PE.
11. **Roche-C nov 2024 en base fondos totales: ≈1.15 con PE dic 2024 como proxy.** Supuesto, no medición; no se usa como fecha de entrada.
12. **Fondos dic 2024: cuatro cifras (PDF 1.687, balance 1.740, Asoban 1.747, ABC 1.76 billones) → Roche-C 1.08–1.13.** Todas > 1.0; la conclusión no depende de cuál se elija. Valor primario: 1.08 (PDF).
13. **Exposición IPS / fondos Ueno sep 2026: v1 decía 41.8% (CSV); v2 corrige a 41.7%** (348.5/834.825625 = 0.4175). Error de redondeo de v1.
14. **Meseta b: −0.046 (v1) → +0.031 (v2) → −0.0101 (v3).** Cambio de signo con R² ≈ 0.01 en v1/v2 y R² ≈ 0.001 en v3: ruido, no señal. La conclusión (sin tendencia) no cambia.
15. **NOTAS §9 sigue mostrando la pregunta del ratio de Roche como abierta** aunque el documento backcast la resolvió en tres ratios (C/R/S). Se usa el documento backcast como autoridad. NOTAS §12 aparece antes que §§10–11 en la numeración; no afecta los números.
16. **Oct 2024: la etiqueta de procedencia difiere** (el CSV dice archivo_4.pdf; NOTAS §§1/§12 lo atribuyen al patrón con guion bajo). El valor (R = 0.0780) está verificado desde el PDF; la procedencia es un detalle de archivo, no de número. Ver H-6 en el Ap. B #19.

**Nuevas en v3:**

17. **H-1 — (c′) secuencial vs calendario declarado.** v1 y v2 publicaron (c′) con numeración secuencial 1..n (v1 −0.0120, v2 +0.0086) aunque el Apéndice A declaraba calendario (v1 −0.0046, v2 +0.0104). En v3 (c′) es calendario: +0.0065, n=10, R² = 0.0048; calendario y secuencial coinciden en esta ventana. Auditoría §2.2, H-1.
18. **H-5 — conteo de PDFs.** 38 archivos en disco, 39 filas marcadas "MEF PDF": dic 2023 contado dos veces (totales del sistema en su fila, sin PDF local). El "38" de v2 incluía dic 2023 y no mar 2026; el "38" actual incluye mar 2026 y no dic 2023. Auditoría §2.9, H-5.
19. **H-6 — clasificación de oct 2024.** NOTAS §1 lo pone en el patrón "guion bajo"; su URL real es del patrón genérico (`archivo_4.pdf`). Reparto real 16 estándar + 6 guion bajo + 16 genéricos = 38, no 16+7+15. Detalle de archivo, no de número. Auditoría §2.9, H-6.
20. **Discrepancia mar 2026: GAP de definición.** Gs 557,038M solo en Gs; USD 235,381,762 sin conciliar aparte (+Gs 1,412,290,572,000 a FX 6,000); total en equivalentes Gs 1,969,328,585,754. v2 no la mencionaba. Auditoría §2.8.
21. **C-16 — φ paso 1.** v2 se atribuyó una corrección (70 → 60, sin fecha) que no existe: v1 ya decía 65 → 60 con fecha 9 nov 2023. El encabezado §6 de v2 ("Sin cambio") contradecía su propio paréntesis. Valor 65 → 60 sin cambio. Auditoría §5.3, C-16.
22. **C-17 — φ pasos 3–5.** Fechas estrechadas sin listar en v2: paso 3 2024–2025 → 2025; paso 4 2024 → 2025; paso 5 2024–2026 → jun–oct 2026, sin la notificación del 24 jul 2026. Sin motivo registrado. Auditoría §5.3, C-17.
23. **C-18 — φ paso 4, periodo de intangibles.** Mismo incremento (+Gs 654,799M) atribuido a "solo 2025" (v1) y a "2024–2025" (v2). Periodo POR CONFIRMAR en v3. Auditoría §5.3, C-18.
24. **C-30 — IPS 9.70%, año.** v2 decía 30 oct 2025; las fuentes del parteaguas (F5 `:47` y `:262`, F6 `:28`) dicen 30 oct 2026. Valor 9.70% sin disputa. Auditoría §3.7 y §5.3, C-30.

## Apéndice C — Qué debe cambiar en el espacio y en el podcast (pendiente, fuera de esta v3)

> **Para aplicar después, con el visto bueno de Elán. Esta v3 es solo el modelo en staging; no se ha tocado ni el espacio ni el podcast.**

El Apéndice C de v2 (19 cambios para el espacio, 10 para el podcast) sigue pendiente y sigue siendo la lista de referencia, con los números actualizados por esta v3 donde cambian:

- Espacio, C.1 #2: "31 meses con R, todos con PDF" (antes 30); nuevo mar 2026, R = 0.2662.
- Espacio, C.1 #6: b (c) meseta **−0.010 (n=10, R² = 0.001)** (antes +0.031, n=9).
- Espacio, C.1 #7: b (e) serie completa **0.823 (n=31, R² = 0.911)** (antes 0.819, n=30).
- Espacio, C.1 #18: **6 PDFs faltantes** (2023-01–05, 2024-08) (antes 7, incluía 2026-03).
- Podcast, C.2 #2: la meseta tiene b **−0.010**, no +0.031; la serie completa es **0.823**, no 0.819.
- Podcast, C.2 #8: "treinta y un meses con razón, todos con P D F, y la diferencia máxima es cero".
- Además, cuando se apliquen: corregir φ paso 1 (quitar la atribución falsa de corrección, C-16), precisar las fechas de φ pasos 3–5 (C-17), marcar el periodo de intangibles por confirmar (C-18), y corregir el año del 9.70% del IPS a 30 oct 2026 (C-30).

Los 10 cambios del Apéndice C.2 de v2 siguen sin aplicar en el podcast "v2" (auditoría §4.3); la regrabación sigue pendiente. Esta v3 no regraba ni reescribe el podcast: solo deja los números correctos para cuando Elán decida.
