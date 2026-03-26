#Exercise 6

#Ask the user for a password. Allow up to 3 attempts. If correct ("python123"), print "Access granted". After 3 wrong attempts → "Account locked".
# Ex 6
attempts = 3
while attempts > 0:
    pw = input("Password: ")
    if pw == "python123":
        print("Access granted")
        break
    attempts -= 1
    print(f"Wrong. {attempts} left.")
else:
    print("Account locked")
#---------------------------------
#Exercise 7
#Print this pattern using nested for loops:
'''
*
**
***
****
*****
'''
# Ex 7
for i in range(1, 6):
    print("*" * i)
#---------------------------------
#Exercise 8
#Given this list:
numbers = [4, 7, 2, 9, 12, 5, 8, 1, 15]
#Print only numbers that are greater than 5 and even.
# Ex 8
for n in numbers:
    if n > 5 and n % 2 == 0:
        print(n)
#---------------------------------
#Exercise 9
'''Use a for loop + else clause to check whether the list contains the number 7.
Print "7 found" if it exists, otherwise print "7 not found" (without using any if inside the loop).
'''
# Ex 9
for num in numbers:
    if num == 7:
        print("7 found")
        break
else:
    print("7 not found")
#---------------------------------
#Exercise 10
#Write a program that keeps asking for numbers until the user enters 0. Then print the sum of all numbers entered (excluding 0).
# Ex 10
total = 0
while True:
    n = int(input("Number (0 to stop): "))
    if n == 0:
        break
    total += n
print("Sum =", total)