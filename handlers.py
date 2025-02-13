import os
from fpdf import FPDF

import random
import string

def generate_random_string(length=20) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
    
def delete_file(file_path: str) -> None:
    """Função para excluir o arquivo após o envio."""
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Erro ao excluir {file_path}: {e}")

def save_file(file_path: str, content: str, doc_type: str = "txt") -> None:
    """Função para salvar o conteúdo em um arquivo."""

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
    
def save_audio_file(file_path: str, content: bytes):
    """
    Saves an audio file as a binary file on the filesystem.

    Args:
        file_path (str): Path where the file will be saved.
        content (bytes): Binary content of the audio file.

    Raises:
        TypeError: If the content is not in bytes format.
        OSError: If there is an error while saving the file.
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