import sys
import pytesseract 
from PIL import Image, ImageEnhance, ImageFilter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to extract text from graph 
def extract_text(image_file, graph_type):

    text = pytesseract.image_to_string(cv2.imread(image_file))

    print("Extracted text:", text)
    return text

# Function to summarize a bar graph
def summarize_bar_graph(text):
    print("Summarizing bar graph...")  

    summary_info = {
        "Title": "Bar Graph Summary",
        "Extracted Text": text,
    }

    return summary_info

# Function to summarize a line graph
def summarize_line_graph(text):
    print("Summarizing line graph...")  

    summary_info = {
        "Title": "Line Graph Summary",
        "Extracted Text": text,
    }

    return summary_info


# Function to summarize a scatter plot
def summarize_scatter_plot(text):
    print("Summarizing scatter plot...")  

    summary_info = {
        "Title": "Scatter Plot Summary",
        "Extracted Text": text,
    }

    return summary_info

# Function to summarize an area graph
def summarize_area_graph(text):
    print("Summarizing area graph...")  

    summary_info = {
        "Title": "Area Graph Summary",
        "Extracted Text": text,
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
    elif graph_type == "linegraph":
        summary_info = summarize_line_graph(extracted_text)
    elif graph_type == "scatterplot":
        summary_info = summarize_scatter_plot(extracted_text)
    elif graph_type == "areagraph":
        summary_info = summarize_area_graph(extracted_text)
    else:
        print("Invalid graph type. Supported types: bargraph, linegraph, scatterplot, areagraph")
        sys.exit(1)

    # Generate PDF report based on the summary information
    generate_pdf_report(summary_info, "summary_report.pdf")

