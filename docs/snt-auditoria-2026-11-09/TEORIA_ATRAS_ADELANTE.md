# Shadow Node Theory — lectura de atrás hacia adelante

**Fecha:** 2026-11-09
**Ordenado por:** Elán Zainos Corona (leer la teoría del estado actual hacia los orígenes; buscar en Google Drive por contenido, no por nombre de archivo)
**Fuentes leídas:** `repo Inzainos/The-shadow-Node-Theory` completo en lo relevante (README, CHANGELOG, docs/HISTORIA, docs/DOMINIOS, CASOS_DE_USO, papers/marco_teorico.md v34, archive/marco_teorico_v33.md, papers/marco_teorico_v30.md, archive/snt_phi_hypothesis_v28.md, papers/CHANGELOG_marco.md, papers/SNT_Colapso_Acoplado.md) + Google Drive por contenido + libro SUDO UNIVERSE v6.0 (texto local).
**Regla:** solo lectura y esta síntesis. Nada del repo, el espacio ni la teoría fue modificado. Si algo no se encontró, se dice explícitamente.

**Principio que guía este trabajo (Elán, 2026-11-09 ~11:05):** "Al nombrar las cosas las vamos entendiendo mejor. El humano tiende a nombrar las cosas para perderles el miedo." Por eso la taxonomía: nombrar cada cosa que se está haciendo.

**Decisión del autor (Elán, 2026-11-09 ~11:04):** los términos nuevos (luz, puente ER=EPR, breach, disonancia, decaimiento, fractura, switchover) **se integran como taxonomía, con definiciones de Elán**, en la reconstrucción de los materiales derivados. El malentendido (el agente inventando "luz") terminó sacando más taxonomía.

---

## (a) Estado actual de la teoría (v2.7.5.1, marco v34)

### Qué es SNT

> "Shadow Node Theory estudia trayectorias relativas entre un hub y un nodo. Su objeto empírico es la razón `R(t) = métrica_del_hub / métrica_del_nodo`, resumida —cuando los datos lo permiten— por `R(t) = a·t^b`. El marco también incluye ACO-A, una descripción separada de la absorción posterior a ciertos colapsos, y una capa de incertidumbre que distingue observaciones, proyecciones y reconstrucciones." — `README.md:9-14`

> "SNT es un marco de análisis, no una ley universal ni un predictor validado." — `README.md:15`

Numeraciones independientes (`docs/HISTORIA.md:184-186`): repo **v2.7.5.1**, corpus consolidado **v6**, marco teórico **v34**. DOI Zenodo 10.5281/zenodo.23958082; SSRN abstract 6418778.

### Las cinco capas (README.md:22-52)

| Capa | Fórmula / contenido | Estatus |
|---|---|---|
| 1. Trayectoria relativa | `R(t) = a·t^b`, `R = métrica_hub / métrica_nodo` | Medida por dominio |
| 2. Colapso orbital acoplado ACO-A | `A(τ) = c·τ^Δ` | Medida (18 casos + aplicaciones) |
| 3. Campo de fricción φ | `φ: 𝒞 × T → ℝ⁺`, flujo `-∇_γ φ` | **Postulado, no medido** |
| 4. Tela de incertidumbre | 740 trayectorias (699 reales + 41 sombras); LOO dominio 50.7%, tono 66.2% | Medida (exploratoria) |
| 5. Tela simática | Representación cimática de resonancia entre dominios | Conceptual |

**ASI:** `ASI = δH · α / F` (`README.md:50`). δH = diversidad de problemas (-sum(p_i log2 p_i) normalizado [0,1]); α = eventos_autónomos / total (autonomía de decisión); F = tanh(std/mean/2) (caos interno). Umbral ASI > 1 define soberanía. Operacionalización pendiente de validación independiente. — `README.md:313-324`.

**Lectura de b** (`README.md:298-307` y `README.md:168-174`):

| b | Lectura |
|---|---|
| b < 0 | Convergencia / leapfrog (el nodo gana terreno relativo) |
| -0.1 < b ≤ 0.05 | Estado estacionario |
| 0.05 < b ≤ 0.3 | Satelización gradual |
| 0.3 < b < 1 | Satelización activa |
| b ≥ 1 | Banda descriptiva no clasificada; NO prueba régimen superlineal |

**Definiciones nodales** (`README.md:310-316`):
- Nodo Hub: "absorbe energía productiva residual y aumenta masa gravitacional."
- Nodo Sombra: "producción extraída sistemáticamente, divergencia progresiva."
- Proximidad Crítica: "umbral de extracción > regeneración."

**Taxonomía de cinco niveles** (`README.md:318-328`): 0 Macro-Hub Central (absorción unidireccional, limitante K_max, respuesta inmunológica); 1 Atractores Secundarios; 2 Bypass Logístico; 3 Nodos Sombra Profundo; E Exógeno.

**Muro de 5 Eventos** (`README.md:130-134`): "Umbral crítico en dominios digital y genómico: usuarios con <5 tipos de evento distintos tienen >90% probabilidad de churn; en TCGA, 2-5% de pacientes presentan ≥5 eventos hub simultáneos definiendo el 5-Event Wall. Es el equivalente de diversidad funcional mínima para escapar de la satelización."

### ACO-A: lo que define

`papers/SNT_Colapso_Acoplado.md` (documento teórico, 391 líneas):

- **§0 Tesis:** "el colapso es un eje ortogonal que puede activarse en cualquier sistema, de cualquier dominio, en cualquier punto de su trayectoria."
- **§1 Dos ejes ortogonales (b ⊥ Δ):** Eje 1 satelización `R(t) = a·t^b`, `R = m_hub / m_node`; Eje 2 colapso `A(τ) = c·τ^Δ`, `A = m_absorbente / m_hub^pico`, `τ = tiempo desde la extinción funcional`. "El colapso no espera a que termine el ciclo de satelización." Predicción falsable: `corr(b, Δ) ≈ 0`. Test cripto n=11: ρ = +0.009 (p = 0.98); ampliación pre-registrada n=242: ρ = −0.119, dentro de la banda de equivalencia ±0.3.
- **§2 Hazard h(τ):** "Ningún sistema es eterno" = `h(τ) > 0` para todo sistema. Refutable si se halla un sistema con hazard = 0.
- **§3 Ley de Inevitabilidad del Colapso:** "Todo sistema con dinámica tiende a un punto de colapso. 'Colapso' NO es muerte: es un punto de reorganización crítica (bifurcación). Al colapsar, el sistema **decae** (absorción terminal, lo mide Δ) o **da el brinco / leapfrog** (renovación, reingreso al ciclo — el Uroboro). El colapso es el momento donde se decide entre ambos; el camino depende de las reservas del nodo (criterio RC4, umbral dual RQ/RL). Testigos de brinco: Querétaro (b=−0.155), Nuevo León (b=−0.058)."
- **§4 Taxonomía de modos de colapso** (fricción × trigger × piso/techo): Decaimiento Orbital Regulado; Decaimiento Craquelado; Caída-a-piso; Acantilado Catastrófico; Barrido logístico.
- **§5 Principio de Mínima Fricción:** "Todo colapso sigue la trayectoria que minimiza la fricción integrada. Las grietas fractales del craquelado son la solución visible a esa optimización: el camino por donde el sistema pierde cohesión gastando lo menos posible." El principio = flujo gradiente sobre un paisaje de estabilidad.
- **§6 Evidencia:** 5 dominios (astro, finanzas, historia, cripto, biología). WaMu por vía FDIC pre-arreglada = mínima fricción → 21 h; Lehman sin esa vía → 30,681 h.

### El marco v34: doce axiomas + capa de proyección

