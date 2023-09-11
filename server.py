import socket
import threading

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))  # Listen on all available network interfaces
server_socket.listen(5)  # Listen for up to 5 incoming connections

# List to store client sockets
client_sockets = []

def broadcast(message, sender_socket):
    for client_socket in client_sockets:
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except:
                # Remove the broken socket
                client_sockets.remove(client_socket)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            # Remove the disconnected client
            client_sockets.remove(client_socket)
            client_socket.close()
            break

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    client_sockets.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

