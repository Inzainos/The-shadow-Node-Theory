# COPIA DE REGISTRO — Ueno v3 (corrección 2026-11-09)
# Archivo original: snt-taxonomia/tabla-maestra-NOTAS.md
# Versión: vigente (corregida; §§1-12 + §13, corrección noche 2026-11-06 y añadido 2026-11-07)
# Estado: archivo de registro — SIN CAMBIOS respecto al original. Cuerpo intacto; solo se añadió esta cabecera.
# Fecha de la copia: 2026-11-09
# md5 original: 761b2f71aad18322be90ab08b28c7e22
# sha256 original: 4ed85af8ed5efafe1f4dafacb618751e664cf9b0a3bfcd7c158866cd4ba771c4
#
# NOTA DE CORRECCIÓN (2026-11-09) — cabecera añadida a esta copia; el cuerpo queda intacto, sin reescribir.
# H-5 (auditoría REVISION_DOCUMENTOS_UENO.md §2.9): conteo de PDFs inconsistente en NOTAS vigente: 38 archivos en disco, 39 filas marcadas MEF PDF, dic 2023 contado dos veces (recuperado como archivo_5.pdf según §1/§12, pero sin archivo local; la fila 2023-12 figura como MEF PDF). El "38" de v2 no es el mismo "38" actual: el de v2 incluía dic 2023 y no mar 2026; el actual incluye mar 2026 y no dic 2023. Ningún documento advierte esta coincidencia.
# H-6 (auditoría §2.9): oct 2024 clasificado en NOTAS §1 en el patrón "guion bajo" (hacienda.gov.py), pero su URL real es https://www.mef.gov.py/sites/default/files/2024-11/archivo_4.pdf (patrón genérico; verificado en mef-informe-bancos/download_log.csv). Reparto real: 16 estándar + 6 guion bajo + 16 genéricos = 38, no 16+7+15.
#
# Tabla maestra Ueno — NOTAS de construcción y validación

Fecha: 2026-11-06/07. Corrección: noche del 2026-11-06 (ventana de b y ancla de nov 2024; ver §4 y §12).
Fuente primaria: MEF Paraguay, Informe de Bancos (Dirección General del Tesoro Público).
Documento base: `fondos-publicos-ueno-bank-adquisicion-datos-SNT-v2751__1__1_1e9t.md` (Paso 1 + Paso 6 del plan de adquisición).
Tabla: `~/workspace/snt-taxonomia/tabla-maestra-ueno-mef.csv` (45 filas, ene 2023 – sep 2026).
PDF: `~/workspace/snt-taxonomia/mef-informe-bancos/` (38 archivos `MEF_Informe_Bancos_AAAA-MM.pdf` + `download_log.csv` + `txt/` con el texto extraído).

Reglas aplicadas (del documento): R(t) = fondos públicos en Ueno / fondos públicos en el resto del sistema
(total menos Ueno). Series MEF / ABC / IPS en columnas separadas, sin mezclar definiciones. Tipo de cambio
registrado por fila. Celda sin fuente verificada queda vacía con nota. b es descriptor de deriva, no prueba
de mecanismo. Discrepancias registradas como incertidumbre, nunca corregidas en silencio.

## 1. PDFs descargados (38)

**Patrón estándar** — `https://www.mef.gov.py/sites/default/files/{AAAA-MM-publicación}/Informe%20de%20Bancos%20Web%20-%20{Mes}%20{AAAA}.pdf`
(publicación = informe + 1 mes). 16 informes: 2025-04, 2025-05, 2025-06, 2025-07, 2025-08, 2025-09, 2025-10,
2025-11, 2025-12, 2026-02, 2026-04, 2026-05, 2026-06, 2026-07, 2026-08, 2026-09.

**Patrón con guion bajo (dominio hacienda.gov.py)** — los informes de oct 2024 a mar 2025 y ene 2026 usan
`http://www.hacienda.gov.py/sites/default/files/{AAAA-MM-publicación}/Informe%20de%20Bancos%20Web_{Mes}%20{AAAA}.pdf`
(guion bajo en lugar de ` - `). 7 informes: 2024-10 (publicación 2024-11), 2024-11 (2024-12), 2024-12 (2025-01),
2025-01 (2025-02), 2025-02 (2025-03), 2025-03 (2025-04), 2026-01 (2026-02). La variante que los hizo
recuperables fue el guion bajo, no una carpeta distinta.

