#!/bin/python3
import os
import yfinance as yf
from requests.exceptions import HTTPError

SYMBOLS = os.environ.get("SYMBOLS")


def get_stock_quote(symbol):
    "returns the current value of a stock in dollars"

    try:
        stock = yf.Ticker(symbol)
        return stock.info["previousClose"]
    except HTTPError:
        return "Unknown"


def main():
    if not SYMBOLS:
        print("SYMBOLS environment variable not set")
        return

    for symbol in SYMBOLS.split(","):
        print(f"{symbol}\t{get_stock_quote(symbol)}")


if __name__ == "__main__":
    main()
