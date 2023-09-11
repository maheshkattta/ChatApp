import socket
import threading
from chat_ui import ChatUI
from multimedia_handler import MultimediaHandler

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("server_ip_address", 12345))  # Replace "server_ip_address" with the server's IP address

# Callback function for sending a message
def send_message():
    message = ui.get_input_text()
    if message:
        client_socket.send(message.encode())
        ui.clear_input_text()

# Callback function for sending multimedia
def send_multimedia():
    file_path = filedialog.askopenfilename()
    if file_path:
        multimedia_handler = MultimediaHandler(client_socket)
        multimedia_handler.send_image(file_path)

# Callback function for receiving multimedia
def receive_multimedia():
    multimedia_handler = MultimediaHandler(client_socket)
    while True:
        try:
            message = client_socket.recv(1024).decode()
            result = multimedia_handler.receive_image(message)
            if result:
                ui.set_chat_text(result)
        except:
            break

# Create a UI instance with callback functions
root = tk.Tk()
ui = ChatUI(root, send_message, send_multimedia)

# Create a thread for receiving multimedia
receive_multimedia_thread = threading.Thread(target=receive_multimedia)
receive_multimedia_thread.start()

# Start the UI
ui.run()

