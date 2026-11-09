# Ueno Bank — Corrección v3 (7 de noviembre de 2026)

**Fecha de la corrección:** 2026-11-09
**Orden del autor (Elán, WhatsApp 2026-11-09 ~12:37):** corregir y subir todo lo que se usó en Ueno el 7 de nov; después él lo pasará por otros 2 filtros antes de integrar.
**Alcance de este staging:** `~/workspace/ueno-correccion-2026-11-09/` — solo texto UTF-8, sin binarios.
**NO se tocó:** `~/workspace/snt-taxonomia/` (originales intactos), el espacio SNT, ni `main` de ningún repo.
**NO se subió nada a GitHub desde aquí:** el push lo hace el agente padre. No se crearon chats.
**Regla aplicada:** NUNCA ASUMAS, SIEMPRE VERIFICA contra documentación, no contra memoria. Lo NO VERIFICABLE se marca GAP, nunca se inventa.

Base: auditoría completa `REVISION_DOCUMENTOS_UENO.md` (564 líneas, 113.134 B, incluida en este staging, md5 `36b8cac1ed2916d7a6ad7561fa1f18fe`, idéntica al original en `~/workspace/snt-taxonomia/auditoria-terminos/`).

## Números vigentes v3 (recomputados, ver `VERIFICACION_V3.md`)

- R(t): **31 meses** con R. Mar 2026 **R = 0,2662** (participación 0,2103), máximo de la meseta, supera nov 2025 (0,2643).
- R nov 2024 **0,0963** (no 0,110 — RETIRADO); cruce Roche-R **dic 2024 (0,1021)**; Roche-C (IPS) **nov 2024 (1,06)**; Roche-S **2 nov 2026 (0,463)**.
- b ventana dic24–nov25: **0,383 extremo / 0,436 OLS (n=12, R² 0,873)**; segunda mitad abr–nov25: **0,802** (origen dic24; 0,906 artefacto de origen, RETIRADO como valor de ventana; origen local 0,344).
- Meseta dic25–sep26: **n=10, b ≈ −0,010 (b = −0,0101, R² = 0,0007), sin tendencia** — el +0,031 de v2 queda desactualizado por mar 2026. Rango de meseta **0,2132–0,2662** (v2: 0,213–0,254).
- Serie completa: **b ≈ 0,823 (b = 0,8234, a = 0,0157, R² = 0,9108, n=31)** — v2 decía 0,819, n=30.
- (c′) meseta local, calendario: **b = +0,0065, R² = 0,0048, n=10**; en v3 calendario == secuencial (sin huecos en dic25–sep26 con mar 2026). Controles H-1 reproducen la auditoría: v2 n=9 calendario +0,0104 / secuencial +0,0086 (publicado); v1 n=8 calendario −0,0046 / secuencial −0,0120 (publicado).
- b IPS **2,934** (sobre r_ips, n=3 anual). Roche-C fondos totales: dic24 **1,08**; dic25 **1,89**; mar26 **≈2,08**.
- ACO-A: FGD/exposición IPS **0,011%**; anticipo **4,38%**; IPS/fondos sep26 **41,7%** (CSV) vs 40,8% (doc); USD 146M/PE **39,8%** (dic25) / **35,5%** (abr26); salvadoras PE implícito **Gs 2,59 billones** (+4,9% vs abr26, tensión no resuelta); fondeo no a préstamos **91,75%** (insumos externos); embargo **Gs 2,1005 billones, −0,25%** vs Derechos Fiduciarios.
- φ paso 1: **65 → 60, 9 nov 2023** (igual en v1 y v2; la "corrección" que v2 se atribuye no existe, C-16).
- PDFs faltantes hoy: **6** (2023-01–05, 2024-08).
- Secuencia de bandas **sin cambio** con mar 2026: Roche-C nov 2024 → Roche-R dic 2024 → Roche-S 2 nov 2026.

## Inventario exacto

