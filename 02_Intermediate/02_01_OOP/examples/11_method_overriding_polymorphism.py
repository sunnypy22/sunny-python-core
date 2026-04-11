
 
class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
   
    def area(self):                    # Method Overriding
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
   
    def area(self):                    # Method Overriding
        import math
        return math.pi * self.radius ** 2
    
# Polymorphism in action
shapes = [Rectangle(5, 3), Circle(7), Rectangle(10, 2)]
for shape in shapes:
    print(f"Area = {shape.area():.2f}")
