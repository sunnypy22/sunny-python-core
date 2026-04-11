
# Public, Protected, and Private members
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder                    # Public
        self._balance = balance                 # Protected (convention)
        self.__pin = "4321"                     # Private (name mangling)
   
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited successfully.")
   
    def show_balance(self):
        return self._balance
   
    def _internal_audit(self):                  # Protected method
        print("Internal audit performed.")
    def get_pin(self):                          # Only way to access private
        return self.__pin
acc = BankAccount("Sunny", 50000)
print("Holder (Public):", acc.holder)
print("Balance (via method):", acc.show_balance())
# Protected member - accessible but not recommended
print("Protected balance:", acc._balance)
# Private member - will raise error
# print(acc.__pin)        # AttributeError
print("PIN (via getter method):", acc.get_pin())
