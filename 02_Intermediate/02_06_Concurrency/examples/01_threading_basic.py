import threading
import time
def worker(name, delay):
    print(f"Thread {name} started")
    time.sleep(delay)
    print(f"Thread {name} finished after {delay} seconds")
# Create threads
t1 = threading.Thread(target=worker, args=("A", 2))
t2 = threading.Thread(target=worker, args=("B", 3))
t1.start()
t2.start()
t1.join()   # Wait for thread to finish
t2.join()
print("All threads completed")
