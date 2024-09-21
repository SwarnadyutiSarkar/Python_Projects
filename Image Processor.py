import numpy as np
from tkinter import Tk, Label, Button, filedialog, Text, END
from PIL import Image, ImageTk
import cv2
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processor")

        self.label = Label(master, text="Load an image:")
        self.label.pack()

        self.load_button = Button(master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.gray_button = Button(master, text="Convert to Grayscale", command=self.convert_to_grayscale, state='disabled')
        self.gray_button.pack()

        self.blur_button = Button(master, text="Apply Gaussian Blur", command=self.apply_blur, state='disabled')
        self.blur_button.pack()

        self.edge_button = Button(master, text="Apply Edge Detection", command=self.apply_edge_detection, state='disabled')
        self.edge_button.pack()

        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()

        self.image_path = None
        self.image = None

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if self.image_path:
            self.image = cv2.imread(self.image_path)
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, f"Loaded Image: {self.image_path}\n")
            self.gray_button.config(state='normal')
            self.blur_button.config(state='normal')
            self.edge_button.config(state='normal')

    def convert_to_grayscale(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.show_image(gray_image, "Grayscale Image")

    def apply_blur(self):
        blurred_image = cv2.GaussianBlur(self.image, (15, 15), 0)
        self.show_image(blurred_image, "Blurred Image")

    def apply_edge_detection(self):
        edges = cv2.Canny(self.image, 100, 200)
        self.show_image(edges, "Edge Detected Image")

    def show_image(self, image, title):
        plt.figure(title)
        if len(image.shape) == 2:  # Grayscale image
            plt.imshow(image, cmap='gray')
        else:  # Color image
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.title(title)
        plt.show()

if __name__ == "__main__":
    root = Tk()
    app = ImageProcessor(root)
    root.mainloop()
