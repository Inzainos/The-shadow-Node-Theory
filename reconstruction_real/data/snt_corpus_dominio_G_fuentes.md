# Provenance — Dominio G (paquetes cósmicos / desempaquetado)

Generado por `reconstruction_real/code/build_dominio_G.py` el 2026-09-11. Bloque para pegar en `data/FUENTES.md`.

> Regla del repo (AGENTS.md): **real data first**. Este dominio se entrega con metadatos y citas primarias; las series temporales `t`/`R` están vacías porque ningún caso publicado ofrece hoy ≥3 puntos de señal orgánica vs tiempo de exposición para un mismo cuerpo. NaN, no cero.

## Casos

| id | tipo_muestra | trigger | cita verificada en sesión | estado |
|---|---|---|---|---|
| `G01_Murchison_1969` | caida | 1969-09-28 | sí | PENDIENTE — sin serie temporal real |
| `G02_Ryugu_Hayabusa2_2020` | retorno_de_muestra | 2020-12-06 | sí | PENDIENTE — sin serie temporal real |
| `G03_Bennu_OSIRISREx_2023` | retorno_de_muestra | 2023-09-24 | sí | AJUSTADO |
| `G04_Orgueil_1864` | caida | 1864-05-14 | sí | PENDIENTE — sin serie temporal real |
| `G05_TagishLake_2000` | caida | 2000-01-18 | NO | PENDIENTE — sin serie temporal real |

## Fuentes primarias por caso

### `G01_Murchison_1969`

Kvenvolden K. et al. (1970). Evidence for extraterrestrial amino-acids and hydrocarbons in the Murchison meteorite. Nature 228, 923-926. DOI 10.1038/228923a0; Kvenvolden K., Lawless J., Ponnamperuma C. (1971). Nonprotein amino acids in the Murchison meteorite. PNAS 68(2), 486-490; Cronin J.R. & Moore C.B. (1971). Science 172, 1327; Engel M.H. & Macko S.A. (1997). Isotopic evidence for extraterrestrial non-racemic amino acids in the Murchison meteorite. Nature 389, 265; Koga T. et al. (2024). Abundant extraterrestrial purine nucleobases in the Murchison meteorite. Geochim. Cosmochim. Acta 365, 253-265; Glavin D.P. et al. (2018). In: Primitive Meteorites and Asteroids (Abreu N., ed.), Elsevier, 205-271

**Campo candidato para `t`/`R`:** Fracción de aminoácidos no proteinogénicos (AIB, isovalina) sobre el inventario total, o grado de racemización de aminoácidos quirales, medida en alícuotas curadas con historial documentado, en función del tiempo de residencia terrestre desde 1969. Requiere revisión de literatura de re-análisis 1970→2024 con condiciones de almacenamiento registradas.

### `G02_Ryugu_Hayabusa2_2020`

Oba Y. et al. (2023). Uracil in the carbonaceous asteroid (162173) Ryugu. Nat. Commun. 14, 1292. DOI 10.1038/s41467-023-36904-3; Naraoka H. et al. (2023). Soluble organic molecules in samples of the carbonaceous asteroid (162173) Ryugu. Science 379, abn9033; Parker E. et al. (2023). Extraterrestrial amino acids and amines identified in asteroid Ryugu samples returned by the Hayabusa2 mission. Geochim. Cosmochim. Acta 347, 42-57; Yada T. et al. (2022). Preliminary analysis of the Hayabusa2 samples returned from C-type asteroid Ryugu. Nat. Astron. 6, 214-220; Yokoyama T. et al. (2023). Science 379, eabn7850; Oba Y. et al. (2026). A complete set of canonical nucleobases in the carbonaceous asteroid (162173) Ryugu. Nat. Astron. DOI 10.1038/s41550-026-02791-z

**Campo candidato para `t`/`R`:** Concentración de uracilo (y B3) por muestra en función de la dosis de exposición espacial estimada (superficie vs subsuperficie). Hoy solo existen 2 puntos (A0106, C0107): n=2 < 3, no ajustable. Se necesitan alícuotas adicionales o un proxy de dosis por grano.

### `G03_Bennu_OSIRISREx_2023`

