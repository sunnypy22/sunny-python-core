
class Calculator:
    # Instance Method
    def add(self, a, b):
        return a + b
   
    def multiply(self, a, b):
        return a * b
   
    # Class Method
    @classmethod
    def get_version(cls):
        return "Calculator v2.1"
   
    # Static Method
    @staticmethod
    def is_even(number):
        return number % 2 == 0
calc = Calculator()
print("10 + 15 =", calc.add(10, 15))
print("Version:", Calculator.get_version())
print("Is 42 even?", Calculator.is_even(42))
