import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Gallery")

        # Create buttons
        self.open_button = ttk.Button(root, text="Open Image", command=self.open_image)
        self.open_button.pack(pady=20)

        self.prev_button = ttk.Button(root, text="Previous", command=self.prev_image)
        self.prev_button.pack(side="left", padx=20)

        self.next_button = ttk.Button(root, text="Next", command=self.next_image)
        self.next_button.pack(side="right", padx=20)

        # Create label to display image
        self.image_label = ttk.Label(root)
        self.image_label.pack(pady=20)

        # Initialize variables
        self.image_paths = []
        self.current_index = 0

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        
        if file_path:
            self.image_paths.append(file_path)
            self.current_index = len(self.image_paths) - 1
            self.display_image()

    def display_image(self):
        try:
            image = Image.open(self.image_paths[self.current_index])
            image = image.resize((300, 300), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")

    def prev_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_image()

    def next_image(self):
        if self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGallery(root)
    root.mainloop()
