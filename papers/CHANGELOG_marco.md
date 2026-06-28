# Marco Teórico — Linaje de versiones y auditoría (v01 → v30)

Documento de trazabilidad del marco teórico de la Shadow Node Theory. Registra la
evolución entre versiones y la auditoría de junio 2026 que verificó que **nada
sustantivo se omitió** a lo largo del linaje (salvo la truncación de la v29, ya
restaurada en la v30).

## Línea de versiones (Google Drive)

| Versión | Formato | Tamaño aprox. | Estado |
|---------|---------|---------------|--------|
| v01 | docx | 19 KB | Semilla: 4 niveles de certeza, 3 casos históricos (Tlaxcala/Toledo/Brujas), leapfrog (Estonia/Rwanda/Medellín/Irlanda), anécdota fundacional (Wheeler), GRB 250702B |
| v02–v26 | docx | 22→92 KB | Crecimiento monótono: se agregan módulos, taxonomía de nodos, extensión biológica/astronómica, ASI, Sentinel Omega, herramientas matemáticas |
| **v27** | docx | **96 KB** | **Última versión de texto completo.** 126 secciones, 15+ módulos, apéndices A/B |
| v28 | pdf | 4 MB | = v27 en texto (verificado, ~230 K caracteres idénticos) + figuras |
| v29 ES/EN | gdoc | ~7 KB | **Truncada**: una instancia colapsó el cuerpo a una nota de actualización del corpus (sólo lista módulos por nombre) |
| **v30** | md + pdf | 76 pp | **Versión completa actual**: cuerpo v27 restaurado íntegro (Anexo A) + corpus real v30 + capa de Colapso Acoplado (ACO-A) + φ Ronda 4 |

## Auditoría de continuidad (junio 2026)

Se comparó el inventario de v01/v10/v15/v22 contra v27 en tres niveles:

1. **Secciones/módulos:** v10 y v15 son subconjuntos limpios de v27 (0 secciones
   ausentes en v27). v22 sólo difiere en subsecciones del Módulo XI que v27
   **renombró/corrigió** (no perdió).
2. **Acrónimos e índices nombrados** (ASI, CSI, K_max, criterios RC, fórmulas):
   ninguno desapareció en v27.
3. **Elementos narrativos distintivos** (anécdota de Wheeler/las pastillas;
   leapfrog real Medellín/Rwanda/Estonia; Grinberg/Lattice; Antikythera;
   Schumann/Sentinel Omega; Bitcoin como índice colectivo): todos presentes en
   v27 **y** en v30.

**Conclusión: v27 es un superconjunto estricto de todas las versiones previas.**
Los "cambios entre versiones" fueron mejoras/correcciones acumulativas, no
pérdidas.

## Correcciones documentadas a lo largo del linaje

- **GRB 250702B vs AT2025ulz:** en v01 se trataron como un mismo evento; v27 los
  **separa** correctamente (GRB 250702B = burst de ~7 h, 2 jul 2025; AT2025ulz =
  candidata a superkilonova, 18 ago 2025).
- **Trigger más rápido:** v22 reportaba "los triggers híbridos son la categoría
  más rápida" (artefacto del corpus de 57 casos); v27 lo **corrige** a la
  jerarquía estable "abruptos > híbridos > graduales".
- **Umbral ASI:** recalibrado de 0.5 (arbitrario) a 0.167 (mediana Intermediate,
  empírico) con HackerEarth 2026.
- **Corpus de 502 casos (v28 y anteriores): OBSOLETO.** La auditoría detectó
  ~188 valores de b sintéticos (`np.random.normal()`) y R² imposibles (hasta
  −7.332). Reemplazado por el corpus real v30 (721 casos, 89% significativos,
  R² ∈ [0,1], reproducible desde `reconstruction_real/`). En `marco_teorico_v30`
  el bloque estadístico del Módulo XI fue sustituido por una corrección que
  apunta al corpus real.
- **Truncación de v29:** única omisión real del linaje; el cuerpo completo fue
  restaurado en la v30 (Anexo A).

## Novedades introducidas en la v30 (no existían en v27/v28)

- **Capa de Colapso Orbital Acoplado (ACO-A):** eje ortogonal Δ, Ley de
  Inevitabilidad `h(τ)>0`, taxonomía de 5 modos de colapso, Principio de Mínima
  Fricción, evidencia en 5 dominios reales, y los 4 resultados de la hoja de ruta
  (fricción operacionalizada ρ=−1.0; ortogonalidad b⊥Δ ρ=+0.009; biología sin
  techo exponencial R²=0.96; hazard cripto h(τ)>0).
- **Hipótesis φ — Ronda 4:** re-test sobre corpus 721 con control placebo;
  refutada (señal aparente = artefacto de cobertura de bandas +
  pseudoreplicación COVID). 4 rondas, 0 señal robusta.

---

*Fractal Core Research · Tlaxcala, México · Auditoría de versiones junio 2026.*
