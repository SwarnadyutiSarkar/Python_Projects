import tkinter as tk
from tkinter import ttk, messagebox
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StockDashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-time Stock Market Dashboard")
        
        # Create and configure the main frame
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Stock ticker entry
        self.stock_label = ttk.Label(self.frame, text="Enter Stock Ticker:")
        self.stock_label.grid(row=0, column=0, padx=5, pady=5)

        self.stock_entry = ttk.Entry(self.frame)
        self.stock_entry.grid(row=0, column=1, padx=5, pady=5)

        # Fetch data button
        self.fetch_btn = ttk.Button(self.frame, text="Fetch Data", command=self.fetch_data)
        self.fetch_btn.grid(row=0, column=2, padx=5, pady=5)

        # Historical comparison
        self.compare_label = ttk.Label(self.frame, text="Compare with:")
        self.compare_label.grid(row=1, column=0, padx=5, pady=5)

        self.compare_entry = ttk.Entry(self.frame)
        self.compare_entry.grid(row=1, column=1, padx=5, pady=5)

        # Plot historical data button
        self.compare_btn = ttk.Button(self.frame, text="Compare", command=self.compare_data)
        self.compare_btn.grid(row=1, column=2, padx=5, pady=5)

        # Matplotlib Figure
        self.figure = plt.Figure(figsize=(8, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)

        # Canvas for Matplotlib
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=3)

    def fetch_data(self):
        ticker = self.stock_entry.get().strip()
        if not ticker:
            messagebox.showwarning("Input Error", "Please enter a stock ticker.")
            return

        try:
            data = yf.download(ticker, period='1d', interval='1m')
            if data.empty:
                raise ValueError("No data fetched. Please check the ticker symbol.")

            self.ax.clear()
            self.ax.plot(data.index, data['Close'], label=ticker)
            self.ax.set_title(f'Real-time Stock Price: {ticker}')
            self.ax.set_xlabel('Time')
            self.ax.set_ylabel('Price')
            self.ax.legend()
            self.ax.grid()
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def compare_data(self):
        ticker = self.stock_entry.get().strip()
        compare_ticker = self.compare_entry.get().strip()
        if not ticker or not compare_ticker:
            messagebox.showwarning("Input Error", "Please enter both stock tickers.")
            return

        try:
            data1 = yf.download(ticker, period='1mo', interval='1d')
            data2 = yf.download(compare_ticker, period='1mo', interval='1d')

            if data1.empty or data2.empty:
                raise ValueError("No data fetched. Please check the ticker symbols.")

            self.ax.clear()
            self.ax.plot(data1.index, data1['Close'], label=ticker)
            self.ax.plot(data2.index, data2['Close'], label=compare_ticker)
            self.ax.set_title(f'Comparison: {ticker} vs {compare_ticker}')
            self.ax.set_xlabel('Date')
            self.ax.set_ylabel('Price')
            self.ax.legend()
            self.ax.grid()
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = StockDashboardApp(root)
    root.mainloop()
