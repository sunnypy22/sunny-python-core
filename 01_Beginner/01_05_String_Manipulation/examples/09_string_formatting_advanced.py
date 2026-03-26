# 09_string_formatting_advanced.py
data = [
    ("Sunny", 25, 92.5),
    ("Priya", 22, 88.0),
    ("Rahul", 28, 95.75)
]
print("Student Report".center(40, "="))
for name, age, score in data:
    print(f"Name: {name:<8} Age: {age:2} Score: {score:6.2f}")