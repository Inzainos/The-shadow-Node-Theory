# FUENTES.md — provenance de datos externos

Este archivo ancla las **fuentes externas** del corpus SNT: de dónde salen, en
qué versión, y el checksum de los archivos derivados que sí viven en el repo.
Nació de un hallazgo de la auditoría integral v32: los resultados no estaban
anclados a una versión de datos, así que dos personas ejecutando el mismo
script en fechas distintas podían obtener cifras distintas sin saberlo.

> Regla del repo (AGENTS.md): **real data first**, reproducibilidad + provenance.
> Este documento es el índice de provenance. Actualízalo cuando cambie una
> fuente.

---

## 1. Fuentes externas que hay que descargar (NO están en el repo)

### `data/owid-maddison.csv` — **presente en el repo** (descargado 2026-07-25)

- **Quién la usa:** `reconstruction_real/code/expand_dominio_B.py` (línea 11) y
  `reconstruction_real/code/prueba_discriminante_dominio_B.py` (bloque 1).
- **Peso:** dominio B = **446 casos = 62% del corpus**.
- **Fuente primaria:** Maddison Project Database (Bolt & van Zanden), Groningen
  Growth and Development Centre (GGDC), vía Our World in Data.
- **Cuidado — dato vivo:** el Maddison Project **revisa sus estimaciones
  históricas de PIB entre ediciones**. Por eso se fija edición + fecha + SHA-256.

| Campo | Valor |
|---|---|
| Origen | OWID grapher `gdp-per-capita-maddison` (base: Maddison Project Database, cobertura hasta 2022 → release 2023) |
| URL de descarga | <https://ourworldindata.org/grapher/gdp-per-capita-maddison.csv> |
| Fecha de descarga | 2026-07-25 |
| Columnas conservadas | `Entity, Code, Year, GDP per capita` (se descartó la columna vacía de anotaciones) |
| Cobertura | 178 entidades · años 1–2022 · 21,586 filas |
| Licencia | OWID: CC BY 4.0 (atribuir Maddison Project Database + Our World in Data) |
| SHA-256 | `6e905c41324d50f2e4e468bad9d204a1efd44f6f34368c98425e8e0b33d6a4ec` |

> **Nota de reproducibilidad:** esta es la edición **vigente** de OWID/Maddison
> al 2026-07-25, no necesariamente la que se usó para construir
> `dominio_B_real.csv` originalmente. Para la prueba discriminante (b vs brecha
> inicial) eso no importa —testea una correlación, no reproduce el ajuste—, pero
> re-generar el dominio B con esta edición puede dar cifras algo distintas a las
> publicadas (el Maddison revisa el PIB histórico entre ediciones). Cobertura
> sobre el corpus: 102/103 países (falta "Sudan"), 441/446 pares con `year_min`
> disponible.

### Fuente de E3 (COVID-19) — series crudas **AUSENTES en el repo**

- **Quién la usa:** el dominio E3 (234 casos, 32% del corpus). En el repo solo
  vive el resumen ya ajustado (`by_domain/dominio_E3_real.csv`: `b,r2,p,n`), **no
  las curvas de casos acumulados**.
- **Fuente primaria (según la columna `fuente`):** Our World in Data COVID-19,
  a su vez de Johns Hopkins University (JHU CSSE).
  URL: <https://github.com/owid/covid-19-data/tree/master/public/data>
- **Consecuencia:** la corrección por autocorrelación de E3 está **bloqueada**
  hasta recuperar las series crudas (la aproximación AR(1) necesita los
  residuos, y E3 no los trae).

| Campo | Valor |
|---|---|
| Snapshot / commit de OWID | _(pendiente)_ |
| Fecha de descarga | _(pendiente)_ |
| SHA-256 del archivo crudo | _(pendiente)_ |

---

## 2. Archivos derivados que SÍ están en el repo (checksums)

Checksums SHA-256 al 2026-07-25. Sirven para detectar si un archivo cambió sin
que se documente. Recalcular con `sha256sum <archivo>`.

| Archivo | SHA-256 |
|---|---|
| `reconstruction_real/data/by_domain/dominio_B_real.csv` | `e0c7738a31b45b913c73d851ac1b81a9d2ea56aef7e9168ae991eda2687ce583` |
| `reconstruction_real/data/by_domain/dominio_E3_real.csv` | `11a99cc42a62a73dbe4b282acd66d48c8e86839e6a0fc8cdddc187f9c70c0e82` |
| `reconstruction_real/data/snt_corpus_REAL_v5.csv` | `6a4a89ed780552facfc0cd77a1abf7ce49b02d73211205d04f51f5eb5d38e9b1` |
| `reconstruction_real/data/snt_corpus_aco_timeseries_v29.csv` | `68c11e95e3b609008820111e303141b2d9391923960a5f7855c074e44512d31c` |
| `data/snt_asi_scores.csv` | `57e38ee9f779efc117b747247cb72ce6f869ae433f885aa116a653b766531fb6` |
| `data/owid-maddison.csv` | `6e905c41324d50f2e4e468bad9d204a1efd44f6f34368c98425e8e0b33d6a4ec` |

> Para regenerar la tabla:
> ```sh
> for f in reconstruction_real/data/by_domain/dominio_B_real.csv \
>          reconstruction_real/data/by_domain/dominio_E3_real.csv \
>          reconstruction_real/data/snt_corpus_REAL_v5.csv \
>          reconstruction_real/data/snt_corpus_aco_timeseries_v29.csv \
>          data/snt_asi_scores.csv; do
>   sha256sum "$f"
> done
> ```

---

## 3. Pendientes de provenance (heredados de la auditoría v32)

- [x] Descargar `data/owid-maddison.csv`, fijar edición + fecha + SHA-256 arriba.
      **Hecho 2026-07-25** (OWID grapher, cobertura hasta 2022).
- [ ] Recuperar las series crudas de E3 (OWID COVID snapshot) para desbloquear
      su corrección AR(1).
- [ ] Conseguir la matriz de comercio bilateral direccional (IMF DOTS / CEPII
      BACI / UN Comtrade) para desbloquear el bloque 2 de la prueba discriminante.
- [ ] Opcional: `download_sources.sh` que baje ambas fuentes y verifique los
      checksums, para que el corpus sea regenerable de punta a punta.
