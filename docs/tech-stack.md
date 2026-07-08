# Technology Stack Design

This document details the selected technologies for each layer of the **AutoDev AI** platform, prioritizing modularity, performance, and compliance with the Model Context Protocol (MCP).

---

## 1. Core Frameworks & Languages

### 1.1 Backend Core
- **Python 3.11+**: Chosen for its robust AI/LLM libraries, system scripting capabilities, and overall speed.
- **Pydantic / Pydantic Settings**: For strongly-typed configuration validation and schema definitions.
- **SQLAlchemy & Alembic**: For database ORM mapping and version-controlled migration scripts.

### 1.2 Frontend Core
- **Vanilla CSS + Modern ES6 Javascript**: Providing lightweight, fast UI interfaces without frameworks.
- **Vite**: Modern front-end toolchain providing ultra-fast HMR (Hot Module Replacement) and bundling.

---

## 2. Agent & Protocol Orchestration

- **Model Context Protocol (MCP)**: Standardized protocol developed by Anthropic allowing agents to discover and interact with tools securely.
- **LLM APIs**: SDK integrations for Anthropic Claude, OpenAI GPT-4, and Google Gemini models.

---

## 3. Database & Cache

- **PostgreSQL**: Production-grade relational database to save long-running executions, task lists, messages, and state tracking.
- **SQLite (Local fallback)**: Used in development environment setups for zero-config startup.

---

## 4. Containerization & Infrastructure

- **Docker & Docker Compose**: Orchestrates multi-container execution setups (frontend, backend, database).
- **GitHub Actions**: Automated CI/CD system validating format rules, executing lint checkers, and checking unit tests.
