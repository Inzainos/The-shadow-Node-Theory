# Backcast Roche — notas sobre el cuarto documento (v3 CORREGIDA)

**Fecha: 2026-11-09. Staging: `docs/ueno-2026-11-07/backcast-roche-notas-v3.md`**
**Base:** `backcast-roche-notas.md` (84 líneas, 2026-11-06/07) — estructura conservada; solo se
sustituyen los números v1 retirados y las listas pre-v2 por los valores vigentes.
**Fuentes:** `modelo-ueno-resultados-v2.md` + tabla maestra vigente
(`tabla-maestra-ueno-mef.csv`, 31 meses con R) + `REVISION_DOCUMENTOS_UENO.md` (2026-11-09,
§3.4, C-25, C-26, §8). No se tocó el original, no se subió nada a GitHub.

**Cambios v3 (resumen):**
- Serie v1 retirada sustituida por la vigente: nov 2024 R = 0,0963 (no 0,110); nov 2025 0,2643;
  feb 2026 0,2357; ago 2026 0,2161; sep 2026 0,2395; b ventana 0,383 extremo / 0,436 OLS.
- Ventana de inicio jul–dic 2024, mes focal dic 2024 (no jul–nov / 12 nov 2024).
- Roche-C (IPS) nov 2024 y Roche-R dic 2024: NO el mismo mes (la frase contraria queda retirada).
- φ paso 1: 65→60, 9 nov 2023 (con fecha, como en v2 §6).
- PDFs MEF faltantes: 6 (2023-01–05, 2024-08), no la lista pre-v2. Oct 2024 SÍ tiene PDF (R = 0,0780).
- Meseta dic 2025–sep 2026: R 0,2132–0,2662 en v3 (mar 2026, R = 0,2662, es el máximo de la
  meseta y supera nov 2025); b meseta −0,010 en v3 (n=10; +0,031 en v2, n=9), sin tendencia.
- Serie completa: b 0,823 (n=31) en v3; 0,819 (n=30) en v2.
- "92% del fondeo sin ir a préstamos" → 91,75% exacto (el 92% es redondeo de ABC).
- La verificación de Mole de 2026-11-06 queda actualizada: su ✓ a "nov 2024 R 0,110 (ancla)"
  era pre-corrección v2; el valor vigente es 0,0963.

Fuente: `fuentes del autor (no incluidas en el repo)backcast-roche-ueno_4_54ov.md`
Título: "BACKCAST — ¿Cuándo inició el fallo y cuándo entró Ueno al ratio de Roche?"
Fecha base: 2026-11-06/07; corrección v3: 2026-11-09. Base: tabla maestra (45 filas) + notas. Es la "aproximación aparte" que la v2 del parteaguas decía que era el paso siguiente.

## Respuesta corta
El fallo estructural no inició el 2 nov 2026. Inició en la ventana **jul – dic 2024**, punto focal **dic 2024**. Entrada a Roche-concentración: **nov 2024** (Roche-C base IPS = 106%) y entrada a Roche-relativa: **dic 2024** (R = 0,1021) — NO el mismo mes. El 2 nov 2026 es solo el reconocimiento legal de Roche-solvencia, no su cruce económico, que no se puede fechar con datos públicos.

## Las tres versiones operativas de "ratio de Roche" (no es término oficial BCP/MEF; metáfora de Elán del límite de Roche)
| Nombre | Definición | Umbral | Qué mide |
| --- | --- | --- | --- |
| Roche-C (concentración) | Fondos públicos en Ueno / Patrimonio efectivo de Ueno | > 1,0 | El hub custodia más dinero público que su capital para absorber pérdidas |
| Roche-R (relativa) | R(t) = Ueno / resto del sistema | > 0,10 | Ueno = 10% del resto (9,09% del total). Primer umbral observable en la tabla |
| Roche-S (solvencia) | Solvencia reportada / mínimo legal (12%) | < 0,50 | Gatillo legal Ley 2334/03 art. 13 inc. b. BCP 2 nov 2026: 5,56/12 = 0,463 |

