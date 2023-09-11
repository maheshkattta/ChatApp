import tkinter as tk
from tkinter import scrolledtext, filedialog

class ChatUI:
    def __init__(self, root, send_message_callback, send_multimedia_callback):
        self.root = root
        self.root.title("Chat Application")

        self.chat_text = scrolledtext.ScrolledText(self.root, state=tk.DISABLED)
        self.chat_text.pack(fill=tk.BOTH, expand=True)

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack(fill=tk.BOTH, expand=True)

        self.send_button = tk.Button(self.root, text="Send", command=send_message_callback)
        self.send_button.pack(fill=tk.BOTH, expand=True)

        self.send_multimedia_button = tk.Button(self.root, text="Send Multimedia", command=send_multimedia_callback)
        self.send_multimedia_button.pack(fill=tk.BOTH, expand=True)

    def get_input_text(self):
        return self.input_entry.get()

    def set_chat_text(self, text):
        self.chat_text.configure(state=tk.NORMAL)
        self.chat_text.insert(tk.END, text + '\n')
        self.chat_text.configure(state=tk.DISABLED)

    def clear_input_text(self):
        self.input_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

