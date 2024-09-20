import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

class ImageDataAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Data Analyzer")

        # Create and configure the main frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Upload button
        self.upload_btn = tk.Button(self.frame, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=10)

        # Label to display the image
        self.image_label = tk.Label(self.frame)
        self.image_label.pack(pady=10)

        # Button to plot histogram
        self.hist_btn = tk.Button(self.frame, text="Show Histogram", command=self.show_histogram)
        self.hist_btn.pack(pady=10)

        self.image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if not file_path:
            return
        
        try:
            self.image = Image.open(file_path)
            self.display_image(self.image)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")

    def display_image(self, img):
        # Resize image for display
        img = img.resize((300, 300), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk  # Keep a reference

    def show_histogram(self):
        if self.image is None:
            messagebox.showwarning("Warning", "Please upload an image first!")
            return

        # Convert image to numpy array
        img_array = np.array(self.image)

        # Plot histogram for each color channel
        colors = ('red', 'green', 'blue')
        plt.figure(figsize=(12, 6))

        for i, color in enumerate(colors):
            hist, bins = np.histogram(img_array[:, :, i], bins=256, range=(0, 255))
            plt.plot(bins[:-1], hist, color=color)

        plt.title('Color Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.xlim([0, 255])
        plt.legend(colors)
        plt.grid()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDataAnalyzerApp(root)
    root.mainloop()
