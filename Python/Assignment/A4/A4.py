import numpy as np

# Example stock prices (4 stocks over 10 days)
stock_prices = np.array([
    [100, 102, 101, 105, 104, 106, 107, 109, 108, 110],
    [50, 52, 51, 55, 54, 53, 56, 57, 56, 59],
    [200, 202, 204, 205, 206, 209, 208, 210, 212, 213],
    [150, 148, 149, 152, 151, 154, 155, 157, 156, 158]
])

# 1. Calculate the daily percentage change for each stock
daily_pct_change = np.diff(stock_prices, axis=1) / stock_prices[:, :-1] * 100
print("Daily percentage change:\n", daily_pct_change)

# 2. Identify the stock with the highest volatility (variance in daily returns)
volatility = np.var(daily_pct_change, axis=1)
most_volatile_stock = np.argmax(volatility)
print("Most volatile stock:", most_volatile_stock)

# 3. Determine the best-performing stock over the 10-day period
best_performing_stock = np.argmax(stock_prices[:, -1] - stock_prices[:, 0])
print("Best performing stock:", best_performing_stock)

# 4. Find the days where any stock price dropped more than 5% from the previous day
drop_days = np.where(np.diff(stock_prices, axis=1) / stock_prices[:, :-1] < -0.05)
print("Days where any stock price dropped more than 5%:", drop_days)
