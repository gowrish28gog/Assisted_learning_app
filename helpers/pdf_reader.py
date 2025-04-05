from pypdf import PdfReader

# This module provides a function to extract text from a PDF file.
# The function takes the path to the PDF file as input and returns the extracted text as a string.  
def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts plain text from a PDF file.

    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    try:
        reader = PdfReader(pdf_path)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text.strip()
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""