from pypdf import PdfReader
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a given PDF file.

    Args:
        pdf_file: A file-like object representing the PDF.

    Returns:
        A string containing the extracted text.
    """
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip() if text else "No text found in the PDF."
    except Exception as e:
        return f"Error extracting text: {e}"

