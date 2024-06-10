import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor App")
        self.image = None
        self.edited_image = None
        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.create_menu()
        self.create_toolbar()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        open_button = ttk.Button(toolbar, text="Open", command=self.open_image)
        open_button.pack(side=tk.LEFT, padx=2, pady=2)

        save_button = ttk.Button(toolbar, text="Save", command=self.save_image)
        save_button.pack(side=tk.LEFT, padx=2, pady=2)

        rotate_button = ttk.Button(toolbar, text="Rotate", command=self.rotate_image)
        rotate_button.pack(side=tk.LEFT, padx=2, pady=2)

        resize_button = ttk.Button(toolbar, text="Resize", command=self.resize_image)
        resize_button.pack(side=tk.LEFT, padx=2, pady=2)

        filter_button = ttk.Button(toolbar, text="Apply Filter", command=self.apply_filter)
        filter_button.pack(side=tk.LEFT, padx=2, pady=2)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def save_image(self):
        if self.edited_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                self.edited_image.save(file_path)
                messagebox.showinfo("Image Editor", "Image saved successfully!")
        else:
            messagebox.showerror("Image Editor", "No edited image to save!")

    def display_image(self, image):
        self.edited_image = image
        tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image

    def rotate_image(self):
        if self.image:
            self.image = self.image.rotate(90, expand=True)
            self.display_image(self.image)

    def resize_image(self):
        if self.image:
            new_width = 300
            new_height = 300
            self.image = self.image.resize((new_width, new_height))
            self.display_image(self.image)

    def apply_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)
            self.display_image(self.image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
