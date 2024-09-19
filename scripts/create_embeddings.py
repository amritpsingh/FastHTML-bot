# scripts/create_embeddings.py

import json
from pathlib import Path
from src.embedding.embedder import Embedder
from src.storage.vector_store import VectorStore
from config.settings import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    """
    Main function to create embeddings for processed documents and add them to the vector store.
    """
    embedder = Embedder(settings.EMBEDDING_MODEL_NAME)
    vector_store = VectorStore(embedder.embedding_model, settings.VECTOR_STORE_DIR)

    processed_data_dir = Path(settings.PROCESSED_DATA_DIR)

    for json_file in processed_data_dir.glob("*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            chunks = json.load(f)
        
        embedded_chunks = embedder.embed_chunks(chunks)
        vector_store.add_documents(embedded_chunks)
        logger.info(f"Processed and added embeddings for {json_file}")

if __name__ == "__main__":
    main()