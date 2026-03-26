# 04_dict_basic.py

student = {
    "name": "Sunny",
    "age": 25,
    "city": "Pune",
    "scores": [88, 92, 79]
}
# Access
print("Name:", student["name"])
print("Age:", student.get("age"))           # safe
print("Phone:", student.get("phone", "Not set"))
# Add / update
student["grade"] = "A"
student["age"] = 26

# Remove
del student["city"]
# Iteration
print("\nKeys:")
for key in student:
    print(key)
print("\nItems:")
for k, v in student.items():
    print(f"{k:>8} : {v}")