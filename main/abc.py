import sys
import pytesseract 
from PIL import Image, ImageEnhance, ImageFilter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(img_path):
    print("Preprocessing image...")

    # Read the image using OpenCV
    image = cv2.imread(img_path)
    orig = image.copy()

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to remove noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, 30, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort the contours from left to right
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    for contour in contours:
        # Approximate the contour
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        # If the contour has four vertices, it is likely a text region
        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save the preprocessed image to a file
    preprocessed_image_path = "preprocessed_image.png"
    cv2.imwrite(preprocessed_image_path, image)

    print(f"Preprocessed image saved as '{preprocessed_image_path}'.")

    print("Finished preprocessing image.")

    # Return the original image for further processing
    return orig, preprocessed_image_path


# Function to extract text from graph 
def extract_text(image_file, graph_type):
    if graph_type == "piechart":
        # Convert image to grayscale
        gray_image = cv2.cvtColor(cv2.imread(image_file), cv2.COLOR_BGR2GRAY)

        # Threshold the image to get binary image
        _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Invert the binary image
        inverted_image = cv2.bitwise_not(binary_image)

        # Extract text from inverted image
        text = pytesseract.image_to_string(inverted_image)
    else:
        # Extract text from original image
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

# Function to summarize a pie chart
def summarize_pie_chart(text):
    print("Summarizing pie chart...")  

    summary_info = {
        "Title": "Pie Chart Summary",
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

    # Preprocess the image
    orig_image, preprocessed_image = preprocess_image(image_file)

    plt.imshow(cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB))
    plt.title("Preprocessed Image")
    plt.show()

    # Extract text from preprocessed image
    extracted_text = extract_text(preprocessed_image, graph_type)

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
