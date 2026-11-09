# Verificación v3 del modelo Ueno — salida de `verificar_v3.py`

**Fecha:** 2026-11-09. **Script:** `verificar_v3.py` (Python stdlib, sin dependencias externas), en este mismo directorio de staging. **Fuente:** `docs/ueno-2026-11-07/tabla-maestra-ueno-mef.csv` (tabla vigente, 45 filas, 07 nov 10:48). **Método:** R(t) = `ueno_total_usd_equiv / (total_sistema_usd_equiv − ueno_total_usd_equiv)`, con verificación cruzada desde los componentes crudos (USD×6,000 + Gs); OLS log-log (log R = log a + b log t) por ventana, con origen de t declarado; (c′) en calendario y en secuencial.

## Comparación: lo publicado en v3 vs lo recomputado

| Magnitud | Publicado en v3 | Recomputado por el script | Estado |
|---|---|---|---|
| Meses con R | 31 | 31 | ✓ reproduce |
| R mar 2026 | 0.2662 | 0.266246 → 0.2662 | ✓ reproduce |
| R nov 2025 (comparación) | 0.2643 | 0.264286 → 0.2643; mar 2026 > nov 2025: True | ✓ reproduce |
| Rango meseta dic25–sep26 | 0.2132–0.2662 | min 0.2132, max 0.2662 | ✓ reproduce |
| Diferencia máx. R recomputada vs R_csv | 0.0000 a 4 decimales | 0.000050 en valor absoluto (puro redondeo de la columna R_t a 4 decimales), tanto desde equivalentes como desde crudos | ✓ reproduce |
| (c) meseta, origen dic24 | b = −0.0101, a = 0.2397, R² = 0.0007, n=10 | b = −0.0101, a = 0.2397, R² = 0.0007, n=10, t=13..22 | ✓ reproduce |
| (c) meseta, origen nov24 (sensibilidad) | b = −0.0114, a = 0.2407, R² = 0.0008 | b = −0.0114, a = 0.2407, R² = 0.0008 | ✓ reproduce |
| (c′) meseta, origen local dic25, CALENDARIO | b = +0.0065, a = 0.2306, R² = 0.0048, n=10 | b = +0.0065, a = 0.2306, R² = 0.0048, n=10, t=1..10 | ✓ reproduce |
| (c′) meseta, origen local dic25, SECUENCIAL | +0.0065 (coincide con calendario en v3) | b = +0.0065, R² = 0.0048, t=1..10; calendario == secuencial: True | ✓ reproduce (sin huecos en dic25–sep26) |
| (e) completa, origen feb24 calendario | b = 0.8234, a = 0.0157, R² = 0.9108, n=31 | b = 0.8234, a = 0.0157, R² = 0.9108, n=31, t máx 32 | ✓ reproduce |
| Controles H-1 (c′) v2 n=9 | calendario +0.0104 / R² 0.0226; secuencial +0.0086 / R² 0.0132 (publicado en v2) | calendario b=+0.0104 R²=0.0226; secuencial b=+0.0086 R²=0.0132 | ✓ reproduce los valores de la auditoría §2.2 |
| Controles H-1 (c′) v1 n=8 | calendario −0.0046 / R² 0.005; secuencial −0.0120 / R² 0.0296 (publicado en v1) | calendario b=−0.0046 R²=0.0050; secuencial b=−0.0120 R²=0.0296 | ✓ reproduce los valores de la auditoría §2.2 |
| Discrepancia mar 2026 solo Gs | Gs 557,038,013,754 | 3,721,013,013,754 − 3,163,975,000,000 = 557,038,013,754 | ✓ reproduce |
| USD mar 2026 sin conciliar a FX 6,000 | +Gs 1,412,290,572,000 | USD exacto CSV fila 2026-03: 235,381,762 × 6,000 = 1,412,290,572,000 | ✓ reproduce (la cifra "1.412.290M" de la auditoría §2.8 usa el USD exacto, no 235,000,000 redondeados) |
| Discrepancia total en equivalentes | Gs 1,969,328,585,754 | 557,038,013,754 + 1,412,290,572,000 = 1,969,328,585,754 | ✓ reproduce |
| Filas "MEF PDF" / "sin PDF" | 39 / 6 | 39 / 6 | ✓ reproduce |

