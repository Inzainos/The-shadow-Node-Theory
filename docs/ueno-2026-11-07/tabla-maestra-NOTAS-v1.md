# COPIA DE REGISTRO — Ueno v3 (corrección 2026-11-09)
# Archivo original: snt-taxonomia/tabla-maestra-NOTAS-v1.md
# Versión: v1
# Estado: archivo de registro — SIN CAMBIOS respecto al original. Cuerpo intacto; solo se añadió esta cabecera.
# Fecha de la copia: 2026-11-09
# md5 original: b1daaaf57c4646926027a27cb0733705
# sha256 original: 6ba18a28c3d27a3e4df065b6d35e2c75e65049fae200ff8857de68238eb2c6cb
#
# Tabla maestra Ueno — NOTAS de construcción y validación

Fecha: 2026-11-06/07. Fuente primaria: MEF Paraguay, Informe de Bancos (Dirección General del Tesoro Público).
Documento base: `fondos-publicos-ueno-bank-adquisicion-datos-SNT-v2751__1__1_1e9t.md` (Paso 1 + Paso 6 del plan de adquisición).
Tabla: `~/workspace/snt-taxonomia/tabla-maestra-ueno-mef.csv` (45 filas, ene 2023 – sep 2026).
PDF: `~/workspace/snt-taxonomia/mef-informe-bancos/` (30 archivos `MEF_Informe_Bancos_AAAA-MM.pdf` + `download_log.csv` + `txt/` con el texto extraído).

Reglas aplicadas (del documento): R(t) = fondos públicos en Ueno / fondos públicos en el resto del sistema
(total menos Ueno). Series MEF / ABC / IPS en columnas separadas, sin mezclar definiciones. Tipo de cambio
registrado por fila. Celda sin fuente verificada queda vacía con nota. b es descriptor de deriva, no prueba
de mecanismo. Discrepancias registradas como incertidumbre, nunca corregidas en silencio.

## 1. PDFs descargados (30)

**Patrón estándar** — `https://www.mef.gov.py/sites/default/files/{AAAA-MM-publicación}/Informe%20de%20Bancos%20Web%20-%20{Mes}%20{AAAA}.pdf`
(publicación = informe + 1 mes). 16 informes: 2025-04, 2025-05, 2025-06, 2025-07, 2025-08, 2025-09, 2025-10,
2025-11, 2025-12, 2026-02, 2026-04, 2026-05, 2026-06, 2026-07, 2026-08, 2026-09.

**Archivos genéricos "archivo (N)_M"** — los informes anteriores a 2025 no usan el nombre estándar. Se recuperaron
14 de la carpeta `2024-11` del MEF (los únicos con la tabla "Total de Saldos Bancarios"; el resto de esa carpeta
son decretos, resoluciones, manuales SINARH y otras presentaciones del Tesoro). Mes verificado por contenido
(fecha de cierre "al 30/31 de Mes de Año" en la propia tabla): 2023-06, 2023-07, 2023-08, 2023-09, 2023-10,
2023-11, 2024-01, 2024-02, 2024-03, 2024-04, 2024-05, 2024-06, 2024-07, 2024-09. Copiados con nombre
normalizado; el origen (`archivo (N)_M`) consta en `download_log.csv`.

**Extracción**: `pdftotext -layout`. Tabla "Total de Saldos Bancarios de los OEE en el Sistema Financiero
Nacional — Clasificación por Entidad Bancaria" (sección USD y sección Gs; se toma la primera aparición de cada
banco por sección, porque el gráfico duplica los valores a la derecha). Verificación: la suma de los bancos
listados reproduce el TOTAL del informe en 28 de 30 PDFs (USD y Gs). Excepciones: 2023-06 y 2023-07 (USD),
donde dos filas están partidas en dos líneas por el PDF (jun 2023: REGIONAL 9,730,741 + CITIBANK 4,661,590 =
14,392,331 = diferencia exacta con el TOTAL; jul 2023: SUDAMERIS 11,292,035 + INTERFISA 10,050,000 =
21,342,035 ≈ diferencia 21,342,034, dif. 1 por redondeo). Los TOTALES del informe se usan tal cual; las filas
partidas no afectan a Ueno ni a los totales.

