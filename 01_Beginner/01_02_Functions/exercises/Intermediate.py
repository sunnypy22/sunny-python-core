#6. Write a function `total(*numbers)` that returns sum of any number of arguments.

def total(*numbers):
    # *numbers becomes a tuple
    return sum(numbers)

# Test cases
print(total(1, 2, 3))          # 6
print(total(10, 20))           # 30
print(total())                 # 0
print(total(5, 15, 25, 35))    # 80

#7. Write a function `person_info(**kwargs)` that prints name, age, city if provided.
def person_info(**kwargs):
    print("Person information:")
    for key, value in kwargs.items():
        print(f"  {key.capitalize():<8}: {value}")

# Different calls
person_info(name="Sunny", age=25, city="Pune")
person_info(name="Aisha", profession="Designer")
person_info()

# Example output for first call:
# Person information:
#   Name    : Sunny
#   Age     : 25
#   City    : Pune

#8. Write a function that uses `global` to modify a variable defined outside.

counter = 0
def increment():
    global counter      # tells Python we want to modify the global variable
    counter += 1
    print(f"Counter is now: {counter}")

# Call multiple times
increment()     # Counter is now: 1
increment()     # Counter is now: 2
increment()     # Counter is now: 3
print("Final counter:", counter)   # Final counter: 3

#9. Sort list of names by length using `lambda` as key in `sorted()`.

names = ["Aarav", "Saanvi", "Vihaan", "Ananya", "Reyansh", "Diya"]

# Sort by length of name (shortest → longest)
sorted_names = sorted(names, key=lambda name: len(name))
print("Sorted by name length:")
for name in sorted_names:
    print(f"{name} ({len(name)} letters)")

# Output example:
# Diya (4 letters)
# Ananya (6 letters)
# Aarav (5 letters)
# Saanvi (6 letters)
# Vihaan (6 letters)
# Reyansh (7 letters)
#10. Write a function `apply_twice(func, x)` that calls func(x) twice.
def apply_twice(func, x):
    # Call the function twice
    first = func(x)
    second = func(first)
    return second

# Example usage with different functions
def double(n):
    return n * 2
def square(n):
    return n * n
print(apply_twice(double, 5))    # 5 → 10 → 20
print(apply_twice(square, 3))    # 3 → 9 → 81


