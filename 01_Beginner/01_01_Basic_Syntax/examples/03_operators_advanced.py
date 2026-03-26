# Operator Overloading

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2
print(v3.x, v3.y)   # 6 4