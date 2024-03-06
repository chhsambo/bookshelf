import os
from flask import Flask, render_template
from ebooklib import epub

from utils import get_folders, get_files
from helpers import pdf 

app = Flask(__name__)

cur_dir = os.getcwd()
print(cur_dir)


@app.get("/")
def home():
    path = os.path.join(cur_dir, "assets")
    data = {}
    
    folders = get_folders(path)
    data["folders"] = folders
    
    files = get_files(path)
    data["files"] = files
    
    return render_template("index.html", data=data)


# @app.get("/view/<file_name>.epub")
@app.get("/view/<file_name>")
def view(file_name):
    data = {}
    path = os.path.join(cur_dir, "assets", file_name)
    if os.path.isfile(path):
        data["title"] = file_name

    pdf_path = os.path.join("assets", f"{file_name}")

    if file_name.endswith(".pdf"):
        metadata = pdf.read_pdf_metadata(pdf_path)
        print(metadata)

    image_filename = pdf.read_cover(pdf_path)

    data["book"] = metadata
    data["cover_filename"] = f'images/{image_filename}'

    return render_template("view.html", data=data)


@app.get("/browse/<folder_name>")
def browse(folder_name):
    data = {}
    path = os.path.join(cur_dir, "assets", folder_name)

    folders = get_folders(path)
    data["folders"] = folders

    files = get_files(path)
    data["files"] = files
    data["title"] = folder_name

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
