# Intermediate - Scope & Unpacking
def my_func():
    global x
    x = 100
x = 50
my_func()
print(x)  # 100
# Unpacking
person = ("Sunny", 25, "Pune")
name, age, city = person
print(name, age, city)