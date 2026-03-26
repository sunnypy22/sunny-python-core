# 03_assert_example.py
def set_age(age):
    assert age >= 0, f"Age cannot be negative! Got {age}"
    assert isinstance(age, int), "Age must be an integer"
    print(f"Age set to: {age}")
set_age(25)
# set_age(-5)   # This will raise AssertionError