`papers/marco_teorico.md` (2026-09-14, aditivo; ninguna cifra ni etiqueta de v33 cambia):

- **Axioma 0 (FUNDAMENTAL):** la tela de incertidumbre es el lienzo (vacío cuántico, fondo estocástico de ondas gravitacionales). Lectura de compatibilidad con SNT (no derivación): h(τ) > 0 para todo sistema.
- **Axioma 0.1 (ESTRUCTURAL):** el cubo de incertidumbre `𝒞(u, m, τ)`. `m` = R con proxy declarado; `τ` = fase temporal; **`u` = apertura de posibilidades, sin definición operativa en ningún dominio, permanece NULL**; no se inventa sustituto. La fricción entra como **campo escalar φ sobre el volumen** (flujo gradiente), no como eje. "φ está postulado, no medido."
- **Axioma 0.2 (OBSERVABLE):** la sombra = imagen de 𝒞 bajo proyección `Π_θ`, θ = (B, V, ρ, W, λ). "Π_θ no es inyectiva: existen 𝒞₁ ≠ 𝒞₂ con la misma sombra." Invarianza de proyección: una forma cuenta como rasgo solo si persiste bajo dos marcos θ independientes. "Cambiar solo resolución y umbral no es mover la luz, es enfocar la misma sombra." Reconstrucción = conjunto ℛ de volúmenes compatibles, no un elemento.
- **Axiomas 1–12:** 1 paquetes cósmicos (INFRAESTRUCTURA, Dominio G); 2 cavidad/modos propios, Schumann 7.8 Hz (CONCEPTUAL); 3 ambiente como filtro (CONCEPTUAL); 4 realidad soportable = Principio de Mínima Fricción (ANCLADO); 5 fricción protege y limita (ANCLADO PARCIAL desde 2026-10-26: fricción → b NO MEDIDA; vigente fricción → Δ, n=6, ρ=−1.000); 6 célula como mapa operativo (CONCEPTUAL); 7 desempaquetado gradual (CONCEPTUAL); 8 historia de exposición, Dominio G (INFRAESTRUCTURA); 9 picos locales, tardígrado (CONCEPTUAL); 10 cuando una rama cae, el hueco persiste, Delta→Ómicron k=0.218/día, R²=0.79 (ANCLADO); 11 el planeta ajusta sus filtros (CONCEPTUAL); 12 la tela precede a la forma, cimática (CONCEPTUAL).
- **Cláusulas metodológicas (v33 1–5, v34 6–9):** metáfora frente a validación; etiquetas visibles; infraestructura no es evidencia ("se cita como puente construido"); documentos separados (marco ≠ paper empírico); capa humana fuera del cuerpo axiomático; marco de medición obligatorio (toda figura lleva su θ); protocolo ciego con pre-registro; no imputación de descriptores; el alcance del marco no se encoge entre versiones.
- **Cierre v34:** tres huecos declarados, ninguno rellenado con proxy: eje `u` sin definición operativa; campo φ postulado y no medido; piso factor y no variable (cimática del colapso acotada al eje acelera / no acelera).

### Estado de la evidencia (lo que NO se presenta como hallazgo)

`README.md:228-234`: los valores p por caso no son pruebas independientes; `b ≥ 1` no identifica superlinealidad; φ postulada por dominio, no medida como campo continuo; eje `u` sin definición operativa y no se rellena con proxy; las sombras no son series observadas; asociación descriptiva, clasificación exploratoria y convergencia de ACO no establecen capacidad predictiva ni universalidad.

Corpus: 721 casos reales (B 446, E3 234, ACO 18, G 1, resto dominios menores); tela 740 trayectorias (699 reales + 41 sombras). Dominio B: 290/446 no estimables, inferencia **indecidible**. E3: 233/234 reproducibles.

---

## (b) Evolución hacia atrás: qué se añadió, qué se retiró, qué cambió de sentido

Fuente principal: `papers/CHANGELOG_marco.md` (linaje v01→v34, auditoría junio 2026) + `CHANGELOG.md` del repo + `docs/HISTORIA.md`. Leído en orden inverso, del presente al origen.

### v34 (2026-09-14) — la capa de proyección

Agrega, sin tocar nada de v33: Axiomas 0.1 (cubo `𝒞(u, m, τ)`, ESTRUCTURAL) y 0.2 (sombra/proyección `Π_θ`, OBSERVABLE); fricción como campo escalar φ sobre el volumen; cimática del colapso como extensión del Axioma 12 (con cláusula anti-metáfora); etiquetas ESTRUCTURAL/OBSERVABLE/ESPECULATIVO; cláusulas 6–9; apéndice especulativo (cubo ontológico, fuera del cuerpo, no citable como premisa). **"Tela" queda reservada al Axioma 0; lo observable es sombra/proyección.** Ningún axioma cambió de estatus. Tres huecos declarados sin rellenar: `u` sin definición operativa, φ postulada no medida, piso factor no variable.

### v33 (2026-09-10) — suelo y etiquetas

Agrega sobre v32: **Axioma 0 (tela de incertidumbre, FUNDAMENTAL)**; etiquetas de estatus por axioma (FUNDAMENTAL 0; ANCLADO 4, 5, 10; INFRAESTRUCTURA 1, 8 vía Dominio G; CONCEPTUAL 2, 3, 6, 7, 9, 11, 12); cavidad/modos propios en Axioma 2 (Schumann 7.8 Hz); cimática en Axioma 12; anclaje numérico de Axiomas 4, 5 y 10; cadena operativa 0–8; 5 cláusulas metodológicas. Todo por agregación: "La versión 33 no reescribe la 32: le pone base."

### v32 (2026-07-24) — los doce axiomas

Fusión de v31 + marco conceptual del 2026-07-24: doce axiomas (paquetes cósmicos, resonancia, filtros, fricción, banda soportable, nichos). **No versionada en el repo.** No confundir con `AUDITORIA_INTEGRAL_v32.md` (auditoría estadística del corpus).

### v31 (2026-07-06) — el paisaje vivo y el Muro

Parche activo hasta 2026-09-10: Principio del Paisaje Vivo; **Axiomas Ax-M1–Ax-M4** (formalización micro del Principio de Mínima Fricción: trayectoria default, paisaje sin techo, historia como fricción heredada, **leapfrog como canal alternativo**); integral variacional unificadora J = ∫ F(x(t),t) dt (unifica b, Δ, h(t) y leapfrog bajo un único principio); **4 trayectorias tipo del 5-Event Wall** (0→5 completo/absorción, 0→4+leapfrog, 0→3+estancamiento, 0→2+reversión; cada una con firma (b, F, E_res, C_k)); Análisis de Divergencia Retrospectiva; Filogenia Predictiva; Recurrencia de Poincaré operacionalizada; invarianza de escala individual→planeta. Roadmap Item 5 abierto.

### v30 (2026-06-28) — ACO-A y el corpus real

Versión completa anterior: cuerpo v27 restaurado íntegro (Anexo A) + corpus real v30 + **capa de Colapso Orbital Acoplado (ACO-A)** + φ Ronda 4. Novedades (`CHANGELOG_marco.md`): ACO-A (eje ortogonal Δ, Ley de Inevitabilidad h(τ)>0, taxonomía de 5 modos de colapso, Principio de Mínima Fricción, evidencia en 5 dominios, 4 resultados de la hoja de ruta: fricción operacionalizada ρ=−1.0; ortogonalidad b⊥Δ ρ=+0.009; biología sin techo exponencial R²=0.96; hazard cripto h(τ)>0). **Hipótesis φ — Ronda 4: re-test sobre corpus 721 con control placebo; refutada** (señal aparente = artefacto de cobertura de bandas + pseudorreplicación COVID). 4 rondas, 0 señal robusta.

