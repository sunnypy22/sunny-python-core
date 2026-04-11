
import asyncio
async def fetch_data(task_id):
    await asyncio.sleep(1)
    return f"Data from task {task_id}"
async def main():
    tasks = [fetch_data(i) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    print("Results:", results)
asyncio.run(main())
