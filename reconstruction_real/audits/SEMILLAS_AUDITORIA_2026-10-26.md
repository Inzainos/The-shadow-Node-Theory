# Auditoría de semillas (pendiente 2.4) — manual, no grep

**Fecha:** 2026-10-26 · **Alcance:** todos los scripts activos con RNG
(`np.random`, `default_rng`, `random`) en `code/` y
`reconstruction_real/code/`.

## Resultado: 22/22 con semilla explícita y fechada

La búsqueda automática previa solo detectaba literales
`default_rng(123)`; esta auditoría resolvió también constantes
(`SEMILLA = N` → `default_rng(SEMILLA)`), imports entre módulos y
parámetros default (`seed=N`). Veredicto: **cero scripts sin semilla**.

| Script | Semilla | Dónde |
|---|---|---|
| `code/matriz_mexico_ncuerpos.py` | 20261025 | literal (el que corrigió el grep original) |
| `code/build_aco_v29.py` | 42 | literal |
| `code/generate_figures_v29.py` | 7 | literal |
| `code/generate_readme_figures.py` | 20260927 | literal |
| `code/make_collapse_landscapes.py` | 7 | literal |
| `rc1_superlineal.py` | 20261002 | constante `SEMILLA` |
| `rc1_dominios_restantes.py` | 20261017 | constante |
| `deriva_forma_friccion.py` | 20261002 | constante |
| `dominio_B_recalibracion.py` | 20261003 | constante |
| `dominio_B_valor_puntual.py` | 20261002 | constante |
| `nbody_lognormal_clauset.py` | 20261002 | constante |
| `rango_tamano_internacional.py` | 20261002 | constante (fuente) |
| `rango_tamano_diagnostico.py` | 20261002 | import de internacional |
| `rango_tamano_percapita.py` | 20261002 | import |
| `reconstruccion_B_hub_comercio.py` | 20260927 | constante |
| `friction_aco_18.py` | 20261018 | default param |
| `prueba_discriminante_dominio_B.py` | 20260725 | default param |
| `tela_clasificacion_baseline.py` | 20261025 | constante |
| `nulos_ar1_aco.py` | 20261026 | constante |
| `sensibilidad_nulos_ar1.py` | 20261026 | import |
| `potencia_cointegracion.py` | 20261026 | constante |
| `modelo_jerarquico_b.py` | 20261026 | constante |

## Semilla en el informe

Los análisis pre-registrados citan su semilla en el documento
(preregistro o informe): RC1 (20261002 en el preregistro), tela baseline
(20261025 en el informe), nulos AR(1) (20261026 en el preregistro),
modelo jerárquico (20261026), potencia (20261026). Verificado por grep
de la cifra en `preregistro/` y `audits/`.

**Criterio de cierre del pendiente: satisfecho.**
