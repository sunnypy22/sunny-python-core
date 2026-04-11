
# Python doesn't care about the type, only about the behavior
class Laptop:
    def code(self):
        print("Coding on Laptop...")
class Desktop:
    def code(self):
        print("Coding on Desktop PC...")
class Developer:
    def work(self, computer):
        computer.code()          # No inheritance required!
# Different classes, same method name → Duck Typing
dev = Developer()
laptop = Laptop()
desktop = Desktop()
dev.work(laptop)
dev.work(desktop)
