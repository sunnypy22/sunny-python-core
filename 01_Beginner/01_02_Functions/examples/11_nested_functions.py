# Functions inside functions + closure
def create_counter():
    count = 0           # enclosed variable
    def increment():
        nonlocal count
        count += 1
        return count
    def reset():
        nonlocal count
        count = 0
        return count
    return increment, reset
counter_up, counter_reset = create_counter()
print(counter_up())     # 1
print(counter_up())     # 2
print(counter_up())     # 3
print(counter_reset())  # 0
print(counter_up())     # 1