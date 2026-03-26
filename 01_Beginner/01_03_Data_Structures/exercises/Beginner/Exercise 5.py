# Ask user for name and age. Print "Hello [name], next year you'll be [age+1]".
# Exercise 5 - Simple input + output
name = input("What is your name? ").strip()
age_input = input("How old are you? ").strip()
try:
    age = int(age_input)
    next_year = age + 1
    print(f"Hello {name.title()}, next year you'll be {next_year}!")
except ValueError:
    print("Sorry, age must be a number.")
# Example run:
# What is your name? sunny
# How old are you? 25
# Hello Sunny, next year you'll be 26!
#DIR Intermediate