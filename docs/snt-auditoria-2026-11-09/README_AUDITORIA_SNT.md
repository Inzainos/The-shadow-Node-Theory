# Auditoría SNT — documentos del 2026-11-09 (para revisión)

Subidos a esta rama por orden de Elán (WhatsApp, 2026-11-09 ~19:18: "Sube lo que se actualizó y lo revisamos").
**Nada de esto va a main desde aquí: es material para revisar.**

## Qué hay aquí

Auditoría de términos de la Shadow Node Theory (SNT v2.7.5.1, marco v34), trabajo del
chat general del 2026-11-09:

| Archivo | Contenido |
|---|---|
| `TEORIA_ATRAS_ADELANTE.md` | Síntesis de la teoría: qué dice la documentación, término por término, con fuentes |
| `AUDITORIA_VEREDICTOS.md` | Veredictos de la auditoría |
| `EVIDENCIA_TERMINOS.md` | Evidencia por término, con citas archivo:línea del repo, del espacio SNT y de los papers |
| `QUE_DICEN_LOS_PAPERS_SNT.md` | Qué dicen los 11 papers leídos completos (y qué NO dicen: puente, luz como concepto SNT, switchover, breach, disonancia, fractura como modo de colapso, entre otros) |

## Qué cambió respecto a los originales locales

Solo portabilidad, para que los documentos se lean en GitHub:

- Las rutas locales (`~/workspace/snt-repo/...`) se reemplazaron por referencias del repo
  (`papers/...`, `AGENTS.md`, `Inzainos/The-shadow-Node-Theory`).
- Las rutas a archivos locales de trabajo se marcaron como tales
  (p. ej. `taxonomia-por-dominio.md (archivo local de trabajo)`).
- El contenido, las citas y los veredictos **no se tocaron**.
- Verificado: 0 ocurrencias de la frase retirada en v3.1 en estos 4 archivos.

Nota: la línea final de `QUE_DICEN_LOS_PAPERS_SNT.md` ("no se subió nada a GitHub")
refleja el estado al momento de escribir el informe; esta subida es la excepción,
hecha para su revisión.

## Qué NO es esto

- No modifica la teoría: `papers/marco_teorico.md` (v34) y los demás documentos del
  marco no se tocan en esta rama.
- No toca el espacio SNT.
- No aplica los 19 cambios del Apéndice C.1 (lista en `modelo-ueno-resultados-v2.md`,
  ya en GitHub en `docs/ueno-2026-11-07/`): esos siguen pendientes del visto bueno de
  Elán para aplicarlos al espacio.
- No modifica ningún paper.

## Definiciones corregidas el 2026-11-09 (de Elán, en audio)

- ASI crea la luz, nunca luz → ASI.
- El hub distribuye activamente energía entre sus nodos, no solo por desborde de K_max.
- Puente = comunicación de inicio entre nodos del mismo nivel.
- Fractura es cómo avanza el decaimiento, no un resultado aparte.
- Disonancia es el único término nuevo pendiente (no está en la documentación SNT).

## Revisión

Revisan Elán y el chat general (auditoría SNT). Después de la revisión, Elán decide
qué se integra y qué se corrige.
