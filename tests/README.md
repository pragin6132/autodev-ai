# Testing Suite Configuration

This directory contains automated unit, integration, and E2E test files for backend and frontend packages.

---

## Test Directory Structure

- **`backend/`**: Pytest verification suites checks backend routes, ORM database commits, and MCP client actions.
- **`frontend/`**: Client side event logic tests.

## Running Tests

### Run Backend Tests:
```bash
pytest
```

### Run Coverage Reports:
```bash
pytest --cov=backend
```
