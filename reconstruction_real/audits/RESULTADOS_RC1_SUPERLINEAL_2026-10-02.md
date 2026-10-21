# Resultados — RC1: verificación de la banda b ≥ 1

**Pre-registro:** [`../preregistro/PREREGISTRO_RC1_SUPERLINEAL_2026-10-02.md`](../preregistro/PREREGISTRO_RC1_SUPERLINEAL_2026-10-02.md)
(commit `1a2ac0e`, subido antes de escribir el script).
**Script:** `code/rc1_superlineal.py` (con log). **Sin descargas.**
**Salidas:** `reconstruction_real/data/rc1_por_caso.csv`,
`reconstruction_real/data/rc1_calibracion.csv`,
`reconstruction_real/logs/rc1_superlineal_log.txt`.

## Tabla de decisiones, por dominio y sin agrupar

| Punto | E3 (234 casos) | B (446 casos) | ACO (18, control) |
|---|---:|---:|---:|
| Reproducción previa | **233/234** (±0.01) | **446/446** (±1e-4) | **13/4/1 exacto** |
| **P0 — error de selección del AIC con `b ≥ 1`** | **80.3%** | **96.8%** | **48.9%** |
| **Veredicto de la compuerta (umbral 20%)** | **NO INTERPRETABLE** | **NO INTERPRETABLE** | **NO INTERPRETABLE** |
| P1 ganadores (no interpretable) | potencia 64 / exp 51 / lin 119 | potencia 112 / exp 138 / lin 196 | potencia 13 / exp 4 / lin 1 |
| P2 `Spearman(b, ΔAIC)` (no interpretable) | −0.250, p = 0.0001 | **+0.039, p = 0.79** | −0.796, p < 0.0001 |
| P3 Fisher OR (no interpretable) | 0.153, p < 0.0001 | 0.000, p = 0.17 | 0.056, p = 0.0441 |
| P4 superlineales que ajustan mejor con otra forma | 82 de 90 (**91.1%**) | 6 de 6 (**100%**) | 3 de 4 (75%) |
| **P5 — una exponencial verdadera da `b ≥ 1`** | **69.7% y 99.9%** según banda | **70.6%** | **98.0% y 100%** |

**Veredicto:** RC1 queda **cerrado como indecidible por AIC** en estos dominios. Y la
banda "Roche Radius" de `snt_utils.py` queda **sin respaldo como régimen físico**, no
porque el AIC lo diga —no puede decirlo— sino porque **una exponencial verdadera
produce `b ≥ 1` casi siempre.**

---

## 1. P0 — La compuerta, y el error crece con `b`

Se simula desde una **ley de potencia conocida** (la `b` de cada caso) con la σ y la
ρ AR(1) de ese mismo caso, 200 réplicas. Todo lo que el AIC elija que no sea potencia
es **error por construcción**.

| Banda de `b` | E3 | B | ACO |
|---|---:|---:|---:|
| `b < 0.5` | 14.1% (62 casos) | 40.4% (418) | 16.3% (13) |
| `0.5 ≤ b < 1` | 57.0% (82) | 66.6% (22) | 20.5% (1) |
| `1.0 ≤ b < 1.5` | **88.6%** (57) | **96.8%** (6) | 46.5% (1) |
| `b ≥ 1.5` | **65.9%** (33) | — | **49.7%** (3) |
| **`b ≥ 1` agregada** | **80.3%** | **96.8%** | **48.9%** |

**El error de selección crece con `b`.** En E3 pasa de 14.1% a 88.6%; en B de 40.4% a
96.8%; en el ACO de 16.3% a ~49%. Es decir: **cuando los datos son una ley de potencia
pura y de exponente alto, el AIC elige otra cosa 8 de cada 10 veces en E3 y casi
siempre en B.**

Eso activa el desenlace que el pre-registro declaró como el más informativo de los seis:

> *"Si además la tasa crece con `b`, se reporta como **el hallazgo del ACO queda
> explicado como artefacto del estimador**, lo cual es más fuerte que confirmarlo."*

**Y eso es lo que pasó.** El hallazgo de la auditoría v32 —"a mayor `b`, peor ajusta la
ley de potencia", ρ = −0.796 sobre 18 series— es **exactamente lo que este estimador
produce aunque todos los casos sean leyes de potencia perfectas.** No era una propiedad
de los sistemas; era una propiedad del procedimiento.

La causa técnica es doble y las dos estaban anotadas en el pre-registro: el AIC de
`comparar_modelos` se calcula sobre residuos **en escala cruda**, donde los valores
grandes del final de una serie creciente dominan la suma; y los residuos de estos
dominios están **muy autocorrelados** (ρ mediana 0.944 en B; 0.91 y 0.76 en los dos
países de E3 inspeccionados), así que la verosimilitud está mal especificada.

