# Exercise 1: Create 4 variables (name, age, city, is_student) and print them with f-string

# Exercise 2: Swap two variables without using a third variable

# Solution
name = "Sunny"
age = 25
city = "Pune"
is_student = True
print(f"Name: {name}, Age: {age}, City: {city}, Student: {is_student}")

# Swap without third variable
x, y = 10, 20
x, y = y, x
print(x, y)   # 20 10