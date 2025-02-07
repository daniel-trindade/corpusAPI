#Inicializa o servidor FastAPI em desenvolvimento: fastapi dev main.py
#Inicializa o servidor FastAPI em produção: fastapi run main.py

from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import FileResponse

from scrapers.youtube_scraper import get_video_transcript, list_languages, translate_video_transcript
from scrapers.web_scraper import extract_text

from handlers import delete_file

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/video")
async def read_item(id_video: str, language_code: str, doc_type: str, background_tasks: BackgroundTasks):
    filename = "arquivo.pdf" if doc_type == "pdf" else "arquivo.txt"
    transcript_path = get_video_transcript(id_video, language_code, doc_type)
    background_tasks.add_task(delete_file, transcript_path)
    return FileResponse(transcript_path, filename=filename)

@app.get("/video/language_list")
async def read_item(id_video: str):
    transcript_list = list_languages(id_video)
    return {"video": transcript_list}

@app.get("/video/translate")
async def read_item(id_video: str, source_language_code: str, target_language_code: str, doc_type: str, background_tasks: BackgroundTasks):
    filename = "arquivo.pdf" if doc_type == "pdf" else "arquivo.txt"
    transcript_path = translate_video_transcript(id_video, source_language_code, target_language_code)
    background_tasks.add_task(delete_file, transcript_path)
    return FileResponse(transcript_path, filename=filename)

@app.get('/web/{_:path}')
async def read_item(request: Request, doc_type: str, background_tasks: BackgroundTasks):
    # mudar código para aceitar url sem o http:// ou https://

    filename = "arquivo.pdf" if doc_type == "pdf" else "arquivo.txt"
    url = request.url._url.split('/', 4)[-1]
    url = url.split("?")[0]

    file_path = extract_text(url, doc_type=doc_type)
    background_tasks.add_task(delete_file, file_path)
    
    return FileResponse(file_path, filename=filename)
    