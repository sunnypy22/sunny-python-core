# 06_list_comprehension.py

# Basic
squares = [x**2 for x in range(1, 11)]
print("Squares 1–10:", squares)
# With condition
evens_squared = [x**2 for x in range(1, 21) if x % 2 == 0]
print("Even numbers squared:", evens_squared)

# Nested
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print("Flattened:", flat)

# With if-else
labels = ["positive" if n > 0 else "non-positive" for n in [-3, 0, 5, -1, 7]]
print("Labels:", labels)