**Ningún número publicado en v3 dejó de reproducir.** No hubo que marcar ningún GAP por no-reproducción en v3. Los GAP que v3 marca (discrepancia mar 2026 como GAP de definición, periodo de intangibles por confirmar, notificación 24 jul 2026, H-5/H-6) son GAP de documentación, no de cálculo: vienen de la auditoría, no de un fallo de esta verificación.

## Salida completa del script

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

## Notas de verificación

- La "diferencia máxima 0.000050" no es un error: es el redondeo de la columna `R_t` del CSV a 4 decimales (p. ej. 2024-02: recomputada 0.028361 vs CSV 0.0284). A 4 decimales la diferencia es 0.0000 en las 31 filas, como dice la auditoría §2.1 ("las 31 filas con R reproducen el CSV exacto (diferencia 0,0000 en todas)").
- La (e) completa usa t calendario con hueco en ago 2024 (t salta de 6 a 8) y t máx 32 para 31 meses: es el calendario declarado, no la numeración secuencial.
- La (c′) v3 es el caso en que H-1 se cierra por los datos y por el método a la vez: con mar 2026 presente la ventana dic25–sep26 no tiene huecos, así que t calendario = t secuencial = 1..10 y ambos métodos dan +0.0065. Los controles v1/v2 (con huecos) reproducen exactamente la discrepancia que la auditoría documenta, lo que valida que el script distingue ambos métodos.
- Lo que este script NO verifica (fuera de su alcance, igual que en v2): los valores que no dependen de la tabla — Roche-C/Roche-S (insumos del parteaguas y anclas PE de NOTAS §12), b IPS (3 puntos anuales del documento), y toda la aritmética ACO-A (FGD, anticipo, USD 146M, salvadoras, fondeo, embargo). Esos valores se mantienen de v2 porque la auditoría los verificó (§2.4–§2.7, §5.3) y mar 2026 no los mueve; no se recomputaron aquí.

## Lo que NO se pudo verificar / corregir

1. **Periodo del incremento de intangibles (C-18):** v1 dice "solo en 2025", v2 dice "2024–2025". No hay forma de resolverlo desde la tabla ni desde la auditoría: hace falta verificarlo contra los EEFF 2024/2025. En v3 queda marcado POR CONFIRMAR; no se eligió un periodo.
2. **Notificación del 24 jul 2026 en φ paso 5 (C-17):** v1 la citaba, v2 la omitió sin motivo registrado. No se restableció en la tabla de φ: queda como GAP de traslado, pendiente de verificar contra parteaguas v2 §1.4. Las fechas 5 jun / 15 jun / 24 jul 2026 son NO VERIFICABLES contra v2 (auditoría §3.5).
3. **H-5 (conteo de PDFs):** se explica en v3 pero no se resuelve: dic 2023 sigue sin PDF local aunque su fila figure como "MEF PDF". Resolverlo requiere el archivo o una corrección de la fila en la tabla/NOTAS, fuera del alcance de este modelo en staging.
4. **H-6 (clasificación de oct 2024):** se registra en v3 (reparto real 16+6+16=38); la clasificación de NOTAS §1 sigue sin corregirse en su archivo. Detalle de archivo, no de número (R = 0.0780 verificado).
5. **Discrepancia mar 2026:** se registra y se cuantifica en sus dos partes, pero sigue sin resolverse si el USD debe sumarse al Gs: es un GAP de definición, no un error aritmético, y no hay documento en el corpus que lo resuelva.
6. **Procedencia de la Nota BCP/P N.° 019 e informe de 31 fojas (C-37):** GAP de la auditoría — ese dato de v2 §12 no proviene de ninguna de las 7 fuentes verificadas. No se pudo verificar ni corregir en este pase.
7. **Año IPS 9.70% (C-30):** corregido a 30 oct 2026 en v3 según F5 `:47`/`:262` y F6 `:28` citados por la auditoría §3.7; la fecha "30 oct" y la afirmación de "sin nuevas colocaciones en 2026" siguen siendo NO VERIFICABLES dentro del corpus (auditoría §2.10: el 9,70% coincide con sep 2026, 2,03/20,96 = 9,69%).
8. **Alcance del script:** no se recomputaron Roche-C/Roche-S, b IPS ni la aritmética ACO-A (ver "Notas de verificación"); se mantienen de v2 por verificación de la auditoría, no por recomputación propia en este pase.
