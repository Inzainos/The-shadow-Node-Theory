# VERIFICACION_V31 — Corrección v3.1 de Ueno (2026-11-09)

**Fecha:** 2026-11-09. **Base:** staging `el staging v3.1 (docs/ueno-2026-11-07/)` (misma estructura `docs/ueno-2026-11-07/`).
**Método:** Regla 0 — verificar contra documentación, no contra memoria. No se subió nada a GitHub; el push lo hace el agente padre.

## (a) verificar_v3.py corriendo desde /tmp

Comando: `cd /tmp && python3 <staging>/docs/ueno-2026-11-07/verificar_v3.py` — exit 0. El script lee ahora `Path(__file__).parent / "tabla-maestra-ueno-mef.csv"` (el CSV junto al script, en la misma carpeta del repo).
Resumen de la salida (salida completa en este archivo, abajo):
- R mar 2026 = 0.2662; R nov 2025 = 0.2643 (mar 2026 supera nov 2025).
- Meseta (c) origen dic24: b = -0.0101, a = 0.2397, R² = 0.0007, n = 10.
- (c') calendario = secuencial = +0.0065, R² = 0.0048, n = 10; controles H-1 reproducen v2 (+0.0104 / +0.0086) y v1 (-0.0046 / -0.0120).
- Serie completa (e): b = 0.8234, a = 0.0157, R² = 0.9108, n = 31; diferencia máxima R recomputada vs CSV = 0.000050 (0.0000 a 4 decimales, redondeo).
- Discrepancia mar 2026: solo Gs 557,038,013,754; USD 235,381,762 → Gs 1,412,290,572,000 a FX 6,000; total en equivalentes Gs 1,969,328,585,754.

```
filas totales (sin cabecera): 45
filas marcadas 'MEF PDF': 39
filas marcadas 'sin PDF': 6

meses con R_t en CSV: 31
diferencia maxima R_equiv vs R_csv: 0.000050
diferencia maxima R_crudos vs R_csv: 0.000050
  2024-02  csv=0.0284  equiv=0.028361  crudos=0.028361
  2024-03  csv=0.0319  equiv=0.031919  crudos=0.031919
  2024-04  csv=0.0332  equiv=0.033161  crudos=0.033161
  2024-05  csv=0.0346  equiv=0.034559  crudos=0.034559
  2024-06  csv=0.0338  equiv=0.033820  crudos=0.033820
  2024-07  csv=0.0610  equiv=0.060984  crudos=0.060984
  2024-09  csv=0.0777  equiv=0.077694  crudos=0.077694
  2024-10  csv=0.0780  equiv=0.077995  crudos=0.077995
  2024-11  csv=0.0963  equiv=0.096350  crudos=0.096350
  2024-12  csv=0.1021  equiv=0.102150  crudos=0.102150
  2025-01  csv=0.1094  equiv=0.109444  crudos=0.109444
  2025-02  csv=0.1253  equiv=0.125251  crudos=0.125251
  2025-03  csv=0.1315  equiv=0.131471  crudos=0.131471
  2025-04  csv=0.1396  equiv=0.139592  crudos=0.139592
  2025-05  csv=0.1628  equiv=0.162759  crudos=0.162759
  2025-06  csv=0.1706  equiv=0.170594  crudos=0.170594
  2025-07  csv=0.2079  equiv=0.207867  crudos=0.207867
  2025-08  csv=0.2457  equiv=0.245692  crudos=0.245692
  2025-09  csv=0.2467  equiv=0.246711  crudos=0.246711
  2025-10  csv=0.2670  equiv=0.267024  crudos=0.267024
  2025-11  csv=0.2643  equiv=0.264286  crudos=0.264286
  2025-12  csv=0.2280  equiv=0.227975  crudos=0.227975
  2026-01  csv=0.2132  equiv=0.213220  crudos=0.213220
  2026-02  csv=0.2357  equiv=0.235652  crudos=0.235652
  2026-03  csv=0.2662  equiv=0.266246  crudos=0.266246
  2026-04  csv=0.2543  equiv=0.254273  crudos=0.254273
  2026-05  csv=0.2254  equiv=0.225399  crudos=0.225399
  2026-06  csv=0.2246  equiv=0.224596  crudos=0.224596
  2026-07  csv=0.2306  equiv=0.230627  crudos=0.230627
  2026-08  csv=0.2161  equiv=0.216092  crudos=0.216092
  2026-09  csv=0.2395  equiv=0.239512  crudos=0.239512

R mar 2026: 0.2662 (csv 0.2662)
R nov 2025: 0.2643  -> mar 2026 supera nov 2025: True
R dic 2024 (cruce Roche-R): 0.1021; R nov 2024: 0.0963

meseta dic25-sep26: n=10 meses: ['2025-12', '2026-01', '2026-02', '2026-03', '2026-04', '2026-05', '2026-06', '2026-07', '2026-08', '2026-09']
rango meseta: min=0.2132 max=0.2662
(c) meseta origen dic24 calendario: b=-0.0101 a=0.2397 R2=0.0007 n=10 t=[13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
(c) meseta origen nov24 calendario (sensibilidad): b=-0.0114 a=0.2407 R2=0.0008
(c') v3 meseta origen local dic25 CALENDARIO: b=0.0065 a=0.2306 R2=0.0048 n=10 t=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
(c') v3 meseta origen local dic25 SECUENCIAL: b=0.0065 a=0.2306 R2=0.0048 n=10 t=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
(c') v3 calendario == secuencial: True (sin huecos en dic25-sep26 con mar 2026 presente)
(c') CONTROL v2 n=9 calendario: b=0.0104 R2=0.0226 (auditoria: +0.0104 / R2 0.0226)
(c') CONTROL v2 n=9 secuencial: b=0.0086 R2=0.0132 (auditoria: +0.0086 / R2 0.0132; valor publicado en v2)
(c') CONTROL v1 n=8 calendario: b=-0.0046 R2=0.0050 (auditoria: -0.0046 / R2 0.005)
(c') CONTROL v1 n=8 secuencial: b=-0.0120 R2=0.0296 (auditoria: -0.0120 / R2 0.0296; valor publicado en v1)

(e) completa origen feb24 calendario: b=0.8234 a=0.0157 R2=0.9108 n=31 t_max=32
(e) t calendario serie completa: [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]

discrepancia mar 2026 solo Gs: 557,038,013,754 Gs
USD mar 2026 exacto (CSV fila 2026-03): 235,381,762 USD
USD mar 2026 sin conciliar a FX 6000: 1,412,290,572,000 Gs
discrepancia total en equivalentes (Gs + USD*6000): 1,969,328,585,754 Gs

=== RESUMEN v3 ===
R_mar2026=0.2662
b_meseta_c_origen_dic24=-0.0101 R2=0.0007 n=10
b_meseta_cprima_calendario=0.0065 R2=0.0048 n=10
b_meseta_cprima_secuencial=0.0065 R2=0.0048 n=10
b_completa_e=0.8234 a=0.0157 R2=0.9108 n=31
max_diff_R=0.000050
```

## (b) grep de la frase retirada en el staging

Ocurrencias en los documentos: **1** (no 0), y es la esperada. (Los dos archivos de registro del cambio, `CAMBIOS_V31.md` y este `VERIFICACION_V31.md`, citan la frase entre comillas como constancia de lo retirado; no son documentos del caso.)
- `REVISION_DOCUMENTOS_UENO.md:41` (§1.3, tabla de inventario): cita histórica de lo que decía el archivo original de rastro al auditarse. El cuerpo de la auditoría no se reescribió, por orden expresa de la tarea. En todos los documentos v3.1 la frase está retirada (rastro: línea eliminada + nota v3.1; README: sin ocurrencias).

## (c) Nombres de personas físicas restantes, con su atribución

Todos son la lista del embargo del 3 nov 2026 (empresas + personas + cuatro directores). Ninguno aparece como afirmación suelta del locutor:

- `modelo-ueno-resultados-v3.md`: lista del embargo, con atribución a la orden de embargo del 3 nov 2026 (y, en los guiones, a la denuncia del MEF del 5 nov 2026).
- `video-largo-ueno/guion-video-largo.txt`: lista del embargo, con atribución a la orden de embargo del 3 nov 2026 (y, en los guiones, a la denuncia del MEF del 5 nov 2026).
- `modelo-ueno-resultados-v2.md`: lista del embargo, con atribución a la orden de embargo del 3 nov 2026 (y, en los guiones, a la denuncia del MEF del 5 nov 2026).
- `forecast-ueno-2026-11-06.md`: lista del embargo, con atribución a la orden de embargo del 3 nov 2026 (y, en los guiones, a la denuncia del MEF del 5 nov 2026).
- `podcast/script-v3.txt`: lista del embargo, con atribución a la orden de embargo del 3 nov 2026 (y, en los guiones, a la denuncia del MEF del 5 nov 2026).
- `parteaguas-notas-v3.md`: lista del embargo, con atribución a la orden de embargo del 3 nov 2026 (y, en los guiones, a la denuncia del MEF del 5 nov 2026).
- `rastro-del-dinero-ueno-v3.md`: lista del embargo, con atribución a la orden de embargo del 3 nov 2026 (y, en los guiones, a la denuncia del MEF del 5 nov 2026).

Detalle por archivo:
- `modelo-ueno-resultados-v3.md:331` (§13, escalera del backcast): fila del embargo, 3 nov 2026.
- `modelo-ueno-resultados-v2.md:271` (registro v1→v2, sin cambios): misma fila del embargo.
- `forecast-ueno-2026-11-06.md:170`: sección del embargo, Juzgado en lo Civil y Comercial del Octavo Turno, a solicitud del BCP.
- `parteaguas-notas-v3.md:42`: viñeta del embargo, 3 nov 2026.
- `rastro-del-dinero-ueno-v3.md:61` (§4): con atribución explícita añadida en v3.1 («Según la orden de embargo del 3 nov 2026, contra…»).
- `podcast/script-v3.txt:74`: con atribución explícita añadida en v3.1 («Según la orden de embargo del tres de noviembre… Son los nombres que aparecen en esa orden y en la denuncia del MEF del cinco de noviembre»).
- `video-largo-ueno/guion-video-largo.txt:68`: con atribución explícita añadida en v3.1 (misma fórmula).
- `video-resumen-ueno/guion-video.txt`: sin nombres de personas físicas (verificado).
- Traspaso Mowi / Grupo Hendy / Grupo M (podcast, turno de las tres pruebas): atribuido al Informe de la Intendencia de Supervisión del 8 jun 2026. USD 146M (podcast): atribuido al informe de supervisión del 8 jun 2026, recogido en el parteaguas.
- Salvaguarda hablable («La malversación es presunta, denunciada e investigada; no hay sentencia. El motivo oficial fue la insolvencia.»): al inicio de los tres guiones (podcast L26, video largo C1a, video resumen intro).

## (d) grep de rutas locales

> Nota: en este archivo la ruta local se escribe como `[ruta-local]` para no reintroducirla; el conteo 0 es sobre los documentos del staging, sin contar este archivo de verificación ni `CAMBIOS_V31.md`, que citan las rutas antiguas como registro del cambio.

- `[ruta-local]/` en el staging: **0 ocurrencias**.
- `[carpeta-local-original]` (ruta local original): **0 ocurrencias** (sustituida por `docs/ueno-2026-11-07/` o por la nota `(no incluido en el repo)`; detalle en `CAMBIOS_V31.md` §2).

## (e) Integridad del staging

- Total: 594,640 B (34 archivos, incluidos los 2 nuevos `CAMBIOS_V31.md` y `VERIFICACION_V31.md`), todo texto UTF-8/ASCII, 0 binarios, 0 symlinks, < 16 MiB. Apto para el conector GitHub (snapshot, solo texto).
- No se tocó `main`, ni el espacio SNT, ni los originales en el equipo local. No se creó ningún chat. No se subió nada a GitHub.

## (f) Pendientes fuera de esta v3.1 (no resueltos aquí)

- Los guiones de video largo y resumen conservan los números v2 del guion original (30 meses, meseta +0.031, +511,865M): su actualización a v3 queda pendiente.
- Audio del podcast sin regrabar (números v1). Regrabación, decisión de Elán.
- Periodo de intangibles (C-18) sigue POR CONFIRMAR; procedencia Nota 019 / 31 fojas (C-37) sigue GAP; resto de huecos §6 de la auditoría, sin cambio.
