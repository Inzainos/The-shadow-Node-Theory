# Pre-registro — RC1: ¿el régimen superlineal `b ≥ 1` es un régimen o es mala especificación?

**Fecha:** 2026-10-02 · **Rama:** `claude/charming-brown-w9h8iu` · **Base:** `main` en `676adf4`
· **Autor de la teoría:** Elán Zainos Corona · **Análisis:** Claude Code, a pedido del autor.

## 0. El pendiente

**RC1**, tal como lo enuncia el README: *"Power law fits no better than
linear/exponential **across all domains**"*. Está marcado **NOT REFUTED** sobre una
sola prueba, hecha en la auditoría v32 sobre las **18 series crudas del ACO** —las
únicas que había entonces—, y el propio README anota: *"Other domains untested (raw
series absent)"*.

Lo que esa única prueba encontró, reproducido hoy caso por caso:

| Modelo ganador por AIC | n | b medio | rango de b |
|---|---:|---:|---|
| potencia | 13 | +0.324 | [+0.009, +1.244] |
| **exponencial** | **4** | **+1.541** | [+0.349, +2.195] |
| lineal | 1 | +0.453 | — |

`Spearman(b, ΔAIC_potencia) = −0.796, p = 0.0001` · `Fisher (b≥1 × gana potencia):
OR = 0.056, p = 0.0441` — **3 de 4 casos superlineales ajustan mejor con exponencial.**

Con la convención de `comparar_modelos` (`ΔAIC_potencia = AIC_mejor_otro −
AIC_potencia`, **positivo = gana la potencia**), el signo negativo significa: **a mayor
`b`, peor ajusta la ley de potencia.**

**La consecuencia que esto abre:** la banda de clasificación de `snt_utils.py` que
etiqueta `b > 1` como *"Satelización rápida sin fricción / Roche Radius"* podría estar
llamando **régimen físico** a lo que es **mala especificación de modelo** — curvas
exponenciales forzadas a ley de potencia. El corpus reporta
**`pct_b_super = 14.1%`, 102 de 721 casos.**

### Corrección de una cifra previa, hecha antes de este pre-registro

La prosa de `audits/AUDITORIA_INTEGRAL_v32.md` tecleaba `rho = +0.657`. El runner
(`code/snt_auditoria_integral_v32.py:209`) siempre registró `−0.657`, el CSV de salida
lo marca `REPLICA_SIGNO`, y la tabla y la conclusión de esa sección siempre apuntaron
en la dirección negativa. Corregido, con la verificación anotada. Las otras cinco
cifras del bloque reproducen exactas.

## 0.1 La regla por dominio, aplicada desde el diseño

El marco establece que **cada dominio tiene sus propios valores, y cada área dentro de
un dominio también, y cada una es independiente** — Axioma 0.1
(`papers/marco_teorico.md:110`): *"obliga a que cada eje tenga definición operativa por
dominio... no entra en ningún ajuste para ese dominio"*; Axioma 2
(`papers/marco_teorico.md:163`): *"modos propios, no con una frecuencia universal
idéntica para todo"*.

Este diseño la respeta así, y queda fijado aquí:

- **Cada dominio se prueba por separado**, con su serie cruda y su propio proxy.
- **RC1 es una afirmación universal** (*"across all domains"*), así que un contraejemplo
  en un dominio la refuta. Eso es lógica, no agrupamiento.
- Los resultados se **cuentan por dominio**, nunca se agrupan en un estadístico único.
- **No hay ordenamiento entre dominios**, ni escala de fricción, ni se lee la diferencia
  entre dominios como medición de nada. Ése fue el error del 2026-10-02 que el autor
  detuvo (`audits/AUDITORIA_REGLA_POR_DOMINIO_2026-10-02.md`).

## 0.2 Ceguera: **parcial**. Declarada

- **Visto:** todas las cifras del ACO de arriba, incluida la ρ recomputada hoy. Los
  conteos de superlineales por dominio (E3 90/234, B 6/446, E1 4/4, F2 1, F3 1). La
  receta de E3 y su tasa de reproducción (233/234). El Durbin-Watson de dos países de
  E3. La convención de signo de `comparar_modelos`.
- **No visto, y no existe en el repositorio:** ningún resultado de AIC sobre E3 ni
  sobre B, y ninguna calibración del AIC bajo autocorrelación en ningún dominio.

