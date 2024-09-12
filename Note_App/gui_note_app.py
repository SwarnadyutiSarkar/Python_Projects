import tkinter as tk
from tkinter import filedialog, messagebox

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note App")

        # Create a Text widget for writing notes
        self.text_area = tk.Text(root, wrap='word', font=('Arial', 12))
        self.text_area.pack(expand=1, fill='both')

        # Create a menu bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # Create File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', command=self.new_file)
        self.file_menu.add_command(label='Open', command=self.open_file)
        self.file_menu.add_command(label='Save', command=self.save_file)
        self.file_menu.add_command(label='Exit', command=root.quit)

        # Create Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Edit', menu=self.edit_menu)
        self.edit_menu.add_command(label='Undo', command=self.undo)
        self.edit_menu.add_command(label='Redo', command=self.redo)
        self.edit_menu.add_command(label='Cut', command=self.cut)
        self.edit_menu.add_command(label='Copy', command=self.copy)
        self.edit_menu.add_command(label='Paste', command=self.paste)

    def new_file(self):
        if self.text_area.get("1.0", tk.END).strip() != "":
            if messagebox.askyesno("Save", "Do you want to save changes?"):
                self.save_file()
        self.text_area.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get("1.0", tk.END))

    def undo(self):
        self.text_area.event_generate("<<Undo>>")

    def redo(self):
        self.text_area.event_generate("<<Redo>>")

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
