# Exercise 1: Basic Class and Object
# Create a class named 'Book' with:
# - Instance attributes: title, author, pages
# - A method display_info() that prints book details
# Create two book objects and call the method




# Exercise 2: __init__ Method (Constructor)
# Create a class 'Student' with:
# - __init__ method that takeƶs name, roll_no, and marks
# - Automatically calculate grade (A, B, C, F) based on marks
# - A method show_details() to display all information



# Create 3 student objects with different marks
# Exercise 3: self Keyword
# Create a class 'Rectangle' with:
# - length and width as attributes
# - A method calculate_area() that returns area
# - A method calculate_perimeter() that returns perimeter
# - A method compare_area(other_rect) that compares area with another rectangle
# Create two rectangle objects and compare them




# Exercise 4: Attributes (Class vs Instance)
# Create a class 'Employee' with:
# - Class attribute: company_name = "xAI"
# - Instance attributes: name, salary, department
# - A method show_employee_count() using class attribute
# Create 3 employees and show total employee count



# Exercise 5: Methods
# Create a class 'Calculator' with:
# - Instance method: add, subtract, multiply, divide
# - Class method: get_version() that returns "Calculator v1.0"
# - Static method: is_prime(number) that checks if a number is prime
# Test all methods



# Exercise 6: Access Modifiers
# Create a class 'BankAccount' with:
# - Public: account_holder
# - Protected: _balance
# - Private: __account_pin
# - Methods: deposit(), withdraw(), get_balance()
# - Try accessing private attribute from outside and handle it




# Exercise 7: Property Decorator
# Create a class 'Temperature' with:
# - Private attribute _celsius
# - @property for celsius and fahrenheit
# - Setter for celsius that validates temperature (> -273.15)
# - When celsius is set, fahrenheit should be automatically calculated




# Exercise 8: Magic/Dunder Methods
# Create a class 'Point' with x and y coordinates
# Implement following magic methods:
# - __str__() : "Point(x, y)"
# - __add__() : to add two points
# - __eq__()  : to check if two points are equal
# - __len__() : return distance from origin (use math.sqrt)




# Exercise 9: Encapsulation
# Create a class 'Student' with:
# - Private attribute __marks
# - Use @property and @marks.setter to control marks (0 to 100 only)
# - Raise ValueError if invalid marks are assigned
# Test with valid and invalid marks




# Exercise 10: Combined Concepts
# Create a class 'LibraryBook' that demonstrates:
# - __init__ with multiple parameters
# - Class attribute (total_books)
# - Public, protected, and private attributes
# - Property for book_status
# - Magic method __str__



# Exercise 11: Advanced Magic Methods
# Create a class 'Matrix' (2x2) that supports:
# - __add__ for matrix addition
# - __mul__ for matrix multiplication with scalar and another matrix
# - __str__ for nice printing
# - __eq__ to compare two matrices



# Exercise 12: Real-world Encapsulation
# Create a class 'EmployeeManagement' with:
# - Private list of employees
# - Methods to add_employee(), remove_employee(), get_employee_by_id()
# - Property to get total_salary
# - Proper validation and encapsulation



# Exercise 13: Inheritance + Encapsulation
# Create parent class 'Vehicle' with protected _speed and private __fuel
# Create child class 'Car' that properly uses super() and adds its own attributes
# Demonstrate access to protected vs private members



# Exercise 14: Comprehensive Class Design
# Design a class 'ShoppingCart' that includes:
# - List of items (private)
# - Methods: add_item(), remove_item(), get_total()
# - Property: item_count
# - Magic method: __len__ and __str__
# - Proper encapsulation




# Exercise 15: All Concepts Combined
# Create a class 'UniversityStudent' that demonstrates:
# - __init__ with validation
# - Class attributes
# - Public, protected, private members
# - @property and setter
# - At least two magic methods
# - Proper documentation



# Exercise 16: Single Inheritance
# Create a parent class 'Vehicle' with:
# - Attributes: brand, year
# - Method: show_info() that prints brand and year
# Create a child class 'Car' that inherits from Vehicle and adds:
# - Attribute: model
# - Method: show_car_info() that calls parent's show_info() and prints model
# Create a Car object and test both methods



# Exercise 17: Constructor in Inheritance
# Create a parent class 'Person' with __init__ taking name and age
# Create a child class 'Student' that:
# - Inherits from Person
# - Adds attribute: roll_no and marks
# - Uses super() to call parent's __init__
# - Has a method show_details() to display all information
# Create a Student object and call show_details()



# Exercise 18: Method Overriding
# Create a parent class 'Animal' with method make_sound() that prints "Animal makes sound"
# Create two child classes:
# - Dog: overrides make_sound() to print "Woof Woof!"
# - Cat: overrides make_sound() to print "Meow Meow!"
# Create objects of Dog and Cat and call make_sound() on both



# Exercise 19: Basic Polymorphism
# Create a function make_sound(animal) that calls animal.make_sound()
# Using the Animal, Dog, and Cat classes from Exercise 3,
# Create a list of animals and loop through them calling make_sound()
# This demonstrates polymorphism



