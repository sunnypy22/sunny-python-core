#Use list comprehension to create list of squares 1–20.

# Exercise 6 - List comprehension
squares = [x**2 for x in range(1, 21)]
print("Squares from 1 to 20:")
print(squares)
# Bonus: only odd numbers squared
odd_squares = [x**2 for x in range(1, 21) if x % 2 == 1]
print("\nOdd numbers squared:", odd_squares)
# Output (partial):
# Squares from 1 to 20:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]