# 04_try_except_debugging.py
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Debug: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print(f"Error: Invalid types! Got {type(a)} and {type(b)}")
        return None
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__} - {e}")
        return None
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "2"))