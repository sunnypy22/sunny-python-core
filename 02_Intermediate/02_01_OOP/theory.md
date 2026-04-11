# Object-Oriented Programming (OOP) in Python

**Definition**: OOP is a programming paradigm that uses **objects** and **classes** to organize code. It helps in modeling real-world entities and promotes code reusability, modularity, and maintainability.

Python supports all four major OOP principles:
- **Encapsulation**
- **Inheritance**
- **Polymorphism**
- **Abstraction**




## 1. Classes and Objects

**Definition**:
- A **class** is a blueprint or template for creating objects.
- An **object** is an instance of a class. It is a real entity that contains both data (attributes) and behavior (methods).

Python is an **object-oriented programming** language where almost everything is an object (even numbers, strings, functions, etc.).



```python
class Person:                    # Class definition
    def __init__(self, name, age):   # Constructor (Initializer)
        self.name = name             # Instance attributes
        self.age = age

    def introduce(self):             # Instance method        
    print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


# Creating objects (instances)
p1 = Person("Sunny", 25)
p1.introduce()
```

```python
class Person:                          # Class Definition
    """This is a Person class"""       # Docstring
   
    # Class Attribute (shared by all objects)
    species = "Homo sapiens"

       # Constructor / Initializer
    def __init__(self, name, age, city="Pune"):
        # Instance Attributes (unique to each object)
        self.name = name
        self.age = age
        self.city = city
        self.energy = 100
   # Instance Method    
   
   def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old from {self.city}.")
   
    def eat(self, food):
        self.energy += 10
        print(f"{self.name} ate {food}. Energy now: {self.energy}")
```



### Creating Objects (Instances):

```python
# Creating objects
p1 = Person("Sunny", 25)           # Using default city
p2 = Person("Priya", 22, "Mumbai")

p1.introduce()
p2.introduce()
p1.eat("pizza")
```



### Key Components

### a. __init__ Method (Constructor)

Automatically called when object is created
Used to initialize instance variables
self refers to the current object




### b. self Keyword

Represents the instance of the class
Must be the first parameter in every instance method
Allows access to instance attributes and methods


### c. Attributes

Instance Attributes: Unique to each object (self.name)
Class Attributes: Shared by all objects (species)


### d. Methods

Instance Methods: Operate on instance data (have self)
Class Methods: Operate on class data (@classmethod, use cls)
Static Methods: Utility methods (@staticmethod, no self or cls)


**Instance Variables vs Class Variables**
```python
class Student:
    school = "ABC School"           # Class variable (shared)
   
    def __init__(self, name):
        self.name = name            # Instance variable (unique per object)
```


###  Access Modifiers (Naming Conventions)

```python
class Student:
    def __init__(self):
        self.public_var = "Accessible anywhere"
        self._protected_var = "Should not be accessed directly (convention)"
        self.__private_var = "Name mangled - difficult to access"
```

###  Special (Magic/Dunder) Methods

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
   
    def __str__(self):
        return f"{self.title} ({self.pages} pages)"
   
    def __len__(self):
        return self.pages
```

###  Class vs Instance

Feature,            Class Attribute,                        Instance Attribute
Defined,            "Inside class, outside methods",        Inside __init__ using self
Shared,             Yes (all objects),                      No (unique per object)
Memory,             One copy,                               One copy per object
Example,            "species = ""Human""",                  "self.name = ""Sunny"""

###  Best Practices for Classes

Use meaningful class names (PascalCase: BankAccount)
Keep classes focused (Single Responsibility Principle)
Use type hints where possible
Write docstrings for class and methods
Validate data in __init__
Prefer composition over inheritance when appropriate

**Real-world Analogy:**

Class = Blueprint of a car
Object = Actual car built from that blueprint
Multiple objects can be created from one class



## 2. Inheritance

**Definition**: Inheritance is a core OOP principle that allows a new class (child/derived/subclass) to inherit attributes and methods from an existing class (parent/base/superclass). It promotes code reusability and establishes a hierarchical relationship between classes.

### Why Use Inheritance?
- Avoid code duplication
- Create logical class hierarchies
- Enable polymorphism
- Support the "is-a" relationship (e.g., Dog is an Animal)



### a. Basic Inheritance (Single Inheritance)

```python
class Animal:                    # Parent / Base class
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):               # Child / Derived class
    def bark(self):
        print(f"{self.name} says Woof Woof!")

    # Method Overriding
    def eat(self):
        print(f"{self.name} is eating bones.")
