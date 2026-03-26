# Higher-order function: function that takes another function
def apply_operation(a, b, operation):
    """Apply the given operation function to a and b"""
    return operation(a, b)
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
print(apply_operation(10, 4, add))       # 14
print(apply_operation(10, 4, subtract))  # 6
print(apply_operation(10, 4, multiply))  # 40
# Using lambda directly
print(apply_operation(15, 6, lambda x,y: x ** y))   # 15^6 = 11390625