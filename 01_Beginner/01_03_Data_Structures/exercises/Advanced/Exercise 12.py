# Use collections.defaultdict(int) to count word occurrences in a sentence.

# Exercise 12 - defaultdict for counting
from collections import defaultdict
sentence = "python is fun python is easy python is powerful"
word_count = defaultdict(int)
for word in sentence.split():
    word_count[word] += 1
print("Word frequencies:")
for word, count in sorted(word_count.items()):
    print(f"{word:10} : {count:2}x")
# Output:
# easy       :  1x
# fun        :  1x
# is         :  3x
# powerful   :  1x
# python     :  3x