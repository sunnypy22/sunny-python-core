# Create a dictionary with 3 friends: name → age. Add one more, print all keys & values.
# Exercise 4 - Dictionary basics
friends = {
    "Rahul": 24,
    "Priya": 22,
    "Aarav": 26
}
# Add one more
friends["Neha"] = 23
# Print keys and values in nice format
print("My friends:")
for name, age in friends.items():
    print(f"  {name:8} → {age} years old")
# Or separately:
print("\nNames:", list(friends.keys()))
print("Ages :", list(friends.values()))
# Example output:
# My friends:
#   Rahul    → 24 years old
#   Priya    → 22 years old
#   Aarav    → 26 years old
#   Neha     → 23 years old