# φ como Atractor Teórico del Algoritmo de Satelización
## Hipótesis Deductiva — SNT v2.3.1 | Estado: REFUTADA (3 validaciones independientes)

---

## 1. El argumento matemático

La razón áurea φ = (1 + √5) / 2 ≈ 1.6180 satisface la ecuación algebraica:

    φ² = φ + 1

Esta propiedad la distingue de cualquier otra constante: es la única proporción
donde el cuadrado es igual al número más uno. En términos dinámicos, φ es la
solución al problema de crecimiento autorreferente bajo dos restricciones
acopladas de la forma:

    Xₙ = Xₙ₋₁ + Xₙ₋₂

Cualquier proceso donde el estado presente depende de los dos estados anteriores
converge a φ como razón de crecimiento, independientemente de los valores
iniciales. La sucesión de Fibonacci es el caso entero más conocido, pero el
patrón es general: es la dinámica de cualquier sistema donde el presente es la
suma del pasado inmediato y el anterior.

---

## 2. La conexión con el mecanismo SNT

El algoritmo de satelización SNT opera mediante preferential attachment: el
nodo que ya tiene ventaja acumulada atrae más recursos. Matemáticamente:

    ΔR/Δt ∝ R(t)

Bajo esta dinámica, el sistema tiene una restricción de crecimiento (la masa
acumulada del hub) y una restricción de regeneración (la energía residual del
nodo satélite que sustenta la extracción). Dos restricciones acopladas.

Si el mecanismo de preferential attachment opera bajo exactamente esas dos
restricciones, el atractor matemático del sistema debería ser φ. No porque la
naturaleza "conozca" φ, sino porque cualquier proceso de optimización iterativa
bajo dos restricciones acopladas lo descubrirá inevitablemente.

---

## 3. Hipótesis formal

**H-φ:** En sistemas donde el mecanismo de satelización opera sin fricción
institucional y bajo exactamente dos restricciones acopladas, el exponente b
de la ley de potencia R(t) = a·t^b converge hacia φ como límite teórico
superior. Los sistemas con fricción institucional parcial producen exponentes
que son fracciones racionales de φ proporcionales al grado de fricción.

Predicción específica y falsificable:

> En un corpus nuevo de n ≥ 30 casos de invasión biológica con datos de
> series temporales directamente extraídos de fuentes primarias, más del
> 60% de los exponentes b positivos deberán caer dentro de ±0.10 de
> alguna fracción racional de φ del conjunto {φ/4, φ/3, φ/2, 2φ/3, 3φ/4, φ}.
> Si el porcentaje observado no supera significativamente el porcentaje
> esperado por azar (test Mann-Whitney, α = 0.05), la hipótesis queda
> refutada.

---

## 4. Por qué φ y no otro número

φ es el número irracional de más difícil aproximación racional — requiere la
secuencia más lenta posible de fracciones continuas (precisamente los cocientes
de Fibonacci). En sistemas dinámicos, esto se traduce en máxima resistencia a
la resonancia destructiva.

Los sistemas que deben crecer sin entrar en resonancia — plantas distribuyendo
hojas, galaxias formando brazos espirales, nodos acumulando ventaja sin
destruir al satélite que los sustenta — convergen a φ porque minimiza las
interferencias internas. Es la solución al problema de partición óptima entre
el presente y el pasado inmediato.

---

## 5. Limitaciones explícitas

Esta hipótesis es deductiva. Los análisis exploratorios del corpus mostraron
señales consistentes con H-φ en dominios biológicos (E3, p < 0.001), pero esos
tests fueron post-hoc sobre el mismo corpus usado para construir la teoría.

---

## 6. RESULTADOS DE VALIDACIÓN INDEPENDIENTE (Mayo 2026)

### Ronda 1 — Datos Crypto (BTC/Altcoin)

Métrica: R(t) = Marketcap_BTC / Marketcap_altcoin  
Modelo: ley de potencia log-log | Permutation test N=2,000 | Tolerancia ±0.10

