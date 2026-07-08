# Model Context Protocol - Custom Tools

This directory contains definitions and script files for custom tools exposed through local MCP servers.

---

## Implementing Custom Tools

Any new custom tool must conform to the Model Context Protocol standards:

1. **Define Tool Schema**:
   Specify a name, detailed description, and a Pydantic-compliant parameter schema.
2. **Implement Tool Handler**:
   Write the execution code mapping parameters to operations.
3. **Expose Tool**:
   Register the handler inside the local MCP server initialization file.