## 2. PDFs faltantes (15 de 45 meses)

2023-01, 2023-02, 2023-03, 2023-04, 2023-05, 2023-12, 2024-08, 2024-10, 2024-11, 2024-12, 2025-01, 2025-02,
2025-03, 2026-01, 2026-03. Intentos: patrón estándar con mes de publicación +0/+1/+2 y variante "Setiembre";
sondeo HEAD de `archivo (N)_M` (n=1..15, m=1..6) en las carpetas 2024-11, 2024-12, 2025-01, 2025-02, 2025-03,
2025-04, 2026-02, 2026-04 — 0 aciertos fuera de 2024-11; búsquedas web de los informes nov/dic 2024 y
ene–mar 2025 sin resultado útil. Filas vacías en el CSV, sin inventar.

Cobertura parcial para meses sin PDF: ene 2026 y mar 2026 usan la serie mensual 2026 de ABC Color reproducida
en el documento (solo Ueno Gs y USD; sin total del sistema, por lo que R_t no es calculable). Nov 2024 usa el
ancla del documento (ver §3).

## 3. Validación de los 5 anclajes del documento

Equivalentes en USD calculados con FX 6,000 (instrucción del documento), salvo nov 2024 (sin PDF).

| Ancla | Ueno FX 6,000 vs documento | Sistema FX 6,000 vs documento | R FX 6,000 vs documento | FX implícito (Ueno / sistema) |
|---|---|---|---|---|
| nov 2024 | sin PDF: componentes doc. USD 47M + Gs 1,500,000M; a FX 6,000 darían 297M (doc. 271M) | sin desglose USD/Gs del sistema: no verificable | 0.110 (doc.; no verificable) | Ueno ≈ 6,696 |
| nov 2025 | 792.6M vs 722M (+9.8%) | 3,791.6M vs 3,357M (+12.9%) | 0.2643 vs 0.274 (−0.0097) | 6,760 / 6,996 |
| feb 2026 | 770.9M vs 728M (+5.9%) | 4,042.2M vs 3,828M (+5.6%) | 0.2357 vs 0.235 (+0.0007) ✓ | 6,504 / 6,461 |
| ago 2026 | 812.3M vs 835M (−2.7%) | 4,571.5M vs 4,571M (+0.0%) ✓ | 0.2161 vs 0.224 (−0.0079) | 5,771 / 6,001 |
| sep 2026 | 834.8M vs 855M (−2.4%) | 4,320.4M vs 4,320M (+0.0%) ✓ | 0.2395 vs 0.247 (−0.0075) | 5,805 / 6,001 |

**Lectura**: el FX 6,000 reproduce EXACTAMENTE los totales del sistema de jul/ago/sep 2026 (el artículo de ABC
usa FX 6,000 para el sistema), pero NO reproduce los totales de Ueno del documento en esos meses (dif. −2.4%
a −2.7%) ni los totales de nov 2025 (+9.8%/+12.9%) y feb 2026 (+5.6%/+5.9%). Los anclajes se publicaron con
tipos de cambio distintos por periodo: nov 2024 ≈ 6,696; nov 2025 ≈ 6,760–6,996; feb 2026 ≈ 6,460–6,504;
jul 2026 ≈ 5,979 (Ueno); ago 2026 ≈ 5,771 (Ueno) con sistema a 6,000; sep 2026 ≈ 5,805 (Ueno) con sistema
a 6,000. El rango 6,000–6,700 que cita el documento (§3.1) NO cubre el FX implícito del sistema en nov 2025
(≈ 6,996). No se forzó ningún FX: la tabla usa 6,000 en todas las filas PDF y registra el FX implícito por
ancla aquí. R(t) es mucho menos sensible al FX que los totales: con FX 6,000, R difiere del documento en
−0.010 (nov 2025), +0.001 (feb 2026), −0.008 (ago 2026), −0.008 (sep 2026).

