
import multiprocessing
def producer(queue):
    for i in range(5):
        queue.put(f"Item {i}")

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print("Consumed:", item)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=producer, args=(q,))
    c = multiprocessing.Process(target=consumer, args=(q,))
   
    p.start()
    c.start()
    p.join()
    q.put(None)   # Signal consumer to stop
    c.join()