import sys
import pytesseract 
from PIL import Image, ImageEnhance, ImageFilter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import cv2
import numpy as np
import matplotlib.pyplot as plt
import textacy.extract

# Function to extract text from graph 
def extract_text(image_file, graph_type):
    text = pytesseract.image_to_string(cv2.imread(image_file))

    print("Extracted text:", text)
    return text

# Function to summarize a bar graph
def summarize_bar_graph(text):
    print("Summarizing bar graph...")  

    # Extracting relevant information from text
    summary_sentences = []

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
            "Total Sales": None
        }

    if not y_axis_values:
        print("Error: Unable to extract valid Y-axis values from the graph text.")
        return {
            "Title": "Bar Graph Summary",
            "Summary Sentences": ["Unable to extract valid Y-axis values from the graph text."],
            "Total Sales": None
        }

    # Calculate the total sales
    total_sales = sum(y_axis_values)

    # Generate summary sentences for each category
    for i, category in enumerate(categories):
        summary_sentences.append(f"{category} on the Y-axis is {y_axis_values[i]}")

    summary_sentences.append(f"Total Sales: {total_sales}")

    summary_info = {
        "Title": "Bar Graph Summary",
        "Summary Sentences": summary_sentences,
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

    extracted_text = extract_text(image_file, graph_type)

    # Call the appropriate summarization function based on the specified graph type
    if graph_type == "bargraph":
        summary_info = summarize_bar_graph(extracted_text)
    else:
        print("Invalid graph type. Supported types: bargraph")
       
