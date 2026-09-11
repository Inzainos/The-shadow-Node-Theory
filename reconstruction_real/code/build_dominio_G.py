"""
Shadow Node Theory v2.5.1 — Dominio G: Paquetes Cósmicos / Desempaquetado de Vida
Esqueleto de corpus (estructura + provenance), sin series temporales fabricadas

Origen:
    Integración del marco teórico v33 (`papers/marco_teorico_v33.md`;
    marco conceptual: paquetes cósmicos, resonancia,
    filtros geofísicos, fricción, banda de realidad soportable, nichos) al
    aparato empírico ACO-A (`A(τ) = c·τ^Δ`, hub / absorbente, extinción
    funcional). Axiomas que este dominio pretende anclar: 1 (el universo
    envía paquetes) y 8 (la historia de exposición importa). Versión SNT
    que lo introduce: 2.5.1.

Criterio Dominio G (definitorio, paralelo al criterio ACO):
    1. Un paquete extraterrestre con inventario orgánico documentado en el
       momento de entrega o de hallazgo (hub = señal prístina: aminoácidos,
       nucleobases, aminas, sales).
    2. Un proceso de absorción/alteración identificable que compite con esa
       señal a lo largo del tiempo de exposición o residencia (absorbente =
       radiólisis/UV/rayos cósmicos en el espacio, alteración acuosa o térmica
       en el cuerpo padre, contaminación e hidrólisis terrestres tras la
       caída).
    Sin ambos elementos el caso NO califica como Dominio G.

Regla del repo (AGENTS.md §2): "Real data first. No fabricated values in the
active corpus; derived data cite a primary source. Missing values stay
missing, not zero." Por eso:
    - `t` y `R` se dejan VACÍOS salvo donde exista serie publicada ≥3 puntos
      del mismo cuerpo y mismo protocolo (hoy: solo G03). En los demás,
      `fit_power_law` devuelve "PENDIENTE" y el CSV conserva NaN, no cero.
    - `valores_reportados` contiene únicamente cifras publicadas con cita
      primaria (verificadas en sesión salvo donde se marca lo contrario).
    - `campo_candidato` describe qué medición exacta habría que extraer de
      la literatura para poblar `t`/`R` sin inventar.

Casos (n=5):
    G01 Murchison 1969 (caída, CM2)            — cita verificada, t/R pendiente
    G02 Ryugu / Hayabusa2 2020 (retorno)       — cita verificada, t/R pendiente
    G03 Bennu / OSIRIS-REx 2023 (retorno)      — cita verificada, SERIE REAL n=3
    G04 Orgueil 1864 (caída, CI1)              — cita verificada (parcial)
    G05 Tagish Lake 2000 (caída, C2 ungr.)     — cita NO verificada en sesión

Primera serie poblada (2026-09-10): G03. Fuente: Mojarro A. et al. (2025),
PNAS 122(49) e2512461122, Table 2. Tres piedras de Bennu, mismo protocolo
(one-pot MTBSTFA:DMF + GC-QqQ-MS), medición única por piedra:
    angular  OREX-800055-113  ΣC1-Np/Ph = 8.6   11/20 α-aminoácidos proteicos
    hummocky OREX-800088-108  ΣC1-Np/Ph = 9.4    8/20
    mottled  OREX-800023-103  ΣC1-Np/Ph = 17     4/20
    (agregado OREX-800107-0  ΣC1-Np/Ph = 6.6–9.6  15/20 — EXCLUIDO del ajuste
     principal por los propios autores: sesgo de detección por masa, 5 mg vs
     <1 mg. Se corre solo como sensibilidad, punto medio 8.1.)
    t = ΣC1-alquilnaftalenos/fenantreno (proxy adimensional de alteración
        acuosa en el cuerpo padre; sube con la alteración).
    R = fracción de los 20 α-aminoácidos proteicos detectados (diversidad).
    Lectura de los autores: "α-amino acid diversity decreased with increasing
    ΣC1-Np/Ph values". n=3 es el mínimo ajustable; p con 1 grado de libertad.

Salida:
    reconstruction_real/data/snt_corpus_dominio_G.csv
    reconstruction_real/data/snt_corpus_dominio_G_timeseries.csv (cabecera)
    reconstruction_real/data/snt_corpus_dominio_G_fuentes.md
    reconstruction_real/data/snt_corpus_dominio_G_changelog_entry.md
    reconstruction_real/logs/build_dominio_G_log.txt

Fractal Core Research | Tlaxcala, Mexico | 2026
"""

import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from scipy.stats import pearsonr

warnings.filterwarnings("ignore")

# =============================================================================
# RUTAS
# =============================================================================

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT / "reconstruction_real" / "data"
LOG_DIR = ROOT / "reconstruction_real" / "logs"
DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

