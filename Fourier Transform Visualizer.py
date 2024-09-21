import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, Text, END, messagebox

class FourierTransformVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Fourier Transform Visualizer")

        self.label = Label(master, text="Enter time-domain signal (comma separated):")
        self.label.pack()

        self.signal_entry = Entry(master, width=50)
        self.signal_entry.pack()

        self.transform_button = Button(master, text="Perform Fourier Transform", command=self.perform_fourier_transform)
        self.transform_button.pack()

        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()

    def get_signal(self):
        try:
            signal = np.array([float(x) for x in self.signal_entry.get().split(',')])
            return signal
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical data.")
            return None

    def perform_fourier_transform(self):
        signal = self.get_signal()
        if signal is not None:
            # Perform Fourier Transform
            fft_result = np.fft.fft(signal)
            freq = np.fft.fftfreq(len(signal))

            # Display results
            self.display_results(freq, fft_result)
            self.plot_results(freq, fft_result)

    def display_results(self, freq, fft_result):
        self.result_text.delete(1.0, END)
        result_str = "Frequency Components:\n"
        for f, amplitude in zip(freq, np.abs(fft_result)):
            result_str += f"Frequency: {f:.2f} Hz, Amplitude: {amplitude:.2f}\n"
        self.result_text.insert(END, result_str)

    def plot_results(self, freq, fft_result):
        plt.figure(figsize=(10, 5))

        # Plot amplitude spectrum
        plt.subplot(1, 2, 1)
        plt.plot(freq, np.abs(fft_result))
        plt.title('Amplitude Spectrum')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude')
        plt.grid()

        # Plot phase spectrum
        plt.subplot(1, 2, 2)
        plt.plot(freq, np.angle(fft_result))
        plt.title('Phase Spectrum')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Phase (radians)')
        plt.grid()

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = Tk()
    app = FourierTransformVisualizer(root)
    root.mainloop()
