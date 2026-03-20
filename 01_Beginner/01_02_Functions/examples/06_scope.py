# Demonstrating LEGB rule + global / nonlocal
x = "global variable"
def outer_function():
    x = "enclosing variable"
    def inner_function():
        x = "local variable"
        print("Inside inner:", x)
        # nonlocal x    # uncomment to change enclosing x
        # x = "modified enclosing"
    inner_function()
    print("Inside outer:", x)
outer_function()
print("Global scope:", x)
# Try uncommenting nonlocal and global lines to see difference