OUT_CSV = DATA_DIR / "snt_corpus_dominio_G.csv"
OUT_TS_CSV = DATA_DIR / "snt_corpus_dominio_G_timeseries.csv"
OUT_FUENTES = DATA_DIR / "snt_corpus_dominio_G_fuentes.md"
OUT_CHANGELOG = DATA_DIR / "snt_corpus_dominio_G_changelog_entry.md"
OUT_COMPL = DATA_DIR / "snt_corpus_dominio_G_ajustes_complementarios.csv"
LOG_FILE = LOG_DIR / "build_dominio_G_log.txt"

# =============================================================================
# LOGGING (misma convención que prueba_discriminante_dominio_B.py)
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("DOMINIO-G")

DOMINIO = "G"
DOMINIO_NOMBRE = "Paquetes cósmicos / desempaquetado de vida"
FECHA_BUILD = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# =============================================================================
# CORPUS G — 5 CASOS (metadatos reales, series temporales PENDIENTES)
# R(t) = señal_orgánica_alterada_o_absorbida(t) / señal_prístina_pico
# =============================================================================

CORPUS_G = {

    "G01_Murchison_1969": {
        "descripcion": "Meteorito Murchison (CM2) → biosfera/atmósfera "
                       "terrestre tras la caída",
        "dominio": DOMINIO,
        "trigger_año": 1969,
        "trigger_fecha": "1969-09-28",
        "tipo_trigger": "abrupto",
        "tipo_muestra": "caida",
        "t_unidad": "años",
        "hub": "Inventario orgánico prístino del paquete CM2 (aminoácidos "
               "racémicos, nucleobases purínicas, hidrocarburos)",
        "absorbente": "Contaminación e hidrólisis terrestres + alteración "
                      "durante curación (décadas de residencia en Tierra)",
        "contaminacion_terrestre": "Mínima en 1970 (aminoácidos quirales "
                                   "racémicos D≈L); acumulable con la "
                                   "residencia terrestre",
        "t": [],
        "R": [],
        "valores_reportados": {
            "glicina_extracto_hidrolizado_1970_ug_g": 6,
            "masa_muestra_extracto_1970_g": 10,
            "enantiomeros_1970": "racémicos (D≈L) — indica contaminación "
                                 "terrestre mínima al momento del análisis",
            "aminoacidos_no_proteinogenicos_1971": 12,
            "marcadores_extraterrestres_1971": "AIB (ácido "
                                               "alfa-aminoisobutírico), "
                                               "isovalina — raros o ausentes "
                                               "en la biosfera terrestre",
            "aminoacidos_nombrados_2018": 96,
            "exceso_L_isotopico_1997": "enriquecimiento en 15N respecto a "
                                       "contrapartes terrestres — exceso L "
                                       "de origen extraterrestre",
            "nucleobases_2024": "purinas extraterrestres abundantes; "
                                "Murchison enriquecido en purinas frente a "
                                "Ryugu (comparación 2026)",
            "aminoacidos_total_C2_C6_nmol_g_2025": 250,
            "purina_sobre_pirimidina_2025": "~2.8",
            "amoniaco_relativo_2025": "1/12 de Bennu (mismo protocolo, "
                                      "Glavin 2025)",
        },
        "campo_candidato": "Fracción de aminoácidos no proteinogénicos "
                           "(AIB, isovalina) sobre el inventario total, o "
                           "grado de racemización de aminoácidos quirales, "
                           "medida en alícuotas curadas con historial "
                           "documentado, en función del tiempo de "
                           "residencia terrestre desde 1969. Requiere "
                           "revisión de literatura de re-análisis "
                           "1970→2024 con condiciones de almacenamiento "
                           "registradas.",
        "eje_axioma": [1, 8],
        "fuente": "Kvenvolden K. et al. (1970). Evidence for extraterrestrial "
                  "amino-acids and hydrocarbons in the Murchison meteorite. "
                  "Nature 228, 923-926. DOI 10.1038/228923a0; "
                  "Kvenvolden K., Lawless J., Ponnamperuma C. (1971). "
                  "Nonprotein amino acids in the Murchison meteorite. PNAS "
                  "68(2), 486-490; "
                  "Cronin J.R. & Moore C.B. (1971). Science 172, 1327; "
                  "Engel M.H. & Macko S.A. (1997). Isotopic evidence for "
                  "extraterrestrial non-racemic amino acids in the Murchison "
                  "meteorite. Nature 389, 265; "
                  "Koga T. et al. (2024). Abundant extraterrestrial purine "
                  "nucleobases in the Murchison meteorite. Geochim. "
                  "Cosmochim. Acta 365, 253-265; "
                  "Glavin D.P. et al. (2018). In: Primitive Meteorites and "
                  "Asteroids (Abreu N., ed.), Elsevier, 205-271",
        "cita_verificada_en_sesion": True,
        "estimado": False,
        "datos_pendientes": True,
    },

    "G02_Ryugu_Hayabusa2_2020": {
        "descripcion": "Asteroide (162173) Ryugu, muestras Hayabusa2 → "
                       "alteración por partículas energéticas (UV, rayos "
                       "cósmicos) en superficie vs subsuperficie",
        "dominio": DOMINIO,
        "trigger_año": 2020,
        "trigger_fecha": "2020-12-06",
        "tipo_trigger": "abrupto",
        "tipo_muestra": "retorno_de_muestra",
        "t_unidad": "años (exposición espacial estimada)",
        "hub": "Inventario orgánico prístino (uracilo, ácido nicotínico, "
               "aminoácidos racémicos, 5 nucleobases canónicas)",
        "absorbente": "Radiólisis y fotólisis por UV y rayos cósmicos en "
                      "la superficie del asteroide",
        "contaminacion_terrestre": "Nula por diseño (cápsula sellada; "
                                   "contaminación descartada por el equipo "
                                   "de análisis)",
        "t": [],
        "R": [],
        "valores_reportados": {
            "masa_retornada_g": 5.4,
            "uracilo_ppb_rango": "6-32",
            "acido_nicotinico_B3_ppb_rango": "49-99",
            "muestras_comparadas": "A0106 (touchdown 1, superficie) vs "
                                   "C0107 (touchdown 2, cerca del cráter "
                                   "artificial, material subsuperficial)",
            "diferencia_uracilo_A0106_vs_C0107": "atribuida tentativamente "
                                                 "por Oba et al. (2023) a "
                                                 "distinto grado de "
                                                 "alteración por partículas "
                                                 "energéticas (UV, rayos "
                                                 "cósmicos) — señal directa "
                                                 "de historia de exposición "
                                                 "(Axioma 8)",
            "nucleobases_canonicas_2026": "las 5 (adenina, guanina, "
                                          "citosina, timina, uracilo); "
                                          "purinas ≈ pirimidinas",
            "aminoacidos": "racémicos (Naraoka 2023; Parker 2023)",
            "afinidad_meteoritica": "similar a condritas CI tipo Ivuna "
                                    "(Yokoyama 2023)",
            "aminoacidos_total_C2_C6_nmol_g_2025": 15,
            "beta_alanina_sobre_glicina": ">2.7 (alteración hidrotermal "
                                          "extensa; Glavin 2025)",
            "amoniaco_relativo_2025": "1/75 de Bennu",
        },
        "campo_candidato": "Concentración de uracilo (y B3) por muestra en "
                           "función de la dosis de exposición espacial "
                           "estimada (superficie vs subsuperficie). Hoy solo "
                           "existen 2 puntos (A0106, C0107): n=2 < 3, no "
                           "ajustable. Se necesitan alícuotas adicionales o "
                           "un proxy de dosis por grano.",
        "eje_axioma": [1, 8],
        "fuente": "Oba Y. et al. (2023). Uracil in the carbonaceous asteroid "
                  "(162173) Ryugu. Nat. Commun. 14, 1292. DOI "
                  "10.1038/s41467-023-36904-3; "
                  "Naraoka H. et al. (2023). Soluble organic molecules in "
                  "samples of the carbonaceous asteroid (162173) Ryugu. "
                  "Science 379, abn9033; "
                  "Parker E. et al. (2023). Extraterrestrial amino acids and "
                  "amines identified in asteroid Ryugu samples returned by "
                  "the Hayabusa2 mission. Geochim. Cosmochim. Acta 347, "
                  "42-57; "
                  "Yada T. et al. (2022). Preliminary analysis of the "
                  "Hayabusa2 samples returned from C-type asteroid Ryugu. "
                  "Nat. Astron. 6, 214-220; "
                  "Yokoyama T. et al. (2023). Science 379, eabn7850; "
                  "Oba Y. et al. (2026). A complete set of canonical "
                  "nucleobases in the carbonaceous asteroid (162173) Ryugu. "
                  "Nat. Astron. DOI 10.1038/s41550-026-02791-z",
        "cita_verificada_en_sesion": True,
        "estimado": False,
        "datos_pendientes": True,
    },

    "G03_Bennu_OSIRISREx_2023": {
        "descripcion": "Asteroide (101955) Bennu, muestras OSIRIS-REx → "
                       "alteración acuosa heterogénea en el cuerpo padre",
        "dominio": DOMINIO,
        "trigger_año": 2023,
        "trigger_fecha": "2023-09-24",
        "tipo_trigger": "abrupto",
        "tipo_muestra": "retorno_de_muestra",
        "t_unidad": "ΣC1-alquilnaftalenos/fenantreno (adimensional; proxy "
                    "de alteración acuosa por pirólisis a ~610 °C)",
        "hub": "Diversidad de α-aminoácidos proteicos (de 20) en el "
               "inventario orgánico prístino del cuerpo padre",
        "absorbente": "Alteración acuosa heterogénea entre litologías del "
                      "mismo cuerpo padre (angular → hummocky → mottled; "
                      "número y cronología de eventos de fluido)",
        "contaminacion_terrestre": "Nula por diseño (control de "
                                   "contaminación y curación en NASA JSC)",
        "t": [8.6, 9.4, 17.0],
        "R": [11 / 20, 8 / 20, 4 / 20],
        "puntos": ["OREX-800055-113 (angular)",
                   "OREX-800088-108 (hummocky)",
                   "OREX-800023-103 (mottled)"],
        "R_definicion": "α-aminoácidos proteicos detectados / 20 "
                        "(Mojarro 2025, Table 2; medición única por piedra)",
        "ajustes_complementarios": [
            {
                "nombre": "sensibilidad_con_agregado_n4",
                "nota": "Incluye OREX-800107-0 (agregado, cuadruplicado) "
                        "con ΣC1-Np/Ph = punto medio 8.1 del rango 6.6-9.6 y "
                        "15/20. Los autores lo EXCLUYEN por sesgo de masa; se "
                        "reporta solo como sensibilidad.",
                "t": [8.1, 8.6, 9.4, 17.0],
                "R": [15 / 20, 11 / 20, 8 / 20, 4 / 20],
            },
            {
                "nombre": "absorcion_ACO_A_n3",
                "nota": "Forma ACO-A A(τ) = c·τ^Δ: fracción absorbida "
                        "relativa al máximo observado en el mismo cuerpo "
                        "(15/20 en el agregado): A = 1 - div/15.",
                "t": [8.6, 9.4, 17.0],
                "R": [1 - 11 / 15, 1 - 8 / 15, 1 - 4 / 15],
            },
        ],
        "valores_reportados": {
            "serie_t_R": "Table 2, Mojarro 2025: (8.6, 11/20), (9.4, 8/20), "
                         "(17, 4/20); agregado 6.6-9.6 → 15/20",
            "masa_analizada_mg": "agregado 2.6-3.2 por split; angular 1.0; "
                                 "hummocky 0.7; mottled 0.8 (one-pot)",
            "lectura_autores": "α-amino acid diversity decreased with "
                               "increasing ΣC1-Np/Ph; angular = un evento "
                               "acuoso mayor, hummocky y mottled = más de "
                               "uno; mottled comparable a Tagish Lake 5b",
            "aminoacidos_total_C2_C6_nmol_g": "~70 (hot-water, OREX-803001-0; "
                                              "Glavin 2025); 3.6x menor que "
                                              "Murchison, 4.7x mayor que Ryugu",
            "glicina_nmol_g": 44,
            "beta_alanina_sobre_glicina": 0.08,
            "amoniaco_umol_g": 13.6,
            "amoniaco_relativo": "12x Murchison, 75x Ryugu A0106",
            "metilamina_nmol_g": 914,
            "acido_formico_nmol_g": 4106,
            "acido_acetico_nmol_g": 1436,
            "N_heterociclos_nmol_g": "~5 (5-10x Ryugu y Orgueil)",
            "purina_sobre_pirimidina": 0.55,
            "C_wt_pct": "4.5-4.7",
            "N_wt_pct": "0.23-0.25",
            "d15N_extracto_permil": "+180 ± 47",
            "masa_retornada_g": 121.6,
            "aminoacidos_total": 33,
            "aminoacidos_proteicos_de_20": 14,
            "aminoacidos_no_proteicos": 19,
            "nucleobases_canonicas": "las 5 (adenina, guanina, citosina, "
                                     "timina, uracilo)",
            "amoniaco": "excepcionalmente abundante; con formaldehído "
                        "presente",
            "minerales_salinos_evaporiticos": 11,
            "heterogeneidad": "distribución de orgánicos solubles e "
                              "insolubles difiere entre piedras distintas "
                              "(PNAS 2025); triptófano tentativo, primera "
                              "detección en material extraterrestre",
            "nucleobases_2026": "enriquecido en pirimidinas frente a "
                                "Ryugu; ratio purina/pirimidina correlaciona "
                                "negativamente con amoníaco entre "
                                "Ryugu-Bennu-Orgueil",
        },
        "campo_candidato": "POBLADO (n=3, diversidad). Siguiente paso: "
                           "abundancias absolutas (nmol/g) por piedra con el "
                           "mismo proxy, o más piedras por litología, para "
                           "subir n y pasar de conteo a concentración.",
        "eje_axioma": [1, 2, 8],
        "fuente": "Mojarro A., Aponte J.C., Dworkin J.P., Elsila J.E., "
                  "Glavin D.P., Connolly H.C., Lauretta D.S. (2025). "
                  "Prebiotic organic compounds in samples of asteroid Bennu "
                  "indicate heterogeneous aqueous alteration. PNAS 122(49), "
                  "e2512461122. DOI 10.1073/pnas.2512461122 (Table 2; datos "
                  "en Astromat DOI 10.60707/1k00-p463, 10.60707/sxy1-sq73, "
                  "10.60707/kacg-nb16); "
                  "Glavin D.P., Dworkin J.P. et al. (2025). Abundant ammonia "
                  "and nitrogen-rich soluble organic matter in samples from "
                  "asteroid (101955) Bennu. Nat. Astron. DOI "
                  "10.1038/s41550-024-02472-9; "
                  "McCoy T.J. et al. (2025). An evaporite sequence from "
                  "ancient brine recorded in Bennu samples. Nature 637, "
                  "1072-1077; "
                  "Lauretta D.S. et al. (2024). Asteroid (101955) Bennu in "
                  "the laboratory. Meteorit. Planet. Sci. 59, 2453-2486; "
                  "PNAS (2025). Prebiotic organic compounds in samples of "
                  "asteroid Bennu indicate heterogeneous aqueous alteration. "
                  "DOI 10.1073/pnas.2512461122",
        "cita_verificada_en_sesion": True,
        "estimado": False,
        "datos_pendientes": False,
    },

    "G04_Orgueil_1864": {
        "descripcion": "Meteorito Orgueil (CI1) → 160 años de residencia "
                       "terrestre y curación en colecciones",
        "dominio": DOMINIO,
        "trigger_año": 1864,
        "trigger_fecha": "1864-05-14",
        "tipo_trigger": "abrupto",
        "tipo_muestra": "caida",
        "t_unidad": "años",
        "hub": "Inventario orgánico prístino CI1 (nucleobases, "
               "aminoácidos)",
        "absorbente": "Contaminación e hidrólisis terrestres acumuladas "
                      "durante >160 años de residencia y manipulación",
        "contaminacion_terrestre": "Documentada como problema histórico; "
                                   "usado como referencia meteorítica "
                                   "frente a Ryugu (retorno prístino)",
        "t": [],
        "R": [],
        "valores_reportados": {
            "clase": "CI1 (referencia terrestre de la afinidad CI/Ivuna de "
                     "Ryugu)",
            "comparacion_2023": "compuestos orgánico-solubles analizados "
                                "en paralelo con Ryugu A0106/C0107 "
                                "(Aponte 2023)",
            "nucleobases_2026": "enriquecido en pirimidinas; participa en "
                                "la correlación negativa purina/pirimidina "
                                "vs amoníaco (Ryugu-Bennu-Orgueil)",
            "purina_sobre_pirimidina_2025": "~1.1 (Glavin 2025)",
            "amoniaco_2025": "dos extractos publicados discrepan "
                             "fuertemente (heterogeneidad o método); "
                             "valor no fijable en sesión",
        },
        "campo_candidato": "Mismo índice que G01 (fracción no "
                           "proteinogénica o racemización) en alícuotas de "
                           "distintas colecciones con historial de curación "
                           "conocido, contra tiempo de residencia. Caso de "
                           "mayor t disponible (>160 años) pero con "
                           "provenance de alícuota más incierta.",
        "eje_axioma": [1, 8],
        "fuente": "Aponte J. et al. (2023). Organic-soluble compounds in "
                  "asteroid Ryugu samples A0106 and C0107 and the Orgueil "
                  "(CI1) meteorite. Earth Planets Space 75, 28; "
                  "Oba Y. et al. (2026). Nat. Astron. DOI "
                  "10.1038/s41550-026-02791-z; "
                  "Burton A.S. et al. (2014). The effects of parent-body "
                  "hydrothermal heating on amino acid abundances in CI-like "
                  "chondrites. Polar Sci. 8, 255-263; "
                  "Stoks P.G. & Schwartz A.W. (1979). Uracil in carbonaceous "
                  "meteorites. Nature 282, 709-710",
        "cita_verificada_en_sesion": True,
        "estimado": False,
        "datos_pendientes": True,
    },

    "G05_TagishLake_2000": {
        "descripcion": "Meteorito Tagish Lake (C2 ungrouped) → caída con "
                       "recuperación en frío casi prístina",
        "dominio": DOMINIO,
        "trigger_año": 2000,
        "trigger_fecha": "2000-01-18",
        "tipo_trigger": "abrupto",
        "tipo_muestra": "caida",
        "t_unidad": "años",
        "hub": "Inventario orgánico prístino C2",
        "absorbente": "Contaminación terrestre (mínima por recuperación "
                      "rápida sobre hielo, sin contacto manual directo)",
        "contaminacion_terrestre": "Mínima — caso de control entre 'caída' "
                                   "y 'retorno de muestra'",
        "t": [],
        "R": [],
        "valores_reportados": {
            "nota": "Sin cifras registradas: la cita primaria no fue "
                    "verificada en sesión. No se incluyen valores hasta "
                    "verificar.",
        },
        "campo_candidato": "Mismo índice que G01/G04. Su valor es de "
                           "control: caída natural con contaminación "
                           "cercana a la de un retorno de muestra.",
        "eje_axioma": [1, 8],
        "fuente": "Brown P.G. et al. (2000). The fall, recovery, orbit, and "
                  "composition of the Tagish Lake meteorite: a new type of "
                  "carbonaceous chondrite. Science 290, 320-325 "
                  "[POR VERIFICAR — cita de memoria, no confirmada en "
                  "sesión]",
        "cita_verificada_en_sesion": False,
        "estimado": False,
        "datos_pendientes": True,
    },
}