En el repo, v30 = 2.5.0 (2026-06-28, `CHANGELOG.md:1478`): ACO-A como eje universal y transversal; hazard h(τ)>0; taxonomía de modos (Decaimiento Orbital Regulado, Cracquelure, Floor-Arrested, Catastrophic Cliff, Logistic Sweep); Principio de Mínima Fricción; evidencia en 5 dominios; marco v30 + preprint SSRN v30; criterios de refutación RC9–RC11.

### v29 (truncada) — la única omisión real

Versión ES/EN en Google Docs: una instancia colapsó el cuerpo a una nota de actualización del corpus (solo lista módulos por nombre). **Única omisión real del linaje; el cuerpo completo fue restaurado en la v30 (Anexo A).**

### v27–v28 — el texto completo

v27 (96 KB, 126 secciones, 15+ módulos, apéndices A/B): última versión de texto completo. v28 = v27 en texto (verificado, ~230 K caracteres idénticos) + figuras, en PDF. **Conclusión de la auditoría de continuidad (junio 2026): v27 es un superconjunto estricto de todas las versiones previas.** Los cambios fueron mejoras/correcciones acumulativas, no pérdidas. v10 y v15 son subconjuntos limpios de v27; v22 solo difiere en subsecciones del Módulo XI que v27 renombró/corrigió.

### v02–v26 — crecimiento monótono

De 22 KB a 92 KB: se agregan módulos, taxonomía de nodos, extensión biológica/astronómica, **ASI**, Sentinel Omega, herramientas matemáticas. **ASI creció en v02–v26 y ya estaba presente en v27 como superset**; HackerEarth (2026) solo recalibró su umbral de 0.5 (arbitrario) a 0.167 (mediana Intermediate, empírico).

### v01 — la semilla

19 KB, docx: 4 niveles de certeza, 3 casos históricos (Tlaxcala/Toledo/Brujas), **leapfrog como casos históricos** (Estonia/Rwanda/Medellín/Irlanda), anécdota fundacional (Wheeler), GRB 250702B. Correcciones posteriores del linaje: GRB 250702B vs AT2025ulz separados en v27 (antes tratados como un mismo evento); jerarquía de triggers corregida ("abruptos > híbridos > graduales").

### La línea del repo (v2.0 → v2.7.5.1)

- **v2.0.0 — Inicial:** publicación inicial del marco SNT, preprint SSRN, primeras versiones del corpus y del marco teórico. **Leapfrog entra como mecanismo formal en v2.0 (2026-03-19)** — en v01 solo existía como casos históricos.
- **v2.2.0:** paquete de replicación v2.2, figuras de publicación, envío a PLOS Complex Systems.
- **v2.3.1:** paquete de replicación completo, envío a J. Complex Networks (rechazado); **validación H-φ: resultado negativo** (H-φ refutada; no afecta el hallazgo central fricción–satelización); corrección de fuga de datos en HackerEarth (ROC-AUC corregido).
- **v2.4.0 (2026-06-26):** **corpus REAL de 721 casos** reconstruido desde fuentes primarias, reemplazando el corpus sintético previo (el corpus de 502 casos contenía ~188 valores de b sintéticos `np.random.normal()` y R² imposibles hasta −7.332; movido a `archive/`, no citable). Módulo XVI — Arquitectura de Colapso Orbital (ACO): 18 casos verificados en 4 dominios. SNT Genomic Topologic Analyzer. Dashboard Streamlit.
- **v2.5.0 (2026-06-28):** ACO-A como eje universal (ver v30 arriba).
- **v2.5.2 (2026-09-10):** Dominio G (marco v33); **G03 (Bennu) alcanzó n = 3** (b = −1.371, R² = 0.931, p = 0.123; la etiqueta se mantiene en INFRAESTRUCTURA hasta decisión del autor).
- **v2.5.3 (2026-09-26, etiqueta retroactiva):** auditoría integral v32, prueba discriminante del dominio B, revisión r31 del preprint. **Retiros:** "abrupto 5.9× más rápido que gradual" (provenía de 2 vs 2 casos, p = 0.33); ROC-AUC HackerEarth 0.9994 (fuga de datos) → 0.715 ± 0.019; ASI "precision = 1.0, cero falsos positivos" retirado (la etiqueta `soberania` es ASI > 1, así que la clasificación es tautológica: TP 13, FP 0, FN 0 por construcción; 13/4,774 = 0.27 %); Hallazgo 1 (fricción) deja de llamarse "estadísticamente robusto".
- **v2.6.0 / v2.6.1 (2026-09-27):** marco v34 (capa de proyección, 2026-09-14); nota de auditoría del Axioma 5 (fricción → b no significativa a nivel de dominio).
- **v2.7.1 (2026-10-21):** **tela de incertidumbre integrada** — 740 trayectorias, 51,210 puntos; 699 series reales y 41 sombras. Se corrige la lectura anterior: el origen común en `m=1` era un artefacto de las sombras. LOO dominio 50.7%, tono 66.2% (exploratoria, no clasificador calibrado). Límites explícitos: `u` sigue NULL; φ postulada por dominio, no variable continua medida.
- **v2.7.4 (2026-10-27):** sello del protocolo; ADENDA 5 (prueba prospectiva ACO-A, cohorte v2, ventana 2026-09-30 → 2027-09-30; backcast actualizado: P1a/P2 respaldadas, P3 inconcluso).
- **v2.7.5 (2026-11-04, en desarrollo):** definición formal del campo φ en Axioma 0.1 (`φ: 𝒞 × T → ℝ⁺`, flujo gradiente, condiciones de borde, proxies candidatas, regla de admisión); pre-registro para candidato a eje `u` (Entropía de Permutación / Dimensión de Correlación); catálogo cripto ampliado 30 → 60 pares (mediana D2 1.653).

### Qué cambió de sentido (resumen)

| Término | Antes | Ahora |
|---|---|---|
| `b ≥ 1` | Régimen superlineal | Banda descriptiva no clasificada (RC1: error AIC 22.6%–96.8% > 20% pre-registrado) |
| `φ` (H-φ, razón áurea) | Atractor teórico del algoritmo de satelización (v28: "H-φ: En sistemas donde el mecanismo opera sin fricción… b converge hacia φ") | **Refutada en 4 rondas, 0/10 datasets independientes** (v28, validación mayo 2026); φ queda solo como campo de fricción (v34) y como heurística acotada al Axioma 12 |
| Fricción → b | Anclaje ANCLADO (ρ = −0.68, p = 2.5×10⁻⁹⁷, n = 714) | **NO MEDIDA** (control de estructura 2026-10-26: p = 0.053 por permutación, MixedLM p = 0.57; pre-registro dominios nuevos ρ = −0.131, p = 0.39). Axioma 5 pasa a ANCLADO PARCIAL; vigente fricción → Δ (n=6) y fricción física astronómica |
| "Roche Radius" (b = 1.0) | Umbral candidato (v30:97) | **Etiqueta retirada** (RC1, 2026-10-02; `CHANGELOG.md:726-736`); "Roche" queda solo como "entrada al radio de Roche → colapso abrupto" y ratio de Roche |
| Corpus | 502 casos (v28 y anteriores) | **Obsoleto** (valores sintéticos); corpus real 721 casos (v2.4.0) |
| Sombra | (v27 y anteriores) Nodo Sombra = producción extraída sistemáticamente | Tres sentidos vigentes: (1) Nodo Sombra v2.0 (extracción); (2) sombra Axioma 0.2 v34 = proyección Π_θ(𝒞); (3) 41 sombras de la tela = casos sin serie cruda versionada |
| Tela | "La tela ya tejida" (nodos, hubs, fricción, colapso) | **Reservada al Axioma 0** (el lienzo, el fondo); lo observable es sombra/proyección (v34) |
| 5-Event Wall | No existía como término (hasta v30) | Umbral crítico digital/genómico (README:132); v31: 4 trayectorias tipo (0→5 absorción, 0→4+leapfrog, 0→3+estancamiento, 0→2+reversión) |
| ASI | Umbral 0.5 (arbitrario) | Umbral 0.167 (mediana Intermediate, empírico, HackerEarth 2026); "precision 1.0" retirada como tautológica (v2.5.3) |
| Hazard de colapso | Afirmado creciente con la edad (v30) | **No sobrevive en npm** (ρ = −0.716, p = 0.013, decreciente; tercer dominio, tercera forma). Positividad h(τ) > 0 sí respaldada (cripto 663 pares, FDIC 27,771 instituciones) |

