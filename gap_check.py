import yfinance as yf
import pandas as pd

def get_gap_up_down(ticker, start_date, end_date):
    # Fetch historical market data
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Ensure the data is sorted by date
    data.sort_index(inplace=True)
    
    # Calculate gaps
    data['Previous Close'] = data['Close'].shift(1)
    data['Gap'] = data['Open'] - data['Previous Close']
    
    # Determine gap type
    data['Gap Type'] = data['Gap'].apply(lambda x: 'Gap Up' if x > 0 else 'Gap Down' if x < 0 else 'No Gap')
    
    # Select relevant columns
    result = data[['Open', 'Previous Close', 'Gap', 'Gap Type']]
    
    return result

if __name__ == "__main__":
    ticker = 'SPY'  # Example ticker for S&P 500 ETF
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    
    gap_data = get_gap_up_down(ticker, start_date, end_date)
    print(gap_data)
