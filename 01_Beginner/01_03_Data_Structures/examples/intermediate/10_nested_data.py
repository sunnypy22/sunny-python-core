# 10_nested_data.py
# List of dictionaries
classroom = [
    {"name": "Sunny", "marks": [85, 92, 88], "city": "Pune"},
    {"name": "Priya", "marks": [78, 81, 95], "city": "Mumbai"},
    {"name": "Rahul", "marks": [90, 87, 84], "city": "Delhi"}
]
# Average marks per student
for student in classroom:
    avg = sum(student["marks"]) / len(student["marks"])
    print(f"{student['name']} (from {student['city']}): avg = {avg:.1f}")
# Nested list (matrix)
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
print("\nMatrix diagonal:")
for i in range(3):
    print(matrix[i][i])