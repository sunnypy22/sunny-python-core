#Create two sets: even numbers 0–10, multiples of 3 0–10. Print union, intersection.

# Exercise 3 - Set operations


evens = set(range(0, 11, 2))                # {0,2,4,6,8,10}
multiples_of_3 = set(range(0, 11, 3))       # {0,3,6,9}
print("Evens:", evens)

print("Multiples of 3:", multiples_of_3)
print("\nUnion:", evens | multiples_of_3)
print("Intersection:", evens & multiples_of_3)
print("Evens only:", evens - multiples_of_3)
print("Multiples of 3 only:", multiples_of_3 - evens)

# Output example:
# Evens: {0, 2, 4, 6, 8, 10}
# Multiples of 3: {0, 3, 6, 9}
# Union: {0, 2, 3, 4, 6, 8, 9, 10}
# Intersection: {0, 6}