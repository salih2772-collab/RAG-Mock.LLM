from typing import List


class BaseEmbedding:
    def embed(self, texts: List[str]) -> List[List[float]]:
        raise NotImplementedError


class MockEmbedding(BaseEmbedding):
    def embed(self, texts: List[str]) -> List[List[float]]:
        return [[float(len(text))] * 10 for text in texts]


class EmbeddingFactory:
    @staticmethod
    def create(provider: str, **kwargs) -> BaseEmbedding:
        provider = provider.lower()

        if provider == "mock":
            return MockEmbedding()

        raise ValueError(f"Unknown embedding provider: {provider}")
