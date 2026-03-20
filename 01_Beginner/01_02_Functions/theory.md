## Functions : Defining functions, parameteres, return values and lambda functions

# 1. Functions in Python

**Definition**: A function is a reusable block of code that performs a specific task. Functions help organize code, avoid repetition, and make programs easier to read, test, and maintain.

## 1. Defining and Calling Functions
### Basic syntax (beginner)

```python
def function_name():
    # code block (indented)
    print("Hello from function!")
```

# Calling / invoking the function

function_name()

**Rules:**
def keyword
Function name follows variable naming rules
Parentheses () are mandatory
Colon : after name
Indented body (4 spaces)

# 2. Parameters and Arguments

**Parameters (in definition)**

def greet(name):           # name → parameter
    print(f"Hello, {name}!")

**Arguments (when calling)**
greet("Sunny")             # "Sunny" → argument

**Types of parameters**

Type,                    Syntax,                        Example call,                      Notes
Positional,              "def add(a, b):",              "add(5, 3)",                       Order matters
Keyword,                 "def info(name, age):",        "info(age=25, name=""Sunny"")",    Order doesn't matter
Default,                 "def greet(name=""Guest""):",  "greet() or greet(""Sunny"")",     Optional
*args (variable pos.),   def sum_all(*numbers):,        "sum_all(1,2,3,4)",                Tuple
**kwargs (variable kw),  def show(**info):,             "show(city=""Pune"", age=25)",     Dictionary


## 3. Return Values
def square(x):
    return x * x           # exits function + sends value back
result = square(7)         # result = 49

**return ends function execution**
**Without return → function returns None**
**Multiple returns possible (early exit)**

def check_even(n):
    if n % 2 == 0:
        return True
    return False           # else not needed


## 4. Scope – LEGB Rule (beginner → intermediate)
**LEGB = Local → Enclosing → Global → Built-in**
x = "global"
def outer():
    x = "enclosing"
   
    def inner():
        x = "local"
        print(x)           # local
   
    inner()
    print(x)               # enclosing
outer()
print(x)                   # global

**Use global x to modify global variable**
**Use nonlocal x in nested functions to modify enclosing scope**

## 5. Lambda Functions (anonymous functions)

# Normal function
def add(a, b):
    return a + b

# Same as lambda
add = lambda a, b: a + b

**Common uses:**
**Short throw-away functions**
**sort(), map(), filter(), sorted(key=...)**

points = [(3,4), (1,7), (5,2)]
points.sort(key=lambda p: p[1])   # sort by y-coordinate


# Quick Summary Table
Feature,                Beginner Example,                   Intermediate / Advanced Use-case
No parameters,          def hello():,                       Utility functions
Positional args,        "def add(a,b):",                    Most math/logic ops
Default params,         "def greet(name=""User""):",        Flexible APIs
*args,                  def total(*nums):,                  "Sum, join, min/max of any count"
**kwargs,               def config(**settings):,            "Configuration, forwarding"
Return,                 return result,                      Almost every meaningful function
Lambda,                 lambda x: x*2,                      "key functions, callbacks"
Scope modification,     —,                                  "global, nonlocal"

