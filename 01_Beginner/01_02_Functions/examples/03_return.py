# Returning values from functions
def add(a, b):
    result = a + b
    return result
def multiply(x, y):
    return x * y
sum_result = add(8, 12)
product = multiply(7, 6)
print("8 + 12 =", sum_result)      # 20
print("7 × 6 =", product)          # 42
# You can return multiple values using tuple packing
def get_min_max(a, b, c):
    return min(a,b,c), max(a,b,c)
small, big = get_min_max(5, 1, 9)
print(f"min = {small}, max = {big}")