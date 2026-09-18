from qdrant_client import QdrantClient
from qdrant_client.models import (Distance,VectorParams,PointStruct)
import uuid
class QdrantService:
    def __init__(self,host: str = "localhost",port: int = 6333):
        self.client = QdrantClient(host=host,port=port)
        self.collection_name = "documents"

    def ensure_collection(self, vector_size: int):
        collections = self.client.get_collections()
        exists = any(
            collection.name == self.collection_name
            for collection in collections.collections
        )
        if exists:
            return
        self.client.create_collection(collection_name=self.collection_name,vectors_config=VectorParams(size=vector_size,distance=Distance.COSINE))
    def insert_chunks(self,chunks: list[dict],vectors: list[list[float]],document_id: str,filename: str):
        points = []
        for chunk, vector in zip(chunks, vectors):
            point = PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "document_id": document_id,
                    "filename": filename,
                    "page_number": chunk["page_number"],
                    "chunk_id": chunk["chunk_id"],
                    "text": chunk["text"],
                },
            )
            points.append(point)
        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )