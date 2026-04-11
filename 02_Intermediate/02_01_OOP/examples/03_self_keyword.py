class Car:
    def __init__(self, brand, model):
        self.brand = brand      # self refers to current object
        self.model = model
   
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started!")
   
    def show_info(self):
        print(f"Car: {self.brand} {self.model}")
   
    def compare(self, other_car):
        if self.brand == other_car.brand:
            print(f"Both cars are from {self.brand}")
        else:
            print(f"Different brands: {self.brand} vs {other_car.brand}")
# Usage
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "City")
car1.start_engine()
car1.show_info()
car2.show_info()
car1.compare(car2)