**Archivos genéricos "archivo (N)_M"** — los informes anteriores a 2025 no usan el nombre estándar. Se recuperaron
15 de la carpeta `2024-11` del MEF (los únicos con la tabla "Total de Saldos Bancarios"; el resto de esa carpeta
son decretos, resoluciones, manuales SINARH y otras presentaciones del Tesoro). Mes verificado por contenido
(fecha de cierre "al 30/31 de Mes de Año" en la propia tabla): 2023-06, 2023-07, 2023-08, 2023-09, 2023-10,
2023-11, 2023-12 (archivo_5.pdf), 2024-01, 2024-02, 2024-03, 2024-04, 2024-05, 2024-06, 2024-07, 2024-09.
Copiados con nombre normalizado; el origen (`archivo (N)_M`) consta en `download_log.csv`.

**Extracción**: `pdftotext -layout`. Tabla "Total de Saldos Bancarios de los OEE en el Sistema Financiero
Nacional — Clasificación por Entidad Bancaria" (sección USD y sección Gs; se toma la primera aparición de cada
banco por sección, porque el gráfico duplica los valores a la derecha). Verificación: la suma de los bancos
listados reproduce el TOTAL del informe en 36 de 38 PDFs (USD y Gs). Excepciones: 2023-06 y 2023-07 (USD),
donde dos filas están partidas en dos líneas por el PDF (jun 2023: REGIONAL 9,730,741 + CITIBANK 4,661,590 =
14,392,331 = diferencia exacta con el TOTAL; jul 2023: SUDAMERIS 11,292,035 + INTERFISA 10,050,000 =
21,342,035 ≈ diferencia 21,342,034, dif. 1 por redondeo). Los TOTALES del informe se usan tal cual; las filas
partidas no afectan a Ueno ni a los totales.

## 2. PDFs faltantes (6 de 45 meses)

2023-01, 2023-02, 2023-03, 2023-04, 2023-05, 2024-08. (2023-12: el PDF se recuperó como archivo_5.pdf según §1, pero NO está en el directorio local; en todo caso no es usable: Ueno dentro de "OTROS BANCOS".) Intentos: patrón estándar con mes de publicación +0/+1/+2 y variante "Setiembre";
sondeo HEAD de `archivo (N)_M` (n=1..15, m=1..6) en las carpetas 2024-11, 2024-12, 2025-01, 2025-02, 2025-03,
2025-04, 2026-02, 2026-04 — 0 aciertos fuera de 2024-11; búsquedas web de los informes nov/dic 2024 y
ene–mar 2025 sin resultado útil. Filas vacías en el CSV, sin inventar.

Cobertura parcial para meses sin PDF: **mar 2026 YA TIENE PDF** (recuperado 2026-11-07, ver §13): R_t ahora
calculable, **0.2662** (participación 0.2103), con el Gs exacto del PDF 3,721,013,013,754 (la serie ABC
redondeaba a 3,721,013,000,000). Nov 2024, dic 2024, ene–mar 2025 y ene 2026, antes cubiertos con anclas o serie ABC, YA TIENEN PDF (ver §1 y §12).

## 3. Validación de los anclajes del documento

Equivalentes en USD calculados con FX 6,000 (instrucción del documento).

