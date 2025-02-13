from fastapi import File, UploadFile, BackgroundTasks
from fastapi import APIRouter
from fastapi.responses import FileResponse

from scrapers.audio_scraper import AudioScraper
from handlers import save_audio_file, delete_file
import os

AudioScraper = AudioScraper("small")

router = APIRouter(prefix="/audio", tags=["audio"])
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post('/')
async def upload_file(doc_type: str, file: UploadFile, background_tasks: BackgroundTasks):
    temp_path = os.path.join(UPLOAD_DIR, file.filename)

    #read file
    content = await file.read()

    save_audio_file(file_path=temp_path, content=content)

    processed_path = AudioScraper.transcribe_audio(temp_path, doc_type)

    output_filename = "arquivo.pdf" if doc_type == "pdf" else "arquivo.txt"

    background_tasks.add_task(delete_file, temp_path)
    background_tasks.add_task(delete_file, processed_path)
    
    return FileResponse(processed_path, filename=output_filename)
    