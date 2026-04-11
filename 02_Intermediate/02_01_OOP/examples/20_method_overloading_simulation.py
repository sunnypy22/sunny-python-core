
# Python does not support traditional method overloading
# We simulate it using default arguments or *args

class Calculator:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
        
            return a + b + c
        
calc = Calculator()
print(calc.add(5))           # 1 argument
print(calc.add(5, 10))       # 2 arguments
print(calc.add(5, 10, 15))   # 3 arguments