| Ancla | Ueno FX 6,000 vs documento | Sistema FX 6,000 vs documento | R FX 6,000 vs documento | FX implícito (Ueno / sistema) |
|---|---|---|---|---|
| nov 2024 | **CORREGIDO (ver §12)**: PDF USD 47,965,843 + Gs 1,504,360,097,661 = 298.7M a FX 6,000 (documento: 271M, que usaba FX ≈ 6,696 para Ueno) | PDF USD 532,769,353 + Gs 17,196,008,927,451 = 3,398.8M a FX 6,000 (documento: 2,739M, que usaba FX ≈ 7,793 para el sistema) | **0.0963** (documento: 0.110) — R es casi invariante al FX: 0.0963 a 6,000; 0.0965 a 7,793 | Ueno ≈ 6,696 / sistema ≈ 7,793 |
| nov 2025 | 792.6M vs 722M (+9.8%) | 3,791.6M vs 3,357M (+12.9%) | 0.2643 vs 0.274 (−0.0097) | 6,760 / 6,996 |
| feb 2026 | 770.9M vs 728M (+5.9%) | 4,042.2M vs 3,828M (+5.6%) | 0.2357 vs 0.235 (+0.0007) ✓ | 6,504 / 6,461 |
| ago 2026 | 812.3M vs 835M (−2.7%) | 4,571.5M vs 4,571M (+0.0%) ✓ | 0.2161 vs 0.224 (−0.0079) | 5,771 / 6,001 |
| sep 2026 | 834.8M vs 855M (−2.4%) | 4,320.4M vs 4,320M (+0.0%) ✓ | 0.2395 vs 0.247 (−0.0075) | 5,805 / 6,001 |

**Lectura**: el FX 6,000 reproduce EXACTAMENTE los totales del sistema de jul/ago/sep 2026 (el artículo de ABC
usa FX 6,000 para el sistema), pero NO reproduce los totales de Ueno del documento en esos meses (dif. −2.4%
a −2.7%) ni los totales de nov 2025 (+9.8%/+12.9%) y feb 2026 (+5.6%/+5.9%). Los anclajes se publicaron con
tipos de cambio distintos por periodo: nov 2024 ≈ 6,696 (Ueno) / ≈ 7,793 (sistema); nov 2025 ≈ 6,760–6,996; feb 2026 ≈ 6,460–6,504;
jul 2026 ≈ 5,979 (Ueno); ago 2026 ≈ 5,771 (Ueno) con sistema a 6,000; sep 2026 ≈ 5,805 (Ueno) con sistema
a 6,000. El rango 6,000–6,700 que cita el documento (§3.1) NO cubre el FX implícito del sistema en nov 2025
(≈ 6,996) NI el del sistema en nov 2024 (≈ 7,793). No se forzó ningún FX: la tabla usa 6,000 en todas las filas PDF y registra el FX implícito por
ancla aquí. R(t) es mucho menos sensible al FX que los totales: con FX 6,000, R difiere del documento en
−0.010 (nov 2025), +0.001 (feb 2026), −0.008 (ago 2026), −0.008 (sep 2026), y −0.014 (nov 2024, corregido).

**Otras verificaciones que SÍ cierran**:
- Jul 2025 (documento §2.2): Ueno USD 139,991,357, Gs 3,033,632,265,311; totales USD 592,762,842,
  Gs 18,951,869,062,744 — coincidencia EXACTA con el PDF 2025-07.
- Ago 2026 (ancla verificada en vivo): Ueno USD 239,745,862 (19.9%), Gs 3,435,498,847,147 (17.0%);
  totales USD 1,207,017,455, Gs 20,186,996,090,438 — exacto.
- Serie ABC 2026 vs PDF: USD de Ueno exactos feb–sep; Gs exactos al millón feb–ago. Excepción: sep 2026,
  ABC publica Gs 3,608,850M y el PDF dice Gs 3,608,550,782,201 (dif. 299M Gs, 0.008%); se usa el PDF.
- Jul 2026: Ueno a FX 6,000 = 860.1M vs 862M del documento (−0.2%, esencialmente coincide).

## 4. Recálculo de b (ventana dic 2024 – nov 2025, t=1 en dic 2024) — CORREGIDO noche 2026-11-06

**Motivo de la corrección**: la ventana anterior (nov 2024 – nov 2025, b = 0.356) usaba como punto inicial el
ancla del documento (R = 0.110), que mezclaba tipos de cambio (Ueno a ≈ 6,696, sistema a ≈ 7,793). Con los
componentes del PDF de nov 2024 a tipo de cambio único, R(nov 2024) = 0.0963, no 0.110. La ventana correcta
empieza en dic 2024, primer mes con PDF verificado después del ancla corregida, y termina en nov 2025.

- **Pendiente extremo a extremo con los componentes del PDF** (R 0.1021 → 0.2643, t=1 → 12):
  b = ln(0.2643/0.1021)/ln(12) = **0.383**.
