import os
import requests
import bs4

from handlers import generate_random_string, save_file

def extract_text(url: str, doc_type: str = "txt") -> str:
    """
    Extracts the main text from an HTML page and saves it in the specified format.

    Parameters
    ----------
    url : str
        URL of the webpage to extract text from.
    doc_type : str, optional
        File format for saving the extracted text ("txt" or "pdf", default: "txt").

    Returns
    -------
    file_path : str
        Path to the saved file containing the extracted text.

    Notes
    -----
    - The output file name is generated randomly.
    - The file is saved in the "files/" directory.
    - If the directory does not exist, it is created automatically.
    - The text is cleaned to remove unnecessary whitespace and special characters.
    - If the URL request fails, a `ValueError` is raised.
    """

    save_path = "files/"
    file_name = generate_random_string()

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Erro ao acessar a URL: {url}. Código de status: {response.status_code}")

    #corrige o encoding para evitar erros em caracteres acentuados
    response.encoding = response.apparent_encoding
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    text = soup.get_text()
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    text = " ".join(text.split())

    #verifica se o caminho para salvar o texto já existe. Caso não exista, é criado.
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = os.path.join(save_path, f"{file_name}.{doc_type}")
    
    save_file(file_path, text, doc_type)

    return file_path