# Exercise 20: Protected Members
# Create a parent class 'Bank' with:
# - Protected attribute: _balance
# - Method: deposit(amount)
# Create a child class 'SavingsAccount' that inherits from Bank
# Add a method show_balance()
# Test accessing protected attribute from child class



# Exercise 21: Using super() Effectively
# Create a class hierarchy:
# Person → Employee → Manager
# Each class should:
# - Have its own __init__
# - Use super() to call parent's __init__
# - Have its own display_info() method that calls parent's display_info()
# Create a Manager object and call display_info()



# Exercise 22: Multiple Inheritance
# Create two parent classes:
# - Flyable with method fly()
# - Swimmable with method swim()
# Create a child class 'Duck' that inherits from both
# Add a method quack()
# Create a Duck object and call all three methods



# Exercise 23: Method Resolution Order (MRO)
# Create classes A, B, C, D with multiple inheritance like:
# D inherits from B and C
# B and C both inherit from A
# In each class, define a method show() that prints the class name
# Call show() on D object and print D.__mro__



# Exercise 24: Polymorphism with Shapes
# Create an abstract-like parent class 'Shape' with method area()
# Create child classes: Rectangle and Circle
# Both should override area() method
# Write a function print_area(shape) that works with any shape object
# Test with both Rectangle and Circle objects



# Exercise 25: Encapsulation in Inheritance
# Create parent class 'Account' with:
# - Private attribute __balance
# - Protected attribute _account_type
# Create child class 'SavingsAccount'
# Demonstrate how child class can access protected but not private members directly



# Exercise 26: Complex Inheritance
# Design a class hierarchy for a University System:
# Person → Student → EngineeringStudent
# Person → Faculty
# Use super() properly in all constructors
# Add appropriate methods and attributes in each level



# Exercise 27: Operator Overloading + Inheritance
# Create class 'Shape' with __add__ method (to combine areas)
# Create Rectangle and Circle classes that inherit from Shape
# Implement __add__ so that shape1 + shape2 returns total area



# Exercise 28: Real-world Inheritance
# Create a class hierarchy for Employees:
# Employee → Developer → SeniorDeveloper
# Employee → Manager
# Use protected and private members appropriately
# Demonstrate method overriding and polymorphism



# Exercise 29: MRO Challenge
# Create 4 classes with diamond inheritance pattern:
# A → B → D
# A → C → D
# Define a method in each class and observe MRO behavior
# Print __mro__ of class D



# Exercise 30: Comprehensive Inheritance
# Build a complete system with:
# - Multiple inheritance
# - Proper use of super()
# - Method overriding & polymorphism
# - Protected and private members
# - Magic methods (__str__, __repr__)
# Topic: Vehicle → ElectricVehicle and FlyingVehicle



# Exercise 31: Method Overriding (Basic)
# Create a parent class 'Vehicle' with a method move() that prints "Vehicle is moving"
# Create two child classes:
# - Car: overrides move() to print "Car is driving on road"
# - Bicycle: overrides move() to print "Bicycle is cycling"
# Create objects of Car and Bicycle and call move() on both



# Exercise 32: Polymorphism with Function
# Create a function make_sound(animal) that calls animal.make_sound()
# Create these classes:
# - Dog with make_sound() → "Woof Woof!"
# - Cat with make_sound() → "Meow Meow!"
# - Cow with make_sound() → "Moo Moo!"
# Create a list of animals and use the function to make them all speak



# Exercise 33: Polymorphism with Shapes
# Create a parent class 'Shape' with method area()
# Create child classes:
# - Rectangle (length, width)
# - Square (side)
# Both should override area() method
# Write a function print_area(shape) and test it with both shapes



# Exercise 34: Basic Operator Overloading
# Create a class 'Point' with x and y coordinates
# Implement __add__ method so that you can add two points (p1 + p2)
# The result should return a new Point with summed coordinates
# Also implement __str__ to print "Point(x, y)"



# Exercise 35: Duck Typing
# Create a class 'Developer' with a method work(computer)
# Create two classes:
# - Laptop with code() method
# - Desktop with code() method
# The Developer should be able to work with both without any inheritance



# Exercise 36: Polymorphism with Abstract Classes
# Create an abstract class 'Payment' with abstract method pay(amount)
# Create three child classes:
# - CreditCard
# - UPI
# - Cash
# Each should implement pay() differently
# Write a polymorphic function process_payment(payment, amount) and test all types



# Exercise 37: Advanced Polymorphism with Shapes
# Create an abstract class Shape with methods area() and perimeter()
# Implement three shapes: Rectangle, Circle, Triangle
# Create a list of different shapes and loop through them to print area and perimeter



# Exercise 38: Simulate Method Overloading
# Create a class 'MathOperations' with a method 'multiply'
# The method should handle:
# - One argument (return the number)
# - Two arguments (multiply them)
# - Three arguments (multiply all three)
# Use default parameters or *args to achieve this



