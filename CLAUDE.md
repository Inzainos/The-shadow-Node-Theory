# CLAUDE.md

Guidance for Claude Code (and other AI agents) working in this repository.

The operating rules live in **[`AGENTS.md`](AGENTS.md)** — read it first. In short:

- Develop on a **designated branch → PR → merge to `main`** (never commit to `main`).
- **Real data first**; reproducibility + provenance; **no PHI/secrets/`.env`**.
- **Update `CHANGELOG.md`** on every relevant change.
- **Conventional Commits** (`feat:`/`fix:`/`docs:`/`chore:`/`test:`…).
- **CI must pass before merge**: `flake8 .` (config in `.flake8`), `compileall`,
  and the ACO smoke test (`reconstruction_real/code/build_aco_v29.py`).

Fuller detail: `AGENTS.md`, `CONTRIBUTING.md`, `dev-guide.md`.

Projects: SNT theory + corpus (`reconstruction_real/`, `papers/`), the Genomic
Topologic Analyzer (`genomic_agent/`), and Delta (`delta/`).
