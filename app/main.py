#Inicializa o servidor FastAPI em desenvolvimento: fastapi dev app/main.py
#Inicializa o servidor FastAPI em produção: fastapi run main.py

from fastapi import FastAPI
from app.routers import video, web, audio

app = FastAPI()

app.include_router(video.router)
app.include_router(web.router)
app.include_router(audio.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
