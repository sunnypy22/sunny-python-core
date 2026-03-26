# 09_try_except_basic.py

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"{num1} ÷ {num2} = {result}")
finally:
    print("Calculation attempt finished.")