
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
# Operator Overloading    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
   
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
   
    def __len__(self):
        return 2   # A 2D vector has 2 components
    
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1)                    # Uses __str__
print(v1 + v2)               # Uses __add__
print(v1 * 3)                # Uses __mul__
print("Length of vector:", len(v1))

