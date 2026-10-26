# Modelo jerárquico de b y nulo por dominios para fricción→b — Resultados

**Fecha:** 2026-10-26
**Preregistro:** [`../preregistro/PREREGISTRO_MODELO_JERARQUICO_2026-10-26.md`](../preregistro/PREREGISTRO_MODELO_JERARQUICO_2026-10-26.md) (commit `4107679`, antes del script).
**Script:** `code/modelo_jerarquico_b.py` (semilla 20261026, N=5 000 permutaciones).
**Salida:** `data/modelo_jerarquico_resumen.csv`.

## Resultados

| Análisis | Resultado |
|---|---|
| A — Réplica caso-nivel | Spearman = **−0.6503** (p = 6.6×10⁻⁸⁸, n = 721) — la aritmética del ancla replica (Axioma 5: −0.68, n=714) |
| B — Nulo por dominios | p_perm = P(ρ* ≤ ρ_obs) = **0.0530** — al borde del umbral, NO distingue la asignación real |
| C — MixedLM b ~ fric + (1\|dominio) | pendiente **−0.2081** (SE 0.3683, **p = 0.572**) |
| D — Por dominio (n=10) | Spearman = **−0.0063** (p = 0.986) — la salvedad del propio Axioma 5, confirmada y más débil |

**Veredicto pre-especificado 2** (el que salió): el ρ caso-nivel no se
distingue de una asignación arbitraria de tiers entre dominios
(p_perm = 0.053) y la pendiente del modelo mixto no es significativa
(p = 0.57). El ancla "ρ = −0.68, p = 2.5×10⁻⁹⁷, n = 714" queda como
**descriptivo del agrupamiento de dominios**, no como medición de fricción.

## Lectura honesta

1. **El p-value del ancla es un artefacto de independencia asumida.** Con
   fricción constante por dominio, los 721 casos no aportan 721 datos
   independientes para el contraste entre tiers: aportan ~10. El modelo
   mixto lo cuantifica: la pendiente (−0.21) sobrevive en magnitud pero su
   SE honesto (0.37) la engulle.
2. **El borde (p_perm = 0.053) no es despreciable.** A diferencia del tono
   φ (p = 0.39, plano), el orden real de tiers está en la cola del nulo —
   hay algo de señal direccional — pero bajo el umbral pre-especificado y
   sin la corroboración del modelo mixto. Se reporta como está: borderline
   que NO pasa la compuerta.
3. **D mata la lectura ecológica con esta codificación:** correlación
   prácticamente cero entre medias de dominio y su tier. El Axioma 5 ya
   viajaba con esa salvedad (p=0.25); con la codificación ordinal
   pre-especificada aquí es aún más plana.
4. **Patrón consistente con el tono φ y la tela:** tercera pieza donde una
   etiqueta constante por dominio no sobrevive el control de estructura
   (tela por tono: p=0.39; fricción→b: p_perm=0.053, MLM p=0.57). La regla
   que emerge: con fricción/tono constantes por dominio, el caso-nivel
   hereda la identidad del dominio — y el dominio, no el campo, es lo que
   la prueba mide.

## Consecuencia para el marco

El Axioma 5 (ANCLADO) merece actualizarse: el ρ caso-nivel se reporta
como descriptivo del agrupamiento con la salvedad de estructura ahora
MEDIDA (p_perm, MLM SE), no solo intuición. Para reclamar fricción como
campo medido se necesita lo mismo que el tono (pendiente 5.5): fricción
**continua por caso** o pre-asignada en dominios no vistos. La fricción
ordinal de la cohorte 2008 (n=6, dentro de un dominio) sigue siendo la
vía operativa más limpia y no la toca esta prueba.

## Cómo regenerar

```sh
python reconstruction_real/code/modelo_jerarquico_b.py   # ~2 s, determinista
```

---

*Fractal Core Research · Tlaxcala, México · 2026-10-26*
