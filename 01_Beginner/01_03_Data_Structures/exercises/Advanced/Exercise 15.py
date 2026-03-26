# Write function that opens file, handles FileNotFoundError and PermissionError differently.

# Exercise 15 - Specific exception handling
def read_important_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        print("First 60 characters:")
        print(content[:60] + "..." if len(content) > 60 else content)
        return True
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return False
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        return False
    except Exception as e:
        print(f"Unexpected error while reading '{filename}': {type(e).__name__}")
        return False
    finally:
        print("→ File operation attempt finished.\n")
# Test calls
read_important_file("config.txt")
read_important_file("secret.txt")      # probably not found
# read_important_file("/root/secret")  # would trigger PermissionError on most systems