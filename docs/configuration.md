<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->

# Configuring JGS Archi Bridge

There are no environment variables and no config file to edit by hand. Every
setting lives in Archi's own preferences UI: **Window > Preferences > MCP
Server**.

## Settings

| Setting | Default | Description |
|---|---|---|
| **Port** | `18090` | HTTP(S) server port |
| **Bind Address** | `127.0.0.1` | Network interface (localhost only by default) |
| **Auto-Start** | `false` | Start the server automatically when Archi launches |
| **Log Level** | `INFO` | Logging verbosity: `DEBUG`, `INFO`, `WARN`, `ERROR` |
| **Enable TLS** | `false` | Use HTTPS with TLS encryption |
| **Keystore File** | *(empty)* | Path to PKCS12/JKS keystore (auto-generated if using self-signed) |
| **Keystore Password** | *(empty)* | Password for the keystore file, stored in your OS keychain via Equinox secure storage; never written to disk in cleartext |
| **Enable bearer-token authentication** | `false` | Require an `Authorization: Bearer <token>` header on every request |

## Worked example

See [`examples/mcp.json.example`](../examples/mcp.json.example), the
Claude Code `.mcp.json` entry for the default, no-auth configuration:

```json
{
  "mcpServers": {
    "archi": {
      "type": "http",
      "url": "http://127.0.0.1:18090/mcp"
    }
  }
}
```

`type: http` tells the client to speak Streamable HTTP directly to the
`url`; there is no command to launch, because the server already runs
inside Archi. If you change the port or bind address in preferences, update
`url` to match. If your client doesn't support Streamable HTTP natively
(Claude Desktop), or you enable bearer-token authentication, see the
[README's client-configuration section](../README.md#2-configure-your-llm-client)
for the proxy and header variants.

## TLS / HTTPS

1. In preferences, check **Enable TLS (HTTPS)**.
2. Click **Generate Self-Signed Certificate** to create a keystore
   automatically.
3. Restart the server: the endpoint changes to `https://127.0.0.1:18090`.

Clients must trust the self-signed certificate (use `curl -k` for testing;
import the certificate into your client's trust store or the JVM `cacerts`
otherwise). The keystore password lives in your OS keychain via Equinox
secure storage, never in a plaintext preference file.

## Security notes

By default the server requires no authentication and binds to loopback
only, so anything that can reach `127.0.0.1:18090` on your own machine can
call the tools. To require a secret even on loopback, or before binding to
a non-loopback address, enable the opt-in bearer token in **Window >
Preferences > MCP Server > Authentication**; a 256-bit token generates
automatically on first opt-in and is stored in your OS keychain, never in a
config file. Rotate it with **Generate / Regenerate token**, which
invalidates any client still using the old value. If you bind off-loopback,
also enable TLS so the token isn't sent in cleartext.

Read [`SECURITY.md`](../SECURITY.md) for the full trust-boundary breakdown
(what the server protects against by default versus what is the operator's
responsibility) before binding off-loopback or pointing an agent at
untrusted input.
