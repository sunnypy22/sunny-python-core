# 08_file_read_write.py
# Writing
with open("names.txt", "w") as f:
    f.write("Sunny\n")
    f.write("Rahul\n")
    f.write("Priya\n")
    f.write("Aarav\n")

# Appending
with open("names.txt", "a") as f:
    f.write("Neha\n")

# Reading
print("\nReading line by line:")
with open("names.txt", "r") as f:
    for line in f:
        print("→", line.strip())

# Read all at once
with open("names.txt", "r") as f:
        content = f.read()
        print("\nWhole content:\n" + content)