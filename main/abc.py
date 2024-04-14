


import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import pytesseract 
from PIL import Image, ImageEnhance, ImageFilter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to extract text from graph 
def extract_text(image_file):
    text = pytesseract.image_to_string(cv2.imread(image_file))
    return text

# Function to summarize a bar graph
def summarize_bar_graph(text, bar_heights):
    print("Summarizing bar graph...")  

    # Extracting relevant information from text
    summary_sentences = []
    x_axis_values = []

    # Extract numerical values from the text as potential Y-axis values
    y_axis_values = [int(val) for val in text.split() if val.isdigit()]

    # Extracting categories from the text
    categories_line = text.split("Bar Graph")[-1].split("Xaxis")[0].strip()
    categories = [val.strip() for val in categories_line.split()]

    # Check if categories and Y-axis values are extracted successfully
    if not categories:
        print("Error: Unable to extract categories from the graph text.")
        return {
            "Title": "Bar Graph Summary",
            "Summary Sentences": ["Unable to extract categories from the graph text."],
            "Total heights": None
        }

    if not y_axis_values:
        print("Error: Unable to extract valid Y-axis values from the graph text.")
        return {
            "Title": "Bar Graph Summary",
            "Summary Sentences": ["Unable to extract valid Y-axis values from the graph text."],
            "Total heights": None
        }

    # Calculate the total heights
    total_heights = sum(y_axis_values)

    # Generate summary sentences for each category
    for i, category in enumerate(categories):
        # Append the summary sentence with the reversed bar height
        summary_sentences.append(f"{category} has the corresponding bar height = {bar_heights[i]} on the Y-axis")
        # Append the X-axis value
        x_axis_values.append(f"{category}")
    summary_sentences.append(f"Total heights (in terms of Y axis): {total_heights}")

    summary_info = {
        "Title": "Bar Graph Summary",
        "Summary Sentences": summary_sentences,
        "Y Axis Values": y_axis_values,
        "X Axis Values": x_axis_values,
        "Bar Heights": bar_heights
    }

    return summary_info

# Function to generate PDF report
def generate_pdf_report(summary_info, pdf_filename):
    # Canvas for PDF generation
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Set font and font size
    c.setFont("Helvetica", 12)

    # Set initial y-coordinate for text
    y = 700

    # Write the summary information to the PDF
    for key, value in summary_info.items():
        if key == "Summary Sentences":
            for sentence in value:
                c.drawString(100, y, sentence)
                y -= 20  # Move down 20 units for the next line
        else:
            c.drawString(100, y, f"{key}: {value}")
            y -= 20  # Move down 20 units for the next line

    # Save the PDF file
    c.save()

if __name__ == "__main__":
    # Parse command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python abc.py summarize graph_type image.png")
        sys.exit(1)

    _, action, graph_type, image_file = sys.argv

    # Load the image
    image = cv2.imread(image_file)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define range of blue color in HSV
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    blue_bars = cv2.bitwise_and(image, image, mask=mask)

    # Convert the blue bars image to grayscale
    gray = cv2.cvtColor(blue_bars, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Extract heights of the bars and associate them with Y-axis values
    bar_heights = []

    # Set to store unique heights encountered
    unique_heights = set()

    # Iterate over each column of the blue bars image
    for col in range(blue_bars.shape[1]):
        # Find the indices of non-zero elements in the column
        indices = np.nonzero(blue_bars[:, col])[0]
        if len(indices) > 0:
            # Calculate the height of the bar in this column
            bar_height = max(indices) - min(indices)
            # Check if this height is unique
            if bar_height not in unique_heights:
                # Add the unique height to the list and set
                bar_heights.append(bar_height)
                unique_heights.add(bar_height)

    extracted_text = extract_text(image_file)

    # Call the appropriate summarization function based on the specified graph type
    if graph_type == "bargraph":
        summary_info = summarize_bar_graph(extracted_text, bar_heights)
    else:
        print("Invalid graph type. Supported types: bargraph")
        sys.exit(1)

    # Generate PDF report based on the summary information
    generate_pdf_report(summary_info, "summary_report.pdf")
