import numpy as np

# Hypothetical options data (implied volatilities)
options_data = {
    'strike_prices': [3000, 3050, 3100],  # Example strike prices
    'call_implied_vol': [0.15, 0.17, 0.18],  # Example call implied volatilities
    'put_implied_vol': [0.16, 0.18, 0.19]  # Example put implied volatilities
}

# Function to calculate the VIX index
def calculate_vix(options_data):
    call_implied_vol = np.array(options_data['call_implied_vol'])
    put_implied_vol = np.array(options_data['put_implied_vol'])

    # Midpoint strike price
    midpoint_strike = (max(options_data['strike_prices']) + min(options_data['strike_prices'])) / 2

    # Interpolate call and put implied volatilities to find the at-the-money volatility
    at_the_money_vol = np.interp(midpoint_strike, options_data['strike_prices'], (call_implied_vol + put_implied_vol) / 2)

    # Square the time to expiration (in days), assuming 30 days for simplicity
    t = (30 / 365) ** 0.5

    # Calculate the variance by multiplying at-the-money volatility by the time to expiration
    variance = at_the_money_vol ** 2 * t

    # Calculate the VIX index
    vix = 100 * variance

    return vix

# Calculate and print the VIX index
vix_index = calculate_vix(options_data)
print("VIX Index:", vix_index)

