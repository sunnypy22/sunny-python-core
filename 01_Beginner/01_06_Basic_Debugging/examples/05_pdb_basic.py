# 05_pdb_basic.py
# Basic usage of Python Debugger (pdb)
import pdb
def add_numbers(a, b):
    pdb.set_trace()        # Breakpoint here
    result = a + b
    return result
print("Starting calculation...")
sum_result = add_numbers(15, 25)
print("Sum is:", sum_result)