# Model Context Protocol - Client Layer

This directory contains the client implementation of the Model Context Protocol (MCP) used by the AutoDev AI orchestrator.

---

## Technical Overview

The **MCP Client** is responsible for:
1. **Server Orchestration**: Starting, checking, and terminating connection processes for configured MCP servers.
2. **Session Initialization**: Conducting the standard handshake sequence, sending capability arrays, and validating protocol versions.
3. **Dynamic Schema Parsing**: Fetching tool definitions, and formatting them into a standard JSON tool schema understandable by agent models.
4. **Command Forwarding**: Receiving tool execution requests from agent LLMs, sending them to the target server, and returning the output.
