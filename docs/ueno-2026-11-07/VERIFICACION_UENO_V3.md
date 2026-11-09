# Verificación — Forecast CSV v3 y copias de registro Ueno v3

Fecha: 2026-11-09. Staging: `docs/ueno-2026-11-07/`.
Fuentes leídas completas (Regla 0): `auditoria-terminos/ (no incluido en el repo)REVISION_DOCUMENTOS_UENO.md`
(564 líneas), `docs/ueno-2026-11-07/forecast-ueno-valores.csv`, `docs/ueno-2026-11-07/forecast-ueno-2026-11-06.md`.
No se modificó nada en `docs/ueno-2026-11-07/` ni en el espacio SNT. No se subió nada a GitHub. No se crearon chats.

## Tarea 1 — forecast-ueno-valores-v3.csv

- Original: 71 líneas, 5.706 B, md5 `cce53a6cbdbe53e425779633743958af`
  (coincide con el md5 declarado en forecast-ueno-2026-11-06.md L3),
  sha256 `61d11b72aca15c88e899e4a9e25cff36f0580516e67e40aea9d8147680c5c5f0`.
- v3: 70 líneas, 5.616 B, md5 `d80bf8359a79557b74cb8588c2d990f1`,
  sha256 `3a5fa7d90880e267a3a43f756f3d80c7dc4f38549aa089822e111205fb7bafdb`.
- Cambios (únicos): se eliminó L2 (cabecera duplicada) y L46
  `(30 oct 2025)` → `(30 oct 2026)` (ahora L45 de v3). Finales de línea CRLF preservados.
- Verificación: comparadas las 70 líneas una a una contra el original sin L2 —
  difiere EXACTAMENTE 1 línea (la del 30 oct), y solo en `2025`→`2026` dentro del
  texto de referencia `(30 oct ...)`. Todos los tokens numéricos son idénticos.
  Ningún valor numérico cambió; no hubo nada que detener.

### diff original → v3 (también en `forecast-ueno-valores-v3.diff`)

```diff
2d1
< seccion,banco,usd_sep2026,gs_sep2026,total_usd_equiv_sep2026,share_sep2026,R_X_sep2026,,
46c45
< cartera_total_implicita_ESTIMADO,20927835051546,,2.03 billones / 9.70% (30 oct 2025),ESTIMADO
---
> cartera_total_implicita_ESTIMADO,20927835051546,,2.03 billones / 9.70% (30 oct 2026),ESTIMADO
```

## Tarea 2 — copias de registro (cuerpo verificado contra el original)

Cabecera de registro añadida al inicio de cada copia de texto (archivo de registro,
versión, SIN CAMBIOS, fecha 2026-11-09, md5/sha256 original). Los CSV se copiaron
byte a byte SIN cabecera dentro, con archivo `.NOTA.md` acompañante (la huella, con
el nombre pedido `ueno-huella-cimatica-NOTA.md`). Verificación independiente:
para textos, md5 de la cola de N bytes de la copia == md5 del original; para CSV,
md5 copia == md5 original.

| Copia en staging | Bytes copia | md5 original | md5 cuerpo/copia | Verificación |
|---|---|---|---|---|
| modelo-ueno-resultados.md (v1) | 32.200 | 61d0497454d5ab7c068e7834ae17195c | 61d0497454d5ab7c068e7834ae17195c | OK cuerpo==original |
| modelo-ueno-resultados-v2.md (v2) | 51.296 | 986d79b469c031dc345638347b5bb616 | 986d79b469c031dc345638347b5bb616 | OK cuerpo==original |
| modelo-ueno-valores.csv (v1) | 2.920 | d41df2e5f4bf62898b45ae6659291a3d | d41df2e5f4bf62898b45ae6659291a3d | OK byte-a-byte |
| modelo-ueno-valores-v2.csv (v2) | 4.017 | 38977724d76307f5913540f0f11abbed | 38977724d76307f5913540f0f11abbed | OK byte-a-byte |
| tabla-maestra-ueno-mef.csv (vigente) | 12.335 | 7c22f9f046a67d6e950cb54afef38f12 | 7c22f9f046a67d6e950cb54afef38f12 | OK byte-a-byte |
| tabla-maestra-ueno-mef-v1.csv (v1) | 11.535 | 69566dc48555fdf4bec452d6e2772809 | 69566dc48555fdf4bec452d6e2772809 | OK byte-a-byte |
| tabla-maestra-NOTAS-v1.md (v1) | 15.647 | b1daaaf57c4646926027a27cb0733705 | b1daaaf57c4646926027a27cb0733705 | OK cuerpo==original |
| tabla-maestra-NOTAS.md (vigente, + nota H-5/H-6) | 25.169 | 761b2f71aad18322be90ab08b28c7e22 | 761b2f71aad18322be90ab08b28c7e22 | OK cuerpo==original |
| forecast-ueno-2026-11-06.md (sin nº versión; punto partida v2) | 33.577 | d1260013838662e8b7309b43dcc7510a | d1260013838662e8b7309b43dcc7510a | OK cuerpo==original |
| ueno-acoa-tela-cimatica-incertidumbre.md (marco v2.7.5.1/v34) | 24.743 | 8eca6f13c5a299108056227cf2f7fb19 | 8eca6f13c5a299108056227cf2f7fb19 | OK cuerpo==original |
| ueno-huella-cimatica.csv | 420 | fafc1c01b5d123ad9cc52c3104804a92 | fafc1c01b5d123ad9cc52c3104804a92 | OK byte-a-byte |
| finanzas-mundo-snt.md (sin nº versión) | 34.643 | f26ef328d479325173e7d491aa2bf24b | f26ef328d479325173e7d491aa2bf24b | OK cuerpo==original |
| video-largo-ueno/guion-video-largo.txt (BORRADOR orig. + nota estado) | 19.566 | ee24ade86441f03e0e8ccd19581ce309 | ee24ade86441f03e0e8ccd19581ce309 | OK cuerpo==original |
| video-resumen-ueno/guion-video.txt (+ nota estado) | 6.643 | 7beef5344cbb7e3e9fec44defde53acd | 7beef5344cbb7e3e9fec44defde53acd | OK cuerpo==original |