| Par       | b observado | R²    | Dist. a φ | p perm. | Confirmada |
|-----------|-------------|-------|-----------|---------|------------|
| BTC/ETH   | −0.6123     | 0.454 | 1.017     | 1.000   | ✗          |
| BTC/XRP   | −0.4258     | 0.192 | 0.830     | 1.000   | ✗          |
| BTC/DOGE  | +0.0126     | 0.000 | 0.392     | 0.192   | ✗          |
| BTC/ADA   | +0.0839     | 0.013 | 0.321     | <0.001  | ✗          |

**Resultado: 0/4 confirmados.**

### Ronda 2 — Corpus Biológico Primario (Literatura Publicada)

Fuentes: Norway MRSA 1997–2010 (PLoS ONE 2013), EU EARS-Net 2012–2023 (ECDC),
UK MRSA BSI 2008–2021 (PHE/UKHSA), USA MRSA 2005–2017 (CDC AR Threats 2019),
HIV/CD4 (cohorte MACS publicada), Trypanosoma brucei (Pays et al. 2014).

| Dataset                  | b      | R²    | Dist. a φ | p perm. | Near φ | Confirmada |
|--------------------------|--------|-------|-----------|---------|--------|------------|
| Norway MRSA 1997–2010    | 0.688  | 0.940 | 0.121     | 0.083   | No     | ✗          |
| EU EARS-Net 2012–2023    | −0.064 | 0.367 | 0.469     | 0.973   | No     | ✗          |
| UK MRSA BSI 2008–2021    | −0.588 | 0.985 | 0.993     | 1.000   | No     | ✗          |
| USA MRSA 2005–2017       | −0.458 | 0.956 | 0.863     | 1.000   | No     | ✗          |
| HIV CD4 ratio (meses)    | −0.078 | 0.030 | 0.483     | 0.709   | No     | ✗          |
| Trypanosoma parasitemia  | 2.091  | 0.289 | 0.067     | 0.158   | Sí*    | ✗          |

\* near_φ=True (b cerca de φ·4/3=2.157), pero p_perm=0.158 con N=10 — sin poder estadístico suficiente.

**Resultado: 0/6 confirmados.**

### Conclusión de validación

**H-φ: NO CONFIRMADA. Total: 0/10 datasets independientes.**

H-φ se clasifica como **hipótesis especulativa de segundo orden**. No se incluye
en los claims del paper principal (Journal of Complex Networks). No afecta la
validez del marco general SNT, el exponente crítico b, ni el Índice ASI.

Sub-hipótesis H-3 (denominador 3 dominante en b/φ): **DESCARTADA definitivamente.**

---

## 7. Criterios de refutación (originales, conservados)

- **RC-φ-1:** Corpus ≥ 50 casos sin fricción institucional, datos primarios,
  distribución de b uniforme sin clustering cerca de fracciones de φ. ← **CUMPLIDO parcialmente con corpus de validación actual.**

- **RC-φ-2:** El mecanismo bajo dos restricciones acopladas puede producir
  atractores distintos de φ bajo condiciones especificadas a priori.

- **RC-φ-3:** Los exponentes b del corpus SNT son estadísticamente
  indistinguibles de una distribución uniforme tras corrección Bonferroni.

---

## 8. Protocolo de validación futura (si se desea continuar)

Para una validación concluyente se requiere:

1. Pre-registro en OSF o AsPredicted **antes** de recolectar datos nuevos
2. Corpus: ≥ 30 sistemas E3 parásito-huésped **sin intervención terapéutica activa**
3. Fuentes: NCBI, GenBank, bases de datos de coevolución
4. Criterio de éxito pre-registrado: >60% con b en ±0.10 de fracción φ, p < 0.05
5. Grupos control obligatorios: E1 (invasión biológica), D (digital)

---

*Fractal Core Research | Tlaxcala, México | Mayo 2026*  
*Estado: Hipótesis especulativa — validación independiente completada, resultado negativo*  
*SSRN: 6418778 | Zenodo: 10.5281/zenodo.19446521 | GitHub: Inzainos*
