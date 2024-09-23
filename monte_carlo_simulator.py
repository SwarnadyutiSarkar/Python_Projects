import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

class MonteCarloSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Monte Carlo Simulator")

        # Parameters
        self.initial_price = DoubleVar(value=100.0)
        self.mu = DoubleVar(value=0.05)  # Expected return
        self.sigma = DoubleVar(value=0.2)  # Volatility
        self.days = IntVar(value=30)  # Number of days to simulate
        self.simulations = IntVar(value=1000)  # Number of simulations

        # Initial Price
        Label(root, text="Initial Stock Price:").pack(pady=5)
        Entry(root, textvariable=self.initial_price).pack(pady=5)

        # Expected Return
        Label(root, text="Expected Return (mu):").pack(pady=5)
        Entry(root, textvariable=self.mu).pack(pady=5)

        # Volatility
        Label(root, text="Volatility (sigma):").pack(pady=5)
        Entry(root, textvariable=self.sigma).pack(pady=5)

        # Days
        Label(root, text="Number of Days:").pack(pady=5)
        Entry(root, textvariable=self.days).pack(pady=5)

        # Simulations
        Label(root, text="Number of Simulations:").pack(pady=5)
        Entry(root, textvariable=self.simulations).pack(pady=5)

        # Run Simulation Button
        self.run_button = Button(root, text="Run Simulation", command=self.run_simulation)
        self.run_button.pack(pady=10)

    def run_simulation(self):
        S0 = self.initial_price.get()
        mu = self.mu.get()
        sigma = self.sigma.get()
        T = self.days.get()
        N = self.simulations.get()

        # Time steps
        dt = 1
        time_steps = np.arange(0, T, dt)
        results = np.zeros((N, T))

        # Run simulations
        for i in range(N):
            # Generate random price paths
            random_shocks = np.random.normal(loc=mu * dt, scale=sigma * np.sqrt(dt), size=T)
            price_path = S0 * np.exp(np.cumsum(random_shocks))
            results[i] = price_path

        # Plot results
        self.plot_results(time_steps, results)

    def plot_results(self, time_steps, results):
        plt.figure(figsize=(10, 6))
        plt.plot(time_steps, results.T, color='blue', alpha=0.1)
        plt.title("Monte Carlo Simulation of Stock Price")
        plt.xlabel("Days")
        plt.ylabel("Stock Price")
        plt.grid()
        plt.show()

if __name__ == "__main__":
    root = Tk()
    app = MonteCarloSimulator(root)
    root.mainloop()
