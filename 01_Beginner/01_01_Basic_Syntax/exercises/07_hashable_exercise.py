# Exercise 7: Show that tuple can be dict key but list cannot

d = {}
d[(1,2)] = "tuple works"     # OK
# d[[1,2]] = "list fails"    # TypeError
print(d)