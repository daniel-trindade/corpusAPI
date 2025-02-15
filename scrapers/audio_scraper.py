import whisper
from handlers import save_file, generate_random_string
import os

class AudioScraper:
    def __init__(self, model):
        print("Carregado modelo ...")
        self.model = whisper.load_model(model, device="cpu")
        print("Modelo carregado")

    def transcribe_audio(self, audio_path: str, doc_type: str = "txt") -> str:
        """
        Transcribe an audio file and save the transcription as a text file.

        Parameters
        ----------
        audio_path : str
            Path to the audio file to be transcribed.
        doc_type : str, optional
            File format for saving the transcription (default: "txt").

        Returns
        -------
        file_path : str
            Path to the saved file containing the transcription.

        Notes
        -----
        - The output file name is generated randomly.
        - The file is saved in the "files/" directory.
        - Transcription is performed using the model instance stored in `self.model`.
        """
        
        result = self.model.transcribe(audio_path)

        save_path = "files/"
        file_name = generate_random_string()
        file_path = os.path.join(save_path, f"{file_name}.{doc_type}")
        save_file(file_path, result["text"])

        return file_path

