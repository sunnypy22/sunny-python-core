# 01_list_comprehension.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
cubes_of_odds = [x**3 for x in numbers if x % 2 == 1]
print("Squares:", squares)
print("Evens:", evens)
print("Cubes of odds:", cubes_of_odds)



