import yfinance as yf

ticker = yf.Ticker("GRG.L")

print(ticker.financials)