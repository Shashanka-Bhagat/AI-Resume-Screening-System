import pdfplumber

def extract_text(pdf_source):
    text=''
    with pdfplumber.open(pdf_source) as pdf:
        for page in pdf.pages:
             text += page.extract_text() + "\n"
    return text