- **OLS log-log sobre los 12 meses con PDF de la ventana** (dic 2024 – nov 2025, t=1..12, R a FX 6,000):
  R: 0.1021, 0.1094, 0.1253, 0.1315, 0.1396, 0.1628, 0.1706, 0.2079, 0.2457, 0.2467, 0.2670, 0.2643 →
  b = **0.436**. Es el valor que debe citarse para la ventana dic 2024 – nov 2025.
- **Referencia con la ventana nov 2024 – nov 2025 corregida** (13 puntos, t=1 en nov 2024, R(nov 2024) = 0.0963):
  extremo a extremo b = ln(0.2643/0.0963)/ln(13) = **0.394**; OLS log-log b = **0.451**.
  El 0.356 anterior queda **retirado**: era un artefacto del ancla con FX mezclado.
- **Pendiente LOCAL de la segunda mitad** (abr–nov 2025, mismo origen t=1 en dic 2024, t=5..12):
  b = **0.802**. Sigue siendo mayor que la b de la ventana completa (0.436): la deriva se empinó en la
  segunda mitad. El 0.906 citado antes para esta subventana usaba otro origen de t (t=1 en nov 2024,
  t=6..13); la pendiente OLS log-log depende del origen de t, por eso aquí se reporta con el origen
  consistente de la ventana (t=1 en dic 2024). No sustituye al 0.436.
- Ya no falta ningún mes de la ventana: los 12 tienen PDF (nov 2024 – mar 2025 recuperados en esta corrección).

## 5. Serie R(t) obtenida (FX 6,000, PDF salvo indicación)

2024-02 0.0284 · 2024-03 0.0319 · 2024-04 0.0332 · 2024-05 0.0346 · 2024-06 0.0338 · 2024-07 0.0610 ·
2024-09 0.0777 · 2024-10 0.0780 · 2024-11 0.0963 (PDF, corregido; antes ancla doc. 0.110) · 2024-12 0.1021 ·
2025-01 0.1094 · 2025-02 0.1253 · 2025-03 0.1315 · 2025-04 0.1396 · 2025-05 0.1628 · 2025-06 0.1706 ·
2025-07 0.2079 · 2025-08 0.2457 · 2025-09 0.2467 · 2025-10 0.2670 · 2025-11 0.2643 · 2025-12 0.2280 ·
2026-01 0.2132 (PDF; antes serie ABC sin total) · 2026-02 0.2357 · 2026-04 0.2543 · 2026-05 0.2254 ·
2026-06 0.2246 · 2026-07 0.2306 · 2026-08 0.2161 · 2026-09 0.2395. Confirma el documento: subida
dic 2024 → nov 2025 (R cruza 0.10 en dic 2024, no en nov 2024) y meseta 0.21–0.25 en 2026.

Observaciones registradas en la tabla (no ajustadas):
- **Salto jul 2024**: Ueno USD 15.1M → 39.6M y Gs 536,147M → 880,971M en un mes (R 0.034 → 0.061).
  Visión Banco seguía listado por separado en esa fecha.
- **USD de Ueno feb–mar 2024 casi idéntico** (15,068,603 → 15,068,619; +USD 16) mientras Gs sube
  452,929M → 504,675M: posible cifra arrastrada; se registra sin ajustar.
- **Caída dic 2025**: Ueno USD −12.1% y Gs −12.6% vs nov 2025 (R 0.264 → 0.228) mientras el sistema
  sube; el documento no la comenta.
- **2023**: Ueno no figura en la tabla jun–ago 2023 (sin fila OTROS BANCOS; los bancos listados suman el
  TOTAL: saldo nulo o no reportado, no se imputa cero). Sep–nov 2023 está dentro de OTROS BANCOS
  (USD 18.4M / 15.9M / 21.7M agregados; Gs 669,582M / 791,508M / 822,858M). Dic 2023: dentro de
  OTROS BANCOS (USD 15,104,287; Gs 724,917,280,452); totales del sistema registrados en el CSV
  (USD 317,535,802; Gs 15,928,669,506,336), Ueno no extraíble. Ene 2024: USD dentro de
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
- **7 PDFs faltantes** del MEF (ver §2): 2023-01 a 2023-05, 2024-08 y 2026-03. Los informes de
  nov 2024, dic 2024, ene–mar 2025 y ene 2026 YA se recuperaron en esta corrección.
