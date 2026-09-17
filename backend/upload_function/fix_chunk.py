
from .chunker import chunk_text
def chuck_text(pages:list[dict],chunk_size:int=1000 , overlap:int=100)->list[dict]:
    """
    Function to chunk the text into smaller pieces.
    Args:
        text (list[dict]): List of dictionaries containing page number and text.
        chunk_size (int): Size of each chunk. Default is 1000 characters.
    Returns:
        list[dict]: List of dictionaries containing page number and chunked text.
    """
    chunks=[]
    chunk_id=0
    for page in pages:
        page_chunks = chunk_text(page["text"],chunk_size=chunk_size,overlap=overlap)
        for chunk in page_chunks:
            chunks.append({"chunk_id": chunk_id,"page_number": page["page_number"],"text": chunk})
            chunk_id += 1
    return chunks