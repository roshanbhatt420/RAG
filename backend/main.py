
from fastapi import FastAPI,UploadFile, File
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
import logging
from api.routes import router
from fastapi.responses import JSONResponse
from upload_function.embedding import EmbeddingService
from upload_function.v_store import QdrantService

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
@asynccontextmanager
async def lifespan(app: FastAPI):
    embedding_service = EmbeddingService()
    qdrant_service = QdrantService()
    # Ensure the Qdrant collection exists
    vector_size = (embedding_service.model.get_sentence_embedding_dimension())
    qdrant_service.ensure_collection(vector_size)
    app.state.embedding_service = embedding_service
    app.state.qdrant_service = qdrant_service
    print("Embedding model loaded")
    print("Qdrant collection ready")

    yield

    print("Application shutting down")
app.include_router(router)


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred."},
    )