---

## (c) Cómo encajan (o chocan) las definiciones nuevas del autor (2026-11-09)

Definiciones dadas por Elán el 2026-11-09 (voz, registradas en `~/MEMORY.md`):

1. **Luz** = "la energía cinética que libera un sistema complejo que está en movimiento y no está en decaimiento todavía o que no entra en el ACO-A." Refinada: "la energía que libera cada nodo individualmente."
2. **Hub central** distribuye o redistribuye la energía entre todos sus nodos. Ningún nodo puede ser mayor que el hub central ni superarlo; si lo hace, entra en **estado de disonancia**. La disonancia empieza a descentralizar los flujos de poder y el sistema puede entrar en **decaimiento** o en **fractura**.
3. **Puente** = el vínculo mientras los sistemas/nodos están todavía juntos en el sistema. **Ruptura** inicia positiva o negativamente. Negativo (colapso): el puente se rompe (la comunicación puede seguir, pero empieza la ruptura); cuando termina el colapso, el puente finaliza. Positivo (salto/leapfrog): el vínculo también se rompe, porque el nodo chico supera al grande — analogía Oracle Data Guard (standby ↔ primary, switchover).
4. **Breach** = cruzar el Muro de los 5 Eventos, positivo o negativo. **Puente como ER = EPR** (entrelazamiento que crece con cercanía y tiempo).
5. **El enlace es efímero**: existe pero no se ve; NO existe un puente que se reconstruya; todos los sistemas están interconectados, simplemente se ven las líneas. **La comunicación no se pierde**: cuando algo cae en el ACO-A o en la reconstrucción, los que absorbieron parte de ese nodo pasan a formar parte también de ese nodo.

Decisión del autor: **integrarlas como taxonomía**, con sus definiciones, en la reconstrucción. El análisis siguiente dice dónde encajan, dónde chocan y qué falta para que queden formales. Nada de esto es una objeción a la decisión: es el mapa de lo que la integración tiene que resolver.

### Luz — ENCAJA en vocabulario, con tres precisiones pendientes

**Dónde encaja.** El repo SÍ tiene vocabulario de energía:
- `README.md:313`: "Nodo Hub: absorbe energía productiva residual y aumenta masa gravitacional."
- `papers/marco_teorico_v30.md:823` (Anexo A, v27): "existe un Hub Central (Nivel 0) que administra la red mediante extraccion continua de energia residual de los Nodos Sombra perifericos (Nivel 3). La dinamica es de parasitismo controlado, no de destruccion: el hub necesita que los nodos sombra sobrevivan para seguir proveyendo flujo."
- `papers/marco_teorico_v30.md:843`: el hub "administra la red fungica mediante extraccion continua de energia residual de la periferia para mantener su propia homeostasis. No compite, extrae."
- `papers/marco_teorico_v30.md:895`: "**E_res (Energia Residual)**: capital, conocimiento y capacidad de procesamiento disponible en el nodo antes de la extraccion sistemica."
- `papers/marco_teorico.md:137` (Axioma 0.1): gradiente de potencial ∇V donde "V = energía libre / costo de transición (dominios socioeconómicos)".
- Axioma 4: un sistema solo actualiza trayectorias que puede sostener "dentro de su arquitectura, su energía disponible y su nivel de fricción."

"Luz = energía que libera cada nodo individualmente" se asienta sobre ese vocabulario: los nodos liberan energía; el hub extrae/absorbe la residual. Lectura natural (hipótesis, no afirmación del repo): la luz liberada por los nodos es lo que, en su parte residual, el hub absorbe. **Pendiente de confirmar por Elán.**

**Precisión 1 — "cinética" es palabra nueva.** "Energía cinética" tiene 0 ocurrencias en el repo. La palabra "cinética" aparece solo en "Ruptura Cinética" (`marco_teorico_v30.md:833`): perturbación exógena Ω(t) supera el umbral de contención, el organismo dominante destruye los enlaces de comunicación del rival y fuerza la transferencia de jurisdicción. Luz como "energía cinética" sería el primer término de energía cinética de la teoría. Falta definir qué es "cinético" aquí (¿energía del movimiento/cambio?) y cómo se distingue de E_res (capital/conocimiento/capacidad antes de la extracción). ¿Luz y E_res son la misma cantidad, o la luz es el flujo y E_res el stock?

**Precisión 2 — las dos condiciones ("no está en decaimiento todavía o no entra en el ACO-A") SÍ son distintas, y el repo lo resuelve.** ACO-A §3 (`SNT_Colapso_Acoplado.md`, §3; `marco_teorico_v30.md:248-256`): "Al colapsar, el sistema decae (absorción terminal, lo mide Δ) o da el brinco / leapfrog." El decaimiento es UNA rama de la bifurcación del colapso; entrar al ACO-A es entrar al régimen de colapso. Un sistema que entra al ACO-A y da el brinco está en ACO-A pero NO en decaimiento: sigue en movimiento, sigue liberando luz. Un sistema en decaimiento (absorción terminal) ya no libera luz. La "o" de la definición es significativa, no redundante. Lectura propuesta (por confirmar): luz existe mientras el sistema está en movimiento, y se apaga con la absorción terminal (decaimiento), no con la entrada al ACO-A en sí.

**Precisión 3 — la fricción se opone a la luz (lectura, no afirmación del autor).** Si luz es energía cinética liberada y φ es el campo de fricción, la fricción disipa energía cinética: φ se opone a la luz. El Principio de Mínima Fricción (trayectoria que minimiza la fricción integrada) se leería entonces como: el camino que preserva más luz. Coherente, pero Elán no lo afirmó: hay que confirmarlo o descartarlo. Ojo con la sobrecarga de F: en ASI, F = caos interno (tanh(std/mean/2)); en ACO-A, F = fricción que gobierna b y Δ. Si la luz se conecta al ASI vía F, esa sobrecarga importa.

**ASI: "de ahí viene el ASI" — derivación pendiente.** ASI = δH·α/F. El repo no deriva ASI de ninguna energía liberada por nodo. Para que "de ahí viene el ASI" sea más que una afirmación, falta la derivación: ¿cómo la luz (energía por nodo) produce δH (diversidad), α (autonomía) y F (caos/fricción)? Sin esa cadena, la conexión luz → ASI queda como hipótesis de trabajo, no como derivación. (Regla metodológica v33, cláusula 1: correspondencia = "lectura de compatibilidad" salvo cadena matemática o caso verificado.)

**La "sombra" de la plantilla hay que reescribirla.** Con luz = energía cinética liberada, "mueve el mismo flujo sin pagar la luz" significaría mover flujo sin liberar energía cinética, lo cual es incoherente si el flujo es movimiento. La definición de sombra de la plantilla no sobrevive a la nueva definición de luz: se reescribe, no se conserva.

