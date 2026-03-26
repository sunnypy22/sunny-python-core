## 1. Modules and Packages : INport standard libraries (i.e. math, random) , understanding __init__.py

# Modules and Packages in Python

**Definition**:
- A **module** is a single Python file (.py) containing functions, classes, and variables.
- A **package** is a collection of modules organized in a directory with a special `__init__.py` file.
**Modules and packages help organize code, promote reusability, and avoid naming conflicts.**

## 1. Importing Modules
### Basic import syntax
```python
import math                    # import entire module
import random
from math import sqrt, pi      # import specific items
from random import randint     # import specific function
import math as m               # alias (short name)
from math import *             # import everything (not recommended)
```

### Using imported modules
```python
print(math.sqrt(16))           # 4.0
print(math.pi)                 # 3.14159...
print(random.randint(1, 100))  # random integer between 1 and 100
```

## 2. Standard Library Modules (Most Useful)

Module,         Purpose,                            Common Functions / Usage
math,           Mathematical operations,            "sqrt, pow, sin, cos, floor, ceil, pi, e"
random,         Generate random numbers,            "randint, random, choice, shuffle"
os,             Operating system interaction,       "getcwd, listdir, mkdir, path"
sys,            System-specific parameters,         "argv, path, exit"
datetime,       Date and time handling,             "datetime, date, timedelta"
json,           JSON encoding/decoding,             "dumps, loads"
collections,    Specialized container datatypes,    "Counter, defaultdict, namedtuple"


## 3. Understanding Packages and __init__.py

**A package is a folder containing __init__.py**
**__init__.py makes the folder a Python package**
**It can be empty or contain initialization code, variable definitions, or __all__ list**

### Package Structure Example
myproject/
├── __init__.py          # Makes 'myproject' a package
├── math_utils.py
├── string_utils.py
└── utils/
    ├── __init__.py
    └── helper.py
**In __init__.py you can do:**

# __init__.py
from .math_utils import add, multiply
from .string_utils import reverse
__all__ = ['add', 'multiply', 'reverse']
This allows users to do: from myproject import add
## 4. Relative vs Absolute Imports
```python
# Absolute import
import math
from package.module import func
# Relative import (inside package)
from . import module
from ..parent import func
```

## 5. Best Practices
Use import module or from module import specific_name
Avoid from module import *
Use meaningful aliases (import pandas as pd)
Keep __init__.py clean
Use virtual environments for third-party packages
**name == "main" trick (very important):**
```Python
# In any module
if __name__ == "__main__":
    print("This code runs only when file is executed directly")
```
