
# Generator expression (lazy)
squares_gen = (x**2 for x in range(1, 1000000))
print("Type:", type(squares_gen))
print("First 5 squares:", [next(squares_gen) for _ in range(5)])