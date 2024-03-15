import numpy as np
import pandas as pd

# Simulated RSI values for one year (example data)
# Replace this with actual RSI data
rsi_data = pd.DataFrame({'timestamp': pd.date_range(start='2023-01-01', end='2023-12-31', freq='T'),
                         'rsi': np.random.uniform(10, 90, size=(525600,))})

# Capital
capital = 20000

# Function to simulate option trading
def simulate_trades(rsi_data, capital):
    trades = []
    position = None
    entry_price = 0
    
    for index, row in rsi_data.iterrows():
        if row['rsi'] > 80 and position != 'long':
            position = 'long'
            entry_price = row['close']  # Assuming close price for simplicity
            trades.append(('buy', row['timestamp'], entry_price))
        elif row['rsi'] < 20 and position != 'short':
            position = 'short'
            entry_price = row['close']  # Assuming close price for simplicity
            trades.append(('sell', row['timestamp'], entry_price))
        elif position == 'long' and row['close'] >= entry_price * 1.1:
            capital *= 1.1
            position = None
            entry_price = 0
            trades.append(('sell', row['timestamp'], row['close']))
        elif position == 'short' and row['close'] <= entry_price * 0.9:
            capital *= 1.1
            position = None
            entry_price = 0
            trades.append(('buy', row['timestamp'], row['close']))

    return trades, capital

# Run simulation
trades, final_capital = simulate_trades(rsi_data, capital)

# Print trades
for trade in trades:
    print(trade)

# Print final capital
print("Final capital:", final_capital)

