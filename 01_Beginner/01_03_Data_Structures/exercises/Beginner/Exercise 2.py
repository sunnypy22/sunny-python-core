# Create a tuple of 4 numbers. Unpack it into 4 variables.
# Exercise 2 - Tuple unpacking
numbers = (15, 27, 8, 42)
# Unpack into variables
a, b, c, d = numbers
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
# One-liner style with meaningful names
min_temp, max_temp, avg_temp, humidity = (18, 32, 25.5, 65)
print(f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C, Humidity: {humidity}%")
# Output:
# a = 15
# b = 27
# c = 8
# d = 42
# Min: 18°C, Max: 32°C, Avg: 25.5°C, Humidity: 65%
