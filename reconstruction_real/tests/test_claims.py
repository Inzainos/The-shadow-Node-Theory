#!/usr/bin/env python3
"""Regresión: las cifras del README coinciden con los datos versionados.

`reconstruction_real/claims.yaml` liga cada cifra citada en README.md con el
CSV de donde sale. Estos tests hacen dos cosas distintas:

  1. Verifican que HOY todos los claims del repo pasan (si alguien cambia un
     dato o una cifra del README sin actualizar el otro, este test falla).
  2. Verifican que el propio verificador detecta los tres modos de falla
     (cifra cambiada en el README, dato distinto, CSV ausente). Sin esto, un
     verificador roto pasaría en silencio.

Corre con pytest o directo:
    python reconstruction_real/tests/test_claims.py
"""

import os
import sys
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "reconstruction_real", "code"))

import verificar_claims as vc  # noqa: E402

CAMPOS = {"id", "readme", "archivo", "expr", "esperado"}


def _mini_repo(readme_texto, esperado, con_csv=True):
    """Crea un repo mínimo en un directorio temporal. Devuelve (dir, rutas)."""
    tmp = tempfile.TemporaryDirectory()
    raiz = tmp.name
    if con_csv:
        with open(os.path.join(raiz, "datos.csv"), "w") as fh:
            fh.write("x\n1\n2\n3\n")
    with open(os.path.join(raiz, "README.md"), "w") as fh:
        fh.write(readme_texto)
    with open(os.path.join(raiz, "claims.yaml"), "w") as fh:
        fh.write(
            "claims:\n"
            "  - id: tres_filas\n"
            "    readme: 'hay 3 filas'\n"
            "    archivo: datos.csv\n"
            "    expr: 'len(df)'\n"
            f"    esperado: {esperado}\n")
    return tmp, raiz


def _correr(raiz):
    return vc.verificar(os.path.join(raiz, "claims.yaml"),
                        os.path.join(raiz, "README.md"), raiz)


def test_claims_del_repo_coinciden_con_los_datos():
    resultados = vc.verificar()
    malos = [(r["id"], r["estado"], r["detalle"]) for r in resultados
             if r["estado"] != "OK"]
    assert not malos, f"claims con problemas: {malos}"
    assert len(resultados) >= 20, "el registro de claims se vació"


def test_todos_los_claims_tienen_los_campos_obligatorios():
    for c in vc.cargar_claims(vc.CLAIMS_DEFECTO):
        faltan = CAMPOS - set(c)
        assert not faltan, f"{c.get('id')} sin campos {faltan}"
        assert os.path.exists(os.path.join(vc.RAIZ, c["archivo"])), c["id"]


def test_redondeo_mitad_hacia_arriba_sin_ruido_de_coma_flotante():
    assert vc.redondear(96.75, 1) == 96.8
    assert vc.redondear(7.9622, 3) == 7.962
    assert vc.redondear(0.5, 0) == 1.0
    assert vc.redondear(2.21, 1) == 2.2


def test_verificador_acepta_un_claim_correcto():
    tmp, raiz = _mini_repo("el corpus: hay 3 filas.", esperado=3)
    with tmp:
        assert [r["estado"] for r in _correr(raiz)] == ["OK"]


def test_verificador_detecta_dato_distinto():
    tmp, raiz = _mini_repo("el corpus: hay 3 filas.", esperado=4)
    with tmp:
        r = _correr(raiz)[0]
        assert r["estado"] == "FALLA" and r["calculado"] == 3.0


def test_verificador_detecta_cifra_cambiada_en_el_readme():
    tmp, raiz = _mini_repo("el corpus: hay 5 filas.", esperado=3)
    with tmp:
        assert _correr(raiz)[0]["estado"] == "README_SIN_FRAGMENTO"


def test_verificador_reporta_csv_ausente_como_error():
    tmp, raiz = _mini_repo("el corpus: hay 3 filas.", esperado=3,
                           con_csv=False)
    with tmp:
        assert _correr(raiz)[0]["estado"] == "ERROR"


def test_ids_repetidos_se_rechazan():
    tmp, raiz = _mini_repo("el corpus: hay 3 filas.", esperado=3)
    with tmp:
        ruta = os.path.join(raiz, "claims.yaml")
        with open(ruta) as fh:
            texto = fh.read()
        with open(ruta, "w") as fh:
            fh.write(texto + texto.split("claims:\n")[1])
        try:
            vc.cargar_claims(ruta)
        except ValueError as exc:
            assert "repetidos" in str(exc)
        else:
            raise AssertionError("no se rechazó el id repetido")


if __name__ == "__main__":
    pruebas = [v for k, v in sorted(globals().items())
               if k.startswith("test_") and callable(v)]
    for t in pruebas:
        t()
        print("OK  ", t.__name__)
    print(f"{len(pruebas)} pruebas OK")
