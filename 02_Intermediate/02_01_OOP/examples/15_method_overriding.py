
# 15_method_overriding.py
# Run-time Polymorphism using Method Overriding
class Animal:
    def speak(self):
        print("Animal makes a generic sound")
class Dog(Animal):
    def speak(self):                    # Method Overriding
        print("Dog barks: Woof! Woof!")
class Cat(Animal):
    def speak(self):                    # Method Overriding
        print("Cat meows: Meow! Meow!")
class Cow(Animal):
    def speak(self):
        print("Cow moos: Moo! Moo!")

# Demonstrating Run-time Polymorphism
animals = [Dog(), Cat(), Cow(), Animal()]
for animal in animals:
    animal.speak()      # Same method name, different behavior