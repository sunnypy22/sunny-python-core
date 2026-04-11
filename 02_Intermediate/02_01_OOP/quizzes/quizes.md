# Advanced Quiz - Classes and Objects

1. What is the purpose of the `@property` decorator?

2. Explain the difference between `__str__` and `__repr__` magic methods.

3. What is name mangling? Why does Python use it?

4. When should you use a static method (`@staticmethod`) instead of instance or class method?

5. What is the recommended way to control access to an attribute in modern Python? Why is it better than traditional getter/setter methods?

**Answers**:
1. To create managed attributes that look like normal attributes but have getter/setter logic behind them.

2. `__str__` is for user-friendly string representation (used by print()). `__repr__` is for unambiguous developer representation (used by repr() and debugging).

3. Name mangling renames `__var` to `_ClassName__var` to prevent accidental overriding in subclasses and to signal strong internal use only.

4. When the method doesn't need access to instance (`self`) or class (`cls`) data — it's a utility function related to the class.

5. Using `@property` and `@attribute.setter`. It is better because it provides clean syntax (`obj.attr = value`) while allowing validation and encapsulation.



# Beginner Quiz - Classes and Objects

1. What is a class in Python?
   a) A function  
   b) A blueprint for creating objects  
   c) A variable  
   d) A loop

2. What is the purpose of the `__init__` method?
   a) To print something  
   b) To initialize object attributes when object is created  
   c) To delete an object  
   d) To import modules

3. What does the `self` keyword represent?
   a) The class itself  
   b) The current instance of the class  
   c) A global variable  
   d) A static method

4. Which of the following is a class attribute?
   a) self.name  
   b) name  
   c) species = "Human" (defined inside class)  
   d) __init__

5. How do you create an object from a class?
   a) Person()  
   b) new Person()  
   c) create Person()  
   d) Person.create()

**Answers**:
1. b  
2. b  
3. b  
4. c  
5. a


# Quick Conceptual Quiz - Classes and Objects

1. True or False: In Python, you must declare attributes before using them in `__init__`.

2. What happens when you create an object? (e.g., `p = Person()`)

3. Can you have multiple `__init__` methods in one class? Why or why not?

4. What is the difference between `self.name` and `Person.name`?

5. How do you make an attribute "private" in Python?

**Answers**:
1. False - Python is dynamic. You can create attributes on the fly.
2. `__init__` method is automatically called.
3. No. Python doesn't support method overloading by default.
4. `self.name` is instance attribute. `Person.name` would be class attribute.
5. By prefixing with double underscore `__name` (name mangling).

