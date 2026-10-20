# Resultados — RC1: el régimen superlineal `b ≥ 1`

**Pre-registro:** [`../preregistro/PREREGISTRO_RC1_SUPERLINEAL_2026-10-02.md`](../preregistro/PREREGISTRO_RC1_SUPERLINEAL_2026-10-02.md)
(commit `1a2ac0e`, subido antes de escribir el script).
**Script:** `code/rc1_superlineal.py` (con log). **Sin descargas.**
**Salidas:** `data/rc1_por_caso.csv`, `data/rc1_calibracion.csv`, `data/rc1_resumen.csv`.

Dos resultados, y conviene separarlos porque uno es un "no se puede saber" y el otro es
un hallazgo positivo:

1. **RC1 no es decidible por AIC** en ninguno de los tres dominios con serie cruda. La
   compuerta pre-registrada lo rechaza en los tres.
2. **La etiqueta `b ≥ 1` queda mostrada como, en gran parte, otro nombre para el
   desajuste** — y eso **sobrevive a la compuerta**, porque no depende del AIC.

---

## Tabla de decisiones, por dominio y sin agrupar

| Punto | E3 (234 casos) | B (446 casos) | ACO (18, control) |
|---|---|---|---|
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
ρ AR(1) de ese mismo caso, 200 réplicas. Todo lo que el AIC elija que no sea "potencia"
es **error por construcción**.

| Banda de `b` | E3 | B | ACO |
|---|---:|---:|---:|
| `b < 0.5` | 14.1% (62 casos) | 40.4% (418) | 16.3% (13) |
| `0.5 ≤ b < 1` | 57.0% (82) | 66.6% (22) | 20.5% (1) |
| `1.0 ≤ b < 1.5` | **88.6%** (57) | **96.8%** (6) | 46.5% (1) |
| `b ≥ 1.5` | 65.9% (33) | — | 49.7% (3) |
| **`b ≥ 1` agregada** | **80.3%** | **96.8%** | **48.9%** |

**El error de selección crece con `b`.** En E3 pasa de 14.1% a 88.6%; en B de 40.4% a
96.8%; en el ACO de 16.3% a ~49%. Es decir: **cuando los datos son una ley de potencia
pura y de exponente alto, el AIC elige otra cosa 8 de cada 10 veces en E3 y casi
siempre en B.**

Eso activa el desenlace que el pre-registro declaró como el más informativo de los seis:

> *"Si además la tasa crece con `b`, se reporta como **el hallazgo del ACO queda
> explicado como artefacto del estimador**, lo cual sería más fuerte que confirmarlo."*

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
"la ley de potencia no ajusta aquí".** La `b` que se usa para etiquetar el régimen se
estimó bajo el modelo cuya validez está en duda, así que la etiqueta y el desajuste son
la misma observación con dos nombres.

Es la lectura que el pre-registro fijó de antemano:

> *"Una exponencial verdadera produce `b ≥ 1` en una fracción alta → La etiqueta
> 'superlineal' es, en parte, **otro nombre para el desajuste exponencial**. El 14.1% no
> mide un régimen, mide un error de forma."*

---

## 3. P1 a P4 — Se reportan, no se interpretan

Por regla pre-registrada, ningún dominio pasó la compuerta, así que **estas cifras no
son evidencia sobre los sistemas.** Se publican completas porque el pre-registro obliga
a reportar todo resultado, y porque su patrón es informativo sobre el estimador.

| | E3 | B | ACO |
|---|---|---|---|
| Gana potencia | 64 / 234 (27%) | 112 / 446 (25%) | 13 / 18 (72%) |
| Gana exponencial | 51 | 138 | 4 |
| Gana lineal | **119** | **196** | 1 |
| `Spearman(b, ΔAIC)` | −0.250 | **+0.039** | −0.796 |
| Fisher OR | 0.153 | 0.000 | 0.056 |
| P4: superlineales con otra forma | **91.1%** | **100%** | 75% |

Dos observaciones que valen aunque las cifras no se interpreten:

1. **El ρ de P2 no replica entre dominios:** −0.796 en el ACO, −0.250 en E3, **+0.039 y
   sin significancia en B**. Tres dominios, tres valores, uno de ellos con el signo
   contrario. Es la regla por dominio afirmándose sola (Axioma 2: modos propios, no una
   frecuencia universal), y una razón más para no haber agrupado nada.
2. **El modelo lineal gana más que ningún otro en E3 y en B**, lo cual es implausible
   como hallazgo de forma —una recta no describe una curva epidémica acumulada— y
   encaja con el efecto de escala del AIC crudo que P0 cuantifica.

---

## 4. Qué significa para la SNT