# =============================================================================
# RELACIÓN TRANSVERSAL CANDIDATA (no temporal) — registrada, no ajustada
# =============================================================================

RELACION_TRANSVERSAL = {
    "id": "GX01_purina_pirimidina_vs_amoniaco",
    "descripcion": "Ratio purina/pirimidina correlaciona negativamente con "
                   "amoníaco entre Ryugu, Bennu y Orgueil (mineralogía y "
                   "composición elemental similares). Murchison enriquecido "
                   "en purinas, Ryugu ≈ equilibrado, Bennu y Orgueil "
                   "enriquecidos en pirimidinas.",
    "eje": "química del entorno receptor (amoníaco) — no tiempo",
    "cuerpos": ["Ryugu", "Bennu", "Orgueil", "Murchison (cualitativo)"],
    "valores_numericos": {
        "purina_sobre_pirimidina": {"Bennu": 0.55, "Orgueil": 1.1,
                                    "Murchison": 2.8, "Ryugu": None},
        "amoniaco_nmol_g": {"Bennu": 13600, "Murchison": "≈1130 (1/12)",
                            "Ryugu": "≈181 (1/75)", "Orgueil": None},
        "fuente_cifras": "Glavin 2025, Nat. Astron. (texto principal y "
                         "Extended Data Table 6)",
    },
    "nota": "Puntos limpios con ambas variables: Bennu y Murchison (n=2). "
            "Orgueil tiene ratio pero amoníaco discrepante entre extractos; "
            "Ryugu tiene amoníaco pero ratio solo cualitativo (≈1, Oba "
            "2026). n limpio = 2 < 3: sigue sin ajustar. Eje 'resonancia "
            "del receptor' (Axioma 2), no el eje temporal de ACO-A.",
    "eje_axioma": [2, 3],
    "fuente": "Oba Y. et al. (2026). A complete set of canonical nucleobases "
              "in the carbonaceous asteroid (162173) Ryugu. Nat. Astron. "
              "DOI 10.1038/s41550-026-02791-z",
    "cita_verificada_en_sesion": True,
}


