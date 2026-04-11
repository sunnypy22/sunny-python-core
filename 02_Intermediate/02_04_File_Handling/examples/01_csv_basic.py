# 01_csv_basic.py
import csv
# Writing CSV
data = [
    ["Name", "Age", "City", "Score"],
    ["Sunny", 25, "Pune", 92],
    ["Priya", 22, "Mumbai", 88],
    ["Rahul", 28, "Delhi", 95]
]
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
print("CSV file written successfully!")