No es el teorema de Rouché, no es la garantía de depósitos, no es prueba de malversación. Cruzar Roche-C o Roche-R es ruptura estructural, no delito. La malversación es hipótesis penal aparte y su fecha de inicio NO se puede deducir de R(t).

## Backcast (hacia atrás desde el 2 nov 2026)
0. Trigger 2 nov 2026: reconocimiento, no inicio. Solvencia reportada >12% hasta sep (15,01% mar, 14,5% jun, 13,85% sep); el cruce económico real está oculto por rezago contable.
1. Meseta dic 2025–sep 2026: R 0,2132–0,2662 (v3, con mar 2026 R = 0,2662, máximo de la meseta). IPS 9,70% de su cartera el 30 oct 2026, sin nuevas colocaciones (tope 10%). Ya más allá de Roche, sin retorno. b meseta −0,010 en v3 (n=10; +0,031 en v2, n=9), sin tendencia medible en ambos casos.
2. Segunda ruptura jun–jul 2025: R cruza 0,20 entre jun (0,1706) y jul (0,2079); interpolación ≈ 24 jun 2025.
3. Confirmación dic 2024–mar 2025: depósitos +Gs 1,755,304M (+17%) vs crédito neto +Gs 144,737M (+2%); 91,75% del fondeo sin ir a préstamos (ABC redondea a 92%). Comportamiento post-Roche.
4. Entrada a Roche nov–dic 2024: Roche-C (base IPS) nov 2024, 1,7 / patrimonio efectivo 1,6 = 106%; Roche-R dic 2024, R = 0,1021 (nov 2024 R = 0,0963, por debajo del umbral); cierre 2024 IPS 1,766/1,56 = 113%; sector público dic 2024: 1,747/1,56 = 112%; base fondos totales dic 2024: 1,08. Los dos indicadores NO cruzan el mismo mes: Roche-C en nov 2024, Roche-R en dic 2024 (corrección clave de v2; la frase v1 "los dos indicadores cruzan 1,0 el mismo mes" queda RETIRADA).
5. Acto institucional 12 nov 2024: IPS elimina límite de patrimonio efectivo y baja calificación A-Py fuerte → A genérica (Res. 093-046/2024). El phi que permite el cruce.
6. Primera ruptura jul 2024: R salta 0,0338 → 0,0610 (+80% en un mes). Ueno total +78,5% (USD 104,4M → 186,4M). Fusión Visión efectiva 1 jul 2024; facilidades G. 5,1 billones autorizadas 27 may 2024. Antes R plano (0,028–0,035 feb–jun); después nunca vuelve.
7. Pre-condición 9 nov 2023: IPS baja puntaje 65 → 60. Prepara el terreno, R no se mueve. No es inicio.

## Tres fechas, no una
- A. Inicio del fallo estructural: jul–dic 2024; mes focal dic 2024 (Roche-R 0,1021, Roche-C fondos totales 1,08, inicio de la captura masiva en CDA); inicio más temprano jul 2024 (el salto). No se precisa un día: los datos son mensuales. Oct 2024 SÍ tiene PDF (R = 0,0780); la ventana de cruce nov–dic 2024 queda cerrada al mes (sep 0,0777 → oct 0,0780 → nov 0,0963 → dic 0,1021).
- B. Entrada a Roche-concentración: nov 2024 (Roche-C 106% nov, 113% cierre 2024; Roche-R 0,1021 en dic 2024). Todo lo posterior es permanencia más allá de Roche. Roche-C y Roche-R NO entran el mismo mes.
- C. Cruce de Roche-solvencia: reconocido 2 nov 2026 (0,463 < 0,50); económico no fechable con datos públicos (sostenido por intangibles Gs 761,444M, Derechos Fiduciarios Gs 2,105,743M, Participaciones +8,000% en 2025 — saldos de cierre 2025, sin fecha mensual).

## Qué NO concluye
- No concluye que la malversación empezó en nov–dic 2024 (concluye que la ruptura estructural empezó ahí). Puede ser anterior, simultánea o posterior; sin el Informe 016 no se fecha.
- No concluye que el 2 nov 2026 sea el cruce de Roche (es el reconocimiento legal de Roche-S).
- No usa interpolación para fechar (huecos vacíos); solo para decir "entre jun y jul 2025 cruzó 0,20".
- No mezcla bases: Roche-C usa IPS y total público por separado, ambos > 1 en nov–dic 2024.

