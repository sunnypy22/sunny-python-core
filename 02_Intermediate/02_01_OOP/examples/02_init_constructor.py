
class Student:
    def __init__(self, name, roll_no, marks=0):
        """Constructor - called automatically when object is created"""
        print(f"Creating student object for {name}...")
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = self.calculate_grade()

  
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        else:
            return "F"
        
  
    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}, Grade: {self.grade}")
# Creating objects - __init__ is called automatically
s1 = Student("Sunny", 101, 92)
s2 = Student("Rahul", 102, 75)
s1.display()
s2.display()


