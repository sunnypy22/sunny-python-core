# Read "numbers.txt" (assume one number per line), sum valid numbers, ignore invalid lines.
# Exercise 14 - Safe file reading + error handling
total = 0
count = 0
try:
    with open("numbers.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                num = float(line)
                total += num
                count += 1
            except ValueError:
                print(f"Skipping invalid line: {line}")
except FileNotFoundError:
    print("Error: numbers.txt not found.")
    exit(1)
if count > 0:
    print(f"\nSum of {count} valid numbers: {total}")
    print(f"Average: {total / count:.2f}")
else:
    print("No valid numbers found.")