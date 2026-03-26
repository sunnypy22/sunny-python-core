# 05_input_output.py

name = input("Enter your name: ")
age = input("Enter your age: ")
try:
    age_int = int(age)
    print(f"Hello {name.title()}, you will be {age_int + 1} next year!")
except ValueError:
    print("Age must be a number!")

# Simple file write
with open("greeting.txt", "w") as file:
    file.write(f"Welcome {name}!\n")
    file.write(f"Recorded age: {age}\n")
print("Data saved to greeting.txt")