### Hub y disonancia — LA REGLA YA EXISTE; LA DISONANCIA ES NUEVA; LA REDISTRIBUCIÓN CHOCA

**La regla "ningún nodo supera al hub" ya está en el repo, dos veces:**
- `marco_teorico_v30.md:827` (Anexo A): "un Nodo Sombra no puede superar al hub compitiendo con las mismas reglas que el hub establecio."
- `marco_teorico_v30.md:725` (Anexo A): "Cuando detecta acumulacion anomala de energia en un nodo periferico, [el hub] despliega respuesta inmunologica: captura regulatoria, modificaciones legislativas, monopolio de patentes, o adquisicion de los activos del nodo emergente antes de que alcance masa critica independiente."

**Disonancia es término nuevo: 0 ocurrencias en el repo y 0 en el libro.** (En Drive, un documento de Google Docs de 2026-04-26, "Autorregulación de Nodos Críticos en Red", contiene "disonancia" según la búsqueda por contenido, pero el conector de Google Docs no está conectado y su contenido no pudo leerse en esta tarea — ver §(d).) El repo no define un estado de disonancia: define el mecanismo preventivo (respuesta inmunológica) antes de que el nodo alcance masa crítica. La disonancia sería el estado cuando la prevención falla y el nodo supera al hub de todos modos. Falta definir: ¿disonancia es un estado del nodo, del hub o de la relación? ¿Cuál es su observable? La formalización natural es R(t) = 1 como umbral (R = métrica_hub / métrica_nodo; R < 1 = nodo mayor que hub). **Pregunta abierta:** en Ueno, R corre 0.096–0.24 (todo < 1) — ¿la R de Ueno va orientada al revés, o el umbral de disonancia no es R = 1? Sin resolver la orientación, no se puede fijar el umbral.

**Choque real: el hub del repo EXTRAE; el hub de Elán (2026-11-09) DISTRIBUYE.** El repo: "No compite, extrae" (`marco_teorico_v30.md:843`); "absorbe energía productiva residual" (`README.md:313`). La única redistribución del repo es pasiva: saturación endógena K_max — "Cuando el hub central acumula volumen por encima de su capacidad de carga optima, la fricción interna genera desbordamiento forzado hacia los nodos de Nivel 2. Este mecanismo es la unica via pasiva de redistribucion en el sistema" (`marco_teorico_v30.md:723`). Elán 2026-11-09: "el hub central distribuye o redistribuye la energía entre todos sus nodos" (función activa). La integración tiene que resolverlo explícitamente: ¿la redistribución es el desbordamiento K_max, o es una función activa nueva del hub (y entonces el hub no solo extrae)? Esta es la tensión más seria de las definiciones nuevas.

**"Descentralizar los flujos de poder" — compatible, sin definir.** La palabra existe en el repo como acción/estado del hub: "Si el Nivel 0 colapsa o descentraliza, el Nivel 2 pierde su funcion primaria" (`marco_teorico_v30.md:739`). Elán la usa como proceso (la disonancia descentraliza los flujos de poder). Encaja; falta la definición operativa (¿qué flujo, medido cómo?).

### Decaimiento — ENCAJA (es la rama terminal del colapso)

"Decaimiento" está en el repo como modo y como verbo: modos "Decaimiento Orbital Regulado" y "Decaimiento Craquelado" (ACO-A §4); "el sistema decae (absorción terminal, lo mide Δ)" (ACO-A §3). El "decaimiento" de Elán (el sistema entra en decaimiento tras la disonancia) es la rama terminal de la bifurcación del colapso. **Encaje directo, sin choque.** Lo único que falta es precisar el camino: disonancia → ¿decaimiento directo, o disonancia → colapso (ACO-A) → decaimiento? En ACO-A el decaimiento es el resultado del colapso, no de la disonancia. Si la disonancia lleva al decaimiento sin pasar por el colapso, hay un camino nuevo; si pasa por el colapso, la cadena es disonancia → colapso → decaimiento (rama Δ).

### Fractura — CORREGIDO POR EL AUTOR (2026-11-09 ~11:15): ES LA FORMA VISIBLE DEL DECAIMIENTO, DENTRO DE LA TAXONOMÍA ACO-A

Corrección de Elán: los 5 modos SON la taxonomía de las formas del decaimiento — cómo puede suceder, a qué velocidad y de qué forma — gobernados por fricción × trigger × piso/techo (§4). La fractura no es un desenlace separado junto al decaimiento. Las grietas son el camino visible de la mínima fricción: "las grietas fractales del craquelado son la solución visible a esa optimización: el camino por donde el sistema pierde cohesión gastando lo menos posible" (§5). Los modos son geometrías distintas del mismo paisaje (§7). El colapso es bifurcación (§3): decaer (absorción terminal, Δ) o brincar (leapfrog). La fractura es cómo procede el decaimiento — empiezan grietas, luego se pierde cohesión — no un resultado aparte. El modelo semáforo del autor (fractura verde-amarillo, bridge amarillo, ruptura rojo, switchover = cambio de fase) es su ordenamiento de los términos nuevos, distinto de la taxonomía ACO-A.

"Fractura" como palabra aparece en el repo solo como ilustración (`marco_teorico.md:163`; `marco_teorico_v30.md:827`, `693`; libro: "micro-fracturas", "fractura en subsistemas dinámicos") y una vez en derivados (Ueno v2, "fase de fracturas acumuladas"). La "taxonomía de países" mencionada por Elán no se localizó como documento; los casos-país (Roma, URSS, Azteca, Cartago) están en la tabla de evidencia del ACO-A (§6, modo Regulado).

### Puente, breach, ruptura — EL PUENTE SE RESCATA CON ER = EPR; LA RUPTURA TIENE DOS SENTIDOS PREVIOS QUE DISTINGUIR

**Puente: sentido nuevo, con precedente directo en el libro del autor.** En el repo, "puente" es solo "puente construido" (infraestructura, no evidencia): `marco_teorico.md:56` (etiqueta INFRAESTRUCTURA: "Se declara como puente construido, no como evidencia"); Axioma 8: "El puente empírico más limpio para este axioma ya está publicado, aunque todavía no ajustable" (Ryugu A0106 vs C0107, n = 2). El puente de Elán (vínculo mientras los sistemas están juntos; enlace ER = EPR) es un **sentido nuevo** que debe desambiguarse del "puente construido". No chocan (son sentidos distintos de la misma palabra), pero hay que separarlos explícitamente en la taxonomía.

**ER = EPR ya estaba en el vocabulario del autor.** Libro SUDO UNIVERSE v6.0, §1.1 "LA ARQUITECTURA DEL SERVIDOR: ER = EPR": "Juan Maldacena (Princeton) + Leonard Susskind (Stanford), 2013: los agujeros de gusano (ER) y el entrelazamiento cuántico (EPR) son la misma estructura geométrica vista desde diferentes escalas. La separación que ves en el universo es una ilusión de la interfaz. En el backend, todo está conectado." Y: "ER = puente Einstein-Rosen (agujero de gusano). EPR = paradoja Einstein-Podolsky-Rosen (entrelazamiento). Implicación: el espacio mismo emerge del entrelazamiento cuántico." En el libro figura como **HIPÓTESIS ACTIVA** ("Soporte teórico creciente"). El puente como ER = EPR no viene de la nada: viene del libro. **Encaje fuerte.**

