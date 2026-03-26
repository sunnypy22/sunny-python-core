# Intermediate Quiz - Modules and Packages

1. What is the difference between `import math` and `from math import pi`?
2. What does `__name__ == "__main__"` check?
3. Which module would you use to work with dates and times?
4. What happens if you use `from module import *`? (pros and cons)
5. How do you make certain functions available when someone does `from mypackage import *`?

**Answers**:
1. First imports whole module, second imports only pi
2. Checks if the file is run directly or imported
3. datetime module
4. Imports everything — convenient but pollutes namespace (not recommended)
5. Define `__all__ = ['func1', 'func2']` in __init__.py