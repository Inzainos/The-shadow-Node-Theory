# φ como Atractor Teórico del Algoritmo de Satelización
## Hipótesis Deductiva — SNT v2.3.1

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

Esta hipótesis es deductiva, no empírica. El corpus SNT v2.3.1 no confirma
ni refuta H-φ por las siguientes razones:

1. Los exponentes b del corpus fueron calculados mediante regresión log-log
   OLS sobre series R(t) construidas a partir de fuentes secundarias. No
   son mediciones directas de sistemas físicos.

2. Los análisis exploratorios del corpus mostraron señales estadísticas
   consistentes con H-φ en dominios biológicos (p < 0.001), pero estos
   tests fueron definidos después de observar los datos y sobre el mismo
   conjunto usado para construir la teoría. Los p-values están inflados.

3. La hipótesis requiere validación sobre datos primarios independientes
   con series temporales verificadas — condición que el corpus actual no
   satisface completamente.

Lo publicable en este momento es el argumento deductivo. La confirmación
empírica es trabajo futuro con protocolo pre-registrado.

---

## 6. Criterio de refutación

H-φ queda refutada si:

- RC-φ-1: Un corpus ≥ 50 casos de dominios sin fricción institucional,
  con datos primarios verificados, muestra distribución de b uniforme
  sin clustering cerca de fracciones de φ.

- RC-φ-2: El mecanismo de preferential attachment bajo dos restricciones
  acopladas puede producir distribuciones estacionarias con atractores
  distintos de φ bajo condiciones especificadas a priori.

- RC-φ-3: Los exponentes b del corpus SNT son estadísticamente
  indistinguibles de una distribución uniforme en el mismo rango cuando
  se aplica corrección de Bonferroni por tests múltiples.

---

*Fractal Core Research | Tlaxcala, Mexico | 2026*
*Estado: Hipótesis deductiva — pendiente de validación empírica pre-registrada*
