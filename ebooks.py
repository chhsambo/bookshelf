import os
from flask import Flask, render_template

from utils import get_folders, get_files
from helpers import pdf

app = Flask(__name__)

cur_dir = os.getcwd()
print(cur_dir)


@app.get("/")
def home():
    path = os.path.join(cur_dir, "assets")

    folders = get_folders(path)
    files = get_files(path)

    return render_template("browse.html", folders=folders, files=files)


@app.get("/browse/<path:folder_name>")
def browse(folder_name):
    path = os.path.join(cur_dir, "assets", folder_name)

    title = folder_name.replace("/", " ")
    folders = get_folders(path)
    files = get_files(path)

    return render_template(
        "browse.html", title=title, path=folder_name, folders=folders, files=files
    )


@app.get("/view/<path:file_name>")
def view(file_name: str):
    pdf_path = os.path.join("assets", f"{file_name}")

    if file_name.endswith(".pdf"):
        book, book_content = pdf.read_pdf_metadata(pdf_path)

    image_filename = pdf.read_cover(pdf_path)

    # Use filename as title
    if not book["title"]:
        book["title"] = file_name.split(".")[0].replace("-", " ").title()

    return render_template(
        "view.html",
        book=book,
        content=book_content[:20],
        cover_filename=f"images/{image_filename}",
    )


if __name__ == "__main__":
    app.run(debug=True)
