# 11_set_frozenset.py
# Mutable set
colors = {"red", "green", "blue"}
colors.add("yellow")
print("Mutable set:", colors)
# Immutable frozenset → can be dict key
fs = frozenset(["apple", "banana", "cherry"])
print("Frozenset:", fs)
# Using as dict key
categories = {
    fs: "fruits",
    frozenset(["car", "bus"]): "vehicles"
}
print("Categories:", categories)
# colors cannot be key → TypeError: unhashable type: 'set'