# Basic Syntax: Variables, Data Types & Operators

## 1. Variables in Python

**Definition** A variable is a symbolic name (identifier) that refers to a value or object stored in memory. In Python, variables are dynamically typed — you do not need to declare the type when creating them. The type is determined at runtime based on the value assigned. Python follows the principle "everything is an object," so a variable is actually a reference (pointer) to an object in memory.

### Beginner Level

**Creating a variable**: Just assign a value with =.Python

name = "Sunny"      # string
age = 25            # integer
height = 5.9        # float
is_student = True   # boolean

**Rules for naming**:

Must start with a letter (a-z, A-Z) or underscore _.
Can contain letters, digits (0-9), and underscores.
Case-sensitive: Age and age are different.
Cannot be a Python keyword (if, for, def, class, etc.).

**Reassignment**: You can change the value (and even the type) anytime.Python
x = 10
x = "Hello"   # type changed from int to str

**Printing**: Use print(variable)
print(f"My name is {name} and I am {age} years old.")


### Intermediate Level

**Multiple assignment**
a, b, c = 1, 2, 3
x = y = z = 0   # all point to the same object

**Unpacking**
coordinates = (10, 20)
x, y = coordinates

**Scope**
*Local*: Inside a function.
*Global*: Outside functions (use global keyword to modify inside function).
*Nonlocal* (Python 3+): For nested functions.

**Deleting**
del variable removes the reference (object may be garbage-collected if no other references exist).


### Advanced Level

**Memory & References**: Variables hold references, not values. Use id() to see memory address.Python
a = 256
b = 256
print(id(a) == id(b))  # True (small integers are cached)

**Mutability matters**
*Immutable objects (int, float, str, tuple, frozenset):* Changing value creates a new object.
*Mutable objects (list, dict, set):* Can be changed in place.

**Garbage Collection**: Python uses reference counting + cyclic garbage collector (module gc).

**Type Hints**
age: int = 25
name: str = "Sunny"

**Variable Annotations (PEP 526) and typing module for complex types**:
from typing import List, Dict
scores: List[int] = [95, 87]
data: Dict[str, int] = {"age": 25}

**Walrus Operator (:=) — assignment expression (Python 3.8+)**:
if (n := len("Python")) > 5:
    print(f"Length {n} is greater than 5")

## 2. Data Types in Python

**Definition**: Data types classify the type of data a variable can hold and define the operations allowed on it. Python has built-in (primitive) types and container types. All are objects with their own methods and attributes.

