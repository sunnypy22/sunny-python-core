# 08_advanced_string_ops.py
text = "Python is an amazing programming language"
# Word frequency
words = text.lower().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequency:", freq)
# Remove vowels
no_vowels = ''.join(c for c in text if c.lower() not in 'aeiou')
print("Without vowels:", no_vowels)
# Anagram check
def is_anagram(s1, s2):
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))
print("Are 'listen' and 'silent' anagrams?", is_anagram("listen", "silent"))