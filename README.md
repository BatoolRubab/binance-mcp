# Binance-mcp
This project is a **Model Context Protocol (MCP)** tool that connects to Binance's API to fetch current cryptocurrency prices and their 24-hour price change using a custom MCP server.

## 🚀 Features

- ✅ Get the current price of any crypto asset
- 📉 Get the 24-hour price change and stats
- ⚡ Easy integration with MCP AI assistants like Claude, Zapier, etc.
- 🧠 Auto-symbol recognition (e.g., "bitcoin" → `BTCUSDT`)

## 🛠️ Tools & Technologies

- Python 3.10+
- [`FastMCP`](https://github.com/Context-Labs/mcp) (MCP server framework)
- Binance Public API
- `requests` for API calls

---
## 🧠 Auto Symbol Handling

You can input friendly names or symbols:

| Input      | Output Symbol |
| ---------- | ------------- |
| `bitcoin`  | `BTCUSDT`     |
| `eth`      | `ETHUSDT`     |
| `dogeusdt` | `DOGEUSDT`    |

Made with ❤️ by Rubab Batool

