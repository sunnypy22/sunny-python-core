# 12_defaultdict.py
from collections import defaultdict
# Normal dict → KeyError on missing key
# d = {}
# d["python"] += 1   # error
dd = defaultdict(int)           # default value = 0
words = "apple banana apple cherry banana apple"
for word in words.split():
    dd[word] += 1
print("Word counts:", dict(dd))
# Default list
groups = defaultdict(list)
for name, group in [("Sunny", "A"), ("Rahul", "B"), ("Priya", "A")]:
    groups[group].append(name)
print("Groups:", dict(groups))