- **Total del sistema nov 2024**: el 2,739M del documento es el total del PDF a FX ≈ 7,793 (no a FX 6,000);
  queda registrado en §3 y §12, no como discrepancia sin explicar.

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

## 12. Corrección noche 2026-11-06: 8 PDFs recuperados, ancla nov 2024 y ventana de b

**Qué se recuperó**: los informes MEF de oct 2024, nov 2024, dic 2024, ene 2025, feb 2025, mar 2025
(patrón con guion bajo en hacienda.gov.py), dic 2023 (archivo_5.pdf en la carpeta 2024-11 del MEF) y
ene 2026 (guion bajo). Total: 38 PDFs (antes 30). Las 8 filas del CSV se reescribieron con los componentes
exactos del PDF (USD y Gs de Ueno y del sistema); R recomputado desde componentes y verificado contra el CSV.

**Ancla nov 2024, corregida**: el documento citaba Ueno 271M y sistema 2,739M con R 0.110. Esos dos totales
usan tipos de cambio distintos: Ueno a ≈ 6,696 (47M + 1,500,000M Gs / 271M) y sistema a ≈ 7,793
(532.8M USD + 17,196,008M Gs / 2,739M). Con los componentes del PDF a tipo de cambio único:
Ueno 298.7M, sistema 3,398.8M, **R = 0.0963** (0.0965 a FX 7,793: R es casi invariante al FX porque
numerador y denominador se mueven juntos). ABC Color (29 dic 2025) confirma los componentes:
"1,5 billones en guaraníes y 47 millones en dólares" para Ueno nov 2024, y sistema 2,739M.
El cruce de R = 0.10 se traslada de nov 2024 a **dic 2024** (R = 0.1021).

**Ventana de b, corregida**: dic 2024 – nov 2025, b OLS = **0.436** (extremo a extremo 0.383).
La ventana nov 2024 – nov 2025 corregida da OLS 0.451 / extremo 0.394. El 0.356 anterior queda retirado.
La pendiente local abr–nov 2025 con origen consistente (t=1 dic 2024) es 0.802 (antes 0.906 con otro origen
de t). Ver §4.

**Ene 2026**: el PDF da Ueno USD 132,844,442 + Gs 3,331,631,730,293 y sistema USD 939,279,352 +
Gs 17,856,614,782,382 → R = 0.2132. Reemplaza la serie ABC (solo Ueno, sin total). ABC acertaba en los
componentes de Ueno (redondeo a 3,331,631M Gs).

**Dic 2023**: el PDF no lista a Ueno individualmente; está dentro de OTROS BANCOS
(USD 15,104,287; Gs 724,917,280,452). Se registraron los totales del sistema; R no calculable.

**Anclas de patrimonio efectivo (PE) — NO forman parte del CSV** (no hay serie mensual de PE; son
puntos fechados, de balances y boletines del BCP citados por ABC Color). Se registran aquí porque el
documento las usa como referencia de solvencia, y porque PE ≠ patrimonio neto (ver abajo):

| Fecha | PE (Gs) | Fuente (vía ABC Color) |
|---|---|---|
| dic 2023 | 337,228M | ABC 14 jul 2026 (balance Ueno) |
| dic 2024 | 1.56 billones | ABC 12 jul 2026 / 14 jul 2026 (balance Ueno) |
| oct 2025 | 1.8 billones | ABC 30 dic 2025 (cuadro del legislador: inversiones IPS 2.1 billones vs PE 1.8 billones) |
| dic 2025 | 2.2 billones (US$ 335M) | ABC 14 jul 2026 / 22 sep 2026 (balance Ueno) |
| abr 2026 | 2.4 billones (US$ 410M, boletines BCP); tope 20% = 493,447M implica PE = 2,467,235M | ABC 12 oct 2026 (informe BCP EFS 8 jun 2026) |
| ene 2026 | > US$ 335M tras bonos subordinados (sin cifra exacta) | documento |

