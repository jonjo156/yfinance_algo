import yfinance as yf
from dividend_yield import get_dividend_yield
from financials_check import financials_check

ticker = "GRG.L"

print(get_dividend_yield(ticker))
print(financials_check(ticker))