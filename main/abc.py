# import os
# import sys
# import pytesseract 
# from PIL import Image
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import cv2
# import numpy as np

# # Function to preprocess the image
# def preprocess_image(img_path):
#     print("preprocessing image...")  # Debugging output

#     # Open the image using PIL
#     img = Image.open(img_path)

#     # Convert image to grayscale
#     gray_img = img.convert("L")

#     # Convert PIL image to OpenCV format
#     opencv_img = np.array(gray_img)

#     # Apply thresholding to binarize the image
#     _, binary_img = cv2.threshold(opencv_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

#     print("finished preprocessing image.")  # Debugging output

#     return binary_img

# #Function to extract text from graph 
# def extract_text(image_file):

#     text = pytesseract.image_to_string(image_file)
#     print("Extracted text :",text)
#     return text



# # Function to summarize a bar graph
# def summarize_bar_graph(text):
#     print("Summarizing...")  # Debugging output

#     summary_info = {
#         "Title": "Bar Graph Summary",
#         "Axis X & Y": text,
#     }

#     # print("Summary :",summary_info)
#     return summary_info

# # Function to summarize a line graph
# def summarize_line_graph(text):

#     summary_info = {
#         "Title": "Line Graph Summary",
#         "Slope": 0.5,
#         "Intercept": 10,
#         # Add more summary info as needed
#     }
#     return summary_info

# # Function to summarize a pie chart
# def summarize_pie_chart(text):

#     summary_info = {
#         "Title": "Pie Chart Summary",
#         "Slices": text,
#     }
#     # print("Summary :",summary_info)
#     return summary_info

# # Function to summarize a scatter plot
# def summarize_scatter_plot(text):

#     summary_info = {
#         "Title": "Scatter Plot Summary",
#         "Points": [
#             {"x": 1, "y": 3},
#             {"x": 2, "y": 5},
#         ]
#     }
#     return summary_info

# # Function to summarize an area graph
# def summarize_area_graph(text):

#     summary_info = {
#         "Title": "Area Graph Summary",
#         "Area": 50,
#     }
#     return summary_info

# # Function to generate PDF report
# def generate_pdf_report(summary_info, pdf_filename):
#     # Canvas for PDF generation
#     c = canvas.Canvas(pdf_filename, pagesize=letter)

#     # Set font and font size
#     c.setFont("Helvetica", 12)

#     # Save the PDF file
#     c.save()

# if __name__ == "__main__":
#     # Parse command-line arguments
#     if len(sys.argv) != 4:
#         print("Usage: python abc.py summarize graph_type image.png")
#         sys.exit(1)

#     _, action, graph_type, image_file = sys.argv

#     # Preprocess the image
#     preprocessed_image = preprocess_image(image_file)
#     cv2.imshow("Preprocessed Image", preprocessed_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows() 

#     extracted_text=extract_text(preprocessed_image) #print after every function 
#     #library substitute 

#     # Call the appropriate summarization function based on the specified graph type
#     if graph_type == "bargraph":
#         summary_info = summarize_bar_graph(extracted_text)
#     elif graph_type == "linegraph":
#         summary_info = summarize_line_graph(extracted_text)
#     elif graph_type == "piechart":
#         summary_info = summarize_pie_chart(extracted_text)
#     elif graph_type == "scatterplot":
#         summary_info = summarize_scatter_plot(extracted_text)
#     elif graph_type == "areagraph":
#         summary_info = summarize_area_graph(extracted_text)
#     else:
#         print("Invalid graph type. Supported types: bargraph, linegraph, piechart, scatterplot, areagraph")
#         sys.exit(1)

#     # Generate PDF report based on the summary information
#     generate_pdf_report(summary_info, "summary_report.pdf")


import os
import sys
import pytesseract 
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import cv2
import numpy as np
# import easyocr 

# Function to preprocess the image
def preprocess_image(img_path):
    print("preprocessing image...")  # Debugging output

    # Open the image using PIL
    img = Image.open(img_path)

    # Convert image to grayscale
    gray_img = img.convert("L")

    # Apply thresholding to binarize the image
    _, binary_img = cv2.threshold(np.array(gray_img), 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    print("finished preprocessing image.")  # Debugging output

    return binary_img

# Function to extract text from graph 
def extract_text(image_file):

    text = pytesseract.image_to_string(image_file)
    print("Extracted text :",text)
    return text

# reader = easyocr.Reader(['en'])

# def extract_text(image_file):
#     # Perform OCR on the image
#     result = reader.readtext(image_file)

#     # Extract and concatenate the recognized text
#     text = ' '.join([res[1] for res in result])

#     print("Extracted text:", text)
#     return text

# Function to summarize a bar graph
def summarize_bar_graph(text):
    print("Summarizing...")  # Debugging output

    summary_info = {
        "Title": "Bar Graph Summary",
        "Axis X & Y": text,
    }

    # print("Summary :",summary_info)
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
        "Slices": text,
    }
    # print("Summary :",summary_info)
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

    # Convert preprocessed image to PIL image
    pil_image = Image.fromarray(preprocessed_image)

    # Display preprocessed image
    cv2.imshow("Preprocessed Image", preprocessed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

    extracted_text = extract_text(pil_image)  # Extract text from preprocessed image

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
