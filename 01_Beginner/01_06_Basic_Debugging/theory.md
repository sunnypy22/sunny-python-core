theory.md
# Basic Debugging in Python
**Definition**: Debugging is the process of finding and fixing errors (bugs) in your code. Python provides several built-in tools and techniques to make debugging easier and more efficient.
## 1. Types of Errors
| Error Type          | Description                                      | Example |
|---------------------|--------------------------------------------------|--------|
| SyntaxError         | Code violates Python syntax rules                | Missing `:` or `)` |
| NameError           | Using a variable that hasn't been defined        | `print(x)` before defining x |
| TypeError           | Operation on incompatible types                  | `"2" + 3` |
| ValueError          | Correct type but invalid value                   | `int("abc")` |
| IndexError          | Accessing list/tuple index that doesn't exist    | `lst[10]` when len=5 |
| KeyError            | Accessing missing key in dictionary              | `d["missing"]` |
| ZeroDivisionError   | Division by zero                                 | `10 / 0` |
| FileNotFoundError   | Trying to open a file that doesn't exist         | `open("missing.txt")` |
## 2. Basic Debugging Techniques
### 1. Print Debugging (Most Common for Beginners)
```python
print("Variable x =", x)
print(f"After calculation: {result}")
```
### 2. Using assert Statements
```python
assert age >= 0, "Age cannot be negative"
```
### 3. The pdb Debugger (Python Debugger)
```python
import pdb
pdb.set_trace()   # Sets a breakpoint
```
### 4. Common Debugging Commands in pdb
n → next line
c → continue
l → list code
p variable → print variable
q → quit
## 3. Good Debugging Practices
Read the full error message and traceback carefully
Use meaningful variable names
Test small parts of code first
Add comments explaining complex logic
Use try-except blocks wisely (don't hide errors)
Write small functions that do one thing
## 4. Preventive Debugging (Best Practice)
```Python
# Good practice
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```
**Pro Tip: Always read the traceback from bottom to top — the actual error is usually at the bottom.**