## Tabla Roche-C
Nov 2024 IPS 1,7/1,6 = 1,06; cierre 2024 IPS 1,766/1,56 = 1,13; dic 2024 sector público 1,747/1,56 = 1,12; 31 oct 2025 IPS 2,1/1,8 = 1,17; cierre 2025 IPS 2,24/2,20 = 1,02. Base fondos totales (nueva en v2): dic 2024 1,08; dic 2025 1,89; mar 2026 ≈2,08 (PE abr 2026 como proxy, aproximado).

## Pendiente para fechar la malversación
- Informe BCP/P N.° 016 (precintado, Senado): única vía. Salvedad v2 §12: existe la Nota BCP/P N.° 019 (denuncia a Fiscalía con informe de ~200 fojas) y un informe sellado de 31 fojas al Senado que NO precisa la fecha ni el monto total del exceso — así que ni siquiera es seguro que el 016 lo feche. GAP C-37: la procedencia de la Nota 019 / informe de 31 fojas no está en las 7 fuentes verificadas.
- PDFs MEF faltantes (v3, tabla vigente): 6 meses — 2023-01, 02, 03, 04, 05 y 2024-08. [La lista pre-v2 del original (oct 2024, dic 2024–mar 2025, ene/mar 2026) queda RETIRADA: esos meses ya tienen PDF en v2; mar 2026 tiene PDF en la tabla vigente.] GAP H-5: el conteo de PDFs en NOTAS es inconsistente (38 archivos en disco, 39 filas marcadas MEF PDF; dic 2023 sin archivo local).
- Serie mensual de patrimonio efectivo (no solo cierres).

## Verificación de Mole (actualizada v3, 2026-11-09)
Contra tabla-maestra-ueno-mef.csv (vigente, 31 meses con R): jun 2024 R 0,0338 ✓; jul 2024 R 0,0610 ✓ (+80,5%); sep 2024 R 0,0777 ✓; oct 2024 R 0,0780 ✓ (SÍ tiene PDF); nov 2024 R 0,0963 ✓ (corregido; el 0,110 quedó RETIRADO); dic 2024 R 0,1021 ✓; mar 2026 R 0,2662 ✓ (nuevo, máximo de la meseta); jun 2025 0,1706 ✓; jul 2025 0,2079 ✓ (interpolación propia ≈ 25 jun, documento ≈ 24 jun, dentro de redondeo); Roche-S 5,56/12 = 0,463 ✓.
[La verificación original de 2026-11-06 marcaba "nov 2024 R 0,110 ✓ (ancla)": ese ✓ era pre-corrección v2 y queda sustituido por el 0,0963 de arriba.]

## Qué cambia en el trabajo en curso
- **Corrige el marco anterior:** el evento del 2 nov NO fue "el cruce del ratio de Roche" — fue el reconocimiento legal de Roche-S. El cruce económico de Roche-C/Roche-R fue nov–dic 2024 (Roche-C nov, Roche-R dic, un mes aparte). Y la malversación NO se fecha con R(t): el backcast fecha la ruptura estructural, no el delito. La frase de Elán "el ratio tuvo que haber entrado desde que inició la malversación" queda como coherente pero no fechable sin el Informe 016.
- **Responde la pregunta abierta del ratio:** no es un solo ratio — son tres, y el de solvencia era solo uno de ellos.
- **Regrabación final (al último):** debe usar las tres definiciones Roche-C/R/S, la ventana jul–dic 2024 con focal dic 2024, el salto de jul 2024 (fusión Visión 1 jul, facilidades G. 5,1 billones 27 may), el cruce 0,20 ≈ 24 jun 2025, y la distinción reconocimiento vs cruce económico. La línea "el 2 nov fue el cruce de Roche" de la v1 queda sustituida.
- **Inyección a los modelos:** Roche-C, Roche-R y Roche-S son ahora fórmulas operativas a calcular desde la tabla (Roche-C necesita la serie mensual de patrimonio efectivo, hoy solo cierres).

