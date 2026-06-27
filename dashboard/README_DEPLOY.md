# Deploy to Hugging Face Spaces

## Option 1: Connect from HF UI (recommended)

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space)
2. Name: `snt-dashboard`
3. SDK: **Streamlit**
4. Click "Create Space"
5. In the Space settings, connect to GitHub repo:
   - Repository: `Inzainos/The-shadow-Node-Theory`
   - Branch: `main`
   - Subdirectory: leave empty (HF will find `app.py` in dashboard/)

## Option 2: Manual files upload

Copy these files to a new HF Space:
- `dashboard/app.py` → `app.py`
- `dashboard/requirements.txt` → `requirements.txt`
- `reconstruction_real/data/snt_corpus_REAL_v5.csv` → `data/snt_corpus_REAL_v5.csv`
- `reconstruction_real/data/snt_corpus_aco_v29.csv` → `data/snt_corpus_aco_v29.csv`

Add this to the Space README.md header:
```yaml
---
title: Shadow Node Theory v2.4.0
emoji: 🔬
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: "1.58.0"
app_file: app.py
pinned: false
license: mit
---
```

## Local testing

```bash
cd The-shadow-Node-Theory
streamlit run dashboard/app.py
```
