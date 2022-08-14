import datetime
import yfinance as yf


def get_dividend_yield(ticker):
    stock = yf.Ticker(ticker)

    dividends = stock.dividends

    latest_price = stock.info['regularMarketPrice']
    this_year_dividends = sum(dividends.loc[lambda x: x.index>datetime.datetime.now() - datetime.timedelta(days=365)])

    dividend_yield = this_year_dividends / latest_price

    dividend_dict = {}

    dividend_dict[ticker] = dividend_yield

    return dividend_dict

