import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_pickle('data/preprocessed.pkl')

# Basic Visualizations

# Plotting the closing price
df.groupby('ticker')['Close'].plot(legend=True)
plt.title('Closing Price')
plt.show()

# Plotting daily returns
df.groupby('ticker')['daily_return'].plot(legend=True)
plt.title('Daily Returns')
plt.show()

# Plotting cumulative returns
df.groupby('ticker')['cumulative_return'].plot(legend=True)
plt.title('Cumulative Returns')
plt.show()

# Plotting moving averages
df.groupby('ticker')['50_day_moving_avg'].plot(legend=True)
df.groupby('ticker')['200_day_moving_avg'].plot(legend=True)
plt.title('50-day and 200-day Moving Averages')
plt.show()