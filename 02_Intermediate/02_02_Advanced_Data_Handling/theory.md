# List/Dict Comprehensions, Generators & Iterators
**Definition**: These are powerful Python features for creating sequences efficiently and working with iterable data in a clean, Pythonic way.

## 1. List Comprehensions
**Syntax**: `[expression for item in iterable if condition]`
```python
# Basic

squares = [x**2 for x in range(10)]
# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Nested
matrix = [[1,2,3], [4,5,6]]
flat = [num for row in matrix for num in row]
```
## 2. Dictionary & Set Comprehensions
# Dict comprehension
squares_dict = {x: x**2 for x in range(6)}
# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# Set comprehension (removes duplicates automatically)
unique = {x for x in [1,2,2,3,3,4]}

## 3. Generators
Generator Expressions (lazy version of list comprehensions):
```python
gen = (x**2 for x in range(10))   # Returns a generator object
```
**Generator Functions (using yield):**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

## 4. Iterators vs Iterables
Iterable: Any object that can be looped over (list, tuple, str, etc.) → has __iter__()
Iterator: Object that produces values one at a time → has __iter__() and __next__()
```python
# Manual iterator
nums = [10, 20, 30]
it = iter(nums)
print(next(it))   # 10
print(next(it))   # 20
```
**Key Advantage**: Generators and iterators are lazy — they generate values only when needed (memory efficient).

## 5. When to Use What?
Feature,                        Use Case,                                   Memory Usage
List Comprehension,             Small to medium data,                       High
Dict/Set Comprehension,         Creating mappings or unique sets,           High
Generator Expression,           Large data / infinite sequences,            Very Low
Generator Function,             "Complex logic, streaming, pipelines",      Very Low
Iterator,                       Custom iteration behavior,                  Low


**Best Practice:**

Use comprehensions for simple transformations
Use generators when working with large or infinite data
Prefer yield over returning large lists