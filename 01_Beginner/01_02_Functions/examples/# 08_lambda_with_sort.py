# Using lambda as sorting key
students = [
    ("Rahul", 22, 85),
    ("Priya", 19, 92),
    ("Sunny", 25, 78),
    ("Aarav", 21, 88)
]
# Sort by age
sorted_by_age = sorted(students, key=lambda student: student[1])
print("Sorted by age:")
for s in sorted_by_age:
    print(s)
print("\nSorted by marks (descending):")
sorted_by_marks_desc = sorted(students, key=lambda s: s[2], reverse=True)
for s in sorted_by_marks_desc:
    print(s)