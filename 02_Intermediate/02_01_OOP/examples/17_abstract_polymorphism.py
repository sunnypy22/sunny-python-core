
# 17_abstract_polymorphism.py
from abc import ABC, abstractmethod
class Shape(ABC):               # Abstract Base Class
    @abstractmethod
    def area(self):
        pass
   
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
   
    def area(self):
        return self.length * self.width
   
    def perimeter(self):
        return 2 * (self.length + self.width)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
   
    def area(self):
        import math
        return math.pi * self.radius ** 2
   
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius
# Polymorphic usage

shapes = [Rectangle(5, 3), Circle(7)]
for shape in shapes:
    print(f"Area: {shape.area():.2f} | Perimeter: {shape.perimeter():.2f}")
