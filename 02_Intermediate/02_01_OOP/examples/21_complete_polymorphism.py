


from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")
class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")
class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} in Cash")

# Polymorphic Function
def process_payment(payment_method, amount):
    payment_method.pay(amount)
# Using polymorphism
payments = [CreditCard(), UPI(), Cash()]

for method in payments:
    process_payment(method, 1500)
