import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class QuizDashboard:
    def __init__(self, master):
        self.master = master
        master.title("Educational Quiz Performance Dashboard")

        self.scores = []
        self.quiz_names = []

        # Labels
        self.label = tk.Label(master, text="Enter Quiz Name and Score:")
        self.label.pack()

        # Quiz Name
        self.quiz_name_label = tk.Label(master, text="Quiz Name:")
        self.quiz_name_label.pack()
        self.quiz_name_entry = tk.Entry(master)
        self.quiz_name_entry.pack()

        # Quiz Score
        self.score_label = tk.Label(master, text="Score (out of 100):")
        self.score_label.pack()
        self.score_entry = tk.Entry(master)
        self.score_entry.pack()

        # Add Score Button
        self.add_score_button = tk.Button(master, text="Add Score", command=self.add_score)
        self.add_score_button.pack()

        # Show Performance Button
        self.show_performance_button = tk.Button(master, text="Show Performance", command=self.show_performance)
        self.show_performance_button.pack()

    def add_score(self):
        quiz_name = self.quiz_name_entry.get()
        score = self.score_entry.get()

        if quiz_name and score.isdigit() and 0 <= int(score) <= 100:
            self.quiz_names.append(quiz_name)
            self.scores.append(int(score))
            messagebox.showinfo("Success", f"Added {quiz_name} with score {score}.")
            self.quiz_name_entry.delete(0, tk.END)
            self.score_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid quiz name and score (0-100).")

    def show_performance(self):
        if not self.scores:
            messagebox.showwarning("No Data", "No scores to display.")
            return

        # Plotting the results
        plt.figure(figsize=(10, 5))
        plt.bar(self.quiz_names, self.scores, color='skyblue')
        plt.xlabel('Quizzes')
        plt.ylabel('Scores')
        plt.title('Quiz Performance Dashboard')
        plt.ylim(0, 100)
        plt.axhline(y=sum(self.scores) / len(self.scores), color='r', linestyle='--', label='Average Score')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = QuizDashboard(root)
    root.mainloop()
