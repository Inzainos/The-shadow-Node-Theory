# Análisis: LFS vs DVC para los binarios pesados (pendiente 2.1)

**Fecha:** 2026-10-26 · **DECISIÓN DEL OPERADOR: NO MIGRAR** (2026-10-26)
— el repo se queda como está. Este documento queda como el registro del
análisis y del porqué: LFS arriesga el sellado Zenodo, DVC necesita un
remote inexistente, y los 49 MB no rompen nada.

## El problema

`.git` pesa 49 MB. Archivos grandes versionados:

| Archivo | Peso |
|---|---|
| `figures/Fig1–Fig4.tif` | ~6 MB c/u |
| `data/COW_Trade_4.0.zip` | 12 MB |
| `reconstruction_real/data/tela_exogena_series.csv` | 5,9 MB |
| `data/binance_cierres_diarios.csv.gz` | 3,8 MB |

## Opción A: Git LFS — tiene un problema REAL con el sellado

LFS mueve el contenido a storage externo y deja punteros en el repo.
**Riesgo medido en la documentación de Zenodo**: el archivador
GitHub→Zenodo de releases NO siempre resuelve los archivos LFS — en
varios casos archiva los PUNTEROS sin el contenido. Para un repo cuyo
sellado externo de preregistros DEPENDE de que el snapshot Zenodo
contenga los datos (el DOI 23661819 archiva el zip completo del repo,
43 MB, CON los CSV), **LFS puede romper la cadena de sellado**: un
preregistro sellado que referencia `tela_exogena_series.csv` quedaría
sellado sin el dato. Además: mover los archivos a LFS no reduce los
49 MB ya escritos en la historia — eso exige un rebase destructivo
(rewriting history) que invalidaría todos los commits firmados
anteriores, incluyendo los preregistros sellados por fecha de git.

## Opción B: DVC — necesita infraestructura que no existe

DVC guarda los datos fuera del repo con caché local + remote. No rompe
Zenodo (los archivos quedan en el working tree) PERO necesita un
storage remote configurado (S3/GDrive/SSH) que este repo no tiene;
sin remote, la "reproducibilidad" de DVC es solo local — no más
portátil que el status quo.

## Recomendación (no vinculante)

1. **No migrar ahora** — el costo de romper el sellado Zenodo (LFS) o
   de montar infra nueva (DVC) supera el beneficio: 49 MB de .git es
   incómodo, no disfuncional.
2. Si el peso crece: preferir **DVC con un remote explícito** antes que
   LFS, precisamente por el sellado Zenodo.
3. Mitigación barata disponible YA: los `.tif` de figures son
   exportables desde los scripts versionados (`generate_figures_v29.py`
   los produce) — dejar de versionar los .tif y regenerarlos en CI
   reduce ~24 MB de los futuros pushes sin tocar datos ni sellado.
