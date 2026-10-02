"""
Construye la cohorte npm del pre-registro 2026-10-02 (capa ACO-A en software libre).

Pre-registro: reconstruction_real/preregistro/PREREGISTRO_NPM_2026-10-02.md
(commit 3ff9fca, subido antes de descargar cualquier dato de analisis).

Etapas, todas con cache en disco para poder reanudar:
    A. Muestreo sistematico de 12,000 nombres desde replicate.npmjs.com/_all_docs
       (una de cada k filas; desplazamiento inicial derivado de la semilla 20261002).
    B. Metadatos del registro por paquete: nacimiento, deprecated, repositorio.
    C. Filtros de fecha del pre-registro (nacido 2015-07-01..2024-10-02, no despublicado).
    D. Series de descargas diarias, en peticiones bulk de 128 paquetes y ventanas de
       18 meses (limites del servicio, verificados el 2026-10-02).
    E. Agregacion mensual, filtro de actividad (>= 1,000 descargas en los primeros
       180 dias), ajuste de b_subida y Delta_caida, extincion funcional.
    F. Avisos OSV y clase de disparador (abrupto / anunciado / sin clasificar).

Salidas:
    data/raw_npm/                                (no versionado; ver .gitignore)
    reconstruction_real/data/npm_cohorte_aco.csv.gz   (versionado: una fila por paquete)
    reconstruction_real/logs/npm_cohorte_aco_log.txt

Uso (desde la raiz del repo):
    python reconstruction_real/code/npm_cohorte_aco.py
"""

import gzip
import hashlib
import json
import logging
import math
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RAW = ROOT / "data" / "raw_npm"
RAW.mkdir(parents=True, exist_ok=True)
OUT = ROOT / "reconstruction_real" / "data" / "npm_cohorte_aco.csv.gz"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "npm_cohorte_aco_log.txt"

SEMILLA = 20261002
N_MUESTRA = 12000
PAGINA = 10000                          # maximo de filas por peticion a _all_docs
NACIDO_DESDE = date(2015, 7, 1)
NACIDO_HASTA = date(2024, 10, 2)
PISO_DESCARGAS = date(2015, 1, 10)     # primer dia con datos del servicio
MIN_DESCARGAS_180D = 1000
MIN_MESES = 24
MIN_LADO = 6                            # meses a cada lado del maximo
MIN_PUNTOS = 6                          # puntos por ajuste
UMBRAL_EXTINCION = 0.01                 # 1% del maximo mensual
RACHA_EXTINCION = 6                     # meses consecutivos
CVSS_ABRUPTO = 7.0
VENTANA_ABRUPTO = (-3, 6)               # meses respecto al maximo

REPLICA = "https://replicate.npmjs.com/_all_docs"
REGISTRY = "https://registry.npmjs.org/"
DESCARGAS = "https://api.npmjs.org/downloads/range/"
OSV = "https://api.osv.dev/v1/query"

FUNDACIONES = {"apache", "eclipse", "openjs-foundation", "cncf", "nodejs",
               "gnome", "mozilla"}
CORPORATIVAS = {"microsoft", "google", "facebook", "aws", "vercel", "shopify",
                "ibm", "oracle", "netflix"}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("NPM")


def abrir(url, datos=None, cabeceras=None, timeout=120):
    """urlopen con hasta 4 reintentos y espera exponencial (2, 4, 8, 16 s)."""
    for intento in range(5):
        try:
            req = urllib.request.Request(url, data=datos,
                                         headers=cabeceras or {})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (404, 400):     # no existe / peticion invalida: no reintentar
                return None
            if intento == 4:
                raise
            time.sleep(2 ** (intento + 1))
        except Exception:
            if intento == 4:
                raise
            time.sleep(2 ** (intento + 1))


