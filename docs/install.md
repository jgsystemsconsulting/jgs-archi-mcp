<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->

# Installing JGS Archi Bridge

## Prerequisites

- [Archi](https://www.archimatetool.com/) 5.7 or later
- Java 21 or later (Archi's own bundled JRE satisfies this on most installs)
- An MCP-compatible LLM client: Claude Code, Claude Desktop, Cline, or any
  other client that speaks MCP over Streamable HTTP or stdio-via-proxy

## Install

1. Download the latest `.archiplugin` from the
   [Releases](https://github.com/jgsystemsconsulting/jgs-archi-mcp/releases)
   page (or the `bin/` directory in this repository for pre-built
   artifacts).
2. In Archi: **Help > Manage Plug-ins > Install New...**, or copy the file
   directly into Archi's `dropins/` folder.
3. Restart Archi.

## Verify

1. Open (or create) an ArchiMate model in Archi.
2. **MCP Server > Start MCP Server** from the menu bar. The menu item
   toggles to **Stop MCP Server** once running, confirming the embedded
   server started.
3. Test connectivity without an LLM client, using `curl`:

   ```bash
   curl -X POST http://127.0.0.1:18090/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}'
   ```

   A JSON-RPC response (not a connection error) confirms the plugin is
   installed and serving MCP correctly. Full client wiring for Claude Code,
   Claude Desktop, and Cline is in the [README](../README.md#2-configure-your-llm-client);
   the connection settings themselves (port, bind address, TLS, auth) are
   in [`configuration.md`](configuration.md).

## Troubleshooting

- **Server won't start** — check whether port 18090 is already in use
  (`lsof -i :18090` on macOS/Linux, `netstat -ano | findstr :18090` on
  Windows), and confirm the bind address set in preferences is valid.
- **LLM client can't connect** — confirm the Archi menu shows "Stop MCP
  Server" (meaning it's running), that the port in your client config
  matches, and re-run the `curl` command above to isolate the server from
  the client.
- **Model appears empty** — an ArchiMate model must be open in Archi before
  a client connects; if you opened the model after the session started,
  reconnect the client.

For deeper troubleshooting (TLS, secure-storage errors, mutation
validation), see the [README's Troubleshooting section](../README.md#troubleshooting).
