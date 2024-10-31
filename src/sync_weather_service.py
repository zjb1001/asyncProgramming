import socket
import time
import json

def get_weather_data(city):
    """Simulate weather API call with delay"""
    time.sleep(2)  # Simulate network delay
    return {
        "city": city,
        "temperature": 20,
        "conditions": "sunny"
    }

def handle_client(client_socket):
    """Handle a single client request"""
    # Read client request
    data = client_socket.recv(1024).decode()
    city = json.loads(data)["city"]
    
    # Get weather data (blocking operation)
    weather = get_weather_data(city)
    
    # Send response
    client_socket.send(json.dumps(weather).encode())
    client_socket.close()

def run_weather_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8000))
    server.listen(5)
    print("Weather server started on port 8000")
    
    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr}")
        handle_client(client)  # Blocking call

if __name__ == "__main__":
    run_weather_server()