## 0.3 Reglas generales

1. **Se reporta todo resultado**, por dominio, favorable o no.
2. **α = 0.05.** Las pruebas de P2 y P3 son **de una cola**, porque la dirección la fija
   el resultado previo del ACO; eso se declara aquí y no se cambia después.
3. **Semilla fija:** `20261002`.
4. **Log obligatorio.**
5. **Sin descargas.** Todo sale de archivos versionados.
6. **Nada se recorta por su valor.** Las exclusiones son por falta de serie cruda o por
   n insuficiente, y se cuentan.

---

## 1. Dominios, y qué se puede y qué no

| Dominio | Casos | Superlineales `b ≥ 1` | Serie cruda | Papel |
|---|---:|---:|---|---|
| **E3** (COVID-19 por país) | 234 | **90 (38.5%)** | `data/owid_covid_casos_totales.csv.gz`, versionado | **Primario** |
| **B** (pares de países) | 446 | 6 (1.3%) | `data/maddison_mpd2020.csv`, versionado | Secundario |
| **ACO** | 18 | 4 | `data/snt_corpus_aco_timeseries_v29.csv` | **Control / reproducción** |
| E1 (COVID-19, otra fase) | 4 | **4 (100%)** | **ausente** — declarado no reproducible el 2026-09-27 | **Excluido y contado** |
| F2, F3 | 1 y 1 | 1 y 1 | ausente, n = 1 | **Excluidos y contados** |

**Cobertura: 96 de los 102 casos superlineales del corpus (94%)** quedan testeables.
Los 6 restantes se reportan como no testeables, con su motivo.

### Construcción de las series, fijada aquí

- **E3:** receta ya identificada y verificada el 2026-09-27 — casos **acumulados**,
  ventana que arranca en el primer día con **≥ 100 casos acumulados**, **60 días**,
  `t = 1..60`. Reproduce la `b` publicada en **233 de 234** países dentro de ±0.01. Se
  vuelve a verificar antes de probar nada; si no reproduce, el análisis se detiene.
- **B:** exactamente como `calc()` de `expand_B_massive.py` — años comunes 1900–2018,
  `t = 1..n`. Se verifica contra la `b` publicada con |Δ| ≤ 1×10⁻⁴.
- **ACO:** las 18 series de `snt_corpus_aco_timeseries_v29.csv` tal cual.
  **Advertencia declarada:** el ACO mide el exponente de **absorción**
  (`R` = masa del absorbedor / pico del hub que colapsa), **no** el de satelización. Es
  otro eje, y por eso entra como control de reproducción y no como evidencia sobre el
  `b` del corpus.

---

## 2. P0 — La compuerta: ¿es el AIC válido aquí?

**Esto es lo primero y lo decide todo.** `comparar_modelos` compara AIC calculado sobre
residuos crudos suponiendo independencia. Los residuos de estos dominios **no son
independientes**: en E3 el `dw` de los dos países inspeccionados daba 0.18 y 0.47
(ρ AR(1) 0.91 y 0.76), y en B la ρ mediana es 0.944. Con residuos autocorrelados la
verosimilitud está mal especificada y **el AIC puede elegir el modelo que mejor sigue
el vagabundeo del ruido, no el que generó los datos.**

**Calibración, por dominio.** Para cada caso real se simulan series desde una **ley de
potencia conocida** —la `b` estimada de ese caso—, con la σ y la ρ AR(1) de ese mismo
caso y su misma n. Todo lo que el AIC elija que no sea "potencia" es un **error de
selección por construcción**. `N_CAL = 200` réplicas por caso.

**Se reporta la tasa de error de selección por banda de `b`**, porque la pregunta no es
solo cuánto se equivoca, sino **si se equivoca más cuando `b` crece** — que es
exactamente el patrón que el hallazgo del ACO interpreta como físico.

### Regla de admisión, fijada aquí

El conteo de P1 y las pruebas P2–P4 de un dominio **se interpretan solo si** su tasa de
error de selección en la banda **`b ≥ 1`** es **< 20%**.

- Si la tasa es ≥ 20% en esa banda, el dominio se reporta como **no interpretable**, y
  se dice que el AIC sobre residuos autocorrelados no puede decidir RC1 ahí. Eso es un
  resultado, no un fracaso.
