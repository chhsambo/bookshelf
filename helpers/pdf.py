import os
import fitz   # PyMuPDF


def read_pdf_metadata(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Get metadata
    metadata = pdf_document.metadata

    # Initialize an empty string to store the text content
    content = []
    
    # Iterate through each page in the PDF
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document.load_page(page_number)
        
        # Extract text from the page
        content.append(page.get_text())
    
    # Close the PDF document
    pdf_document.close()
    
    return metadata, content


def read_cover(pdf_path):
    filename = os.path.basename(pdf_path)

    # Open the PDF document
    doc = fitz.open(pdf_path)

    # Get the first page
    page = doc.load_page(0)  # Page index starts from 0

    # Extract the page as a pixmap (image)
    # You can adjust the matrix parameter for different scaling and DPI
    pixmap = page.get_pixmap(matrix=fitz.Matrix(50/72, 50/72))

    image_filename = f"{filename}.png"
    # Save the pixmap as an image (with desired format, e.g., PNG)
    pixmap.save(os.path.join("static", "images", image_filename))
    return image_filename