# =============================================================================
# AJUSTE (idéntico a build_aco_v29.fit_power_law para compatibilidad)
# =============================================================================

def fit_power_law(t_vals, R_vals):
    """
    Ajusta R(t) = a * t^b por OLS log-log. Devuelve dict con a, b, r2,
    p_value, n. Si n < 3 devuelve None en los parámetros (nunca cero).
    """
    datos = [(t, r) for t, r in zip(t_vals, R_vals) if t > 0 and r > 0]
    if len(datos) < 3:
        return {"a": None, "b": None, "r2": None, "p_value": None,
                "n": len(datos)}

    t_arr = np.array([d[0] for d in datos], dtype=float)
    r_arr = np.array([d[1] for d in datos], dtype=float)

    coef = np.polyfit(np.log(t_arr), np.log(r_arr), 1)
    b, a = coef[0], np.exp(coef[1])

    r_pred = a * t_arr ** b
    ss_res = np.sum((r_arr - r_pred) ** 2)
    ss_tot = np.sum((r_arr - r_arr.mean()) ** 2)
    r2 = max(0.0, 1 - ss_res / ss_tot) if ss_tot > 0 else 0.0

    _, pv = pearsonr(np.log(t_arr), np.log(r_arr))

    return {
        "a": round(a, 4), "b": round(b, 4),
        "r2": round(r2, 4), "p_value": round(pv, 6),
        "n": len(t_arr),
    }