Mojarro A., Aponte J.C., Dworkin J.P., Elsila J.E., Glavin D.P., Connolly H.C., Lauretta D.S. (2025). Prebiotic organic compounds in samples of asteroid Bennu indicate heterogeneous aqueous alteration. PNAS 122(49), e2512461122. DOI 10.1073/pnas.2512461122 (Table 2; datos en Astromat DOI 10.60707/1k00-p463, 10.60707/sxy1-sq73, 10.60707/kacg-nb16); Glavin D.P., Dworkin J.P. et al. (2025). Abundant ammonia and nitrogen-rich soluble organic matter in samples from asteroid (101955) Bennu. Nat. Astron. DOI 10.1038/s41550-024-02472-9; McCoy T.J. et al. (2025). An evaporite sequence from ancient brine recorded in Bennu samples. Nature 637, 1072-1077; Lauretta D.S. et al. (2024). Asteroid (101955) Bennu in the laboratory. Meteorit. Planet. Sci. 59, 2453-2486; PNAS (2025). Prebiotic organic compounds in samples of asteroid Bennu indicate heterogeneous aqueous alteration. DOI 10.1073/pnas.2512461122

**Campo candidato para `t`/`R`:** POBLADO (n=3, diversidad). Siguiente paso: abundancias absolutas (nmol/g) por piedra con el mismo proxy, o más piedras por litología, para subir n y pasar de conteo a concentración.

### `G04_Orgueil_1864`

Aponte J. et al. (2023). Organic-soluble compounds in asteroid Ryugu samples A0106 and C0107 and the Orgueil (CI1) meteorite. Earth Planets Space 75, 28; Oba Y. et al. (2026). Nat. Astron. DOI 10.1038/s41550-026-02791-z; Burton A.S. et al. (2014). The effects of parent-body hydrothermal heating on amino acid abundances in CI-like chondrites. Polar Sci. 8, 255-263; Stoks P.G. & Schwartz A.W. (1979). Uracil in carbonaceous meteorites. Nature 282, 709-710

**Campo candidato para `t`/`R`:** Mismo índice que G01 (fracción no proteinogénica o racemización) en alícuotas de distintas colecciones con historial de curación conocido, contra tiempo de residencia. Caso de mayor t disponible (>160 años) pero con provenance de alícuota más incierta.

### `G05_TagishLake_2000`

Brown P.G. et al. (2000). The fall, recovery, orbit, and composition of the Tagish Lake meteorite: a new type of carbonaceous chondrite. Science 290, 320-325 [POR VERIFICAR — cita de memoria, no confirmada en sesión]

**Campo candidato para `t`/`R`:** Mismo índice que G01/G04. Su valor es de control: caída natural con contaminación cercana a la de un retorno de muestra.

## Relación transversal registrada (no temporal)

`GX01_purina_pirimidina_vs_amoniaco` — Ratio purina/pirimidina correlaciona negativamente con amoníaco entre Ryugu, Bennu y Orgueil (mineralogía y composición elemental similares). Murchison enriquecido en purinas, Ryugu ≈ equilibrado, Bennu y Orgueil enriquecidos en pirimidinas.

Eje: química del entorno receptor (amoníaco) — no tiempo. Valores numéricos: {'purina_sobre_pirimidina': {'Bennu': 0.55, 'Orgueil': 1.1, 'Murchison': 2.8, 'Ryugu': None}, 'amoniaco_nmol_g': {'Bennu': 13600, 'Murchison': '≈1130 (1/12)', 'Ryugu': '≈181 (1/75)', 'Orgueil': None}, 'fuente_cifras': 'Glavin 2025, Nat. Astron. (texto principal y Extended Data Table 6)'}. Puntos limpios con ambas variables: Bennu y Murchison (n=2). Orgueil tiene ratio pero amoníaco discrepante entre extractos; Ryugu tiene amoníaco pero ratio solo cualitativo (≈1, Oba 2026). n limpio = 2 < 3: sigue sin ajustar. Eje 'resonancia del receptor' (Axioma 2), no el eje temporal de ACO-A.

Fuente: Oba Y. et al. (2026). A complete set of canonical nucleobases in the carbonaceous asteroid (162173) Ryugu. Nat. Astron. DOI 10.1038/s41550-026-02791-z
