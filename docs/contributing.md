# Contributing Guide

Thank you for your interest in contributing to **AutoDev AI**! Follow these instructions to set up your environment, write tests, and submit changes.

---

## 1. Local Development Setup

1. Fork and clone the repository.
2. Setup virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install development dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Install frontend packages:
   ```bash
   cd frontend
   npm install
   ```

---

## 2. Style and Standards

### Python (Backend)
- Use standard PEP 8 naming and formatting convention.
- Format check command: `black . --check`
- Import sorting command: `isort . --check`
- Linter validation: `flake8`

### Javascript (Frontend)
- Use standard ES6 syntax rules.
- Run code checkers: `npm run lint`

---

## 3. Pull Request (PR) Lifecycle

1. Create a descriptive branch: `git checkout -b feature/agent-communication-loop`
2. Write unit tests for new functionality under `tests/`.
3. Verify existing tests pass.
4. Submit PR against main branch. Ensure all continuous integration (CI) workflow tasks complete successfully.
5. Code reviews are required by the **Team Lead** agent or a human repository maintainer before merge approval.
