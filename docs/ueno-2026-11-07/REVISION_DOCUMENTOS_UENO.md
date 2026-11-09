> **Nota v3.1 (2026-11-09):** la auditoría cita en §1.3 una anotación personal del autor que fue retirada de los documentos v3.1 por recomendación de auditoría (Claude, 2026-11-09). La auditoría se conserva como registro, sin reescribir su cuerpo.

# Revisión de TODOS los documentos de Ueno Bank — verificación completa contra documentación y datos fuente

**Fecha:** 2026-11-09
**Pregunta del autor (Elán, WhatsApp ~12:26):** "Revisa todos tus documentos que hiciste del ueno"
**Alcance:** todos los documentos de Ueno Bank listados en el encargo, leídos COMPLETOS, sin resumir destruyendo sustancia.
**Método:** lectura íntegra por 4 lectores paralelos con la misma regla (cita archivo:línea, GAP explícito si no está) + recomputación independiente en Python (stdlib) desde `tabla-maestra-ueno-mef.csv` y `tabla-maestra-ueno-mef-v1.csv`: R(t) = `ueno_total_usd_equiv / (total_sistema_usd_equiv − ueno_total_usd_equiv)` y desde componentes crudos (USD×6.000 + Gs); OLS log-log por ventana con origen de t declarado; aritmética Roche/ACO/IPS rehecha cifra por cifra.
**Reglas del autor aplicadas:** NUNCA ASUMAS, SIEMPRE VERIFICA contra la documentación, no contra la memoria. No construir sobre la idea del agente; construir solo sobre lo que ya está escrito. Lo que NO está se marca GAP, nunca se inventa. Un número retirado en v2 no se usa como vigente.
**No se tocó el espacio SNT, no se subió nada a GitHub, no se modificó ningún documento de Ueno.** Solo lectura, verificación y reporte.

## Veredicto en una frase

Sí se hizo Ueno Bank, y está hecho en v2, con casi todos sus números reproduciendo exactos. Pero **la v2 ya está desactualizada respecto a la tabla maestra vigente** (mar 2026 recuperado: 31 meses con R, no 30; meseta b +0,031 → −0,010; serie completa b 0,819 → 0,823), **el podcast episodio "v2" sigue hablando los números v1 retirados** (los 10 cambios del Apéndice C.2 de v2 no están aplicados), y **las notas backcast-roche y parteaguas-notas presentan la serie v1 como confirmada**. El reporte PDF de 9 páginas es el documento más limpio contra v2. Lo que no está en los papers ni en el modelo — puente, luz, disonancia — sigue fuera de estos documentos; aquí solo se verifica Ueno.

## 1. Inventario exacto

### 1.1 Modelo, valores, tabla maestra y NOTAS

| # | Archivo | Líneas | Fecha / versión | Qué cubre | Fuente que usa |
|---|---|---|---|---|---|
| 1 | `docs/ueno-2026-11-07/modelo-ueno-resultados.md` | 262 | 2026-11-06/07. **v1, registro** — queda intacta; sus números quedan RETIRADOS donde v2 los cambia | R(t), b por ventana, Roche-R/C/S, φ en 5 pasos, ASI documental, ACO-A, muro de 5 eventos, bandas, huecos. Tabla de 24 meses con R (23 PDF + 1 ancla) | `tabla-maestra-ueno-mef-v1.csv` + NOTAS-v1 (§§1–11), documento base de adquisición, parteaguas v2, backcast Roche. Script citado `/tmp/modelo_ueno.py` (fuera del corpus: NO VERIFICADO) |
| 2 | `docs/ueno-2026-11-07/modelo-ueno-resultados-v2.md` | 370, 50.878 B | 2026-11-06/07. **v2 (BACKCAST), vigente** como documento de resultados | Lo mismo que v1 + tabla de cambios v1→v2 (19 filas), backcast en 13 peldaños (§13), Apéndice C (qué debe cambiar en espacio y podcast, pendiente de visto bueno de Elán) | Tabla maestra CORREGIDA + NOTAS corregidas (§§1–12), documento base, parteaguas v2, backcast Roche. Script citado `/tmp/modelo_ueno_v2.py`, md5 declarado `306d4a5cfdefebbadb6c43abb86d8349` (hash NO comprobado en esta revisión) |
| 3 | `docs/ueno-2026-11-07/modelo-ueno-valores.csv` | 50 | v1 | 24 filas R(t) + 10 filas de ajustes b + 11 filas Roche | Tabla maestra v1 |
| 4 | `docs/ueno-2026-11-07/modelo-ueno-valores-v2.csv` | 63 | v2 | 30 filas R(t) + 13 filas de ajustes b + 15 filas Roche (añade base fondos totales en Roche-C) | Tabla maestra corregida (sin mar 2026) |
| 5 | `docs/ueno-2026-11-07/tabla-maestra-ueno-mef.csv` | 46 (1 cabecera + 45 filas), 12.335 B, **07 nov 10:48 — posterior al v2** | ene 2023 – sep 2026. **Vigente; incluye mar 2026 con PDF** | 45 meses; 39 filas con fuente "MEF PDF", 6 "sin PDF"; **31 meses con R_t calculable**; columnas IPS (CDA anual + cortes mar/sep 2026 + nov 2025 exposición total) y `diferencia_balance_vs_tesoro` (solo mar 2026) | 38 archivos PDF en `mef-informe-bancos/` + valores del documento (IPS, parteaguas) |
| 6 | `docs/ueno-2026-11-07/tabla-maestra-ueno-mef-v1.csv` | 46 (1 + 45) | ene 2023 – sep 2026. **v1, registro** | 45 meses; 30 filas "MEF PDF", 12 "sin PDF", 3 ancla/ABC; **24 meses con R_t** | 30 PDFs + ancla del documento (nov 2024) + serie ABC/MEF-planilla (ene y mar 2026) |
| 7 | `docs/ueno-2026-11-07/tabla-maestra-NOTAS.md` | 294 | 2026-11-06/07, corrección noche 2026-11-06 (§12) y añadido 2026-11-07 (§13) | Construcción y validación de la tabla vigente: PDFs (38), faltantes, validación de 5 anclajes, recálculo de b, serie R(t), columnas IPS, discrepancia balance/Tesoro, pendientes, nota Roche/backcast, corrección de 8 PDFs, anclas de patrimonio efectivo (§12), cifras IPS del parteaguas (§11), recuperación mar 2026 (§13). **Numeración desordenada: §12 va antes que §§10–11** | MEF Informe de Bancos; documento base; parteaguas; CGR vía ABC 2026-09-15 |
| 8 | `docs/ueno-2026-11-07/tabla-maestra-NOTAS-v1.md` | 195 | 2026-11-06/07. **v1, registro** | Lo mismo sin la corrección: 30 PDFs, 15 faltantes, b ventana nov 2024–nov 2025, ancla nov 2024 sin corregir | MEF (30 PDFs); documento base; parteaguas |

Conteo de PDFs en disco (verificado por `ls`): 38 archivos `MEF_Informe_Bancos_*.pdf`. No existe `MEF_Informe_Bancos_2023-12.pdf` en disco — ver hallazgo H-5 en §2.9.

### 1.2 Forecast, ACO-A/tela, rastro, backcast, parteaguas, Finanzas-mundo

| # | Archivo | Líneas | Fecha / versión | Qué cubre | Fuente que usa |
|---|---|---|---|---|---|
| 9 | `docs/ueno-2026-11-07/forecast-ueno-2026-11-06.md` | 315 | 2026-11-06/07; sin nº de versión; punto de partida v2 | Forecast desde el 2 nov 2026: FGD, absorción/redistribución (escenarios A/A5/B/C/D), embargo, salvadoras, megacuentas, proceso legal, cadena política, IPS, lectura SNT, huecos, vigilancia | v2 + tela + parteaguas v2; MEF sep 2026 (cifras preliminares); scripts `/tmp/forecast_ueno.py`, `/tmp/forecast_csv.py` (L3, L293–299) |
| 10 | `docs/ueno-2026-11-07/forecast-ueno-valores.csv` | 71 | Sin fecha interna; md5 declarado `cce53a6cbdbe53e425779633743958af` (forecast L3) | Valores del forecast: base sep 2026 por banco (16), escenarios A/A5/B/C, FGD, IPS, embargo, hitos/fechas | MEF sep 2026; mismo script. **md5 recomputado = `cce53a6cbdbe53e425779633743958af` — coincide** |
| 11 | `docs/ueno-2026-11-07/ueno-acoa-tela-cimatica-incertidumbre.md` | 394 | 2026-11-07; marco SNT v2.7.5.1 / marco v34 | Forma ACO-A, firma cimática (FFT), huella, LOO, tendencia en tela de incertidumbre, huecos | Tabla maestra CORREGIDA (45 filas, 30 meses) + v2; repo `snt-repo` HEAD a3cd14c, `tela_cimatica.py` / `tela_de_incertidumbre.py` verbatim; script `/tmp/ueno_tela.py` (L3–11, L365–394) |
| 12 | `docs/ueno-2026-11-07/ueno-huella-cimatica.csv` | 3 (cabecera + 2 filas) | Sin fecha interna | Huella cimática: ventana primaria dic 2024→nov 2026 + sensibilidad feb 2024→sep 2026; log₁₀m en τ=0/0,25/0,5/0,75/1, log máx, A1/A2/A3 | Mismo formato que `tela_cimatica_huellas.csv` (tela L181–196) |
| 13 | `docs/ueno-2026-11-07/rastro-del-dinero-ueno.md` | 65 | 2026-11-07; nota de Elán 2026-11-07 ~03:17 "[anotación personal retirada en v3.1]" (L3, original) | Rastro del dinero: fondeo público, avalancha dic 2024–mar 2025, salvadoras/vinculadas/fideicomiso, embargo, qué quedó, huecos | Tabla maestra v2 (38 PDFs), v2, forecast 2026-11-06, parteaguas v2; "nada nuevo, nada inventado" (L5) |
| 14 | `docs/ueno-2026-11-07/backcast-roche-notas.md` | 84 | 2026-11-06/07; notas sobre `backcast-roche-ueno_4_54ov.md` ("cuarto documento") | Backcast Roche: 3 ratios C/R/S, ventana de inicio, 3 fechas, muro de 5 eventos, corrección leapfrog | Tabla maestra (45 filas) + notas; verificación de Mole 2026-11-06 (L48–49) |
| 15 | `docs/ueno-2026-11-07/parteaguas-notas.md` | 82 | Sin fecha propia; doc v1 subido 2026-11-06 noche; **v2: 313 líneas, subido 2026-11-06 ~20:14** (L44) | Notas sobre el "tercer documento" (parteaguas): tesis, φ, salvadoras, ASI/ACO-A, v2 con cambios | `analisis-completo-parteaguas-ueno_2_s54f.md` y `analisis-completo-parteaguas-ueno__1__3_xnox.md` |
| 16 | `docs/ueno-2026-11-07/finanzas-mundo-snt.md` | 258 | 2026-11-07; Banco Mundial API v2, 24 indicadores, descargados 2026-11-07 | Primera aplicación SNT a dominio nuevo tras Ueno: flujo/luz/hub/sombra/puente mundo, R-análogo por país, bandas tipo Roche, fichas, gaps | Banco Mundial WDI+GFDD (216 países, 11.948 filas, 1960–2024); molde Ueno = v2 + rastro (L3–5, L18) |

### 1.3 Reporte PDF, podcast, videos

| # | Archivo | Tamaño / extensión | Fecha (mtime) | Versión / estado | Qué cubre |
|---|---|---|---|---|---|
| 17 | `goals/shadow-node-theory-ueno-live-case-and-per-domain-taxonomy/files/reporte-investigacion-ueno-bank/reporte-investigacion-ueno-bank.pdf` | 231.775 B, **9 páginas** A4 (verificado con `pdfinfo`: 9 páginas, creado 2026-11-07 17:50 UTC), 398 líneas de texto extraído | 2026-11-07 17:50 | Informe de investigación, **modelo v2**, fecha del informe 7 nov 2026 | Portada + resumen ejecutivo + §§1–8: pregunta/método, serie R(t), tres bandas Roche, φ en 5 pasos + avalancha + salvadoras, backcast, absorción/ASI/muro, hitos (5 y 17 nov), huecos; material complementario con enlaces YouTube/LinkedIn |
| 18 | `docs/ueno-2026-11-07/podcast-backcast-ueno/script.txt` | 16.622 B, 55 líneas, 2.774 palabras, 28 turnos Mole + 27 Lucía | 2026-11-07 02:02 | **Episodio v1** (previo al modelo v2) | Backcast narrado: resolución 2 nov, marco, serie R(t), b, φ, avalancha, salvadoras, embargo, FGD, cierre con CAME |
| 19 | `docs/ueno-2026-11-07/podcast-backcast-ueno/script-v2.txt` | 19.716 B, 53 líneas, **3.334 palabras**, 27 turnos Mole + 26 Lucía | 2026-11-07 04:10 | **Llamado "v2", pero con números v1** (ver §3.2) | Episodio "con la tabla maestra aprobada": correcciones malversación y Roche, serie, b por regímenes, φ, salvadoras, ASI, muro, absorción, cadena posterior |
| 20 | `docs/ueno-2026-11-07/podcast-backcast-ueno/topics.txt` | **NO EXISTE** | — | — | **GAP de inventario:** el archivo pedido como `topics.txt` no está en el directorio. El archivo v1 real es `topics.md` |
| 21 | `docs/ueno-2026-11-07/podcast-backcast-ueno/topics.md` | 1.966 B, 12 viñetas, 330 palabras | 2026-11-07 02:03 | Temas del episodio **v1** | Lista de temas del script v1 (backcast, Roche, b = 0.357, φ 70→60, salvadoras, BCP/P 016, FGD, CAME) |
| 22 | `docs/ueno-2026-11-07/podcast-backcast-ueno/topics-v2.md` | 2.312 B, 13 viñetas, 374 palabras | 2026-11-07 04:10 | Temas del episodio **"v2"**, con números v1 | Lista de temas del script-v2 (números finales v1, regímenes de b, Roche, φ, ASI, muro, absorción, cadena, CAME) |
| 23 | `docs/ueno-2026-11-07/video-largo-ueno/guion-video-largo.txt` | 18.352 B, 69 líneas, 3.015 palabras | 2026-11-07 12:24 | **BORRADOR**, 12 capítulos, ~13 min, 16:9 1280×720 | Video largo: teoría, hub, luz, R(t)/avalancha, backcast, Roche ×3, dinero/salvadoras, caída, forma ACO-A/tela, embargo, forecast, cierre |
| 24 | `docs/ueno-2026-11-07/video-largo-ueno/capitulos.txt` | 1.138 B, 19 líneas | 2026-11-07 12:32 | Marcas de corte para Elán | 15 segmentos (C1, C9 y C11 partidos en dos), duración total declarada 13:02 (782,39 s) |
| 25 | `docs/ueno-2026-11-07/video-resumen-ueno/guion-video.txt` | 5.633 B, 31 líneas, 983 palabras | 2026-11-07 05:45 | Guion resumen, 9 secciones (0–8) | Resumen: backcast, b, telas/forma, forecast, EFIPEM (control México), cierre |

Archivos adyacentes no pedidos pero relevantes, solo como contexto de fechas: `episodio.mp3` 8.030.245 B, 2026-11-07 02:08 (tras script.txt 02:02); `episodio-v2.mp3` 9.339.109 B, 2026-11-07 04:21 (tras script-v2.txt 04:10); `video-largo-ueno-paraguay.mp4` 20.221.914 B, 2026-11-07 12:32; tres variantes mp4 del resumen (05:57/06:03/06:38). **El contenido de audio/video no se escuchó ni se vio en esta verificación** — solo se verificaron los guiones escritos; el audio se evalúa por su guion fuente y su marca temporal. El PDF es el documento más tardío (17:50) y su fuente `.src/OUTLINE.md` (no pedida, leída como apoyo) cita como fuentes modelo v2 §§1–13 y forecast §§1–2, 8–9, y sus afirmaciones coinciden con v2.

### 1.4 Documentos fuente subidos por Elán (`fuentes del autor (no incluidas en el repo)`, todos 2026-11-07)

| # | Archivo | Líneas | Bytes | md5 |
|---|---|---|---|---|
| F1 | `fondos-publicos-ueno-bank-adquisicion-datos-SNT-v2751__1__1_1e9t.md` | 197 | 36.170 | `6a0d03b704a79b337239cdbc4e7aebc4` |
| F2 | `tabla-maestra-ueno-NOTAS__1__0_bosm.md` | 268 | 21.450 | `941ce3d028c46ac01f51eb9cfdbfdf3f` |
| F3 | `tabla-maestra-ueno-NOTAS_5_4x2a.md` | 195 | 15.232 | `b1daaaf57c4646926027a27cb0733705` |
| F4 | `analisis-completo-parteaguas-ueno_2_s54f.md` | 276 | 40.181 | `d72a85c3a8a611899eefd7afe99f92d4` |
| F5 | `analisis-completo-parteaguas-ueno__1__3_xnox.md` | 313 | 52.963 | `70843eee02f2cfed870ba4bec9d333fa` |
| F6 | `backcast-roche-ueno_4_54ov.md` | 79 | 9.357 | `214e9a23c5798fe248048da30d88d114` |
| F7 | `global-bank-public-deposits-pattern_0_bjlt.md` | 191 | 41.232 | `c4989e64625365be13cc09365a6b487d` |

**Relación F2/F3 (clave):** F3 es la versión **antigua** (30 PDFs, ancla 0.110, b 0.356) y F2 es la **corregida** (noche 2026-11-06, 38 PDFs, ancla 0.0963, b 0.436). F3 es byte-idéntica a `docs/ueno-2026-11-07/tabla-maestra-NOTAS-v1.md` (mismo md5 `b1daaaf5…`). **F2 sustituye a F3 en todos los números que cambian; citar F3 como vigente es un error.** Observación: el `tabla-maestra-NOTAS.md` canónico en `docs/ueno-2026-11-07/` tiene md5 distinto de F2 y de F3 (`761b2f71…`, mismo tamaño 15.232 B que F3) — queda como punto a aclarar cuál NOTAS es la vigente en disco; no se resolvió en este pase.

