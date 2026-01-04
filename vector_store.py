from typing import List, Dict
import math


def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (norm1 * norm2 + 1e-10)


class InMemoryVectorStore:
    def __init__(self):
        self.vectors = []
        self.metadata = []

    def add(self, vectors: List[List[float]], metadatas: List[Dict]):
        for v, m in zip(vectors, metadatas):
            self.vectors.append(v)
            self.metadata.append(m)

    def search(self, query_vector: List[float], top_k: int = 3):
        scores = []

        for idx, vector in enumerate(self.vectors):
            score = cosine_similarity(query_vector, vector)
            scores.append((score, self.metadata[idx]))

        scores.sort(key=lambda x: x[0], reverse=True)
        return scores[:top_k]
