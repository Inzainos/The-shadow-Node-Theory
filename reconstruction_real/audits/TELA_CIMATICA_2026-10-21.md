# Capa Cimática de la Tela de Incertidumbre — Resultados

**Fecha:** 2026-10-21
**Script:** `code/tela_cimatica.py`
**Salidas:** `figures/fig_tela_cimatica_chladni.{png,svg}`,
`figures/fig_tela_cimatica_tonos.{png,svg}`,
`data/tela_cimatica_huellas.csv`,
`data/tela_cimatica_clasificacion.csv`,
`data/tela_cimatica_clasificacion_phi.csv`
**Origen de la idea:** `conocimiento/Tela/` (prototipo + lluvia de ideas
2026-10-20 — la tela nació como capa cimática: "la tela vibra en modos
propios; cada dominio tiene su tono resonante")

## Qué es

La lectura cimática del cubo 𝒞(u, m, τ): la tela es la placa de Chladni,
los 7,306 puntos son la arena, y el campo φ (fricción) es el tono. Se
implementan cinco piezas:

| Pieza | Qué produce |
|-------|-------------|
| **La placa** | Mapa de densidad (τ × log₁₀ m) de los 7,306 puntos, con líneas nodales (zonas vacías) |
| **La figura** | Trayectoria mediana log₁₀ m(τ) por dominio con banda IQR |
| **Los tonos** | Espectro FFT (armónicos 1-16 de la fase τ) mediano por dominio |
| **Las huellas** | CSV por dominio: m en τ=0/0.25/0.5/0.75/1, amplitudes A1/A2/A3, m máx |
| **La prueba** | Clasificación leave-one-out por centroide cercano: ¿viendo la figura se identifica el dominio? ¿y el tono? |

## Resultados medidos

### Identificación por dominio (el objetivo declarado)

| Configuración | Exactitud |
|---------------|-----------|
| Todos los rasgos (m en 5 fases + A1/A2/A3) | **21.2%** (156/737) |
| Solo-forma (sin τ=0, que es 1.0 por construcción en sombras) | **19.8%** (146/737) |

Por dominio: A 3/4 · ACO 13/18 · B 30/446 · C 2/24 · D 2/3 · E1 3/4 ·
E2 0/2 · E3 101/234 · F1 2/2.

**Veredicto: NO.** La figura sola no identifica el dominio. B y C —
mismo φ alta, distribuciones de b solapadas — dibujan la misma figura y
se confunden entre sí.

### Identificación por tono φ (la predicción cimática)

| Tono | Configuración | Exactitud |
|------|---------------|-----------|
| Por dominio | todos / solo-forma | 21.2% / 19.8% |
| **Por tono φ** | todos / solo-forma | **53.7% / 43.7%** |

Por tono: alta 207/472 · fisica 0/4 · media 3/4 · nula 174/241 ·
variable (ACO) 13/18.

**Veredicto: PARCIAL.** El tono se identifica mejor que el dominio
(2.5× con todos los rasgos), como predice la cimática — la figura
revela el régimen de fricción, no la etiqueta del instrumento. El tono
`nula` se identifica bien (174/241 = 72%): sin fricción la arena vuela a
m extremos (mediana de m máx = 32.5, hasta 24 millones) y eso es
inconfundible. El tono `alta` se confunde (44%) porque muchos casos con
b bajo dibujan la misma figura sin importar su φ nominal.

### Los regímenes extremos SÍ se identifican

- **ACO real (serie cruda): 13/18 = 72%** con todos los rasgos — las
  trayectorias reales empiezan abajo (m<1) y terminan cerca de 1; la
  sombra siempre empieza exactamente en 1. El rasgo τ=0 es señal REAL
  para casos crudos y artefacto de construcción para sombras (disclosed).
- **nula (D+E1+E3): 72%** — la cavidad sin fricción es visible.

## Lectura cimática honesta

1. La placa funciona: la arena se organiza en bandas por φ, y las líneas
   nodales (vacías entre m≈2 y m≈30) separan los regímenes.
2. La figura identifica **frecuencias, no instrumentos** — igual que en
   Chladni: el patrón dice el tono que vibra, no qué violín lo tocó.
3. Para el objetivo operacional ("al ver la figura, identificar rápido"):
   un caso nuevo que caiga en la placa se puede asignar a su **régimen de
   fricción** con ~54% (72% en los extremos), y como "colapso real
   (ACO-like)" con 72% — pero NO a su dominio nominal.
4. El φ postulado es categórico por dominio; la medición muestra que la
   figura depende de (b, n), y donde los (b, n) se solapan entre tonos,
   el tono no es recuperable de la forma sola. Calibrar φ por caso
   (no por dominio) es el paso siguiente natural.

## Limitaciones

- 721 de 739 casos son sombras: su forma está determinada por (b, n) del
  ajuste; m(τ=0)=1 por construcción (a=1, t=1).
- Solo 18 casos tienen trayectoria real (ACO).
- La clasificación es centroide-cercano sin calibrar; no es una frontera
  definitiva, es la medición de base de la capa.
- u sigue NULL (sin definición operativa en ningún dominio).

## Reproducir

```bash
python reconstruction_real/code/tela_cimatica.py   # ~4 s, sin descargas
```

Lee `data/tela_de_incertidumbre.csv` (generado por
`code/tela_de_incertidumbre.py`). Log en
`logs/tela_cimatica_log.txt`.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-21*
