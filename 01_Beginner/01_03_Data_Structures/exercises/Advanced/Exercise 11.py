# Show difference between set and frozenset (try to use frozenset as dict key).

# Exercise 11 - set vs frozenset

mutable_set = {"red", "green", "blue"}
mutable_set.add("yellow")
print("Mutable set:", mutable_set)
# frozenset is immutable → can be dict key
immutable = frozenset(["apple", "banana", "cherry"])
categories = {
    immutable: "fruits",
    frozenset(["car", "bus", "bike"]): "vehicles"
}
print("\nUsing frozenset as key:")
print(categories)
# This would fail:
# categories[mutable_set] = "colors"   # TypeError: unhashable type: 'set'
