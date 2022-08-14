import yfinance as yf
from matplotlib import pyplot as plt

def gross_profit_margin_check(ticker):
    stock = yf.Ticker(ticker)

    gross_profit = stock.financials.loc["Gross Profit"][0]
    total_revenue = stock.financials.loc["Total Revenue"][0]

    gross_profit_margin = gross_profit / total_revenue

    return gross_profit_margin