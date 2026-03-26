# Write names of 5 people to "names.txt", then read and print them.
# Exercise 8 - File write + read
people = ["Sunny", "Rahul", "Priya", "Aarav", "Neha"]
# Write to file
with open("names.txt", "w", encoding="utf-8") as f:
    for person in people:
        f.write(person + "\n")
# Read and display
print("Names from file:")
with open("names.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("→", line.strip())
# Output:
# Names from file:
# → Sunny
# → Rahul
# → Priya
# → Aarav
# → Neha