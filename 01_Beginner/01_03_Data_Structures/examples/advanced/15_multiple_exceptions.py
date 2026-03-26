# 15_multiple_exceptions.py
import os
filename = "important.txt"
try:
    with open(filename, "r") as f:
        content = f.read()
    print("First 50 chars:", content[:50])
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except PermissionError:
    print(f"Error: No permission to read '{filename}'.")
except Exception as e:
    print(f"Unexpected error: {type(e).__name__} - {e}")
else:
    print("File read successfully.")
finally:
    print("Cleanup / logging would go here.")
