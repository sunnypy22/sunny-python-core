
class A:
    def show(self):
        print("Method from A")
class B(A):
    def show(self):
        print("Method from B")
        super().show()
class C(A):
    def show(self):
        print("Method from C")
        super().show()
class D(B, C):          # Multiple Inheritance
    def show(self):
        print("Method from D")
        super().show()      # Follows MRO

d = D()
d.show()
print("\nMethod Resolution Order (MRO):")
print(D.__mro__)
