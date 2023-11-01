import pandas as pd
import numpy as np

df = pd.read_pickle('../data/preprocessed.pkl')
# Mean daily return
mean_daily_return = df.groupby('ticker')['daily_return'].mean()

# Standard deviation of daily return
std_daily_return = df.groupby('ticker')['daily_return'].std()

# Annualized mean return (assuming 252 trading days in a year)
annualized_mean_return = mean_daily_return * 252

# Annualized standard deviation (assuming 252 trading days in a year)
annualized_std_return = std_daily_return * np.sqrt(252)

print(annualized_mean_return)
