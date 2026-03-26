# 05_string_validation.py
def validate_string(s):
    print(f"String: '{s}'")
    print("Is alphabetic:", s.isalpha())
    print("Is numeric:", s.isdigit())
    print("Is alphanumeric:", s.isalnum())
    print("Is title case:", s.istitle())
    print("Is uppercase:", s.isupper())
    print("-" * 40)
validate_string("Sunny")
validate_string("12345")
validate_string("Python3")
validate_string("HELLO")