Medido con `wc -l -c` / `du -sb` / `file` / `find -type l` el 2026-11-09 ~12:44, antes de añadir este README. Total del staging sin este README: **551.532 B** (438.398 B previos + 113.134 B de la auditoría). **Todo texto UTF-8/ASCII, 0 symlinks, 0 binarios** (sin PDF, sin mp3/mp4, sin PNG, sin PDFs MEF).

### A. Archivos CORREGIDOS v3 (nuevos)

| Archivo | Líneas | Bytes | Qué cambió |
|---|---|---|---|
| `modelo-ueno-resultados-v3.md` | 412 | 62.979 | Basado en v2 completo (§§1–13 y apéndices íntegros, sin resumir sustancia). Tabla de cambios v2→v3 de 16 filas con cita archivo:línea. 31 meses, mar 2026 0,2662, meseta −0,0101 n=10, completa 0,8234 n=31, rango 0,2132–0,2662, 6 PDFs faltantes, discrepancia mar 2026, H-1 (c′ calendario), C-16, C-17, C-18 (periodo POR CONFIRMAR), IPS 9,70% a 30 oct 2026, H-5 explicado, H-6 registrado. |
| `podcast/script-v3.txt` | 78 (25 cabecera + 53 turnos) | 24.410 | 12 líneas cambiadas contra v2. 10 cambios C.2 + v3 (meseta −0,010, serie 0,823, 31 meses). 27 turnos Mole + 26 Lucía, 4.155 palabras. Cabecera: GUION CORREGIDO v3, AUDIO NO regrabado. |
| `podcast/topics-v3.md` | 23 (10 cabecera + 13 viñetas) | 4.802 | Mismos números corregidos que el guion. |
| `backcast-roche-notas-v3.md` | 106 | 13.211 | Serie vigente, ventana jul–dic 2024 focal dic 2024, Roche-C nov / Roche-R dic (no mismo mes), φ 65→60, 6 PDFs faltantes, oct 2024 sí con PDF (R=0,0780). |
| `parteaguas-notas-v3.md` | 101 | 14.588 | Bloque "Lo que confirma" corregido (C-24), φ paso 1 marcado RETIRADO en bloque v1 (C-28), "triplica"→2,43× (C-29). Sección VERSIÓN 2 conservada. |
| `rastro-del-dinero-ueno-v3.md` | 85 | 7.496 | C-27: +511.865M solo componente Gs; totales +572,7 billones +33,9% (verificado en CSV: dic 2024 USD equiv 281.207.595 → mar 2025 376.654.602 a FX 6.000; diferencia Gs 572.682.042.000 = +33,94%). USD 153M→151,0M a FX 6.000; excedente USD 73M / 63,8M. |
| `forecast-ueno-valores-v3.csv` | 70 | 5.616 | Solo 2 cambios: eliminada cabecera duplicada L2; L46 "(30 oct 2025)"→"(30 oct 2026)". Ningún valor numérico cambió (md5 `d80bf8359a79557b74cb8588c2d990f1`; original md5 `cce53a6cbdbe53e425779633743958af`, coincide con el declarado en forecast L3). Diff en `forecast-ueno-valores-v3.diff` (297 B). |

### B. Verificación

| Archivo | Líneas | Bytes | Qué es |
|---|---|---|---|
| `verificar_v3.py` | 171 | 8.137 | Script stdlib: lee `tabla-maestra-ueno-mef.csv`, recomputa R(t) 31 filas desde equivalentes y desde crudos, b meseta y completa, (c′) calendario vs secuencial + controles H-1. Re-ejecuta limpio, exit 0. |
| `VERIFICACION_V3.md` | 119 | 10.822 | Salida del script: R mar 2026 0,2662; diferencia máx. vs CSV 0,000050 (0,0000 a 4 decimales, puro redondeo); b meseta −0,0101 R² 0,0007 n=10; b completa 0,8234 R² 0,9108 n=31; (c′) +0,0065 en ambos relojes; discrepancia mar 2026: solo Gs 557.038.013.754; USD exacto 235.381.762 → a FX 6.000 Gs 1.412.290.572.000; total en equivalentes Gs 1.969.328.585.754. |
| `VERIFICACION_UENO_V3.md` | 104 | 7.420 | Verificación del frente de copias: forecast v3 línea por línea y por tokens numéricos; cada copia por md5 de cuerpo o byte a byte. |

