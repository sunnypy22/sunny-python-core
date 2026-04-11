
# Pure Python way (no pandas)
import csv
from collections import defaultdict
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)
# Group by city
city_group = defaultdict(list)
for row in data:
    city_group[row["City"]].append(row)
print("Students per city:")
for city, students in city_group.items():
    print(f"{city}: {len(students)} students")