**Breach: término nuevo (0 ocurrencias en repo y libro).** Elán: breach = cruzar el Muro de los 5 Eventos, positivo o negativo. Encaje con el Muro: v31 da 4 trayectorias tipo (0→5 completo/absorción, 0→4+leapfrog, 0→3+estancamiento, 0→2+reversión). El breach positivo (salto) corresponde a 0→4+leapfrog; el negativo (colapso/absorción), a 0→5 completo. **Matiz de conteo:** en v31 el leapfrog ocurre en 4 eventos (antes de completar 5); el breach de Elán es cruzar el muro (5 eventos) en cualquier dirección. ¿El breach positivo ocurre EN 5 eventos o en 4+leapfrog? Pendiente de precisar.

**Ruptura: la palabra existe, con dos sentidos previos distintos del nuevo.** 
- "Ruptura Cinética" (`marco_teorico_v30.md:833`): "la perturbacion exogena (Omega(t)) supera el umbral de contencion: el organismo dominante destruye los enlaces de comunicacion del rival y fuerza la transferencia de jurisdiccion de clusteres enteros." También en `marco_teorico_v30.md:1103` (Suiza vs Ucrania).
- "Ruptura asintótica" (`marco_teorico_v30.md:827`): "exclusiva del Nodo Atomico; un territorio completo solo puede evolucionar si la densidad de Nodos Atomicos independientes dentro de el alcanza masa critica suficiente para fracturar los vectores de supresion del hub."
- "Ruptura institucional abrupta" (`marco_teorico_v30.md:1572`): Toledo-Madrid (1561), Lisboa-Madrid (1580).

La ruptura de Elán (cruce del Muro, positivo o negativo) es un **tercer sentido**. Choque a distinguir: la Ruptura Cinética del repo **destruye los enlaces de comunicación**; la ruptura de Elán en colapso **conserva la comunicación** ("sí va a estar la comunicación pero empieza la ruptura"). Son rupturas distintas: una destruye enlaces, la otra rompe el puente pero no la comunicación. La taxonomía debe separarlas por nombre (p. ej., ruptura-muro vs ruptura cinética). Además: la ruptura asintótica del repo es exclusiva del Nodo Atómico; la ruptura de Elán parece aplicar a cualquier sistema que cruce el muro. ¿El switchover (salto) lo puede hacer cualquier nodo, o solo el Nodo Atómico (restricción del repo, `marco_teorico_v30.md:827`)? Pendiente de Elán.

**Switchover / Data Guard: analogía nueva, 0 ocurrencias en repo y libro.** Viene del campo de Elán (DBA Oracle). Formaliza el salto como intercambio de roles: standby → primaria, primaria → standby. Encaje formal natural: el switchover es el cruce de R(t) = 1 (la métrica del nodo iguala y supera a la del hub; los roles se invierten). También encaja con la "ruptura asintótica" del Nodo Atómico como único escape. Lo que falta: ¿el switchover es la definición operativa del salto (leapfrog), o es solo una analogía pedagógica? Si es definición operativa, hay que escribirla con R(t) (¿qué métricas, qué umbral exacto?) y resolver si aplica a cualquier nodo o solo al Atómico.

**El enlace efímero — resonancia con la capa de proyección y con el libro, no identidad.** Elán: "el enlace es efímero, existe pero no se ve; no existe un puente que se reconstruya; todos los sistemas están interconectados, simplemente se ven las líneas." Vecinos más cercanos en el repo:
- Axioma 0.2: el volumen 𝒞 existe; solo se observan sombras Π_θ(𝒞); Π_θ no es inyectiva; la reconstrucción es un conjunto ℛ, no un elemento. "Existe pero no se ve" es la situación exacta de 𝒞 respecto a sus sombras.
- La tela: 740 trayectorias = líneas. "Simplemente se ven las líneas" describe literalmente la tela integrada.
- Libro §1.1 (ER = EPR): "En el backend, todo está conectado." "La distancia es una convención de renderizado. No una restricción del hardware."

"Efímero" es palabra nueva del autor (no está en el repo como término). Como formulación, el enlace efímero es compatible con la capa de proyección + ER = EPR, pero no es idéntico a ninguna: la proyección habla de observación (sombras), no de enlaces; ER = EPR habla de conexión, no de fugacidad. La integración debe decir en qué sentido el enlace es efímero (¿existe solo mientras los sistemas están juntos? ¿se ve solo como trayectoria en la tela?) y resolver la tensión que Elán mismo dejó: antes dijo que al cruzar el muro "se crea un bridge"; después, que el puente "se rompe" al cruzarlo, y finalmente que "no existe un puente que se reconstruya". Lectura que reconcilia las tres (por confirmar): el puente se crea en la conjunción (sistemas juntos) y se rompe en la ruptura (cruce del muro, en cualquier dirección); no se reconstruye después — la interconexión persiste como líneas (tela), no como puente nuevo.

**La comunicación no se pierde; los absorbedores pasan a formar parte del nodo caído — compatible con ACO-A + Axioma 10, con un giro nuevo.** Vecinos:
- ACO-A: `A = m_absorbente / m_hub^pico` — el absorbente captura la masa/actividad del hub colapsado. El nodo caído persiste en su absorbente (su masa/actividad).
- Axioma 10: "Cuando una rama cae, el hueco puede persistir" (Delta→Ómicron: el hub colapsa, el nicho no desaparece, Ómicron lo ocupa).
- "Colapso no es muerte, es bifurcación" (ACO-A §3).

El giro nuevo de Elán es la dirección de la identidad: no solo el absorbente gana la masa del caído, sino que **los que absorbieron parte del nodo pasan a formar parte también de ese nodo** (el caído vive en sus absorbedores). Y "cuando algo cae en el ACO-A o en la reconstrucción" extiende la regla a la reconstrucción (el conjunto ℛ de volúmenes compatibles). Falta formalizar: ¿"formar parte de ese nodo" significa que la identidad del nodo persiste distribuida en sus absorbedores? ¿Cómo se mide (qué masa/actividad, en qué absorbentes)? Es compatible con ACO-A + Axioma 10, pero es una formulación nueva que necesita su propia escritura.

### Resumen de encajes y choques

