# Corpus SNT — datos, resultados y reproducibilidad

El corpus consolidado vigente es [`data/snt_corpus_REAL_v6.csv`](data/snt_corpus_REAL_v6.csv)
(721 casos). La cifra de casos no implica independencia estadística: los
registros se agrupan por dominios, sus fuentes y recetas difieren, y la
reproducibilidad no es uniforme. Los resultados principales se resumen por
evidencia y límite, no por significancia nominal por fila.

## Estado empírico por dominio

| Dominio | Casos | Resultado de reconstrucción | Límite inferencial principal |
|---|---:|---|---|
| A — ciudades | 4 | 1/4 reproduce una pendiente publicada, pero con ventana temporal incompatible; coincidencia espuria. | No reproducible como dominio. |
| B — países | 446 | Reproduce byte a byte con Maddison Project Database 2020. | 445/446 presentan autocorrelación severa; 290/446 no son estimables por `n_eff < 3`. Ninguno de 12 métodos supera la compuerta de falsos positivos; el valor puntual es **indecidible**. |
| C — regiones | 24 en el corpus; 23 trayectorias en RC1 | Las 23 trayectorias reproducen con una receta preespecificada. El caso restante es rango-tamaño, no `R(t)`. | AIC no es interpretable en la banda `b ≥ 1` (error de selección 22.6%); la significancia nominal por caso no corrige la autocorrelación. |
| D — digital | 3 | Basado en HackerEarth. | Datos de origen propietarios; no reproducible desde el repositorio. |
| E1 — expansión espacial | 4 | No reproduce desde las series crudas con las construcciones evaluadas. | No reproducible; no presentarlo como validación independiente. |
| E2 — depredador-presa | 2 | E2_01 reproduce exactamente; E2_02 no reproduce. | La calibración de RC1 corresponde a un solo caso. |
| E3 — expansión epidemiológica | 234 | 233/234 pendientes reproducidas desde la serie OWID anclada; `r2_raw` está disponible para 233/234. | 198/234 son estimables tras AR(1); 176–196 de esos casos siguen significativos según la cota y variante analítica. |
| F1–F3 — sistemas físicos | 4 | Se conservan como relaciones de masa/órbita. | No son trayectorias temporales `R(t)` equivalentes; no calibrables como RC1. |

Los resultados de `r2_raw` están disponibles en **720/721** filas del corpus
v6; `p_exacto`, en **680/721**. Las celdas faltantes permanecen como faltantes.
Los valores p por fila del corpus son nominales y no deben agregarse como
pruebas independientes.

## Hallazgos y pruebas

### Inferencia en el Dominio B

El dominio B se reproduce exactamente desde MPD2020, pero la autocorrelación
impide declarar un valor puntual de significancia. La simulación recalibrada
con `N=200,000` encontró que los 12 métodos evaluados quedan fuera de la banda
de falsos positivos predefinida `[2.5%, 7.5%]`; la cota inferior AR(1) mide
7.96% (IC95 `[7.76%, 8.17%]`). La proporción puntual del Dominio B queda
**indecidible**, no sustituida por una estimación nominal.

En la prueba discriminante con un hub emergente del comercio, `ρ(b, brecha) =
-0.153` (`p=0.125`) y la comparación hub–control no detecta diferencia
(`p=0.78`). La reconstrucción no rescata evidencia de acoplamiento SNT por
encima del nulo calibrado.

### Fricción y agrupación por dominio

La correlación por fila publicada para fricción y `b` no es una inferencia
válida sobre 714 observaciones independientes. Al resumir por seis dominios,
`ρ=-0.556`, `p=0.253`; la prueba preespecificada con dominios nuevos tampoco
respalda la relación (`ρ=-0.131`, permutación exacta `p=0.39`). El polo de
menor fricción incluye 238 registros de expansión COVID-19, no casos de
invasión biológica.

### RC1 — banda `b ≥ 1`

La tasa de error de selección AIC supera el umbral preespecificado del 20% en
todos los dominios calibrados: E3 80.3%, B 96.8%, ACO 48.9%, C 22.6% y E2_01
94.0%. La banda no es interpretable por AIC en esos dominios. La frecuencia con
que una exponencial produce `b ≥ 1` también depende de la estructura del
dominio: 70–100% en E3/B/ACO, frente a 0.7% en C. Por sí sola, `b ≥ 1` no
establece un régimen físico universal.

### ACO-A y aplicaciones externas

- En los 18 casos ACO, la diferencia descriptiva entre disparadores abruptos y
  graduales no es concluyente (`p=0.101`); la permutación intra-dominio da
  `p=0.938`. El disparador está confundido con el dominio.
- En la cohorte npm externa al corpus, `b` y `Δ` presentan una asociación
  pequeña (`ρ=+0.114`, IC95 `[+0.016,+0.209]`), compatible con el criterio de
  equivalencia preespecificado. El hazard decrece con la edad (`ρ=-0.716`,
  `p=0.013`, dos colas), con cautela por censura y mezcla edad-periodo-cohorte.
- El seguimiento fricción→`Δ` es post-hoc: `ρ=-0.377`, `p=0.121` en ACO
  (`n=18`) y `ρ=+0.163`, `p=0.0005` en npm (`n=450`). Requiere réplica
  pre-registrada en otro ecosistema.
- Para rango-tamaño, la lognormal mejora el AIC frente a la potencia en 65.04
  puntos en las 32 entidades mexicanas. La prueba de Clauset sigue teniendo
  alta tasa de falso “sobrevive” en todos los niveles de la réplica
  internacional, incluso 42.6% con 5,570 municipios brasileños.

## Datos y procedencia

- Datos consolidados por dominio: [`data/by_domain/`](data/by_domain/).
- Corpus actual: [`data/snt_corpus_REAL_v6.csv`](data/snt_corpus_REAL_v6.csv).
- Fuentes, ediciones y SHA-256: [`../data/FUENTES.md`](../data/FUENTES.md).
- Auditorías y decisiones completas: [`audits/`](audits/).
- Pre-registros: [`preregistro/`](preregistro/).
- Las series crudas de HackerEarth no se redistribuyen; sus resultados
  agregados y evaluación temporal están en
  [`../data/hackerearth_zerve/NUMEROS_REALES_2026-10-18.md`](../data/hackerearth_zerve/NUMEROS_REALES_2026-10-18.md).

## Reproducir

Desde la raíz del repositorio, con el entorno descrito en
[`../AGENTS.md`](../AGENTS.md):

```bash
python reconstruction_real/code/snt_auditoria_integral_v32.py
pytest reconstruction_real/tests
```

Para regenerar B desde MPD2020:

```bash
python reconstruction_real/code/build_maddison_mpd2020_csv.py
python reconstruction_real/code/expand_B_massive.py
```

Para el módulo ACO-A ejecutado por CI:

```bash
python reconstruction_real/code/build_aco_v29.py
```
