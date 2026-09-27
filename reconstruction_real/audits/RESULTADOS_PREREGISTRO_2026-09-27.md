# Resultados del pre-registro 2026-09-27

**Pre-registro:** [`../preregistro/PREREGISTRO_2026-09-27.md`](../preregistro/PREREGISTRO_2026-09-27.md)
(commit `c319fac`, subido antes de descargar datos nuevos o correr pruebas).
**Rama:** `claude/charming-brown-w9h8iu` · PR #46.

Cada punto tiene su script (con log en `reconstruction_real/logs/`) y sus salidas
en `reconstruction_real/data/`. Las fuentes nuevas y sus SHA-256 están en
[`data/FUENTES.md`](../../data/FUENTES.md).

## Tabla de decisiones

| Punto | Hipótesis (SNT) | Resultado principal | Decisión pre-registrada |
|---|---|---|---|
| 1. Hub variable en el tiempo | El país diverge más de su hub comercial vigente que de un país con la misma brecha (d > 0) | d mediana por nodo −0.009; d > 0 en 38/96; Wilcoxon 1 cola p = 0.95 | **NO RESPALDADA** (H = 20); H = 10 no respaldada; **H = 30 CONTRARIA** |
| 2. Fricción con dominios nuevos | ρ(fricción, b̄ del dominio) < 0 sin COVID | ρ = −0.131 en 7 dominios; permutación exacta p = 0.39 | **NO RESPALDADA** (y en todas las variantes) |
| 3. Series crudas COVID | Sin dirección (corrección de reporte) | E3 reproducido 233/234; Newey-West p < 0.05 en 233/234 | E3 **sobrevive** la corrección; E1 **no reproducible** |
| 4. Disparadores a ciegas | El retador abrupto gana terreno más rápido que ciudades con la misma razón inicial (d > 0) | d > 0 en 8/8; Wilcoxon 1 cola p = 0.0039 | **RESPALDADA** (también con el año de decisión) |
| 5a. Ortogonalidad b ⊥ Δ | IC 95% de ρ(b_subida, Δ_caída) dentro de [−0.3, 0.3] | 242 pares Binance: ρ = −0.119, IC [−0.241, +0.007] | **RESPALDADA** (equivalencia) |
| 5b-i. Hazard positivo | Toda banda de edad con ≥ 30 en riesgo tiene fines | Cripto 8/8 bandas; bancos (cualquier fin) 39/39 | **RESPALDADA** en ambas cohortes; solo quiebras bancarias: sin evidencia en 4 bandas de ≥ 155 años |
| 5b-ii. Hazard crece con la edad | Spearman(edad, h) > 0 | Cripto ρ = +0.881, p = 0.002; bancos (entrada 1970) ρ = +0.050, p = 0.38 | **Respaldada en cripto** (confundida con el calendario); **no respaldada en bancos** (forma de bañera) |
| 5c. Fricción → Δ | — | No se amplía (sin datos públicos comparables) | Declarado |

---

## 1. Hub variable en el tiempo (pares de países)

Script: `code/prueba_hub_temporal.py` → `data/hub_temporal_espacios.csv`.

Para cada uno de los 103 países del dominio B y cada década de 1900 a 1990, el hub es el
mayor destino de exportaciones en los 5 años previos (COW), y se mide R(t) = PIBpc_hub /
PIBpc_nodo en los H años siguientes contra hasta 5 países con la misma brecha inicial que
no son socios principales.

| Horizonte | Periodos (nodo × década) | Nodos | d mediana por nodo | d > 0 | Wilcoxon 1 cola | 2 colas | Decisión |
|---|---:|---:|---:|---:|---:|---:|---|
| **20 años (principal)** | 593 | 96 | −0.009 | 38/96 | 0.95 | 0.10 | **No respaldada** |
| 10 años | 590 | 96 | +0.004 | 54/96 | 0.068 | 0.14 | No respaldada |
| 30 años | 593 | 96 | −0.017 | 25/96 | 1.00 | **0.0002** | **Contraria** |

- Por cluster de hub (H = 20): 34 hubs, d mediana +0.004, 18/34 positivos, p = 0.31.
- Solo con hub más rico al inicio: igual (d mediana −0.009, p = 0.95). Sin los 20 periodos
  con comercio CMEA dudoso: igual (p = 0.97).
- Con hub más rico, b > 0 (divergencia) en 209/518 periodos: domina la convergencia.
- El hub cambia 185 veces entre décadas; 78 de 96 países cambian de hub al menos una vez.
  Hubs más frecuentes: Estados Unidos (206 periodos), Reino Unido (157), Francia (41),
  Alemania (37), Japón (30), URSS (25).
