# 07_dict_comprehension.py

# {number: square}

squares_dict = {x: x**2 for x in range(1, 11)}
print("Number → Square:", squares_dict)
# Filter
names = ["sunny", "rahul", "priya", "aarav"]
upper_dict = {name: name.upper() for name in names if len(name) > 4}
print("Long names uppercased:", upper_dict)

# From two lists
keys = ["name", "age", "city"]
values = ["Sunny", 25, "Pune"]
person = {k: v for k, v in zip(keys, values)}
print("Zipped dict:", person)