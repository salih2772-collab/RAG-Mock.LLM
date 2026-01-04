from embedding_factory import EmbeddingFactory
from vector_store import InMemoryVectorStore
from llm_factory import LLMFactory


class RAGPipeline:
    def __init__(self, store: InMemoryVectorStore):
        self.store = store
        self.embedder = EmbeddingFactory.create(provider="mock")
        self.llm = LLMFactory.create(provider="mock")

    def answer(self, question: str, top_k: int = 3) -> str:
        query_vector = self.embedder.embed([question])[0]
        results = self.store.search(query_vector, top_k=top_k)

        context_parts = []
        for score, meta in results:
            context_parts.append(meta["preview"])

        context = "\n---\n".join(context_parts)

        return self.llm.generate(question=question, context=context)
