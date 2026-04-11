
import asyncio
async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello {name} after {delay} seconds")
async def main():
    await asyncio.gather(
        say_hello("Sunny", 1),
        say_hello("Priya", 2),
        say_hello("Rahul", 1.5)
    )
if __name__ == "__main__":
    asyncio.run(main())