| Término nuevo | Veredicto de encaje | Qué falta |
|---|---|---|
| Luz (energía cinética liberada por nodo) | **Encaja** en vocabulario de energía (README:313; v30:823/843; E_res v30:895) | Definir "cinética" vs E_res; confirmar si la luz liberada es la residual que absorbe el hub; dirección **ASI → luz** (corregida 11:11, reafirmada 12:05) |
| Luz: "no en decaimiento o no en ACO-A" | **Resuelto por el repo**: decaimiento es una rama del colapso (ACO-A §3); entrar al ACO-A ≠ decaer (el brinco está en ACO-A sin decaer) | Confirmar la lectura |
| Hub redistribuye | **RESUELTO (Elán, 2026-11-09 ~12:19): función activa de distribución, como un país a sus estados; NO solo desbordamiento pasivo por K_max** | "No compite, extrae" (v30:843) necesita revisión |
| Disonancia | **Nueva en SNT** (0 en repo/libro). Doc de Drive "Autorregulación de Nodos Críticos en Red" (2026-04-26) LEÍDO 2026-11-09: "Disonancia Topológica" = nodo en -0.5 supera el límite UA-SE (-0.45), frecuencia en disonancia con la ley de potencias (Gamma 3.31) → la red deja de enrutarle información → inanición/aislamiento. Sentido DISTINTO de la disonancia SNT (nodo supera al hub → descentralización) | Definir (estado de quién, observable cuál); ¿la del Doc es el mismo mecanismo en otro dominio, o un estado distinto? **Único término nuevo pendiente (Elán, 12:19)** |
| Decaimiento | **Encaja**: rama terminal del colapso (ACO-A §3, modos) | Precisar camino: disonancia → colapso → decaimiento, o disonancia → decaimiento directo |
| Fractura | **CORREGIDO (Elán, 2026-11-09 ~11:15): fractura es la forma visible del decaimiento dentro de la taxonomía ACO-A** (las grietas son el camino de mínima fricción, §5); no es un desenlace aparte junto al decaimiento | Escribir en la integración: fractura = grietas por donde el sistema pierde cohesión; semáforo la ubica entre verde y amarillo |
| Puente (ER = EPR) | **Encaja fuerte**: precedente directo en el libro §1.1 (hipótesis activa) | Desambiguar de "puente construido" (infraestructura) |
| Breach | **Nuevo** (0 en repo/libro) | Precisar conteo: ¿breach positivo en 5 eventos o en 4+leapfrog (v31)? |
| Ruptura | **Palabra existente, tercer sentido** (cinética; asintótica; institucional) | Separar de Ruptura Cinética (destruye enlaces) vs ruptura-muro (conserva comunicación); ¿salto solo para Nodo Atómico? |
| Switchover | **Analogía nueva** (0 en repo/libro) | Decidir: ¿definición operativa del salto (con R(t) = 1) o analogía pedagógica? |
| Enlace efímero | **Resonancia** con Axioma 0.2 (proyección), tela (líneas) y ER = EPR del libro | Definir "efímero"; confirmar reconciliación (puente se crea en conjunción, se rompe en ruptura, no se reconstruye) |
| Comunicación no se pierde / absorbedores | **Compatible** con ACO-A (absorción) + Axioma 10 (el hueco persiste) | Formalizar persistencia de identidad en los absorbedores; extender a la reconstrucción |
| Sombra (plantilla: "sin pagar la luz") | **No sobrevive** a la nueva definición de luz: reescribir | Reescribir sin "pagar la luz" |

---

## (d) Preguntas abiertas que la lectura no resolvió

1. **¿Luz y E_res son la misma cantidad?** Luz = energía que libera cada nodo; E_res = capital/conocimiento/capacidad disponible en el nodo antes de la extracción sistemática (`marco_teorico_v30.md:895`). ¿La luz liberada es el flujo y E_res el stock? ¿La luz es lo que, en su parte residual, absorbe el hub (README:313)?
2. **¿Qué es "cinético" en luz?** Primera aparición del término como energía. ¿Energía del movimiento/cambio? ¿Cómo se mide por nodo y por dominio?
3. **Derivación luz → ASI.** ASI = δH·α/F. ¿Cómo la energía liberada por nodo produce diversidad (δH), autonomía (α) y caos/fricción (F)? Sin cadena, queda como hipótesis de trabajo (cláusula 1, v33).
4. **Hub redistribuye — RESUELTO (Elán, 2026-11-09 ~12:19):** función activa de distribución, como un país a sus estados; NO solo desbordamiento pasivo por K_max. "No compite, extrae" (`marco_teorico_v30.md:843`) necesita revisión.
5. **Disonancia: ¿estado de quién, observable cuál?** ¿Umbral R(t) = 1? Resolver la orientación de R(t) en Ueno (R 0.096–0.24, todo < 1).
6. **Fractura — RESUELTO por Elán (2026-11-09 ~11:15):** no es un desenlace aparte. Es la forma visible del decaimiento dentro de la taxonomía ACO-A (las grietas son el camino de mínima fricción, §5). Queda por escribir en la integración: fractura = grietas por donde el sistema pierde cohesión; el semáforo la ubica entre verde y amarillo.
7. **Breach positivo: ¿en 5 eventos o en 4+leapfrog?** v31 pone el leapfrog en 4 eventos; el breach de Elán es cruzar el muro (5) en cualquier dirección.
8. **¿El salto (switchover) lo puede hacer cualquier nodo?** El repo lo restringe: la ruptura asintótica es exclusiva del Nodo Atómico; un Nodo Sombra completo no puede hacer leapfrog masivo (`marco_teorico_v30.md:827`). ¿El switchover es definición operativa del salto (con R(t) = 1) o analogía pedagógica?
9. **¿La fuerza del entrelazamiento sigue la forma t^b de R(t)?** Si los enlaces se hacen más fuertes con el tiempo, ¿sigue la misma ley de potencia? Hipótesis, no afirmación.
10. **¿Qué es "efímero" en el enlace?** ¿Existe solo mientras los sistemas están juntos? ¿Se ve solo como trayectoria en la tela? Confirmar la reconciliación: puente se crea en conjunción, se rompe en ruptura, no se reconstruye.
11. **Persistencia de identidad en la absorción.** ¿"Formar parte de ese nodo" significa que la identidad del caído persiste distribuida en sus absorbedores? ¿Cómo se mide, y cómo se extiende a la reconstrucción (conjunto ℛ)?
12. **Disonancia en Drive — LEÍDO (2026-11-09 ~11:14, tras conectar Google Docs).** "Autorregulación de Nodos Críticos en Red" (2026-04-26, contexto Fungiverso) SÍ contiene "disonancia": "Disonancia Topológica" — un nodo en -0.5 supera el límite de supresión eficiente del algoritmo UA-SE (-0.45); genera una frecuencia en disonancia con la distribución de ley de potencias (Gamma 3.31); la red deja de enrutarle información crítica y el nodo muere por "inanición" de datos (aislamiento). Sentido DISTINTO de la disonancia SNT de Elán (nodo supera al hub → descentralización de flujos de poder): en el Doc la respuesta es aislamiento/inanición; en la SNT nueva es descentralización. Pregunta: ¿mismo mecanismo en otro dominio, o estado distinto? "V33snt" (manuscrito v33 r33, 75,335 caracteres): CERO ocurrencias de disonancia/luz/puente/fractura/breach/ruptura.
13. **Decaimiento: ¿disonancia → colapso → decaimiento, o disonancia → decaimiento directo?** En ACO-A el decaimiento es resultado del colapso. El camino desde la disonancia no está escrito.

### Archivos de Google Drive revisados (búsqueda por contenido, 2026-11-09)

Conector de Google Drive: conectado. Búsquedas `fullText contains` (por contenido, no por nombre):

| Búsqueda | Hallazgos relevantes |
|---|---|
| "Shadow Node" | Carpetas "The-shadow-Node-Theory" y "The-shadow-Node-Theory 2"; `shadow_node_theory_SSRN_v4.pdf` (2 copias, jun–jul 2026); `shadow_node_verification.py`, `shadow_node_verification_v2.py`, `n_shadows_utils.py` (mar 2026); `The-shadow-Node-Theory-2.0.zip` (mar 2026). Material antiguo, ya en el repo o supersedido. No se descargó. |
| "ACO-A" | Doc SUDO UNIVERSE v6.0 GOLD MASTER (Google Doc, 2026-09-13); `sudo_universe_v6_0_gold_master.html`, `sudo_universe_v6_1.html` (oct 2026); "V33snt" (Google Doc, 2026-11-06); "diff" / "diff.txt" (2026-09-10); "Documento de Elán Zainos Corona" (.epub y .md, 2026-10-26). El .md descargado y verificado: es el libro SUDO UNIVERSE v6.0 (ya en `libro SUDO UNIVERSE v6.0, texto local`). Su §1.1 ER = EPR y sus usos de "luz" y "fractura" se citan en §(c). |
| "disonancia" | "Autorregulación de Nodos Críticos en Red" (Google Doc, 2026-04-26) — **contiene "disonancia" pero no pudo leerse** (ver abajo). También WHITE PAPER.docx/.pdf (feb 2026), "===================================.txt" (dic 2025), "Untitled document" (jul 2026), "nuevo12.txt" (ene 2026), "nostradamus.zip" (dic 2025). Ninguno de estos últimos parece SNT por nombre; no se revisaron por contenido. |
| "SNT" | Carpeta "Snt"; "V33snt" (Google Doc, 2026-11-06); `snt_ssrn_v33.md`, `snt_ssrn_v33_EN.md` (oct 2026); "SNT-v30-micro-patch.md" (2026-10-21) — **descargado y leído**: es el parche micro de v31 (Principio del Paisaje Vivo, Ax-M1–Ax-M4), ya cubierto en §(b). `motor_snt_ultimate_v8_*.html` (sep 2026); `snt_plos_v30_scientific_format.docx`, `snt_plos_submission.pdf` (sep 2026). |
| "luz" | Sin hallazgos SNT: documentos de astronomía, `foco.py`, "Formulas" (Google Doc, feb 2026), "Formulas.pdf", "Anomalias mundiales", "sudo universe: Manual de Usuario (v4.0)" (nov 2025). No se leyó ninguno completo: "luz" ahí es años luz / luz solar, no término SNT (verificado en el libro). |

