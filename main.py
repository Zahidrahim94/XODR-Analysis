import tkinter as tk
from tkinter import filedialog
import processing
import visualization

def process_file():
    file_path = filedialog.askopenfilename(title="Select XODR File", filetypes=(("XODR files", "*.xodr"), ("All files", "*.*")))
    if file_path:
        object_counts, signal_counts = processing.count_objects_and_signals(file_path)
        visualization.plot_counts(object_counts, signal_counts)

# Create the main application window
window = tk.Tk()
window.title("XODR Analysis")
window.geometry("800x600")

# Create the input file field
file_label = tk.Label(window, text="Select XODR File:")
file_label.pack()

# Create the button to browse for the file
browse_button = tk.Button(window, text="Browse", command=process_file)
browse_button.pack()

# Run the application
window.mainloop()
