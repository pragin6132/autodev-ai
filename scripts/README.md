# System Scripts

This directory houses administrative and workspace automation scripts for AutoDev AI.

---

## Script Files

- **`init_project.py`**: Initializes directory workspaces, checks Python runtime versions, and configures `.env` from template variables.
- **`setup.py`**: Facilitates packaging the backend application modules.

## How to run

To initialize project structure:
```bash
python scripts/init_project.py
```

To install project in editable development mode:
```bash
pip install -e .
```
