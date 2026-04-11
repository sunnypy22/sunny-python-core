

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Overloading + operator    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
   
    # Overloading * operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
   
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
v1 = Vector(2, 3)

v2 = Vector(5, 1)
print("v1 + v2 =", v1 + v2)
print("v1 * 3  =", v1 * 3)
