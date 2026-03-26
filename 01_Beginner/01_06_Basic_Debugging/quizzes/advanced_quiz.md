# Advanced Quiz - Basic Debugging
1. What does `traceback.print_exc()` do?
2. When should you use `assert` vs `if` + `raise`?
3. Explain the "read traceback from bottom to top" rule.
4. What is a debugging wrapper function?
**Answers**:
1. Prints full traceback when exception occurs
2. assert for development/debugging, raise for production error handling
3. The root cause is usually the last line shown
4. A decorator/function that logs entry, arguments, and exit of another function