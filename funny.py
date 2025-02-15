import random
from handlers import generate_random_string

def generate_funny_name(extension: str) -> str:
    """
    Generates a random funny file name with the given extension.

    Parameters
    ----------
    extension : str
        The file extension to be used in the generated name.

    Returns
    -------
    file_name : str
        A randomly generated funny file name in the format "<adjective>_<noun>_<random_id>.<extension>".

    Notes
    -----
    - The name consists of a randomly chosen adjective and noun from predefined lists.
    - A random string of 5 characters is appended to ensure uniqueness.
    - The final name is formatted as "<adjective>_<noun>_<random_id>.<extension>".
    """

    adjectives = ["maluco", "bizarro", "zueiro", "doido", "biruta", "tonto", "esquisito", "tretado"]
    nouns = ["pamonha", "tatu", "chinelão", "coquinho", "jiló", "jabuti", "pirulito", "pangaré"]
    
    adj = random.choice(adjectives)
    subst = random.choice(nouns)
    random_id = generate_random_string(5)

    return f"{adj}_{subst}_{random_id}.{extension}"