import socket
import platform

def get_client_ip(client_socket):
    client_ip = client_socket.getpeername()[0]
    return client_ip

def get_system_info():
    system_info = platform.uname()

    # formats the system info into a string
    return f"System: {system_info.system}\nNode Name: {system_info.node}\nRelease: {system_info.release}\nVersion: {system_info.version}\nMachine: {system_info.machine}\nProcessor: {system_info.processor}"

def handle_client(client_socket):
    while True:
        command = input("Enter command (get_ip, system_info, custom_command, exit): ").strip()
        client_socket.send(command.encode())
        if command.lower() == "exit":
            # breaks out of the while loop
            break

        elif command.lower() == "get_ip":
            # gets the client IP
            client_ip = get_client_ip(client_socket)
            print("Client IP:", client_ip)
            client_socket.send(("Client IP: " + client_ip).encode())


        elif command.lower() == "system_info":
            # gets the system info
            info = get_system_info()
            print("System Info:\n", info)
            client_socket.send(info.encode())


        elif command.lower() == "custom_command":
            # enables the use of several commands such as "dir", "tasklist" and "ipconfig"
            custom_command = input("Enter custom command to execute on client: ").strip()
            client_socket.send(custom_command.encode())
            response = client_socket.recv(4096).decode()
            print("Response from client:", response)
        else:
            response = client_socket.recv(4096).decode()
            print("Response from client:", response)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## IMPORTANT SERVER IP & ADDRESS BELOW ##
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print("Connected to client:", client_address)
        handle_client(client_socket)
        client_socket.close()

if __name__ == "__main__":
    main()
