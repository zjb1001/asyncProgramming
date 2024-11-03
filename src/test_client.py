
import asyncio
import json
import time

async def test_client(city):
    """Async test client that connects to the weather service"""
    reader, writer = await asyncio.open_connection('localhost', 8000)
    
    writer.write(json.dumps({"city": city}).encode())
    await writer.drain()
    
    response = await reader.read(1024)
    print(f"Received weather for {city}: {response.decode()}")
    
    writer.close()
    await writer.wait_closed()

async def run_multiple_clients():
    """Run multiple clients concurrently to demonstrate async benefits"""
    cities = ["London", "Paris", "New York", "Tokyo", "Berlin"]
    start_time = time.time()
    
    # Create tasks for all clients to run concurrently
    tasks = [test_client(city) for city in cities]
    await asyncio.gather(*tasks)
    
    total_time = time.time() - start_time
    print(f"\nProcessed {len(cities)} requests in {total_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(run_multiple_clients())