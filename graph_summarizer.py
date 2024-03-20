import fitz
import os
import numpy
import cv2
import pytesseract 
from PIL import Image

# -------function to extract graphs from the  the pdf----------

def extract_graphs(pdf_path, output_folder):

    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]

            with open(f"{output_folder}/page_{page_num+1}_image_{img_index+1}.png", "wb") as img_file:
                img_file.write(image_bytes)

    # Close the PDF document
    pdf_document.close()

    

# -----------function to extract text from graph -----------

def extract_text(text_folder,output_folder):
    for filename in os.listdir(output_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path=os.path.join(output_folder,filename)
            img=Image.open(image_path)
            text=pytesseract.image_to_string(img)
            with open(os.path.join(text_folder,f"{os.path.splitext(filename)[0]}.txt"),"w") as text_file:
                text_file.write(text)




pdf_path = "sample3.pdf"
output_folder = "graphs"
text_folder = "extracted_text"
# extract_graphs(pdf_path,output_folder)
extract_text(text_folder, output_folder)
