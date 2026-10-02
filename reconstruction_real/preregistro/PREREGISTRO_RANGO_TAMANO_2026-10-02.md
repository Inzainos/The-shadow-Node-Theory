# Pre-registro — ¿la lognormal gana en todas partes? Réplica internacional del hallazgo de N-cuerpos

**Fecha:** 2026-10-02 · **Rama:** `claude/charming-brown-w9h8iu` · **Base:** `main` en `8f5f27b`
· **Autor de la teoría:** Elán Zainos Corona · **Análisis:** Claude Code, a pedido del autor.

## 0. De qué se trata

El 2026-10-02 se retiró la lectura de apego preferencial del Módulo de N-cuerpos: sobre
la curva rango-tamaño de las 32 entidades mexicanas, **la lognormal gana por ΔAIC = 65**
(informe `audits/RESULTADOS_LOGNORMAL_2026-10-02.md`).

Ese resultado tiene un límite duro y declarado: **n = 32**. La prueba de distribución de
Clauset no pudo decidir, y una prueba de poder mostró por qué — el procedimiento no
descarta la ley de potencia en **964 de 1,000** muestras que son lognormales por
construcción.

**La pregunta que México no puede responder es si eso es un hecho general o una
peculiaridad de 32 entidades con 0.81 órdenes de magnitud de rango.**

Otros países publican sus datos subnacionales abiertos y con **miles** de unidades. Con
n grande la prueba de Clauset recupera poder, y la pregunta deja de ser indecidible.

Esto es, además, una prueba directa de la afirmación de **invariancia** de la SNT: si el
patrón se repite en economías e instituciones distintas, deja de ser una curiosidad
mexicana; si no se repite, también se aprende algo.

## 0.1 Ceguera: **parcial**. Declarada

- **Visto:** el resultado completo de México (ΔAIC = 65 a favor de la lognormal, tasa de
  falso "sobrevive" del 96.4%). Es la motivación de este documento y sería absurdo
  fingir lo contrario.
- **No visto:** **ningún ajuste de Brasil ni de la Unión Europea.** De esas fuentes solo
  se ha inspeccionado el **esquema**: que responden, cuántas unidades devuelve cada
  nivel territorial, qué variables existen en cada tabla y en qué unidad de medida. No
  se ha calculado ni un exponente, ni un R², ni un AIC sobre esos datos.

## 0.2 Reglas generales

1. **Se reporta todo resultado**, por nivel y por país, favorable o no.
2. **α = 0.05**; p de dos colas.
3. **Semilla fija:** `20261002`.
4. **Log obligatorio** y SHA-256 de cada descarga en `data/FUENTES.md`.
5. **Unidad de inferencia:** el nivel territorial. Cada nivel es una réplica
   independiente; no se agrupan.

---

## 1. Datos y niveles

Año **2021** en todas las fuentes, por ser el más reciente con cobertura completa en
ambas (verificado en el esquema).

| Nivel | Fuente | Unidades |
|---|---|---:|
| Brasil, estados | IBGE SIDRA tabla 5938, variable 37, nivel `n3` | 27 |
| **México, entidades** | `data/matriz_mexico_32.csv` (ya versionado) | 32 |
| UE, NUTS1 | Eurostat `nama_10r_3gdp`, unidad `MIO_EUR` | 127 |
| UE, NUTS2 | Eurostat `nama_10r_3gdp`, unidad `MIO_EUR` | 309 |
| UE, NUTS3 | Eurostat `nama_10r_3gdp`, unidad `MIO_EUR` | 1,343 |
| **Brasil, municipios** | IBGE SIDRA tabla 5938, variable 37, nivel `n6` | **5,570** |

### Cantidad analizada: **PIB total**, no per cápita. Y por qué

La tabla de IBGE no publica per cápita, pero la decisión no es por conveniencia:

1. Es la única cantidad disponible en **todos** los niveles y países.
2. Es la cantidad de tipo Zipf donde una ley de potencia es siquiera plausible.
3. **Abarca muchos órdenes de magnitud.** El fracaso de México vino de usar per cápita,
   que abarcaba 0.81 órdenes: justo el régimen donde el método de Clauset no distingue
   nada.

**México entra en esta comparación por su columna `pct_pib`** (participación en el PIB
nacional), que es proporcional al PIB total y por tanto comparable en forma.

**Secundaria:** se repite todo con **per cápita** donde exista (Eurostat `EUR_HAB`, y
México con `pib_pc`), para medir cuánto del veredicto depende de la cantidad elegida.

### Exclusiones, fijadas aquí

- Se descartan los códigos agregados de Eurostat que no son del nivel analizado
  (`EU27_2020`, códigos de país de 2 letras, y los niveles superiores) quedándose solo
  con los códigos de la longitud que corresponde: 3 para NUTS1, 4 para NUTS2, 5 para
  NUTS3.
- Se descartan unidades con valor ausente, cero o negativo (el logaritmo no existe).
- No se descarta ninguna unidad por su valor. **Nada de recortar colas.**

---

## 2. Punto 1 — Curva rango-tamaño: potencia contra lognormal

