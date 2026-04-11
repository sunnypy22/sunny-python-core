# Demonstrating Name Mangling for Private Members
class Parent:
    def __init__(self):
        self.public = "This is public"
        self._protected = "This is protected"
        self.__private = "This is private (mangled)"
class Child(Parent):
    def access_members(self):
        print("Public:", self.public)
        print("Protected:", self._protected)
        # print(self.__private)     # This will fail
        print("Private via mangling:", self._Parent__private)
print("=== Name Mangling Demo ===")
child = Child()
child.access_members()
# Direct access to mangled name from outside
print("\nDirect mangled access:", child._Parent__private)
