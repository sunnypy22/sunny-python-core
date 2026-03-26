# 07_palindrome_check.py
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
print("Is 'radar' palindrome?", is_palindrome("radar"))
print("Is 'Python' palindrome?", is_palindrome("Python"))
print("Is 'A man a plan a canal Panama' palindrome?", is_palindrome("A man a plan a canal Panama"))