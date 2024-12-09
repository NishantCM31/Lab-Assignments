import numpy as np

def get_stock_prices():
    prices = []
    for i in range(4):  # For 4 stocks
        stock_price = []
        print(f"\nEnter prices for Stock {i + 1} for 10 days:")
        for j in range(10):  # 10 days
            price = float(input(f"Day {j + 1}: "))
            stock_price.append(price)
        prices.append(stock_price)
    return np.array(prices)

def daily_percentage_change(prices):
    return np.diff(prices) / prices[:, :-1] * 100

def calculate_volatility(daily_changes):
    return np.var(daily_changes, axis=1)

def best_performing_stock(prices):
    return np.argmax(np.sum(prices[:, 1:] - prices[:, :-1], axis=1))

def find_drops(prices):
    drops = []
    for i in range(4):  # For 4 stocks
        for j in range(1, 10):  # From day 2 to day 10
            if prices[i][j] < prices[i][j - 1] * 0.95:
                drops.append((i + 1, j + 1))
    return drops    

def print_daily_changes(changes):
    print("\nDaily Percentage Change:")
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format("Day", "Stock 1", "Stock 2", "Stock 3", "Stock 4"))
    for day in range(9):  # Only 9 changes
        print("{:<10} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f}".format(day + 2,changes[0][day], changes[1][day], changes[2][day], changes[3][day]))

def main():
    prices = get_stock_prices()

    while True:
        print("\nMenu:")
        print("1. Calculate daily percentage change for each stock")
        print("2. Identify the stock with the highest volatility")
        print("3. Determine the best-performing stock")
        print("4. Find the days where any stock dropped more than 5%")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            changes = daily_percentage_change(prices)
            print_daily_changes(changes)
        
        elif choice == 2:
            changes = daily_percentage_change(prices)
            volatility = calculate_volatility(changes)
            highest_volatility_stock = np.argmax(volatility) + 1
            print(f"\nStock with the highest volatility: Stock {highest_volatility_stock} (Variance: {volatility[highest_volatility_stock - 1]:.2f})")
        
        elif choice == 3:
            best_stock = best_performing_stock(prices)
            print(f"\nBest performing stock over 10 days: Stock {best_stock + 1}")
        
        elif choice == 4:
            drops = find_drops(prices)
            if drops:
                print("\nDays where stock dropped more than 5%:")
                for stock, day in drops:
                    print(f"Stock {stock} dropped on Day {day}")
            else:
                print("\nNo significant drops found.")
        
        elif choice == 5:
            print("Exiting the program.")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
