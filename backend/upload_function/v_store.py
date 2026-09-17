from qdrant_client import QdrantClient
from qdrant_client.models import (Distance,VectorParams,PointStruct)

class QdrantStore:
    def __init__(self,host: str = "localhost",port: int = 6333):
        self.client = QdrantClient(host=host,port=port)
        self.collection_name = "documents"

    