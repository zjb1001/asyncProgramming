
import asyncio
import json

async def get_weather_data(city):
    """Simulate async weather API call with delay"""
    await asyncio.sleep(2)  # Simulate network delay without blocking
    return {
        "city": city,
        "temperature": 20,
        "conditions": "sunny"
    }

async def handle_client(reader, writer):
    """Handle a single client request asynchronously"""
    # Read client request
    data = await reader.read(1024)
    city = json.loads(data.decode())["city"]
    
    # Get weather data (non-blocking operation)
    weather = await get_weather_data(city)
    
    # Send response
    writer.write(json.dumps(weather).encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def run_weather_server():
    server = await asyncio.start_server(
        handle_client,
        'localhost',
        8000
    )
    print("Async weather server started on port 8000")
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(run_weather_server())