**Otras verificaciones que SÍ cierran**:
- Jul 2025 (documento §2.2): Ueno USD 139,991,357, Gs 3,033,632,265,311; totales USD 592,762,842,
  Gs 18,951,869,062,744 — coincidencia EXACTA con el PDF 2025-07.
- Ago 2026 (ancla verificada en vivo): Ueno USD 239,745,862 (19.9%), Gs 3,435,498,847,147 (17.0%);
  totales USD 1,207,017,455, Gs 20,186,996,090,438 — exacto.
- Serie ABC 2026 vs PDF: USD de Ueno exactos feb–sep; Gs exactos al millón feb–ago. Excepción: sep 2026,
  ABC publica Gs 3,608,850M y el PDF dice Gs 3,608,550,782,201 (dif. 299M Gs, 0.008%); se usa el PDF.
- Jul 2026: Ueno a FX 6,000 = 860.1M vs 862M del documento (−0.2%, esencialmente coincide).

## 4. Recálculo de b (ventana nov 2024 – nov 2025, t=1 en nov 2024)

- **Pendiente extremo a extremo con los anclajes del documento** (R 0.110 → 0.274, t=1 → 13):
  b = ln(0.274/0.110)/ln(13) = **0.356** (documento: 0.357; dif. 0.001, redondeo de R). **Reproduce el
  valor del documento.**
- **OLS log-log sobre los 8 meses con PDF dentro de la ventana** (abr–nov 2025, t=6..13, R a FX 6,000):
  R: 0.1396, 0.1628, 0.1706, 0.2079, 0.2457, 0.2467, 0.2670, 0.2643 → b = **0.906**. Es la pendiente
  LOCAL de la segunda mitad de la ventana (la aceleración abr–ago 2025), NO la b de la ventana completa.
  No sustituye al 0.356; muestra que la deriva se empinó en la segunda mitad.
- No se pudo hacer OLS sobre la ventana completa (nov 2024–mar 2025 sin PDF). Si aparecen esos informes,
  el OLS de 13 puntos es el siguiente paso.

## 5. Serie R(t) obtenida (FX 6,000, PDF salvo indicación)

2024-02 0.0284 · 2024-03 0.0319 · 2024-04 0.0332 · 2024-05 0.0346 · 2024-06 0.0338 · 2024-07 0.0610 ·
2024-09 0.0777 · 2024-11 0.110 (ancla doc.) · 2025-04 0.1396 · 2025-05 0.1628 · 2025-06 0.1706 ·
2025-07 0.2079 · 2025-08 0.2457 · 2025-09 0.2467 · 2025-10 0.2670 · 2025-11 0.2643 · 2025-12 0.2280 ·
2026-02 0.2357 · 2026-04 0.2543 · 2026-05 0.2254 · 2026-06 0.2246 · 2026-07 0.2306 · 2026-08 0.2161 ·
2026-09 0.2395. Confirma el documento: subida nov 2024 → nov 2025 y meseta 0.22–0.25 en 2026.

Observaciones registradas en la tabla (no ajustadas):
- **Salto jul 2024**: Ueno USD 15.1M → 39.6M y Gs 536,147M → 880,971M en un mes (R 0.034 → 0.061).
  Visión Banco seguía listado por separado en esa fecha.
- **USD de Ueno feb–mar 2024 casi idéntico** (15,068,603 → 15,068,619; +USD 16) mientras Gs sube
  452,929M → 504,675M: posible cifra arrastrada; se registra sin ajustar.
- **Caída dic 2025**: Ueno USD −12.1% y Gs −12.6% vs nov 2025 (R 0.264 → 0.228) mientras el sistema
  sube; el documento no la comenta.
- **2023**: Ueno no figura en la tabla jun–ago 2023 (sin fila OTROS BANCOS; los bancos listados suman el
  TOTAL: saldo nulo o no reportado, no se imputa cero). Sep–nov 2023 está dentro de OTROS BANCOS
  (USD 18.4M / 15.9M / 21.7M agregados; Gs 669,582M / 791,508M / 822,858M). Ene 2024: USD dentro de
  OTROS (11,236,858); Gs individual 453,353,383,656.

## 6. Columnas IPS (solo valores del documento; sin descargas del IPS)

