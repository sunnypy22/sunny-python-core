#11. Write a function with type hints: `def divide(a: float, b: float) -> float:`

def divide(a: float, b: float) -> float:
    """
    Divide two numbers.
    Returns float result.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Usage
print(divide(10, 2))     # 5.0
print(divide(7, 3))      # 2.333...
# print(divide(5, 0))    # raises ValueError

#12. Use `map()` + lambda to square all numbers in a list.

numbers = [1, 2, 3, 4, 5, 6, 7]
# map() applies lambda to every element
squared = list(map(lambda x: x**2, numbers))
print("Original:", numbers)
print("Squared :", squared)


# Output:
# Original: [1, 2, 3, 4, 5, 6, 7]
# Squared : [1, 4, 9, 16, 25, 36, 49]


#13. Use `filter()` + lambda to get only even numbers from a list.

numbers = [10, 15, 22, 33, 40, 51, 68, 79, 84]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("All numbers:", numbers)
print("Even numbers only:", evens)
# Output:
# All numbers: [10, 15, 22, 33, 40, 51, 68, 79, 84]
# Even numbers only: [10, 22, 40, 68, 84]

#14. Create a closure: function that returns a multiplier function.

def make_multiplier(factor: int):
    """Factory function that creates multiplier functions"""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier
# Create different multipliers
times_two = make_multiplier(2)
times_five = make_multiplier(5)
times_ten = make_multiplier(10)
print(times_two(7))    # 14
print(times_five(3))   # 15
print(times_ten(4))    # 40

#15. Write a decorator that prints "Function started" and "Function ended".
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' started")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' ended")
        return result
    return wrapper
@log_execution
def calculate_sum(a, b):
    return a + b
@log_execution
def say_hello(name):
    print(f"Hello, {name}!")


# Test
print(calculate_sum(8, 12))
say_hello("Sunny")
# Example output:
# Function 'calculate_sum' started
# Function 'calculate_sum' ended
# 20
# Function 'say_hello' started
# Hello, Sunny!
# Function 'say_hello' ended