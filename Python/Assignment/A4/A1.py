import numpy as np

# Example temperature data (5 cities over 7 days)
temperatures = np.array([
    [30, 32, 34, 33, 31, 35, 36],
    [29, 31, 33, 34, 32, 36, 38],
    [28, 29, 32, 31, 30, 34, 33],
    [25, 27, 29, 30, 28, 31, 32],
    [20, 22, 24, 26, 25, 23, 27]
])

# 1. Average temperature per city
avg_temp_per_city = np.mean(temperatures, axis=1)
print("Average temperature per city:", avg_temp_per_city)

# 2. Hottest day overall and in each city
hottest_day_each_city = np.max(temperatures, axis=1)
hottest_day_overall = np.max(temperatures)
print("Hottest day in each city:", hottest_day_each_city)
print("Hottest day overall:", hottest_day_overall)

# 3. City with the highest average temperature
highest_avg_city_index = np.argmax(avg_temp_per_city)
print("City with the highest average temperature:", highest_avg_city_index)

# 4. Days where the temperature exceeded 35°C in any city
days_exceeded_35 = np.where(temperatures > 35)
print("Days where temperature exceeded 35°C:", days_exceeded_35)
