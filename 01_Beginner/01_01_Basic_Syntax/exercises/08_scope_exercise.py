# Exercise 8: Create global and local variable with same name and print both

x = "global"
def func():
    x = "local"
    print(x)
func()
print(x)   # global