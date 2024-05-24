import tkinter as tk
from tkinter import filedialog
import csv
import math
import matplotlib.pyplot as plt

class TraverseAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("Traverse Analyzer")

        self.file_label = tk.Label(master, text="Select Traverse Data File:")
        self.file_label.grid(row=0, column=0)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=1)

        self.point1_label = tk.Label(master, text="Point 1:")
        self.point1_label.grid(row=1, column=0)

        self.point1_entry = tk.Entry(master)
        self.point1_entry.grid(row=1, column=1)

        self.point2_label = tk.Label(master, text="Point 2:")
        self.point2_label.grid(row=2, column=0)

        self.point2_entry = tk.Entry(master)
        self.point2_entry.grid(row=2, column=1)

        self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze_traverse)
        self.analyze_button.grid(row=3, column=0, columnspan=2)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.file_label.config(text=file_path)
            self.traverse_data = self.read_traverse_data(file_path)

    def read_traverse_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip header if present
                traverse_data = []
                for row in csv_reader:
                    if len(row) != 3:
                        print("Error: Invalid data format in the CSV file.")
                        return None
                    try:
                        point_number = int(row[0])
                        easting = float(row[1])
                        northing = float(row[2])
                        traverse_data.append((point_number, easting, northing))
                    except ValueError:
                        print("Error: Invalid data format in the CSV file.")
                        return None
            return traverse_data
        except FileNotFoundError:
            print("Error: File not found.")
            return None

    def analyze_traverse(self):
        if not hasattr(self, 'traverse_data'):
            print("Error: Traverse data not loaded.")
            return

        try:
            point1 = int(self.point1_entry.get())
            point2 = int(self.point2_entry.get())

            if not all(point in [point[0] for point in self.traverse_data] for point in [point1, point2]):
                print("Error: Invalid point numbers.")
                return

            point1_data = next(point for point in self.traverse_data if point[0] == point1)
            point2_data = next(point for point in self.traverse_data if point[0] == point2)

            distance = self.calculate_distance(point1_data, point2_data)
            bearing = self.calculate_bearing(point1_data, point2_data)

            print(f"Distance between point {point1} and point {point2}: {distance}")
            print(f"Bearing from point {point1} to point {point2}: {bearing} degrees")
        except ValueError:
            print("Error: Invalid point numbers.")

    def calculate_distance(self, point1, point2):
        dx = point2[1] - point1[1]
        dy = point2[2] - point1[2]
        return math.sqrt(dx**2 + dy**2)

    def calculate_bearing(self, point1, point2):
        dx = point2[1] - point1[1]
        dy = point2[2] - point1[2]
        bearing = math.atan2(dy, dx)
        return math.degrees(bearing)

root = tk.Tk()
app = TraverseAnalyzerApp(root)
root.mainloop()
