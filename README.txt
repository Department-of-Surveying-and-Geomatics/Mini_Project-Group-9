Traverse Analyzer

Introduction:
The Traverse Analyzer is a Python-based tool designed to analyze and visualize land survey traverse data. It provides functionalities to read traverse data from a CSV file, calculate basic traverse characteristics, compute distance and bearing between two points, and visualize the traverse using Matplotlib.

Functionality:
1. Data Input and Parsing:
   - Reads traverse data from a CSV file containing point number, Easting, and Northing coordinates.
   - Handles potential errors in the data format.

2. Traverse Analysis:
   - Calculates basic traverse characteristics such as the total number of points, minimum and maximum Easting and Northing values.
   - Computes the distance and bearing between any two points provided by the user.

3. Data Visualization:
   - Creates a scatter plot using Matplotlib to visualize the traverse.
   - Marks each data point with its corresponding point number on the plot.

Usage Instructions:
1. Install Python (if not already installed) from https://www.python.org/.
2. Clone or download the Traverse Analyzer repository.
3. Open a terminal or command prompt and navigate to the directory containing the Traverse Analyzer files.
4. Run the GUI application by executing the command: `python traverse_analyzer_gui.py`.
5. Click the "Browse" button to select the traverse data file (in CSV format).
6. Enter the point numbers of two points in the respective entry fields.
7. Click the "Analyze" button to compute the distance and bearing between the selected points.

Additional Details:
- Ensure that the traverse data file is in CSV format and contains three columns: point number, Easting, and Northing.
- The computed distance is in the same unit as the coordinate values (e.g., meters, feet).
- The bearing is measured clockwise from the North direction in degrees.
- The GUI provides a simple and user-friendly interface for interacting with the tool.

Note: This tool is developed as part of a mini project to evaluate proficiency in Python programming for land surveying applications.

For any issues or inquiries, please contact [r203829m@students.msu.ac.zw].