def estado_caso(caso, fit):
    """Clasifica el estado del caso sin inventar valores."""
    if caso.get("datos_pendientes", False) or fit["n"] == 0:
        return "PENDIENTE — sin serie temporal real"
    if fit["n"] < 3:
        return f"INSUFICIENTE — n={fit['n']} < 3"
    return "AJUSTADO"


def significancia(pv):
    if pv is None:
        return ""
    if pv < 0.001:
        return "***"
    if pv < 0.01:
        return "**"
    if pv < 0.05:
        return "*"
    return "n.s."


# =============================================================================
# PROVENANCE Y CHANGELOG (se emiten como archivos, no se tocan los del repo)
# =============================================================================

def escribir_fuentes(df):
    lineas = [
        "# Provenance — Dominio G (paquetes cósmicos / desempaquetado)",
        "",
        f"Generado por `reconstruction_real/code/build_dominio_G.py` el "
        f"{FECHA_BUILD}. Bloque para pegar en `data/FUENTES.md`.",
        "",
        "> Regla del repo (AGENTS.md): **real data first**. Este dominio se "
        "entrega con metadatos y citas primarias; las series temporales "
        "`t`/`R` están vacías porque ningún caso publicado ofrece hoy ≥3 "
        "puntos de señal orgánica vs tiempo de exposición para un mismo "
        "cuerpo. NaN, no cero.",
        "",
        "## Casos",
        "",
        "| id | tipo_muestra | trigger | cita verificada en sesión | "
        "estado |",
        "|---|---|---|---|---|",
    ]
    for _, r in df.iterrows():
        lineas.append(
            f"| `{r['id']}` | {r['tipo_muestra']} | {r['trigger_fecha']} | "
            f"{'sí' if r['cita_verificada_en_sesion'] else 'NO'} | "
            f"{r['estado']} |"
        )
    lineas += ["", "## Fuentes primarias por caso", ""]
    for cid, caso in CORPUS_G.items():
        lineas.append(f"### `{cid}`")
        lineas.append("")
        lineas.append(caso["fuente"])
        lineas.append("")
        lineas.append(f"**Campo candidato para `t`/`R`:** "
                      f"{caso['campo_candidato']}")
        lineas.append("")
    lineas += [
        "## Relación transversal registrada (no temporal)",
        "",
        f"`{RELACION_TRANSVERSAL['id']}` — "
        f"{RELACION_TRANSVERSAL['descripcion']}",
        "",
        f"Eje: {RELACION_TRANSVERSAL['eje']}. "
        f"Valores numéricos: {RELACION_TRANSVERSAL['valores_numericos']}. "
        f"{RELACION_TRANSVERSAL['nota']}",
        "",
        f"Fuente: {RELACION_TRANSVERSAL['fuente']}",
        "",
    ]
    OUT_FUENTES.write_text("\n".join(lineas), encoding="utf-8")


