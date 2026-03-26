
# 06_random_examples.py
import random
# Random password generator (simple version)
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ''.join(random.choice(chars) for _ in range(8))
print("Generated password:", password)
# Simulate dice roll 10 times
rolls = [random.randint(1, 6) for _ in range(10)]
print("Dice rolls:", rolls)
print("Most common roll:", max(set(rolls), key=rolls.count))