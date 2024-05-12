import socket
import threading

# Function to handle incoming connections from other peers
def handle_connection(client_socket, client_address):
    print(f"Connected to {client_address}")
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received message from {client_address}: {data}")
        # Echo the received message back to the client
        client_socket.sendall(data.encode())
    # print(f"Disconnected from {client_address}")
    client_socket.close()

# Function to start the server
def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    print(f"Server started, listening for connections on port {port}...")
    while True:
        client_socket, client_address = server_socket.accept()
        # Start a new thread to handle the incoming connection
        client_thread = threading.Thread(target=handle_connection, args=(client_socket, client_address))
        client_thread.start()

# Start the server on a separate thread
server_thread = threading.Thread(target=start_server, args=(5001,))
server_thread.start()

# Function to send a message to another peer
def send_message(peer_ip, peer_port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((peer_ip, peer_port))
    client_socket.sendall(message.encode())
    response = client_socket.recv(1024).decode()
    # print(f"Received response: {response}")
    client_socket.close()

# Function to handle the discovery message and respond with IP address
def handle_discovery():
    discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    discovery_socket.bind(('localhost', 5002))
    while True:
        data, addr = discovery_socket.recvfrom(1024)
        if data == b"DISCOVER":
            print("Discovery message received, responding...")
            discovery_socket.sendto(b"DISCOVERED", addr)

# Start the discovery process on a separate thread
discovery_thread = threading.Thread(target=handle_discovery)
discovery_thread.start()

# Connect to the other peer and send custom messages
while True:
    message = input("Enter your message: ")
    send_message('localhost', 5000, message)
