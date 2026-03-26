#Exercise 11
#FizzBuzz: Print numbers 1 to 100.
'''
If divisible by 3 → "Fizz"
If divisible by 5 → "Buzz"
If both → "FizzBuzz"
Otherwise → the number itself
'''

# Ex 11 – FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Exercise 12
'''Write a program that finds the first prime number greater than 100 using a while loop + helper function is_prime().
'''
# Ex 12 (simple is_prime)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
n = 101
while True:
    if is_prime(n):
        print("First prime > 100:", n)
        break
    n += 1
   

#Exercise 13
#Use nested loops to print this multiplication table (1–10):
'''
1   2   3   4 ...
  2   4   6   8 ...
  3   6   9  12 ...
...
'''
#(align numbers nicely if possible)
# Ex 13
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end=" ")
    print()


#Exercise 14

'''Create a number guessing game:
Computer picks random number 1–100.
User has 7 attempts.
After each guess tell "Too high", "Too low", or "Correct!".
Use import random'''


# Ex 14 (needs import random)
import random
secret = random.randint(1, 100)
attempts = 7
while attempts > 0:
    guess = int(input(f"Guess (1-100), {attempts} left: "))
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
    attempts -= 1
else:
    print("Game over. Number was", secret)


#Exercise 15
#Write code that removes all vowels from a string using a for loop + continue.
# Ex 15
text = "Sunny is learning Python in Pune"
result = ""
for char in text:
    if char.lower() in 'aeiou':
        continue
    result += char
print(result)