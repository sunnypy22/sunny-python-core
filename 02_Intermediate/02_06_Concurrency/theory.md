# Threading, Multiprocessing & Asyncio in Python
**Definition**: These are Python's three main approaches to achieve **concurrency** and **parallelism** — running multiple tasks efficiently.
## 1. Threading (Thread-based Concurrency)
- Uses **threads** (lightweight subprocesses)
- Good for **I/O-bound** tasks (waiting for network, file, database, etc.)
- Threads share memory (GIL limitation for CPU-bound tasks)
- Global Interpreter Lock (GIL) prevents true parallelism in CPU-bound code
**Module**: `threading`
## 2. Multiprocessing (Process-based Parallelism)
- Uses separate **processes** with their own memory space
- Bypasses GIL → true parallelism on multi-core CPUs
- Best for **CPU-bound** tasks (computations, data processing, ML, etc.)
- Higher memory and startup overhead
**Module**: `multiprocessing`
## 3. Asyncio (Asynchronous Programming)
- Single-threaded concurrency using **co-routines**
- Best for **I/O-bound** tasks with high concurrency (web scraping, APIs, servers)
- Uses `async`/`await` syntax
- Extremely efficient for thousands of concurrent connections
**Module**: `asyncio`
### Comparison Table
| Feature              | Threading              | Multiprocessing         | Asyncio                  |
|----------------------|------------------------|-------------------------|--------------------------|
| Best for             | I/O-bound              | CPU-bound               | High I/O concurrency     |
| Memory Overhead      | Low                    | High                    | Very Low                 |
| GIL Impact           | Affected               | Not affected            | Not affected (single thread) |
| Difficulty           | Medium                 | Medium-High             | High (async mindset)     |
| Use Case             | File download, APIs    | Image processing, ML    | Web servers, scraping    |