- 2023 (fila 2023-12): CDA Gs 80,000M = 1.0% del inventario; total relevante DERIVADO 8,000,000M
  (80,000M ÷ 1.0%; porcentaje redondeado, total aproximado); r_ips = 0.0101.
- 2024 (fila 2024-12): CDA Gs 659,000M = 8.4%; total derivado 7,845,238M; r_ips = 0.0917.
- nov 2025 (fila 2025-11): exposición TOTAL Gs 2.2 billones / cartera IPS 19.6 billones (11.22%);
  r_ips = 0.1264 (base exposición total, distinta de las filas CDA; sin desglose CDA ese mes).
- 2025 (fila 2025-12): CDA Gs 1,602,000M = 19.7%; total derivado 8,132,487M; r_ips = 0.2453.
- mar 2026 (fila 2026-03): CDA Gs 1.5 billones / total CDA 9.36 billones (16.0%); r_ips = 0.1908.
- sep 2026 (fila 2026-09): CDA Gs 1.577 billones / total CDA 7.47 billones (21.1%); r_ips = 0.2676;
  exposición total Gs 2.03 billones / cartera 20.96 billones (9.69%) en notas.
- r_ips = exposición IPS en Ueno / exposición IPS en el resto. La base (CDA vs exposición total) se indica
  por fila en `notas`; no mezclar.

## 7. Discrepancia balance vs Tesoro (mar 2026, solo esa fila)

Balance Gs 3,163,975M vs Tesoro Gs 3,721,013M + USD 235M (Tesoro excede balance en Gs 557,038M).
REGISTRADA, no resuelta, en la columna `diferencia_balance_vs_tesoro`. La serie ABC/MEF-planilla de mar 2026
usa la cifra del Tesoro (Gs 3,721,013M).

## 8. Qué queda pendiente (fuera de este encargo)

- **IPS**: boletines mensuales de cartera del IPS (paso 2 del plan) — solo están los valores del documento.
- **Balances**: balances de Ueno Bank (paso 3) — solo la cifra de mar 2026 del documento.
- **Informe BCP/P N.° 016** (precintado, Senado) — única vía para fechar con precisión el inicio de la
  malversación (ver §9).
- **15 PDFs faltantes** del MEF (ver §2); en particular nov 2024, dic 2024, ene–mar 2025 y ene/mar 2026,
  que cerrarían la ventana de b y la meseta 2026.
- **Verificación del total del sistema nov 2024** (2,739M): sin desglose USD/Gs no es reproducible a FX 6,000.

## 9. Nota sobre el "ratio de Roche" y el BACKCAST (decisión de Elán, 2026-11-06 noche)

Elán: lo ocurrido el 2 nov 2026 fue SOLO el cruce del "ratio de Roche" (umbral de ruptura); la ratio ya
estaba quebrada desde que empezó la malversación, por lo que la fecha del evento es fecha de detonante, NO
de inicio del fallo. El inicio verdadero es cuando empezó la malversación (aún por fechar). Método nombrado
por Elán: **BACKCAST** — trabajar hacia atrás desde el cruce del 2 nov 2026 por las anomalías fechadas
(resolución IPS 12 nov 2024 que quitó el límite de renta variable; depósitos dic 2024–mar 2025
+Gs 1,755,304M con crédito neto +2%; fideicomiso / Derechos Fiduciarios 99.44% del patrimonio neto;
Participación en otras sociedades +8,000% en 2025) hasta una ventana aproximada de inicio: **fines de 2024**,
aproximada, no fecha probada. Pregunta abierta a Elán: qué ratio es el "ratio de Roche" — la ratio de
solvencia (5.56% vs 12% mínimo; resolución por debajo del 50% del mínimo) es la candidata principal; si se
confirma, se añade como columna a la tabla maestra para fechar el cruce. Elán propuso un pódcast para
presentar ese panorama backcast (encargo aparte, no hecho aquí).

## 10. Archivos

