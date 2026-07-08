# Product Roadmap

The development trajectory of **AutoDev AI** is divided into four main phases, starting from a local architecture-ready scaffold to a production-grade multi-tenant platform.

---

## Phase 1: Foundation (Current State)
- [x] Complete project directory structure scaffolding.
- [x] Create initial documentation (Architecture, API, Requirements).
- [x] Design Agent Prompt templates.
- [x] Draft Database sql schemas and Docker files.

## Phase 2: Local MVP Orchestrator
- [ ] Implement backend orchestrator server.
- [ ] Build the core MCP client parser.
- [ ] Connect standard filesystem and command-runner MCP servers.
- [ ] Integrate local SQLite database store.
- [ ] Develop simple static HTML/JS dashboard showing execution tree.

## Phase 3: Advanced Agent Capabilities & Collaboration
- [ ] Implement Plan-Execute-Verify loops.
- [ ] Integrate multiple LLM adapters (OpenAI, Anthropic, Gemini).
- [ ] Implement Tester agent with auto-debugging feedback loops.
- [ ] Build real-time streaming UI using WebSockets.
- [ ] Support manual developer checkpoints/approvals in UI.

## Phase 4: Production Scale & Multi-Tenancy
- [ ] Migrate database to production PostgreSQL.
- [ ] Introduce User Authentication & RBAC (Role-Based Access Control).
- [ ] Create containerized agent environments (dynamic sandbox orchestration).
- [ ] Integrate advanced external MCP Servers (Git, Slack, Linear, Cloud providers).
- [ ] Introduce performance analytics and token/cost budgeting features.
