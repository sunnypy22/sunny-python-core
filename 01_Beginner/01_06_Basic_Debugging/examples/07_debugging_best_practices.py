# 07_debugging_best_practices.py
def calculate_grade(marks):
    """Calculate grade with proper debugging support"""
    print(f"DEBUG: Received marks = {marks}")
   
    if not isinstance(marks, (int, float)):
        raise TypeError(f"Marks must be number, got {type(marks)}")
   
    assert 0 <= marks <= 100, f"Marks {marks} out of valid range 0-100"
   
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "F"
   
    print(f"DEBUG: Calculated grade = {grade}")
    return grade
# Test
print(calculate_grade(85))
# print(calculate_grade(105))   # Will raise AssertionError