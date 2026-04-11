
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder        # Public
        self._balance = balance                     # Protected (convention)
        self.__pin = "9876"                         # Private (name mangling)
   
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}")
   
    def get_balance(self):
        return self._balance
   
    def _internal_check(self):                      # Protected method
        print("Internal system check...")
    def show_pin(self):
        # Accessing private variable inside class
        print(f"Pin (for demo): {self.__pin}")
acc = BankAccount("Sunny", 50000)
print("Account Holder:", acc.account_holder)
print("Balance:", acc.get_balance())
acc.deposit(10000)
# These are not recommended:
print("Protected balance (not recommended):", acc._balance)
# print(acc.__pin)          # This will raise AttributeError
acc.show_pin()
