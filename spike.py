import yfinance as yf
import pandas as pd
import numpy as np

def calculate_intraday_spikes(ticker, start_date, end_date, interval='1m', spike_threshold=0.02):
    # Fetch historical intraday market data
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    
    # Ensure data is sorted by date and time
    data.sort_index(inplace=True)

    # Calculate the percentage change between consecutive prices
    data['Pct Change'] = data['Close'].pct_change()

    # Identify spikes
    data['Spike'] = data['Pct Change'].apply(lambda x: 'Spike Up' if x > spike_threshold else 'Spike Down' if x < -spike_threshold else 'No Spike')

    # Return relevant columns
    return data[['Open', 'Close', 'Pct Change', 'Spike']]

# Define the stock market ticker, start date, and end date
ticker = 'AAPL'  # Example: Apple Inc.
start_date = '2023-07-01'
end_date = '2023-07-31'

# Calculate intraday spikes
intraday_spikes_df = calculate_intraday_spikes(ticker, start_date, end_date)

# Display the result
print(intraday_spikes_df)

# Optionally, save the result to a CSV file
intraday_spikes_df.to_csv('intraday_spikes.csv')