```

### b. Using super() – Calling Parent Methods

```python
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # Call parent constructor
        self.breed = breed
   
    def show_info(self):
        super().eat()                 # Call parent method
        print(f"Breed: {self.breed}")
```

### c. Types of Inheritance

Type,                      Description,                                           Syntax Example
Single Inheritance,        "One parent, one child",                               class Dog(Animal):
Multiple Inheritance,      "One child, multiple parents",                         "class Duck(Flyable, Swimmable):"
Multilevel Inheritance,    Chain of inheritance (Grandparent → Parent → Child),   class Puppy(Dog):
Hierarchical,              "One parent, multiple children",                       "Dog, Cat, Cow inherit from Animal"


### d. Method Overriding & Polymorphism

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
   
    def area(self):                    # Overriding
        return self.length * self.width
```

### e. The super() Function

Calls methods from parent class
Especially useful in multiple inheritance (MRO - Method Resolution Order)
Helps avoid hardcoding parent class names

### f. Private & Protected Members in Inheritance

```python
class Parent:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"      # Convention only
        self.__private = "Private"         # Name mangling

class Child(Parent):
    def show(self):
        print(self.public)
        print(self._protected)
        # print(self.__private)   # This will fail
```

### g. Method Resolution Order (MRO)

Python uses C3 linearization to decide the order of method lookup in multiple inheritance.

```python
print(Duck.__mro__)        # Shows the order Python searches for methods
```

### Best Practices for Inheritance:

Use inheritance only when there is a clear "is-a" relationship
Prefer composition ("has-a") over deep inheritance
Keep inheritance hierarchies shallow
Always call super().__init__() in child class constructor
Document inherited behavior clearly

### When NOT to use Inheritance:

When classes are unrelated
When you just want to reuse code (use composition or helper functions instead)




## 3. Polymorphism

**Definition**:
Polymorphism means **"many forms"**. In OOP, it refers to the ability of an object to take many forms — i.e., the same method name can behave differently depending on the object that calls it.

Polymorphism allows us to write more flexible, reusable, and elegant code.

### 1. Types of Polymorphism in Python

### a. Compile-time Polymorphism (Method Overloading)
Python does **not** support traditional method overloading (same method name with different parameters).  
Instead, we use **default arguments** or `*args` / `**kwargs`.

### b. Run-time Polymorphism (Method Overriding)
This is the main form of polymorphism in Python. It occurs when a child class redefines a method that is already defined in the parent class.



### 2. Method Overriding (Core of Polymorphism)

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):                    # Method Overriding
        print("Dog barks: Woof Woof!")

class Cat(Animal):
    def speak(self):                    # Method Overriding
        print("Cat meows: Meow Meow!")
```



### 3. Polymorphism with Functions and Loops

```python
def make_sound(animal):                 # Polymorphic function
    animal.speak()                      # Same method name, different behavior

dog = Dog()
cat = Cat()

make_sound(dog)   # Output: Dog barks: Woof Woof!
make_sound(cat)   # Output: Cat meows: Meow Meow!
```
**Using in a loop:**

```python
animals = [Dog("Buddy"), Cat("Whiskers"), Animal("Generic")]
for animal in animals:
    animal.speak()                      # Polymorphic behavior
```



### 4. Polymorphism with Inheritance & Abstract Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):                       # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
   
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
   
    def area(self):
        import math
        return math.pi * self.radius ** 2

# Polymorphic usage
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(f"Area = {shape.area():.2f}")
```


