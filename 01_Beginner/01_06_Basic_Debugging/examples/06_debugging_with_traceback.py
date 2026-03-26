# 06_debugging_with_traceback.py
import traceback
def deep_function():
    x = 10
    y = 0
    return x / y
def middle_function():
    return deep_function()
def main():
    try:
        middle_function()
    except Exception as e:
        print("=== ERROR OCCURRED ===")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {e}")
        print("\n=== FULL TRACEBACK ===")
        traceback.print_exc()
if __name__ == "__main__":
    main()