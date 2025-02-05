import os
import requests
import bs4

from handlers import generate_random_string, save_file

def extract_text(url: str, doc_type: str = "txt") -> str:
    """
    Extrai o texto principal da página HTML, retorna como string e salva no formato especificado.

    :param url: URL da página para extração do texto.
    :param doc_type: Tipo de documento para salvar o texto ("txt" ou "pdf").
    :param save_path: Caminho para salvar o arquivo extraído.
    :return: O texto extraído da página.
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