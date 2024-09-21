import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import datetime

class FitnessTracker:
    def __init__(self, master):
        self.master = master
        master.title("Fitness Tracker")

        self.dates = []
        self.distances = []
        self.calories = []

        # Labels
        self.label = tk.Label(master, text="Log Your Workout")
        self.label.pack()

        # Date
        self.date_label = tk.Label(master, text="Date (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(master)
        self.date_entry.pack()

        # Distance
        self.distance_label = tk.Label(master, text="Distance (km):")
        self.distance_label.pack()
        self.distance_entry = tk.Entry(master)
        self.distance_entry.pack()

        # Calories
        self.calories_label = tk.Label(master, text="Calories Burned:")
        self.calories_label.pack()
        self.calories_entry = tk.Entry(master)
        self.calories_entry.pack()

        # Add Workout Button
        self.add_workout_button = tk.Button(master, text="Add Workout", command=self.add_workout)
        self.add_workout_button.pack()

        # Show Progress Button
        self.show_progress_button = tk.Button(master, text="Show Progress", command=self.show_progress)
        self.show_progress_button.pack()

    def add_workout(self):
        date_str = self.date_entry.get()
        distance = self.distance_entry.get()
        calories = self.calories_entry.get()

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            distance = float(distance)
            calories = int(calories)

            self.dates.append(date)
            self.distances.append(distance)
            self.calories.append(calories)

            messagebox.showinfo("Success", f"Added workout on {date_str} with {distance} km and {calories} calories.")
            self.date_entry.delete(0, tk.END)
            self.distance_entry.delete(0, tk.END)
            self.calories_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")

    def show_progress(self):
        if not self.dates:
            messagebox.showwarning("No Data", "No workouts logged.")
            return

        # Plotting the progress
        fig, ax1 = plt.subplots(figsize=(10, 5))

        ax2 = ax1.twinx()
        ax1.plot(self.dates, self.distances, 'g-', marker='o', label='Distance (km)')
        ax2.plot(self.dates, self.calories, 'b-', marker='x', label='Calories Burned')

        ax1.set_xlabel('Date')
        ax1.set_ylabel('Distance (km)', color='g')
        ax2.set_ylabel('Calories Burned', color='b')

        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        plt.title('Workout Progress Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    fitness_tracker = FitnessTracker(root)
    root.mainloop()
