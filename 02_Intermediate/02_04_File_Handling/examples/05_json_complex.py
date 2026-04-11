
import json
with open("student.json", "r") as f:
    data = json.load(f)
print("Name:", data["name"])
print("Skills:", data["skills"])
print("City:", data["address"]["city"])
