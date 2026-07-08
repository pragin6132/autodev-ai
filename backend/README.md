# AutoDev AI - Backend Server

This directory contains the Python-based backend orchestration layer for the AutoDev AI platform.

---

## Structure Overview

- **`app/`**: Contains core modules including agent configurations, state engine, and server configuration.
- **`main.py`**: Entrance script setup to initialize configuration settings and start the app daemon.
- **`requirements.txt`**: Standard dependencies list.

## Local setup without Docker

1. Ensure Python 3.11+ is installed.
2. Initialize environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the environment template from the root folder:
   ```bash
   cp ../.env.example .env
   ```
5. Launch the backend engine daemon:
   ```bash
   python main.py
   ```
