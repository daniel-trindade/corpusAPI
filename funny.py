import random
from handlers import generate_random_string

def generate_funny_name(extension):
    """Generate a funny name based on the seed."""
    adjectives = ["maluco", "bizarro", "zueiro", "doido", "biruta", "tonto", "esquisito", "tretado"]
    nouns = ["pamonha", "tatu", "chinelão", "coquinho", "jiló", "jabuti", "pirulito", "pangaré"]
    
    adj = random.choice(adjectives)
    subst = random.choice(nouns)
    random_id = generate_random_string(5)

    return f"{adj}_{subst}_{random_id}.{extension}"