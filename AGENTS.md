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
`papers/`), the **Genomic Topologic Analyzer** (`genomic_agent/`), and **Delta**
(`delta/`, independent crypto & bolsa signal engine).

## Working method (good practices)

1. **Designated branch → PR → merge to `main`.** Never commit directly to `main`.
2. **Real data first.** No fabricated values in the active corpus; derived data
   cite a primary source (`sources.md`). Missing values stay missing, not zero.
3. **Reproducibility + provenance.** Every result ships with its script and source.
4. **Security.** Never commit PHI, secrets, or `.env` (see `.gitignore`,
   `SECURITY.md`). `genomic_agent` blocks raw patient RNA-seq patterns.
5. **Update `CHANGELOG.md`** on every relevant change (the practice that slips most).
6. **Tests/CI must pass before merge.**

## Commands

```bash
# Lint (config in .flake8) — the single source of truth
flake8 .

# Compile active modules
python -m compileall -q code reconstruction_real genomic_agent dashboard delta

# Smoke test (CI runs this)
python reconstruction_real/code/build_aco_v29.py
```

CI lives in `.github/workflows/python-package-conda.yml` (Conda env `snt-env`
from `environment.yml`): checkout → env → deps → flake8 → compileall → smoke test.

## Commit convention — Conventional Commits

Subject in English, typed prefix: `feat:` `fix:` `docs:` `data:` `refactor:`
`chore:` `test:`. Example: `feat: add crypto real-data adapter`.

## Repository map

- `reconstruction_real/` — real 721-case corpus (data + code + methodology).
- `papers/` — academic documents and preprints (marco teórico v31 is active).
- `genomic_agent/` — SNT Genomic Topologic Analyzer (empirical baseline; validated
  on real TCGA patients up to the full 976-case cohort).
- `delta/` — independent crypto & bolsa signal engine (real CoinGecko + Yahoo data).
- `code/`, `data/` — historical scripts/data (v28).
- `figures/` — publication figures.
- `archive/` — superseded versions (do not cite).

## Tracking

Changes are reflected across **GitHub** (code) + **Asana** (tasks) + **Notion**
(docs/status).

## Security reports

Do not open a public issue. Email **elan.zainos.corona@gmail.com**
(Elán Zainos Corona — Fractal Core Research).
