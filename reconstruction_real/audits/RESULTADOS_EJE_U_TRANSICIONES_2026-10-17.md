# Resultados — eje `u` por entropia condicional de transiciones

**Pre-registro:** `reconstruction_real/preregistro/PREREGISTRO_EJE_U_TRANSICIONES_2026-10-17.md`
**Revision ejecutada:** `083145c548c201e99cc7af619521fc4159391344`

Esta corrida evalua `u^H` por dominio. No promedia ni ordena B y cripto, no usa `b`, `Delta` ni friccion como descriptor, y no hace una afirmacion causal o predictiva.

## Procedencia

| Archivo | SHA-256 |
|---|---|
| `data/maddison_mpd2020.csv` | `1c0b15ae4b78d54134d3c781e361784ee06c8519762ca6ceb45ef65fc31d54c0` |
| `reconstruction_real/data/by_domain/dominio_B_real.csv` | `e0c7738a31b45b913c73d851ac1b81a9d2ea56aef7e9168ae991eda2687ce583` |
| `data/binance_cierres_diarios.csv.gz` | `fcb2ad7e34f7b5d0ad3ee4a685f952f3e9391bc9d85212b2eb110428d375915e` |
| `reconstruction_real/data/eje_u_transiciones_por_caso.csv` | `c2e006a364dcc207e035469ce86f1d7785eb3d02607087814314559ae0af3629` |
| `reconstruction_real/data/eje_u_transiciones_resumen.csv` | `a71f3ccaf1b4a739451c3717ffd844e6f6cc05103c168190913bb90ba1176d5a` |

## Compuertas por dominio

| Dominio | Compuerta | Estado | Valor | Umbral | Detalle |
|---|---|---|---:|---|---|
| B | A_cobertura | **PASA** | 96 | >=30 | Casos con ambas proyecciones y al menos 12 posiciones alineadas. |
| B | B_invarianza | **FALLA** | -0.0652226619068 | evaluables>=90%; mediana>=0.60; casos>=67% con rho>=0.30 | fraccion_evaluable=1.000; fraccion_casos=0.104 |
| B | C_variacion | **PASA** | 0.145524119939 | mediana_IQR>=0.05 | IQR de h_t bajo theta1. |
| B | D_no_colapso | **PASA** | 0.0208333333333 | evaluables>=90%; casos_colapsados<75% con |rho|>=0.90 | fraccion_evaluable=1.000; casos_colapsados=2 |
| Cripto | A_cobertura | **PASA** | 571 | >=30 | Casos con ambas proyecciones y al menos 12 posiciones alineadas. |
| Cripto | B_invarianza | **FALLA** | 0.075779762226 | evaluables>=90%; mediana>=0.60; casos>=67% con rho>=0.30 | fraccion_evaluable=1.000; fraccion_casos=0.004 |
| Cripto | C_variacion | **PASA** | 0.107355009926 | mediana_IQR>=0.05 | IQR de h_t bajo theta1. |
| Cripto | D_no_colapso | **PASA** | 0 | evaluables>=90%; casos_colapsados<75% con |rho|>=0.90 | fraccion_evaluable=1.000; casos_colapsados=0 |

## Decision pre-especificada

- **B:** `NO_ADMITIDO`
- **Cripto:** `NO_ADMITIDO`
- **Resultado:** El eje `u` sigue sin definicion operativa: el candidato no supero todas las compuertas en ambos dominios.

## Desviaciones

Ninguna. Se ejecutaron las fuentes, proyecciones, umbrales y desenlaces fijados en el pre-registro.
