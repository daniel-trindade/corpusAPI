from fastapi import Request, BackgroundTasks
from fastapi import APIRouter
from fastapi.responses import FileResponse

from scrapers.web_scraper import extract_text
from handlers import delete_file
from funny import generate_funny_name

router = APIRouter(prefix="/web", tags=["web"])

@router.get('/{_:path}')
async def read_item(request: Request, doc_type: str, background_tasks: BackgroundTasks):
    # mudar código para aceitar url sem o http:// ou https://

    filename = generate_funny_name("pdf") if doc_type == "pdf" else generate_funny_name("txt")
    url = request.url._url.split('/', 4)[-1]
    url = url.split("?")[0]

    file_path = extract_text(url, doc_type=doc_type)
    background_tasks.add_task(delete_file, file_path)
    
    return FileResponse(file_path, filename=filename)
    