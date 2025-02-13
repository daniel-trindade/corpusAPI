import whisper
from handlers import save_file, generate_random_string
import os

class AudioScraper:
    def __init__(self, model):
        print("Carregado modelo ...")
        self.model = whisper.load_model(model, device="cpu")
        print("Modelo carregado")

    def transcribe_audio(self, audio_path, doc_type="txt"):
        result = self.model.transcribe(audio_path)

        save_path = "files/"
        file_name = generate_random_string()
        file_path = os.path.join(save_path, f"{file_name}.{doc_type}")
        save_file(file_path, result["text"])

        return file_path

