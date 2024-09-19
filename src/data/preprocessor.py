# src/data/preprocessor.py

from typing import List, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Preprocessor:
    """
    A class to preprocess text sections by chunking them into smaller parts.

    Attributes:
        chunk_size (int): The size of each chunk.
        chunk_overlap (int): The overlap between chunks.
    """
    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", " ", ""],
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )

    def chunk_section(self, section: Dict[str, str]) -> List[Dict[str, str]]:
        """
        Chunks a text section into smaller parts.

        Args:
            section (Dict[str, str]): The section to chunk.

        Returns:
            List[Dict[str, str]]: A list of chunked sections.
        """
        chunks = self.text_splitter.create_documents(
            texts=[section["text"]],
            metadatas=[{
                "source": section["source"],
                "previous_section": section.get("previous_section"),
                "next_section": section.get("next_section"),
                "metadata": section.get("metadata")
            }]
        )
        return [{
            "text": chunk.page_content,
            "source": chunk.metadata["source"],
            "previous_section": chunk.metadata["previous_section"],
            "next_section": chunk.metadata["next_section"],
            "metadata": chunk.metadata["metadata"]
        } for chunk in chunks]