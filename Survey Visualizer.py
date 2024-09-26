import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, filedialog
import os

class SurveyVisualizer:
    def __init__(self, master):
        self.master = master
        master.title("Survey Results Visualizer")

        self.label = Label(master, text="Upload your survey data CSV file:")
        self.label.pack()

        self.upload_button = Button(master, text="Upload CSV", command=self.upload_file)
        self.upload_button.pack()

        self.visualize_button = Button(master, text="Visualize Data", command=self.visualize_data)
        self.visualize_button.pack()
        self.visualize_button.config(state="disabled")  # Disable until a file is uploaded

        self.file_path = None

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if self.file_path:
            self.label.config(text=os.path.basename(self.file_path))
            self.visualize_button.config(state="normal")

    def visualize_data(self):
        # Read the CSV file
        data = pd.read_csv(self.file_path)

        # Check if the necessary columns are present
        if 'Rating' not in data.columns or 'Demographic' not in data.columns:
            self.label.config(text="Error: Ensure 'Rating' and 'Demographic' columns exist.")
            return
        
        # Create count plot for survey responses
        plt.figure(figsize=(10, 5))
        sns.countplot(data=data, x='Response')  # Adjust 'Response' according to your data
        plt.title('Survey Responses Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Create box plot for ratings
        plt.figure(figsize=(10, 5))
        sns.boxplot(data=data, x='Demographic', y='Rating')  # Adjust 'Demographic' and 'Rating'
        plt.title('Box Plot of Ratings by Demographic')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Create joint plot for comparisons
        if 'Age' in data.columns and 'Rating' in data.columns:  # Assuming Age is another demographic
            g = sns.jointplot(data=data, x='Age', y='Rating', kind='scatter')  # Adjust accordingly
            g.fig.suptitle('Joint Plot of Age vs Rating', y=1.02)
            plt.show()
        else:
            self.label.config(text="Warning: 'Age' column not found for joint plot.")

if __name__ == "__main__":
    root = Tk()
    app = SurveyVisualizer(root)
    root.mainloop()
