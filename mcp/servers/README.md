# Model Context Protocol - Servers Config

This directory manages configuration mappings and launch contexts for all external and internal MCP servers.

---

## Server Catalog

AutoDev AI connects to servers to equip agents with tools:

1. **Filesystem Server**:
   - *Tools*: `read_file`, `write_file`, `list_dir`, `grep_search`.
   - *Description*: Controls modifications within the active project workspace.

2. **Command Sandbox Runner**:
   - *Tools*: `run_command`, `manage_task`.
   - *Description*: Executes terminal builds, Pytest suites, and Node processes.

3. **Web Search & Crawler**:
   - *Tools*: `search_web`, `read_url_content`.
   - *Description*: Fetches public API docs and library manuals.