### 5. Operator Overloading (Another form of Polymorphism)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x        
        self.y = y       
    def __add__(self, other):           # Overloading + operator        
        return Vector(self.x + other.x, self.y + other.y)

   
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 1)
print(v1 + v2)          # Vector(7, 4)
```


### 6. Duck Typing (Python's Special Polymorphism)

Python follows Duck Typing principle:
"If it walks like a duck and quacks like a duck, then it is a duck."

```python
class Car:
    def move(self):
        print("Car is moving on road")

class Airplane:
    def move(self):
        print("Airplane is flying in sky")

def travel(vehicle):
    vehicle.move()          # No inheritance needed!

travel(Car())
travel(Airplane())
```

### 7. Advantages of Polymorphism

Code is more flexible and extensible
Reduces duplication
Easier to maintain
Supports Interface-based programming
Works beautifully with inheritance and abstract classes


### 8. When to Use Polymorphism?

When you have multiple classes with similar behavior
When you want to write generic functions that work with different object types
When designing libraries or frameworks
When implementing design patterns (Strategy, Factory, etc.)


**Key Takeaway:**
Polymorphism allows the same interface (speak(), area(), move()) to have different implementations based on the actual object type.




## 4. Magic Methods (Dunder Methods)


**Special methods surrounded by double underscores (__method__).**

Magic Method,                   Purpose,                                Example
__str__,                        String representation,                  print(obj)
__repr__,                       Official string representation,         repr(obj)
__len__,                        Length using len(),                     len(obj)
__add__,                        + operator,                             obj1 + obj2
__eq__,                         == operator,                            obj1 == obj2
__init__,                       Constructor,                            Object creation
__del__,                        Destructor,                             When object is deleted



```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):        
        return f"Vector({self.x}, {self.y})"

```


## 5. Encapsulation & Access Modifiers

**Definition**:
**Encapsulation** is one of the fundamental principles of Object-Oriented Programming. It is the process of **bundling data (attributes) and methods (functions) that operate on that data into a single unit (class)**, while restricting direct access to some of the object's components.

The main goals of encapsulation are:
- Protect the internal state of an object
- Hide implementation details
- Provide controlled access to data
- Improve code maintainability and security



### 1. Access Modifiers in Python

Python does **not** have strict access modifiers like `public`, `private`, `protected` in Java or C++. Instead, it uses **naming conventions**.


### Three Levels of Access:

Access Level    Naming Convention     Meaning                                                        Can be accessed from

Public          `variable`            Can be accessed from anywhere                                   Everywhere
Protected       `_variable`           Should not be accessed directly (convention)                    Same class + subclasses
Private         `_variable`           Name mangling applied—very difficult to access from outside     Only inside the class


### Example:

```python
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder                    # Public
        self._balance = balance                 # Protected
        self.__transaction_pin = "1234"         # Private (name mangled)
   
    def get_balance(self):                      # Public method
        return self._balance
   
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
```

### 2. Name Mangling for Private Members

When you use __variable, Python automatically changes its name to _ClassName__variable.

```python
acc = BankAccount("Sunny", 50000)
print(acc.__transaction_pin)           # AttributeError
print(acc._BankAccount__transaction_pin)  # Works but not recommended
```


### 3. Using @property for Controlled Access

This is the Pythonic way to implement encapsulation:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks          # Protected
   
    @property
    def marks(self):
        return self._marks
   
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100")
   
    @marks.deleter
    def marks(self):
        print("Marks deleted")
        del self._marks
```


### 4. Getter and Setter Methods (Traditional Way)

```python
class Person:
    def __init__(self):
        self._age = 0
   
    def get_age(self):
        return self._age
   
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative")
```

### 5. Advantages of Encapsulation

Data Hiding: Internal implementation is hidden
Data Validation: Control what values can be assigned
Flexibility: You can change internal logic without affecting external code
Security: Prevents accidental or malicious modification
Maintainability: Easier to debug and modify

### 6. When to Use What?

Use public attributes/methods for general use
Use protected (_) when you want to signal "don't touch directly" but allow subclass access
Use private (__) when the attribute should only be used inside the class
Prefer @property over traditional getters/setters in modern Python

**Best Practice:**
Always validate and control access to sensitive or critical data using properties or setter methods.

