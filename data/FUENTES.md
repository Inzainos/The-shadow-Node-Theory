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

### `data/owid-maddison.csv` — **AUSENTE en el repo**

- **Quién la usa:** `reconstruction_real/code/expand_dominio_B.py` (línea 11:
  `pd.read_csv('data/owid-maddison.csv')`).
- **Peso:** dominio B = **446 casos = 62% del corpus**. Sin este archivo el
  dominio B **no se regenera clonando el repo**.
- **Fuente primaria:** Maddison Project Database, Groningen Growth and
  Development Centre (GGDC).
  URL: <https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases>
  (mirror habitual vía Our World in Data: <https://ourworldindata.org/grapher/gdp-per-capita-maddison>).
- **Cuidado — dato vivo:** el Maddison Project **revisa sus estimaciones
  históricas de PIB entre ediciones**. Hay que fijar edición + fecha + SHA-256.

| Campo | Valor |
|---|---|
| Edición | _(pendiente: p.ej. "Maddison Project Database 2023")_ |
| Fecha de descarga | _(pendiente)_ |
| URL exacta del archivo | _(pendiente)_ |
| SHA-256 | _(pendiente — correr `sha256sum data/owid-maddison.csv` tras descargar)_ |

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

- [ ] Descargar `data/owid-maddison.csv`, fijar edición + fecha + SHA-256 arriba.
- [ ] Recuperar las series crudas de E3 (OWID COVID snapshot) para desbloquear
      su corrección AR(1).
- [ ] Opcional: `download_sources.sh` que baje ambas fuentes y verifique los
      checksums, para que el corpus sea regenerable de punta a punta.
