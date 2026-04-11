
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
   
    def __exit__(self, exc_type, exc_value, traceback):
        import time
        self.end = time.time()
        print(f"Time taken: {self.end - self.start:.4f} seconds")
with Timer() as t:
    for i in range(1000000):
        pass