- **F1** — Documento base de todo el trabajo. Qué significa "fondos públicos" en cada fuente (MEF, IPS, BCP, CGR); verificación de la serie MEF e IPS; reconstrucción de R(t) con 5 anclas y ajuste de b; discrepancia balance vs Tesoro mar 2026 y crecimiento del balance 2025; ACO-A/ASI y megacuentas; 7 datos faltantes; **plan de adquisición en 7 pasos** (§7). Anclas: nov 2024 (271M, R 0.110), nov 2025 (722M, R 0.274), feb 2026 (728M, R 0.235), ago 2026 (835M, R 0.224), sep 2026 (855M, R 0.247) — `fondos…1e9t.md:76-77`; b = 0.357 (`:90`); b IPS = 2.93 (`:94`); FGD 75 SM = Gs 228.300.000, primer pago Gs 10.000.000, ~32.000 jubilados, 7 bancos (`:122` y §5); megacuentas Gs 3.7 billones = 177.5% del patrimonio neto (§5).
- **F2** — NOTAS corregidas. 38 PDFs con patrones de URL (§1); 7 PDFs faltantes (§2); validación de los 5 anclajes con FX implícito por ancla (§3, `:59-60`); **recálculo de b corregido** — ventana dic 2024–nov 2025, OLS 0.436, extremo 0.383 (§4); serie R(t) completa (§5, `:109`); columnas IPS (§6); discrepancia mar 2026 (§7, `:146`); pendientes (§8); nota Roche/BACKCAST con decisión de Elán (§9, `:171`); archivos y scripts (§10); cifras IPS del parteaguas que NO entran al CSV (§11, `:263-267`); **corrección §12** — 8 PDFs recuperados, ancla nov 2024 corregida a R 0.0963 (`:182-183`), anclas de patrimonio efectivo (PE) con tabla dic 2023–abr 2026 y distinción PE ≠ patrimonio neto. Anomalía de numeración: §12 aparece antes que §§10–11.
- **F3** — NOTAS antiguas, pre-corrección: 30 PDFs, 15 faltantes, b extremo 0.356, b local abr–nov 2025 = 0.906, serie R(t) con nov 2024 = 0.110 ancla. **Todos sus números de ventana/ancla están retirados por F2.** Conserva valor como registro de lo que se corrigió y por qué.
- **F4** — Parteaguas v2 (`_2_s54f`, 276 líneas). Marco R(t)/b/φ/ACO-A/ASI; 4 dominios; meta-dominio comparativo global con **5 casos** (Ueno, Master, Fassil, SVB/First Republic, CAME); taxonomía por dominio; nodos sombra: 3 pruebas; colapso y absorción. Aporta tabla R(t) con los 5 anclajes viejos (`:19-20`), b 0.357 y ×2.49 (`:25`), megacuentas, circuito salvadoras, embargo, Caja y Equivalentes 2024 (`:67`), CDA USD 27.427.000 = 19.95% (`:77`). **No contiene:** §1.4 del trigger, denuncia MEF, imputación a 27 personas, USD 146M a vinculadas, ni trayectoria de solvencia 15.01/14.5/13.85%.
- **F5** — Parteaguas v2 (`__1__3_xnox`, 313 líneas). Misma base que F4 (37 líneas más) con material decisivo: caja "Cómo leer este informe"; §1.3 con ASI definido correctamente como **Índice de Soberanía Atómica**; **§1.4 el trigger del 2 nov** — USD 146M a vinculadas sep 2025–may 2026, informe supervisión 8 jun 2026, notificaciones 5 jun / 24 jul 2026, solvencias 15.01% mar / 14.5% jun / 13.85% sep → 5.56%, inspección 31 oct, IPS 9.70% el 30 oct, denuncia MEF por presunta malversación Gs 250.000M + Gs 123.838M intereses, imputación a 27 personas (`:47`); §4.3 φ fechado (puntaje 65→60 el 9 nov 2023); §9.1 secuencia fragilidad→trigger→cadena; §9.3 evaluación ASI. Es la versión del parteaguas que el v2 usa como autoridad para φ, Roche-S y la cadena penal.
- **F6** — Backcast Roche (79 líneas). Definición operativa de Roche en tres versiones — Roche-C (fondos/PE > 1.0), Roche-R (R(t) > 0.10), Roche-S (solvencia/12% < 0.50) (`:15-17`); backcast en 7 pasos hacia atrás desde el 2 nov 2026 (`:31-33`, facilidades Gs 5.1 billones autorizadas 27 may 2024 y fusión Visión 1 jul 2024); tres fechas A/B/C (`:39`, `:42`); tabla de verificación Roche-C (`:54` y §5); qué NO concluye (§4, `:50-52`); pendientes (§7). **Usa el ancla vieja R = 0.110** (`:5`, `:31`, `:39`, `:42`) — anterior a la corrección de F2.
- **F7** — Global comparative (191 líneas, en inglés). Marco de las tres concentraciones (pasivo, activo, gobernanza); **17 casos en tabla comparativa** — Ueno, Fassil, Master, SVB, Iceland/Icesave, Banco Espírito Santo, Banco Popular, Cyprus/Laiki, Credit Suisse, Baoshang, Henan, PMC Bank, Yes Bank, VBS, Ghana, Lebanon, Northern Rock; **4 marcadores** que separan concentración normal de patológica (prima de tasa/inducement, velocidad, concentración conectada de activos, captura de gobernanza + supervisión tardía); límite Basilea de grandes exposiciones 25% (15% entre G-SIBs); **5 modelos de resolución**; implicaciones para Paraguay. Datos Ueno propios: depósitos públicos ~USD 850M dentro de depósitos totales ~USD 2.800M (30.4%), ~3 millones de clientes, solvencia por debajo del 50% del mínimo. **Ninguna cifra de R(t), b, Roche, IPS ni PE.**


## 2. Verificación numérica

Leyenda: **VERIFICADO** = coincide con la fuente / aritmética correcta. **RETIRADO** = número v1 que v2 retiró expresamente y que un documento usa como vigente. **INCONSISTENTE** = contradice v2 o la tabla vigente. **NO VERIFICABLE** = no está en v2 ni se deriva de él con los archivos leídos (no es falso, es fuera de alcance). **GAP** = el propio documento lo marca como hueco.

### 2.1 R(t) — desde la tabla maestra vigente

**VERIFICADO.** Recomputada fila por fila desde las columnas de equivalentes y desde los componentes crudos (USD + Gs/6.000): **las 31 filas con R reproducen el CSV exacto (diferencia 0,0000 en todas)**, y la participación reproduce igual (muestreo: 2024-11 0,0879; 2025-11 0,2090; 2025-12 0,1857; 2026-03 0,2103 — todos exactos).

Serie vigente (31 meses): 2024-02 0,0284 · 03 0,0319 · 04 0,0332 · 05 0,0346 · 06 0,0338 · 07 0,0610 · 09 0,0777 · 10 0,0780 · 11 0,0963 · 12 0,1021 · 2025-01 0,1094 · 02 0,1253 · 03 0,1315 · 04 0,1396 · 05 0,1628 · 06 0,1706 · 07 0,2079 · 08 0,2457 · 09 0,2467 · 10 0,2670 · 11 0,2643 · 12 0,2280 · 2026-01 0,2132 · 02 0,2357 · **03 0,2662 (nuevo, no está en v2)** · 04 0,2543 · 05 0,2254 · 06 0,2246 · 07 0,2306 · 08 0,2161 · 09 0,2395.

