
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/stock-trends")
def get_stock_trends():
    tickers = ['AAPL', 'MSFT', 'TSLA']
    stock_data = {}

    for ticker in tickers:
        try:
            t = yf.Ticker(ticker)
            hist = t.history(period="1d", interval="5m")
            info = t.info
            latest = hist.iloc[-1] if not hist.empty else None
            stock_data[ticker] = {
                "price": float(latest["Close"]) if latest is not None else info.get("regularMarketPrice"),
                "change": info.get("regularMarketChangePercent"),
                "dayHigh": info.get("dayHigh"),
                "dayLow": info.get("dayLow"),
                "volume": info.get("volume"),
            }
        except Exception as e:
            stock_data[ticker] = {"error": f"Failed to fetch data: {str(e)}"}

    suggestions = [
        "AAPL is showing real-time strength in recent candles.",
        "MSFT appears stable; monitor for breakout setups.",
        "TSLA is volatile — watch closely for entry signals."
    ]

    return {"trends": stock_data, "suggestions": suggestions}
