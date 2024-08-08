import pandas as pd

# Example closing prices for 9 days
closing_prices = [44.34, 44.09, 44.15, 43.61, 44.33, 44.83, 45.10, 45.42, 45.84]

# Convert the list to a pandas DataFrame
data = pd.DataFrame(closing_prices, columns=['Close'])

# Calculate the daily price changes
data['Change'] = data['Close'].diff()

# Separate gains and losses
data['Gain'] = data['Change'].apply(lambda x: x if x > 0 else 0)
data['Loss'] = data['Change'].apply(lambda x: -x if x < 0 else 0)

# Calculate the average gain and average loss
avg_gain = data['Gain'].mean()
avg_loss = data['Loss'].mean()

# Calculate the Relative Strength (RS)
rs = avg_gain / avg_loss

# Calculate the RSI
rsi = 100 - (100 / (1 + rs))

# Print the RSI value
print(f"9-day RSI: {rsi:.2f}")
