import pandas as pd

# Sample data
data = pd.read_csv('historical_price_data.csv', index_col='Date', parse_dates=True)

# Calculate momentum
data['momentum'] = data['Close'].pct_change(periods=10)

# Define buy and sell signals
data['buy_signal'] = np.where(data['momentum'] > 0, 1, 0)
data['sell_signal'] = np.where(data['momentum'] < 0, -1, 0)

# Print signals
print(data[['Close', 'momentum', 'buy_signal', 'sell_signal']])
