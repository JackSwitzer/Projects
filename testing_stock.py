import yfinance as yf
import pandas as pd
import plotly.express as px

# List of all Fortune 100 companies
#"BRK.B", "ANTM", "FORTUM" "DWDP and "BRK.A" have been removed as they may be delisted?
tickers = ["AAPL", "MSFT", "AMZN", "JPM", "GOOG", "GOOGL", "XOM", "BAC", "WFC", "V", "CVX", "JNJ", "PG", "KO", "T", "PFE", "HD",    "UNP", "INTC", "CSCO", "VZ", "TMO", "PEP", "PNC", "CMCSA", "WMT", "BA",    "USB", "MA", "MCD", "C", "IBM", "MDT", "ABT", "NKE", "CRM", "ADBE",    "ACN", "COST", "PM", "HON", "TJX", "ORCL", "LLY", "DHR", "LMT", "BABA",    "HPE", "MMM", "MMC", "CVS", "PRU", "AVGO", "UNH", "MDLZ", "GILD", "AXP",    "BK", "APTV", "CHTR", "LOW", "FIS", "ITW", "UPS", "DIS", "TXN", "GE",    "AMT", "BAX", "EMR", "CME", "CAT", "ADP", "SCHW", "CCI", "RTX",    "AFL", "SO", "DUK", "NEE", "DE", "BIDU", "PPG", "AEP", "MCK", "D", "AMGN",    "GIS", "EXC", "DOW", "HUM", "PSX", "CNI", "PPL", "FDX", "NOC"]

# Download the stock price data for all Fortune 100 companies
data = yf.download(tickers, start="2022-01-01", end="2022-12-31")

# Reshape the data into a long format
df = data.stack().reset_index().rename(columns={'level_0': 'Date', 'level_1': 'Ticker', 0: 'Close'})

# Plot the data using plotly.express
fig = px.line(df, x="Date", y="Close",title="All Fortune 100 Company stock prices for 2022", color='Ticker')
fig.show()