# Exercise 39: Polymorphism in Real-world Scenario
# Create parent class 'Employee' with method calculate_salary()
# Create child classes:
# - FullTimeEmployee
# - PartTimeEmployee
# - Intern
# Each should override calculate_salary() differently
# Demonstrate polymorphism by storing all in a list and calculating total salary


# Exercise 40: Operator Overloading + Polymorphism
# Create a class 'Vector' with __add__, __sub__, and __mul__ methods
# Also implement __str__ and __eq__ (to compare two vectors)
# Test vector addition, subtraction, multiplication by scalar, and equality check


# Exercise 41: Comprehensive Polymorphism
# Design a Notification System:
# Create an abstract class 'Notification' with send() method
# Implement:
# - EmailNotification
# - SMSNotification
# - PushNotification
# Create a function send_all(notifications, message) that sends the same message
# using all notification types (demonstrates polymorphism)


# Exercise 42: Polymorphism with Multiple Inheritance
# Create classes:
# - Flyable with fly() method
# - Swimmable with swim() method
# Create a class 'AmphibiousVehicle' that inherits from both and adds move() method
# Demonstrate polymorphic behavior with different vehicle types


# Exercise 43: Advanced Operator Overloading
# Create a class 'Matrix' (2x2) that supports:
# - Addition using +
# - Multiplication using *
# - String representation using __str__
# Also implement __eq__ to compare two matrices


# Exercise 44: Real-world Polymorphism
# Create a 'PaymentProcessor' system where different payment gateways
# (Stripe, PayPal, Razorpay) implement the same interface but process differently
# Use abstract class and demonstrate polymorphism


# Exercise 45: Challenge - Full Polymorphism System
# Build a small Animal Kingdom system with:
# - Abstract class Animal with make_sound() and move()
# - At least 5 different animals (Lion, Eagle, Fish, Snake, Penguin)
# - A Zoo class that can add animals and make all animals perform actions
# - Demonstrate polymorphism, method overriding, and duck typing


# Exercise 46: Basic Magic Methods
# Create a class 'Book' with title, author, and year
# Implement __str__ and __repr__ methods
# Create a book object and test print(book) and repr(book)


# Exercise 47: Operator Overloading
# Create a class 'Point' with x and y
# Implement __add__ and __str__
# Test: p1 + p2 should return a new Point


# Exercise 48: Advanced Operator Overloading
# Create class 'Vector' with __add__, __mul__, __eq__, and __str__
# Support both vector + vector and vector * scalar


# Exercise 49: Container Magic Methods
# Create a 'ShoppingCart' class that supports:
# - cart["item"] = quantity   (__setitem__)
# - print(cart["item"])       (__getitem__)
# - "item" in cart            (__contains__)
# - len(cart)                 (__len__)


# Exercise 50: Fraction Class
# Create a 'Fraction' class with numerator and denominator
# Implement __add__, __str__, and __eq__
# Bonus: Simplify the fraction automatically


# Exercise 51: Matrix with Magic Methods
# Create a 2x2 Matrix class that supports:
# - Addition using +
# - Multiplication using *
# - __str__ for nice printing
# - __eq__ for comparison


# Exercise 52: Custom List Class
# Create a class 'MyList' that behaves like a list:
# Support indexing, slicing, len(), + operator, and 'in' operator


# Exercise 53: Complex Number
# Create class 'Complex' that supports:
# - Addition, subtraction, multiplication
# - __str__ to show as "a + bi"
# - __abs__ for magnitude


# Exercise 54: Basic Encapsulation
# Create a class 'Person' with:
# - Public attribute: name
# - Protected attribute: _age
# - Private attribute: __ssn (social security number)
# Add a method show_details() that displays name and age
# Try accessing all three attributes from outside the class


# Exercise 55: Traditional Getter and Setter
# Create a class 'Employee' with:
# - Private attribute __salary
# - Getter method get_salary()
# - Setter method set_salary() with validation (salary > 0)


# Exercise 56: Using @property
# Create a class 'Circle' with:
# - Private attribute _radius
# - @property for radius (getter)
# - @radius.setter with validation (radius > 0)
# - @property for area (read-only)


# Exercise 57: Real-world Encapsulation
# Create a class 'BankAccount' with:
# - Private attribute __balance
# - Public attribute account_holder
# - Methods: deposit(), withdraw(), get_balance()
# - withdraw() should check for sufficient balance


# Exercise 58: Name Mangling
# Create a parent class 'Device' with a private attribute __serial_number
# Create a child class 'Phone' that tries to access the private attribute
# Demonstrate how name mangling works


# Exercise 59: Comprehensive Encapsulation
# Create a class 'StudentRecord' with:
# - Private attribute __marks
# - @property and setter for marks (0-100 validation)
# - @property for grade (calculated based on marks)
# - Traditional getter/setter methods as backup


# Exercise 60: Secure Bank Account
# Create a class 'SecureAccount' that uses:
# - Private balance and pin
# - Property for balance (read-only)
# - Method to change_pin() with old pin verification
# - Proper encapsulation and validation


# Exercise 61: Product Class with Full Encapsulation
# Create a class 'Product' with:
# - Private __price and __stock
# - Properties for price and stock with validation
# - Methods to sell() and restock()
