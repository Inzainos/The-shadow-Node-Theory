# Tela de Incertidumbre — Implementación del Axioma 0.1 (marco v34)

**Fecha:** 2026-10-21
**Script:** `code/tela_de_incertidumbre.py`
**Salida:** `data/tela_de_incertidumbre.csv` (7,306 puntos)
**Fuente teórica:** `papers/marco_teorico.md` Axioma 0.1 (líneas 97-118) y Axioma 0.2 (líneas 120-145)

## Qué es

El cubo de incertidumbre 𝒞(u, m, τ) es el volumen de estados por el que un
sistema transita antes, durante y después del colapso. El Axioma 0.1 del
marco teórico v34 lo define con tres ejes:

| Eje | Definición v34 | Estado |
|-----|-----------------|--------|
| `m` | **R** con el proxy declarado de cada dominio (la razón medida) | DEFINIDO en todos los dominios |
| `τ` | fase temporal normalizada (sobre la que opera `h(τ)`) | DEFINIDO en todos los dominios |
| `u` | apertura de posibilidades / incertidumbre | **NO DEFINIDO en ningún dominio** — NULL |

El volumen opera en **(m, τ)** mientras `u` pende de definición operativa.
La regla de admisión (v34:114) es: un eje entra a 𝒞 con definición
operativa en dos dominios o más; con uno solo es etiqueta, no coordenada.

El campo de fricción `φ` es un **campo escalar postulado** sobre el volumen
(categórico por dominio, no medido). La sombra de cada caso es la proyección
`Π_θ(𝒞)` con marco de medición `θ = (B, V, ρ, W, λ)` declarado.

## Correcciones aplicadas (2026-10-21)

La implementación anterior tenía **tres errores fundamentales** contra el
marco, corregidos en el commit `cbdeec6`:

| Eje | Marco v34 exige | Antes (erróneo) | Ahora |
|-----|-----------------|-----------------|-------|
| `m` | `R` (la razón) | `\|b\|/2` (el exponente) | `R` — cada punto tiene su valor de razón |
| `τ` | fase temporal normalizada | `n_eff/n` | `(t−t_min)/(t_max−t_min)` ∈ [0,1] |
| `u` | NO DEFINIDO | inventaba fórmula con ρ, n_eff, se_b | `NULL` — 0/7306 puntos |

## Datos en la tela

| Fuente | Casos | Puntos | Descripción |
|--------|-------|--------|-------------|
| **Serie cruda ACO** | 18 | 109 | (t, R) reales de `snt_corpus_aco_timeseries_v29.csv` |
| **Sombra modelo ajustado** | 703 | 7,197 | R=a·t^b con a=1 relativa, t=1..n, 10 puntos por caso |
| **Total** | 721 | **7,306** | |

Los puntos de dominios sin serie cruda son **sombras** del modelo ajustado,
no datos crudos — el Axioma 0.2 permite sombras: "una sombra es válida y
parcial a la vez". Solo ACO tiene serie (t,R) real versionada.

## Marco de medición θ

```
B = (m, τ)                    — base de observación
V = R crudo (ACO) / R ajustado a·t^b (otros) — selección de variables
ρ = 1 punto por dato (ACO) / 10 por caso (otros) — resolución
W = ventana completa del caso — ventana temporal
λ = sin corte — umbral
```

## Fricción φ (postulada)

Categórica por dominio (los 11 del README), NO medida:

| Dominio | φ |
|---------|---|
| A (ciudades) | media |
| B (países) | alta |
| C (estados EEUU) | alta |
| D (HackerEarth) | nula |
| E1 (expansión territorial) | nula |
| E2 (biológico) | alta |
| E3 (epidémico) | nula |
| F (planetario) | física |
| ACO (colapso) | variable (regulado/craquelado/etc.) |

## Cómo usar

```bash
python reconstruction_real/code/tela_de_incertidumbre.py
```

Produce `data/tela_de_incertidumbre.csv` con columnas:
`id, dominio, fuente, t, R, m, tau, u, phi_friccion, theta_B, theta_V`

## Pendientes declarados

1. Eje `u` sin definición operativa en ningún dominio (marco v34:112).
2. Campo `φ` postulado, no medido (marco v34:118).
3. Solo ACO (18/721 casos) tiene serie cruda (t,R) — los demás dominios
   aportan sombras del modelo ajustado, no datos crudos.
4. Invarianza de proyección (v34:141) no verificada — requiere dos θ
   independientes y comparar formas.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-21*