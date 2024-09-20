import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    filepath = filedialog.askopenfilename()
    if filepath:
        data = pd.read_csv(filepath)
        # Process and visualize data
        visualize_data(data)

def visualize_data(data):
    # Sample visualization
    data['Date'] = pd.to_datetime(data['Date'])
    sales_per_day = data.groupby('Date')['Sales'].sum()
    plt.figure(figsize=(10, 5))
    sales_per_day.plot(kind='bar')
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.show()

root = tk.Tk()
root.title("Sales Performance Tracker")

load_button = tk.Button(root, text="Load Sales Data", command=load_data)
load_button.pack()

root.mainloop()
