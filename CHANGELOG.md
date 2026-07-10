# Changelog

## v1.0.0 (2026-07-05)

Initial public release. JGS Archi Bridge is an Eclipse plugin for Archi that embeds an HTTP server speaking the Model Context Protocol (MCP), enabling AI agents to query, analyse, and modify ArchiMate models through natural language.

- 69 MCP tools across querying, searching, creating, layout, routing, quality assessment, batch operations, images, specializations, and view composition.
- 14 MCP resources with ArchiMate reference material, workflow guides, and a viewpoint recipe library.
- Every mutation routes through Archi's own CommandStack, so agent changes are undo-able exactly like a manual edit, with an optional human-owned approval gate.
- A layout and routing engine (ELK-based) with a layout-quality assessment tool, so an agent can detect and fix its own diagrams' defects.
- Optional TLS and bearer-token authentication; loopback-only bind by default.

See the [README](README.md) for the complete tool catalog and documentation.
