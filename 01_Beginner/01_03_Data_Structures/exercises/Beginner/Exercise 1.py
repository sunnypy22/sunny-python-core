#Create a list of 5 favorite fruits. Add one more, remove one, print reversed.


# Exercise 1 - List operations
favorite_fruits = ["mango", "banana", "apple", "orange", "grapes"]
print("Original list:", favorite_fruits)
# Add one more
favorite_fruits.append("pineapple")
print("After append:", favorite_fruits)
# Remove one (by value or index)
favorite_fruits.remove("banana")          # remove by value
# or: favorite_fruits.pop(1)              # remove by index
print("After remove:", favorite_fruits)
# Print reversed (without modifying original)
print("Reversed:", favorite_fruits[::-1])
# Alternative: modify in place
favorite_fruits.reverse()
print("Reversed in place:", favorite_fruits)
# Example output:
# Original list: ['mango', 'banana', 'apple', 'orange', 'grapes']
# After append: ['mango', 'banana', 'apple', 'orange', 'grapes', 'pineapple']
# After remove: ['mango', 'apple', 'orange', 'grapes', 'pineapple']
# Reversed: ['pineapple', 'grapes', 'orange', 'apple', 'mango']