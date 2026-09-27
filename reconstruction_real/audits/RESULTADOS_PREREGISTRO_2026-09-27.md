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
| 5. Cohortes ACO-A | 5a ortogonalidad; 5b-i h > 0; 5b-ii h crece con la edad | _(ver §5)_ | _(ver §5)_ |

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

_(pendiente: corriendo la descarga del archivo de Binance)_

## Desviaciones respecto al pre-registro

1. **Punto 1:** el mínimo de observaciones para H = 10 y 30 no estaba fijado; se usó
   ceil(0.75·H).
2. **Punto 2 (D2):** en social media y mobile vendor, StatCounter trae meses iniciales sin
   datos (todas las cuotas en 0) y filas desordenadas; se ordenó por fecha y se descartaron
   esos meses antes de tomar los "primeros 12 meses". Mobile vendor solo existe para móvil.
3. **Punto 4:** el archivo anual de WUP 2018 es el F22 (el F12 es quinquenal); el
   pre-registro decía "archivo anual".
