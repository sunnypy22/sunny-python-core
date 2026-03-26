# 01_list_basic.py
# Basic list operations
fruits = ["apple", "banana", "cherry", "date"]
print("Original list:", fruits)
# Add elements
fruits.append("elderberry")
fruits.insert(1, "blueberry")
print("After append & insert:", fruits)
# Modify
fruits[2] = "blackberry"
print("After modification:", fruits)
# Remove
fruits.remove("banana")
popped = fruits.pop()           # removes last by default
print("After remove & pop:", fruits)
print("Popped item:", popped)
# Slicing & length
print("First two:", fruits[:2])
print("Last two:", fruits[-2:])
print("Length:", len(fruits))
print("Reversed:", fruits[::-1])