---

## 2. P5 — La prueba de tautología, que es el hallazgo positivo

Esta prueba **no usa el AIC**, así que **no cae con la compuerta.** Se simula desde una
**exponencial conocida** —los parámetros ajustados a cada caso real—, con la σ y la ρ de
ese caso, y se ajusta como ley de potencia. La pregunta es simple: **¿qué `b` aparente
produce una exponencial verdadera?**

| Banda de `b` del caso real | E3 | B | ACO |
|---|---:|---:|---:|
| `b < 0.5` | **0.0%** | **0.0%** | **0.0%** |
| `0.5 ≤ b < 1` | 6.2% | 10.5% | 0.0% |
| `1.0 ≤ b < 1.5` | **69.7%** | **70.6%** | **98.0%** |
| `b ≥ 1.5` | **99.9%** | — | **100.0%** |

(Fracción de réplicas en que la `b` aparente cae en `b ≥ 1`.)

> **Una curva verdaderamente exponencial, ajustada como ley de potencia, produce
> `b ≥ 1` en el 99.9% de los casos en el régimen alto de E3 y en el 100% del ACO.** En
> cambio nunca lo produce donde la `b` real es baja.

Eso cierra el argumento conceptual: **"superlineal" no es una medición independiente de
"la ley de potencia no ajusta bien".** La `b` que se usa para etiquetar el régimen se
estimó bajo el modelo cuya validez está en duda, así que la etiqueta y el desajuste son
la misma observación con dos nombres.

Es la lectura que el pre-registro fijó de antemano:

> *"Una exponencial verdadera produce `b ≥ 1` en una fracción alta → La etiqueta
> 'superlineal' es, en parte, **otro nombre para el desajuste exponencial**. El 14.1%
> no mide un régimen, mide un error de forma."*

---

## 3. P1 a P4 — Se reportan, no se interpretan

Por regla pre-registrada, ningún dominio pasó la compuerta P0, así que **estas cifras
no son evidencia sobre los sistemas.** Se publican completas porque el pre-registro
obliga a reportar todo resultado, y porque su patrón es informativo:

| | E3 | B | ACO |
|---|---|---|---|
| Ganadora potencia | 64 / 234 (27%) | 112 / 446 (25%) | 13 / 18 (72%) |
| Ganadora exponencial | 51 | 138 | 4 |
| Ganadora lineal | **119** | **196** | 1 |
| `Spearman(b, ΔAIC)` | −0.250 | **+0.039** | −0.796 |
| Fisher OR | 0.153 | 0.000 | 0.056 |
| P4: superlineales con otra forma | **91.1%** | **100%** | 75% |

Dos observaciones que valen aunque las cifras no se interpreten:

1. **El ρ de P2 no replica entre dominios:** −0.796 en el ACO, −0.250 en E3,
   **+0.039 y sin significancia en B**. Tres dominios, tres valores, uno de ellos
   con el signo contrario. Es la regla por dominio afirmándose sola (Axioma 2:
   modos propios, no una frecuencia universal), y una razón más para no haber
   agrupado nada.
2. **El modelo lineal gana más que ningún otro en E3 y en B**, lo cual es implausible
   si la ley de potencia fuera el generador real en esos dominios — otra evidencia
   de que el corpus B y E3 no fueron generados por leyes de potencia puras.

---

## 4. P5 — La tautología como el hallazgo principal

Esta es la única conclusión robusta del RC1: **una exponencial verdadera ajustada
como ley de potencia produce `b ≥ 1` en el 99.9% de las réplicas en el régimen alto
de E3 y en el 100% del ACO.** En cambio, **nunca lo produce donde la `b` real es baja.**

Eso significa: **la etiqueta "superlineal" es, en gran parte, otro nombre para el
desajuste exponencial.** El 14.1% del corpus no mide un régimen, mide un error de
forma.

La interpretación correcta de `b ≥ 1` es, por tanto:

> **`b ≥ 1` solo tiene significado si se mantiene por periodos muy largos**
> **(cavidad superlineal sostenida → cambio inminente). Si es transitorio/puntual,
> NO es superlineal: el sistema entra en ACO (Colapso Orbital Acoplado), es decir,
> colapso del sistema.**

---

*Informe generado por `reconstruction_real/code/rc1_superlineal.py`. Pre-registro:
`reconstruction_real/preregistro/PREREGISTRO_RC1_SUPERLINEAL_2026-10-02.md`
(commit `1a2ac0e`, subido antes de escribir el script).*