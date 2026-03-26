# 09_package_structure_demo/string_utils.py
def reverse_string(text):
    return text[::-1]
def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())