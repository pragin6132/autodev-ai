# AutoDev AI

Autonomous Multi-Agent Software Engineering Platform powered by Model Context Protocol (MCP).

## Overview

AutoDev AI is a production-ready, autonomous multi-agent platform designed to execute complex software engineering tasks. By leveraging the Model Context Protocol (MCP), AutoDev AI coordinates specialized AI agents (Team Lead, Planner, Frontend, Backend, Tester, DevOps) to collaborate on codebase analysis, system design, code generation, testing, and deployment.

---

## Directory Structure

```text
autodev-ai/
├── .github/
│   └── workflows/
│       └── ci.yml
├── agents/
│   ├── team_lead/
│   │   ├── prompt.md
│   │   └── README.md
│   ├── planner/
│   │   ├── prompt.md
│   │   └── README.md
│   ├── frontend_agent/
│   │   ├── prompt.md
│   │   └── README.md
│   ├── backend_agent/
│   │   ├── prompt.md
│   │   └── README.md
│   ├── tester/
│   │   ├── prompt.md
│   │   └── README.md
│   └── devops/
│       ├── prompt.md
│       └── README.md
├── backend/
│   ├── app/
│   │   └── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── config/
│   ├── settings.py
│   └── README.md
├── database/
│   ├── schema.sql
│   └── README.md
├── docker/
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── README.md
├── docs/
│   ├── requirements.md
│   ├── architecture.md
│   ├── workflow.md
│   ├── roadmap.md
│   ├── tech-stack.md
│   ├── api-design.md
│   ├── deployment.md
│   └── contributing.md
├── frontend/
│   ├── src/
│   │   └── main.js
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
├── mcp/
│   ├── client/
│   │   └── README.md
│   ├── servers/
│   │   └── README.md
│   └── tools/
│       └── README.md
├── scripts/
│   ├── init_project.py
│   ├── setup.py
│   └── README.md
├── tests/
│   ├── backend/
│   │   └── README.md
│   ├── frontend/
│   │   └── README.md
│   └── README.md
├── .env.example
├── .gitignore
├── docker-compose.yml
└── LICENSE
```

---

## Getting Started

1. **Prerequisites**:
   - Python 3.11+
   - Node.js 20+
   - Docker & Docker Compose

2. **Environment Setup**:
   Copy the example environment file and fill in your API keys:
   ```bash
   cp .env.example .env
   ```

3. **Initialize the Project**:
   Run the initialization script to verify configuration and environments:
   ```bash
   python scripts/init_project.py
   ```

## Development and Architecture

Please refer to the `docs/` folder for comprehensive documentation on architecture, API design, workflows, and developer guidelines.
