import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

class ChatroomClient:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname:", parent=window)

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive_messages)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.window = tk.Tk()
        self.window.title("Chatroom")

        self.chat_area = scrolledtext.ScrolledText(self.window)
        self.chat_area.pack(pady=20, padx=20)

        self.input_area = tk.Text(self.window, height=3)
        self.input_area.pack(pady=20, padx=20)

        send_button = tk.Button(self.window, text="Send", command=self.send_message)
        send_button.pack(pady=20)

        self.gui_done = True
        self.window.mainloop()

    def send_message(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', tk.END)}"
        self.client.send(message.encode("utf-8"))
        self.input_area.delete("1.0", tk.END)

    def receive_messages(self):
        while self.running:
            try:
                message = self.client.recv(1024).decode("utf-8")
                if message == "NICK":
                    self.client.send(self.nickname.encode("utf-8"))
                else:
                    if self.gui_done:
                        self.chat_area.insert(tk.END, message)
                        self.chat_area.yview(tk.END)
            except:
                print("An error occurred!")
                self.client.close()
                break

if __name__ == "__main__":
    window = tk.Tk()
    window.withdraw()

    client = ChatroomClient("127.0.0.1", 55555)
