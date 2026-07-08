# Deployment Guide

This document describes the instructions to build, configure, and deploy **AutoDev AI** in production environments.

---

## 1. Local Deployment with Docker Compose

Running the entire stack locally is configured via `docker-compose.yml`.

### Steps:
1. Ensure Docker and Docker Compose are installed.
2. Setup environment settings:
   ```bash
   cp .env.example .env
   ```
3. Set your active LLM provider key in `.env` (e.g. `ANTHROPIC_API_KEY`).
4. Build and start services:
   ```bash
   docker-compose up --build -d
   ```
5. View container states:
   ```bash
   docker-compose ps
   ```

---

## 2. Production Security Best Practices

### 2.1 Sandboxing Execution
- **CRITICAL**: The backend devops agent runs terminal commands. Do not run the backend as root on host.
- Utilize virtual machines or separate AWS ECS / GCP GKE tasks with read-only root filesystems and write permissions limited to target folders.

### 2.2 HTTPS / SSL
- Place the frontend and backend services behind a reverse proxy (e.g., Nginx, Traefik, or AWS ALB) with SSL termination.

### 2.3 Database Management
- Enable database connection pooling and restrict connections to the database container to the backend subnet only.
