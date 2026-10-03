import yfinance as yf
# Download 1 month of S&P 500 ETF data
sp500_data = yf.download("SPY", period="1mo")
print(sp500_data.head())
