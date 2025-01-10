import pdfplumber

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"  # Extract text page by page
    return text

file_path = "..\Dataset\Papers\P001.pdf"
pdf_text = extract_text_from_pdf(file_path)
print(pdf_text)