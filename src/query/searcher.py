# src/query/searcher.py

from typing import List, Dict
from src.storage.vector_store import VectorStore

class Searcher:
    """
    A class to perform search queries on the vector store.

    Attributes:
        vector_store (VectorStore): The vector store instance.
    """
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def search(self, query: str, k: int = 5) -> List[Dict[str, str]]:
        """
        Searches the vector store for similar documents.

        Args:
            query (str): The search query.
            k (int): The number of results to return.

        Returns:
            List[Dict[str, str]]: The search results.
        """
        return self.vector_store.similarity_search(query, k)