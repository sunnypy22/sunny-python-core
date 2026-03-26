# 04_formatting.py
name = "Sunny"
age = 25
city = "Pune"
# f-string (Recommended)
print(f"My name is {name}, I am {age} years old, from {city}.")
# .format() method
print("My name is {}, I am {} years old.".format(name, age))
# Old style %
print("Name: %s, Age: %d" % (name, age))