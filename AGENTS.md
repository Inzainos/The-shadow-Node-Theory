# AGENTS.md — Shadow Node Theory (SNT)

Operating guide for AI agents and collaborators working in this repository
(Claude Code, Cursor, Copilot, Codex, …). This is the neutral file all tools
read; `CONTRIBUTING.md` and `dev-guide.md` carry the fuller detail.

> Mirror of the standard used in the sibling `workspaces` repo (Sentinel Omega),
> so both repos speak the same language.

## What this repo is

**Shadow Node Theory** — a research repository: scale-invariant satellization
(`R(t) = a·t^b`) and the Coupled Orbital Collapse layer (ACO-A, `A(τ) = c·τ^Δ`),
with a verified 721-case real corpus. Author: Elán Zainos Corona (Fractal Core
Research, Tlaxcala, Mexico). Code, data, and theory must stay traceable and
reproducible.

Projects housed here: the SNT theory + corpus (`reconstruction_real/`,
`papers/`) and **Delta** (`delta/`, independent crypto & bolsa signal engine).
The **Genomic Topologic Analyzer** migrated to its own standalone project on
2026-10-20: `/home/deamon/genomic_agent` (own git repo, full 45-commit history
preserved via `git subtree split`; Docker services run from there).

## Working method (good practices)

1. **Designated branch → PR → merge to `main`.** Never commit directly to `main`.
2. **Real data first.** No fabricated values in the active corpus; derived data
   cite a primary source (`sources.md`). Missing values stay missing, not zero.
3. **Reproducibility + provenance.** Every result ships with its script and source.
4. **Security.** Never commit PHI, secrets, or `.env` (see `.gitignore`,
   `SECURITY.md`). The standalone `genomic_agent` project blocks raw patient
   RNA-seq patterns and PHI (see its own AGENTS_USE.md).
5. **Update `CHANGELOG.md`** on every relevant change (the practice that slips most).
6. **Report inference honestly.** Per-case p-values in the corpus are inflated
   (serial autocorrelation in Domain B; 714 non-independent cases). Never cite
   the per-row p-value without the audit v32 caveats (README → "Audit v32").
7. **Tests/CI must pass before merge.**

## Commands

```bash
# Lint (config in .flake8) — the single source of truth
flake8 .

# Compile active modules
python -m compileall -q code reconstruction_real dashboard delta

# Smoke test (CI runs this)
python reconstruction_real/code/build_aco_v29.py

# Regression test + full audit re-run (not in CI; run when touching the corpus)
pytest reconstruction_real/tests
python reconstruction_real/code/snt_auditoria_integral_v32.py
```

CI lives in `.github/workflows/python-package-conda.yml` (Conda env `snt-env`
from `environment.yml`): checkout → env → deps → flake8 → compileall → smoke test.

## Commit convention — Conventional Commits

Subject in English, typed prefix: `feat:` `fix:` `docs:` `data:` `refactor:`
`chore:` `test:`. Example: `feat: add crypto real-data adapter`.

## Repository map

- `reconstruction_real/` — real 721-case corpus (data + code + methodology);
  `audits/` holds the v32 integral audit and the Domain B discriminant test,
  `tests/` the regression test (`pytest reconstruction_real/tests`).
- `papers/` — academic documents and preprints. Active conceptual framework:
  **marco teórico v34** (`papers/marco_teorico.md`; lineage in
  `papers/CHANGELOG_marco.md`). Framework and corpus are numbered independently.
- `genomic_agent` — **MOVED 2026-10-20** to `/home/deamon/genomic_agent` (standalone
  project, own git repo with preserved history; Docker services :8081/:8501 loopback
  run from the new location). It remains the empirical genomic application of SNT
  topology (TCGA 976-case validation; 5-Event Wall corpus n=2,746).
- `delta/` — independent crypto & bolsa signal engine (real CoinGecko + Yahoo data).
- `code/` — shared utilities (`snt_utils.py`, audit extension `snt_utils_v32.py`)
  and historical v28 scripts.
- `data/` — source data and provenance (`FUENTES.md`: URLs, editions, SHA-256).
- `dashboard/` — Streamlit dashboard (Hugging Face Spaces).
- `figures/` — publication figures.
- `archive/` — superseded versions (do not cite).

## Tracking

Changes are reflected across **GitHub** (code) + **Asana** (tasks) + **Notion**
(docs/status).

## Security reports

Do not open a public issue. Email **elan.zainos.corona@gmail.com**
(Elán Zainos Corona — Fractal Core Research).
