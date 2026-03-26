#Common patterns – Beginner → Intermediate
# 1. Over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. Using range()
for i in range(5):          # 0,1,2,3,4
    print(i)
for i in range(2, 10, 2):   # 2,4,6,8
    print(i)

# 3. Over string
for char in "Python":
    print(char)

# 4. With index (common pattern)
for i, fruit in enumerate(fruits):
    print(i, fruit)

# 5. Over dictionary

# 1. Over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. Using range()
for i in range(5):          # 0,1,2,3,4
    print(i)
for i in range(2, 10, 2):   # 2,4,6,8
    print(i)

# 3. Over string
for char in "Python":
    print(char)

# 4. With index (common pattern)
for i, fruit in enumerate(fruits):
    print(i, fruit)

# 5. Over dictionary
person = {"name": "Sunny", "city": "Pune", "age": 25}
for key in person:
    print(key, "→", person[key])
for k, v in person.items():
    print(f"{k:>6} : {v}")