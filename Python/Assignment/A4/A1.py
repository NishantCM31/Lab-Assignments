import numpy as np

def input_temperature_data():
    cities = []
    for i in range(5):
        city_name = input(f"Enter the name of city {i + 1}: ")
        cities.append(city_name)
    
    temperature_data = []
    for city in cities:
        while True:
            print(f"Enter the temperatures for {city} over 7 days (space-separated): ")
            temperatures = list(map(float, input().split()))
            if len(temperatures) == 7:
                temperature_data.append(temperatures)
                break
            else:
                print("Please enter exactly 7 temperature readings.")
    
    return cities, np.array(temperature_data)

def calculate_average_temperature(temperature_data):
    return np.mean(temperature_data, axis=1)

def find_hottest_day_overall(temperature_data):
    return np.max(temperature_data)

def find_hottest_day_per_city(temperature_data):
    return np.max(temperature_data, axis=1)

def identify_city_with_highest_average(average_temperatures, cities):
    max_avg_index = np.argmax(average_temperatures)
    return cities[max_avg_index], average_temperatures[max_avg_index]

def identify_days_above_threshold(temperature_data, threshold=35):
    days_exceeding_threshold = []
    for day in range(7):
        if any(temperature_data[:, day] > threshold):
            days_exceeding_threshold.append(day + 1) 
    return days_exceeding_threshold

def main():
    print("Welcome to the Climate Data Analysis Program")
    
    cities, temperature_data = input_temperature_data()
    
    while True:
        print("\nMenu:")
        print("1. Calculate average temperature per city")
        print("2. Find the hottest day overall")
        print("3. Find the hottest day in each city")
        print("4. Identify the city with the highest average temperature")
        print("5. Identify days where temperature exceeded 35°C")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            avg_temps = calculate_average_temperature(temperature_data)
            for i, city in enumerate(cities):
                print(f"Average temperature for {city}: {avg_temps[i]:.2f}°C")
        
        elif choice == 2:
            hottest_overall = find_hottest_day_overall(temperature_data)
            print(f"Hottest temperature overall: {hottest_overall:.2f}°C")
        
        elif choice == 3:
            hottest_per_city = find_hottest_day_per_city(temperature_data)
            for i, city in enumerate(cities):
                print(f"Hottest day for {city}: {hottest_per_city[i]:.2f}°C")
        
        elif choice == 4:
            avg_temps = calculate_average_temperature(temperature_data)
            city, highest_avg = identify_city_with_highest_average(avg_temps, cities)
            print(f"City with highest average temperature: {city} ({highest_avg:.2f}°C)")
        
        elif choice == 5:
            days = identify_days_above_threshold(temperature_data)
            if days:
                print(f"Days where temperature exceeded 35°C: {', '.join(map(str, days))}")
            else:
                print("No days exceeded 35°C.")
        
        elif choice == 6:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please try again.")


main()
