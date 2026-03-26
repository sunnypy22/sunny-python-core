# Exercise 8: Add __lt__ and __eq__ to a class Student for comparison by marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __lt__(self, other):
        return self.marks < other.marks
    def __eq__(self, other):
        return self.marks == other.marks
    
s1 = Student("Sunny", 85)
s2 = Student("Rahul", 90)
print(s1 < s2)   # True