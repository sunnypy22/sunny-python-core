# 01_print_debugging.py # Simple print debugging example

def calculate_average(numbers):
        print(f"Debug: Received list = {numbers}")
        total = 0
        for num in numbers:
            print(f"Debug: Adding {num}")
            total += num
            avg = total / len(numbers)
            print(f"Debug: Total = {total}, Count = {len(numbers)}, Average = {avg}")
            return avg
result = calculate_average([10, 20, 30, 40])
print("Final Result:", result)
