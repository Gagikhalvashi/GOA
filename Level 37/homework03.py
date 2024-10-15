# Creating the list of integers from 1 to 10
numbers = list(range(1, 11))

# Using list slicing to create first_half
first_half = numbers[:5]

# Using list slicing to create second_half
second_half = numbers[5:]

# Using a list comprehension to create squares
squares = [num ** 2 for num in numbers]

# Printing all three lists
print("First half:", first_half)
print("Second half:", second_half)
print("Squares:", squares)
