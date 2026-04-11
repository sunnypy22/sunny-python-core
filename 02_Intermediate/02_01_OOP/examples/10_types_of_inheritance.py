

# 1. Single Inheritance
class Animal:
    pass
class Dog(Animal):
    pass
# 2. Multilevel Inheritance
class Mammal(Animal):
    pass
class Dog(Mammal):
    pass

# 3. Multiple Inheritance
class Flyable:
    def fly(self):
        print("Flying...")
class Swimmable:
    def swim(self):
        print("Swimming...")
class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack!")
# 4. Hierarchical Inheritance

class Cat(Animal):
    pass
class Cow(Animal):
    pass
