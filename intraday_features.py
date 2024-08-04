import yfinance as yf
import pandas as pd
import numpy as np

def calculate_intraday_features(ticker, start_date, end_date, interval='1m'):
    # Fetch historical intraday market data
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    
    # Ensure data is sorted by date and time
    data.sort_index(inplace=True)
    
    # Calculate percentage change
    data['Pct Change'] = data['Close'].pct_change()

    # Calculate intraday volatility (standard deviation of percentage changes)
    data['Volatility'] = data['Pct Change'].rolling(window=20).std()

    # Calculate high-low spread
    data['High-Low Spread'] = data['High'] - data['Low']

    # Calculate volume weighted average price (VWAP)
    data['VWAP'] = (data['Close'] * data['Volume']).cumsum() / data['Volume'].cumsum()

    # Calculate moving averages
    data['5-Period MA'] = data['Close'].rolling(window=5).mean()
    data['20-Period MA'] = data['Close'].rolling(window=20).mean()

    # Calculate RSI (Relative Strength Index)
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # Calculate Bollinger Bands
    data['Middle Band'] = data['20-Period MA']
    data['Upper Band'] = data['Middle Band'] + 2 * data['Close'].rolling(window=20).std()
    data['Lower Band'] = data['Middle Band'] - 2 * data['Close'].rolling(window=20).std()

    # Calculate momentum
    data['Momentum'] = data['Close'] - data['Close'].shift(4)
    
    # Calculate MACD
    short_ema = data['Close'].ewm(span=12, adjust=False).mean()
    long_ema = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = short_ema - long_ema
    data['Signal Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

    # Calculate autocorrelation
    data['Autocorrelation'] = data['Close'].rolling(window=20).apply(lambda x: x.autocorr(), raw=False)

    # Return relevant columns
    return data[['Open', 'Close', 'Pct Change', 'Volatility', 'High-Low Spread', 'VWAP', 
                 '5-Period MA', '20-Period MA', 'RSI', 'Middle Band', 'Upper Band', 'Lower Band',
                 'Momentum', 'MACD', 'Signal Line', 'Autocorrelation']]

# Define the stock market ticker, start date, and end date
ticker = 'AAPL'  # Example: Apple Inc.
start_date = '2023-07-01'
end_date = '2023-07-31'

# Calculate intraday features
intraday_features_df = calculate_intraday_features(ticker, start_date, end_date)

# Display the result
print(intraday_features_df)

# Optionally, save the result to a CSV file
intraday_features_df.to_csv('intraday_features.csv')
