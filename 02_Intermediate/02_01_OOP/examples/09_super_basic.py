
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
   
    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")
class Car(Vehicle):
    def __init__(self, brand, year, model, fuel_type):
        super().__init__(brand, year)        # Calling parent __init__
        self.model = model
        self.fuel_type = fuel_type
   
    def display_info(self):
        super().display_info()               # Calling parent method
        print(f"Model: {self.model}")
        print(f"Fuel Type: {self.fuel_type}")
car = Car("Toyota", 2023, "Camry", "Petrol")
car.display_info()