- **v1 (24 meses): VERIFICADO en su marco.** Las 24 filas reproducen, salvo nov 2024 con diferencia −0,0002 (0,1100 CSV vs 0,1098 recalculada) — exactamente lo que v1 declara (`modelo-ueno-resultados.md:14-51`, `modelo-ueno-valores.csv` fila 2024-11). El ancla mezclaba FX: Ueno ≈6.696, sistema ≈7.793 (`tabla-maestra-ueno-mef-v1.csv` fila 2024-11; `tabla-maestra-NOTAS.md:175-226` §12).
- **v2 (30 meses): VERIFICADO en su marco.** Diferencia máxima 0,0000 (`modelo-ueno-resultados-v2.md:39-82`).
- **INCONSISTENTE (v2 vs tabla vigente):** v2 afirma "30 meses con R calculable, todos con PDF" (`modelo-ueno-resultados-v2.md:39-82`, tabla de cambios #2, #18) y "Huecos: mar 2026 (sin total del sistema)" (`modelo-ueno-resultados-v2.md:80`). La tabla vigente tiene **31 meses**: mar 2026, R = 0,2662, participación 0,2103, fuente MEF PDF (`tabla-maestra-ueno-mef.csv:40`; `tabla-maestra-NOTAS.md:49-50,289-293` §13). La propia NOTAS §13 lo reconoce: "la serie R(t) pasa de 30 a 31 meses calculables; el backcast v2 (30 meses) NO se recalculó — ampliarlo es decisión de Elán". **v2 queda desactualizada en este punto; no es un error de cálculo, es un desfase temporal documentado.**
- **Consecuencia no calculada en ningún documento:** mar 2026 (0,2662) es el **máximo de la meseta 2026 y supera nov 2025 (0,2643)**. El rango de meseta que v2 cita ("0,213–0,254", `modelo-ueno-resultados-v2.md:39-82` y §11) pasa a ser **0,2132–0,2662** con la tabla vigente.
- Salto jul 2024 R 0,034→0,061 (+80,5%; Ueno USD 104,4M→186,4M, +78,5%) **VERIFICADO**; USD feb–mar 2024 +16 USD con Gs subiendo **VERIFICADO** (`tabla-maestra-ueno-mef.csv` filas 2024-02/03); caída dic 2025 Ueno −12,5% USD / −12,6% Gs, R 0,264→0,228 **VERIFICADA** aritméticamente, sin explicación en ningún documento (GAP, ver §4).

### 2.2 b — descriptor de deriva por ventana (OLS log-log)

Recomputación propia (mismo método declarado: OLS sobre log R vs log t):

| Ajuste | Ventana / origen | v1 | v2 | Recomputación | Estado |
|---|---|---|---|---|---|
| (a) extremo | nov24→nov25 (doc 0,110→0,274) | 0,356 | — | 0,3558 | **VERIFICADO v1; RETIRADO en v2** (artefacto FX mezclado) |
| (a′) extremo | nov24→nov25 (CSV 0,110→0,2643) | 0,342 | — | 0,3418 | **VERIFICADO v1; RETIRADO en v2** |
| (a) extremo | dic24→nov25 (0,1021→0,2643) | — | 0,383 | 0,3828 | **VERIFICADO v2** |
| (a-OLS) | dic24→nov25, t=1 dic24, n=12 | — | 0,436 (R² 0,873) | 0,4356 (R² 0,8726) | **VERIFICADO v2** |
| (a′) extremo | nov24→nov25 corregida | — | 0,394 | 0,3936 | **VERIFICADO v2** |
| (a′-OLS) | nov24→nov25, t=1 nov24, n=13 | — | 0,451 (R² 0,855) | 0,4510 (R² 0,8551) | **VERIFICADO v2** |
| (b) | abr–nov25, origen dic24, n=8 | — | 0,802 (R² 0,957) | 0,8020 (R² 0,9572) | **VERIFICADO v2** |
| (b) v1 | abr–nov25, origen nov24, n=8 | 0,906 (R² 0,955) | 0,906 reproducido (b″) | 0,9058 (R² 0,9553) | **VERIFICADO como artefacto de origen; RETIRADO como valor de ventana** |
| (b′) local | abr–nov25, t=1 abr25, n=8 | 0,344 | 0,344 | 0,3438 (R² 0,9415) | **VERIFICADO ambas** |
| (c) meseta | dic25–sep26, origen dic24 | −0,046 (n=8, R² 0,025) | +0,031 (n=9, R² 0,011) | v1: −0,0462 ✓; v2: +0,0308 ✓ | **VERIFICADO en cada marco; v1 RETIRADO; v2 DESACTUALIZADO** |
| (c′) meseta local | t=1 dic25 | v1 −0,012 (R² 0,030) | v2 +0,009 (R² 0,013) | v1 secuencial −0,0120 ✓ / calendario −0,0046 ✗; v2 secuencial +0,0086 ✓ / calendario +0,0104 ✗ | **INCONSISTENTE (método) — hallazgo nuevo H-1** |
| (d) pre-Roche | feb–jul24, n=6 | 0,288 (R² 0,503) | 0,288 | 0,2876 (R² 0,5030) | **VERIFICADO ambas** |
| (e) completa | feb24–sep26 | 0,813 (n=24; solo PDF 0,814, n=23) | 0,819 (n=30, R² 0,909) | v1: 0,8133 / 0,8136 ✓; v2: 0,8186 ✓ | **VERIFICADO en cada marco; v2 DESACTUALIZADO con tabla vigente** |
| (IPS) | 2023–2025 anual, r_ips | 2,934 (R² 0,995) | 2,934 | 2,9337 (R² 0,9954); sobre participaciones 2,7516; sobre montos 2,762 | **VERIFICADO ambas; variable identificada: r_ips** |

**Valores vigentes con la tabla actual (recomputación de esta revisión, ningún documento los trae):**
- (e) completa, t=1 feb 2024 (calendario): **b = 0,8234, a = 0,0157, R² = 0,9108, n=31** (v2 decía 0,819, n=30).
- (c) meseta dic25–sep26, **n=10** (entra mar 2026): origen dic24 **b = −0,0101, R² = 0,0007**; origen nov24 **b = −0,0114, R² = 0,0008**; origen local dic25 **b = +0,0065, R² = 0,0048**. **El signo vuelve a negativo; con R² ≈ 0,001 el signo es ruido.** La conclusión ("sin tendencia medible") se mantiene; el número v2 (+0,031) no.

**H-1 — INCONSISTENTE: la variante local (c′) no usa el calendario que v2 declara.** v2 Apéndice A (`modelo-ueno-resultados-v2.md:290-299`) establece: "t es el mes calendario (meses desde el origen, con huecos cuando falta el PDF)". Pero los valores publicados de (c′) corresponden a **numeración secuencial 1..n**: v1 (c′) −0,0120 / R² 0,0296 = secuencial exacto; con calendario da −0,0046 / R² 0,005. v2 (c′) +0,0086 / R² 0,0132 = secuencial exacto; con calendario da +0,0104 / R² 0,0226. Los ajustes principales (c), (e), (a-OLS), (b) sí usan calendario y reproducen. La diferencia es pequeña y no cambia ninguna conclusión (R² ≈ 0,01), pero el método declarado y el aplicado difieren en (c′) en ambas versiones, sin que ningún documento lo registre. **GAP de método a corregir si se publica una v3.**

### 2.3 Roche-R (R > 0,10) y cruce de 0,20

- **Primer cruce: dic 2024 (R = 0,1021)** — **VERIFICADO** (`modelo-ueno-resultados-v2.md:110-115`; `tabla-maestra-ueno-mef.csv` filas 2024-11 0,0963 / 2024-12 0,1021). Ventana nov–dic 2024 cerrada al mes, ambos con PDF. Variaciones: nov→dic +6,0%, dic→ene +7,1% — **VERIFICADAS**.
- **v1: nov 2024 (R = 0,110) — RETIRADO** (`modelo-ueno-resultados.md:75-79`; tabla de cambios v2 #3).
- **Cruce de 0,20: ≈24 jun 2025** (interpolación lineal, fracción 0,788; convención inicio de mes; alternativa 24 jul con fin de mes) — **VERIFICADO** aritméticamente (0,1706→0,2079). La fecha exacta depende de la convención; los documentos lo declaran como artefacto, correcto.
- R se mantuvo > 0,10 desde dic 2024 hasta sep 2026 en todos los meses con dato (mínimo posterior 0,1094, ene 2025) — **VERIFICADO** con la serie vigente.

### 2.4 Roche-C (fondos públicos / patrimonio efectivo > 1,0)

**Base IPS — VERIFICADA** (aritmética sobre cifras redondeadas del documento; insumos externos): nov 2024 1,7/1,6 = 1,06; cierre 2024 1,766/1,56 = 1,13; 31 oct 2025 2,1/1,8 = 1,17; cierre 2025 2,24/2,20 = 1,02. Entrada nov 2024, mismo valor en v1 y v2. **La fila "dic 2024 sector público 1,12" de v1** (`modelo-ueno-resultados.md:81-95`) **desaparece de la tabla IPS de v2** (`modelo-ueno-resultados-v2.md:117-142`) pero **se conserva en el texto** de v2 §4 como una de las cuatro cifras de dic 2024 (1,740/1,56 = 1,12).

**Base fondos totales (nueva en v2) — VERIFICADA** desde CSV a FX 6.000 + anclas PE de NOTAS §12: dic 2024 1.687.245.570.000/1,56 billones = **1,08** (v2: 1,08 ✓); dic 2025 4.161.083.046.000/2,20 = **1,89** (v2: 1,89 ✓; NOTAS §12 dice 1,91 con 4,2 redondeados — diferencia de redondeo de entrada, registrada en Ap. B #9 de v2); mar 2026 5.133.303.588.000/2.467.235.000.000 = **2,08** (v2: ≈2,08 ✓; NOTAS §12 dice ≈2,2 con 5,2/2,4 redondeados — 5,2/2,4 = 2,17, no 2,20; redondeo grueso, registrado en Ap. B #10).

**Discrepancia dic 2024 (cuatro cifras) — VERIFICADA como rango:** PDF 1,687 → 1,08; balance 1,740 → 1,12; Asoban 1,747 → 1,12; ABC 1,76 → 1,13. Todas > 1,0; la conclusión no depende de la elegida. NOTAS §12 explica 1,76 como mismo saldo a FX ≈6.300 — **coherente** (1,687×6.300/6.000 ≈ 1,772 ≈ 1,76).

**Roche-C nov 2024 en base fondos totales ≈1,15** (1.792/1,56 con PE dic como proxy) — marcado como **supuesto, no medición** en v2 §4 y Ap. B #11. Correcto así; **NO VERIFICABLE** como medición (no hay PE nov 2024).

**HUECO (ambas versiones): serie mensual de Roche-C NO calculable.** PE solo en anclas: dic 2023 337.228M; dic 2024 1,56 billones; oct 2025 1,8; dic 2025 2,20; ene 2026 >USD 335M (sin cifra exacta); abr 2026 2.467.235M implícito por tope 20% (493.447M×5 — **VERIFICADO**). PE ago 2026 sin documentar.

### 2.5 Roche-S (solvencia / 12%)

**VERIFICADO** (aritmética; insumos del parteaguas, fuente externa): mar 2026 15,01/12 = 1,251; jun 14,5/12 = 1,208; sep 13,85/12 = 1,154; 2 nov 2026 5,56/12 = 0,463. Sin cambio v1→v2. **Cruce económico NO fechable** con datos públicos (salto 13,85% → 5,56% tras previsiones > Gs 1,6 billones, inspección 31 oct) — declarado hueco en ambas versiones. El 2 nov 2026 es reconocimiento legal, no cruce económico. **NO VERIFICABLE** dentro de estos archivos si las solvencias reportadas son correctas (no hay balances en el corpus).

### 2.6 IPS — exposición y r_ips

**VERIFICADO** desde la tabla: 2023 CDA 80.000M/1,0% → total 8.000.000M, r = 0,0101 ✓; 2024 659.000M/8,4% → 7.845.238M, r = 0,0917 ✓; 2025 1.602.000M/19,7% → 8.132.487M, r = 0,2453 ✓; mar 2026 1,5/9,36 billones = 16,0%, r = 0,1908 ✓; sep 2026 1,577/7,47 = 21,1%, r = 0,2676 ✓; nov 2025 exposición total 2,2/19,6 = 11,22%, r = 0,1264 ✓ (base distinta, indicada). CDA USD cierre 2025 USD 27.427.000 = 19,95% (15.127.000 + 12.300.000 heredado Visión = 27.427.000 exacto ✓; total implícito USD 137.478.697 ✓). Caja y Equivalentes 2024 Gs 665.685.348.380 + USD 12.241.087,73 y Bonos 2025 Gs 250.000M: **NO VERIFICABLES** en el CSV (van en NOTAS §11 por instrucción expresa, no en columnas — correcto según la regla de no mezclar definiciones).

**b IPS 2,934 — VERIFICADO** sobre r_ips (0,0101; 0,0917; 0,2453; t=1,2,3): b = 2,9337, R² = 0,9954. Sobre participaciones 2,7516; sobre montos 2,762. Sin cambio v1→v2. Banda b ≥ 1 no clasificada; n=3 anual.

### 2.7 ACO-A — aritmética (insumos externos; aritmética verificada, insumos NO VERIFICABLES en el corpus)

| Magnitud | Valor | Verificación |
|---|---|---|
| FGD / exposición IPS sep 2026 | 228,3M / 2,03 billones = **0,011%** | **VERIFICADO** (0,01125% → 0,011%) |
| Anticipo FGD Gs 10M / tope | **4,38%** | **VERIFICADO** (10/228,3 = 4,38%) |
| Exposición IPS / fondos Ueno sep 2026 | doc 40,8% (348,5/855); CSV **41,7%** (348,5/834,825625 = 0,41745) | **VERIFICADO; v1 decía 41,8% — error de redondeo corregido en v2** (tabla de cambios #15, Ap. B #13). Discrepancia doc/CSV por total distinto (855 vs 834,8), no por cálculo |
| USD 146M vinculados / PE | **39,8%** con PE dic 2025 (2,2 billones = USD 366,7M); **35,5%** con PE abr 2026 (2.467.235M = USD 411,2M) | **VERIFICADO** (146/366,67 = 39,82%; 146/411,21 = 35,51%). Tope 20%: USD 73,3M / USD 82,2M ✓. El 35,5% es nuevo en v2. Insumo "USD 146M" (ABC [17]): **NO VERIFICABLE** en el corpus |
| Salvadoras: PE implícito | 905.825M / 0,35 = **Gs 2.588 billones** | **VERIFICADO** (2.588.071M). +4,9% sobre ancla abr 2026; +17,6% sobre cierre 2025 — ambos **VERIFICADOS**. Tensión reducida, no resuelta (PE ago 2026 sin documentar) |
| Fondeo dic24–mar25 no a préstamos | **91,75%** (depósitos +1.755.304M; crédito neto +144.737M = 8,25%) | **Aritmética VERIFICADA** (144.737/1.755.304 = 8,2457%). **Insumos NO VERIFICABLES** en estos archivos: no hay columnas de depósitos/crédito en la tabla maestra; fuente citada Asoban vía ABC [7] |
| Embargo total | USD 70M + Gs 1.621.853.458.972 + Gs 58.639.000.000 = **Gs 2.1005 billones** (FX 6.000) | **VERIFICADO** (2.100.492M). vs Derechos Fiduciarios 2.105.743M: **−0,25%** (−0,2493%) ✓. Coincidencia numérica, no identidad |
| Δ de ACO-A | No estimable | **Correcto: GAP.** No hay serie A(τ) ni montos por receptor/fecha |
| 7 bancos licitantes, balance de exclusión 15 días, ~32.000 jubilados, primer pago 17 nov | — | **NO VERIFICABLE** en el corpus (fuentes citadas: Infobae, BCP vía ABC — externas, no incluidas) |

**Ambigüedad heredada de v2 (no nueva):** "el excedente es USD 146M" — 146M es el total vinculado; el excedente sobre el tope (USD 73M / USD 82,2M) sería USD 73M / USD 63,8M. Forecast, rastro y v2 dicen lo mismo; la ambigüedad es de v2. Igual con "Salvadoras ≈ USD 153M" sin FX — a FX 6.000 son USD 151,0M; solo el forecast lo declara (`forecast-ueno-2026-11-06.md:166–172`).

### 2.8 Discrepancia mar 2026 (balance vs Tesoro)

Balance Gs 3.163.975M vs Tesoro Gs 3.721.013M (+ USD 235M): diferencia Gs **557.038M** — **VERIFICADA** (3.721.013.013.754 − 3.163.975.000.000 = 557.038.013.754). **Matiz no advertido en los documentos:** los 557.038M son diferencia solo en Gs; el componente USD 235M queda "sin conciliar" aparte y no se suma (a FX 6.000 serían +Gs 1.412.290M). Los documentos la registran como no resuelta (`tabla-maestra-ueno-mef.csv:40`; NOTAS §7) — correcto como registro, pero la cifra citada no es la discrepancia total en equivalentes. **GAP de definición, no error aritmético.** Además: **el v2 NO menciona la discrepancia en ningún punto** (grep "3,163,975" en v2 = 0). GAP de traslado v2 — está en el CSV sí, en el v2 no.

### 2.9 PDFs faltantes

- **v1: 15 faltantes — VERIFICADO** en su marco (2023-01–05, 2023-12, 2024-08, 2024-10, 2024-11, 2024-12, 2025-01–03, 2026-01, 2026-03; NOTAS-v1 §2; 30 PDFs).
- **v2: 7 faltantes — VERIFICADO en su marco, DESACTUALIZADO hoy** (2023-01–05, 2024-08, 2026-03; `modelo-ueno-resultados-v2.md` tabla #18 y §12). Hoy mar 2026 tiene PDF, así que **quedan 6 meses sin PDF: 2023-01–05 y 2024-08** (`tabla-maestra-ueno-mef.csv`: 6 filas "sin PDF"; NOTAS §2).
- **H-5 — INCONSISTENTE (conteo de PDFs en NOTAS vigente):** NOTAS §1 dice 38 PDFs; §2 dice "6 faltantes de 45 meses" (38+6 = 44 ≠ 45); §13 y `download_log.csv` dicen 38 OK y **7 MISSING (2023-01–05, 2023-12, 2024-08)**. La fila 2023-12 del CSV vigente figura como "MEF PDF" con totales del sistema (`tabla-maestra-ueno-mef.csv:13`), pero §2 admite que ese PDF "NO está en el directorio local" y el log lo marca MISSING. Es decir: **hay 38 archivos en disco, 39 filas marcadas MEF PDF, y 2023-12 es el mes contado dos veces** (recuperado como `archivo_5.pdf` según §1/§12, pero sin archivo local). Además el "38" de v2 no es el mismo "38" actual: el de v2 incluía dic 2023 y no mar 2026; el actual incluye mar 2026 y no dic 2023. Ningún documento advierte esta coincidencia.
- **H-6 — INCONSISTENTE (clasificación de oct 2024):** NOTAS §1 (`tabla-maestra-NOTAS.md:14-31`) clasifica oct 2024 en el patrón "guion bajo" (hacienda.gov.py). Pero `download_log.csv` muestra su URL real como `.../2024-11/archivo_4.pdf` (patrón genérico), y el CSV lo anota como "(archivo_4.pdf)". v2 Ap. B #16 (`modelo-ueno-resultados-v2.md:301-323`) registra la diferencia de etiqueta pero no corrige la clasificación de §1. Con la corrección, el reparto real sería 16 estándar + 6 guion bajo + 16 genéricos = 38, no 16+7+15. Detalle de archivo, no de número (R oct 2024 = 0,0780 verificado desde el PDF).

### 2.10 Otros números verificados

- "La captura ×2,6 en 11 meses" (v2 §11): 0,2643/0,1021 = 2,589 ✓. "2,4–2,5 veces" (v1 §11): 0,2643/0,110 = 2,40; 0,274/0,110 = 2,49 ✓ en marco v1 — **RETIRADO** con v2.
- "Cuota de Ueno en fondos del Estado 18,6% (dic 2025)" (v1 §7): participación dic 2025 = 0,1857 → 18,6% ✓.
- "Roche-C fondos totales dic24→mar26 +Gs 3,446 billones en 15 meses" (v2 §8): 5,133−1,687 = 3,446 ✓.
- "9,70% de cartera (30 oct)" y "tope 10% del IPS, sin nuevas colocaciones en 2026" (v1 §7 y §11; v2 §11): **NO VERIFICABLE** en estos archivos. El 9,70% coincide con sep 2026 (2,03/20,96 = 9,69%), no con ninguna fila de oct 2025. La fecha "30 oct" y la afirmación de no colocaciones no tienen fuente dentro del corpus. GAP. Ver además §3.7: el año es inconsistente (2025 en v2, 2026 en las fuentes).
- "Sagas 3.000×, Kasas 800× vs resto del sistema" (v2 §13, peldaño 6): **NO VERIFICABLE** en el corpus — aparece solo ahí, sin cita a NOTAS ni a tabla. El circuito Sagas→Kasas→Vinanzas→Itti→Grupo M y las deudas Gs 905.825M tampoco tienen fuente dentro de los 8 archivos del frente 1.


## 3. Verificación por documento derivado (contra v2)

### 3.1 Forecast + CSV — 100% de los valores verificables coinciden con v2

- R(t) sep 2026 0,2395; Ueno USD 834,8M equiv; sistema USD 4.320,4M equiv — **VERIFICADO** (forecast L19; CSV L4; v2 L76, L203). Suma de la base CSV recomputada: USD 4.320.353.014 vs total declarado 4.320.353.015 (forecast L75, L296): diferencia **−1 USD, trivial**, por redondeo; R y participaciones reproducen exactas a 4 decimales en los 16 bancos.
- b ventana 0,383 / 0,436 (forecast L20), meseta +0,031 (L21), Roche-R dic 2024 (L22), Roche-C 1,08 / 1,89 / ≈2,08 (L23), Roche-S 0,463 (L24), ASI 0/5, 0/4, 0/5 y muro 5 negativos / 0 positivos (L25–27), tendencia tela saturación (L28) — **VERIFICADO** contra v2.
- Doble hito 17 nov 2026: primer pago a jubilados (32.000 a reasignar) + plazo máximo balance de exclusión (2 nov + 15 días) — **VERIFICADO** (forecast L37–40, L62, L147, L282–292; CSV L68–69; v2 L264, L184). Las dos fechas son independientes y caen el mismo día — el documento lo dice explícitamente (forecast L40).
- Anticipo FGD: límite 72 h = **5 nov 2026** (2 nov + 72 h, cálculo) — **VERIFICADO** como cálculo; v2 documenta "adelanto Gs 10M en 72h" sin fechar el 5 nov.
- FGD: tope Gs 228.300.000 (75 SM; SM implícito Gs 3.044.000), USD 38.050 a FX 6.000; anticipo Gs 10.000.000 = 4,38% — **VERIFICADO** (10.000.000/228.300.000 = 4,3802% ✓; v2 L184, L201–202). Tope / exposición IPS = 0,011% (recomputado 0,0112463% ✓). Tope / fondos Ueno sep 2026: 0,0046% (Gs 5,009 billones, CSV) y 0,0045% (Gs 5,13 billones, ABC) — **VERIFICADO**.
- Saldos OEE por banco sep 2026, escenarios A (igual entre 7, USD 119,3M c/u: 834.825.625/7 = 119.260.803,57 → CSV 119.260.804 ✓), A5 (igual entre 5, USD 167,0M c/u), B (proporcional entre 5, pesos suman 100,00 ✓), C (uno toma todo) — **VERIFICADO**, recomputados exactos a 4 decimales. Son proyecciones con supuesto declarado (conservación de masa, total constante), no mediciones.
- Embargo 3 nov 2026: USD 70M + Gs 1.621.853.458.972 + Gs 58.639.000.000 = Gs 2,1005 billones; −0,25% vs Derechos Fiduciarios; +0,45% vs exposición IPS — **VERIFICADO** (recomputado total Gs 2.100.492.458.972 ✓; −0,2493% ✓; 350,08/348,5 = +0,4539% ✓; v2 L207, L263).
- Salvadoras, USD 146M, megacuentas (suma recomputada 3.758.773M; parteaguas-notas L11 da 3.758.774M, 1M de redondeo), denuncia MEF 5 nov 2026, IPS (41,7%, CDA, Bonos, Caja — estos últimos verificados contra parteaguas-notas L25, no contra el cuerpo de v2), cartera total IPS **ESTIMADO Gs 20,93 billones** = 2,03/9,70% (recomputado ✓, etiqueta ESTIMADO declarada), ASI hoja de ruta, muro en reversa, vigilancia, forma en la tela — **VERIFICADO** / coherente con v2 y tela.
- **Defectos menores del CSV del forecast (no afectan los números):** CSV L2 es una **segunda fila de cabecera duplicada** antes de los datos. CSV L46: **"(30 oct 2025)"** vs forecast L209 **"30 oct 2026"** — ver §3.7. v2 L234 también dice "30 oct 2025" en su lectura 1, mientras parteaguas-notas L65 y v2 §13 peldaño 11 usan 30 oct sin año / 2026 en contexto. La fecha correcta por contexto (sin nuevas colocaciones **en 2026**, posición vigente al trigger) es 2026; el "2025" es inconsistente.

### 3.2 Tela cimática / huella (ACO-A, modo, Δ, m, A1–A4, distancias, ventana)

- Ventana primaria dic 2024→nov 2026; τ=0 dic 2024 (R=0,1021), τ=1 trigger 2 nov 2026; R observada dic 2024→sep 2026, **21 puntos**; mar 2026 sin R; en τ=1 m sostenido en último R 0,2395 — **convención, no dato**; 2 meses sep→nov sin R, no se imputan — **VERIFICADO** (tela L24–41, L268–293, L333–364; v2 L39–83). Ventana sensibilidad feb 2024→sep 2026, **30 puntos** — **VERIFICADO**.
- ACO-A criterio cumplido: extinción funcional + absorción identificable (7 bancos, 5 nombrados, balance 15 días) — **VERIFICADO** (tela L44–58; v2 L191–200). "Caso real 19 de la tela, primero en vivo" y "primer caso real del dominio Finanzas" — **NO VERIFICABLE** contra v2 (afirmación sobre el repo, 18 ACO).
- Trayectoria (τ, log₁₀m): τ=0 −0,991 (m 0,1021); ~0,25 −0,769 (0,1701); ~0,5 −0,634 (0,2324); ~0,75 −0,647 (0,2253); τ=1 −0,621 (0,2395) — **VERIFICADO** en los extremos; **NO VERIFICABLE** en los valores intermedios exactos desde v2/CSV solos — son lecturas de la retícula interpolada de 32 fases (tela L146–153): m 0,1701 en τ≈0,25 vs R jun 2025 0,1706 (v2) es interpolación, no un mes observado. El documento lo declara como procedimiento.
- Ueno NO converge a m≈1; |log₁₀m| 0,991→0,621; nunca entra en banda [0,56, 1,78]; m máx 0,267 < 0,56 — **VERIFICADO** (v2 L76, oct 2025 0,2670). Normalizado R/R_max: log₁₀m −0,416→−0,046; distancia centroide ACO **1,24 → 0,49** (mínimo del rango ACO [0,49, 2,74], mediana 0,85) — **VERIFICADO** como consistencia interna (mismo par en §1.3, §2.5 y forecast L265); **NO VERIFICABLE** desde v2/CSV solos — requiere el cálculo de centroides del repo.
- Modo: Acantilado Catastrófico con rasgos de Craquelado (descriptivo); la tela lo **matiza, no lo refuta ni lo confirma**; acantilado en Roche-S (13,85%→5,56% en ~1 mes), no en R(t) — **VERIFICADO** (tela L107–122; v2 L191–200, L150–152).
- **Δ NO estimable** (sin serie A(τ)); modo queda descriptivo — **GAP — VERIFICADO como hueco** (tela L34, L111–122, L333–341; v2 L191–200, L242–256).
- Hazard / prueba prospectiva: cohorte v2 cripto 491 pares vivos al corte 2026-09-30, 440 candidatos; P1a ✓ (53/389), P2 ✓ (mediana Δ=−0,961, n=22 maduros), P3 INCONCLUSO (ρ=+0,189, IC95 [−0,253, +0,566]); **Ueno NO pertenece a la cohorte, no confirma ni refuta P1a/P2/P3** — **NO VERIFICABLE** contra v2 (cifras de la cohorte cripto no están en v2). No hay "hazard" numérico de Ueno en ningún documento: **GAP**.
- Firma cimática: A1 **2,065**, A2 **1,326**, A3 0,438, **A4 0,717** (bulto secundario, firma de saturación); armónicos 9–16 ~0,2 planos; sensibilidad A1 5,926 / A2 2,298 / A3 2,139 — **VERIFICADO** A1/A2/A3 contra el CSV; **A4 = NO VERIFICABLE desde el CSV** — `ueno-huella-cimatica.csv` no tiene columna A4 (solo A1/A2/A3); A4 0,717 solo está en la tabla del .md (tela L161) y en el PNG/script citados.
- Huella: primaria log₁₀m −0,9910 / −0,7693 / −0,6338 / −0,6471 / −0,6207; log máx −0,5752; A1 2,0653 / A2 1,3255 / A3 0,4377. Sensibilidad −1,5467 / −1,1079 / −0,7680 / −0,6712 / −0,6207; máx −0,5735; A1 5,9262 / A2 2,2975 / A3 2,1394 — **VERIFICADO** — CSV L2 y L3 coinciden a 4 decimales. m máx 0,266 = R oct 2025 0,2670 (v2) ✓.
- LOO tela actual (740 casos, 51.210 puntos): dominio todos los rasgos **50,7% (374/737)**; solo-forma 41,9%; tono **66,2% (490/740)**; solo-forma 58,6% — **VERIFICADO** aritméticamente (374/737=50,74%; 490/740=66,22%); **INCONSISTENCIA INTERNA A ACLARAR:** denominadores distintos — dominio sobre 737, tono sobre 740 — sin explicación de por qué 3 casos salen del denominador de dominio. No es un error contra v2, es un hueco de método. La discrepancia "739 vs 740 casos" está registrada en tela L220, L361.
- Asignación Ueno: **ACO en dominio y `variable` en tono, en las 4 configuraciones**; primaria todos los rasgos ACO 1,24 · E2 1,46 · C 1,49 · A 1,51 · B 1,54; solo-forma ACO 1,08 · E2 1,12 · B 1,14; margen delgado, "sugestiva, no decisiva" — **VERIFICADO** como consistencia interna; **NO VERIFICABLE** desde v2/CSV — requiere centroides del repo. El documento declara el margen delgado y que Finanzas no existe en los 11 dominios del repo.
- Tendencia §3.1, incertidumbre §3.2 (OLS a=0,0829, b=0,436, R²=0,873, n=12; residuos log sd **0,132 → ±14,1% en R**; meseta sd 0,057 (±5,9%), b=+0,009 origen local, n=9; FX: R nov 2024 0,0963 a FX 6.000 vs 0,0965 a FX 7.793 — **0,0002, despreciable**; **u = NULL (0/51.210 puntos)**) — **VERIFICADO** (v2 L91, L95–96; exp(0,132)−1=14,11% ✓; exp(0,057)−1=5,87% ✓). Nota: la meseta se cita como +0,031 (origen dic 2024) y +0,009 (origen local) — **no es contradicción**: son dos orígenes de t declarados.
- Hacia adelante §3.3 — **VERIFICADO**, coherente con v2 y forecast.

### 3.3 Rastro del dinero

- IPS CDA 1,0% → 8,4% → 19,7%; exposición IPS sep 2026 ≈ Gs 2,03 billones; fondos IPS en Ueno 41,7%; total Ueno sep 2026 USD 834,8M (19,32%, R=0,2395) — **VERIFICADO** (rastro L11–15; v2 L173–190, L203, L76).
- Caja Fiscal: Gs 250.000M adjudicados el 31 jul 2025 al 12,35% — **NO VERIFICABLE** contra v2 (v2 menciona Gs 250.000M depositados jul 2025 pero no la fecha 31 jul ni el 12,35%). Fuente: parteaguas v2 / denuncia.
- Avalancha dic 2024–mar 2025: depósitos totales +Gs 1.755.304M (+17%), crédito neto +Gs 144.737M (+2%); **91,75% del fondeo incremental NO fue a préstamos** — **VERIFICADO** (v2 L206, L270; 144.737/1.755.304=8,25% ✓). La corrección "depósitos totales, NO solo fondos públicos" (rastro L19) es correcta y está declarada.
- Fondos **públicos** en el mismo periodo +Gs 511.865M (+35,8%): Gs 1.428.909M dic 2024 → Gs 1.940.773M mar 2025 — **INCONSISTENTE en la etiqueta, VERIFICADO en la aritmética de columna**: 1.428.909M es la columna **Gs sola** de Ueno en dic 2024 (`ueno_gs_mef`, tabla-maestra L25) y 1.940.773M la Gs sola de mar 2025 (L28); la diferencia 511.864M y el +35,82% son correctos **para la columna Gs**. Pero los **fondos públicos totales** (USD+Gs a FX 6.000) son Gs 1.687 billones en dic 2024 (v2 L134) y Gs 2.259,9 billones en mar 2025: +Gs 572,7 billones (+33,9%), no +511,9M (+35,8%). El documento etiqueta como "fondos públicos" lo que es solo el componente en guaraníes.
- Dic 2024 mes focal, circuito salvadoras, USD 146M vinculados, fideicomiso, embargo, resolución 2 nov, huecos §6 — **VERIFICADO** contra v2, con las imprecisiones heredadas de v2 (FX de USD 153M; "excedente USD 146M", ver §2.7).

### 3.4 Backcast Roche (notas)

- Tres ratios operativos: Roche-C = fondos públicos/PE > 1,0; Roche-R = R(t) > 0,10 (Ueno = 10% del resto, 9,09% del total); Roche-S = solvencia/12% < 0,50 — **VERIFICADO** (backcast L10–17; v2 L117–156, L218–230). La nota "no es término oficial BCP/MEF; metáfora de Elán" es correcta.
- Respuesta corta: fallo estructural inició ventana **jul–nov 2024**, focal **12 nov 2024**; entrada a Roche-concentración **nov 2024 (R=0,110 y fondos IPS/PE=106%)** — **INCONSISTENTE con v2 (usa número v1 retirado)**: R nov 2024 es **0,0963**, no 0,110 (v2 L11). Roche-C nov 2024 1,06 sí es correcto. La ventana correcta en v2 es **jul–dic 2024, focal dic 2024** (v2 L16, L281–282). El 12 nov 2024 sigue siendo φ paso 2, pero ya no es el mes focal del backcast.
- Meseta ene–sep 2026: R 0,216–0,254; IPS 9,70% al 30 oct 2026 — **VERIFICADO** (v2 L39–83; 9,70% v2 L234, con el problema de año de §3.7).
- Segunda ruptura jun–jul 2025: R cruza 0,20 entre jun (0,1706) y jul (0,2079); interpolación ≈ 24 jun 2025 — **VERIFICADO** (v2 L114–115).
- Confirmación dic 2024–mar 2025: 92% sin ir a préstamos — **VERIFICADO** (v2 L206, 91,75%; "92%" es redondeo de ABC).
- Entrada a Roche nov 2024: **R=0,110**; IPS 1,7/1,6=106%; cierre 2024 IPS 1,766/1,56=113%; sector público dic 2024: 1,747/1,56=112%. "Los dos indicadores cruzan 1,0 el mismo mes" — **INCONSISTENTE en R (0,110 retirado)**; **VERIFICADO** en Roche-C. La frase "los dos indicadores cruzan el mismo mes" es **falsa en v2**: Roche-C (IPS) cruza en nov 2024 y Roche-R en dic 2024 (v2 L19, L228, "corrección clave de v2").
- Acto institucional 12 nov 2024, primera ruptura jul 2024, pre-condición 9 nov 2023 — **VERIFICADO** (v2 L157–172, L39–44, L257–289).
- Tres fechas A/B/C — **INCONSISTENTE en A y B** por el 0,110 retirado y la ventana/focal (v2: jul–dic 2024, focal dic 2024, Roche-R dic 2024). **VERIFICADO** en C (v2 L144–156). También: "No se puede precisar un día en sep–nov 2024: falta el PDF MEF de oct 2024" (backcast L30) — **INCONSISTENTE**: oct 2024 **sí tiene PDF** en v2 (R=0,0780, v2 L10, L17, L56); la ventana quedó cerrada nov–dic 2024.
- Tabla Roche-C: nov 2024 1,06; cierre 2024 1,13; dic 2024 sector público 1,12; 31 oct 2025 1,17; cierre 2025 1,02 — **VERIFICADO** (v2 L124–130).
- Pendiente: Informe 016; **PDFs MEF faltantes: oct 2024, dic 2024–mar 2025, ene/mar 2026** — **INCONSISTENTE / DESACTUALIZADO**: v2 §12 solo **7 PDFs faltantes** (2023-01–05, 2024-08, 2026-03); oct 2024, dic 2024, ene–mar 2025 y ene 2026 **ya tienen PDF** en v2 (v2 L10). La lista de pendientes del backcast es pre-v2.
- Verificación de Mole (2026-11-06): jun 2024 0,0338 ✓; jul 0,0610 ✓; sep 0,0777 ✓; **nov 2024 R 0,110 ✓ (ancla)**; jun 2025 0,1706 ✓; jul 0,2079 ✓; Roche-S 0,463 ✓ — **INCONSISTENTE en un punto, resto VERIFICADO**: el ✓ a "nov 2024 R 0,110 (ancla)" es la verificación **pre-corrección v2**; el ancla quedó retirada.
- "Regrabación final: usar ventana jul–nov 2024 con focal 12 nov 2024…" (backcast L54) — **INCONSISTENTE con v2**: la ventana/focal vigentes son jul–dic 2024 / dic 2024 (v2 L281–282, Apéndice C). Si se regraba con lo escrito aquí, se regraba el dato retirado.
- Muro de 5 eventos como instrumento del ratio de Roche; CORRECCIÓN leapfrog: **leapfrog = b < 0**; "NO escribir '5 eventos positivos = leapfrog'" — **VERIFICADO** como registro de decisión + advertencia (v2 L210–216; forecast L239–250).

### 3.5 Parteaguas (notas)

- "Lo que confirma (sin cambios)": R(t) **0,110 (nov 2024) → 0,274 (nov 2025) → 0,235 (feb 2026) → 0,224 (ago 2026) → 0,247 (sep 2026)**; **b = 0,357** (parteaguas L9–12) — **INCONSISTENTE con v2 — serie completa v1 retirada.** v2: nov 2024 **0,0963** (L11); nov 2025 **0,2643** (L76, L90); feb 2026 **0,2357** (L76 — 0,235 es truncamiento); ago 2026 **0,2161** (L76 — 0,224 es jun 2026 0,2246, mes equivocado); sep 2026 **0,2395** (L76 — 0,247 es sep 2025 0,2467, año equivocado). b **0,357 retirado** (v2 L12, L312). Este bloque describe el documento parteaguas **v1**; como notas no está actualizado a v2. Es el error más grave del conjunto revisado si se lee como vigente.
- Megacuentas Gs 3.758.774M = 177,5% del patrimonio; CDA Gs IPS 1,0% → 8,4% → 19,7%; resolución 2 nov 2026, solvencia 5,56% vs 12% — **VERIFICADO** (v2 L272, L173–190, L150–152).
- φ paso 1: baja puntaje mínimo **70→60** (sin fecha) (parteaguas L15) — **INCONSISTENTE con v2** (65→60, 9 nov 2023, v2 L157–172). El propio archivo lo corrige en su sección v2 (L69–71) — la corrección existe dentro del mismo archivo, pero el bloque v1 queda sin marcar como retirado en L15.
- φ paso 2, 3, 5 — **VERIFICADO** (v2 L157–172); paso 4 nº de resolución (SB.SG. N° 00105/2024) **NO VERIFICABLE** contra v2 (v2 §6 no lo cita). φ contable Gs 2,5 + 2,6 billones — **VERIFICADO** (v2 L157–172).
- Circuito salvadoras, memorando Rivarola 10 jul 2026, secuencia del colapso, embargo, IPS nuevos datos CGR (Caja y Equivalentes 2024 Gs 665.685.348.380 + USD 12.241.087,73; CDA USD cierre 2025 USD 27.427.000 = 19,95%; Bonos 2025 Gs 250.000M) — **VERIFICADO** contra forecast / v2 donde aplica; Caja/Bonos **NO VERIFICABLE** contra el cuerpo de v2.
- Intangibles: +Gs 654.799M solo en 2025, **"triplica la suma de intangibles de nueve bancos (Gs 269.233M)"** (parteaguas L25) — **INCONSISTENTE (aritmética)**: 654.799/269.233 = **2,43×, no 3×** (triplicar serían Gs 807.699M). El +654.799M sí es v2; el "triplica" y el comparador 269.233M **no están en v2**.
- Límites Ley 7235/23, comparador CAME México 2025 — **NO VERIFICABLE** contra v2 (externos al modelo).
- Bandera ASI: v1 lo define como "seguro sistémico de absorción"; repo SNT tiene otro ASI — **VERIFICADO como bandera histórica**, resuelta en la sección v2 del mismo archivo (L57–59: ASI = Índice de Soberanía Atómica, no seguro). Bandera ACO-A — **VERIFICADO** como registro.
- "El documento NO usa la palabra malversación" (v1) (parteaguas L33, L79–80) — **DESACTUALIZADO dentro del propio archivo**: la v2 sí la usa como denuncia penal presunta (parteaguas L51–56); el archivo lo reconoce en L79–80 ("dos líneas [del podcast] quedan desactualizadas… Decisión de Elán pendiente").
- V2 §1.4: USD 146M, 5 jun / 15 jun / 24 jul 2026, ratios capital, IPS 9,70% al 30 oct, cadena penal y cadena política — **VERIFICADO** en ratios de capital, IPS 9,70%, USD 146M, cadena penal; **NO VERIFICABLE** contra v2: las fechas 5 jun / 15 jun / 24 jul 2026 y la cadena política (renuncia/juicio político a Peña) — v2 no las contiene; su fuente es parteaguas v2 [18][21].
- φ corregido y fechado (v2), malversación v2 — **VERIFICADO** (v2 L157–172, L29–33).

### 3.6 Finanzas-mundo — solo la sección Ueno

- §0 plantilla Ueno: cruce Roche-R dic 2024 (R=0,1021); b=0,383/0,436; Roche-C=1,08; Roche-S=0,463; ACO-A con resolución 2 nov 2026 y absorción por 7 bancos; "el umbral no se transfiere mecánicamente" (finanzas L18) — **VERIFICADO** (v2 L11–13, L19, L150–152, L191–200). Es la referencia Ueno más limpia de todo el conjunto revisado.
- §1 plantilla: hub Ueno = "Continental, Itaú, Ueno (híbrido)"; sombra Ueno = "empresa salvadora, cooperativa fuera de FGD, financiera que presta a su grupo"; puente = "fintech wallet, casa de bolsa que coloca CDA" (finanzas L20–29) — **NO VERIFICABLE** contra v2 (mapeo de plantilla del nuevo dominio, no afirmación del modelo v2; v2 no llama "hub" a Continental/Itaú ni define puente para Ueno). Interpretación, no contradicción numérica.
- §4: "Igual que en el forecast de Ueno (BNF 0,3712 y Continental 0,1983 ya estaban por encima de 0,10 sin estar en colapso): se vigila la deriva, no el nivel" (finanzas L79–80) — **VERIFICADO** contra forecast L73–97; **NO VERIFICABLE** contra v2 solo (v2 no desagrega R_X por banco).
- §5 Paraguay (control) y resto de fichas, §§6–8 — **NO VERIFICABLE** contra v2 por diseño (datos del Banco Mundial). Consistencia interna: R_NPL desde NPL 2,27% = 0,0227/0,9773 = 0,0232 ≈ 0,0233 ✓. La lectura clave ("el hub Ueno cayó y el agregado del país apenas se movió; el Banco Mundial no ve el hub") es coherente con v2 y está marcada como prueba del gap 1 (finanzas L236–248).
- §9 gaps 1–10 — **GAP**, registrados como gaps, coherentes con la guarda de v2 (u NULL, ASI fórmula sin calcular — v2 L173–190, L242–256).

### 3.7 Fecha de la posición IPS 9,70%: 2025 vs 2026

- `forecast-ueno-valores.csv:46` "(30 oct 2025)" vs `forecast-ueno-2026-11-06.md:209` ("30 oct 2026") y `backcast-roche-notas.md:21` ("30 oct 2026"). `modelo-ueno-resultados-v2.md:234` dice "30 oct 2025" en su lectura 1, mientras el contexto (sin nuevas colocaciones en 2026, posición vigente al trigger) apunta a 2026. **Inconsistencia interna del conjunto; el valor 9,70% no está en disputa, solo el año.** Las fuentes del parteaguas (F5 `:47` y `:262`, F6 `:28`) dicen 30 oct 2026. **El v2 trae el año mal** (2025 por 2026) según esas fuentes.


## 4. Reporte PDF, podcast y videos contra v2

### 4.1 Reporte PDF — conforme a v2, con omisiones parciales (no errores numéricos)

| Dato en el PDF | Cita PDF | Cita v2 | Veredicto |
|---|---|---|---|
| Portada: "dic 2024 · 0.436 · 0/5 · 2.1005" (mes focal, b OLS, ASI jubilados, embargo) | PDF txt:L13–15 | v2:L91 (0.436), L272 (mes focal dic 2024), L207 (2.1005), §7 ASI 0/5 | **VERIFICADO** |
| R(t) 30 meses, todos PDF, diferencia máx. 0.0000; 38 informes MEF, 45 filas ene 2023–sep 2026 | PDF §1, txt:L101–117 | v2:L10, L55–56 | **VERIFICADO** |
| b OLS dic 2024–nov 2025 **0.436** (n=12, R²=0.873); b local abr–nov **0.802** (n=8, R²=0.957); meseta **+0.031** (n=9, R²=0.011); completa **0.819** (n=30, R²=0.909); pre-Roche **0.288** (n=6, R²=0.503); IPS **2.934** (n=3, R²=0.995) | PDF §2 tabla, txt:L107–117 | v2:L90–102 | **VERIFICADO** (toda la tabla §2) |
| b depende del reloj: mismo tramo 0.802 / 0.906 (origen nov 2024) / 0.344 (origen local) | PDF §2, txt:L120 | v2:L96, L104 | **VERIFICADO** — el 0.906 aparece aquí solo como reproducción con el origen viejo, su único uso legítimo en v2 |
| Roche-C nov 2024 IPS **1.06**; dic 2024 fondos totales **1.08**; dic 2025 **1.89**; mar 2026 **≈2.08**; Roche-R dic 2024 **0.1021** (oct 0.0780, nov 0.0963); Roche-S 1.251/1.208/1.154 y **0.463** el 2 nov 2026 | PDF §3 tabla y texto, txt:L134–157 | v2:L134–136, L112–113, L153, L224–226 | **VERIFICADO** |
| Cruce 0.20 ≈24 jun 2025; R(t) nunca vuelve bajo 0.10 | PDF §3, txt:L149–150 | v2:L112–113 | **VERIFICADO** |
| φ paso 1: puntaje **65→60**, 9 nov 2023; paso 2: Res. 093-046/2024, 12 nov 2024; pasos 3–5 y φ contable Gs 2.5 + 2.6 billones | PDF §4 tabla, txt:L163–207 | v2:L163 y §6 | **VERIFICADO** |
| Avalancha dic 2024–mar 2025: depósitos +Gs 1,755,304M (+17%), crédito neto +Gs 144,737M (+2%), **91.75%** no a préstamos; fondos públicos +Gs 511,865M (+35.8%) | PDF §1/§4, txt:L31, L206 | v2:L206 (91.75%, depósitos, crédito); **los +Gs 511,865M / +35.8% no están en v2** | **VERIFICADO** salvo fondos públicos: **NO VERIFICABLE en v2** (la aritmética interna 511.865/1.428.909 = 35,82% cuadra contra la tabla maestra citada, pero v2 no da esas cifras; ver §3.3, etiqueta Gs sola) |
| Salvadoras 29 abr 2026: Gs 905,825M ≈ USD 153M = 35% PE; Sagas 3.000×, Kasas 800×; USD 146M = **39.8%** PE cierre 2025 | PDF §4, txt:L215 | v2:L204 (39.8%) y §8 | **VERIFICADO** — pero el PDF **omite el 35.5% con PE abr 2026** (v2:L21, L204; Apéndice C.1 #15 lo exige para el espacio). Omisión parcial |
| Backcast: ventana jul–dic 2024, mes focal dic 2024; salto jul 2024 R 0.0338→0.0610 (+80.5%); caída dic 2025 R 0.264→0.228 (−12.5% USD) sin explicación | PDF §5, txt:L229–247 | v2:L82, L272–275, L284 | **VERIFICADO** |
| ASI 0/5 jubilados, 0/4 ahorristas (+1 sin datos), 0/5 OEE; FGD Gs 228,300,000 = **0.011%** exposición IPS; anticipo Gs 10M en 72 h | PDF §6, txt:L280–281 | v2:L201, §7 | **VERIFICADO** |
| Embargo Gs **2.1005 billones**; difiere −0.25% de Derechos Fiduciarios Gs 2.105743 billones | PDF §5/§8, txt:L229, L368 | v2:L207, L311 | **VERIFICADO** |
| Escenarios: A BNF 0.4252 y 29.83%; B 0.5553; C 0.8656 con 46.4%; BNF 0.3712, Continental 0.1983; "reparto proporcional entre los cinco nombrados" = B | PDF §6, txt:L288 | **No en v2** | **NO VERIFICABLE en v2**; verificado contra su fuente citada, `forecast-ueno-2026-11-06.md`: L106 (A 0.4252/29,83%), L122 (B "proporcional a la participación actual entre los 5 nombrados"), L139 (B 0.5553, C 0.8656/46,4%) |
| 17 nov 2026 doble hito; 5 nov vence plazo 72 h anticipo FGD; cartera IPS Gs 20.93 billones, tope 10% = Gs 2.09 billones | PDF §7, txt:L309–331 | **No en v2** | **NO VERIFICABLE en v2**; verificado contra forecast L286 (5 nov), L308 (17 nov), L315 |
| "Entre la entrada a Roche y el reconocimiento transcurrieron **23 meses**" | PDF §3, txt:L165 | v2 no da el número; derivable: dic 2024 → nov 2026 = 23 meses | **VERIFICADO** por derivación (si se contara desde nov 2024 serían 24; el PDF cuenta desde dic 2024, mes de Roche-R) |
| Huecos §8: inicio malversación sin fecha (Nota BCP/P N.° 019 + informe sellado 31 fojas sin fecha ni monto); Roche-C mensual no calculable; Δ no estimable; recursos FGD; vencimientos CDA IPS; cruce económico Roche-S no fechable; caída dic 2025 | PDF §8 | v2 §12 | **VERIFICADO** |

**Omisiones del PDF (no son errores, son huecos respecto a v2):**
- **(P-1)** No cita el b extremo a extremo **0.383** ni la ventana de referencia nov 2024–nov 2025 (**0.394 extremo / 0.451 OLS**, v2:L92). Su tabla §2 solo trae OLS. El Apéndice C.1 #3–4 de v2 exige ambos valores para el espacio.
- **(P-2)** No incluye el escenario **A5 0.4480** (reparto igual entre los 5 nombrados; forecast L116). El video largo sí lo incluye.
- **(P-3)** Su §8 de huecos **no lista los 7 PDFs MEF faltantes** (2023-01–05, 2024-08, 2026-03; v2:L26, §12) ni el **PE ago 2026 sin documentar** (fecha de la cifra de salvadoras; v2 §12).
- **(P-4)** Su tabla de backcast (§5) tiene **10 peldaños** frente a los **14 de v2 §13** (L263–275): faltan 8 jun 2026 (informe de supervisión), 19 jun 2026 (acta BCP), 10 jul 2026 (memo Rivarola) y la fila 2025 de Derechos Fiduciarios/participaciones (+8.000%). Las fechas de φ paso 5 sí aparecen en su §4, así que es condensación, no pérdida de información.

### 4.2 Podcast v1 — `script.txt` y `topics.md`: todo v1, retirado como vigente

| Dato | Cita v1 | Cita v2 | Veredicto |
|---|---|---|---|
| R nov 2024 **0.110**, "271 millones en Ueno y 2.739 millones en el sistema"; nov 2025 **0.274** | `script.txt`:L21 | v2:L9 (0.110 retirado → 0.0963), L55 (0.0963), App C.2 #1 | **RETIRADO** |
| b nov 2024–nov 2025 **0.357** | `script.txt`:L23; `topics.md`:L4 ("b = 0.357") | v2:L12 (0.356/0.342 retirados → 0.383/0.436) | **RETIRADO** (0.357 es redondeo del 0.356 v1) |
| φ paso 1: puntaje **70→60**, sin fecha | `script.txt`:L29; `topics.md`:L6 | v2:L163 (**65→60**, 9 nov 2023) | **RETIRADO** |
| Fondeo: "**noventa y dos por ciento** no fue a préstamos" | `script.txt`:L33 | v2:L206 (91.75%) | **RETIRADO** (redondeo v1) |
| "El ratio ya venía roto **desde que empezó la malversación**" | `script.txt`:L13–15 aprox. | v2, Reglas: malversación **presunta, denunciada e investigada**, inicio **sin fecha**; el backcast fecha la ruptura estructural, no el delito | **INCONSISTENTE** con v2: presenta la malversación como hecho fechable/inicio |
| "Informe BCP/P 016, **remitido al Senado el 7 de octubre de 2026**, bajo reserva" | `script.txt`:L47, L53 | v2 §12: el 016 **sigue sin aparecer en abierto**; existen Nota 019 e informe sellado de 31 fojas que NO precisan fecha ni monto | **NO VERIFICABLE en v2** (la fecha "7 oct 2026" y la remisión no constan en v2) |
| "Unos 850 millones… de unos 2.800 millones en total: **30,4%, casi un tercio**, era dinero del Estado" | `script.txt`:L7 | v2: sep 2026 USD 834,8M, **19,32% del sistema** (fondos públicos); no da total de depósitos de 2.800M | **NO VERIFICABLE en v2** (parece referirse a depósitos totales, no a fondos públicos; v2 no cubre esa cifra) |

### 4.3 Podcast "v2" — `script-v2.txt` y `topics-v2.md`: EL HALLAZGO PRINCIPAL. El episodio v2 habla con números v1 retirados

El modelo v2, Apéndice C.2 (L353–370), dice textualmente: *"El guion v2 (3,334 palabras) lleva los números v1 en los turnos del modelo y del cierre"* y lista **10 cambios exactos por turno**. Verificado cada uno contra el archivo tal como está hoy: **ninguno de los 10 está aplicado**.

| # App C.2 | Lo que exige v2 | Estado en `script-v2.txt` | Veredicto |
|---|---|---|---|
| 1 — R nov 2024 | 0.0963 (no 0.11); Ueno 298,7M / sistema 3.398,8M; dic 2024 0.1021 | L11: *"la razón era cero punto once, con doscientos setenta y un millones en Ueno y dos mil setecientos treinta y nueve millones en el sistema"* — idéntico al v1 | **RETIRADO** |
| 2 — b ventana | dic 2024–nov 2025: **0.383 extremo / 0.436 OLS**; 2ª mitad **0.802** (no 0.906); meseta **+0.031**; serie completa **0.819** | L13: *"da cero punto tres cinco seis… y cero punto tres cuatro dos… En la ventana completa fue cero punto tres cinco seis… se empinó hasta cero punto nueve cero seis… la meseta tiene una be de menos cero punto cero cuatro seis… El número único de toda la serie, cero punto ocho uno tres"* | **RETIRADO** — los cinco números (0.356, 0.342, 0.906, −0.046, 0.813) son los retirados de v2:L12, L15–L17 |
| 3 — b depende del reloj | 0.802 con reloj dic 2024; 0.344 local; 0.906 solo con reloj viejo | L15: *"da cero punto nueve cero seis con el reloj del documento, que arranca en noviembre de dos mil veinticuatro, y cero punto tres cuatro cuatro con un reloj local"* — presenta 0.906 como "el reloj del documento", sin marcarlo retirado | **RETIRADO** |
| 4 — Recap Roche | Roche-R **dic 2024, 0.1021** (nov 0.0963); Roche-C IPS nov 2024 1.06, fondos totales dic 2024 1.08; **ya no el mismo mes** | L41: *"Roche erre… se cruzó en noviembre de dos mil veinticuatro, con la razón en cero punto once. Roche ce… se cruzó el mismo mes, en uno punto cero seis"* | **RETIRADO** — contradice v2:L11, L19, L224–225. Es la contradicción central del guion |
| 5 — Cierre zona de ruptura | "…en **diciembre** de dos mil veinticuatro, por la razón, y en noviembre por el capital" | L51: *"El sistema entró en zona de ruptura en noviembre de dos mil veinticuatro, dos años antes de que alguien actuara"* | **RETIRADO** |
| 6 — "la tabla ya está aprobada tal como está" | Sin cambio | L3 y L51: la frase sigue ahí | **VERIFICADO** (v2 C.2 #6: sigue válida, la tabla corregida es la aprobada) |
| 7 — "Cinco cosas abiertas" | Añadir: existe Nota 019 e informe de 31 fojas al Senado, pero **no precisa fecha ni monto**, así que ni siquiera es seguro que el 016 lo fechara | L47: *"el inicio de la malversación, que solo se puede fechar con el informe B C P P cero dieciséis"* (y L53 repite la misma formulación) | **RETIRADO / incompleto** (v2 §12) |
| 8 — R(t) serie | Añadir: "treinta meses con razón, todos con PDF, diferencia máxima cero" | L11: *"Y la serie se re-verificó fila por fila desde la tabla"* — sin los 30 meses / todos PDF / diferencia 0 | **GAP** (afirmación parcial; le faltan los tres datos que exige C.2 #8) |
| 9 — b IPS 2.93 | Sin cambio | L15: *"La be del I P S, de dos punto nueve tres, se reproduce sobre erre de I P S"* | **VERIFICADO** (v2:L102, 2.934) |
| 10 — FGD 0.011% / embargo / fondeo 91.75% | Sin cambio | L25 (91.75%), L43 (FGD 0.011%, embargo ≈ Derechos Fiduciarios) | **VERIFICADO** (v2:L201, L206–207) |

**Otros datos del script-v2:**
- **VERIFICADO:** φ paso 1 **65→60, 9 nov 2023** (L21); φ paso 2 12 nov 2024 + baja de calificación (L21); avalancha 91.75% (L25); salvadoras 29 abr 2026, Gs 905,825M, 35% PE, Sagas 3.000×/Kasas 800× (L33); ASI 0/5, 0/4, 0/5 y fórmula δH·α/F no calculada (L37–39); muro 5 negativos / 0 positivos, leapfrog vigente b<0, reconciliación pregunta abierta (L43); caída dic 2025 0.264→0.228, −12.5%, sin explicación (L47); 32.000 jubilados, primer pago 17 nov, 7 bancos, balance 15 días (L49).
- **L3 es correcta como historia de v1** (*"la be no es cero punto tres cinco siete, es cero punto tres cinco seis…"*): describe lo que cambió de script.txt a script-v2. El error no está en L3, sino en que las líneas 11/13/15/41/51 **usan** esos números v1 como vigentes en el cuerpo del episodio.
- **INCONSISTENTE / fecha sin año:** L31: *"Y el treinta de octubre, el I P S ya estaba en nueve punto siete por ciento de su cartera"* — sin año, en un turno que viene hablando de junio–julio de **2026** y termina con "la inspección del treinta y uno de octubre". v2:L234 fija el 9,70% al **30 oct 2025**. El oyente entiende octubre de 2026. Falta el año.
- **NO VERIFICABLE en v2:** L5–7, afirmación sobre el parteaguas v2; L31, "5 jun notificó el exceso, 15 jun lo corrigió, 24 jul pidió incorporar empresas"; L9/L53, comparador CAME (México, 1,3M ahorradores, concurso feb 2026).
- **GAP menor:** el script-v2 no incorpora el **35.5% con PE abr 2026** para los USD 146M ni el **+4.9% sobre el ancla abr 2026** de las salvadoras (v2:L21, L204; C.1 #15–16 lo exigen solo para el espacio). Tampoco menciona la base Roche-C fondos totales (1.08/1.89/≈2.08) salvo en el recap retirado.

**`topics-v2.md` repite los mismos números retirados:** L2 *"b extremo a extremo 0.356 con anclajes / 0.342 con valores CSV"* (**RETIRADO**, v2:L12); L3 *"activa 0.356… empinada 0.906… meseta −0.046… b depende del reloj (0.906 o 0.344)"* (**RETIRADO**, v2:L15–L17); L6 *"Roche-R y Roche-C cruzadas juntas en noviembre de 2024"* (**RETIRADO**, v2:L19). Correctos en topics-v2: L2 R nov 2025 0.264 (v2: 0.2643), L3 b pre-Roche 0.288 y b IPS 2.93, L6 Roche-S 0.463 el 2 nov 2026. **GAP:** v2 Apéndice C.2 no lista `topics-v2.md` entre los entregables a corregir, aunque contiene los mismos números retirados que el guion.

**Consecuencia sobre el audio:** `episodio-v2.mp3` (9.339.109 B, 2026-11-07 04:21) se generó 11 minutos después de `script-v2.txt` (04:10) y v2 (L370) lo describe como el episodio actual de **19:27** con los números v1. Por guion fuente y marca temporal, el mp3 publicado **habla los números retirados**. La regrabación está pendiente (ver §6).

### 4.4 Video largo — `guion-video-largo.txt` y `capitulos.txt`: conforme a v2 en lo del modelo

| Dato | Cita guion | Cita v2 | Veredicto |
|---|---|---|---|
| C2: sep 2026 USD 834,8M, **19.32%** del sistema, R = 0.2395; IPS Gs 2.03 billones = **41.7%**; Caja Fiscal Gs 250.000M al 12.35% (31 jul 2025) | C2 (línea ~22) | v2:L203 (41.7%), §1 (R sep 2026 0.2395); 19.32% = 0.2395/1.2395, derivable | **VERIFICADO** |
| C4: R feb 2024 0.0284; salto jul 2024 a 0.061 (+80.5%, fusión Visión); nov 0.0963; dic cruza 0.10 en **0.1021**; b dic 2024–nov 2025 **0.383/0.436**; meseta **+0.031**; IPS 9.70% y deja de colocar; caída dic 2025 0.264→0.228 sin explicación | C4, L28 | v2:L55–56, L82, L90–91, L97, L234 | **VERIFICADO** |
| C4: "En junio de dos mil veinticinco la razón cruzó cero punto veinte" | C4, L28 | v2 §3: cruce entre jun–jul 2025, **≈24 jun 2025** | **VERIFICADO** (impreciso en el mes, preciso en C6: "alrededor del veinticuatro de junio") |
| C4: fondos públicos +Gs 511,865M (+35.8%) dic 2024→mar 2025 | C4, L28 | **No en v2** | **NO VERIFICABLE en v2** (misma cifra que el PDF; ver §3.3) |
| C5: ventana jul–dic 2024, mes focal dic 2024; Res. 093-046/2024 12 nov 2024, un mes antes | C5 | v2:L272–275, L284 | **VERIFICADO** |
| C6: Roche-C fondos totales dic 2024 **1.08**, dic 2025 **1.89**, mar 2026 **≈2.08**; Roche-R dic 2024 0.1021, 0.20 ≈24 jun 2025; Roche-S 5.56/12 = **0.463**; 6 anclas PE; Roche-C mensual no calculable; cruce económico Roche-S no fechable | C6 | v2:L134–136, L112–113, L153, §4 | **VERIFICADO** |
| C6: PE abr 2026 "**≈2.4 billones**" | C6 | v2:L136, L204: **Gs 2.467.235M** (2.467 billones) | **VERIFICADO con redondeo** ("≈2.4" redondea a la baja el 2.467; aceptable como aproximado, pero el valor exacto es 2.467) |
| C6/C8: "concentración en noviembre de 2024" sin valor hablado | C6, C8 | v2:L138 (Roche-C IPS nov 2024 **1.06**) | **GAP / omisión parcial:** el valor IPS 1.06 (y 1.13/1.17/1.02) no se dice en voz en el guion largo; solo aparecen los de fondos totales |
| C7: salvadoras Gs 905,825M ≈ USD 153M = 35% PE; Sagas 3.000×, Kasas 800×; Derechos Fiduciarios Gs 2,105,743M = 99.44%; USD 146M ≈ doble del tope 20%; megacuentas Gs 3.7 billones = 177.5%; φ contable 2.5 + 2.6 billones | C7, L40 | v2 §8, §6 | **VERIFICADO** |
| C8: solvencia 13.85%→5.56% en un mes; previsiones > Gs 1.6 billones tras inspección 31 oct; malversación presunta, trigger oficial insuficiencia de solvencia; denuncia MEF 5 nov (Gs 250.000M + 123.838M), 27 imputados 4 nov | C8 | v2:L155, §8, Reglas | **VERIFICADO** |
| C9: huella cimática m = 0.1021/0.1701/0.2324/0.2253/0.2395, máx 0.266; A1 2.065, A2 1.326, A3 0.438, A4 0.717; ±14.1%; u = NULL en 51.210 puntos; prueba ACO-A cohorte cripto 491 pares, Ueno fuera de cohorte | C9a/C9b, L49, L53 | **No en v2** | **NO VERIFICABLE en v2** (fuente citada: `ueno-acoa-tela-cimatica-incertidumbre.md`; m no es R(t) directa — 0.1701 no es el R jun 2025 0.1706 — y por eso no se marca inconsistente) |
| C10: embargo Gs 2.1005 billones; nombres de documentos públicos | C10, L56 | v2:L207, L263 | **VERIFICADO** |
| C11: 17 nov doble hito; FGD Gs 228.3M = 0.011%, anticipo Gs 10M/72 h; escenarios A 0.4252, **A5 0.4480**, B 0.5553, C 0.8656 con 46.4%; BNF 0.3712, Continental 0.1983; cruces marginales Sudameris/Itaú dentro de ±14.1% | C11a/C11b, L60–65 | **No en v2** | **NO VERIFICABLE en v2**; verificado contra forecast L106 (A), L116 (A5), L122/L139 (B/C), L96 (BNF/Continental), L139 (cruces marginales). El guion largo es el único documento que incluye el A5 |
| Header: "BORRADOR, no publicar sin aprobación de Elán (Elán lo sube a YouTube él mismo)"; nota: punto dic 2024 verificado contra PDF fuente 2026-11-07; "8 PDFs MEF recuperados: oct–dic 2024, ene–mar 2025, ene 2026, mar 2026" | L7–10 | v2:L26 (15→7 faltantes, 8 recuperados); mar 2026 recuperado pero sin total del sistema (R no calculable) | **VERIFICADO** en lo numérico; ver **contradicción de estado** en §5.3 |
| `capitulos.txt`: 15 segmentos, total 13:02 (782,39 s); marcas 0:00–12:39 | 19 líneas | — | **VERIFICADO** (aritmética: la suma de duraciones da 782,1 s frente a 782,39 s declarados — diferencia 0,29 s por redondeo a 0,1 s por segmento; los timestamps encadenan sin huecos) |

### 4.5 Video resumen — `guion-video.txt`: conforme a v2 en lo del modelo; su cabecera se cumple

| Dato | Cita guion | Cita v2 | Veredicto |
|---|---|---|---|
| Cabecera: "Solo cifras v2 corregidas; nada de v1 retirado" | L3 | — | **VERIFICADO** para los números del modelo |
| §1: R feb 2024 0.028; jul 0.061 (+80.5%, fusión Visión); nov 0.0963; dic cruza 0.10 en 0.1021; avalancha 91.75% | L10 | v2:L55–56, L82, L206 | **VERIFICADO** (0.028 es redondeo de 0.0284) |
| §2: b dic 2024–nov 2025 **0.383/0.436**; meseta dic 2025–sep 2026 **+0.031**; IPS 9.70%, deja de colocar; Roche-C nov 2024, Roche-R dic 2024, Roche-S 2 nov 2026 (13.85%→5.56% en un mes); malversación presunta | L13 | v2:L90–91, L97, L224–226, L155 | **VERIFICADO** |
| §3–§5 telas: trayectoria "de 0.416 a 0.045, distancia al centroide 0.49"; huella A1 2.065/A2 1.326/A3 0.438 + bulto en A4; tendencia saturación; incertidumbre ±14.1%; eje u nulo | L16, L19, L22 | **No en v2** | **NO VERIFICABLE en v2** (fuente: doc cimático; la frase "sugestivo, no decisivo" es la guarda correcta) |
| §5: "el detonante llegó un año después de que la subida se detuvo" | L22 | v2: subida se detiene nov 2025 (meseta), trigger nov 2026 | **VERIFICADO** por derivación (≈12 meses) |
| §6: 17 nov doble hito; FGD 0.011%, anticipo Gs 10M/72 h; fondos Ueno USD 834,8M; A 0.4252, B 0.5553, C 0.8656 con 46.4%; IPS reubica Gs 2.03 billones; cartera implícita **Gs 20.93 billones, estimado**; tope 10% no obliga a diversificar | L25 | **No en v2** (834,8M y 0.011% sí: v2:L203, L201) | **NO VERIFICABLE en v2** para escenarios/cartera; verificado contra forecast L106/L122/L139/L315. **Omite el escenario A5 0.4480** (igual que el PDF) |
| §7 EFIPEM 1989–2025: **85.733 nodos, 0 discrepancias, b sin cambio en 62 ajustes** | L28 | **No en v2** | **NO VERIFICABLE en v2** (otro dominio, México; no hay contradicción con v2) |
| §8 cierre: "Ueno se rompió en diciembre de dos mil veinticuatro" | L31 | v2:L272, L284 (mes focal dic 2024) | **VERIFICADO** |

## 5. Fuentes subidas por Elán vs modelo v2 — qué pasó y qué no

### 5.1 Lo que SÍ pasó al v2 (con fuente)

| Dato | Fuente | Estado en v2 |
|---|---|---|
| R(t) serie completa, dif. 0.0000 | F1/F2 + CSV | v2 §1 — pasa (30 meses; CSV hoy 31, ver C4) |
| Ancla nov 2024 corregida R 0.0963 (298.7M/3,398.8M, FX 6,696/7,793) | F2 `:59`, `:182-183` | v2 tabla cambios #1 — pasa |
| b ventana dic 2024–nov 2025: 0.383 extremo / 0.436 OLS (R² 0.873, n=12); referencia nov 2024–nov 2025: 0.394/0.451 | F2 §4 | v2 §2 — pasa; 0.356/0.357 retirado |
| b local abr–nov 2025: 0.802 (origen dic 2024); 0.344 origen local; 0.906 reproducido como artefacto de origen | F2 §4 | v2 §2 — pasa |
| b meseta +0.031 (R² 0.011, n=9); b completa 0.819 (n=30); b IPS 2.934 sobre r_ips | F2 §4; F1 `:94` | v2 §2 — pasa; v2 aclara que 2.93 es sobre r_ips, no participaciones (2.752) |
| Roche-R: primer cruce dic 2024 (0.1021); cruce 0.20 ≈24 jun 2025 | F2 §5; F6 `:31` | v2 §3 — pasa, con fecha corregida |
| Roche-C: nov 2024 base IPS 1.06; + base fondos totales nueva dic 2024 1.08, dic 2025 1.89, mar 2026 ≈2.08 | F6 §5; F2 §12 (anclas PE) | v2 §4 — pasa |
| Roche-S: 15.01% mar / 14.5% jun / 13.85% sep / 5.56% 2 nov (0.463) | F5 `:47` | v2 §5 — pasa, sin cambio |
| φ en 5 pasos (65→60 el 9 nov 2023; Res. 093-046/2024 el 12 nov 2024; fideicomiso; no-desagregación software; reserva supervisora) | F5 §4.3 | v2 §6 — pasa (corrige el "70→60" de F4) |
| ASI conteo documental 0/5, 0/4, 0/5; ASI = δH·α/F sin calcular | F5 §9.3; F1 §5 | v2 §7 — pasa como conteo; fórmula declarada sin calcular |
| ACO-A: criterio cumplido 2 nov 2026; FGD 0.011%; anticipo 4.38%; IPS/fondos sep 2026 41.7%; 146M/PE 39.8% / 35.5%; salvadoras 35% → PE implícito Gs 2.588 billones; fondeo 91.75%; embargo Gs 2.1005 billones vs Derechos −0.25%; circuito Sagas→Kasas→Vinanzas→Itti→Grupo M 29 abr 2026 | F1 §§4–5; F5 §§1.4, 5.3–5.4; F2 §12 | v2 §8 y §13 — pasa |
| Backcast escalera (13 peldaños), ventana inicio jul–dic 2024, mes focal dic 2024 | F6; F2 §9 | v2 §13 — pasa con fechas corregidas |
| Megacuentas: 3.7 billones = 177.5% PN; Derechos Fiduciarios 2,105,743M = 99.44% PN; intangibles 761,444M (+654,799M en 2025); participación 891,586M +8,000% (Red Digital 640,468M + 236,231M) | F1 §5; F4/F5 §5.1 | v2 §6, §13 peldaño 4 — pasa |
| Discrepancia mar 2026 registrada (balance 3,163,975M vs Tesoro 3,721,013M + USD 235M; dif. Gs 557,038M) | F1 `:114`; F2 `:146` | **En el CSV sí** (fila 2026-03); **en el v2 NO aparece** — GAP de traslado v2 |

### 5.2 Lo que NO pasó al v2

- **F7 completo: cero.** Grep en v2 de `fassil|master|silicon|basilea|basel|icesave|baoshang|vbs|pmc|chipre|cyprus|credit suisse|northern rock|banco popular|espírito|henan|yes bank|ghana|líbano|lebanon|came|3 millones|2.8|850 millones` = **0 coincidencias**. Ni siquiera Fassil (que F4/F5 §9.3 usan como referencia de absorción) llegó al v2. No pasaron: los 17 casos, los 4 marcadores, el límite Basilea 25%/15%, los 5 modelos de resolución, las implicaciones para Paraguay, ni los datos Ueno propios de F7 (USD 850M de USD 2,800M = 30.4%; ~3 millones de clientes).
- **F1, no trasladado:** adjudicación Caja Fiscal 31 jul 2025 — Gs 250,000M, tasa 12.35%, tope 25%, 8% de fondos excedentes, 10 entidades AA/AAA (`fondos…1e9t.md:58`); composición nov 2025 (CDA 54.5%, vista 37.6%, cta. cte. 8.0%; CDA USD 1,828M, 69.1% IPS); Asoban +140% (Gs 1,747,130M → 4,192,059M; cuota 5.7% jul 2024 → 18.6% dic 2025; ≤10 depositantes) — verificado consistente con CSV (participación jul 2024 0.0575; dic 2025 0.1857), pero no citado en v2; crecimiento del balance 2025 (Gs 7,113,789M; 34.4% sector público Gs 2,444,929M, 43.9% resto no financiero, 11.6% sector financiero, 0.6% diversas, 9.6% patrimonio); serie mensual ABC 2026 completa (v2 solo usa anclas feb/ago/sep); composición por instrumento ago 2026 de F4/F5 §2.1.
- **Caja y Equivalentes 2024 (Gs 665,685,348,380 + USD 12,241,087.73) y bonos 2025 (Gs 250,000,000,000):** en F4 `:67` y F5 `:85`; **no están en el CSV ni en el v2** (grep en v2 = 0). Quedan solo en F2 §11, por instrucción expresa de no mezclarlos en las columnas IPS del CSV. El CDA USD 27,427,000 = 19.95% solo sobrevive como el "19.95%" en la tabla ASI del v2 §7, sin sus componentes.
- **F5, no trasladado:** tasas 11.11% para CDA en Gs 2025 (grep v2 = 0); detención de 8 directivos el 3 nov; renuncia/juicio político al presidente (grep "Peña" en v2 = 0); 120 funcionarios del BCP en sucursales (grep = 0); primer pago a jubilados el 17 nov (grep = 0). Sí pasaron: denuncia MEF (Gs 250,000M + 123,838M intereses) e imputación a 27 personas (v2, Reglas).
- **Plan de 7 pasos (F1 §7):** ejecutado solo el Paso 1 (MEF, 38→39 PDFs) y parcialmente el Paso 6 (tabla maestra) y el Paso 7 (b por ventanas). **Sin ejecutar:** Paso 2 (boletines mensuales IPS — solo valores del documento), Paso 3 (balances Ueno — solo mar 2026), Paso 4 (informe final completo CGR — solo artículos ABC), Paso 5 (documentos bajo reserva: Informe 016, memorando 29 jun 2026 de Carmen Marín, informe supervisión 8 jun 2026 SBGS.ISEFS.SEFS.4 N.° 006/2026, actas IPS 12 nov 2024). Del Paso 7 faltan: la ventana ene 2025–sep 2026 y la tabla de sensibilidad por definición (R total vs R_IPS) y por FX — el v2 solo anota sensibilidad a FX ≤ 0.002 (Apéndice A).

### 5.3 Contradicciones consolidadas (v1 vs v2, y documentos vs v2)

| # | Contradicción | v1 / documento (cita) | v2 (cita) | ¿Resuelta en v2? |
|---|---|---|---|---|
| C-1 | R nov 2024 | 0,110 ancla (`resultados.md:14-51`) | 0,0963 PDF (`resultados-v2.md:39-82`) | **SÍ.** Ancla con FX mezclado (6.696/7.793); con FX único 0,0963. Tabla #1 |
| C-2 | Meses con R | 24 (23 PDF + 1 ancla) | 30, todos PDF | **SÍ en su marco; DESACTUALIZADA hoy (31 con mar 2026).** Tabla #2 |
| C-3 | Cruce Roche-R | Nov 2024, ventana sep–nov (oct sin PDF) | Dic 2024, ventana nov–dic (ambos con PDF) | **SÍ.** Tabla #3, #17 |
| C-4 | b (a) extremo | 0,356 / 0,342 | 0,383 (dic24–nov25); referencia corregida 0,394 | **SÍ, ambos retirados.** Tabla #4, #6 |
| C-5 | b ventana completa (OLS) | No existía (0,906 era solo tramo abr–nov) | 0,436 (n=12, R² 0,873) | **SÍ.** Tabla #5 |
| C-6 | b (b) local abr–nov25 | 0,906 (origen nov24) | 0,802 (origen dic24); 0,906 reproducido como b″ | **SÍ, explicado como artefacto de origen.** Tabla #7 |
| C-7 | b (c) meseta | −0,046 (n=8) | +0,031 (n=9, R² 0,011) | **SÍ en su marco; DESACTUALIZADO hoy: −0,010 con n=10 (mar 2026).** Tabla #8 |
| C-8 | b (e) completa | 0,813 (n=24; 0,814 solo PDF n=23) | 0,819 (n=30) | **SÍ en su marco; DESACTUALIZADO hoy: 0,823 (n=31).** Tabla #9 |
| C-9 | Roche-C/R mismo mes | Ambas cruzan nov 2024 | Roche-C (IPS) nov 2024; Roche-R dic 2024 | **SÍ.** Tabla #11; §10 corregido |
| C-10 | Roche-C base | Solo base IPS (5 puntos incl. dic24 1,12 sector público) | Base IPS (4 puntos) + base fondos totales nueva (dic24 1,08; dic25 1,89; mar26 ≈2,08) | **SÍ, ampliada.** La fila 1,12 pasa de tabla a texto (§4). Tabla #11 |
| C-11 | USD 146M / PE | 39,8% (PE cierre 2025) | +35,5% con PE abr 2026 (nuevo) | **SÍ, añadido.** Tabla #13 |
| C-12 | Salvadoras: tensión PE implícito | 2,59 billones, por encima de cierres (+17,6% vs 2025) | 2,59 billones; +4,9% vs ancla abr 2026 | **PARCIALMENTE.** Tensión reducida, no resuelta (PE ago 2026 sin documentar). Tabla #14 |
| C-13 | Exposición IPS / fondos sep26 | 41,8% (CSV) | 41,7% | **SÍ, corrección de redondeo.** Tabla #15 |
| C-14 | Ventana de inicio backcast | jul–nov 2024; mes focal nov 2024 | jul–dic 2024; mes focal dic 2024 | **SÍ.** Tabla #16; §13 |
| C-15 | PDFs faltantes | 15 | 7 | **SÍ en su marco; DESACTUALIZADO hoy: 6.** Tabla #18 |
| C-16 | φ paso 1 | 65 → 60, 9 nov 2023 (`resultados.md:114`) | 65 → 60, 9 nov 2023, pero con paréntesis "(v1 decía 70 → 60, sin fecha; v2 lo corrige y fecha)" (`resultados-v2.md:163`) | **NO — nueva contradicción introducida por v2.** v1 YA decía 65 → 60 CON fecha. La "corrección" no existe; la atribución a v1 es falsa contra el propio archivo v1. Además el encabezado de §6 dice "Sin cambio respecto a v1" y a la vez afirma corregir — autocontradicción interna de v2. El valor 65 → 60 en sí es el mismo en ambas. |
| C-17 | φ pasos 3–5: fechas | Paso 3: 2024–2025; paso 4: 2024; paso 5: 2024–2026, con notificaciones 5 jun y 24 jul 2026 (`resultados.md:108-121`) | Paso 3: 2025; paso 4: 2025; paso 5: jun–oct 2026, sin la notificación del 24 jul (`resultados-v2.md:157-171`) | **NO — cambio no listado.** La tabla de cambios #19 dice "φ, ASI, muro… Sin cambio", pero las fechas se estrechan y desaparece la notificación del 24 jul 2026. No hay motivo registrado. El contenido (montos) es el mismo. |
| C-18 | φ paso 4: intangibles | "+Gs 654.799M solo en 2025 (Gs 761.444M total…)" (`resultados.md:114-121`) | "+Gs 654.799M (2024–2025)" (`resultados-v2.md:157-171`) | **NO RESUELTO DEL TODO.** El mismo incremento se atribuye a "solo 2025" en v1 y a "2024–2025" en v2. El total 761.444M es el mismo. Falta precisar el periodo del incremento. |
| C-19 | Meseta: meses con R | n=8 (ene y mar 2026 sin total) | n=9 (ene 2026 con R) | **SÍ en su marco; hoy n=10 (mar 2026).** |
| C-20 | Serie 2026-01/03 | Solo Ueno (ABC), sin R | Ene 2026 con PDF y R; mar 2026 sin total (en v2) | **SÍ para ene 2026; mar 2026 resuelto después de v2 (PDF recuperado, R = 0,2662).** |
| C-21 | 2023-12 | Sin PDF; sin totales del sistema (`tabla-maestra-v1.csv` fila 2023-12) | Con PDF (archivo_5.pdf); totales del sistema registrados, Ueno en OTROS BANCOS | **SÍ en cuanto a totales; con el problema de archivo de H-5** (no hay PDF local). NOTAS §12 |
| C-22 | Gs Ueno ene 2026 | 3.331.631.000.000 (ABC redondeado) | 3.331.631.730.293 (PDF exacto) | **SÍ.** Diferencia 730.293 Gs; R no cambia a 4 decimales. NOTAS §12 |
| C-23 | Gs Ueno mar 2026 | 3.721.013.000.000 (ABC) | 3.721.013.013.754 (PDF exacto) | **SÍ (post-v2).** Diferencia 13.754 Gs. NOTAS §13 |
| C-24 | Serie R(t) y b del bloque "Lo que confirma" de parteaguas-notas | 0.110 → 0.274 → 0.235 → 0.224 → 0.247; b = 0.357 (parteaguas-notas L9–12) | nov 2024 0,0963; nov 2025 0,2643; feb 2026 0,2357; ago 2026 0,2161; sep 2026 0,2395; b 0,383/0,436 (v2 L11, L76, L12) | **NO.** El bloque dice "sin cambios" — falso contra v2. 0,274 no es ningún mes de v2; 0,224 es jun 2026, no ago; 0,247 es sep 2025, no sep 2026. Error más grave si se lee como vigente. |
| C-25 | Backcast-roche-notas usa R nov 2024 = 0,110 y ventana/focal v1 | backcast L8, L24, L30–31, L49, L54 | v2 L11, L16, L281–282, L312 | **NO.** Documento más desactualizado junto con parteaguas-notas. |
| C-26 | Backcast-roche-notas: PDFs faltantes | backcast L45: oct 2024, dic 2024–mar 2025, ene/mar 2026 | v2 L10, L242–256: solo 7 faltantes | **NO.** Lista pre-v2. |
| C-27 | Rastro: "fondos públicos +Gs 511.865M (+35,8%)" | rastro L21 | v2 L134; tabla-maestra L25/L28 (componente Gs sola) | **NO.** Etiqueta incorrecta; fondos totales +33,9%. |
| C-28 | Parteaguas-notas φ paso 1 (bloque v1) | 70→60 sin fecha (L15) | v2 L157–172: 65→60, 9 nov 2023 | **NO en el bloque v1** (el propio archivo se corrige en L69–71, pero L15 no lleva marca de retirado). |
| C-29 | Parteaguas-notas "Intangibles triplica" | 654.799M vs 269.233M (L25) | v2 L157–172 (solo +654.799M) | **NO.** Cociente real 2,43×, no 3×. |
| C-30 | Fecha posición IPS 9,70% | 30 oct 2026 en F5/F6/forecast .md | 30 oct 2025 en v2 L234 y forecast CSV L46 | **NO.** Inconsistencia interna; valor 9,70% no en disputa, solo el año. |
| C-31 | Ancla nov 2024 y FX mezclado (fuentes) | F1 `:76-77`, `:90`: 271M / 2,739M / R 0.110; b 0.357 | F2 `:59`, `:182-183`: 298.7M / 3,398.8M / R 0.0963; v2 tabla #1, #4–5 | **SÍ en v2.** F4, F5 y F6 siguen usando 0.110 / 0.357 / ×2.49 — **retirados, no vigentes**. |
| C-32 | Rango FX 6,000–6,700 | F1 §3.1: tipos de cambio "entre 6,000 y 6,700" en 2025–2026 | F2 `:59-60`: FX implícito sistema nov 2024 ≈7,793 y nov 2025 ≈6,996 — ambos fuera del rango; Ueno ago 2026 ≈5,771 y sep 2026 ≈5,805, por debajo de 6,000 | **NO resuelto en las fuentes.** El FX 6,000 reproduce exactamente los totales del sistema jul/ago/sep 2026 pero no los de Ueno (−2.4% a −2.7%) ni nov 2025 (+9.8%/+12.9%). |
| C-33 | Meseta "0.22–0.25" feb–sep 2026 | F1 `:7` | CSV verificado: feb 0.2357, **mar 0.2662**, abr 0.2543, may 0.2254, jun 0.2246, jul 0.2306, **ago 0.2161**, sep 0.2395 → rango real **0.2161–0.2662** | **NO.** Ago está por debajo de 0.22; abr y mar por encima de 0.25. F6 `:28` ("meseta 0,216–0,254") sí coincide con el CSV sin mar; v2 §1 ("meseta 0.213–0.254") también omite mar. |
| C-34 | Mar 2026: v2 desactualizado vs CSV vigente | F1 `:114`; F2 `:146` (discrepancia registrada) | CSV fila 2026-03 tiene PDF, totales y R = 0.2662; v2 §1, tabla #18, §12 dicen lo contrario | **NO.** CSV actual: 39 PDFs, 31 meses con R, 6 meses sin PDF. F2 §8 repite los 7 faltantes incluyendo 2026-03 — también desactualizada frente al CSV. |
| C-35 | Definición de ASI: F4 vs F5 | F4 `:37`: "ASI designa el seguro sistémico de absorción" | F5 §1.3: "ASI designa el Índice de Soberanía Atómica. **No es un seguro ni un mecanismo de absorción**"; v2 §7 sigue a F5 | **SÍ en v2.** F4 lleva la definición errónea. |
| C-36 | φ paso 1: puntaje 70 vs 65 (fuentes) | F4 `:128`: "de 70 a 60" (sin fecha) | F5 §4.3: "**9 nov 2023**, de **65 a 60**"; v2 §6 | **SÍ en v2.** F4 lleva el dato viejo. |
| C-37 | Nota BCP/P N.° 019 e informe de 31 fojas: procedencia GAP en el v2 | v2 `:246` (§12) y `:351` (Apéndice C #19) afirman que existe la Nota 019 (denuncia a Fiscalía + informe ~200 fojas) y un informe sellado de 31 fojas al Senado | Grep "N.° 019" / "31 fojas" / "200 fojas" en las 7 fuentes = **0** | **NO VERIFICABLE en este pase.** Ese dato del v2 **no proviene de estas 7 fuentes**; su procedencia no es verificable aquí. La conclusión del v2 ("aunque apareciera el 016, es posible que tampoco fechara la malversación") descansa en material fuera del corpus verificado. |
| C-38 | "5.1 billones": colisión numérica | F1 `:84`: pico jul 2026 "5.1 billones de guaraníes, 862 millones de dólares" (saldo de fondos públicos; CSV jul 2026 da 860.07M, −0.2%) | F6 `:33`: "facilidades G. 5,1 billones autorizadas 27 may 2024" (línea de facilidades pre-fusión) | **No es contradicción probada.** Misma cifra, conceptos distintos — **no mezclar**. El v2 §13 peldaño −1 recoge la segunda. |
| C-39 | Roche-C dic 2024/dic 2025: variantes por fuente | F6 §5: dic 2024 sector público Gs 1,747 billones / PE 1.56 = 1.12 | V2 §4: PDF 1.687 → 1.08; lista cuatro variantes (1.08–1.13, todas > 1.0) y adopta 1.08 como primario. Dic 2025: F2 §12 dice 1.91 (4.2 redondeados); v2 §4 dice 1.89 (4.161 exactos) | **SÍ, diferencia de redondeo**, registrada en v2 Apéndice B #9. Mar 2026: F2 §12 ≈2.2 vs v2 ≈2.08 — v2 Apéndice B #10. |
| C-40 | Inconsistencia interna de F2 §11 | F2 `:263-267` afirma que la tabla R(t) del documento (nov 2024: 271/2,739/0.110/9.89%…) "es idéntica a los 5 anclajes ya validados en §3" y la presenta "sin conflicto" | F2 `:59` y §12 (`:182-183`) corrigen ese 0.110 a 0.0963 | **NO.** El §11 parece redactado antes de la corrección y no actualizado. En F3 `:190-194` la misma frase es coherente (F3 aún usa 0.110). |

**Sin cambio v1→v2 (verificado):** b IPS 2,934; Roche-S (1,251/1,208/1,154/0,463); FGD 0,011%; anticipo 4,38%; embargo −0,25%; fondeo 91,75%; ASI 0/5, 0/4, 0/5; muro 5/5 negativos, 0 positivos; Δ no estimable; modo Acantilado Catastrófico con rasgos de Craquelado (juicio descriptivo, no medición); contrafactuales de bandas (hipótesis de trabajo, no mediciones). La tabla #19 de v2 es correcta en estos puntos, salvo C-16/C-17/C-18.

**Diferencias de redacción ASI (no numéricas):** v1 evalúa las condiciones "al momento del fallo" con fuentes por celda (Infobae, La Nación, CGR/ABC); v2 reescribe las celdas en forma más genérica ("reporte 13,85% ocultaba previsiones", "CDA por licitación") y cambia la etiqueta de unidades (Jubilados/Ahorristas/OEEs → Jubilados (IPS)/Ahorristas (FGD)/OEE (MEF)). Los conteos son idénticos. **Sin contradicción numérica; pérdida de granularidad de fuente en v2.**

**No-contradicciones verificadas (para que conste):** forecast y tela **no usan** ningún número v1 retirado (ambos lo declaran: forecast L11–13 "No se usan los números v1 retirados (b 0,356; cruce nov 2024)"; tela L34–41). Finanzas-mundo §0 usa solo valores v2. La guarda leapfrog (b < 0, no redefinir) es idéntica en v2 L210–216, backcast L74–84 y forecast L239–250. La calificación "malversación presunta, denunciada e investigada, no sentenciada" es idéntica en v2 L29–33, forecast L7, rastro L7–9.

### 5.4 Estado de publicación del video largo: BORRADOR vs. publicado

El guion largo dice en su cabecera (L7): *"BORRADOR, no publicar sin aprobación de Elán (Elán lo sube a YouTube él mismo)"*. El PDF (§ Material complementario) afirma que el *"Video explicativo completo (13:02) en YouTube"* ya está publicado, con URL `https://www.youtube.com/watch?v=kRJQKBUc6dI`, más publicación larga y reel en LinkedIn. Ambas cosas no pueden ser el estado actual a la vez: o la cabecera del guion quedó desactualizada tras la subida, o el PDF anticipa una publicación. **INCONSISTENCIA de estado entre documentos, pendiente de confirmar con Elán.** No es numérica. (El video largo existe en disco: mp4 20.221.914 B, 2026-11-07 12:32.)

### 5.5 Escenario A5 — cobertura desigual, no contradicción

El escenario A5 (0.4480, reparto igual entre los 5 nombrados) existe solo en el video largo. PDF §6 y guion resumen §6 saltan de A (0.4252) a B (0.5553); el guion largo C11a sí incluye A5. No es contradicción numérica (los valores coinciden con forecast L106/L116), es cobertura desigual. Tampoco hay contradicción en los escenarios de reparto: la redacción del PDF ("reparto proporcional entre los cinco nombrados", 0.5553) y la del video largo ("proporcional a lo que ya tienen", 0.5553) describen lo mismo (forecast L122).


## 6. Huecos abiertos que siguen sin resolver

Consolidados, sin duplicar: misma lista en v2 §12, forecast §8, rastro §6, tela §4, parteaguas-notas y fuentes F1/F2/F6.

| Hueco | Dónde está registrado | Qué lo cerraría |
|---|---|---|
| **Inicio de la malversación — sin fecha** (solo Informe 016 podría fecharla, y ni siquiera es seguro) | v2 L242–256; backcast L43–46; forecast L178–193; rastro L52–64 (#6); F1 §6, F2 §8–§9, F6 §7 | Informe BCP/P N.° 016 (precintado, Senado, resoluciones P.I. N.° 109, 134, 136, 137 y 139). El backcast fecha la **ruptura estructural** (nov–dic 2024), no el delito (F6 §4, `:50-52`). Nota: la procedencia de la Nota 019 / informe de 31 fojas (v2 §12) es GAP en este pase (C-37) |
| **Roche-C mensual — sin serie** (PE solo en anclas) | v2 L117–143, L242–256; F2 §12 | Serie mensual de PE. Solo 6 anclas (dic 2023 337,228M; dic 2024 1,56 billones; oct 2025 1,8 billones; dic 2025 2,20 billones; ene 2026 >USD 335M; abr 2026 2.467.235M implícito por tope 20%) |
| **Roche-S económico — no fechable** con datos públicos | v2 §5, §12; F6 §3C | Saldos intangibles/fiduciarios de cierre 2025 con fecha mensual; solvencia reportada > 12% hasta sep 2026; salto a 5,56% en nov tras previsiones > Gs 1,6 billones |
| **Δ de ACO-A — sin estimar** | tela L34, L121, L341; forecast L70; v2 L191–200, L242–256 | Montos por receptor y por fecha (balance de exclusión 17 nov + MEF oct/nov 2026) — la serie A(τ) "empieza ahora" (forecast L70) |
| **Leapfrog / reconciliación muro–b — pregunta abierta** | v2 §9, §12; forecast L239–250; backcast L74–84 | Hipótesis (eventos positivos = acciones que bajan R(t), b < 0) no establecida; test medible en publicaciones futuras del MEF y del IPS, sin fecha |
| **ASI = δH·α/F — sin calcular** | v2 §7, §12; tela L333–341; finanzas L236–248 | Sin serie de eventos de comportamiento. Equivalencia entre la fórmula del repo y el conteo documental: pregunta abierta para Elán |
| **Diversificación de ahorristas individuales — sin dato** | v2 §7, §12 | Sin catastro de depositantes |
| **Caída dic 2025 — sin explicación** | v2 L232–241 (#6), L301–324; F2 §5, F3 §5 | Ningún documento la comenta. Ueno USD −12,1% / Gs −12,6% vs nov 2025, R 0,264→0,228 mientras el sistema sube |
| **PDFs MEF faltantes — 6 meses hoy** (2023-01–05, 2024-08) | v2 §12 (dice 7, incluye 2026-03 ya recuperado); NOTAS §2; F2 §8 | Sin ellos no hay R(t) 2023 ni cierre de ago 2024. 2023-12 tiene totales pero Ueno no extraíble (OTROS BANCOS); ene 2024 USD de Ueno dentro de OTROS BANCOS |
| **Serie IPS mensual — solo valores del documento** (CDA anual + cortes) | NOTAS §8, ambas versiones; F1 §6 | Sin boletines mensuales descargados |
| **Balances de Ueno — solo la cifra de mar 2026** del documento | F1 §6; v2 §12 | Sin serie de patrimonio efectivo ni de depósitos del sector público según balance |
| **PE ago 2026 — sin documentar** (fecha de la cifra de salvadoras; tensión +4,9% no resuelta) | v2 L242–256; rastro L52–64 (#5) | Documento del PE de ago 2026 |
| **Pregunta del §9 de NOTAS sigue abierta** aunque el backcast la resolvió en tres ratios (C/R/S) | v2 Ap. B #15; F2 §9 | NOTAS §9 (pregunta "qué ratio es el ratio de Roche") no se actualizó; el backcast es la autoridad |
| **Backcast v2 sin recalcular con mar 2026** | NOTAS §13: decisión pendiente de Elán | Con la tabla vigente, los valores a actualizar en una eventual v3 son: (c) meseta n=10, b ≈ −0,010; (e) b ≈ 0,823, n=31; meseta 0,2132–0,2662; PDFs faltantes 6; 31 meses con R. La secuencia de bandas (Roche-C nov 2024 → Roche-R dic 2024 → Roche-S 2 nov 2026) **no cambia** con mar 2026 |
| **GAP nuevo de esta revisión (método):** la variante (c′) usa numeración secuencial contra la regla de calendario declarada (H-1); y la discrepancia mar 2026 no es solo Gs 557,038M — el USD 235M queda sin conciliar aparte (§2.8) | §2.2 H-1; §2.8 | Corregir en una eventual v3 |
| **Monto total que pagará el FGD + recursos totales del FGD + nº de depositantes de Ueno** | forecast L55–60, L267–281 (#1); rastro L52–64 (#3) | Publicación FGD/BCP |
| **Cronograma de vencimientos de los CDA del IPS** (Gs 2,03 billones sin ritmo) | forecast L217–222, L267–281 (#2); rastro L52–64 (#4); CSV L70 (HUECO) | Publicación del IPS |
| **Balance de exclusión (17 nov 2026)** — reparto real, valuación de lo realizable | forecast L62, L147, L267–281 (#3); rastro L52–64 (#1) | El balance mismo, 17 nov 2026 |
| **PE por banco receptor** (sin él no hay Roche-C de receptores) | forecast L251–262, L267–281 (#4) | Boletines del BCP |
| **Valuación de bienes embargados y megacuentas** (embargo Gs 2,1005 billones congela, no cobra) | forecast L151–176, L267–281 (#6); rastro L52–64 (#2) | Balance de exclusión / remates |
| **Desenlace de la cadena política** (renuncia/juicio político — sin sucesor, fecha ni medidas) | forecast L194–196, L267–281 (#5) | Los hechos |
| **Fechas de Nota BCP/P N.° 019 e informe de 31 fojas al Senado; audiencias, formalización, juicio, sentencia, montos recuperados** | forecast L178–193, L267–281 (#7); CSV L69–70 (HUECO); v2 L242–256 | Fiscalía / juzgado. Procedencia GAP (C-37) |
| **Los 2 oferentes no nombrados** (7 oferentes, 5 nombrados: BNF, Itaú, GNB, Continental, Sudameris) | forecast L68, L267–281 (#8); rastro L52–64 (#8) | Publicación IPS/BCP — decide entre escenarios A (entre 7) y A5 (entre 5) |
| **Haberes mensuales de los 32.000 jubilados** | forecast L55–60, L267–281 (#9) | IPS |
| **MEF oct/nov 2026** (primera R_X post-resolución; ¿Ueno sigue con saldo o desaparece?) | forecast L143–148, L267–281 (#10) | El feed mensual |
| **u = NULL** (0/51.210 puntos; eje sin definición operativa en ningún dominio); **φ postulada, no medida** | tela L21, L277, L333–341 (§4.1–4.2); finanzas L236–248 (gap 8) | Definición operativa de u; calibración de φ por caso |
| **Figura no identifica el dominio** (LOO 50,7%; ACO 4/18); asignación ACO de Ueno sugestiva, margen delgado (1,08 vs 1,12 E2 en solo-forma) | tela L198–265, L333–347 (§4.4) | No es hueco de dato: es límite del método, registrado |
| **Ventana manda en la figura** (A1 2,07 primaria vs 5,93 sensibilidad); **mar 2026 sin R** (interpolación cruza el hueco en τ≈0,6); **τ=1 con m sostenido** (convención) | tela L333–364 (§4.5–4.7) | No se imputa; se declara |
| **Cobertura OEE/IPS por el FGD** (¿los depósitos de OEE/IPS entran al FGD? cobertura por instrumento = cuestión legal) | forecast L55–60 | Definición legal |
| **Prueba prospectiva no cubre a Ueno** (fuera de la cohorte cripto) | tela L124–143, L333–364 (§4.9) | Nada — es límite de alcance, no hueco a cerrar |
| **Gaps Finanzas-mundo** (dato por banco; flujos entre países BIS; GFDD hasta 2020/2021; ASI no computable; puente no medido; método de señales no caza saltos — Ghana) | finanzas L236–248 | Datasets BIS / Bankscope / balances por entidad |
| **R(t) 2023: no calculable** | F2 §5; CSV filas 2023-06–12 | Ueno sin fila individual jun–ago 2023 (saldo nulo o no reportado, no se imputa cero) o dentro de OTROS BANCOS sep–dic 2023 |
| **Serie diaria/semanal del Tesoro en tabular, cronograma individual de vencimientos de CDA del IPS, catastro de depositantes y operativa de pago del FGD por banco receptor, balances trimestrales completos 2023–2026, resoluciones IPS 12 nov 2024, informe final completo CGR** | F1 §6, tabla de 7 faltantes; F2 §8 | La absorción por banco receptor debe medirse, no asumirse como traslado uniforme (F1 §5) |
| **Anomalías registradas sin ajustar:** salto jul 2024 (R 0.034→0.061, +80.5% en un mes; Visión seguía listado por separado); USD Ueno feb–mar 2024 casi idéntico (+USD 16) mientras Gs sube (posible cifra arrastrada) | F2 §5, CSV filas 2024-02/03 | — |

## 7. Qué está pendiente de Ueno

### 7.1 Con fecha o decisión

- **Doble hito 17 nov 2026 — SÍ aparece y es el centro del forecast:** primer pago a jubilados + cierre del balance de exclusión (forecast L37–40, L62, L282–292; rastro L48, L54, L65; tela L317–319; parteaguas-notas L22, L38; PDF §7; guiones largo C11a y resumen §6). Es el primer hito observable: si el balance no cierra ese día, la absorción se retrasa (escenario 1b); si cierra, la A(τ) empieza a medirse. También el 5 nov 2026 (límite 72 h del anticipo) como hito previo.
- **Regrabar el podcast episodio v2 (lo más urgente).** Aplicar los 10 cambios del Apéndice C.2 de v2 a `script-v2.txt` (y los mismos números en `topics-v2.md`, que C.2 no lista pero que los repite), y regrabar `episodio-v2.mp3` (actual 19:27, con números v1 hablados). v2:L370 advierte: con los cambios el episodio queda en **~20:05** si no se recorta nada; si Elán mantiene el objetivo de 15 min, hay que recortar ~5 min en otro bloque o dividirlo en dos partes (oferta abierta). El episodio v1 (`script.txt`/`episodio.mp3`) queda como registro histórico, no se usa.
- **Aplicar los 19 cambios del Apéndice C.1 al espacio SNT** (subsección "Qué muestran los modelos", sección caso Ueno, subsección 5), **solo con el visto bueno de Elán**. v2 lo dice expreso: *"Para aplicar después, con el visto bueno de Elán… No se ha tocado ni el espacio ni el podcast."* No se tocó en esta tarea.
- **Aclarar el estado del video largo:** cabecera BORRADOR (guion) frente a publicado en YouTube/LinkedIn (PDF). Confirmar con Elán cuál es el estado real y actualizar la cabecera o el PDF según corresponda.
- **Decisión de Elán pendiente (podcast):** parteaguas-notas L79–80 — dos líneas del podcast backcast quedan desactualizadas por la v2 (malversación en v2; cruce Roche el 2 nov sustituido por el backcast mismo): "Recomendado: actualización (regrabar episodio o grabar episodio corto de corrección). Decisión de Elán pendiente." También v2 Apéndice C (L325–370) y forecast Apéndice B (L301–315) listan cambios para espacio y podcast "para aplicar después, con el visto bueno de Elán. No se ha tocado ni el espacio ni el podcast."
- **Pendiente de corrección en los propios documentos revisados:** actualizar backcast-roche-notas (C-25, C-26) y el bloque "Lo que confirma" de parteaguas-notas (C-24) a los valores v2, o marcarlos explícitamente como notas pre-v2 / sobre el documento v1; corregir la etiqueta "fondos públicos" del rastro (C-27) a "componente en guaraníes"; corregir "triplica" (C-29); corregir "(30 oct 2025)" del CSV del forecast (C-30); explicar los denominadores LOO 737 vs 740 (tela L209–211); añadir la columna A4 al CSV de huella o citar su fuente (tela L161).
- **Pendiente metodológico (tela §4.2):** calibrar φ por caso, no por dominio — "el paso siguiente natural que la propia auditoría señala" (tela L333–341).
- **Pendiente normativo (forecast §7.2, v2 §9):** la hipótesis muro–b (5 eventos positivos = acciones que bajan R(t), b < 0) sigue **no establecida**; el test es medible en publicaciones futuras del MEF y del IPS, pero no hay fecha.
- **GAP — "etiqueta espacio":** en los documentos leídos **no consta** ninguna "etiqueta" pendiente concreta para el espacio. Lo que consta como pendiente del espacio es la lista C.1 (19 cambios de texto). Si existe una etiqueta pendiente, no está en estos archivos; no se inventa.
- **GAP — `topics.txt`:** el archivo pedido con ese nombre no existe; el v1 es `topics.md` y el v2 es `topics-v2.md`. Conviene confirmar si `topics.txt` debía existir o si la tarea se refería a `topics.md`.
- **Pendientes menores de precisión:** añadir el año (2025) al "30 de octubre" del 9,70% del IPS en el podcast v2 (L31); incorporar en el podcast el 35.5% (PE abr 2026) y el +4.9% de salvadoras y la base Roche-C fondos totales, que hoy solo están en el espacio/PDF; completar en PDF y resumen el escenario A5 y, en el PDF, los 7 PDFs faltantes y el PE ago 2026 en §8, y el b extremo 0.383 / referencia 0.394/0.451 en §2.
- **Actualización a v3 (si Elán la decide):** recalcular el backcast con mar 2026 (31 meses), corregir (c′) a calendario o declarar secuencial, corregir φ paso 1 en v2 (C-16), precisar φ pasos 3–5 y el periodo del incremento de intangibles (C-17/C-18), y resolver H-5/H-6 (conteo y clasificación de PDFs, dic 2023).

### 7.2 Subida a GitHub — BLOQUEADA hasta decisión de Elán

Veredicto de esta revisión: **NO listo para subir tal cual.** La v2 está desactualizada frente a la tabla vigente (31 meses, b meseta −0,010, serie completa 0,823), el podcast "v2" habla números v1 retirados, el conteo de PDFs en NOTAS es inconsistente (H-5/H-6), y el método (c′) es inconsistente con lo declarado. El reporte PDF es lo más limpio contra v2. **No se subió nada en esta revisión.** Queda pendiente la decisión de Elán: ¿subir así con este informe de auditoría, o corregir primero? También faltan, según la nota de coordinación: qué día exacto, qué repo/carpeta/rama, y qué chat es "SUDO Universe" (no hay chat con ese nombre en la lista; el organizador es b7993e90). No se inventan esos datos.

## 8. Qué números usar como vigentes (contra la tabla maestra actual)

- R nov 2024 **0,0963** (no 0,110 — RETIRADO); cruce Roche-R **dic 2024 (0,1021)**; Roche-C (IPS) **nov 2024 (1,06)**; Roche-S reconocido **2 nov 2026 (0,463)**.
- b ventana dic24–nov25: **0,383 extremo / 0,436 OLS (n=12, R² 0,873)**; segunda mitad abr–nov25: **0,802** (origen dic24) — el 0,906 es artefacto de origen, RETIRADO como valor de ventana; con origen local 0,344.
- Meseta dic25–sep26: **n=10, b ≈ −0,010 (R² ≈ 0,001), sin tendencia** — el +0,031 de v2 queda desactualizado por mar 2026.
- Serie completa: **b ≈ 0,823 (n=31, R² 0,911)** — el 0,819 de v2 queda desactualizado.
- b IPS **2,934** (sobre r_ips, n=3 anual, banda no clasificada).
- Roche-C fondos totales: dic24 **1,08**; dic25 **1,89**; mar26 **≈2,08** (PE abr 2026 como proxy, aproximado).
- ACO-A: FGD/exposición IPS **0,011%**; anticipo **4,38%**; IPS/fondos sep26 **41,7%** (CSV) vs 40,8% (doc); USD 146M/PE **39,8%** (dic25) / **35,5%** (abr26); salvadoras PE implícito **Gs 2,59 billones** (+4,9% vs abr26, tensión no resuelta); fondeo no a préstamos **91,75%** (insumos externos); embargo **Gs 2,1005 billones, −0,25%** vs Derechos Fiduciarios.
- φ paso 1: **65 → 60, 9 nov 2023** (igual en v1 y v2; la "corrección" que v2 se atribuye no existe, C-16).
- PDFs faltantes hoy: **6** (2023-01–05, 2024-08). R(t): **31 meses**.
- Mar 2026: **R = 0,2662**, máximo de la meseta 2026, supera nov 2025 (0,2643); rango de meseta **0,2132–0,2662**.

## 9. Resumen ejecutivo por documento

- **Modelo v1/v2 + valores + tabla + NOTAS: v2 internamente coherente en su marco (30 meses), casi todos sus números reproducen exactos. PERO v2 desactualizada vs tabla vigente (31 meses, mar 2026).** Hallazgos nuevos: H-1 (c′ secuencial vs calendario declarado), H-5 (conteo PDFs / dic 2023 contado dos veces), H-6 (clasificación oct 2024), C-16/C-17/C-18 (φ paso 1 atribuida falsamente, fechas φ estrechadas sin listar, periodo intangibles ambiguo).
- **Forecast + CSV: 100% de los valores verificables coinciden con v2 o con su propia aritmética** (base 16 bancos, escenarios A/A5/B/C, FGD, IPS estimados, embargo). Defectos: CSV L2 (cabecera duplicada) y L46 (año 2025 vs 2026).
- **Tela + huella: valores v2 y CSV coinciden;** A1/A2/A3, distancias 1,24/0,49 y LOO son consistentes internamente pero **no verificables desde v2/CSV solos** (requieren el repo y `/tmp/ueno_tela.py`); A4 no está en el CSV; Δ sigue GAP; u NULL.
- **Rastro: casi todo VERIFICADO contra v2;** una etiqueta incorrecta (C-27) y dos imprecisiones heredadas de v2 (FX de USD 153M; "excedente USD 146M").
- **Backcast-roche-notas: mezcla valores verificados con números v1 retirados (C-25, C-26)** — el documento más desactualizado respecto a v2 junto con parteaguas-notas.
- **Parteaguas-notas: el bloque v1 "Lo que confirma" (C-24) y φ paso 1 (C-28) contradicen v2;** su sección v2 (L44–82) sí está actualizada y contiene las correcciones.
- **Finanzas-mundo §0 Ueno: VERIFICADO íntegro contra v2;** el resto del documento es por diseño NO VERIFICABLE contra v2 (datos Banco Mundial) y no presenta contradicciones con Ueno.
- **PDF (9 páginas): VERIFICADO contra v2 en todos sus números del modelo.** Omisiones parciales P-1 a P-4 (b extremo 0.383, A5, 7 PDFs faltantes y PE ago 2026 en huecos, backcast condensado a 10 peldaños). Es el documento más completo y el único posterior a v2 que incorpora todas las correcciones.
- **Guion largo: VERIFICADO contra v2** en todo lo del modelo; sus números de forecast y cimática son NO VERIFICABLES en v2 pero verificados contra sus fuentes citadas (forecast). Pendiente: resolver su estado BORRADOR vs. publicado.
- **Guion resumen: VERIFICADO contra v2** en todo lo del modelo; su cabecera ("solo cifras v2") se cumple. Sus números de telas/EFIPEM/forecast son NO VERIFICABLES en v2.
- **Podcast v2 (script-v2.txt + topics-v2.md + episodio-v2.mp3): RETIRADO en su núcleo numérico.** Lleva los números v1 en los turnos del modelo y del cierre; los 10 cambios del Apéndice C.2 de v2 siguen sin aplicar y el audio de 19:27 habla esos números. **Regrabación pendiente.**
- **Podcast v1 (script.txt + topics.md): RETIRADO** como vigente en su totalidad numérica (0.110, 0.357, 70→60, 92%); queda como registro histórico.
- **Fuentes subidas por Elán: lo sólido** es la serie R(t) del CSV (reproduce exacto), la corrección del ancla nov 2024 (0.110 → 0.0963) y de la ventana de b (0.357 → 0.436 OLS), Roche-C/R/S, φ en 5 pasos y la escalera backcast. **Lo retirado:** todo número que dependa del ancla 0.110 (b 0.357, ×2.49, cruce Roche-R en nov 2024, mes focal nov 2024, "70→60", ASI como "seguro") — presente aún en F3, F4, F6 y en la tabla R(t) de F4/F5. **Lo desactualizado:** el v2 (05:25) frente al CSV vigente (10:48). **Lo no trasladado:** el comparativo global completo (F7, 17 casos, 4 marcadores, Basilea, 5 modelos de resolución), la adjudicación de Caja Fiscal, Asoban, la descomposición del balance 2025, Caja y Equivalentes y bonos del IPS, y los Pasos 2–5 del plan de adquisición. **GAP de procedencia:** Nota BCP/P N.° 019 + informe de 31 fojas (v2 §12) no existen en ninguna de las 7 fuentes verificadas.

## 10. Límites de esta revisión

- El contenido de audio/video no se escuchó ni se vio — solo se verificaron los guiones escritos; el audio se evalúa por su guion fuente y su marca temporal.
- Los scripts citados (`/tmp/modelo_ueno.py`, `/tmp/modelo_ueno_v2.py`, `/tmp/forecast_ueno.py`, `/tmp/ueno_tela.py`) están fuera del corpus: sus hashes / salidas no se comprobaron aquí, salvo el md5 del CSV del forecast, que coincide.
- Todo lo marcado NO VERIFICABLE lo es **dentro del corpus de archivos leídos** — las fuentes externas citadas (parteaguas v2, ABC Color, BCP, Infobae, CGR, Asoban, EEFF, Banco Mundial) no forman parte de todos los frentes, y donde no se incluyeron se marca así.
- Algunas líneas citadas por los lectores paralelos llevan "~aprox." en sus informes de origen; las citas clave de este informe final fueron re-verificadas por grep / recomputación por los lectores; las secundarias se citan tal como las reportaron.
- No se leyeron en este pase: versiones EN de los papers SNT, los .docx/.pdf de los papers, ni `papers/marco_teorico.md` (v34 vigente) — ese es el siguiente paso para la reconstrucción SNT, fuera del alcance Ueno.
- Archivos consultados, sin modificar. Ningún archivo fue editado, movido ni subido; el espacio SNT no se tocó.

---
*Fin del informe. Archivo: `auditoria-terminos/ (no incluido en el repo)REVISION_DOCUMENTOS_UENO.md`*
