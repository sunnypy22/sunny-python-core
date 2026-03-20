# Functions with default argument values
def introduce(name, city="Pune", age=20):
    print(f"My name is {name}.")
    print(f"I live in {city}.")
    print(f"I am {age} years old.\n")
introduce("Sunny")                    # uses defaults for city & age
introduce("Aarav", "Mumbai")
introduce("Neha", age=22, city="Delhi")