Notas acompañantes: `modelo-ueno-valores.csv.NOTA.md` (586 B),
`modelo-ueno-valores-v2.csv.NOTA.md` (592 B), `tabla-maestra-ueno-mef.csv.NOTA.md` (640 B),
`tabla-maestra-ueno-mef-v1.csv.NOTA.md` (599 B), `ueno-huella-cimatica-NOTA.md` (1.492 B).

### Notas especiales añadidas (solo cabeceras; cuerpos intactos)

- **tabla-maestra-NOTAS.md — H-5/H-6 (auditoría §2.9):** H-5: 38 archivos en disco,
  39 filas MEF PDF, dic 2023 contado dos veces; el "38" de v2 no es el mismo "38" actual
  (v2 incluía dic 2023 y no mar 2026; actual incluye mar 2026 y no dic 2023).
  H-6: oct 2024 clasificado en patrón guion bajo pero su URL real es
  `https://www.mef.gov.py/sites/default/files/2024-11/archivo_4.pdf` (patrón genérico,
  verificado en `mef-informe-bancos/download_log.csv`); reparto real 16 estándar +
  6 guion bajo + 16 genéricos = 38.
- **ueno-huella-cimatica-NOTA.md:** A4 0.717 no está en el CSV (solo A1/A2/A3);
  fuente tela L161. Denominadores LOO 737 vs 740 sin explicar (tela L209-211, L220, L361);
  GAP de método.
- **Guion video largo — estado:** la auditoría §5.4 documenta la inconsistencia
  BORRADOR (cabecera del guion) vs publicado en YouTube
  (`https://www.youtube.com/watch?v=kRJQKBUc6dI`, según el PDF). Elán confirmó
  2026-11-09 ~12:39 que SÍ está publicado en esa URL (verificado en vivo; descripción
  con números v2, 30 meses) — registrado en MEMORY.md. La nota en la copia recoge
  ambas cosas: la inconsistencia documentada y la confirmación posterior; la cabecera
  BORRADOR quedó desactualizada y el estado vigente es PUBLICADO. La actualización en
  redes con números v3 queda pendiente y NO es parte de esta copia.
- **Guion video resumen — estado:** para este guion NO se afirma que esté publicado;
  pendiente confirmar con Elán. La nota cita la confirmación del video largo solo como referencia.

## Lo que NO se pudo verificar / no se hizo

- Nada quedó sin verificar dentro de esta tarea: todas las copias verificadas por md5
  (cuerpo o byte-a-byte) y el forecast v3 verificado línea por línea y por tokens numéricos.
- No se copiaron PDFs, mp3, mp4 ni PNG; no se copió `capitulos.txt` ni `topics.txt`
  (no pedido; `topics.txt` no existe según auditoría §1.3). No se copió el PDF del informe.
- No se verificó en vivo el estado de publicación del video resumen ni de las piezas
  de redes (LinkedIn/Facebook/Instagram) — fuera del alcance de esta tarea (sin navegador
  en este subagente) y pendiente de confirmación con Elán.
- La actualización en redes con números v3 ordenada por Elán (MEMORY.md 2026-11-09 ~12:39)
  NO se realizó: no forma parte de esta tarea.

## Archivos en staging NO creados por este constructor

Durante el trabajo, otro proceso escribió en el mismo staging:
`modelo-ueno-resultados-v3.md` (13.955 B, md5 `347e9a57a78df40fd6911a5e0afb23d1`)
y `verificar_v3.py` (8.137 B, md5 `a7c88e5116c515195e6d4c227ae89fff`).
No se tocaron ni se verifican aquí; mis archivos se re-verificaron después y sus hashes
siguen intactos.
