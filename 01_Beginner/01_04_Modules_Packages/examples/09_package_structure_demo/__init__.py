
# 09_package_structure_demo/__init__.py
# This makes the folder a package
from .math_utils import add, multiply
from .string_utils import reverse_string
__all__ = ['add', 'multiply', 'reverse_string']
print("my_utils package initialized")
# 09_package_structure_demo/math_utils.py
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def power(base, exp):
    return base ** exp