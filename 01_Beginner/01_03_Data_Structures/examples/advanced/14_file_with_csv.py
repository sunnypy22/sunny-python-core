# 14_file_with_csv.py
# Simple CSV-like handling (no csv module for clarity)
data = [
    "name,age,city",
    "Sunny,25,Pune",
    "Priya,22,Mumbai",
    "Rahul,28,Delhi"
]
# Write
with open("students.csv", "w") as f:
    f.write("\n".join(data))
# Read and process
print("\nReading CSV-like file:")
total_age = 0
count = 0
with open("students.csv", "r") as f:
    lines = f.readlines()
    header = lines[0].strip().split(",")
    print("Columns:", header)
    for line in lines[1:]:
        row = line.strip().split(",")
        name, age_str, city = row
        try:
            age = int(age_str)
            total_age += age
            count += 1
            print(f"{name:8} {age:3}  {city}")
        except ValueError:
            print(f"Invalid age in row: {line.strip()}")
if count > 0:
    print(f"\nAverage age: {total_age / count:.1f}")