### C. Copias SIN CAMBIAR (registro v1/v2, con cabecera que lo dice; CSV sin cabecera interna, con .NOTA.md aparte)

| Archivo | Líneas | Bytes | md5 original | Nota |
|---|---|---|---|---|
| `modelo-ueno-resultados.md` (v1) | 270 | 32.200 | `61d0497454d5ab7c068e7834ae17195c` | Cuerpo == original. |
| `modelo-ueno-resultados-v2.md` | 378 | 51.296 | `986d79b469c031dc345638347b5bb616` | Cuerpo == original. |
| `modelo-ueno-valores.csv` (v1) | 50 | 2.920 | `d41df2e5f4bf62898b45ae6659291a3d` | Byte a byte. Nota: `modelo-ueno-valores.csv.NOTA.md` (586 B). |
| `modelo-ueno-valores-v2.csv` | 63 | 4.017 | `38977724d76307f5913540f0f11abbed` | Byte a byte. Nota: `.NOTA.md` (592 B). |
| `tabla-maestra-ueno-mef.csv` (vigente) | 46 | 12.335 | `7c22f9f046a67d6e950cb54afef38f12` | Byte a byte. Nota: `.NOTA.md` (640 B). |
| `tabla-maestra-ueno-mef-v1.csv` | 46 | 11.535 | `69566dc48555fdf4bec452d6e2772809` | Byte a byte. Nota: `.NOTA.md` (599 B). |
| `tabla-maestra-NOTAS.md` (vigente) | 306 | 25.169 | `761b2f71aad18322be90ab08b28c7e22` | Cuerpo intacto; solo cabecera de corrección H-5/H-6 al inicio (no se reescribió el cuerpo). |
| `tabla-maestra-NOTAS-v1.md` | 203 | 15.647 | `b1daaaf57c4646926027a27cb0733705` | Cuerpo == original (byte-idéntica a F3). |
| `forecast-ueno-2026-11-06.md` | 323 | 33.577 | `d1260013838662e8b7309b43dcc7510a` | Sin nº de versión; punto de partida v2. |
| `ueno-acoa-tela-cimatica-incertidumbre.md` | 402 | 24.743 | `8eca6f13c5a299108056227cf2f7fb19` | Marco SNT v2.7.5.1 / marco v34. |
| `ueno-huella-cimatica.csv` | 3 | 420 | `fafc1c01b5d123ad9cc52c3104804a92` | Byte a byte. Nota: `ueno-huella-cimatica-NOTA.md` (1.492 B): A4 0,717 no está en el CSV (solo A1/A2/A3, fuente tela L161); denominadores LOO 737 vs 740 sin explicar (tela L209–211, L220, L361). |
| `finanzas-mundo-snt.md` | 266 | 34.643 | `f26ef328d479325173e7d491aa2bf24b` | §0 Ueno verificado íntegro contra v2; resto por diseño NO VERIFICABLE contra v2 (Banco Mundial). |
| `video-largo-ueno/guion-video-largo.txt` | 81 | 19.566 | `ee24ade86441f03e0e8ccd19581ce309` | Cuerpo == original + nota de estado en cabecera (ver discrepancia abajo: estado vigente PUBLICADO). |
| `video-resumen-ueno/guion-video.txt` | 44 | 6.643 | `7beef5344cbb7e3e9fec44defde53acd` | Cuerpo == original + nota de estado en cabecera. |

### D. Auditoría

| Archivo | Líneas | Bytes | md5 |
|---|---|---|---|
| `REVISION_DOCUMENTOS_UENO.md` | 564 | 113.134 | `36b8cac1ed2916d7a6ad7561fa1f18fe` (idéntica al original) |

