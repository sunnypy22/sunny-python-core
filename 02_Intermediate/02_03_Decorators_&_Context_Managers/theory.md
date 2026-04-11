# Decorators and Context Managers in Python
## 1. Decorators
**Definition**: A decorator is a function that takes another function (or class) as input and returns a new function (or class) that usually extends or modifies the behavior of the original one.
Decorators allow you to add functionality **without changing the original code** — following the **Open-Closed Principle**.
### Basic Syntax
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Code before original function
        result = func(*args, **kwargs)
        # Code after original function
        return result
    return wrapper
@decorator          # This is syntactic sugar
def my_function():
    pass
```
**Common Use Cases**
Logging
Timing functions
Authentication / Authorization
Caching
Validation
**Preserving Metadata with functools.wraps**
```python
from functools import wraps
def my_decorator(func):
    @wraps(func)          # Important!
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper
```
## 2. Context Managers (with statement)
**Definition**: Context managers manage resources (files, database connections, locks, etc.) so they are automatically cleaned up after use.
The with statement makes resource management clean and safe.
### Basic Usage
```python
with open("file.txt", "r") as f:
    data = f.read()          # file is automatically closed
```
### How Context Managers Work
A context manager must implement two methods:
__enter__() — called when entering the with block
__exit__() — called when exiting the with block (even if an error occurs)
### Using @contextmanager Decorator (Recommended)
```python
from contextlib import contextmanager
@contextmanager
def my_context():
    # Code before 'with' block
    print("Entering context")
    try:
        yield          # Code inside 'with' block runs here
    finally:
        # Cleanup code
        print("Exiting context")
```