# Developer Guide — Shadow Node Theory

This guide summarizes the key commands for working in the repository.

## Conda environments

Create the runtime environment:

```bash
conda env create -f environment.yml
conda activate snt-env
```

Create the development environment:

```bash
conda env create -f environment-dev.yml
conda activate snt-dev-env
```

Update an existing Conda environment:

```bash
conda env update -f environment.yml --prune
```

## Alternative venv setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Common development commands

### Lint Python files

Configuration lives in `.flake8` (select/exclude/etc.), so just run:

```bash
flake8 .
```

### Run smoke test

```bash
python reconstruction_real/code/build_aco_v29.py
```

### Compile active modules

```bash
python -m compileall -q code reconstruction_real genomic_agent dashboard
```

### Run tests

If you add tests in the future, run them with:

```bash
pytest
```

## GitHub Actions CI

The CI workflow is defined in `.github/workflows/python-package-conda.yml`.

It performs:

- checkout of the repository
- Conda environment setup from `environment.yml`
- installation of Python dependencies
- static checking with `flake8`
- Python module compilation
- smoke testing via `build_aco_v29.py`

## Notes

- `environment.yml` is the runtime environment for the project.
- `environment-dev.yml` includes extra development tools such as `pytest`, `pre-commit`, `black`, `isort`, `mypy`, `ruff`, and `tox`.
- Use `python -m pip install -r requirements.txt` only when you need the raw Python dependency list inside a Conda or venv environment.
