# PREREGISTRO — Modelo jerárquico de b y nulo de permutación por dominios para fricción→b

**Fecha:** 2026-10-26 · **Committeado ANTES del script, los datos y los
resultados.** **Origen:** pendiente 5.3 de `PENDIENTES_SNT.md`.

---

## Pregunta

El Axioma 5 ancla "Fricción → b: Spearman ρ = −0.68, p = 2.5×10⁻⁹⁷, n = 714"
con dos salvedades propias: por dominio p = 0.25, y n mediano efectivo 2.2 en
B. La fricción es **constante por dominio** (tier categórico), así que la
asociación caso-nivel hereda exactamente la estructura que el test del tono φ
(TELA_CLASIFICACION_BASELINE) voló: cualquier agrupamiento de dominios puede
producir lo mismo. ¿Sobrevive el ancla a (a) un nulo de permutación de la
asignación tier→dominio y (b) un modelo mixto con interceptos por dominio?

## Receta exacta (fijada antes de correr)

- **Datos:** `snt_corpus_REAL_v6.csv` (721 casos), columna `b`; casos sin b
  excluidos. Dominio por caso. n esperado ≈ 714.
- **Codificación de fricción por dominio (ordinal, pre-especificada):**
  `nula=1` (D, E1, E3) · `media=2` (A) · `alta=3` (B, C, E2) ·
  `fisica=4` (F1, F2, F3). Es el mismo mapeo declarado de la tela.
- **A — Réplica caso-nivel:** Spearman(fricción_tier, b) sobre los casos con
  b. Referencia: si difiere de −0.68, se reporta la cifra propia y la
  discrepancia NO se reconcilia a la fuerza (el −0.68 original no tiene
  script versionado que lo recalcule).
- **B — Nulo por dominios (el corazón):** permutar la asignación
  tier→dominio entre los 10 dominios (manteniendo la fricción constante
  dentro de dominio y los tamaños de tier), N = 5 000 permutaciones, semilla
  20261026, `numpy.random.default_rng`. Por permutación: Spearman caso-nivel
  con el tier permutado. **p_perm = P(ρ* ≤ ρ_obs)** (una cola inferior — el
  ancla es negativo).
- **C — Modelo mixto:** `MixedLM: b ~ fric + (1|dominio)` (statsmodels),
  pendiente de fricción con interceptos por dominio (partial pooling).
  Se reportan la pendiente, su SE y su p.
- **D — Por dominio (réplica de la salvedad):** Spearman de medias de b por
  dominio contra su tier (n = 10).

## Veredictos pre-especificados

1. **p_perm < 0.05 Y pendiente MixedLM significativa (p < 0.05)** → la
   asociación sobrevive al control de estructura: se reporta con su SE
   honesto y la nota de que es entre-dominios por construcción.
2. **p_perm ≥ 0.05** → "el ρ caso-nivel no se distingue de una asignación
   arbitraria de tiers entre dominios" — mismo veredicto que el tono φ: el
   ancla queda como descriptivo del agrupamiento, no como medición de
   fricción. Se reporta SIEMPRE la pendiente MixedLM con su SE.
3. La réplica D se reporta siempre como descriptiva; no se agrupa entre
   dominios (regla del repo).

## Qué NO afirma esta prueba

- No mide fricción continua por caso (no existe); prueba el AGRUPAMIENTO
  declarado, no el campo φ del marco (que sigue postulado).
- No toca la fricción ordinal de la cohorte 2008 (n=6, otra vía).
- No "salva" ni "mata" el Axioma 5: acota qué puede reclamar el ancla.

## Salidas

- Script: `reconstruction_real/code/modelo_jerarquico_b.py`
  (semilla 20261026, determinista).
- Datos: `reconstruction_real/data/modelo_jerarquico_resumen.csv`.
- Informe: `reconstruction_real/audits/MODELO_JERARQUICO_B_2026-10-26.md`.
