import os
import PyPDF2
import fitz


def read_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        metadata = pdf_reader.metadata

        # num_pages = len(pdf_reader.pages)
        # text = ""
        # for page_num in range(num_pages):
        #     page = pdf_reader.pages[page_num]
        #     text += page.extract_text()

    title = metadata.get('/Title', '')
    author = metadata.get('/Author', '')
    creator = metadata.get('/Creator', '')
    producer = metadata.get('/Producer', '')

    return {
        "title": title,
        "author": author,
        "creator": creator,
        # "content": text.replace("\n", "<br>")
    }

    
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
