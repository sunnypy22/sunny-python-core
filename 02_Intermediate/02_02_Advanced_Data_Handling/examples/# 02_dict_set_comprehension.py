
names = ["sunny", "priya", "rahul", "neha"]
# Dict comprehension
name_length = {name: len(name) for name in names}
print("Name lengths:", name_length)
# Set comprehension
unique_letters = {char for name in names for char in name}
print("Unique letters:", unique_letters)