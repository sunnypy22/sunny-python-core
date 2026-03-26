# Ask user for two numbers. Use try-except to handle division by zero and invalid input.
# Exercise 9 - Basic try-except for division

print("Enter two numbers to divide:")
try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
   
    result = a / b
    print(f"{a} ÷ {b} = {result:.4f}")
   
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"Unexpected error: {e}")
print("Program finished.")