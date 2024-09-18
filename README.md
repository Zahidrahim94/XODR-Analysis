# XODR-Analysis tool
# XODR Analysis

This is a simple Python application that allows you to analyze XODR (OpenDRIVE) files. It provides a graphical user interface (GUI) built using the `tkinter` library for selecting an XODR file and displays visualizations of the object and signal counts within the file using `matplotlib`.
![Screenshot from 2023-05-11 18-33-27](https://github.com/user-attachments/assets/2f57548c-a3b9-49a2-8e4b-b5eff660f190)

![Screenshot from 2023-05-11 18-39-25](https://github.com/user-attachments/assets/0a1e5db6-3a48-4be2-b69f-57c7af5d68ce)


## Requirements

- Python 3.x
- `tkinter` library
- `xml.etree.ElementTree` module
- `matplotlib` library

## Usage

1. Make sure you have Python 3.x installed on your system.

2. Install the required libraries by running the following command:
   ```
   pip install matplotlib
   ```

3. Save the provided code in a Python file, for example, `xodr_analysis.py`.

4. Run the script using the following command:
   ```
   python xodr_analysis.py
   ```

5. The application window titled "XODR Analysis" will open.

6. Click the "Browse" button to select an XODR file for analysis. Only files with the `.xodr` extension will be displayed in the file selection dialog.

7. After selecting a file, the application will process the file and generate two plots:

   - Object Counts: A bar chart showing the counts of different object types present in the XODR file.
   - Signal Counts: A bar chart showing the counts of different signal subtypes present in the XODR file.

8. The plots will be displayed in separate windows using `matplotlib`.

## How It Works

The code consists of two main parts: file processing and visualization.

### File Processing

The `count_objects_and_signals` function takes an XODR file path as input and parses the XML data using the `xml.etree.ElementTree` module. It counts the occurrences of different object types and signal subtypes within the XODR file and returns the counts as dictionaries.

### Visualization

The `plot_counts` function takes the object and signal counts as input and creates two bar charts using `matplotlib`. The first chart shows the counts of different object types, and the second chart shows the counts of different signal subtypes. The charts are displayed using `plt.show()`.

The `process_file` function is triggered when the "Browse" button is clicked. It opens a file selection dialog using `tkinter` and calls the `count_objects_and_signals` function with the selected file path. Then, it calls the `plot_counts` function to visualize the counts.

The main application window is created using `tkinter`. It consists of a label, "Select XODR File," and a "Browse" button. The window is displayed using `window.mainloop()`.

## License

This code is released under the MIT License. Please see the [LICENSE](LICENSE) file for more details.
