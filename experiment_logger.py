import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class ExperimentLogger:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Experiment Logger")

        self.data = []

        # Labels
        self.label = tk.Label(master, text="Input Experimental Data")
        self.label.pack()

        # Data Entry
        self.data_label = tk.Label(master, text="Data Point:")
        self.data_label.pack()
        self.data_entry = tk.Entry(master)
        self.data_entry.pack()

        # Add Data Button
        self.add_data_button = tk.Button(master, text="Add Data Point", command=self.add_data)
        self.add_data_button.pack()

        # Show Plots Button
        self.show_plots_button = tk.Button(master, text="Show Plots", command=self.show_plots)
        self.show_plots_button.pack()

    def add_data(self):
        data_point = self.data_entry.get()
        if data_point.replace('.', '', 1).isdigit():
            self.data.append(float(data_point))
            messagebox.showinfo("Success", f"Added data point: {data_point}.")
            self.data_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid number.")

    def show_plots(self):
        if not self.data:
            messagebox.showwarning("No Data", "No data points logged.")
            return

        # Convert data to numpy array for analysis
        data_array = np.array(self.data)

        # Create a figure for the plots
        plt.figure(figsize=(15, 5))

        # Scatter Plot
        plt.subplot(1, 3, 1)
        plt.scatter(range(len(data_array)), data_array, color='blue', alpha=0.7)
        plt.title('Scatter Plot')
        plt.xlabel('Index')
        plt.ylabel('Data Points')

        # Histogram
        plt.subplot(1, 3, 2)
        plt.hist(data_array, bins=10, color='green', alpha=0.7)
        plt.title('Histogram')
        plt.xlabel('Data Points')
        plt.ylabel('Frequency')

        # Box Plot
        plt.subplot(1, 3, 3)
        plt.boxplot(data_array, vert=True, patch_artist=True)
        plt.title('Box Plot')
        plt.ylabel('Data Points')

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    experiment_logger = ExperimentLogger(root)
    root.mainloop()
