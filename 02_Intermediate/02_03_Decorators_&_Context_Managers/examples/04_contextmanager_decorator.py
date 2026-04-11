
from contextlib import contextmanager
@contextmanager
def database_connection():
    print("Connecting to database...")
    # Simulate connection
    try:
        yield "Connected"
    finally:
        print("Closing database connection...")
with database_connection() as conn:
    print("Using connection:", conn)
# 05_class_decorator.py
class LogCalls:
    def __init__(self, func):
        self.func = func
   
    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__} with {args}, {kwargs}")
        return self.func(*args, **kwargs)
@LogCalls
def add(a, b):
    return a + b
print(add(5, 7))
