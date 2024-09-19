
# src/embedding/embedder.py

import os
from typing import List, Dict
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_embedding_model(embedding_model_name: str, model_kwargs: Dict, encode_kwargs: Dict) -> object:
    """
    Returns the appropriate embedding model based on the model name.

    Args:
        embedding_model_name (str): The name of the embedding model.
        model_kwargs (Dict): The keyword arguments for the model.
        encode_kwargs (Dict): The keyword arguments for encoding.

    Returns:
        object: The embedding model.
    """
    if embedding_model_name == "text-embedding-ada-002":
        embedding_model = OpenAIEmbeddings(
            model = embedding_model_name,
            openai_api_base = os.environ["OPENAI_API_BASE"],
            openai_api_key = os.environ["OPENAI_API_KEY"]
        )
    else:
        embedding_model = HuggingFaceEmbeddings(
            model_name = embedding_model_name,
            model_kwargs = model_kwargs,
            encode_kwargs = encode_kwargs
        )
    return embedding_model

class Embedder:
    """
    A class to embed text chunks using a specified embedding model.

    Attributes:
        embedding_model (object): The embedding model.
    """
    def __init__(self, model_name: str):
        self.embedding_model = get_embedding_model(
            model_name,
            model_kwargs={"device": "cuda"},
            encode_kwargs={"device": "cuda", "batch_size": 100}
        )

    async def embed_chunks(self, chunks: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Embeds text chunks asynchronously.

        Args:
            chunks (List[Dict[str, str]]): The text chunks to embed.

        Returns:
            List[Dict[str, str]]: A list of embedded text chunks.
        """
        texts = [chunk["text"] for chunk in chunks]
        embeddings = await self.embedding_model.aembed_documents(texts)
        return [
            {"text": chunk["text"], "source": chunk["source"], "embedding": embedding}
            for chunk, embedding in zip(chunks, embeddings)
        ]