Réplica exacta del procedimiento aplicado a México, para que los resultados sean
comparables.

Sobre las unidades ordenadas de mayor a menor se ajustan dos modelos de dos parámetros
cada uno:

- **Potencia:** log(valor) = log(a) + b·log(rango).
- **Lognormal:** valor = exp(μ + σ·Φ⁻¹(1 − (rango − 0.5)/n)), con μ y σ de máxima
  verosimilitud.

**H1.** La lognormal gana en todos los niveles, igual que en México.

**Decisión, por nivel**, con la convención habitual de AIC:

| ΔAIC a favor del mejor | Lectura |
|---|---|
| < 2 | Indistinguibles |
| 2 a 10 | Evidencia moderada |
| > 10 | Evidencia fuerte |

Se reportan R² en **ambas escalas** (logarítmica y cruda) por nivel, nunca promediados.

---

## 3. Punto 2 — Poder contra tamaño de muestra

Es la razón de ser de este pre-registro.

Para **cada nivel**, se simulan **500** muestras del mismo n extraídas de una
**lognormal** con los parámetros estimados de los datos reales de ese nivel, y se les
corre el procedimiento de Clauset completo (MLE con `x_min` por KS, bondad de ajuste por
bootstrap paramétrico de 100 réplicas).

**Se reporta, por nivel, la tasa de falso "sobrevive":** la fracción de muestras
lognormales en las que la ley de potencia resulta "no descartable".

**H2.** Esa tasa **decrece conforme n crece**. Se reporta la curva completa, de n = 27 a
n = 5,570.

**Umbral de interpretabilidad, fijado aquí:** un nivel tiene poder suficiente si su tasa
de falso "sobrevive" es **< 20%**. Solo en esos niveles se interpreta el punto 3.

---

## 4. Punto 3 — El veredicto, donde el método sí decide

En los niveles con poder suficiente (§3), se corre el procedimiento de Clauset sobre los
datos reales:

- **Bondad de ajuste** de la ley de potencia por bootstrap paramétrico (2,000 réplicas).
  Regla de Clauset: se descarta si p < 0.1.
- **Vuong** contra lognormal y contra exponencial, con p de dos colas.

**H3.** Donde hay poder, la ley de potencia se descarta y la lognormal gana.

| Resultado | Lectura |
|---|---|
| p < 0.1 en bondad de ajuste | La ley de potencia **se descarta** |
| Vuong R < 0 con p < 0.05 | Favorece la **lognormal** |
| Vuong R > 0 con p < 0.05 | Favorece la **ley de potencia** |
| Vuong p ≥ 0.05 | Indistinguible |

---

## 5. Qué significa cada desenlace

Escrito **antes** de ver los resultados, para que ninguna lectura se acomode después.

| Desenlace | Lectura para la SNT |
|---|---|
| La lognormal gana en todos los niveles | El hallazgo de México es **general**. La lectura de apego preferencial queda retirada no solo para México sino para la jerarquía económica subnacional en general. Es el desenlace que la evidencia actual hace más probable |
| La lognormal gana con n chico y la potencia con n grande | El hallazgo de México sería un **artefacto de n**, y habría que revisar la retirada del 2026-10-02 |
| Resultados mezclados entre países | La forma **depende del contexto institucional**, que sería un hallazgo propio y obligaría a matizar la afirmación de invariancia |
| Todo indistinguible incluso con n = 5,570 | La pregunta no es decidible con datos de este tipo, y el exponente b queda como **descriptivo** en todos los casos |

**Lo que este pre-registro NO hace:** no mide satelización ni prueba el eje b de la SNT.
Mide la **forma de la distribución de tamaños económicos subnacionales**, que es lo que
el Módulo de N-cuerpos usaba como evidencia de apego preferencial. El gradiente compuesto
de Tlaxcala (9.3×) no depende de esto y no se toca.

---

## 6. Salidas previstas

- `reconstruction_real/code/rango_tamano_internacional.py` (descarga y análisis, con log).
- `reconstruction_real/data/rango_tamano_internacional.csv` — una fila por nivel y prueba.
- `reconstruction_real/data/rango_tamano_poder.csv` — la curva de poder contra n.
- `reconstruction_real/audits/RESULTADOS_RANGO_TAMANO_2026-10-02.md`, con la tabla
  hipótesis → resultado → decisión y la sección **Desviaciones**.

## 7. Fuentes

| Fuente | Acceso verificado el 2026-10-02 |
|---|---|
| `https://apisidra.ibge.gov.br/values/t/5938/{nivel}/all/v/37/p/2021` | Responde; 27 estados y 5,570 municipios, en Mil Reais |
| `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10r_3gdp` | Responde; 1,343 NUTS3, 309 NUTS2, 127 NUTS1, en MIO_EUR y EUR_HAB |
| `data/matriz_mexico_32.csv` | Ya versionado en el repositorio |

Los datos de Estados Unidos quedan fuera: la API del BLS respondió
`REQUEST_NOT_PROCESSED` por umbral diario de peticiones agotado desde esta dirección, y
las de BEA y Census exigen clave. Se anota para que no parezca una omisión deliberada.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
