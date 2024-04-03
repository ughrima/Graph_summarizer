# import os
# import sys
# import pytesseract 
# from PIL import Image
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import cv2
# import numpy as np

# def preprocess_image(img_path):
#     # Open the image using PIL
#     img = Image.open(img_path)

#     # Convert image to grayscale
#     gray_img = img.convert("L")

#     # Convert PIL image to OpenCV format
#     opencv_img = np.array(gray_img)

#     # Apply thresholding to binarize the image
#     _, binary_img = cv2.threshold(opencv_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

#     return binary_img

# def summarize_bar_graph(png_file):
#     print("Reading image...")  # Debugging output

#     # Preprocess the image
#     processed_img = preprocess_image(png_file)

#     # Extract text from the preprocessed image using Tesseract OCR
#     text = pytesseract.image_to_string(processed_img)

#     # Define the PDF file path
#     pdf_file = os.path.splitext(png_file)[0] + ".pdf"

#     # Create a canvas for PDF generation
#     c = canvas.Canvas(pdf_file, pagesize=letter)

#     # Set font and font size
#     c.setFont("Helvetica", 12)

#     # Write the extracted text to the PDF file
#     c.drawString(100, 750, text)

#     # Save the PDF file
#     c.save()

# if __name__ == "__main__":

#     print("Command-line arguments:", sys.argv)  # Debugging output

#     if len(sys.argv) != 4:
#         print("Usage: python abc.py summarize bar_graph.png")
#         sys.exit(1)

#     _, action, png_file = sys.argv

#     print("Action:", action)  # Debugging output
#     print("PNG file:", png_file)  # Debugging output

#     if action != "summarize":
#         print("Invalid action. Use 'summarize'.")
#         sys.exit(1)

#     # Extract text from the image and save it to a PDF file
#     summarize_bar_graph(png_file)

import os
import sys
import pytesseract 
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import cv2
import numpy as np

# Function to preprocess the image
def preprocess_image(img_path):
    print("preprocessing image...")  # Debugging output

    # Open the image using PIL
    img = Image.open(img_path)

    # Convert image to grayscale
    gray_img = img.convert("L")

    # Convert PIL image to OpenCV format
    opencv_img = np.array(gray_img)

    # Apply thresholding to binarize the image
    _, binary_img = cv2.threshold(opencv_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    print("finished preprocessing image.")  # Debugging output

    return binary_img

#Function to extract text from graph 
def extract_text(image_file):

    text = pytesseract.image_to_string(image_file)
    # print("Extracted text :",text)
    return text

# Function to summarize a bar graph
def summarize_bar_graph(text):
    print("Summarizing...")  # Debugging output

    summary_info = {
        "Title": "Bar Graph Summary",
        "Axis X & Y": text,
    }

    print("Summary :",summary_info)
    return summary_info

# Function to summarize a line graph
def summarize_line_graph(text):

    summary_info = {
        "Title": "Line Graph Summary",
        "Slope": 0.5,
        "Intercept": 10,
        # Add more summary info as needed
    }
    return summary_info

# Function to summarize a pie chart
def summarize_pie_chart(text):

    summary_info = {
        "Title": "Pie Chart Summary",
        "Slices": {
            "Red": 30,
            "Blue": 40,
            "Green": 20,
        }
    }
    return summary_info

# Function to summarize a scatter plot
def summarize_scatter_plot(text):

    summary_info = {
        "Title": "Scatter Plot Summary",
        "Points": [
            {"x": 1, "y": 3},
            {"x": 2, "y": 5},
        ]
    }
    return summary_info

# Function to summarize an area graph
def summarize_area_graph(text):

    summary_info = {
        "Title": "Area Graph Summary",
        "Area": 50,
    }
    return summary_info

# Function to generate PDF report
def generate_pdf_report(summary_info, pdf_filename):
    # Canvas for PDF generation
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Set font and font size
    c.setFont("Helvetica", 12)

    # Save the PDF file
    c.save()

if __name__ == "__main__":
    # Parse command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python abc.py summarize graph_type image.png")
        sys.exit(1)

    _, action, graph_type, image_file = sys.argv

    # Preprocess the image
    preprocessed_image = preprocess_image(image_file)

    extracted_text=extract_text(preprocessed_image)

    # Call the appropriate summarization function based on the specified graph type
    if graph_type == "bargraph":
        summary_info = summarize_bar_graph(extracted_text)
    elif graph_type == "linegraph":
        summary_info = summarize_line_graph(extracted_text)
    elif graph_type == "piechart":
        summary_info = summarize_pie_chart(extracted_text)
    elif graph_type == "scatterplot":
        summary_info = summarize_scatter_plot(extracted_text)
    elif graph_type == "areagraph":
        summary_info = summarize_area_graph(extracted_text)
    else:
        print("Invalid graph type. Supported types: bargraph, linegraph, piechart, scatterplot, areagraph")
        sys.exit(1)

    # Generate PDF report based on the summary information
    generate_pdf_report(summary_info, "summary_report.pdf")
