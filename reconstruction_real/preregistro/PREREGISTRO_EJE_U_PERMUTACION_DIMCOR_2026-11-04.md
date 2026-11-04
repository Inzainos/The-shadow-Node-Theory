# Pre-registro — eje `u`: Entropía de Permutación para series cortas y Dimensión de Correlación para series largas

**Fecha:** 2026-11-04 · **Rama:** `fix/pendientes-2.7.5` · **Base:** `fix/pendientes-2.7.4` en `e185643` · **Autor de la teoría:** Elán Zainos Corona · **Análisis:** Copilot, a pedido del autor

Este documento se compromete antes de calcular cualquier métrica de `u`. El commit fechado fija el diseño. Cualquier cambio posterior se anota en **Desviaciones** del informe de resultados.

## 0. El pendiente, exactamente

El Axioma 0.1 define `𝒞(u, m, τ)`, donde `u` es apertura de posibilidades o incertidumbre. `m` está definido como `R` con proxy declarado. `τ` está definido como fase temporal normalizada. `u` no tiene definición operativa en ningún dominio.

El candidato anterior `u^H` (entropía condicional de transiciones) falló la compuerta de invarianza en ambos dominios: Dominio B mediana Spearman θ1/θ2 = -0.065, Cripto = 0.076; ambos <0.60 requerido.

Este pre-registro prueba dos candidatos acotados, uno por régimen de longitud de serie:
- **Series cortas (Dominio B)**: `u^PE(t)` = Entropía de Permutación normalizada de orden `m=3`.
- **Series largas (Cripto)**: `u^D2(t)` = Dimensión de Correlación local estimada en ventana deslizante.

No se propone relación direccional entre `u` y `m, τ, b, Δ, φ`.

## 0.1 Ceguera declarada

El analista revisó esquemas de archivos, rutas y cargadores existentes. No calculó ni inspeccionó valores, resúmenes, gráficos, correlaciones o trayectorias de `u^PE` o `u^D2`.

## 0.2 Reglas generales

1. Se reporta todo resultado, incluida no admisión.
2. Sin descargas. Solo archivos versionados al momento de este commit.
3. Sin imputación. Series cortas con <20 puntos quedan fuera con motivo.
4. Sin aleatoriedad. Cálculo determinista.
5. Por dominio. No se promedian dominios.
6. Proyección explícita `θ = (B, V, ρ, W, λ)` como exige Axioma 0.2.
7. Log obligatorio en `reconstruction_real/logs/` con SHA-256 de entradas/salidas.

## 1. Dominios y datos fijados

| Dominio | Casos | `R(t)` | Archivos fijados | Inclusión mínima |
|---|---:|---|---|---|
| **B — pares de países** | pares publicados | PIBpc_hub / PIBpc_nodo | `data/maddison_mpd2020.csv`, `reconstruction_real/data/by_domain/dominio_B_real.csv` | 40 años comunes 1900-2018 |
| **Cripto — moneda/BTC** | pares Binance | cierre_moneda / cierre_BTCUSDT | `data/binance_cierres_diarios.csv.gz` | 200 días comunes con BTCUSDT |

## 2. Construcción de candidatos

### 2.1 Dominio B — `u^PE(t)`, Entropía de Permutación

Para cada serie elegible:
```
x_t = log(R_t)
```
Proyección primaria `θ1`:
- `B`: serie `R(t)`
- `V`: `x_t`
- `ρ`: patrones ordinales de orden `m=3` con `τ=1`
- `W`: ventana deslizante de 20 observaciones
- `λ`: se requiere ventana completa

Entropía de Permutación normalizada:
- `PE_t = - Σ p(π) log p(π) / log(6)`
- `u^PE_t = exp(PE_t * log(6))` = número efectivo de patrones

Proyección de invarianza `θ2`:
- `m=4` (6 patrones para m=3, 24 para m=4)
- Misma ventana `W=20`

### 2.2 Dominio Cripto — `u^D2(t)`, Dimensión de Correlación local

Para cada serie elegible:
```
x_t = log(R_t)
```
Proyección primaria `θ1`:
- `B`: serie `R(t)`
- `V`: `x_t` embedido con demora 1, dimensión 2
- `ρ`: radio `r` = 0.1 × desviación estándar de la ventana
- `W`: ventana deslizante de 200 observaciones
- `λ`: se requieren ≥150 puntos válidos

Estimación:
- `C(r) = (2/(N(N-1))) Σ_{i<j} I(||X_i - X_j|| < r)`
- `D2_t = d log C(r) / d log r` estimado por regresión lineal en rango [0.05σ, 0.3σ]
- `u^D2_t = exp(D2_t)` (número efectivo de grados de libertad)

Proyección de invarianza `θ2`:
- Dimensión de embedding = 3 (en lugar de 2)
- Mismo radio `r`

## 3. Compuertas de admisión

Aplicadas por separado en B y Cripto.

**A. Cobertura**
- Dominio B: ≥30 casos con ≥40 puntos y proyecciones θ1/θ2 convergentes.
- Dominio Cripto: ≥30 casos con ≥200 puntos y proyecciones θ1/θ2 convergentes.

**B. Invarianza de proyección**
- Spearman entre `u` θ1 y `u` θ2 por caso.
- Dominio pasa si mediana ≥0.60 y ≥2/3 casos con ρ ≥0.30.
- ≥90% casos evaluables.

**C. Variación efectiva**
- IQR de `u_t` bajo θ1 por caso.
- Dominio pasa si mediana IQR ≥0.05.

**D. No colapso a magnitud/dispersión**
- `m_t = x_t`, `v_t` = MAD de ventana.
- `|Spearman(u_t, m_t)|` y `|Spearman(u_t, v_t)|` por caso.
- Dominio falla si ≥75% casos con |ρ| ≥0.90.

## 4. Decisión pre-especificada

| Resultado | Decisión |
|---|---|
| B y Cripto pasan A–D | `u` admitido como definición operativa candidata en dos dominios |
| Solo un dominio pasa A–D | `u` descriptor de ese dominio; no entra a `𝒞` |
| Ningún dominio pasa | Eje `u` sigue sin definición operativa |
| Colapso a `m` o `v` | Se rechaza interpretación de apertura de posibilidades |

## 5. Salidas previstas

- `reconstruction_real/code/eje_u_permutacion_dimcor.py` con log y sin red.
- `reconstruction_real/data/eje_u_permutacion_dimcor_por_caso.csv`
- `reconstruction_real/data/eje_u_permutacion_dimcor_resumen.csv`
- `reconstruction_real/audits/RESULTADOS_EJE_U_PERMUTACION_DIMCOR_2026-11-04.md`

---

*Fractal Core Research · Tlaxcala, México · 2026-11-04*