### Beginner Level (Core Built-in Types)
Category,   Type,       Example,                  Mutable?,       Description
Numeric,    int,        "42, -100, 10**100",      No,             Arbitrary precision integers
Numeric,    float,      "3.14, 1e10",             No,             Floating-point numbers
Numeric,    complex,     3 + 4j,                  No,             Real + imaginary part
Text,       str,        """Hello"" or 'World'",   No,             Unicode strings
Boolean,    bool,       "True, False",            No,             "Subclass of int (True=1, False=0)"
None,       NoneType,   None,                     -,              Represents absence of value

**Type checking:**
print(type(42))          # <class 'int'>
print(isinstance(42, int))  # True

### Intermediate Level

**Sequence Types:**
list (mutable): [1, 2, 3]
tuple (immutable): (1, 2, 3)
range: range(1, 10)

**Mapping**
dict (mutable): {"name": "Sunny", "age": 25}

**Set Types**
set (mutable): {1, 2, 3}
frozenset (immutable)

**Binary Types**
bytes, bytearray, memoryview

**Type Conversion (casting)**
int("100")      # 100
str(100)        # "100"
list("abc")     # ['a', 'b', 'c']
tuple([1,2,3])  # (1, 2, 3)

**Common Methods:**
*Strings:* .upper(), .split(), .format(), f-strings.
*Lists:* .append(), .extend(), .pop(), .sort().
*Dicts:* .keys(), .values(), .get(), .update()


### Advanced Level

**Mutable vs Immutable Deep Dive:**

*Immutable types are hashable → can be dict keys or set elements.

**Example of unexpected behavior:Pythona = [1, 2]*

b = a          # b references same list
b.append(3)
print(a)       # [1, 2, 3] ← changed!

**Custom Data Types (Classes):**

class Person:
    def __init__(self, name: str):
        self.name = name

**Abstract Base Classes (from collections.abc):** For duck typing checks.

**TypedDict, NamedTuple, dataclass (Python 3.7+):**

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

**Generics (Python 3.9+ typing):**from typing import TypeVarT = TypeVar('T')

**Protocol** (structural subtyping) and runtime_checkable.

**Special Types:** Any, Union, Optional, Literal, Final (from typing).

## 3. Operators in Python

**Definition:** Operators are special symbols or keywords that perform computations or comparisons on operands (variables/values). Python supports unary, binary, and ternary operators.

### Beginner Level

**Arithmetic Operators:**
+  # addition
-  # subtraction
*  # multiplication
/  # division (float result)
** # exponent (2**3 = 8)
%  # modulo (remainder)

**Comparison:**
==  !=  >  <  >=  <=

**Logical**
and  or  not

**Assignment (basic):**
=   +=   -=   *=   /=   %=   **=

### Intermediate Level

**Full Operator Categories:**
Category,          Operators,                    Example / Note
Arithmetic,        + - * / // % **,              // = floor division (5//2 = 2)
Assignment,        = += -= *= /= //= %= **=,     Compound assignment
Comparison,        == != > < >= <=,              Returns bool
Logical,           and or not,                   Short-circuit evaluation
Bitwise,           & | ^ ~ << >>,                Works on integers
Identity,          is is not,                    Checks same object (id())
Membership,        in not in,                    Works on sequences/sets
Walrus,            := (3.8+),                    Assignment expression

**Operator Precedence (highest to lowest):**
** → unary + - ~ → * / // % → + - → << >> → & → ^ → \| → comparisons → not → and → or
Use parentheses () to override.

**Short-Circuiting:**
False and expensive_function()  # expensive_function never called

### Advanced Level

**Operator Overloading (Dunder methods):**

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):        # +
        return Vector(self.x + other.x, self.y + other.y)    
    def __mul__(self, scalar):       # *        
        return Vector(self.x * scalar, self.y * scalar)    
    def __eq__(self, other):         # ==        
        return self.x == other.x and self.y == other.y
        
**Matrix Multiplication (@ operator, Python 3.5+):**

import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A @ B)   # matrix product

**Rich Comparisons (for sorting/custom objects):**

__lt__, __le__, __gt__, __ge__, __eq__, __ne__.

**Augmented Assignment** under the hood calls __iadd__, __imul__, etc.

**Operator Module (operator stdlib):**from operator import add, mulprint(add(5, 3))   # 8

**Ternary Operator (conditional expression)**status = "Adult" if age >= 18 else "Minor"

**Chained Comparisons**
if 1 < x < 10:   # equivalent to 1 < x and x < 10

## 4. Control Structures in Python [ if-else, for loop, while loop, break, continue, pass, else clauses ]

### A. Conditional Statements (if / elif / else)

**Purpose**: Execute different blocks of code depending on whether a condition is True or False.
**Basic syntax**

```python
if condition:
    # code runs if condition is True
elif another_condition:      # optional, can have multiple
    # code runs if previous conditions were False and this one is True
else:                        # optional
    # code runs if all previous conditions were False
```


**Important notes**
Conditions are evaluated from top to bottom → first True block runs, others are skipped
elif is short for "else if"
You can have zero or more elif clauses
else is optional

**One-liner / Ternary conditional expression**

**ex1**
status = "Adult" if age >= 18 else "Minor"
print(status)

**ex2**
total = 0
discount = 0.2 if total > 1000 else 0.1

## Truthy / Falsy values in conditions
**Falsy values → considered False**
if not 0:           # True (because not False)
if not "":          # True
if not []:          # True
if not None:        # True

# Everything else → Truthy
if "hello":         # True
if 42:              # True
if [1,2]:           # True


### B. for Loop

**Purpose:** Iterate over a sequence (list, tuple, string, range, dictionary keys/values/items, etc.)

**Basic syntax**
for item in sequence:
    # code block executed for each item

### C. while Loop

**Purpose**: Repeat code as long as a condition is True

**Basic syntax**
while condition:
    # code block
    # IMPORTANT: must eventually make condition False

## Infinite loop (intentional or bug)

# Dangerous if you forget to break
while True:
    print("This runs forever...")
    # unless you have break

### D. Loop Control Statements

**break**

**Immediately exits the nearest enclosing loop**
for i in range(1, 11):
    if i == 7:
        break
    print(i)        # prints 1 2 3 4 5 6

**continue**

**Skips the rest of the current iteration and moves to the next one**
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)        # prints only odd numbers: 1 3 5 7 9

**pass**

**Does nothing — placeholder when a statement is syntactically required**
def future_function():
    pass                # TODO: implement later
if x < 0:
    pass                # do nothing for negative values
else:
    print("Positive")

### E. else Clause on Loops (less known, very useful)

**The else block runs only if the loop completed normally (i.e. no break was hit)**

**for ... else**
numbers = [4, 8, 15, 16, 23, 42]
for num in numbers:
    if num % 2 != 0:
        print("Found odd number:", num)
        break
else:
    print("All numbers were even")

**while ... else**
attempts = 3
while attempts > 0:
    pin = input("Enter PIN: ")
    if pin == "2580":
        print("Correct!")
        break
    attempts -= 1
    print(f"Wrong. {attempts} attempts left.")
else:
    print("Account locked after 3 failed attempts.")

### F. Quick Comparison Table

Feature,            for loop,                               while loop
Best for,           Known number of iterations,             Condition-based (unknown count)
Typical use,        "sequences, range(), files, dicts",     "user input, games, waiting"
Risk,               Usually safe,                           Easy to create infinite loop
Has else clause,    Yes,                                    Yes
Initialization,     Automatic (item in sequence),           Manual before loop
## Summary – When to use what

Use if / elif / else → decisions, branching
Use for → you know what you're iterating over (lists, strings, range, files…)
Use while → you need to repeat until a condition changes (input validation, games, sensors…)
Use break → found what you were looking for → stop early
Use continue → skip this item, go to next
Use else on loop → "no break occurred" logic (search not found, no error occurred, etc.)