# Reconstrucción del dominio B con hub emergente de la red de comercio

**Fecha:** 2026-09-27 · **Script:** `reconstruction_real/code/reconstruccion_B_hub_comercio.py`
· **Log:** `reconstruction_real/logs/reconstruccion_B_hub_comercio_log.txt`
· **Salidas:** `reconstruction_real/data/dominio_B_hub_comercio.csv` (1 fila por nodo),
`reconstruction_real/data/dominio_B_hub_comercio_intra_nodo.csv` (prueba 2)

Atiende el pendiente 9 de la auditoría v32 ("reconstruir el dominio B con un hub que
emerja de la red de comercio en lugar de asignarse por PIB medio") y sigue a los
Bloques 2–3 de [`DISCRIMINANTE_DOMINIO_B.md`](DISCRIMINANTE_DOMINIO_B.md).

> **Alcance.** Es una reconstrucción de prueba. **No sustituye** al dominio B del corpus
> (446 casos, release 2.5.2), que sigue intacto y reproducible byte a byte desde MPD2020.
> Si el dominio B del corpus debe reemplazarse o retirarse es una decisión del autor.

---

## 1. Por qué reconstruir

En el dominio B publicado (`expand_B_massive.py`) cada par intra-regional se orienta
poniendo como "hub" al país con **PIB per cápita medio** más alto en toda la ventana.
La auditoría y la prueba discriminante mostraron tres problemas de esa regla:

1. Acopla por construcción la brecha inicial con la pendiente b (el nulo calibrado
   reproduce ρ(b, brecha) = −0.489 sin ningún acoplamiento).
2. El rol no es una posición en la red: 77 de los 91 países que son hub en algún par
   (85%) son también satélite en otro.
3. Con comercio bilateral real (COW), la participación nodo→hub no predice b y la
   participación inicial va con **menor** b (signo opuesto al predicho).

Aquí el hub deja de asignarse: **se lee de los datos de comercio**.

## 2. Diseño

| Elemento | Definición |
|---|---|
| Nodos | Los 103 países del dominio B publicado (91 aparecen como hub y 89 como satélite en algún par), nombres Maddison 2020 |
| Datos | Maddison 2020 (`data/maddison_mpd2020.csv`, SHA `1c0b15ae…`; población de `data/mpd2020.xlsx`, SHA `d20853c2…`) y COW Trade v4.0 (`data/COW_Trade_4.0.zip`, SHA `c44c4b5c…`) |
| Reglas de entidad del nodo | Las mismas que `build_comercio_bilateral_cow.py`: las exportaciones del nodo solo cuentan en años en que el código COW es el mismo territorio (URSS ≠ Rusia 1917–1991, Yugoslavia ≠ Serbia 1918–2005, Vietnam del Norte < 1976, Pakistán unificado < 1972) |
| Socios | Cada destino COW se asigna a una entidad Maddison **con el mismo territorio** (URSS → *Former USSR*, Yugoslavia 1918–1991 → *Former Yugoslavia*, Checoslovaquia → *Czechoslovakia*, etc.); sin equivalente → sin entidad (0.3% del valor exportado) |
| Década de referencia | 10 años desde el primer año ≥ 1900 con exportaciones totales positivas y PIB del nodo (mediana 1948; rango 1900–1993) |
| **Hub emergente** | El socio que recibe la mayor suma de exportaciones del nodo en la década de referencia. Está **predeterminado** respecto a la trayectoria posterior |
| Serie y ajuste | R(t) = PIBpc_hub / PIBpc_nodo, años comunes desde la década de referencia hasta 2018; b por MCO en log-log, **idéntico** a `calc()` de `expand_B_massive.py` |
| Brecha inicial g | Media de log R en las 5 primeras observaciones |

**Predicción SNT (acoplamiento):** a igual brecha inicial, el hub del que el nodo
depende comercialmente debería separarse más de él (b mayor) que un país igual de
distante que no es socio comercial principal. La β-convergencia no predice
diferencia.

## 3. Resultados

### 3.1 Quiénes son los hubs

- 102 de 103 nodos reconstruidos. **Serbia** queda fuera: COW no tiene ningún flujo
  válido del código 345 de 2006 en adelante (1,739 registros, todos −9).
- **19 hubs distintos**, muy concentrados: Reino Unido 37 nodos, Estados Unidos 27,
  Francia 7, Alemania 7, Japón 5; el resto con 1–3.
- La participación del hub en las exportaciones del nodo va de 10.1% a 93.9%
  (mediana 34.5%).
- El hub es más rico que el nodo al inicio en **95/102** casos (93%).
- **Solo 9 de los 102 pares emergentes existen en el dominio B publicado** (11 más
  aparecen invertidos y 82 no aparecen). El dominio B publicado es intra-regional y
  los hubs comerciales reales son mayormente extra-regionales (Reino Unido, Estados
  Unidos), así que **el dominio B publicado casi no mide relaciones hub–nodo
  comerciales**. En los 9 pares comunes b coincide en orden (ρ = +0.95; ventanas
  distintas).
- **El hub no es estable:** el principal destino de 2005–2014 es otro país en
  **77/102** nodos. Una sola pareja fija durante 50–119 años es una aproximación
  fuerte.

Comprobación de casos conocidos: México → Estados Unidos (71.5% en 1900–1909),
Canadá → Estados Unidos, Irlanda → Reino Unido (93.9%), Argentina → Reino Unido,
Cuba → Estados Unidos (87.1%), India → Reino Unido (1947), Polonia → Alemania (1920),
Afganistán → URSS (1955).

### 3.2 Descriptivos de b

| Conjunto | n | b media | b mediana | b > 0 (divergencia) |
|---|---:|---:|---:|---:|
| Todos | 102 | −0.074 | −0.094 | 36/102 |
| Hub más rico al inicio | 95 | −0.087 | −0.111 | **33/95** |

Con el hub definido por comercio, **dos de cada tres nodos convergen hacia su hub**
(b < 0 con hub más rico): el patrón dominante es de alcance, no de satelización.
Durbin-Watson mediana 0.115: la autocorrelación serial es la misma que en el dominio
B publicado, así que los 90/102 "significativos" son nominales.

ρ(b, brecha inicial) = **−0.153** (p = 0.125) frente a −0.489 en el dominio B
publicado: al dejar de asignar el hub por PIB medio, casi desaparece la correlación
brecha–pendiente, lo que confirma que en B era sobre todo un efecto de construcción
(como indicó el nulo calibrado).

### 3.3 Prueba 1 — hub comercial vs controles con la misma brecha

Controles por nodo: hasta 5 socios con serie Maddison que **no** están entre sus 5
principales destinos, misma ventana (n ≥ 90% de la del hub) y |Δg| ≤ 0.25; se toman
los más cercanos en g. d = b_hub − media(b_controles). Todos los nodos tuvieron
controles (mediana 5).

| Variante | Nodos | d mediana | d > 0 | Wilcoxon p | Cluster por hub |
|---|---:|---:|---:|---:|---|
| Todos | 102 | −0.014 | 45/102 | 0.78 | 11/19 hubs, p = 0.62 |
| Hub más rico | 95 | −0.013 | 42/95 | 0.80 | 9/16 hubs, p = 0.82 |
| Sin cobertura CMEA dudosa | 100 | −0.017 | 44/100 | 0.80 | 11/19 hubs, p = 0.62 |
| *Hub de ventana completa (endógeno)* | *101* | *+0.081* | *75/101* | *4.7×10⁻¹⁰* | *16/22, p = 0.007* |

**Con el hub predeterminado no hay diferencia**: el país al que el nodo más exporta se
separa de él igual que un país con la misma brecha con el que apenas comercia.

La variante endógena (hub = mayor destino acumulado en **toda** la ventana) sí da
d > 0 muy significativo, pero **no es evidencia de satelización**: por la ecuación de
gravedad el comercio crece con el tamaño del socio, así que el país que más creció
durante la ventana (b alto) termina siendo el mayor destino acumulado. Es causalidad
inversa por construcción; por eso la definición primaria usa solo la década inicial.

### 3.4 Prueba 2 — dentro de cada nodo

Para cada nodo, entre sus socios más ricos al inicio (g > 0) con registro comercial
válido en la década de referencia (mediana 49 socios; 84 nodos con ≥ 8), ρ de
Spearman parcial entre b y la participación de exportaciones, controlando g.

| Variante | ρ mediana | ρ > 0 | Wilcoxon p | Signo p | Permutación de signos (media) |
|---|---:|---:|---:|---:|---:|
| Sin controlar g | +0.055 | 49/84 | 0.80 | — | — |
| Controlando g | +0.115 | 53/84 | 0.046 | 0.021 | 0.15 |
| Controlando g y tamaño (log PIB total del socio) | +0.074 | 50/84 | 0.046 | 0.10 | — |

Señal positiva **débil y frágil**: la mediana es positiva, pero la media casi es cero
(+0.046; +0.031 con control de tamaño), la permutación sobre la media no es
significativa (p = 0.15), el signo deja de serlo con el control de gravedad
(p = 0.10) y los nodos no son independientes (los mismos socios ricos se repiten en
casi todos). Tampoco sobrevive una corrección por pruebas múltiples. Se reporta como
**no concluyente**. (Los dos Wilcoxon coinciden en p = 0.04572 porque dan el mismo
estadístico W = 1337 con vectores distintos; verificado sobre el CSV.)

## 4. Calidad de datos

- **CMEA.** COW registra como faltante o cero buena parte del comercio intra-CMEA.
  Verificado: las exportaciones de Mongolia a la URSS en 1958–1967 son −9 o 0 en los
  10 años, y por eso su hub sale Estados Unidos (15 M USD de un total pequeño). Se
  marcan los miembros del CMEA cuya década de referencia cae en 1949–1991 y cuyas
  exportaciones a la URSS son faltantes o cero en ≥ 5 de 10 años: **Mongolia (0/10) y
  Vietnam (1/10)**. Excluirlos no cambia la prueba 1.
- **Laos** (1955) sale con hub Myanmar (76%). Es lo que registra COW y no hay regla
  documentada para corregirlo; se deja con esta advertencia.
- **Irán**: su primer destino en la referencia es el Imperio ruso (sin entidad
  Maddison del mismo territorio); se usa el siguiente destino.
- **Emiratos Árabes Unidos**: 2 años con PIB per cápita = 0 en MPD2020; se descartan
  (no admiten logaritmo).
- **Alemania Federal**: la regla RFA → *Germany* (aproximación de territorio) no llegó
  a asignar ningún hub.

## 5. Conclusión

| Pregunta | Respuesta |
|---|---|
| ¿Quién es el hub de un país según su comercio? | Casi siempre una gran economía extra-regional (Reino Unido, Estados Unidos), y cambia con el tiempo (77/102 nodos cambian de hub al final) |
| ¿El dominio B publicado mide esas relaciones? | Casi no: solo 9 de 102 pares hub–nodo comerciales están en él |
| ¿El nodo diverge de su hub comercial (satelización)? | En su mayoría no: 62/95 convergen (b < 0) |
| ¿Diverge más de su hub que de un país igual de lejano con el que no comercia (acoplamiento)? | **No** (d mediana −0.014, p = 0.78; por cluster de hub p = 0.62) |
| ¿Dentro de cada nodo, más comercio va con más divergencia? | Señal débil, no robusta (no concluyente) |

**Veredicto:** reconstruir el dominio B con un hub que emerge del comercio **no
rescata** la lectura de acoplamiento SNT. Con datos de países, la dependencia
comercial inicial no predice que el hub se separe más del nodo, y el patrón dominante
es de convergencia. Esto es coherente con los Bloques 1–3 de la prueba
discriminante: el dominio B se describe mejor como dinámica de convergencia y
divergencia de ingresos que como satelización entre un hub y su nodo. La lectura
"la soberanía política frena la satelización" sigue siendo una hipótesis sin
respaldo empírico en este dominio.

## 6. Reproducción

```bash
python reconstruction_real/code/reconstruccion_B_hub_comercio.py
```

Tiempo aproximado: 40 s. Determinista (la única aleatoriedad, la permutación de
signos, usa semilla 20260927). Requiere `openpyxl` para leer la población de
`data/mpd2020.xlsx`.
