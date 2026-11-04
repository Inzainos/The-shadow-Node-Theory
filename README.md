# Shadow Node Theory — Teoría del Nodo Sombra
## Shadow Node Theory — The Shadow Node Theory

**Versión / Version:** v2.7.5.1  
**DOI Zenodo:** 10.5281/zenodo.23958082  
**Release:** [v2.7.5.1](https://github.com/Inzainos/The-shadow-Node-Theory/releases/tag/v2.7.5.1)

---

## Resumen / Summary

**ES:** Shadow Node Theory estudia la relación relativa entre un hub y un nodo mediante la razón `R(t)=a·t^b`. Incluye la capa de colapso orbital acoplado ACO-A y el campo de fricción φ formalizado en Axioma 0.1. Es un marco de análisis, no una ley universal.

**EN:** Shadow Node Theory studies the relative relationship between a hub and a node via the ratio `R(t)=a·t^b`. It includes the Coupled Orbital Collapse layer ACO-A and the friction field φ formalized in Axiom 0.1. It is an analysis framework, not a universal law.

---

## Marco teórico / Theoretical framework

### Fórmulas centrales / Core formulas
```
R(t) = a · t^b
A(τ) = c · τ^Δ
φ: 𝒞 × T → ℝ⁺ ,  flujo -∇_γ φ
```

### Axioma 0.1 — Campo de fricción
φ es continuo en tiempo, invariante en ≥2 dominios y admite proxies: hazard rate, tiempo a absorción, fricción física.

---

## Casos de uso / Use cases

### 1. Dominio B — Países
- 446 casos, Maddison MPD2020
- `b` indecidible en 290/446 series
- Sin cointegración mayoritaria

### 2. Dominio E3 — Epidémico
- 234 casos, OWID
- 233/234 reproducibles

### 3. Cripto — Eje u
- 60 pares USDT vs BTCUSDT
- D2 mediana 0.800, Spearman emb2/emb3 0.983
- Correlación macro adjunta

Ver `CASOS_DE_USO.md` para detalle.

---

## Hallazgos clave / Key findings
- Eje u operativo con Entropía de Permutación y Dimensión de Correlación pre-registrado
- Campo φ definido formalmente
- Sin evidencia de régimen superlineal general
- ACO-A: convergencia descriptiva ligada a ventanas de evento

---

## Estructura / Structure
- `papers/` — Marco teórico v34
- `figures/` — Figuras publicables
- `legacy/` — Código y datos históricos versionados v2.7.5.1

---

## Scripts / Scripts
- Eje u completo: `legacy/v2.7.5.1/reconstruction_real/code/eje_u_permutacion_dimcor.py`
- Integración macro: `legacy/v2.7.5.1/reconstruction_real/code/eje_u_macro_integracion.py`

---

## Cita / Citation
Ver `CITATION.cff`
