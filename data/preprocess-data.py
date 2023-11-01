from fetch_data import fetch_data
from constants import START_DATE, END_DATE, TICKER_SYMBOLS

# fetch data from Yahoo Finance


def add_basic_features():
    df = fetch_data(START_DATE, END_DATE, TICKER_SYMBOLS)
    df['daily_return'] = df.groupby('ticker')['Close'].pct_change()
    df['cumulative_return'] = (1 + (df.groupby('ticker')['daily_return']).cumprod() - 1)  # DOesnt work
    df['50_day_moving_avg'] = df.groupby('ticker')['Close'].rolling(window=50).mean().reset_index(level=0, drop=True)
    df['200_day_moving_avg'] = df.groupby('ticker')['Close'].rolling(window=200).mean().reset_index(level=0, drop=True)
    df.sort_index(inplace=True)
    return df

df= add_basic_features()
df.to_pickle('data/preprocessed.pkl')