**NO incluidos (a propósito):** reporte PDF de 9 páginas, podcast mp3 (`episodio.mp3`, `episodio-v2.mp3`), videos mp4, PNG, PDFs MEF, `capitulos.txt`, `topics.txt` (no existe; el v1 real es `topics.md`).

## Qué NO se corrigió y por qué

1. **Audio del podcast NO regrabado.** `episodio-v2.mp3` (9.339.109 B, 2026-11-07 04:21, 19:27) sigue hablando los números v1 retirados por guion fuente y marca temporal. El guion v3 está listo; la regrabación es decisión de Elán. Con los cambios el episodio queda en ~20:05 sin recortes (v2 Ap. C.2); si Elán mantiene 15 min, hay que recortar ~5 min o dividirlo en dos.
2. **Video largo: estado confirmado PUBLICADO, pero la copia del guion lleva nota desactualizada.** La auditoría §5.4 registraba BORRADOR (cabecera del guion) vs publicado (PDF). Durante la corrección llegó la confirmación: Elán confirmó 2026-11-09 ~12:39 que el video largo **sí está publicado** en YouTube (https://www.youtube.com/watch?v=kRJQKBUc6dI, verificado en vivo: descripción con números v2, 30 meses, y el error C-27). Estado vigente: **PUBLICADO; la cabecera BORRADOR está desactualizada.** La copia en staging conserva la nota de la auditoría (BORRADOR vs publicado, pendiente confirmar) porque se hizo antes de la confirmación — léase con esta corrección: ya está confirmado, es PUBLICADO. El guion resumen no tiene confirmación de publicación.
3. **Actualización en redes NO hecha.** Elán ordenó 2026-11-09 ~12:39 actualizar TODO en redes con los números corregidos v3 (piezas publicadas 2026-11-07: YouTube largo, LinkedIn post largo, LinkedIn reporte PDF, LinkedIn post corto/reel, Facebook reel personal, Instagram reel @ing.zainos). No forma parte de este staging (solo archivos de texto, sin navegador/redes) y quedó pendiente de que termine la v3, para no corregir dos veces. Tampoco se tocó el espacio SNT (los 19 cambios C.1 requieren visto bueno de Elán).
4. **Huecos abiertos (§6 de la auditoría, siguen sin resolver):** inicio de la malversación sin fecha (Informe 016 bajo reserva); Roche-C mensual sin serie (PE solo en 6 anclas); Roche-S económico no fechable; Δ de ACO-A sin estimar (sin serie A(τ)); leapfrog / muro–b hipótesis no establecida; ASI = δH·α/F sin calcular; diversificación de ahorristas sin dato; caída dic 2025 sin explicación; 6 PDFs MEF faltantes; serie IPS mensual solo valores del documento; balances Ueno solo mar 2026; PE ago 2026 sin documentar; pregunta §9 de NOTAS sigue abierta; backcast v2 sin recalcular con mar 2026 (hecho ahora en v3 para R/b, no para la escalera completa); FGD total / nº depositantes, vencimientos CDA IPS, balance de exclusión 17 nov 2026, PE por banco receptor, valuación de embargos/megacuentas, cadena política, fechas Nota 019 / 31 fojas, 2 oferentes no nombrados, haberes de 32.000 jubilados, MEF oct/nov 2026, u = NULL, φ postulada no medida, R(t) 2023 no calculable, plan de adquisición Pasos 2–5 sin ejecutar.
5. **F7 no trasladado.** El comparativo global completo (17 casos, 4 marcadores, Basilea 25%/15%, 5 modelos de resolución, implicaciones para Paraguay, datos Ueno propios USD 850M de USD 2.800M = 30,4%, ~3 millones de clientes) tiene **cero** traslado a v2/v3. No se inventó ni se añadió: queda como GAP de traslado, fuera del alcance de esta corrección (la v3 corrige lo que ya estaba en v2, no incorpora F7).
6. **Procedencia Nota BCP/P N.° 019 + informe de 31 fojas (C-37): GAP.** Ese dato de v2 §12 no proviene de ninguna de las 7 fuentes verificadas (grep 0). Se conserva en v3 porque C.2 #7 lo exige para el podcast, con el GAP declarado en cada cabecera. Tampoco se resolvió: adjudicación Caja Fiscal 31 jul 2025, Asoban, descomposición del balance 2025, Caja y Equivalentes / bonos IPS (solo en NOTAS §11, por instrucción expresa de no mezclarlos en el CSV).
7. **C-18 periodo de intangibles: POR CONFIRMAR.** "Solo 2025" (v1) vs "2024–2025" (v2); no resoluble desde tabla ni auditoría; falta verificar contra EEFF.
8. **C-17 notificación 24 jul 2026 (φ paso 5):** v1 la citaba, v2 la omitió sin motivo registrado. No restablecida; GAP de traslado, pendiente de verificar contra parteaguas v2 §1.4. Las fechas 5 jun / 15 jun / 24 jul 2026 son NO VERIFICABLES contra v2.
9. **H-5 explicado pero no resuelto:** dic 2023 sigue sin PDF local aunque su fila figure como "MEF PDF"; resolverlo exige el archivo o corregir la fila en tabla/NOTAS, fuera del alcance de este modelo en staging.
10. **H-6 registrado, no corregido en NOTAS:** la clasificación de NOTAS §1 sigue sin corregirse en su archivo (reparto real 16+6+16=38). Detalle de archivo, no de número (R oct 2024 = 0,0780 verificado).
11. **Discrepancia mar 2026:** cuantificada en sus dos partes (solo Gs 557.038.013.754; USD exacto 235.381.762 → Gs 1.412.290.572.000 a FX 6.000; total en equivalentes Gs 1.969.328.585.754), pero sigue sin resolverse si el USD debe sumarse al Gs — GAP de definición, no error aritmético. v2 no la mencionaba.
12. **IPS 9,70%:** año corregido a 2026 por F5/F6, pero la fecha "30 oct" y "sin nuevas colocaciones en 2026" siguen NO VERIFICABLES en el corpus (el 9,70% coincide con sep 2026, 2,03/20,96 = 9,69%).
13. **Alcance de la recomputación:** no se recomputaron Roche-C/Roche-S, b IPS ni la aritmética ACO-A (no dependen de la tabla); se mantienen de v2 por verificación de la auditoría, no por recomputación propia en este pase.
14. **Datos NO VERIFICABLES en v2, conservados y marcados en los derivados** (no borrados ni afirmados como verificados): fechas 5/15 jun y 24 jul 2026, comparador CAME, cifra 850M/2.800M de depósitos totales, Caja Fiscal 31 jul 2025 al 12,35%. Queda además sin marcar en el guion v3 la frase "crisis política: renuncia y juicio político al presidente" (heredada del v2, tampoco verificable en v2) — a decisión del coordinador/padre.
15. **Lección registrada por Elán (2026-11-09 ~12:40):** "Ya me moleste debí auditar tu trabajo no confiarme" — publicar sin auditar antes fue el error; la verificación debe hacerse ANTES de publicar, no después. De ahora en adelante nada se publica sin que Elán lo audite primero. Esta v3 es la corrección; la publicación (GitHub, redes, espacio SNT) espera sus 2 filtros y su decisión.

## Para el push (agente padre)

- Staging total: **551.532 B + este README** — texto UTF-8, <16 MiB, sin binarios ni symlinks: apto para el conector GitHub (snapshot, solo texto, ≤16 MiB).
- Rama propuesta por Elán ("si el nombre que gustes esta bien"): `docs/ueno-v3-2026-11-09` (nombre no confirmado por Elán; él dijo que el nombre que se guste está bien).
- No subir `verificar_v3.py` como documento si no se quiere código en el repo — es herramienta de verificación, no documento Ueno; se incluye en staging como evidencia reproducible.
- Elán pasará esto por otros 2 filtros antes de integrar. No integrar a main desde aquí.
