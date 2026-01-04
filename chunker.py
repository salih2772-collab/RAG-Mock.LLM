from typing import List, Dict


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100
) -> List[str]:
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

        if start < 0:
            start = 0

    return chunks


def chunk_documents(documents: List[Dict]) -> List[Dict]:
    all_chunks = []

    for doc in documents:
        chunks = chunk_text(doc["content"])

        for idx, chunk in enumerate(chunks):
            all_chunks.append({
                "content": chunk,
                "source": doc["source"],
                "type": doc["type"],
                "chunk_id": idx
            })

    return all_chunks