# ---------------------------------------------------------------- etapa A
def muestrear_nombres():
    """Muestreo sistematico desde _all_docs: una de cada k filas."""
    destino = RAW / "muestra_nombres.json"
    if destino.exists():
        d = json.loads(destino.read_text(encoding="utf-8"))
        log.info("A. Muestra en cache: %d nombres (total_rows=%d, k=%d)",
                 len(d["nombres"]), d["total_rows"], d["k"])
        return d["nombres"]

    cab = json.loads(abrir(f"{REPLICA}?limit=1"))
    total = cab["total_rows"]
    k = max(1, total // N_MUESTRA)
    offset = SEMILLA % k
    log.info("A. Marco de muestreo: %d paquetes | k=%d | desplazamiento=%d",
             total, k, offset)

    # El servicio limita cada respuesta a un maximo de filas, asi que se pagina
    # con startkey. La primera fila de cada pagina repite la ultima de la
    # anterior y se descarta. La respuesta no trae saltos de linea, asi que los
    # identificadores se extraen con una expresion regular sobre el bloque.
    # Punto de guardado: el recorrido del marco completo son ~445 paginas y un
    # corte a media etapa obligaria a repetirlo entero.
    parcial = RAW / "muestra_parcial.json"
    if parcial.exists():
        est = json.loads(parcial.read_text(encoding="utf-8"))
        nombres, i, startkey = est["nombres"], est["i"], est["startkey"]
        log.info("A. Reanudando desde la fila %d (%d tomadas)", i, len(nombres))
    else:
        nombres, i, startkey = [], 0, None

    patron = re.compile(rb'\{"id":"((?:[^"\\]|\\.)*)","key":')
    pagina = 0
    while True:
        url = f"{REPLICA}?limit={PAGINA}"
        if startkey is not None:
            url += "&startkey=" + urllib.parse.quote(json.dumps(startkey))
        datos = abrir(url, timeout=300)
        if datos is None:
            raise RuntimeError(f"_all_docs fallo en startkey={startkey!r}")
        ids = [json.loads(b'"' + m.group(1) + b'"')
               for m in patron.finditer(datos)]
        if startkey is not None and ids and ids[0] == startkey:
            ids = ids[1:]          # la pagina solapa una fila con la anterior
        if not ids:
            break
        for nombre in ids:
            if (i - offset) % k == 0 and nombre and not nombre.startswith("_"):
                nombres.append(nombre)
            i += 1
        startkey = ids[-1]
        pagina += 1
        if pagina % 20 == 0:
            parcial.write_text(json.dumps(
                {"i": i, "startkey": startkey, "nombres": nombres}),
                encoding="utf-8")
            log.info("   recorridas %d filas, %d tomadas", i, len(nombres))

    destino.write_text(json.dumps(
        {"total_rows": total, "k": k, "offset": offset, "semilla": SEMILLA,
         "nombres": nombres}), encoding="utf-8")
    parcial.unlink(missing_ok=True)
    log.info("A. Muestra: %d nombres de %d filas recorridas", len(nombres), i)
    return nombres


# ---------------------------------------------------------------- etapa B
def _meta_uno(nombre):
    try:
        crudo = abrir(REGISTRY + urllib.parse.quote(nombre, safe="@/"),
                      timeout=90)
        if crudo is None:
            return {"nombre": nombre, "error": "404"}
        d = json.loads(crudo)
    except Exception as e:
        return {"nombre": nombre, "error": f"{type(e).__name__}: {e}"}

    t = d.get("time", {})
    if not isinstance(t, dict) or "created" not in t:
        return {"nombre": nombre, "error": "sin time.created"}
    ultima = (d.get("dist-tags") or {}).get("latest")
    vers = d.get("versions") or {}
    deprecado = bool(vers.get(ultima, {}).get("deprecated")) if ultima else False
    repo = d.get("repository")
    url_repo = repo.get("url", "") if isinstance(repo, dict) else (repo or "")
    return {
        "nombre": nombre,
        "creado": t["created"][:10],
        "modificado": t.get("modified", "")[:10],
        "n_versiones": len(vers),
        "deprecado": deprecado,
        "despublicado": bool(d.get("time", {}).get("unpublished")),
        "repo": url_repo,
    }


def metadatos(nombres):
    destino = RAW / "metadatos.jsonl"
    hechos = {}
    if destino.exists():
        with destino.open(encoding="utf-8") as fh:
            for linea in fh:
                try:
                    r = json.loads(linea)
                    hechos[r["nombre"]] = r
                except json.JSONDecodeError:
                    continue
        log.info("B. Metadatos en cache: %d", len(hechos))

    faltan = [n for n in nombres if n not in hechos]
    if faltan:
        log.info("B. Pidiendo metadatos de %d paquetes", len(faltan))
        with destino.open("a", encoding="utf-8") as fh, \
                ThreadPoolExecutor(max_workers=16) as ex:
            for i, r in enumerate(ex.map(_meta_uno, faltan), 1):
                fh.write(json.dumps(r) + "\n")
                hechos[r["nombre"]] = r
                if i % 1000 == 0:
                    fh.flush()
                    log.info("   %d / %d", i, len(faltan))

    err = sum(1 for r in hechos.values() if "error" in r)
    log.info("B. Metadatos: %d con datos, %d con error", len(hechos) - err, err)
    return hechos


# ---------------------------------------------------------------- etapa C
def filtrar_fechas(metas):
    """Filtros 1-3 del pre-registro, con atricion reportada."""
    paso = {"total": 0, "sin_meta": 0, "fuera_rango": 0, "despublicado": 0,
            "ok": 0}
    out = []
    for r in metas.values():
        paso["total"] += 1
        if "error" in r:
            paso["sin_meta"] += 1
            continue
        try:
            nac = date.fromisoformat(r["creado"])
        except ValueError:
            paso["sin_meta"] += 1
            continue
        if not (NACIDO_DESDE <= nac <= NACIDO_HASTA):
            paso["fuera_rango"] += 1
            continue
        if r["despublicado"]:
            paso["despublicado"] += 1
            continue
        r["nacimiento"] = nac
        out.append(r)
        paso["ok"] += 1
    log.info("C. Atricion: %d muestreados | -%d sin metadatos | -%d fuera del "
             "rango de fechas | -%d despublicados | = %d",
             paso["total"], paso["sin_meta"], paso["fuera_rango"],
             paso["despublicado"], paso["ok"])
    return out, paso


# ---------------------------------------------------------------- etapa D
def ventanas_18m(desde, hasta):
    """Tramos de 18 meses (limite del servicio) entre dos fechas."""
    out, ini = [], desde
    while ini < hasta:
        y, m = ini.year, ini.month + 17
        y, m = y + (m - 1) // 12, (m - 1) % 12 + 1
        fin = min(date(y, m, 28), hasta)
        out.append((ini.isoformat(), fin.isoformat()))
        y, m = fin.year, fin.month + 1
        ini = date(y + (m - 1) // 12, (m - 1) % 12 + 1, 1)
    return out


def descargar_series(nombres, corte):
    """Series diarias por paquete. Bulk de 128; los scoped van de uno en uno."""
    destino = RAW / "descargas.jsonl.gz"
    series = defaultdict(dict)
    if destino.exists():
        with gzip.open(destino, "rt", encoding="utf-8") as fh:
            for linea in fh:
                r = json.loads(linea)
                series[r["nombre"]] = r["dias"]
        log.info("D. Series en cache: %d paquetes", len(series))
        return series

    ventanas = ventanas_18m(PISO_DESCARGAS, corte)
    planos = [n for n in nombres if not n.startswith("@")]
    scoped = [n for n in nombres if n.startswith("@")]
    log.info("D. %d paquetes (%d planos en bulk, %d scoped individuales) x %d "
             "ventanas de 18 meses", len(nombres), len(planos), len(scoped),
             len(ventanas))

    def pedir(args):
        rango, lote = args
        url = DESCARGAS + rango + "/" + ",".join(
            urllib.parse.quote(n, safe="@/") for n in lote)
        try:
            crudo = abrir(url, timeout=180)
            if crudo is None:
                return {}
            d = json.loads(crudo)
        except Exception as e:
            log.warning("   fallo %s (%d paquetes): %s", rango, len(lote), e)
            return {}
        if "downloads" in d and "package" in d:     # respuesta de un solo paquete
            d = {d["package"]: d}
        return d

    tareas = []
    for ini, fin in ventanas:
        rango = f"{ini}:{fin}"
        for i in range(0, len(planos), 128):
            tareas.append((rango, planos[i:i + 128]))
        for n in scoped:
            tareas.append((rango, [n]))

    with ThreadPoolExecutor(max_workers=12) as ex:
        for i, res in enumerate(ex.map(pedir, tareas), 1):
            for nombre, d in (res or {}).items():
                if not d or not d.get("downloads"):
                    continue
                for punto in d["downloads"]:
                    if punto["downloads"]:
                        series[nombre][punto["day"]] = punto["downloads"]
            if i % 200 == 0:
                log.info("   %d / %d peticiones", i, len(tareas))

    with gzip.open(destino, "wt", encoding="utf-8") as fh:
        for nombre, dias in series.items():
            fh.write(json.dumps({"nombre": nombre, "dias": dias}) + "\n")
    log.info("D. Series descargadas: %d paquetes con al menos un dia > 0",
             len(series))
    return series


# ---------------------------------------------------------------- etapa E
def mensual(dias, corte):
    """Totales mensuales. Descarta el mes del corte (incompleto)."""
    mes_corte = corte.strftime("%Y-%m")
    acc = defaultdict(int)
    for dia, n in dias.items():
        m = dia[:7]
        if m != mes_corte:
            acc[m] += n
    return sorted(acc.items())


def ajustar(valores):
    """MCO de log(y) contra log(t), t = 1..n. Mismo metodo que el corpus."""
    pares = [(i + 1, v) for i, v in enumerate(valores) if v > 0]
    if len(pares) < MIN_PUNTOS:
        return None
    xs = [math.log(t) for t, _ in pares]
    ys = [math.log(v) for _, v in pares]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    if sxx == 0:
        return None
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    syy = sum((y - my) ** 2 for y in ys)
    b = sxy / sxx
    r2 = (sxy ** 2) / (sxx * syy) if syy > 0 else 0.0
    return {"b": b, "r2": r2, "n": n}


def extincion(meses):
    """Primer mes de una racha de >= 6 meses bajo el 1% del maximo."""
    if not meses:
        return None
    pico = max(v for _, v in meses)
    if pico <= 0:
        return None
    umbral = pico * UMBRAL_EXTINCION
    racha = 0
    for i, (m, v) in enumerate(meses):
        if v < umbral:
            racha += 1
            if racha >= RACHA_EXTINCION:
                return meses[i - RACHA_EXTINCION + 1][0]
        else:
            racha = 0
    return None


def friccion(url_repo):
    """Codificacion a priori del pre-registro. Solo descriptiva."""
    m = re.search(r"github\.com[/:]([^/]+)/", url_repo or "")
    if not m:
        return 0
    org = m.group(1).lower()
    if org in FUNDACIONES:
        return 3
    if org in CORPORATIVAS:
        return 2
    return 1


def meses_entre(a, b):
    return (int(b[:4]) - int(a[:4])) * 12 + (int(b[5:7]) - int(a[5:7]))


def construir(candidatos, series, corte):
    paso = {"candidatos": len(candidatos), "sin_serie": 0, "sin_actividad": 0,
            "pocos_meses": 0, "pico_al_borde": 0, "ajuste_fallido": 0, "ok": 0}
    filas = []
    for r in candidatos:
        dias = series.get(r["nombre"])
        if not dias:
            paso["sin_serie"] += 1
            continue

        nac = r["nacimiento"]
        tope = nac.toordinal() + 180
        primeros180 = sum(
            n for d, n in dias.items()
            if nac.toordinal() <= date.fromisoformat(d).toordinal() <= tope)
        if primeros180 < MIN_DESCARGAS_180D:
            paso["sin_actividad"] += 1
            continue

        meses = mensual(dias, corte)
        if len(meses) < MIN_MESES:
            paso["pocos_meses"] += 1
            continue

        valores = [v for _, v in meses]
        i_pico = max(range(len(valores)), key=lambda i: valores[i])
        if i_pico < MIN_LADO or (len(valores) - 1 - i_pico) < MIN_LADO:
            paso["pico_al_borde"] += 1
            continue

        subida = ajustar(valores[:i_pico + 1])
        i_min = i_pico + 1 + min(
            range(len(valores) - i_pico - 1),
            key=lambda j: valores[i_pico + 1 + j])
        caida = ajustar(valores[i_pico:i_min + 1])
        if not subida or not caida:
            paso["ajuste_fallido"] += 1
            continue

        fin = extincion(meses)
        filas.append({
            "nombre": r["nombre"],
            "nacimiento": r["creado"],
            "mes_inicio": meses[0][0],
            "n_meses": len(meses),
            "pico_mensual": valores[i_pico],
            "mes_pico": meses[i_pico][0],
            "edad_al_pico_meses": meses_entre(meses[0][0], meses[i_pico][0]),
            "b_subida": round(subida["b"], 6),
            "r2_subida": round(subida["r2"], 6),
            "n_subida": subida["n"],
            "delta_caida": round(caida["b"], 6),
            "r2_caida": round(caida["r2"], 6),
            "n_caida": caida["n"],
            "minimo_posterior": valores[i_min],
            "mes_extincion": fin or "",
            "edad_extincion_meses": (
                meses_entre(meses[0][0], fin) if fin else ""),
            "deprecado": int(r["deprecado"]),
            "friccion_a_priori": friccion(r["repo"]),
            "repo": r["repo"][:200],
        })
        paso["ok"] += 1

    log.info("E. Atricion: %d candidatos | -%d sin serie | -%d sin actividad "
             "(<%d descargas en 180 d) | -%d con <%d meses | -%d con el pico "
             "al borde | -%d con ajuste fallido | = %d en la cohorte",
             paso["candidatos"], paso["sin_serie"], paso["sin_actividad"],
             MIN_DESCARGAS_180D, paso["pocos_meses"], MIN_MESES,
             paso["pico_al_borde"], paso["ajuste_fallido"], paso["ok"])
    return filas, paso


# ---------------------------------------------------------------- etapa F
def _osv_uno(nombre):
    cuerpo = json.dumps({"package": {"name": nombre, "ecosystem": "npm"}})
    try:
        crudo = abrir(OSV, datos=cuerpo.encode(),
                      cabeceras={"Content-Type": "application/json"},
                      timeout=90)
        if crudo is None:
            return nombre, []
        d = json.loads(crudo)
    except Exception:
        return nombre, []
    out = []
    for v in d.get("vulns", []):
        if not v.get("published"):
            continue
        cvss = 0.0
        for s in v.get("severity", []) or []:
            try:
                cvss = max(cvss, _cvss_base(s.get("score", "")))
            except Exception:
                pass
        # La etiqueta de GitHub que replica OSV es la fuente primaria: HIGH y
        # CRITICAL son por definicion CVSS >= 7.0. El vector queda de respaldo.
        etiqueta = ((v.get("database_specific") or {}).get("severity") or "")
        out.append({"publicado": v["published"][:10], "cvss": cvss,
                    "etiqueta": etiqueta.upper()})
    return nombre, out


_PESOS = {"AV": {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2},
          "AC": {"L": 0.77, "H": 0.44},
          "PR": {"N": 0.85, "L": 0.62, "H": 0.27},
          "UI": {"N": 0.85, "R": 0.62},
          "C": {"H": 0.56, "L": 0.22, "N": 0.0},
          "I": {"H": 0.56, "L": 0.22, "N": 0.0},
          "A": {"H": 0.56, "L": 0.22, "N": 0.0}}


def _cvss_base(vector):
    """Puntaje base CVSS v3 desde el vector. Devuelve 0.0 si no se puede."""
    if not vector.startswith("CVSS:3"):
        return 0.0
    p = dict(x.split(":", 1) for x in vector.split("/")[1:] if ":" in x)
    try:
        iss = 1 - (1 - _PESOS["C"][p["C"]]) * (1 - _PESOS["I"][p["I"]]) * \
            (1 - _PESOS["A"][p["A"]])
        alcance = p.get("S", "U") == "C"
        if alcance:
            impacto = 7.52 * (iss - 0.029) - 3.25 * (iss - 0.02) ** 15
            pr = {"N": 0.85, "L": 0.68, "H": 0.50}[p["PR"]]
        else:
            impacto = 6.42 * iss
            pr = _PESOS["PR"][p["PR"]]
        if impacto <= 0:
            return 0.0
        expl = 8.22 * _PESOS["AV"][p["AV"]] * _PESOS["AC"][p["AC"]] * pr * \
            _PESOS["UI"][p["UI"]]
        bruto = min((1.08 if alcance else 1.0) * (impacto + expl), 10.0)
        entero = int(round(bruto * 100000))
        if entero % 10000 == 0:
            return entero / 100000.0
        return (math.floor(entero / 10000) + 1) / 10.0
    except KeyError:
        return 0.0


def clasificar_disparador(filas):
    destino = RAW / "osv.jsonl"
    avisos = {}
    if destino.exists():
        with destino.open(encoding="utf-8") as fh:
            for linea in fh:
                r = json.loads(linea)
                avisos[r["nombre"]] = r["avisos"]
        log.info("F. OSV en cache: %d paquetes", len(avisos))

    faltan = [f["nombre"] for f in filas if f["nombre"] not in avisos]
    if faltan:
        log.info("F. Consultando OSV para %d paquetes", len(faltan))
        with destino.open("a", encoding="utf-8") as fh, \
                ThreadPoolExecutor(max_workers=12) as ex:
            for i, (nombre, av) in enumerate(ex.map(_osv_uno, faltan), 1):
                fh.write(json.dumps({"nombre": nombre, "avisos": av}) + "\n")
                avisos[nombre] = av
                if i % 500 == 0:
                    fh.flush()
                    log.info("   %d / %d", i, len(faltan))

    conteo = defaultdict(int)
    for f in filas:
        pico = f["mes_pico"]
        abrupto = False
        peor = 0.0
        for a in avisos.get(f["nombre"], []):
            d = meses_entre(pico, a["publicado"][:7])
            if VENTANA_ABRUPTO[0] <= d <= VENTANA_ABRUPTO[1]:
                peor = max(peor, a["cvss"])
                if (a.get("etiqueta") in ("HIGH", "CRITICAL")
                        or a["cvss"] >= CVSS_ABRUPTO):
                    abrupto = True
        if abrupto:
            clase = "abrupto"
        elif f["deprecado"]:
            clase = "anunciado"
        else:
            clase = "sin_clasificar"
        f["disparador"] = clase
        f["cvss_ventana"] = round(peor, 1)
        f["n_avisos"] = len(avisos.get(f["nombre"], []))
        conteo[clase] += 1
    log.info("F. Disparador: %d abruptos, %d anunciados, %d sin clasificar",
             conteo["abrupto"], conteo["anunciado"], conteo["sin_clasificar"])
    return filas


# ---------------------------------------------------------------- main
def main():
    corte = datetime.now(timezone.utc).date()
    log.info("=" * 78)
    log.info("COHORTE npm — pre-registro 2026-10-02 (commit 3ff9fca)")
    log.info("Semilla %d | corte %s | piso de descargas %s",
             SEMILLA, corte, PISO_DESCARGAS)
    log.info("=" * 78)

    nombres = muestrear_nombres()
    metas = metadatos(nombres)
    candidatos, _ = filtrar_fechas(metas)
    series = descargar_series([c["nombre"] for c in candidatos], corte)
    filas, _ = construir(candidatos, series, corte)
    if not filas:
        log.error("Cohorte vacia: no se escribe salida.")
        sys.exit(1)
    filas = clasificar_disparador(filas)

    cols = list(filas[0].keys())
    with gzip.open(OUT, "wt", encoding="utf-8", newline="") as fh:
        import csv
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for f in sorted(filas, key=lambda r: r["nombre"]):
            w.writerow(f)
    h = hashlib.sha256(OUT.read_bytes()).hexdigest()
    log.info("Cohorte -> %s | %d paquetes | SHA-256 %s",
             OUT.relative_to(ROOT), len(filas), h)

    extintos = sum(1 for f in filas if f["mes_extincion"])
    log.info("Extinciones funcionales: %d / %d (%.1f%%)",
             extintos, len(filas), 100 * extintos / len(filas))
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