---

## El muro de los 5 eventos como instrumento del ratio de Roche (decisión de Elán, 2026-11-06 noche)

Elán: el Muro de los 5 eventos entra como instrumento/herramienta del ratio de Roche.

Localizado en el espacio SNT, panel ASI / HackerEarth ("DESDE HACKEREARTH — Soberanía Atómica ASI — ASI = δH · α / F"):
> "5 Event Wall — El Muro de los 5 eventos. Umbral crítico en los dominios digital y genómico: los usuarios con menos de 5 tipos de evento distintos tienen >90% de probabilidad de churn. En TCGA, solo 2–5% de pacientes presentan ≥5 eventos hub simultáneos. Es el equivalente a la diversidad funcional mínima para escapar de la satelización — por debajo de ese umbral, el nodo queda atrapado en la órbita del hub..."

Lectura: las bandas Roche dicen CUÁNDO se rompió el sistema (Roche-C nov 2024, Roche-R dic 2024, Roche-S reconocido 2 nov 2026); el muro dice QUIÉN puede escapar: la unidad atómica necesita ≥5 tipos de evento distintos (diversidad funcional mínima); por debajo, queda atrapada en la órbita del hub. En Ueno: jubilados cautivos con 1 banco, ahorristas con fondos congelados, OEEs con 1 canal — todos por debajo del muro.

ADVERTENCIA HONESTA: el 5 se calibró en digital (HackerEarth, churn) y genómico (TCGA), NO en finanzas. Para usarlo en Ueno hay que definir qué cuenta como "tipo de evento" en finanzas. Candidatos: bancos distintos donde la unidad tiene fondos; instrumentos distintos (CDA, vista, bonos); contrapartes distintas. Sin esa definición, el muro es analogía, no medición. Pregunta abierta a Elán.

BONUS: el ASI del repo también es "Soberanía Atómica" (espacio: "Soberanía atómica desde comportamiento (HackerEarth); umbral recalibrado de 0.5 a 0.167"). La definición de ASI de la v2 del parteaguas COINCIDE con la del repo — la bandera de colisión queda cerrada; la v1 ("seguro sistémico de absorción") era la definición errónea.

---

## CORRECCIÓN — leapfrog YA existe en la SNT desde v1 (Elán, 2026-11-06 noche)

Elán advirtió: el salto de rana (leapfrog) ya está desde la primera versión de la SNT; revisar antes de escribir algo nuevo para no torcerse.

Verificado en el repo (README, Módulo 0) y en el espacio:
- **Leapfrog = b < 0 (Convergencia / leapfrog)**, tabla de b del Módulo 0.
- **Espacio:** los candidatos al leapfrog "pueden saltar directo al Nivel Exógeno sin pasar por los intermedios" (contexto EFIPEM/México).
- **Radio de Roche YA está en el repo** (Módulo 1 ACO-A): "Entrada al radio de Roche → colapso abrupto, Δ negativo, A(τ) decreciente".
- **Muro de 5 eventos YA está en el repo:** "pico de churn en ~5 eventos; umbral de activación en primera sesión" y "diversidad funcional mínima para escapar de la satelización".

Consecuencia: NO escribir "5 eventos positivos = leapfrog" como definición — eso crearía una segunda definición incompatible. El five-event-wall-by-phi es APLICACIÓN al caso Ueno y propuesta de Elán (los 5 pasos de phi = 5 eventos negativos observados; lectura bipolar como propuesta). Pregunta abierta: cómo se relacionan los 5 eventos positivos con la definición vigente de leapfrog (b < 0 y salto al Nivel Exógeno). Posible reconciliación (hipótesis de Mole, NO establecida): los eventos positivos son acciones que bajan R(t) (b < 0) y el salto al Nivel Exógeno es salir de la órbita del hub — pero eso hay que confirmarlo con Elán, no escribirlo como hecho. El constructor del espacio ya fue avisado (artifact.send_input, 2026-11-06 ~20:38).
