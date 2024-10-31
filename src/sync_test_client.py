import socket
import json
import time

def test_client(city):
    """Test client that connects to the weather service"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8000))
    client.send(json.dumps({"city": city}).encode())
    response = client.recv(1024).decode()
    print(f"Received weather for {city}: {response}")
    client.close()

if __name__ == "__main__":
    # Start multiple clients to demonstrate synchronous blocking behavior
    cities = ["London", "Paris", "New York", "Tokyo", "Berlin"]
    start_time = time.time()
    
    # Run clients sequentially to show blocking behavior
    for city in cities:
        test_client(city)
    
    total_time = time.time() - start_time
    print(f"\nProcessed {len(cities)} requests in {total_time:.2f} seconds")