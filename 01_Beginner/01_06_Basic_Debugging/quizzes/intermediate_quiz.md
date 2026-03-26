# Intermediate Quiz - Basic Debugging
1. What is `pdb.set_trace()` used for?
2. Name two common exceptions and when they occur.
3. What is the difference between `except Exception` and specific except blocks?
4. Why should we avoid bare `except:`?
**Answers**:
1. To set a breakpoint and start interactive debugging
2. ZeroDivisionError (divide by 0), ValueError (wrong value for type)
3. Specific is better - gives clear error handling
4. It hides all errors and makes debugging very difficult