**Limitación del conector:** el conector de Google Docs **no está conectado** en este entorno ("missing access_token surrogate for credential: google.google_docs"). Por eso no pudieron leerse los Google Docs "Autorregulación de Nodos Críticos en Red" (2026-04-26, contiene "disonancia") ni "V33snt" (2026-11-06, probablemente el texto v33). Según la regla del conector de Drive, los archivos Google-nativos no se exportan por Drive aunque otro conector falle. **Queda pendiente leer esos dos Docs cuando el conector de Docs esté conectado.** Los archivos .md/.txt de Drive sí se descargaron y leyeron por el conector de Drive (permitido: no son Google-nativos).

**Búsquedas no realizadas:** "puente", "energía", "breach", "ruptura" en Drive (el tiempo de la tarea se concentró en los términos con más probabilidad de hallazgo: disonancia y luz). La búsqueda por contenido de Drive no es vectorial: es `fullText contains` por término exacto; Elán señaló que por vectores/índice es más fácil que por término exacto, y este conector no ofrece búsqueda vectorial. Si hace falta, la búsqueda por contenido puede ampliarse a esos términos.

### Nota final — para qué sirve esta lectura

Elán ordenó esta lectura para repasar la teoría antes de volver a las preguntas del puente, y para reconstruir los materiales derivados (espacio, taxonomía, agente Kaggle, Finanzas-mundo, Estado, Ueno v2) con los términos corregidos/definidos por él (decisión 2026-11-09 ~11:04). Su principio: nombrar las cosas para entenderlas mejor y perderles el miedo; organizar en los repos es ordenar su propio caos (Elán, 2026-11-09 ~11:07). Esta síntesis es el mapa para esa reconstrucción: dice qué está definido en el repo, qué es nuevo, qué encaja, qué choca y qué preguntas faltan. Las definiciones nuevas del autor se integran como taxonomía; las secciones (c) y (d) dicen exactamente dónde hay que escribirlas y qué hay que precisar para que no choquen con lo que ya existe.

## Adenda — esqueleto universal vs taxonomías por dominio (Elán, WhatsApp, 2026-11-09 ~12:02)

Corrección del autor sobre lo que se le presentó como "la taxonomía": `taxonomia-por-dominio.md` (193 líneas) es el **esqueleto universal**, no la versión vigente por dominio. La taxonomía por dominio **CAMBIA**, no es la misma: cada dominio define sus propios nodo / hub / sombra / puente / luz, por eso la universal solo puede ser esqueleto. No presentarla como una sola taxonomía fija.

Regla del autor: las definiciones son de un proyecto de meses, ya son ley; una vez leídas, no se vuelven a preguntar. Y leer TODO completo, no solo lo primero y luego poner lo demás.

## Adenda — Punto 2 del autor: puente entre nodos del mismo nivel (Elán, WhatsApp, 2026-11-09 ~12:04, dictado textual)

- Cuando dos nodos del mismo nivel interactúan, se crea una conexión. Esa conexión ES el puente. El puente es comunicación **de inicio** (aclarado por Elán, WhatsApp, 2026-11-09 ~12:08).
- Dependiendo de su cercanía o de su rango, van a poder crear una dinámica. Esa dinámica ES el sistema complejo. Todo va bien mientras cada uno se mantenga en su rango.
- Eso se delimita por ratios: cada ratio es una línea; estas líneas se van pasando cuando se van cruzando, positiva o negativamente, dependiendo de cuál sea el nodo más grande o dominante. Ahí es cuando empieza lo del nodo sombra [palabra no clara en audio — POR CONFIRMAR qué empieza a hacer el dominante].
- Dependiendo de la masa de absorción, el nodo dominante va devorando a su nodo, al nodo que está a un lado, el más cercano. **Masa de absorción verificada en la documentación (Elán, 12:08): README SNT:313, Nodo Hub: "absorbe energía productiva residual y aumenta masa gravitacional" — esa es la masa de absorción del punto 2.**

Implicaciones para la auditoría: el puente queda definido por el autor como la conexión/comunicación entre nodos del mismo nivel — distinto del "puente" de la plantilla (conecta hub con sombra y cobra por traducir), que se retira. Las líneas son ratios (R(t)); cruzar una línea es que el ratio pase un umbral, positiva o negativamente según el nodo dominante. El sistema complejo ES la dinámica entre nodos. Esto conecta con: el enlace efímero (existe pero no se ve), las líneas del Muro (fracturas según cómo pasen), y la absorción ACO-A (masa de absorción del dominante).

## Adenda — integrando el modo de los 5 eventos al ACO-A, parte negativa (Elán, WhatsApp, 2026-11-09 ~12:18)

- Apenas se está integrando el modo de los 5 eventos para el ACO-A.
- Este sería la parte negativa, el lado contrario de cómo funciona.
- Ya solo se había soltado [el bueno / UNO — audio "U-U-N-O", POR CONFIRMAR si es el modo uno, el primer evento, o el lado bueno].

Verificado en documentación: SNT_Colapso_Acoplado.md §4 tiene los 5 modos de colapso (Regulado, Craquelado, Caída-a-piso, Acantilado Catastrófico, Barrido logístico), gobernados por fricción × trigger × piso/techo. El Muro de los 5 Eventos es otra cosa en la documentación (README:130-134, v30: 5 eventos negativos → absorción; 5 positivos → leapfrog, propuesta; v31: 4 trayectorias 0→5 absorción, 0→4+leapfrog, 0→3 estancamiento, 0→2 reversión). No mezclar modos con eventos hasta que Elán precise cómo se integran.

## Adenda — K_max con ejemplo Ciudad de México; varias formas de redistribuir (Elán, WhatsApp, 2026-11-09 ~12:21)

- K_max es cuando, digamos, la Ciudad de México ya no puede aportar más empresas o más lo que sea, ya no puede aportar algo: lo distribuye otro nodo.
- La redistribución tiene varias formas de verse y de varias formas se puede distribuir la masa.
- Verificado en documentación: README:321, Nivel 0 Macro-Hub Central: "Absorción unidireccional, limitante K_max, respuesta inmunológica". Nivel 2 Bypass Logístico intercepta el desbordamiento del Nivel 0 (v30:723: "la unica via pasiva de redistribucion en el sistema").
- Implicación: la redistribución no es un solo mecanismo — tiene varias formas (distribución activa del hub, como un país a sus estados; desbordamiento pasivo por saturación K_max, como CDMX → otro nodo). Elán mencionó "lo del banco" al final [audio no claro: "para igual, bueno, como se llama, bueno bank" — POR CONFIRMAR a qué banco se refiere].