Ratios fondos públicos / PE (fondos a FX 6,000 del PDF, salvo indicación): dic 2024, 1.69 billones /
1.56 billones = 1.08; dic 2025, 4.2 billones (MEF, cit. ABC) / 2.2 billones = 1.91; mar 2026,
5.2 billones (ABC) / ≈ 2.4 billones = ≈ 2.2. ABC (14 jul 2026) cita 1.76 billones para dic 2024:
es el mismo saldo convertido a otro tipo de cambio (≈ 6,300), no una cifra distinta del PDF.

**Patrimonio efectivo ≠ patrimonio neto**: el PE es el indicador regulatorio de solvencia
(capital computable para absorber pérdidas, base de los límites del art. 59 Ley de Bancos, 20% para
vinculadas); el patrimonio neto es la cifra contable del balance. Al 31 dic 2025: PE 2.2 billones vs
patrimonio neto 2,117,665M (FIX, informe integral: 2,117,665.2 miles de millones → 2.118 billones;
ABC: 2,118 billones). Al 31 dic 2024: patrimonio neto 1,438,036.5M (FIX) vs PE 1.56 billones.
No mezclar: los límites legales (20% vinculadas, 10%/20% IPS) usan PE, no patrimonio neto.

## 10. Archivos

- Tabla: `~/workspace/snt-taxonomia/tabla-maestra-ueno-mef.csv`
- Notas: `~/workspace/snt-taxonomia/tabla-maestra-NOTAS.md` (este archivo)
- PDFs: `~/workspace/snt-taxonomia/mef-informe-bancos/` (38 PDF + `download_log.csv` + `txt/`)
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

## 13. Recuperación de los 8 PDFs faltantes (2026-11-07) — PENDING CERRADO

La auditoría de verificación 2026-11-07 encontró que 7 filas de la tabla (oct 2024, nov 2024, dic 2024,
ene–mar 2025, ene 2026) no tenían PDF local en el workspace (PENDING). El 2026-11-07 se descargaron los
8 PDFs por navegador (03:36–04:47 CST): oct 2024, nov 2024, dic 2024, ene 2025, feb 2025, mar 2025,
ene 2026 y mar 2026. Hallazgo de fuente: el informe NO está en el portal datos.hacienda.gov.py (su Lista
de Datos tiene solo 16 conjuntos, ninguno de bancos); está en el sitio principal del MEF, www.mef.gov.py,
Dirección General del Tesoro Público, sección "Entidades Depositarias de Fondos", que lista los 40 meses
de jun 2023 a sep 2026. URLs de los 8 en `download_log.csv` (reconstruido 2026-11-07: 38 OK, 7 MISSING —
2023-01–05, 2023-12, 2024-08 — sin discrepancias de bytes/SHA-256 contra el log anterior).

Verificación en local (pdftotext, 2026-11-07): los 8 son PDFs reales de 12 páginas, "INFORME DE SALDOS
DE OEE's EN EL SISTEMA FINANCIERO". **Los 4 valores de cada mes (Ueno USD, Ueno Gs, total sistema USD,
total sistema Gs) coinciden EXACTOS con la tabla** en los 7 meses PENDING; R_t recomputado desde los
componentes reproduce el CSV exacto (oct 2024 0.0780, nov 2024 0.0963, dic 2024 0.1021, ene 2025 0.1094,
feb 2025 0.1253, mar 2025 0.1315, ene 2026 0.2132). **El cruce Roche-R en dic 2024 (R = 0.1021), mes focal
del backcast, queda verificado contra su PDF fuente.** La anotación "dic 2024: 0.1021" del reel y del
video largo puede quedarse.

**Mar 2026 (nuevo):** el PDF da el total del sistema que la serie ABC no tenía (USD 1,033,055,423;
Gs 18,215,257,708,451) y el Gs exacto de Ueno 3,721,013,013,754 (la serie ABC redondeaba a
3,721,013,000,000). **R_t mar 2026 = 0.2662, participación 0.2103, ahora calculable** — fila actualizada
en el CSV. La discrepancia Tesoro-vs-balance (Gs 557,038M) sigue REGISTRADA, no resuelta. Consecuencia:
la serie R(t) pasa de 30 a 31 meses calculables; el backcast v2 (30 meses) NO se recalculó — ampliarlo
es decisión de Elán.
