# map() and filter() with lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# map: apply function to every element
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)
# filter: keep only elements that match condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)
# Combined: square only the even numbers
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print("Squares of evens:", even_squares)