- Tabla: `~/workspace/snt-taxonomia/tabla-maestra-ueno-mef.csv`
- Notas: `~/workspace/snt-taxonomia/tabla-maestra-NOTAS.md` (este archivo)
- PDFs: `~/workspace/snt-taxonomia/mef-informe-bancos/` (30 PDF + `download_log.csv` + `txt/`)
- Scripts (reproducibilidad, en /tmp, no entregables): `/tmp/parse_mef.py`, `/tmp/parse_archivo.py`,
  `/tmp/build_master.py`, `/tmp/download_mef.py`, `/tmp/dl_archivo.py`, `/tmp/probe_folders.py`,
  `/tmp/probe_archivo.py`. El CSV se regenera con `python3 /tmp/build_master.py` (lee `txt/`).

## 11. Añadido: cifras IPS del tercer documento ("El parteaguas")

Documento: `~/workspace/user/files/analisis-completo-parteaguas-ueno_2_s54f.md` ("El parteaguas",
análisis completo de concentración, nodos sombra y colapso del hub en Ueno Bank). El CSV ya estaba cerrado
cuando llegó; por instrucción expresa estas cifras van en NOTAS, no en la tabla. Fuente de todas ellas:
auditoría de la Contraloría General de la República (CGR) vía ABC Color, 2026-09-15,
"CGR: Ueno Bank también domina la caja diaria del IPS y un quinto de sus inversiones en dólares"
(https://www.abc.com.py/economia/2026/09/15/cgr-ueno-bank-tambien-domina-la-caja-diaria-del-ips-y-un-quinto-de-sus-inversiones-en-dolares/).

**Por qué no entran en las columnas IPS del CSV**: las columnas `ips_ueno_cda_gs` / `ips_total_relevante` /
`participacion_ips` / `r_ips` son CDA en guaraníes (o exposición total donde así se indica). Estas tres cifras
son rubros distintos: Caja y Equivalentes no es CDA; el CDA en dólares es otra moneda y otra base (el
documento no da FX para convertirlo a Gs); los bonos son otro instrumento. Mezclarlos en esas columnas
rompería la regla de no mezclar definiciones. Quedan aquí, con su base explícita, para una eventual
ampliación de columnas.

- **Caja y Equivalentes del IPS en Ueno, 2024: Gs 665,685,348,380 + USD 12,241,087.73.** La CGR constató
  que Ueno lideró en 2024 la captación de este rubro, superando a entidades con mayor trayectoria y
  calificación crediticia. Es caja diaria (liquidez operativa para pagos), no inversión a plazo: el riesgo
  que mide es de corrida inmediata sobre el pago de haberes, distinto del de los CDA.
- **Bonos 2025: Gs 250,000,000,000** incorporados en 2025 (renta fija de mediano plazo; mismo artículo CGR/ABC).
- **CDA en dólares, cierre 2025: USD 27,427,000 = 19.95% del inventario de CDA en USD.** Composición
  verificada por suma: tres instrumentos por USD 15,127,000 + saldo heredado de Visión Banco por
  USD 12,300,000 = USD 27,427,000 exacto. Total implícito del inventario de CDA en USD (DERIVADO):
  USD 27,427,000 ÷ 19.95% ≈ USD 137,478,697. El documento señala que en 2023 Ueno no tenía participación
  relevante en dólares: el salto a 19.95% es íntegramente 2024–2025.

**Cruce con la tabla (sin conflicto)**: la tabla R(t) del documento (nov 2024: 271 / 2,739 / 0.110 / 9.89%;
nov 2025: 722 / 3,357 / 0.274 / 21.51%; feb 2026: 728 / 3,828 / 0.235 / 19.02%; ago 2026: 835 / 4,571 /
0.224 / 18.27%; sep 2026: 855 / 4,320 / 0.247 / 19.79%) es idéntica a los 5 anclajes ya validados en §3,
y enuncia b = 0.357 para nov 2024–nov 2025. También confirma: ago 2026 Gs 3.4 billones y USD 239.7M
(17.0% / 19.9%); IPS CDA en Gs de 1.0% (2023) a 19.7% (2025) con Gs 1.6 billones; solvencia 5.56% vs 12%
mínimo; exposición total del IPS USD 348.5M (coherente con Gs 2.03 billones de §6 a FX ≈ 5,830).
