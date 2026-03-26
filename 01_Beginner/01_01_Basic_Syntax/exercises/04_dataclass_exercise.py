# Exercise 4: Create a dataclass Car with brand, model, year and print an object

from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str
    year: int
my_car = Car("Toyota", "Camry", 2023)
print(my_car)
