import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cryptography.fernet import Fernet
import os

class EncryptionDecryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Encryption/Decryption Tool")

        # Create key
        self.key = Fernet.generate_key()

        # Create buttons
        self.encrypt_button = ttk.Button(root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack(pady=20)
        self.decrypt_button = ttk.Button(root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack(pady=20)

        # Create text widgets
        self.text_input = tk.Text(root, width=50, height=10)
        self.text_input.pack(pady=20)
        self.text_output = tk.Text(root, width=50, height=10, state=tk.DISABLED)
        self.text_output.pack(pady=20)

    def encrypt_text(self):
        text = self.text_input.get("1.0", tk.END).encode()
        cipher = Fernet(self.key)
        encrypted_text = cipher.encrypt(text)
        self.text_output.config(state=tk.NORMAL)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, encrypted_text.decode())
        self.text_output.config(state=tk.DISABLED)

    def decrypt_text(self):
        encrypted_text = self.text_input.get("1.0", tk.END).encode()
        cipher = Fernet(self.key)
        try:
            decrypted_text = cipher.decrypt(encrypted_text)
            self.text_output.config(state=tk.NORMAL)
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, decrypted_text.decode())
            self.text_output.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", "Invalid key or encrypted text!")

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionDecryptionTool(root)
    root.mainloop()
