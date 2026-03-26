#Exercises – Beginner
#---------------------------------------------
##Exercise 1
#Write a program that asks the user for a number and prints whether it is:
#positive
#negative
#or zero
# Ex 1
n = int(input("Enter number: "))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")
#---------------------------------------------
##Exercise 2

#Ask the user for their age. Print different messages according to these ranges:
#< 13 → "Child"
#13–17 → "Teenager"
#18–64 → "Adult"
#65+ → "Senior"

# Ex 2

age = int(input("Age: "))
if age < 13:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")
#---------------------------------------------
##Exercise 3

#Print all numbers from 1 to 20 using a for loop.
# Ex 3
for i in range(1, 21):
    print(i)
#---------------------------------------------
##Exercise 4
#Print only the even numbers between 1 and 30 (inclusive) using a for loop.
# Ex 4
for i in range(1, 31):
    if i % 2 == 0:
        print(i)
#---------------------------------------------
#Exercise 5
#Use a while loop to print numbers from 10 down to 1, then print "Blast off!".
# Ex 5
count = 10
while count >= 1:
    print(count)
    count -= 1
print("Blast off!")