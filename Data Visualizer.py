import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, filedialog, StringVar, OptionMenu, Toplevel
import seaborn as sns

class DataVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Visualizer")
        self.filename = None

        self.label = Label(master, text="Load a CSV or Excel file:")
        self.label.pack()

        self.load_button = Button(master, text="Load Data", command=self.load_data)
        self.load_button.pack()

        self.data_info_label = Label(master, text="")
        self.data_info_label.pack()

        self.plot_button = Button(master, text="Visualize Data", command=self.visualize_data, state='disabled')
        self.plot_button.pack()

        self.plot_type_label = Label(master, text="Select Plot Type:")
        self.plot_type_label.pack()

        self.plot_type = StringVar(master)
        self.plot_type.set("Histogram")  # default value

        self.plot_options = OptionMenu(master, self.plot_type, "Histogram", "Scatter Plot", "Box Plot")
        self.plot_options.pack()

    def load_data(self):
        self.filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
        if self.filename:
            if self.filename.endswith('.csv'):
                self.data = pd.read_csv(self.filename)
            else:
                self.data = pd.read_excel(self.filename)
            
            self.data_info_label.config(text=f"Data Loaded: {self.filename}\nShape: {self.data.shape}")
            self.plot_button.config(state='normal')

    def visualize_data(self):
        plot_type = self.plot_type.get()
        if plot_type == "Histogram":
            self.plot_histogram()
        elif plot_type == "Scatter Plot":
            self.plot_scatter()
        elif plot_type == "Box Plot":
            self.plot_box()

    def plot_histogram(self):
        self.select_column_and_plot('histogram')

    def plot_scatter(self):
        if self.data.shape[1] < 2:
            self.data_info_label.config(text="Scatter plot requires at least 2 columns.")
            return
        x_col = self.data.columns[0]
        y_col = self.data.columns[1]
        self.plot_scatter_window(x_col, y_col)

    def plot_box(self):
        self.select_column_and_plot('box')

    def select_column_and_plot(self, plot_type):
        if self.data.empty:
            return
        columns = list(self.data.columns)
        if len(columns) == 0:
            return

        top = Toplevel(self.master)
        top.title(f"Select Column for {plot_type.capitalize()}")

        column_var = StringVar(top)
        column_var.set(columns[0])

        option_menu = OptionMenu(top, column_var, *columns)
        option_menu.pack()

        plot_button = Button(top, text=f"Plot {plot_type.capitalize()}", command=lambda: self.create_plot(column_var.get(), plot_type))
        plot_button.pack()

    def create_plot(self, column, plot_type):
        plt.figure()
        if plot_type == 'histogram':
            sns.histplot(self.data[column], bins=30, kde=True)
            plt.title(f"Histogram of {column}")
        elif plot_type == 'box':
            sns.boxplot(y=self.data[column])
            plt.title(f"Box Plot of {column}")
        plt.show()

    def plot_scatter_window(self, x_col, y_col):
        plt.figure()
        sns.scatterplot(data=self.data, x=x_col, y=y_col)
        plt.title(f"Scatter Plot of {x_col} vs {y_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()

if __name__ == "__main__":
    root = Tk()
    app = DataVisualizer(root)
    root.mainloop()
