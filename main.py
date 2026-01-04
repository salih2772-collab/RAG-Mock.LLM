from fastapi import FastAPI
from pydantic import BaseModel

from data_loader import load_documents
from chunker import chunk_documents
from embedding_factory import EmbeddingFactory
from vector_store import InMemoryVectorStore
from rag_pipeline import RAGPipeline


app = FastAPI(title="RAG API (Mock)")

# ---- Build knowledge base at startup ----
documents = load_documents("data")
chunks = chunk_documents(documents)

texts = [c["content"] for c in chunks]
metadata = [
    {
        "source": c["source"],
        "chunk_id": c["chunk_id"],
        "preview": c["content"][:200]
    }
    for c in chunks
]

embedder = EmbeddingFactory.create(provider="mock")
vectors = embedder.embed(texts)

store = InMemoryVectorStore()
store.add(vectors, metadata)

rag = RAGPipeline(store)


# ---- API schema ----
class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str


@app.post("/ask", response_model=AnswerResponse)
def ask_question(req: QuestionRequest):
    answer = rag.answer(req.question)
    return {"answer": answer}
