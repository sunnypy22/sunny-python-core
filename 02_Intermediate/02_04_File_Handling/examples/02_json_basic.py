
import json
student = {
    "id": 101,
    "name": "Sunny",
    "age": 25,
    "skills": ["Python", "SQL", "Machine Learning"],
    "is_active": True,
    "address": {
        "city": "Pune",
        "pincode": 411001
    }
}
with open("student.json", "w") as f:
    json.dump(student, f, indent=4)
print("JSON file created!")