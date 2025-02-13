from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks

from scrapers.youtube_scraper import get_video_transcript, list_languages, translate_video_transcript

from handlers import delete_file
from funny import generate_funny_name

router = APIRouter(prefix="/video", tags=["video"])

@router.get("/")
async def read_item(id_video: str, language_code: str, doc_type: str, background_tasks: BackgroundTasks):
    filename = generate_funny_name("pdf") if doc_type == "pdf" else generate_funny_name("txt")
    transcript_path = get_video_transcript(id_video, language_code, doc_type)
    background_tasks.add_task(delete_file, transcript_path)
    return FileResponse(transcript_path, filename=filename)

@router.get("/language_list")
async def read_item(id_video: str):
    transcript_list = list_languages(id_video)
    return {"video": transcript_list}

@router.get("/translate")
async def read_item(id_video: str, source_language_code: str, target_language_code: str, doc_type: str, background_tasks: BackgroundTasks):
    filename = generate_funny_name("pdf") if doc_type == "pdf" else generate_funny_name("txt")
    transcript_path = translate_video_transcript(id_video, source_language_code, target_language_code)
    background_tasks.add_task(delete_file, transcript_path)
    return FileResponse(transcript_path, filename=filename)