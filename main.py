#Inicializa o servidor FastAPI em desenvolvimento: fastapi dev main.py
#Inicializa o servidor FastAPI em produção: fastapi run main.py

from fastapi import FastAPI

from video_transcript import get_video_transcript, list_languages, translate_video_transcript

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/video")
async def read_item(id_video: str, language_code: str):
    transcript = get_video_transcript(id_video, language_code)
    return {"video": transcript}

@app.get("/video/language_list")
async def read_item(id_video: str):
    transcript_list = list_languages(id_video)
    return {"video": transcript_list}

@app.get("/video/translate")
async def read_item(id_video: str, source_language_code: str, target_language_code: str):
    transcript = translate_video_transcript(id_video, source_language_code, target_language_code)
    return {"video": transcript}
