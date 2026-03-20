# Simple lambda expressions
double = lambda x: x * 2
square = lambda x: x ** 2
add = lambda a, b: a + b
print(double(15))      # 30
print(square(7))       # 49
print(add(10, 25))     # 35
# Immediate usage (not stored in variable)
print((lambda x: x.upper())("python"))   # PYTHON