# Use dict comprehension to create {number: square} for 1–10.
# Exercise 7 - Dictionary comprehension
number_squares = {x: x**2 for x in range(1, 11)}
print("Number → Square dictionary:")
for num, sq in number_squares.items():
    print(f"{num:2} → {sq:3}")
# Output:
# Number → Square dictionary:
#  1 →   1
#  2 →   4
#  3 →   9
# ...
# 10 → 100