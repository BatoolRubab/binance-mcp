from mcp.server.fastmcp import FastMCP
from typing import Any
import requests

mcp = FastMCP("Binance MCP")

def get_symbol_from_name(name: str) -> str:
    name = name.strip().lower()  # Clean input (e.g. remove \n or spaces)
    if name in ["bitcoin", "btc"]:
        return "BTCUSDT"
    elif name in ["ethereum", "eth"]:
        return "ETHUSDT"
    else:
        return name.upper()  # Assume user gives correct Binance symbol

@mcp.tool()
def get_price(symbol: str) -> Any:
    """
    Get the current price of a crypto asset from Binance
    """
    symbol = get_symbol_from_name(symbol)
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

@mcp.tool()
def get_price_price_change(symbol: str) -> Any:
    """
    Get the 24h price change of a crypto asset from Binance
    """
    symbol = get_symbol_from_name(symbol)
    url = f"https://data-api.binance.vision/api/v3/ticker/24hr?symbol={symbol}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")

