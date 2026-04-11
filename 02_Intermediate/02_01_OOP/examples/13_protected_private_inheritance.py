
class Parent:
    def __init__(self):
        self.public = "Public member"
        self._protected = "Protected member"      # Protected
        self.__private = "Private member"         # Private

class Child(Parent):
    def show(self):
        print("Public:", self.public)
        print("Protected:", self._protected)
        # print(self.__private)       # This will raise AttributeError
       
        # Accessing private via name mangling (not recommended)
        print("Private (via mangling):", self._Parent__private)
parent = Parent()
child = Child()
child.show()
