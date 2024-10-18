""" import numpy as np

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
 """

import numpy as np

# Updated example stock prices (4 stocks over 10 days)
stock_prices = np.array([
    [100, 105, 103, 110, 108, 115, 117, 120, 119, 125],  # Stock 1
    [50, 55, 52, 57, 54, 53, 60, 63, 62, 65],           # Stock 2
    [200, 205, 204, 210, 215, 220, 225, 223, 230, 235], # Stock 3
    [150, 148, 140, 150, 145, 144, 155, 160, 158, 170]  # Stock 4
])

# 1. Calculate the daily percentage change for each stock
daily_pct_change = np.diff(stock_prices, axis=1) / stock_prices[:, :-1] * 100
print("Daily Percentage Change for Each Stock:")
for i, changes in enumerate(daily_pct_change):
    print(f"Stock {i + 1}: {changes.round(2)}%")

# 2. Identify the stock with the highest volatility (variance in daily returns)
volatility = np.var(daily_pct_change, axis=1)
most_volatile_stock = np.argmax(volatility)
print(f"\nMost Volatile Stock: Stock {most_volatile_stock + 1} (Variance: {volatility[most_volatile_stock]:.2f})")

# 3. Determine the best-performing stock over the 10-day period
price_difference = stock_prices[:, -1] - stock_prices[:, 0]
best_performing_stock = np.argmax(price_difference)
print(f"\nBest Performing Stock: Stock {best_performing_stock + 1} (Price Increase: {price_difference[best_performing_stock]})")

# 4. Find the days where any stock price dropped more than 5% from the previous day
drop_days = np.where(np.diff(stock_prices, axis=1) / stock_prices[:, :-1] < -0.05)
print("\nDays Where Any Stock Price Dropped More Than 5%:")
for stock, day in zip(drop_days[0], drop_days[1]):
    print(f"Stock {stock + 1} on Day {day + 2}")
