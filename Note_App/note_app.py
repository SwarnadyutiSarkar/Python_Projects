import tkinter as tk
from tkinter import messagebox, simpledialog

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Taking App")
        
        # Create a text area
        self.text_area = tk.Text(root, height=20, width=50)
        self.text_area.pack(pady=20)
        
        # Create buttons
        self.save_button = tk.Button(root, text="Save", command=self.save_note)
        self.save_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_note)
        self.delete_button.pack(side=tk.LEFT, padx=10)
        
        self.edit_button = tk.Button(root, text="Edit", command=self.edit_note)
        self.edit_button.pack(side=tk.LEFT, padx=10)
        
        self.view_button = tk.Button(root, text="View", command=self.view_note)
        self.view_button.pack(side=tk.LEFT, padx=10)
        
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(side=tk.RIGHT, padx=10)
        
    def save_note(self):
        note_content = self.text_area.get("1.0", tk.END)
        if not note_content.strip():
            messagebox.showwarning("Warning", "Note cannot be empty!")
            return
        file_name = simpledialog.askstring("Save Note", "Enter note name:")
        if file_name:
            try:
                with open(f"{file_name}.txt", "w") as file:
                    file.write(note_content)
                messagebox.showinfo("Success", "Note saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save note: {e}")
                
    def delete_note(self):
        file_name = simpledialog.askstring("Delete Note", "Enter note name to delete:")
        if file_name:
            try:
                import os
                os.remove(f"{file_name}.txt")
                messagebox.showinfo("Success", "Note deleted successfully!")
            except FileNotFoundError:
                messagebox.showwarning("Warning", "Note not found!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete note: {e}")
                
    def edit_note(self):
        file_name = simpledialog.askstring("Edit Note", "Enter note name to edit:")
        if file_name:
            try:
                with open(f"{file_name}.txt", "r") as file:
                    note_content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, note_content)
            except FileNotFoundError:
                messagebox.showwarning("Warning", "Note not found!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to edit note: {e}")
                
    def view_note(self):
        file_name = simpledialog.askstring("View Note", "Enter note name to view:")
        if file_name:
            try:
                with open(f"{file_name}.txt", "r") as file:
                    note_content = file.read()
                messagebox.showinfo(f"Note - {file_name}", note_content)
            except FileNotFoundError:
                messagebox.showwarning("Warning", "Note not found!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to view note: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
