import yfinance as yf
import pandas as pd

def calculate_gaps_and_moving_average(ticker, start_date, end_date, ma_window=20):
    # Fetch historical market data
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Ensure data is sorted by date
    data.sort_index(inplace=True)

    # Calculate the gap
    data['Gap'] = data['Open'] - data['Close'].shift(1)

    # Determine the type of gap
    data['Gap Type'] = data['Gap'].apply(lambda x: 'Gap Up' if x > 0 else 'Gap Down' if x < 0 else 'No Gap')

    # Calculate moving average
    data[f'{ma_window}-Day MA'] = data['Close'].rolling(window=ma_window).mean()

    # Return relevant columns
    return data[['Open', 'Close', 'Gap', 'Gap Type', f'{ma_window}-Day MA']]

# Define the stock market index, start date, and end date
ticker = '^GSPC'  # Example: S&P 500 index
start_date = '2023-01-01'
end_date = '2023-12-31'

# Calculate gaps and moving average
gaps_ma_df = calculate_gaps_and_moving_average(ticker, start_date, end_date)

# Display the result
print(gaps_ma_df)

# Optionally, save the result to a CSV file
gaps_ma_df.to_csv('market_index_gaps_moving_average.csv')
