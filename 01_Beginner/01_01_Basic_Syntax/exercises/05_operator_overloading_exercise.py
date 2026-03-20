# Exercise 5: Create class Point that supports + operator (add x and y)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(2, 3)
p2 = Point(4, 1)
print((p1 + p2).x, (p1 + p2).y)   # 6 4