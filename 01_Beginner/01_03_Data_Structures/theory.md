## 1. Data Structure : List, Tuple, Set, Dictionaries, Input/Output, Reading from stdin, writing to files, basic error handling with try-except

# Data Structures + Input/Output + Basic Error Handling

## 1. List

Ordered, mutable, allows duplicates

```python
lst = [10, "hello", 3.14, True, 10]     # duplicates ok
lst.append(99)
lst[1] = "world"                        # mutable
print(lst[-1])      
```                    

**Common methods: append, extend, insert, pop, remove, clear, index, count, sort, reverse**
**Slicing: lst[1:4], lst[::-1] (reverse)**

## 2. Tuple

Ordered, immutable, allows duplicates

```python
t = (5, "python", 5)          # parentheses optional in many cases
a, b = 10, 20                 # tuple unpacking
single = (42,)                # comma needed for 1-element tuple
```

**Use when: data should not change, as dictionary keys, returning multiple values**

## 3. Set
Unordered, mutable, no duplicates, hashable elements only

```python
s = {1, 2, 3, 2}              # → {1,2,3}
s.add(4)
s.remove(2)                   # KeyError if missing
s.discard(99)                 # no error if missing
# Operations
a = {1,2,3,4}
b = {3,4,5,6}
print(a | b)     # union
print(a & b)     # intersection
print(a - b)     # difference
print(a ^ b)     # symmetric difference
```

## 4. Dictionary

Unordered (insertion order since 3.7), mutable, key-value pairs, unique keys

```Python
d = {"name": "Sunny", "age": 25, "city": "Pune"}
d["job"] = "Student"          # add / update
print(d.get("age"))           # safe access
print(d.get("salary", 0))     # default if missing
for k in d:                   # keys
for v in d.values():
for k,v in d.items():
```

## 5. Input / Output

**Reading from stdin**

```python
name = input("Enter name: ")          # always returns str
age = int(input("Age: "))             # type conversion needed
```
**Writing to files**


```Python
# Write
with open("data.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
# Append
with open("data.txt", "a") as f:
    f.write("New line\n")
# Read
with open("data.txt", "r") as f:
    content = f.read()                # whole file
    lines = f.readlines()             # list of lines
```

## 6. Basic Error Handling – try / except

```python
try:
    x = int(input("Number: "))
    result = 100 / x
except ValueError:
    print("Please enter a valid integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:          # catch-all (not recommended as first choice)
    print(f"Unexpected error: {e}")
else:
    print("Calculation successful:", result)
finally:
    print("This always runs")
```

**Common exceptions: ValueError, TypeError, ZeroDivisionError, IndexError, KeyError, FileNotFoundError**
