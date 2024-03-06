import os
import fitz   # PyMuPDF


def read_pdf_metadata(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Get metadata
    metadata = pdf_document.metadata
    
    # Close the PDF document
    pdf_document.close()
    
    return metadata


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
