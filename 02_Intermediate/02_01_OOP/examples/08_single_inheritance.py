
class Animal:                    # Parent / Base Class

    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def eat(self):
        print(f"{self.name} is eating.")

   
    def sleep(self):
        print(f"{self.name} is sleeping.")
class Dog(Animal):               # Child / Derived Class
    def __init__(self, name, age, breed):
        self.breed = breed
        super().__init__(name, age)   # Call parent constructor
   
    def bark(self):
        print(f"{self.name} says Woof Woof!")


# Usage
dog = Dog("Buddy", 5, "Golden Retriever")
dog.eat()      # Inherited from Animal
dog.sleep()    # Inherited from Animal
dog.bark()     # Child's own method


