# Política de seguridad

Shadow Node Theory (SNT) es un repositorio de investigación. Esta política
cubre el manejo de datos sensibles y el reporte de vulnerabilidades.

## Datos que NUNCA deben commitearse

- **Secretos**: claves de API, tokens, credenciales. Los archivos `.env` están
  en `.gitignore`; usa `*.env.example` solo con valores de placeholder.
- **PHI / datos de paciente crudos**: el subproyecto `genomic_agent` bloquea en
  su `.gitignore` los patrones `*.rnaseq.csv`, `*_rnaseq.csv`, `paciente_*.csv`,
  `patient_*.csv`, `*_expression.csv`. Solo se commitea data pública, de acceso
  abierto y de-identificada (p. ej. TCGA vía la API pública NIH GDC), y salidas
  agregadas pre-aprobadas.
- **Datos propietarios**: p. ej. `zerve_hackathon_dataset.csv` no es
  redistribuible (contacto: elan.zainos.corona@gmail.com) y está bloqueado.

## Buenas prácticas operativas

- `SNT_LOG_LEVEL` nunca debe ser `DEBUG` en producción (expone PHI en logs).
- Las bases de datos generadas en runtime (`*.db`, `*.sqlite`) están ignoradas.
- Antes de commitear, revisa `git status` y confirma que no entren datos crudos.

## Reporte de vulnerabilidades o exposición de datos

Si detectas un secreto expuesto, PHI commiteada por error, o cualquier problema
de seguridad, **no abras un issue público**. Escribe directamente a:

**Elán Zainos Corona** — elan.zainos.corona@gmail.com (Fractal Core Research)

Incluye el archivo/commit afectado y, si aplica, los pasos para reproducir.
