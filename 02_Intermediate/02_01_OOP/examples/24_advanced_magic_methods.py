
# __getitem__, __setitem__, __contains__, __del__
class ShoppingCart:
    def __init__(self):
        self.items = {}
   
    # Allows cart["apple"] = 3
    def __setitem__(self, item, quantity):
        self.items[item] = quantity
   
    # Allows print(cart["apple"])
    def __getitem__(self, item):
        return self.items.get(item, 0)
   
    # Allows "apple" in cart
    def __contains__(self, item):
        return item in self.items
   
    # Allows del cart["apple"]
    def __delitem__(self, item):
        if item in self.items:
            del self.items[item]
   
    def __len__(self):
        return len(self.items)
   
    def __str__(self):
        return f"Cart: {self.items}"
cart = ShoppingCart()
cart["apple"] = 5
cart["banana"] = 3
print(cart)
print("Apples in cart:", cart["apple"])
print("Total items:", len(cart))
print("Is mango in cart?", "mango" in cart)
del cart["banana"]
print("After deleting banana:", cart)
# 25_init_and_del.py
# __init__ and __del__
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"Resource '{name}' created")
   
    def __del__(self):
        print(f"Resource '{self.name}' is being destroyed (cleanup)")
# Usage
r1 = Resource("Database Connection")
r2 = Resource("File Handle")
del r1   # Explicitly delete
print("End of program")


