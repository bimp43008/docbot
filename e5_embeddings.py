from langchain_core.embeddings import Embeddings
from sentence_transformers import SentenceTransformer

class E5Embeddings(Embeddings):
    def __init__(self, model_name: str = "intfloat/multilingual-e5-small"):
        self.model = SentenceTransformer(model_name)


    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self.model.encode(
            [f"passage: {t}" for t in texts],
            normalize_embeddings=True,
        )

    def embed_query(self, text: str) -> list[float]:
        return self.model.encode(
            [f"query: {text}"],
            normalize_embeddings=True,
        )[0]
