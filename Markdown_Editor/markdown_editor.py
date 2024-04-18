import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import markdown

class MarkdownEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Editor")

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

        # Create text area
        self.text_area = scrolledtext.ScrolledText(self.root, width=80, height=30)
        self.text_area.pack(padx=10, pady=10)

        # Create preview area
        self.preview_area = tk.Text(self.root, width=80, height=30)
        self.preview_area.pack(padx=10, pady=10)

        # Bind text area to update preview
        self.text_area.bind("<KeyRelease>", self.update_preview)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.preview_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md"), ("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.update_preview()

    def save_file(self):
        if not hasattr(self, "file_path") or not self.file_path:
            self.save_as_file()
        else:
            content = self.text_area.get(1.0, tk.END)
            with open(self.file_path, "w") as file:
                file.write(content)

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown Files", "*.md"), ("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)
            self.file_path = file_path

    def exit_app(self):
        self.root.quit()

    def update_preview(self, event=None):
        content = self.text_area.get(1.0, tk.END)
        html_content = markdown.markdown(content)
        self.preview_area.delete(1.0, tk.END)
        self.preview_area.insert(tk.END, html_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownEditor(root)
    root.mainloop()
