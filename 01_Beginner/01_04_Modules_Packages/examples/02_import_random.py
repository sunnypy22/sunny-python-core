# 02_import_random.py
import random
print("Random Module Examples")
print("Random integer 1-100 :", random.randint(1, 100))
print("Random float 0-1     :", random.random())
print("Random choice        :", random.choice(["apple", "banana", "cherry"]))
numbers = [10, 20, 30, 40, 50]
random.shuffle(numbers)
print("Shuffled list        :", numbers)