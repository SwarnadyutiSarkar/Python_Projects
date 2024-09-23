import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog, messagebox
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

class PCVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("PCA Visualizer")

        self.data = None

        # Load Data Button
        self.load_button = Button(root, text="Load Dataset", command=self.load_data)
        self.load_button.pack(pady=10)

        # PCA Components
        self.components_var = IntVar(value=2)
        self.components_label = Label(root, text="Number of PCA Components:")
        self.components_label.pack(pady=5)

        self.components_entry = Entry(root, textvariable=self.components_var)
        self.components_entry.pack(pady=5)

        # Run PCA Button
        self.pca_button = Button(root, text="Run PCA", command=self.run_pca)
        self.pca_button.pack(pady=10)

        # Plot Button
        self.plot_button = Button(root, text="Plot Results", command=self.plot_results)
        self.plot_button.pack(pady=10)

        self.pca_result = None

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

    def run_pca(self):
        if self.data is None:
            messagebox.showwarning("Warning", "Please load a dataset first.")
            return

        # Standardize the data
        X = self.data.select_dtypes(include=[np.number])  # Select numerical columns
        X_scaled = StandardScaler().fit_transform(X)

        n_components = self.components_var.get()
        if n_components not in [2, 3]:
            messagebox.showwarning("Warning", "Please select either 2 or 3 components for PCA.")
            return

        # Perform PCA
        pca = PCA(n_components=n_components)
        self.pca_result = pca.fit_transform(X_scaled)
        messagebox.showinfo("Success", "PCA Computation Completed!")

    def plot_results(self):
        if self.pca_result is None:
            messagebox.showwarning("Warning", "Please run PCA first.")
            return

        n_components = self.components_var.get()
        plt.figure(figsize=(10, 6))

        if n_components == 2:
            plt.scatter(self.pca_result[:, 0], self.pca_result[:, 1])
            plt.title("PCA Result - 2D Plot")
            plt.xlabel("Principal Component 1")
            plt.ylabel("Principal Component 2")
        elif n_components == 3:
            ax = plt.axes(projection='3d')
            ax.scatter3D(self.pca_result[:, 0], self.pca_result[:, 1], self.pca_result[:, 2])
            ax.set_title("PCA Result - 3D Plot")
            ax.set_xlabel("Principal Component 1")
            ax.set_ylabel("Principal Component 2")
            ax.set_zlabel("Principal Component 3")

        plt.grid()
        plt.show()

if __name__ == "__main__":
    root = Tk()
    app = PCVisualizer(root)
    root.mainloop()
