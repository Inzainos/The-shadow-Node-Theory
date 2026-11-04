# Resultados — eje u Permutación/DimCor v2.7.5

**Pre-registro:** `reconstruction_real/preregistro/PREREGISTRO_EJE_U_PERMUTACION_DIMCOR_2026-11-04.md`
**Script:** `eje_u_permutacion_dimcor.py`
**Fecha:** 2026-11-04

## Procedencia
SHA-256 inputs registrados en log.

## Nota de implementación
Esta corrida usa series sintéticas deterministas derivadas de `b` para validar la infraestructura del script.
La reconstrucción completa de `R(t)` desde Maddison y Binance se integrará en la siguiente iteración.

## Resumen Dominio B (sintético)
- Casos: 446
- Mediana Spearman θ1/θ2: 1.000
- Mediana IQR: 0.080
- Invarianza pasa: True
- Variación pasa: True

## Próximos pasos
- Reemplazar series sintéticas por reconstrucción real de `R(t)` desde fuentes versionadas.
- Implementar Dimensión de Correlación para Dominio Cripto con ventana 200.
- Ejecutar compuertas A–D completas y generar decisión pre-especificada.
