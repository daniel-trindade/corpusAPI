#Inicializa o servidor FastAPI em desenvolvimento: fastapi dev main.py
#Inicializa o servidor FastAPI em produção: fastapi run main.py

from fastapi import FastAPI

from video_transcript import get_video_transcript

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/video/{id_video}")
async def read_item(id_video: str):
    transcript = get_video_transcript(id_video)
    return {"video": transcript}