def escribir_changelog_entry(df):
    n_total = len(df)
    n_pend = int((df["estado"].str.startswith("PENDIENTE")).sum())
    n_verif = int(df["cita_verificada_en_sesion"].sum())
    aj = df[df["n"] >= 3]
    linea_aj = ""
    for _, r in aj.iterrows():
        linea_aj += (f"  Primer ajuste real: `{r['id']}` b = {r['b']:+.3f}, "
                     f"R² = {r['r2']:.3f}, p = {r['p']:.3f}, n = {r['n']} "
                     f"(Mojarro 2025, Table 2; diversidad de α-aminoácidos "
                     f"vs ΣC1-Np/Ph, 3 piedras de Bennu).\n")
    texto = f"""## [2.5.2] — {FECHA_BUILD}

### Añadido
- **Dominio G — primera serie real poblada (G03 Bennu, n=3)**
{linea_aj}
### Contexto (2.5.1)
- **Dominio G — Paquetes cósmicos / desempaquetado de vida (esqueleto)**
  (`reconstruction_real/code/build_dominio_G.py`,
  `data/snt_corpus_dominio_G.csv`, `data/snt_corpus_dominio_G_fuentes.md`).
  Primer puente entre el marco teórico v33 (Axiomas 1 y 8) y el aparato
  ACO-A. {n_total} casos con metadatos y citas primarias ({n_verif}
  verificadas en sesión); {n_pend} casos con serie temporal `t`/`R`
  **pendiente** (vacía, NaN — regla "missing stays missing"). Registra una
  relación transversal candidata (ratio purina/pirimidina vs amoníaco entre
  Ryugu, Bennu y Orgueil) sobre el eje del receptor (Axioma 2), no ajustada.
  No altera el corpus de 721 casos ni los 18 casos ACO. Ningún resultado
  estadístico nuevo: `b`, `Δ`, `R²` y `p` no existen todavía para este
  dominio.
"""
    OUT_CHANGELOG.write_text(texto, encoding="utf-8")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    log.info("=" * 70)
    log.info("SNT v2.5.1 — DOMINIO G: %s", DOMINIO_NOMBRE.upper())
    log.info("Esqueleto de corpus | marco teórico v33 → ACO-A | "
             "Axiomas 1 y 8")
    log.info("Fractal Core Research | Tlaxcala, Mexico | %s", FECHA_BUILD)
    log.info("=" * 70)
    log.info("ROOT      : %s", ROOT)
    log.info("DATA_DIR  : %s", DATA_DIR)
    log.info("LOG_FILE  : %s", LOG_FILE)
    log.info("numpy %s | pandas %s", np.__version__, pd.__version__)

    rows = []
    ts_rows = []
    compl_rows = []

    for caso_id, caso in CORPUS_G.items():
        log.info("-" * 70)
        log.info("Caso %s — %s", caso_id, caso["descripcion"])
        log.info("  tipo_muestra=%s | trigger=%s | contaminación: %s",
                 caso["tipo_muestra"], caso["trigger_fecha"],
                 caso["contaminacion_terrestre"])
        log.info("  hub        : %s", caso["hub"])
        log.info("  absorbente : %s", caso["absorbente"])
        log.info("  puntos t/R : %d | cita verificada en sesión: %s",
                 len(caso["t"]), caso["cita_verificada_en_sesion"])

        fit = fit_power_law(caso["t"], caso["R"])
        estado = estado_caso(caso, fit)

        if fit["b"] is None:
            log.warning("  ajuste     : %s (no se imputa ningún valor)",
                        estado)
        else:
            log.info("  ajuste     : b=%+.4f R²=%.4f p=%.6f n=%d [%s]",
                     fit["b"], fit["r2"], fit["p_value"], fit["n"],
                     significancia(fit["p_value"]))

        for k, v in caso["valores_reportados"].items():
            log.info("  reportado  : %s = %s", k, v)

        rows.append({
            "id": caso_id,
            "descripcion": caso["descripcion"],
            "dominio": caso["dominio"],
            "tipo_muestra": caso["tipo_muestra"],
            "hub": caso["hub"],
            "absorbente": caso["absorbente"],
            "contaminacion_terrestre": caso["contaminacion_terrestre"],
            "trigger_año": caso["trigger_año"],
            "trigger_fecha": caso["trigger_fecha"],
            "tipo_trigger": caso["tipo_trigger"],
            "t_unidad": caso["t_unidad"],
            "a": fit["a"],
            "b": fit["b"],
            "r2": fit["r2"],
            "p": fit["p_value"],
            "n": fit["n"],
            "significancia": significancia(fit["p_value"]),
            "estado": estado,
            "eje_axioma": ";".join(str(x) for x in caso["eje_axioma"]),
            "campo_candidato": caso["campo_candidato"],
            "cita_verificada_en_sesion": caso["cita_verificada_en_sesion"],
            "estimado": caso["estimado"],
            "datos_pendientes": caso["datos_pendientes"],
            "fuente": caso["fuente"],
        })

        for t_val, r_val in zip(caso["t"], caso["R"]):
            ts_rows.append({
                "id": caso_id, "dominio": caso["dominio"],
                "t": t_val, "R": r_val, "t_unidad": caso["t_unidad"],
            })

        for comp in caso.get("ajustes_complementarios", []):
            cfit = fit_power_law(comp["t"], comp["R"])
            if cfit["b"] is None:
                log.warning("  complementario %s: n=%d < 3, sin ajuste",
                            comp["nombre"], cfit["n"])
            else:
                log.info("  complementario %s: b=%+.4f R²=%.4f p=%.6f "
                         "n=%d [%s]", comp["nombre"], cfit["b"],
                         cfit["r2"], cfit["p_value"], cfit["n"],
                         significancia(cfit["p_value"]))
            compl_rows.append({
                "id": caso_id, "ajuste": comp["nombre"],
                "t": ";".join(str(x) for x in comp["t"]),
                "R": ";".join(f"{x:.4f}" for x in comp["R"]),
                "a": cfit["a"], "b": cfit["b"], "r2": cfit["r2"],
                "p": cfit["p_value"], "n": cfit["n"],
                "significancia": significancia(cfit["p_value"]),
                "nota": comp["nota"],
            })

    df = pd.DataFrame(rows)
    df_ts = pd.DataFrame(ts_rows, columns=["id", "dominio", "t", "R",
                                           "t_unidad"])

    df_compl = pd.DataFrame(compl_rows, columns=[
        "id", "ajuste", "t", "R", "a", "b", "r2", "p", "n",
        "significancia", "nota"])

    df.to_csv(OUT_CSV, index=False, encoding="utf-8")
    df_ts.to_csv(OUT_TS_CSV, index=False, encoding="utf-8")
    df_compl.to_csv(OUT_COMPL, index=False, encoding="utf-8")
    escribir_fuentes(df)
    escribir_changelog_entry(df)

    log.info("=" * 70)
    log.info("RESUMEN DOMINIO G")
    log.info("=" * 70)
    log.info("Casos                          : %d", len(df))
    log.info("Con serie temporal real        : %d",
             int((df["n"] >= 3).sum()))
    log.info("Pendientes (t/R vacíos)        : %d",
             int(df["estado"].str.startswith("PENDIENTE").sum()))
    log.info("Citas verificadas en sesión    : %d / %d",
             int(df["cita_verificada_en_sesion"].sum()), len(df))
    log.info("Retorno de muestra (contam. 0) : %d",
             int((df["tipo_muestra"] == "retorno_de_muestra").sum()))
    log.info("Caídas                         : %d",
             int((df["tipo_muestra"] == "caida").sum()))
    axiomas = sorted({int(a) for s in df["eje_axioma"]
                      for a in s.split(";")})
    log.info("Axiomas v32 cubiertos          : %s", axiomas)
    log.info("Relación transversal registrada: %s (eje: %s)",
             RELACION_TRANSVERSAL["id"], RELACION_TRANSVERSAL["eje"])
    ajustados = df[df["n"] >= 3]
    if len(ajustados) == 0:
        log.info("b / R² / p del dominio         : NO EXISTEN todavía "
                 "(ningún valor imputado)")
    for _, r in ajustados.iterrows():
        log.info("AJUSTE %s: b=%+.4f R²=%.4f p=%.6f n=%d [%s] — n mínimo, "
                 "1 g.l.; conteo de diversidad, medición única por piedra",
                 r["id"], r["b"], r["r2"], r["p"], r["n"], r["significancia"])
    log.info("Salidas:")
    log.info("  %s", OUT_CSV)
    log.info("  %s (%d filas)", OUT_TS_CSV, len(df_ts))
    log.info("  %s (%d filas)", OUT_COMPL, len(df_compl))
    log.info("  %s", OUT_FUENTES)
    log.info("  %s", OUT_CHANGELOG)
    log.info("  %s", LOG_FILE)
    log.info("Fin.")
