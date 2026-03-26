# 02_string_methods.py
text = "   Hello Python World!   "
print("Stripped:", text.strip())
print("Left stripped:", text.lstrip())
print("Right stripped:", text.rstrip())
print("Starts with 'Hello':", text.strip().startswith("Hello"))
print("Ends with 'World!':", text.strip().endswith("World!"))
print("Count of 'o':", text.count("o"))
print("Find 'Python':", text.find("Python"))