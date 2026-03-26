# String Manipulation in Python
**Definition**: String manipulation refers to the various operations performed on strings to modify, analyze, format, or extract information from them. In Python, strings are **immutable** sequences of Unicode characters.
## 1. Basic String Operations
```python
s = "Hello Python"
# Concatenation
greeting = "Hello" + " " + "Sunny"
# Repetition
repeat = "Python " * 3
# Length
print(len(s))
# Indexing & Slicing
print(s[0])           # H
print(s[-1])          # n
print(s[0:5])         # Hello
print(s[::-1])        # reverse
```
## 2. String Methods (Most Important)
Category,                   Methods,                                                Description
Case Conversion,            "upper(), lower(), title(), capitalize()",              Change case
Stripping,                  "strip(), lstrip(), rstrip()",                          Remove whitespace
Searching,                  "find(), index(), count(), startswith(), endswith()",   Search
Replacing,                  replace(),                                              Replace substring
Splitting & Joining,        "split(), splitlines(), join()",                        Split & combine
Checking,                   "isalpha(), isdigit(), isalnum(), isspace()",           Validation
Formatting,                 "format(), f-strings",                                  String formatting
## 3. String Formatting
```python
# Old style
print("My name is %s and I am %d years old." % ("Sunny", 25))
# .format()
print("My name is {} and I am {} years old.".format("Sunny", 25))
# f-strings (Python 3.6+) - Recommended
name = "Sunny"
age = 25
print(f"My name is {name} and I am {age} years old.")
```
## 4. Immutability of Strings
```python
s = "hello"
# s[0] = "H"          # TypeError: 'str' object does not support item assignment
# Correct way - create new string
s = s.capitalize()     # "Hello"
```
## 5. Escape Sequences & Raw Strings
```python
print("He said \"Hello\"")     # \"
print('Path: C:\\Users\\Sunny')
print("First line\nSecond line")
# Raw string
print(r"C:\Users\Sunny\Documents")   # ignores escape sequences
```
## 6. Common String Algorithms
Palindrome check
Reversing string
Counting characters
Removing duplicates
Anagram checking