import os

class MultimediaHandler:
    def __init__(self, client_socket):
        self.client_socket = client_socket

    def send_image(self, image_path):
        file_name = os.path.basename(image_path)
        with open(image_path, 'rb') as file:
            data = file.read()
            self.client_socket.sendall(f"image {file_name}".encode())
            self.client_socket.send(data)

    def receive_image(self, message):
        parts = message.split()
        if len(parts) == 2 and parts[0] == "image":
            file_name = parts[1]
            data = self.client_socket.recv(1024)
            with open(file_name, 'wb') as file:
                file.write(data)
                return f"Received image: {file_name}"

