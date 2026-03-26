# 06_string_replacement.py
text = "I love Java. Java is great. Java is fast."
new_text = text.replace("Java", "Python")
print("After replace:", new_text)
# Replace only first occurrence
print("Replace only first:", text.replace("Java", "Python", 1))