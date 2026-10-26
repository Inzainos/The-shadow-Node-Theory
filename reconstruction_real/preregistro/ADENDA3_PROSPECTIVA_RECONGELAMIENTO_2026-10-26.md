# ADENDA 3 — Re-congelamiento de la cohorte al corte 2026-09-30

**Fecha:** 2026-10-26 (cierre) · **Responde a:** `PENDIENTES_SNT.md`
(punto "La cohorte sigue congelada al 2026-08-31" — observación del
operador, aceptada).

---

## El problema

La ADENDA 2 re-ancló la **ventana** (2026-10-26 → 2027-10-26) pero dejó
el **CSV de la cohorte** congelado al corte de datos 2026-08-31: los
pares que colapsaron en las semanas intermedias seguían contados como
candidatos vivos.

## La corrección

- Se re-descargó la fuente con el script versionado
  (`descargar_binance_klines.py`): 685 pares, 794 721 filas, SHA-256
  `dc9c6cd9…23907`, **última fecha 2026-09-30** (Binance Vision publica
  en zips mensuales; octubre no existe todavía — llega en noviembre).
- **Cohorte v2 versionada**:
  `data/cohorte_congelada_cripto_2026-10-26_v2.csv` — congelada al
  corte **2026-09-30**: 491 pares vivos, **440 candidatos** (dd < 99%).
  La v1 (corte 2026-08-31) se conserva como historial.

## Ventana definitiva

**2026-09-30 → 2027-09-30** (12 meses desde el corte del
congelamiento). Con este anclaje:

- Los colapsos de **septiembre** ya son visibles en los datos del
  corte → esos pares quedan correctamente EXCLUIDOS de los candidatos.
- Los colapsos de **octubre en adelante** caen DENTRO de la ventana →
  se registran en la evaluación, que es exactamente donde deben estar.
- El solapamiento de la ADENDA 2 (datos de ventana existentes al
  congelar) queda reducido a cero: todo lo posterior al corte 2026-09-30
  es ventana por diseño.

## Sustituye a

- ADENDA 2, §1 (ventana): la ventana 2026-10-26 → 2027-10-26 queda
  sustituida por 2026-09-30 → 2027-09-30.
- El CSV v1 de la cohorte (paso a historial).
- El preregistro original y las adendas 1–2 se conservan íntegros
  (append-only).

## Sellado

Esta adenda y la ADENDA 2 (que hoy no tiene archivo externo — el DOI
23661819 la precede) quedan selladas en el próximo release del
repositorio procesado por Zenodo, junto con el resto de la ronda de
correcciones.
