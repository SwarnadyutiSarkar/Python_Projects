import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")

        # Create buttons
        self.open_button = tk.Button(root, text="Open Directory", command=self.open_directory)
        self.open_button.pack(pady=20)

        self.listbox = tk.Listbox(root, width=100, height=20)
        self.listbox.pack(pady=20)

        self.delete_button = tk.Button(root, text="Delete File", command=self.delete_file)
        self.delete_button.pack(pady=10)

        self.rename_button = tk.Button(root, text="Rename File", command=self.rename_file)
        self.rename_button.pack(pady=10)

        self.copy_button = tk.Button(root, text="Copy File", command=self.copy_file)
        self.copy_button.pack(pady=10)

        self.move_button = tk.Button(root, text="Move File", command=self.move_file)
        self.move_button.pack(pady=10)

        self.refresh_button = tk.Button(root, text="Refresh", command=self.refresh_list)
        self.refresh_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=20)

    def open_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.current_directory = directory
            self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        try:
            files = os.listdir(self.current_directory)
            for file in files:
                self.listbox.insert(tk.END, file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to list directory contents: {e}")

    def get_selected_file(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            selected_index = int(selected_indices[0])
            selected_file = self.listbox.get(selected_index)
            return os.path.join(self.current_directory, selected_file)
        else:
            messagebox.showwarning("Warning", "No file selected!")
            return None

    def delete_file(self):
        file_path = self.get_selected_file()
        if file_path:
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
                self.refresh_list()
                messagebox.showinfo("Success", "File deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete file: {e}")

    def rename_file(self):
        file_path = self.get_selected_file()
        if file_path:
            new_name = simpledialog.askstring("Rename File", "Enter new file name:")
            if new_name:
                try:
                    os.rename(file_path, os.path.join(self.current_directory, new_name))
                    self.refresh_list()
                    messagebox.showinfo("Success", "File renamed successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to rename file: {e}")

    def copy_file(self):
        file_path = self.get_selected_file()
        if file_path:
            destination = filedialog.askdirectory()
            if destination:
                try:
                    shutil.copy2(file_path, destination)
                    messagebox.showinfo("Success", "File copied successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to copy file: {e}")

    def move_file(self):
        file_path = self.get_selected_file()
        if file_path:
            destination = filedialog.askdirectory()
            if destination:
                try:
                    shutil.move(file_path, destination)
                    self.refresh_list()
                    messagebox.showinfo("Success", "File moved successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to move file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorer(root)
    root.mainloop()