| Afirmación | Estado anterior | Estado ahora |
|---|---|---|
| **RC1**: la potencia no ajusta mejor que lineal/exponencial en todos los dominios | NOT REFUTED sobre una prueba (18 series ACO) | **No decidible por AIC** en los tres dominios con serie cruda. El estatus NOT REFUTED **no se sostiene sobre esa prueba**, porque la prueba no tiene validez a `b` alta |
| El hallazgo de la v32: "a mayor `b`, peor ajusta la potencia" (ρ = −0.796) | Hallazgo nuevo de la auditoría | **Explicado como artefacto del estimador.** Es lo que el AIC produce aunque todo sea potencia pura |
| La banda `b > 1` = *"Satelización rápida sin fricción / Roche Radius"* | Etiqueta de régimen físico, 14.1% del corpus | **Sin respaldo como régimen.** Una exponencial verdadera produce `b ≥ 1` en 99.9% / 100% en las bandas altas. La etiqueta y el desajuste son la misma observación |
| El 14.1% (102 de 721 casos) | Contado como régimen | **No es un conteo de régimen.** Es, en gran parte, un conteo de casos donde la forma funcional elegida no ajusta |
| La `b` de los casos superlineales | Estimada y publicada | **Se estimó bajo el modelo en duda.** Sigue siendo reproducible como número; deja de ser interpretable como exponente de un régimen |
| Ortogonalidad b ⊥ Δ, gradiente de Tlaxcala, los cinco modos de colapso | Vigentes | **Sin cambio.** Esta prueba no los toca |

**Lo que se cae es una etiqueta, no una medición.** Las 721 `b` del corpus siguen siendo
ajustes reproducibles. Lo que no se puede hacer con ellas es **leer `b ≥ 1` como un
régimen físico**, porque ese umbral no distingue "satelización rápida" de "aquí la ley
de potencia no era el modelo".

Es la sexta vez que aparece el mismo patrón en este repositorio —el 5.9×, el ROC-AUC
filtrado, la precisión del ASI, el apego preferencial de N-cuerpos, la inferencia del
Dominio B, y ahora el régimen superlineal—: **la aritmética estaba bien, la
interpretación no.**

### Qué haría falta para reabrir RC1

En orden de viabilidad:

1. **Cambiar el criterio, no el modelo:** comparar las tres formas con una verosimilitud
   que modele la autocorrelación (AIC sobre un AR(1) ajustado, o validación cruzada
   fuera de muestra por bloques). La compuerta de este informe es el banco donde ese
   criterio tendría que pasar primero.
2. **Comparar en la escala correcta:** el AIC crudo favorece lo que sigue los valores
   grandes. Un criterio sobre residuos logarítmicos daría otra respuesta y habría que
   calibrarlo igual.
3. **Reemplazar la etiqueta por una medición independiente:** si "satelización rápida
   sin fricción" es un régimen real, debe tener un observable que **no** sea la `b`
   estimada bajo la ley de potencia. Mientras ese observable no exista, la banda es
   descriptiva.

---

## Desviaciones respecto al pre-registro

**Ninguna de fondo.** Se corrió lo pre-registrado, con los parámetros fijados:
`N_CAL = 200` réplicas, umbral de admisión 20% en la banda `b ≥ 1`, pruebas de una cola
en P2 y P3 con la dirección fijada por el ACO, semilla `20261002`, bandas de `b` tal
como se declararon, y la regla por dominio respetada sin agrupar ni ordenar.

Tres notas de ejecución, por transparencia:

1. **E3 reprodujo 233 de 234** y no 234, igual que en la identificación de la receta del
   2026-09-27. El caso discrepante entra al análisis; con 1 de 234 no cambia nada y
   excluirlo sería un recorte no pre-registrado.
2. **La banda `b ≥ 1.5` no existe en B** (su `b` máxima entre los superlineales queda
   bajo 1.5), así que la tabla de B tiene una fila menos. No es una exclusión.
3. **El ACO entró como control y también quedó no interpretable.** Eso no estaba
   anticipado como tal —se esperaba que reprodujera 13/4/1, y lo hizo—, pero su propia
   calibración lo descalifica con 48.9% de error en `b ≥ 1`. Se reporta así: el control
   reproduce la cifra y, al mismo tiempo, muestra que la cifra no significaba lo que se
   creyó.

## Validación

- **Reproducción previa:** E3 233/234 (±0.01), B 446/446 (±1e-4), ACO **13/4/1 exacto**,
  idéntico a `AUDITORIA_INTEGRAL_v32.md`.
- **Dirección del detector:** en las bandas `b < 0.5`, donde la ley de potencia sí es el
  modelo, el error de P0 baja a 14.1% / 40.4% / 16.3% y el falso `b ≥ 1` de P5 es
  **0.0% en los tres dominios**. El procedimiento no inventa el efecto donde no lo hay.
- **Corrección previa:** la ρ de la v32 estaba tecleada con el signo invertido en la
  prosa del informe; corregida y verificada antes de pre-registrar (ver
  `AUDITORIA_INTEGRAL_v32.md`, nota del 2026-10-02).

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
