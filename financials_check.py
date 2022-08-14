import yfinance as yf

def financials_check(ticker):
    stock = yf.Ticker(ticker)

    total_cash = stock.cashflow.iloc[9]
    cap_exp = stock.cashflow.iloc[15]

    free_cash_flow = total_cash[0] + cap_exp[0]

    fcf_formatted = "£{:0,.0f}".format(free_cash_flow)

    return fcf_formatted

