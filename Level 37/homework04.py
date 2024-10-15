# Creating the list of daily temperatures
temperatures = [72, 68, 75, 70, 78, 74, 71]

# Calculating and printing the highest temperature
highest_temp = max(temperatures)
print("Highest temperature:", highest_temp)

# Calculating and printing the lowest temperature
lowest_temp = min(temperatures)
print("Lowest temperature:", lowest_temp)

# Calculating and printing the average temperature
average_temp = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temp)

# Using a list comprehension to create a new list above_70
above_70 = [temp for temp in temperatures if temp > 70]

# Printing the above_70 list
print("Temperatures above 70 degrees:", above_70)
