
from fastapi import FastAPI,UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import logging
from api.routes import router
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger=logging.getLogger("docuchat")


app = FastAPI(name="docuchat", description="A FastAPI application for document chat.", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred."},
    )