# 01_simple_decorator.py
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper
@timer
def slow_function():
    import time
    time.sleep(1)
    print("Function finished")
slow_function()
