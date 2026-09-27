"""
Descarga las velas diarias (klines 1d) del archivo público de Binance para el
punto 5 del pre-registro 2026-09-27 (cohortes ampliadas de ACO-A).

Fuente: https://data.binance.vision (archivo S3 público; incluye pares ya
retirados). Se listan todos los pares spot contra USDT y se excluyen, con las
reglas del pre-registro:
    * stablecoins y monedas fiat (lista fija abajo, escrita antes de ver precios);
    * tokens apalancados: base = X + {UP, DOWN, BULL, BEAR} donde X es a su vez
      una base con par propio contra USDT (así no se excluye, p. ej., JUP).

Salidas:
    data/raw_binance/klines_1d/<PAR>.csv   (no versionado; ver .gitignore)
    data/binance_cierres_diarios.csv.gz    (versionado: par, fecha, cierre)
    reconstruction_real/logs/descargar_binance_klines_log.txt

Uso (desde la raíz del repo):
    python reconstruction_real/code/descargar_binance_klines.py
"""

import hashlib
import io
import logging
import re
import sys
import time
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
RAW = ROOT / "data" / "raw_binance"
KL = RAW / "klines_1d"
KL.mkdir(parents=True, exist_ok=True)
SUB = ROOT / "data" / "binance_cierres_diarios.csv.gz"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "descargar_binance_klines_log.txt"

S3 = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"
DESCARGA = "https://data.binance.vision/"
ESTABLES_FIAT = {
    "USDC", "BUSD", "TUSD", "USDP", "PAX", "DAI", "FDUSD", "USDS", "USDSB",
    "SUSD", "UST", "USTC", "AEUR", "EURI", "XUSD", "USD1", "BFUSD", "USDE",
    "RLUSD", "PYUSD", "USDD", "VAI", "EUR", "GBP", "AUD", "BRL", "TRY", "RUB",
    "NGN", "UAH", "BIDR", "IDRT", "BVND", "ZAR", "PLN", "RON", "ARS", "JPY",
    "MXN", "COP", "CZK", "BKRW",
}
APALANCADOS = ("UP", "DOWN", "BULL", "BEAR")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("BINANCE")


def abrir(url):
    """urlopen con hasta 4 reintentos y espera exponencial (2, 4, 8, 16 s)."""
    for intento in range(5):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return r.read()
        except Exception:
            if intento == 4:
                raise
            time.sleep(2 ** (intento + 1))


def listar(prefijo, patron):
    """Lista claves o prefijos del bucket (paginado)."""
    out, marker = [], ""
    while True:
        u = f"{S3}?delimiter=/&prefix={prefijo}" + (f"&marker={marker}" if marker
                                                      else "")
        x = abrir(u).decode()
        p = re.findall(patron, x)
        out += p
        if "<IsTruncated>true</IsTruncated>" not in x or not p:
            return out
        marker = p[-1] if patron.startswith("<Key>") else prefijo + p[-1] + "/"


def clasificar(pares):
    bases = {p[:-4] for p in pares}
    incl, excl = [], {}
    for p in pares:
        b = p[:-4]
        if b in ESTABLES_FIAT:
            excl[p] = "estable/fiat"
            continue
        lev = next((s for s in APALANCADOS if b.endswith(s)
                    and b[:-len(s)] in bases), None)
        if lev:
            excl[p] = f"apalancado ({lev})"
            continue
        incl.append(p)
    return incl, excl


def bajar_par(par):
    try:
        return _bajar_par(par)
    except Exception as e:  # se registra y se sigue con los demás pares
        return par, f"error: {type(e).__name__}: {e}"


def _bajar_par(par):
    destino = KL / f"{par}.csv"
    if destino.exists():
        return par, "cache"
    claves = listar(f"data/spot/monthly/klines/{par}/1d/",
                    r"<Key>([^<]+\.zip)</Key>")
    tablas = []
    for k in claves:
        z = zipfile.ZipFile(io.BytesIO(abrir(DESCARGA + k)))
        with z.open(z.namelist()[0]) as fh:
            t = pd.read_csv(fh, header=None, usecols=[0, 4])
        t = t[pd.to_numeric(t[0], errors="coerce").notna()]
        tablas.append(t)
    if not tablas:
        return par, "sin archivos"
    t = pd.concat(tablas)
    t.columns = ["open_time", "close"]
    ot = pd.to_numeric(t.open_time)
    # desde 2025 Binance publica las marcas de tiempo spot en microsegundos
    t["fecha"] = pd.to_datetime([v // 1000 if v > 10 ** 14 else v for v in ot],
                                unit="ms").date
    t[["fecha", "close"]].drop_duplicates("fecha").sort_values("fecha") \
        .to_csv(destino, index=False)
    return par, f"{len(claves)} meses"


def main():
    log.info("=" * 78)
    log.info("DESCARGA BINANCE klines 1d (pre-registro 2026-09-27, punto 5)")
    log.info("=" * 78)
    todos = listar("data/spot/monthly/klines/",
                   r"<Prefix>data/spot/monthly/klines/([^/<]+)/</Prefix>")
    pares = sorted(p for p in todos if p.endswith("USDT") and len(p) > 4)
    incl, excl = clasificar(pares)
    log.info("Pares spot en el archivo: %d | contra USDT: %d | incluidos: %d | "
             "excluidos: %d", len(todos), len(pares), len(incl), len(excl))
    for motivo in sorted(set(excl.values())):
        ps = [p for p, m in excl.items() if m == motivo]
        log.info("  excluidos %-18s %3d: %s", motivo, len(ps), ", ".join(ps))
    with ThreadPoolExecutor(max_workers=24) as ex:
        res = list(ex.map(bajar_par, incl))
    sin = [p for p, e in res if e == "sin archivos"]
    err = [(p, e) for p, e in res if e.startswith("error")]
    log.info("Descargados: %d | sin archivos 1d: %d %s | con error tras "
             "reintentos: %d", len(res) - len(sin) - len(err), len(sin), sin,
             len(err))
    for p, e in err:
        log.warning("  %s -> %s", p, e)
    if err:
        log.error("Hay pares con error: vuelva a correr el script (usa caché) "
                  "antes de analizar.")
        sys.exit(1)
    partes = []
    for p in incl:
        f = KL / f"{p}.csv"
        if f.exists():
            t = pd.read_csv(f)
            t.insert(0, "par", p)
            partes.append(t)
    T = pd.concat(partes)
    T.to_csv(SUB, index=False, compression={"method": "gzip", "mtime": 0})
    h = hashlib.sha256(SUB.read_bytes()).hexdigest()
    log.info("Subconjunto -> %s | %d filas, %d pares | SHA-256 %s",
             SUB.relative_to(ROOT), len(T), T.par.nunique(), h)
    log.info("Última fecha en el archivo: %s", T.fecha.max())
    log.info("LOG -> %s", LOG_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
