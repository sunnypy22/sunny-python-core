# *args and **kwargs
def print_all(*args):
    print("Positional arguments:")
    for item in args:
        print("  ", item)
def describe_person(**kwargs):
    print("Person details:")
    for key, value in kwargs.items():
        print(f"  {key:10} : {value}")
print_all(10, "hello", True, 3.14)
print()
describe_person(name="Sunny", age=25, city="Pune", job="Student")