- Si además la tasa **crece con `b`**, se reporta como **el hallazgo del ACO queda
  explicado como artefacto del estimador**, lo cual sería más fuerte que confirmarlo.

---

## 3. P1 a P4 — Las pruebas, por dominio

- **P1. Conteo de ganadores.** `comparar_modelos` por caso: potencia / exponencial /
  lineal, contado **por dominio**. Nunca agrupado.
- **P2. `Spearman(b, ΔAIC_potencia)`** dentro de cada dominio. **Predicción: negativa**
  —a mayor `b`, peor ajusta la potencia—, una cola, dirección fijada por el ACO.
- **P3. Fisher exacto** de (`b ≥ 1`) × (gana la potencia) dentro de cada dominio.
  **Predicción: OR < 1**, una cola.
- **P4. La cifra que cierra el pendiente:** de los casos **superlineales** de cada
  dominio, **qué fracción ajusta mejor con exponencial o lineal**. Es el número que dice
  si la etiqueta del 14.1% está leyendo mala especificación como régimen.

---

## 4. P5 — La prueba de tautología, que es el corazón conceptual

Hay un confundido que, si no se mide, vuelve circular todo lo anterior: **una curva
verdaderamente exponencial, ajustada como ley de potencia, produce una `b` aparente
grande.** Entonces "los ganadores de la exponencial tienen `b` alta" puede ser
**verdadero por construcción**, porque esa `b` se estimó bajo el modelo equivocado.

**Prueba.** Para cada caso real se simula desde una **exponencial conocida** —calibrada
al rango de la serie real—, con la σ y la ρ de ese caso y su misma n, y se ajusta como
ley de potencia. **Se reporta la distribución de la `b` aparente, y qué fracción cae en
`b ≥ 1`.**

| Resultado | Lectura |
|---|---|
| Una exponencial verdadera produce `b ≥ 1` en una fracción alta | La etiqueta "superlineal" es, en parte, **otro nombre para el desajuste exponencial**. El 14.1% no mide un régimen, mide un error de forma |
| Produce `b ≥ 1` en una fracción baja | `b ≥ 1` **no** es un simple renombre, y el hallazgo del ACO sí apunta a algo de los sistemas |

---

## 5. Qué significa cada desenlace

Escrito **antes** de ver cualquier resultado.

| Desenlace | Lectura |
|---|---|
| En E3, la mayoría de los superlineales gana con exponencial, con P0 admisible | **El 14.1% del corpus es, en su mayor parte, mala especificación.** La banda "Roche Radius" de `snt_utils.py` deja de ser una etiqueta de régimen |
| En E3 la potencia gana también entre los superlineales, con P0 admisible | **RC1 aguanta en E3** y el hallazgo del ACO **no generaliza**: era propio de las 18 series de absorción |
| P0 inadmisible en E3 (error de selección ≥ 20% con `b ≥ 1`) | **RC1 no es decidible por AIC** en residuos como los de E3. El pendiente se cierra como indecidible y la etiqueta del 14.1% queda sin respaldo **y sin refutación** |
| La tasa de error de P0 **crece con `b`** | El hallazgo del ACO queda **explicado como artefacto del estimador**. Es el desenlace más informativo de todos |
| E3 y B discrepan | Se reportan **los dos por separado**, sin promediar ni ordenar: es lo que la regla por dominio predice y no un problema que haya que resolver |
| El ACO no reproduce 13/4/1 | Hay un defecto en la tubería y el análisis se detiene |

**Lo que este pre-registro NO hace.** No reestima ninguna `b` publicada, no modifica el
corpus, no toca la ortogonalidad b ⊥ Δ, el gradiente de Tlaxcala ni la capa ACO-A, y
**no compara dominios entre sí** en ningún sentido que no sea contar sus resultados
independientes.

---

## 6. Salidas previstas

- `reconstruction_real/code/rc1_superlineal.py` (con log).
- `reconstruction_real/data/rc1_por_caso.csv` — una fila por caso: dominio, `b`, AIC de
  los tres modelos, ganador, `ΔAIC_potencia`, `dw`, ρ AR(1).
- `reconstruction_real/data/rc1_calibracion.csv` — P0 y P5 por dominio y banda de `b`.
- `reconstruction_real/audits/RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md`, con la tabla
  hipótesis → resultado → decisión **por dominio** y la sección **Desviaciones**.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
