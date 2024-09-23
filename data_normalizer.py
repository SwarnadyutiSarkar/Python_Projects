import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog, messagebox

class DataNormalizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Normalizer")

        self.data = None

        # Load Data Button
        self.load_button = Button(root, text="Load Dataset", command=self.load_data)
        self.load_button.pack(pady=10)

        # Normalization Technique
        self.technique_var = StringVar(value="Min-Max Normalization")
        self.technique_label = Label(root, text="Select Normalization Technique:")
        self.technique_label.pack(pady=5)
        
        self.technique_menu = OptionMenu(root, self.technique_var,
                                          "Min-Max Normalization",
                                          "Z-Score Standardization",
                                          "Robust Scaling")
        self.technique_menu.pack(pady=5)

        # Normalize Button
        self.normalize_button = Button(root, text="Normalize Data", command=self.normalize_data)
        self.normalize_button.pack(pady=10)

        # Visualization Button
        self.visualize_button = Button(root, text="Visualize Data", command=self.visualize_data)
        self.visualize_button.pack(pady=10)

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    self.data = pd.read_csv(file_path)
                else:
                    self.data = pd.read_excel(file_path)
                messagebox.showinfo("Success", "Data Loaded Successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load data: {str(e)}")

    def normalize_data(self):
        if self.data is None:
            messagebox.showwarning("Warning", "Please load a dataset first.")
            return
        
        technique = self.technique_var.get()
        
        if technique == "Min-Max Normalization":
            self.data_normalized = (self.data - self.data.min()) / (self.data.max() - self.data.min())
        elif technique == "Z-Score Standardization":
            self.data_normalized = (self.data - self.data.mean()) / self.data.std()
        elif technique == "Robust Scaling":
            self.data_normalized = (self.data - self.data.median()) / (self.data.quantile(0.75) - self.data.quantile(0.25))
        
        messagebox.showinfo("Success", "Data Normalized Successfully!")

    def visualize_data(self):
        if self.data_normalized is None:
            messagebox.showwarning("Warning", "Please normalize the data first.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.boxplot(self.data_normalized.values, labels=self.data.columns)
        plt.title("Normalized Data Visualization")
        plt.ylabel("Normalized Values")
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()

if __name__ == "__main__":
    root = Tk()
    app = DataNormalizer(root)
    root.mainloop()
