# 02_tuple_unpack.py
# Tuple creation, unpacking, immutability
coordinates = (10, 20, 30)          # parentheses optional in many cases
x, y, z = coordinates               # unpacking
print("x =", x, "y =", y, "z =", z)
# Single element tuple needs comma
single = (42,)
print("Single element tuple:", single, type(single))
# Tuples are immutable → this would raise error:
# coordinates[0] = 99
# Returning multiple values from function (implicit tuple)
def min_max(values):
    return min(values), max(values)
small, big = min_max([5, 1, 9, 3])
print("Min:", small, "Max:", big)