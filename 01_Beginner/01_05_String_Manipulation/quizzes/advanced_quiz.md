# Advanced Quiz - String Manipulation
1. Why are strings immutable in Python?
2. What is the time complexity of string concatenation in a loop using `+`?
3. Explain how f-strings are better than .format() and % formatting.
4. How would you reverse a string without using slicing `[::-1]`?
**Answers**:
1. For memory efficiency and hashability
2. O(n²) - very inefficient for large n
3. Faster, more readable, supports expressions
4. Use `''.join(reversed(s))` or loop with two pointers