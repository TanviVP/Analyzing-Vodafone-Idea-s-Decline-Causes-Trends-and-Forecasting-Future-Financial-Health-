import os
import fitz  # PyMuPDF
from tkinter import Tk, filedialog

# Properly handle Tkinter root window
root = Tk()
root.withdraw()  # Hide the main window

try:
    pdf_folder = filedialog.askdirectory(title="Select folder containing PDF files")
finally:
    root.destroy()  # Ensure the root window is destroyed

if not pdf_folder:
    print("No folder selected. Exiting.")
    exit()

# Create output folder inside selected folder
output_folder = os.path.join(pdf_folder, "converted_txt")
os.makedirs(output_folder, exist_ok=True)

# Process each PDF
pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

if not pdf_files:
    print("No PDF files found in the selected folder.")
    exit()

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    txt_path = os.path.join(output_folder, pdf_file.replace(".pdf", ".txt"))

    doc = fitz.open(pdf_path)
    all_text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        all_text += f"\n\n--- Page {page_num + 1} ---\n"
        all_text += page.get_text()

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(all_text)

    print(f"Converted: {pdf_file} --> {txt_path}")

print("\nAll PDFs converted to text and saved in:", output_folder)
