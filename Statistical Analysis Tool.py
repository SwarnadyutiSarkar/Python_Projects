import numpy as np
from tkinter import Tk, Label, Button, Entry, Text, END, messagebox

class StatisticalAnalysisTool:
    def __init__(self, master):
        self.master = master
        self.master.title("Statistical Analysis Tool")

        self.label = Label(master, text="Enter numerical data (comma separated):")
        self.label.pack()

        self.data_entry = Entry(master, width=50)
        self.data_entry.pack()

        self.mean_button = Button(master, text="Calculate Mean", command=self.calculate_mean)
        self.mean_button.pack()

        self.median_button = Button(master, text="Calculate Median", command=self.calculate_median)
        self.median_button.pack()

        self.std_button = Button(master, text="Calculate Standard Deviation", command=self.calculate_std)
        self.std_button.pack()

        self.corr_button = Button(master, text="Calculate Correlation", command=self.calculate_correlation)
        self.corr_button.pack()

        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()

    def get_data(self):
        try:
            data = np.array([float(x) for x in self.data_entry.get().split(',')])
            return data
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical data.")
            return None

    def calculate_mean(self):
        data = self.get_data()
        if data is not None:
            mean_value = np.mean(data)
            self.display_result(f"Mean: {mean_value:.2f}")

    def calculate_median(self):
        data = self.get_data()
        if data is not None:
            median_value = np.median(data)
            self.display_result(f"Median: {median_value:.2f}")

    def calculate_std(self):
        data = self.get_data()
        if data is not None:
            std_value = np.std(data)
            self.display_result(f"Standard Deviation: {std_value:.2f}")

    def calculate_correlation(self):
        data = self.get_data()
        if data is not None:
            if len(data) < 2:
                messagebox.showerror("Input Error", "Need at least two data points for correlation.")
                return
            correlation_matrix = np.corrcoef(data)
            self.display_result(f"Correlation Matrix:\n{correlation_matrix}")

    def display_result(self, result):
        self.result_text.delete(1.0, END)
        self.result_text.insert(END, result)

if __name__ == "__main__":
    root = Tk()
    app = StatisticalAnalysisTool(root)
    root.mainloop()
