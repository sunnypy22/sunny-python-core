
class A:
    def process(self):
        print("A")
class B(A):
    def process(self):
        print("B")
        super().process()

class C(A):
    def process(self):
        print("C")
        super().process()
class D(B, C):
    def process(self):
        print("D")
        super().process()
d = D()
d.process()
print("\nMRO of D:", D.__mro__)
print("MRO of C:", C.__mro__)
