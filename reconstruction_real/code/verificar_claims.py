#!/usr/bin/env python3
"""
VERIFICADOR DE CLAIMS — README <-> datos versionados
====================================================

Cada cifra que el README presenta como resultado vigente se registra en
`reconstruction_real/claims.yaml` con:

  id         identificador estable.
  readme     fragmento literal que DEBE aparecer en README.md. Si alguien
             cambia la cifra en el README, el verificador falla hasta que
             `claims.yaml` se actualice a propósito (y viceversa).
  archivo    CSV (.csv o .csv.gz) versionado, ruta desde la raíz del repo.
  expr       expresión de pandas/numpy evaluada con `df` (el CSV), `np` y `pd`.
             El archivo `claims.yaml` es código del repositorio: se revisa por
             PR como cualquier script. No se evalúa nada que venga de fuera.
  esperado   número tal como lo escribe el README.
  escala     1 (por defecto) o 100 cuando el README expresa porcentajes.
  decimales  decimales con que el README redondea (0 por defecto).

El valor calculado se multiplica por `escala` y se redondea a `decimales` con
redondeo convencional (mitad hacia arriba) sobre la representación decimal del
valor, para no depender de errores de coma flotante. El claim pasa si coincide
exactamente con `esperado`.

Uso:
    python reconstruction_real/code/verificar_claims.py          # verifica todo
    python reconstruction_real/code/verificar_claims.py --listar # solo lista

Código de salida: 0 si todo pasa; 1 si algún claim falla o su fragmento ya no
está en el README; 2 si el archivo de claims o un CSV no se puede leer.

Salida: logs/verificar_claims_log.txt
"""

import argparse
import logging
import os
import sys
from decimal import ROUND_HALF_UP, Decimal

import numpy as np
import pandas as pd
import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
CLAIMS_DEFECTO = os.path.join(RAIZ, "reconstruction_real", "claims.yaml")
README_DEFECTO = os.path.join(RAIZ, "README.md")
LOG_DIR = os.path.join(SCRIPT_DIR, "..", "logs")

log = logging.getLogger("verificar_claims")


def _configurar_log():
    os.makedirs(LOG_DIR, exist_ok=True)
    if log.handlers:
        return
    log.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
    for h in (logging.StreamHandler(),
              logging.FileHandler(
                  os.path.join(LOG_DIR, "verificar_claims_log.txt"),
                  mode="w")):
        h.setFormatter(fmt)
        log.addHandler(h)


def redondear(valor, decimales):
    """Redondeo convencional (mitad hacia arriba) sobre la forma decimal."""
    d = Decimal(repr(float(valor)))
    paso = Decimal(1).scaleb(-decimales)
    return float(d.quantize(paso, rounding=ROUND_HALF_UP))


def cargar_claims(ruta):
    with open(ruta, encoding="utf-8") as fh:
        datos = yaml.safe_load(fh)
    claims = datos["claims"] if isinstance(datos, dict) else datos
    ids = [c["id"] for c in claims]
    repetidos = {i for i in ids if ids.count(i) > 1}
    if repetidos:
        raise ValueError(f"ids de claims repetidos: {sorted(repetidos)}")
    return claims


def evaluar(claim, raiz, cache):
    """Calcula el valor de un claim. Devuelve el valor ya escalado/redondeado."""
    ruta = os.path.join(raiz, claim["archivo"])
    if ruta not in cache:
        cache[ruta] = pd.read_csv(ruta)
    df = cache[ruta]
    valor = eval(claim["expr"], {"__builtins__": {}},  # noqa: S307
                 {"df": df, "np": np, "pd": pd, "len": len, "abs": abs,
                  "int": int, "float": float, "round": round, "sum": sum})
    valor = float(valor) * float(claim.get("escala", 1))
    return redondear(valor, int(claim.get("decimales", 0)))


def verificar(ruta_claims=CLAIMS_DEFECTO, ruta_readme=README_DEFECTO,
              raiz=RAIZ):
    """Devuelve una lista de dicts {id, estado, calculado, esperado, detalle}.

    Estados: OK, FALLA, README_SIN_FRAGMENTO, ERROR.
    """
    claims = cargar_claims(ruta_claims)
    with open(ruta_readme, encoding="utf-8") as fh:
        readme = fh.read()
    cache, resultados = {}, []
    for c in claims:
        r = {"id": c["id"], "esperado": c["esperado"], "calculado": None,
             "estado": "OK", "detalle": ""}
        if c["readme"] not in readme:
            r["estado"] = "README_SIN_FRAGMENTO"
            r["detalle"] = f"no aparece en el README: {c['readme']!r}"
            resultados.append(r)
            continue
        try:
            r["calculado"] = evaluar(c, raiz, cache)
        except Exception as exc:  # error de archivo o de expresión
            r["estado"] = "ERROR"
            r["detalle"] = f"{type(exc).__name__}: {exc}"
            resultados.append(r)
            continue
        if abs(r["calculado"] - float(c["esperado"])) > 1e-9:
            r["estado"] = "FALLA"
            r["detalle"] = (f"el dato da {r['calculado']} y el README/claims "
                            f"dice {c['esperado']}")
        resultados.append(r)
    return resultados


def main(argv=None):
    ap = argparse.ArgumentParser(description="Verifica cifras del README "
                                 "contra los CSV versionados.")
    ap.add_argument("--claims", default=CLAIMS_DEFECTO)
    ap.add_argument("--readme", default=README_DEFECTO)
    ap.add_argument("--listar", action="store_true",
                    help="solo lista los claims, sin evaluarlos")
    args = ap.parse_args(argv)
    _configurar_log()

    try:
        if args.listar:
            for c in cargar_claims(args.claims):
                log.info("%-34s %s", c["id"], c["readme"])
            return 0
        resultados = verificar(args.claims, args.readme)
    except (OSError, ValueError, KeyError, yaml.YAMLError) as exc:
        log.error("No se pudo leer claims/README: %s", exc)
        return 2

    malos = [r for r in resultados if r["estado"] != "OK"]
    for r in resultados:
        nivel = logging.INFO if r["estado"] == "OK" else logging.ERROR
        log.log(nivel, "%-22s %-34s calculado=%s esperado=%s %s",
                r["estado"], r["id"], r["calculado"], r["esperado"],
                r["detalle"])
    log.info("Claims: %d verificados, %d OK, %d con problemas",
             len(resultados), len(resultados) - len(malos), len(malos))
    if any(r["estado"] == "ERROR" for r in malos):
        return 2
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main())
