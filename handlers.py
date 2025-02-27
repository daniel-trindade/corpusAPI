import os
from fpdf import FPDF

import random
import string

def generate_random_string(length: int = 20) -> str:
    """
    Generates a random string of the specified length containing letters and digits.

    Parameters
    ----------
    length : int, optional
        The length of the generated string (default is 20).

    Returns
    -------
    random_string : str
        A randomly generated string of the specified length consisting of ASCII letters and digits.

    Notes
    -----
    - The string is generated by randomly selecting characters from the set of ASCII letters (uppercase and lowercase) and digits.
    - The default length is 20, but this can be adjusted by passing a different value to the `length` parameter.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
    
def delete_file(file_path: str) -> None:
    """
    Deletes a file at the specified path.

    Parameters
    ----------
    file_path : str
        The path to the file to be deleted.

    Returns
    -------
    None

    Notes
    -----
    - If the file cannot be deleted (e.g., due to permissions or non-existence), an error message is printed.
    - No value is returned by the function.
    """
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

def save_file(file_path: str, content: str, doc_type: str = "txt") -> None:
    """
    Saves the provided content to a file in the specified format.

    Parameters
    ----------
    file_path : str
        The path where the file will be saved.
    content : str
        The content to be written into the file.
    doc_type : str, optional
        The type of document to save ("txt" or "pdf", default is "txt").

    Returns
    -------
    None

    Notes
    -----
    - If the document type is "txt", the content is saved as a plain text file.
    - If the document type is "pdf", the content is saved as a PDF file.
    - If an unsupported document type is provided, a `ValueError` is raised.
    - The PDF is encoded using 'latin-1' to ensure compatibility with special characters.
    """
    if doc_type == "txt":
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    elif doc_type == "pdf":
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, content.encode('latin-1', 'replace').decode('latin-1'))
        pdf.output(file_path)
    else:
        raise ValueError("Tipo de documento não suportado. Use 'txt' ou 'pdf'.")
    
def save_audio_file(file_path: str, content: bytes) -> None:
    """
    Saves the provided audio content to a file at the specified path.

    Parameters
    ----------
    file_path : str
        The path where the audio file will be saved.
    content : bytes
        The audio content to be written into the file in binary format.

    Returns
    -------
    None

    Notes
    -----
    - The function ensures that the directory for the file path exists.
    - If the provided content is not in bytes format, a `TypeError` is raised.
    - If an error occurs during file saving, an `OSError` is raised with a relevant message.
    """

    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Check if the content is in bytes format
        if not isinstance(content, bytes):
            raise TypeError("Error: Audio file content must be in bytes format.")

        # Save the file as binary
        with open(file_path, "wb") as f:
            f.write(content)

    except Exception as e:
        raise OSError(f"Failed to save the audio file {file_path}: {e}")