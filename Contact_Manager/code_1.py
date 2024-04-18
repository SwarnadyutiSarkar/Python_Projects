import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

# Initialize SQLite database
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                  (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)''')
conn.commit()

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # Create labels and entries
        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Phone:").grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(root, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        # Create buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if not name.strip() or not phone.strip():
            messagebox.showwarning("Warning", "Name and phone number are required!")
            return

        try:
            cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
            conn.commit()
            messagebox.showinfo("Success", "Contact added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add contact: {e}")

    def view_contacts(self):
        try:
            cursor.execute("SELECT * FROM contacts")
            contacts = cursor.fetchall()

            if not contacts:
                messagebox.showinfo("Info", "No contacts found!")
                return

            contact_list = "\n".join([f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}" for contact in contacts])
            messagebox.showinfo("Contacts", contact_list)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch contacts: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
