# Docker Setup Documentation

This directory contains container configurations files for AutoDev AI.

---

## Files

- **`Dockerfile.backend`**: Multi-stage Python container using Alpine Linux, copying built packages and configuring non-root privileges.
- **`Dockerfile.frontend`**: Multi-stage Node build generating Vite static files and packaging them into Nginx.

## Build Commands

To build backend image manually:
```bash
docker build -t autodev-backend -f Dockerfile.backend ..
```

To build frontend image manually:
```bash
docker build -t autodev-frontend -f Dockerfile.frontend ..
```
