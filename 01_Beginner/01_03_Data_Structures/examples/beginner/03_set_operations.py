# 03_set_operations.py



evens = {0, 2, 4, 6, 8, 10}
multiples_of_3 = {0, 3, 6, 9, 12}
print("Evens:", evens)
print("Multiples of 3:", multiples_of_3)
# Operations
print("\nUnion        :", evens | multiples_of_3)
print("Intersection :", evens & multiples_of_3)
print("Difference   :", evens - multiples_of_3)
print("Symmetric diff:", evens ^ multiples_of_3)

# Add / remove

evens.add(12)
evens.discard(0)            # no error if missing

print("\nAfter add & discard:", evens)
# Membership

print("Is 6 in evens?", 6 in evens)