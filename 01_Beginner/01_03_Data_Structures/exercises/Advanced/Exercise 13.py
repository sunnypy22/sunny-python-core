# Use collections.Counter to find 3 most common letters in a long string.

# Exercise 13 - Counter for character frequency
from collections import Counter
text = """
Python is an interpreted high-level general-purpose programming language.
Its design philosophy emphasizes code readability with its use of significant indentation.
"""
# Remove spaces, newlines, punctuation and make lowercase
clean_text = ''.join(c.lower() for c in text if c.isalpha())
letter_freq = Counter(clean_text)
print("Top 5 most common letters:")
for letter, count in letter_freq.most_common(5):
    print(f"{letter} : {count}")