# ADENDA 5 — Pares delistados y sello de la descarga prospectiva

**Fecha:** 2026-10-27 · **Se añade a:** preregistro prospectivo ACO-A y
ADENDA 1–4. **Criterio posterior al sello externo 10.5281/zenodo.23678033:**
el DOI 23678033 contiene el estado v2.7.3 y las ADENDA 1–4, pero precede
esta adenda. Esta regla nueva se identifica como posterior a ese sello y
debe quedar archivada en un release/DOI nuevo antes de evaluar la ventana
2026-09-30 → 2027-09-30.

## Cohorte y delistados

- La cohorte v2 queda congelada: los 491 pares vivos al corte
  2026-09-30, de los que 440 son candidatos (`dd < 99%`). No se añaden
  pares listados después del corte ni se retiran candidatos por su
  supervivencia posterior.
- Un par de la cohorte que Binance retire durante la ventana conserva sus
  cierres reales hasta la última fecha disponible. No se imputan precios
  posteriores y el delisting, por sí solo, **no es un colapso**.
- El criterio de colapso existente requiere observación hasta el fin de
  ventana: mínimo bajo el 1% del ATH congelado y cierre final aún bajo ese
  umbral. Si el seguimiento termina antes del 2027-09-30, el caso queda
  **censurado a la derecha**; no se cuenta como colapso ni como superviviente.
  Permanece en el denominador fijo de 440 candidatos y se informa el número
  censurado. Un hueco de descarga también impide clasificar ese caso; si la
  descarga global no llega al fin de ventana, la evaluación debe detenerse
  como incompleta.
- P2/P3 se calculan solo sobre colapsos observados y maduros, según las
  recetas ya selladas. Los casos censurados no entran como ceros ni como
  no-colapsos.

## Congelamiento y hash de los datos

Antes de ejecutar `evaluar_prospectiva.py` se congela la descarga utilizada
para el corte 2026-09-30 → 2027-09-30. El manifiesto versionado debe registrar:

1. Por cada archivo bruto de Binance usado: URL exacta, fecha/hora UTC de
   descarga, bytes y SHA-256 del archivo sin modificar.
2. Para la tabla combinada de cierres entregada al evaluador: ruta, bytes,
   SHA-256 del archivo exacto y última fecha disponible.
3. La fuente oficial usada para identificar delistings y su fecha, junto
   con URL, fecha/hora UTC, bytes y SHA-256. No inferir un delisting solo
   de un archivo ausente; las interrupciones de cobertura se reportan como
   censura/dato incompleto, nunca como evento.

El manifiesto y los datos exactos se committean y se publican en el release
de sellado **antes** de correr el evaluador. La evaluación cita ese commit,
release y hash de la tabla de entrada. El hash real de la descarga futura no
se conoce hoy; se añadirá al manifiesto cuando exista la ventana, pero antes
de calcular resultados. Esta adenda metodológica es posterior al DOI
23678033; el nuevo release/DOI debe dejar esa cronología explícita.

## Alcance sin cambios

Esta adenda no altera la cohorte, la ventana, la definición de colapso, ni
los criterios P1a/P2/P3 de las ADENDA 2–4. La fracción de colapsos sigue
siendo descriptiva; P1b permanece retirada.
