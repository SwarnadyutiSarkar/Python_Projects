import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from cryptography.fernet import Fernet
import json
import os

class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")

        # Generate or load encryption key
        if not os.path.exists("key.key"):
            self.generate_key()
        self.load_key()

        # Create buttons
        self.add_button = ttk.Button(root, text="Add Password", command=self.add_password)
        self.add_button.pack(pady=20)

        self.retrieve_button = ttk.Button(root, text="Retrieve Password", command=self.retrieve_password)
        self.retrieve_button.pack(pady=10)

    def generate_key(self):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        with open("key.key", "rb") as key_file:
            self.key = key_file.read()
        self.cipher = Fernet(self.key)

    def encrypt_password(self, password):
        encrypted_password = self.cipher.encrypt(password.encode())
        return encrypted_password.decode()

    def decrypt_password(self, encrypted_password):
        decrypted_password = self.cipher.decrypt(encrypted_password.encode())
        return decrypted_password.decode()

    def add_password(self):
        website = simpledialog.askstring("Add Password", "Enter website:")
        username = simpledialog.askstring("Add Password", "Enter username:")
        password = simpledialog.askstring("Add Password", "Enter password:")

        if website and username and password:
            encrypted_password = self.encrypt_password(password)
            data = {website: {"username": username, "password": encrypted_password}}

            if os.path.exists("passwords.json"):
                with open("passwords.json", "r") as file:
                    passwords = json.load(file)
                passwords.update(data)
            else:
                passwords = data

            with open("passwords.json", "w") as file:
                json.dump(passwords, file)

            messagebox.showinfo("Info", "Password added successfully!")

    def retrieve_password(self):
        website = simpledialog.askstring("Retrieve Password", "Enter website:")
        if website:
            if os.path.exists("passwords.json"):
                with open("passwords.json", "r") as file:
                    passwords = json.load(file)

                if website in passwords:
                    username = passwords[website]["username"]
                    encrypted_password = passwords[website]["password"]
                    decrypted_password = self.decrypt_password(encrypted_password)
                    messagebox.showinfo("Info", f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}")
                else:
                    messagebox.showwarning("Warning", "Password not found!")
            else:
                messagebox.showwarning("Warning", "No passwords stored!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()
