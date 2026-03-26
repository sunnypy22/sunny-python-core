# 13_counter.py
from collections import Counter
text = "python is fun and python is powerful and easy"
letter_count = Counter(text.replace(" ", ""))
print("Most common letters:", letter_count.most_common(5))
words = text.split()
word_count = Counter(words)
print("\nMost common words:", word_count.most_common(3))
# Arithmetic
c1 = Counter(a=4, b=2, c=1)
c2 = Counter(a=1, b=3, d=2)
print("Combined:", c1 + c2)
print("Subtract:", c1 - c2)