- Especificación no fijada en el pre-registro: mínimo de observaciones para H = 10 y 30
  (se usó la misma proporción que para 20: ceil(0.75·H) = 8 y 23).

**Lectura:** con el hub comercial vigente, década por década, no aparece el acoplamiento
extractivo. A 30 años el efecto es el opuesto: el país converge más hacia su socio principal
que hacia un país igual de lejano con el que no comercia.

## 2. Fricción con dominios nuevos, sin COVID

Script: `code/prueba_friccion_dominios_nuevos.py` → `data/friccion_dominios_nuevos_*.csv`.

| Dominio | Fricción | n | b̄ | b mediana |
|---|---:|---:|---:|---:|
| E4 mpox 2022 (nuevo) | 0 | 59 | +0.425 | +0.303 |
| D2 cuotas digitales StatCounter (nuevo) | 1 | 18 | +0.018 | +0.072 |
| A ciudades (corpus) | 2 | 4 | +0.082 | +0.060 |
| A2 ciudades WUP 1950–2018 (nuevo) | 2 | 1,704 | −0.315 | −0.214 |
| B-comercio (PR #45) | 3 | 102 | −0.074 | −0.094 |
| C regiones (corpus) | 3 | 24 | +0.091 | +0.059 |
| E2 depredador-presa (corpus) | 3 | 2 | +0.145 | +0.145 |

| Prueba | Dominios | ρ | p (permutación exacta, 1 cola) | Decisión |
|---|---:|---:|---:|---|
| **Principal (media)** | 7 | −0.131 | 0.39 | **No respaldada** |
| Mediana | 7 | −0.430 | 0.17 | No respaldada |
| Con B publicado | 7 | +0.112 | 0.61 | No respaldada |
| + E1 y E3 (con COVID) | 9 | −0.581 | 0.055 | No respaldada |
| + D (exponentes de distribución) | 8 | +0.049 | 0.55 | No respaldada |

**Lectura:** el polo sin fricción se repite con otra epidemia (mpox, b̄ +0.43), pero fuera de
las epidemias no hay orden por fricción: ciudades y países (fricción media y alta) dan b
negativo (convergencia) y los mercados digitales (fricción baja) dan b cercano a cero. La
relación fricción → b del corpus descansa en el contraste epidemias vs. todo lo demás.

## 3. Series crudas de COVID (E3, E1)

Script: `code/covid_E3_series_crudas.py` → `data/dominio_E3_series_crudas.csv`.

- **Receta de E3 identificada** con la regla pre-registrada (la primera de 6 recetas que
  reproduce ≥ 90%): casos acumulados, 60 días desde el primer día con ≥ 100 casos
  acumulados. Reproduce **233/234** b publicados dentro de ±0.01 (Timor Oriental: publicado
  +0.688, crudo +0.111).
- **Corrección por autocorrelación** (mismas funciones que la auditoría v32 usó en B):

| Medida | E3 | Dominio B (auditoría v32) |
|---|---:|---:|
| Durbin-Watson mediana | 0.431 | 0.112 |
| n efectivo mediano (nominal) | 7.25 (60) | 2.2 (69) |
| Estimables (n_eff ≥ 3) | 198/234 | 156/446 |
| Newey-West p < 0.05 | **233/234** | — |
| Cota AR(1) entre estimables | 176–196/198 | 33–112/156 |

- **E1** (4 casos): ninguna construcción natural (países alcanzados por fecha, umbrales
  1/10/100, inicio en los datos o en el primer caso) reproduce los valores publicados; se
  declara **no reproducible**.

**Lectura:** a diferencia del dominio B, la significancia de E3 sobrevive la corrección:
el crecimiento epidémico tipo ley de potencia es una señal real en esos datos.

## 4. Disparadores codificados a ciegas (ciudades)

Script: `code/prueba_disparadores_ciudades.py` → `data/disparadores_ciudades_casos.csv`.

| Caso | Año | b del caso | b̄ controles (5) | d | Percentil en su pool |
|---|---:|---:|---:|---:|---:|
| Brasília / Rio de Janeiro | 1960 | +0.740 | +0.456 | +0.284 | 1.00 (8) |
| Islamabad / Karachi | 1967 | +0.396 | +0.066 | +0.331 | 1.00 (5) |
| Abuja / Lagos | 1991 | +0.391 | −0.089 | +0.480 | 1.00 (8) |
| Astana / Almaty | 1997 | +0.259 | −0.081 | +0.340 | 1.00 (5) |
| Shenzhen / Guangzhou (ZEE) | 1980 | +1.241 | +0.003 | +1.238 | 1.00 (76) |
| Zhuhai / Guangzhou (ZEE) | 1980 | +0.665 | +0.167 | +0.499 | 1.00 (82) |
| Shantou / Guangzhou (ZEE) | 1980 | +0.200 | −0.324 | +0.524 | 1.00 (36) |
| Xiamen / Fuzhou (ZEE) | 1980 | +0.192 | −0.064 | +0.256 | 0.86 (28) |
| Berlín / Bonn | 1999 | −0.005 | sin controles | — | — |

| Prueba | Casos | d mediana | d > 0 | Wilcoxon 1 cola | Decisión |
|---|---:|---:|---:|---:|---|
| **Principal (año efectivo)** | 8 | +0.410 | 8/8 | **0.0039** | **Respaldada** |
| Año de decisión | 8 | +0.513 | 8/8 | 0.0039 | Respaldada |
| Solo capitales | 4 | +0.335 | 4/4 | 0.0625 | (n = 4; razón de b 5.1×) |
| Solo ZEE (descriptivo) | 4 | +0.511 | 4/4 | 0.0625 | — |

- Excluidos por datos (su ciudad no está en el archivo de ≥ 300 mil en 2018): Dodoma,
  Yamoussoukro, Zomba.
- **Salvedad principal:** WUP solo lista aglomeraciones con ≥ 300 mil habitantes en 2018.
  El filtro se aplica igual a casos y controles, pero deja fuera traslados que crecieron
  poco (Dodoma, Yamoussoukro), lo que sesga la muestra de casos hacia los exitosos.
- Lo que se prueba es "decreto abrupto vs dinámica basal con la misma razón inicial", no
  "abrupto vs gradual" en el sentido de la v1.0. La razón de b en capitales (5.1×) es
  parecida al 5.9× de la v1.0, pero con 4 casos.

**Lectura:** primer resultado pre-registrado a favor de la SNT. Una ciudad favorecida por un
decreto abrupto gana terreno contra el incumbente más rápido que ciudades comparables. El
hallazgo retirado en la r31 (5.9×) tiene ahora un sustituto con diseño limpio, con n chico y
la salvedad de supervivencia.

## 5. Cohortes ampliadas de ACO-A

Scripts: `code/descargar_binance_klines.py` (archivo público de Binance; 664 pares spot contra
USDT tras excluir 23 estables/fiat y 48 apalancados; 663 con velas diarias, 780,348 cierres,
2017-08-17 a 2026-08-31) y `code/aco_cohortes_ampliadas.py` → `data/aco_ortogonalidad_binance.csv`,
`data/aco_hazard_bandas.csv`. Bancos: FDIC BankFind (27,834 instituciones, 4,117 quiebras).

### 5a. Ortogonalidad b ⊥ Δ

| | Antes (Yahoo, v25) | Ahora (Binance) |
|---|---:|---:|
| Pares que cumplen las reglas | 11 | **242** |
| Spearman ρ(b_subida, Δ_caída) | +0.009 (p = 0.98) | **−0.119** (p = 0.065) |
| IC 95% (Fisher) | — | [−0.241, +0.007] |
| Pearson r | — | −0.103 (p = 0.11) |

**Decisión: RESPALDADA por equivalencia** — el IC cae dentro de [−0.3, +0.3]. La asociación, si
existe, es débil y negativa (mayor subida, caída algo más pronunciada), no significativa. Salvedades:
153 de los 242 máximos ocurrieron en 2021 (un solo ciclo de mercado), y el "nacimiento" es el
listado en Binance, no el origen de la moneda.

### 5b. Hazard h(τ)

**Cripto** (663 pares; 124 extinciones funcionales ACO; 185 pares retirados; 252 con extinción
o retiro):

| Edad (años) | En riesgo | Extinciones ACO | h (por año) | h con retiro |
|---|---:|---:|---:|---:|
| 0–1 | 663 | 4 | 0.007 | 0.033 |
| 1–2 | 516 | 7 | 0.015 | 0.090 |
| 2–3 | 392 | 17 | 0.048 | 0.104 |
| 3–4 | 321 | 22 | 0.077 | 0.169 |
| 4–5 | 244 | 37 | 0.182 | 0.271 |
| 5–6 | 159 | 24 | 0.199 | 0.299 |
| 6–7 | 83 | 9 | 0.161 | 0.215 |
| 7–8 | 37 | 4 | 0.183 | 0.183 |

- **Positividad:** las 8 bandas con ≥ 30 en riesgo tienen extinciones → **respaldada**.
- **Forma:** el hazard crece con la edad (ρ = +0.881, p 1 cola = 0.002; con retiro, ρ = +0.786,
  p = 0.010) → **respaldada**, pero **confundida con el calendario**: los pares listados en
  2017–2020 llegan a 4–6 años durante el mercado bajista de 2022–2025, que es cuando se concentran
  las extinciones. Separar edad de periodo requiere un modelo edad-periodo-cohorte (pendiente).

**Bancos FDIC** (27,771 instituciones tras excluir 41 fechas de fundación de relleno y 22
inactivas sin fecha de cierre; 23,505 fines por cualquier causa, 3,565 quiebras emparejadas por
CERT):

| Especificación | Positividad (bandas de 5 años, ≥ 30 en riesgo) | Forma: ρ(edad, h) | Decisión forma |
|---|---|---:|---|
| Cualquier fin, entrada pre-registrada 1934 (**sesgada**) | 39/39 con fines | +0.623 (p < 0.001) | respaldada (artefacto) |
| **Cualquier fin, entrada corregida 1970** | **39/39 con fines** | **+0.050 (p = 0.38)** | **no respaldada** |
| Solo quiebras, entrada 1934 (sesgada) | sin fines en 4 bandas (≥ 155 años) | −0.453 | no respaldada |
| Solo quiebras, entrada 1970 | sin fines en 4 bandas (≥ 155 años; n = 43–361) | −0.764 | no respaldada |

- Con la entrada corregida, el hazard de "cualquier fin" es de **bañera**: 0.04–0.06 por año en
  los primeros 35 años, ~0.02–0.03 entre los 35 y los 125, y vuelve a subir en edades muy altas.
  No crece de forma monótona.
- Las quiebras (sin fusiones) bajan con la edad: 0.007–0.014 por año en los primeros 35 años y
  cerca de 0.001–0.003 después; en 4 bandas de más de 155 años no hay ninguna (la cota superior
  3/n va de 0.008 a 0.070).
- La especificación pre-registrada (entrada en 1934) da "respaldada" en la forma solo porque la
  base no registra cierres antes de 1970 (ver Desviaciones): no debe usarse.

**Lectura:** "ningún sistema es eterno" (h > 0) se sostiene en dos cohortes grandes e
independientes, con fines en todas las edades. La afirmación de la v30 de que el hazard **crece**
con la edad solo aparece en cripto, donde está confundida con el calendario; en bancos no se
cumple. La forma del hazard depende del dominio.

### 5c. Fricción → Δ

No se amplía: no hay series públicas de absorción post-quiebra comparables a las de la cohorte
2008 (n = 6). Sigue pendiente.

## Desviaciones respecto al pre-registro

1. **Punto 1:** el mínimo de observaciones para H = 10 y 30 no estaba fijado; se usó
   ceil(0.75·H).
2. **Punto 2 (D2):** en social media y mobile vendor, StatCounter trae meses iniciales sin
   datos (todas las cuotas en 0) y filas desordenadas; se ordenó por fecha y se descartaron
   esos meses antes de tomar los "primeros 12 meses". Mobile vendor solo existe para móvil.
3. **Punto 4:** el archivo anual de WUP 2018 es el F22 (el F12 es quinquenal); el
   pre-registro decía "archivo anual".
4. **Punto 5 (bancos):** la base de la FDIC no registra ningún cierre antes de 1970 (0 en
   1934–1969; 1,653 en 1970–1979). Con la entrada pre-registrada (edad en 1934), el hazard de esas
   décadas sale en cero por construcción. Se reportan ambas especificaciones y la decisión se basa
   en la corregida (entrada en 1970). Se excluyeron además 41 fechas de fundación de relleno
   (01/01/1800) y 22 instituciones inactivas sin fecha de cierre (12/31/9999).
5. **Punto 5 (cripto):** el umbral de "par retirado" (última vela más de 31 días antes del final
   del archivo) no estaba fijado. Un par (USDSOLDUSDT) no tiene velas diarias; uno con nombre no
   ASCII (币安人生USDT) requirió codificar la URL.
6. **Punto 3:** no se usó la serie de Johns Hopkins; la receta se identificó con OWID, como decía el
   pre-registro.
