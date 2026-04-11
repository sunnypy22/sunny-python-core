
def get_numbers():
    for i in range(1, 11):
        yield i
def square(numbers):
    for n in numbers:
        yield n**2
def only_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n
# Lazy pipeline
result = only_even(square(get_numbers()))
for val in result:
    print(val)   # 4 16 36 64 100
