# src/storage/vector_store.py

import os
from pathlib import Path
from typing import List, Dict
from langchain_chroma import Chroma
from langchain_core.documents import Document
import logging

from config.settings import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VectorStore:
    """
    A class to manage vector storage using Chroma.

    Attributes:
        vector_store (Chroma): The Chroma vector store instance.
    """
    def __init__(self, embedding_model, persist_directory: str):
        self.vector_store = Chroma(
            collection_name="fasthtml_docs_db",
            embedding_function=embedding_model,
            persist_directory=persist_directory
        )

    async def add_documents(self, documents: List[Dict[str, str]]):
        """
        Adds documents to the vector store.

        Args:
            documents (List[Dict[str, str]]): The documents to add.
        """
        docs = [
            Document(page_content=doc["text"], metadata={"source": doc["source"]})
            for doc in documents
        ]
        await self.vector_store.aadd_documents(docs)
        logger.info(f"Added {len(docs)} documents to the vector store")

    async def similarity_search(self, query: str, k: int = 5) -> List[Dict[str, str]]:
        """
        Performs a similarity search on the vector store.

        Args:
            query (str): The search query.
            k (int): The number of results to return.

        Returns:
            List[Dict[str, str]]: The search results.
        """
        results = await self.vector_store.asimilarity_search_with_score(query, k=k)
        return [
            {
                "text": doc.page_content,
                "source": doc.metadata.get("source", ""),
                "score": score
            }
            for doc, score in results
        ]