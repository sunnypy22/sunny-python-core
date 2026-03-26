#1. Write a function `say_hello()` that prints "Hello, World!"
def say_hello():
    print("Hello, World!")
# Call the function
say_hello()
# Output:
# Hello, World!

#2. Write a function `add(a, b)` that returns the sum of two numbers.
def add(a, b):
    return a + b
# Test calls
print(add(5, 7))       # 12
print(add(10, -3))     # 7
print(add(0, 0))       # 0

#3. Write a function `is_positive(n)` that returns `True` if number > 0, else `False`.
def is_positive(n):
    if n > 0:
        return True
    else:
        return False
    # shorter version (same result):
    # return n > 0

# Tests
print(is_positive(42))     # True
print(is_positive(-5))     # False
print(is_positive(0))      # False

#4. Write a function `greet(name, greeting="Hello")` that prints e.g. "Hello, Sunny!"

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Different ways to call

greet("Sunny")                    # Hello, Sunny!
greet("Rahul", "Good morning")    # Good morning, Rahul!
greet("Priya", greeting="Hi")     # Hi, Priya!

#5. Write a function `square(num)` and call it with numbers 1 to 10 using a loop.

def square(num):
    return num * num

# Using a for loop to call it
for i in range(1, 11):
    result = square(i)
    print(f"{i}² = {result}")

# Output:
# 1² = 1
# 2² = 4
# 3² = 9
# 4² = 16
# 5² = 25
# 6² = 36
# 7² = 49
# 8² = 64
# 9² = 81
# 10² = 100