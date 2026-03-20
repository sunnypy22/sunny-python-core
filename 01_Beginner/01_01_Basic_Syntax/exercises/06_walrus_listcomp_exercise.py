# Exercise 6: Use walrus operator in list comprehension to filter even numbers > 10
numbers = [5, 12, 8, 15, 3]
evens = [n for n in numbers if (x := n) % 2 == 0 and x > 10]
print(evens)   # [12]