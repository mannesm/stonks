import pandas as pd
import yfinance as yf


def fetch_data(start_date, end_date, tickers):
    df = pd.DataFrame()
    for symbol in tickers:
        ticker_info = yf.Ticker(symbol)
        data = ticker_info.history(start=start_date, end=end_date)
        data['ticker'] = symbol
        df = pd.concat([df, data])
        return df
