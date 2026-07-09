# Delta — Jupyter Notebooks

Launcher interactivo del motor **Delta**, clonado del Jupyter launcher de
Sentinel Omega (repo `workspaces`) y adaptado a este módulo — misma
estructura de 8 secciones, motor Delta en lugar de los bots ONNX/Omega.

## Quick Start

### 1. Instalar dependencias

```bash
pip install -r requirements_jupyter.txt
```

### 2. Lanzar Jupyter

```bash
jupyter lab      # o: jupyter notebook
```

### 3. Abrir `delta_launcher.ipynb`

Corre las celdas en orden:

1. **Setup & Imports** — agrega `delta/` al path, carga el motor
2. **Inicializar motor** — fricción y b esperada por mercado (SNT ρ = −0.68)
3. **Cargar datos** — `USE_REAL_DATA = False` (sintético, sin red) o `True`
   (CoinGecko + Yahoo Finance, sin API key)
4. **Analizar un par** — `analyze_pair()` → `DeltaSignal` completo
5. **Barrido completo** — `RUN_FULL_SWEEP = True` corre `run_real_delta.main()`
   (~23 señales; tarda por el rate-limit de CoinGecko)
6. **Consultar resultados** — DataFrame desde `real_delta_signals.json`
7. **Visualizar** — b por par vs b esperada por fricción; rolling-b
8. **Guardar & cierre**

## Características

- ✅ **Autocontenido** — usa solo los módulos de `delta/`, sin dependencia
  del repo de Sentinel Omega
- ✅ **Sin API keys** — CoinGecko y Yahoo Finance públicos
- ✅ **Modo offline** — series sintéticas para explorar sin red
- ✅ **Solo la esencia** — las señales se guardan en JSON (sin precios crudos)

## Interpretación rápida

| Señal | Lectura |
|---|---|
| `b > 0` | el hub domina (BTC season / stock satelizada) |
| `b < 0` | el shadow gana terreno (alt season / breakout) |
| `anomaly_score` alto | desviación fuerte de la b esperada por fricción — la anomalía operable |
| `leapfrog = true` | el rolling-b cruzó de + a − : cambio de régimen |

> Señal descriptiva / de apoyo a decisión — **no es consejo financiero**.

Teoría base: `../README.md` y el marco SNT en `../../papers/`.
