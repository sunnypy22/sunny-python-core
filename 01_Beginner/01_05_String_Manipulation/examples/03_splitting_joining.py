# 03_splitting_joining.py
sentence = "Python is awesome and powerful"
words = sentence.split()                    # split by whitespace
print("Split into words:", words)
csv_data = "Sunny,25,Pune,Student"
data = csv_data.split(",")
print("CSV split:", data)
# Joining
joined = " | ".join(words)
print("Joined with | :", joined)
numbers = ["1", "2", "3", "4"]
print("Numbers joined:", "-".join(numbers))