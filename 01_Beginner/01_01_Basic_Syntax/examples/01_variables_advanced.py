# Advanced - Type Hints + Walrus
from typing import List
scores: List[int] = [95, 87, 92]
if (length := len(scores)) > 2:
    print(f"Length is {length}")

# Memory reference
a = [1, 2, 3]
b = a
b.append(4)
print(a)          # [1,2,3,4] ← same object
print(id(a) == id(b))


