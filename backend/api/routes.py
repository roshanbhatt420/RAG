from fastapi import FastAPI, UploadFile, File, APIRouter
from upload_function import read_pdf 
from pathlib import Path
import shutil
import uuid

router=APIRouter()
@router.get("/")
async def health():
    return {"status": "ok"}



@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    if file.size and file.size > 10 * 1024 * 1024:
        return {"error": "File size exceeds the limit of 10 MB."}

    suffix = Path(file.filename).suffix.lower()

    if suffix != ".pdf":
        return {"error": "Only PDF files are allowed."}

    upload_dir = Path("data/uploads")
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / f"{uuid.uuid4()}.pdf"

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    content = await read_pdf.read_pdf(str(file_path))

    return {
        "filename": file.filename,
        "content": content
    }