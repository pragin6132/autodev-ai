# API Design Specification

This document details the RESTful and WebSocket API endpoints for communicating between the AutoDev AI frontend and backend orchestrator.

---

## 1. REST API Endpoints

### 1.1 Tasks & Projects
- **`GET /api/v1/tasks`**: Retrieve a list of all active and completed tasks.
- **`POST /api/v1/tasks`**: Create a new task/project request.
  - *Payload*: `{ "name": "Feature X", "description": "Implement authentication", "agent_team": "standard" }`
- **`GET /api/v1/tasks/{task_id}`**: Retrieve detailed state, log URLs, and planning stages for a task.
- **`POST /api/v1/tasks/{task_id}/approve`**: Approve the current planning phase to resume execution.
- **`POST /api/v1/tasks/{task_id}/reject`**: Reject the plan and provide feedback/corrections.
  - *Payload*: `{ "feedback": "Use Postgres instead of SQLite in config" }`

### 1.2 Agents & Configurations
- **`GET /api/v1/agents`**: Retrieve available agent types and statuses.
- **`GET /api/v1/mcp/tools`**: Retrieve a list of all tools exposed by connected MCP servers.

---

## 2. WebSocket Interface

### 2.1 Live Agent Execution Streaming
- **Connection URL**: `/api/v1/tasks/{task_id}/stream`
- **Outgoing Events from Server**:
  - `agent_started`: `{ "agent": "planner", "timestamp": "2026-07-08T12:00:00Z" }`
  - `agent_message`: `{ "agent": "planner", "message": "Analyzing directory..." }`
  - `tool_call`: `{ "tool": "read_file", "arguments": { "path": "./main.py" } }`
  - `tool_response`: `{ "status": "success", "lines": 42 }`
  - `task_status_changed`: `{ "status": "verification_pending" }`
  - `agent_completed`: `{ "agent": "planner", "status": "done" }`
