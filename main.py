import yfinance as yf
from dividend_yield import get_dividend_yield
from financials_check import financials_check
from gross_profit_margin import gross_profit_margin_check

ticker = "GRG.L"

print(get_dividend_yield(ticker))
print(financials_check(ticker))
print(gross_profit_margin_check(ticker))