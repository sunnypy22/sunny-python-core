# Create list of dictionaries: each dict = {"name":…, "score":…}. Print names of those with score > 80.

# Exercise 10 - List of dictionaries + filtering
students = [
    {"name": "Sunny", "score": 92},
    {"name": "Rahul", "score": 78},
    {"name": "Priya", "score": 88},
    {"name": "Aarav", "score": 65},
    {"name": "Neha", "score": 95}
]
print("Students who scored > 80:")
for student in students:
    if student["score"] > 80:
        print(f"  {student['name']:8} - {student['score']}%")
# Output:
# Students who scored > 80:
#   Sunny    - 92%
#   Priya    - 88%
#   Neha     - 95%