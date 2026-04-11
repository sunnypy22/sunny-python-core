
class Person:
    """This is a simple Person class"""

   
    # Class Attribute (shared by all objects)
    species = "Homo sapiens"
   
    def __init__(self, name, age, city="Pune"):
        # Instance Attributes
        self.name = name
        self.age = age
        self.city = city
   
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old from {self.city}.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! Now you are {self.age} years old.")

# Creating objects (instances)
p1 = Person("Sunny", 25)
p2 = Person("Priya", 22, "Mumbai")
p1.introduce()
p2.introduce()
p1.celebrate_birthday()
print(f"\nSpecies: {Person.species}")

