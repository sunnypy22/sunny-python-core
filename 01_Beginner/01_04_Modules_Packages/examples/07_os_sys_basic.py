
# 07_os_sys_basic.py
import os
import sys
print("Current working directory:", os.getcwd())
print("Python version           :", sys.version)
print("Python path              :", sys.path[0])
# List files in current directory
print("\nFiles in current directory:")
for item in os.listdir():
    print("  ", item)