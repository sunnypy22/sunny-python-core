
# 10_name_main_demo.py
def greet(name):
    return f"Hello, {name}!"
def main():
    print(greet("Sunny"))
    print("This runs only when file is executed directly")
# This is the key line
if __name__ == "__main__":
    main()
    print("__name__ is currently:", __name__)
else:
    print("This module was imported")