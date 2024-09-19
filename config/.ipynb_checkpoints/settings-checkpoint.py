# config/settings.py

from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    BASE_URL: str = "https://docs.fastht.ml/"
    RAW_DATA_DIR: Path = BASE_DIR / "data" / "raw-data"
    PROCESSED_DATA_DIR: Path = BASE_DIR / "data" / "processed-data"
    VECTOR_STORE_DIR: Path = BASE_DIR / "data" / "docs_db"
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50
    EMBEDDING_MODEL_NAME: str = "thenlper/gte-base"

    class Config:
        env_file = ".env"
        extra = "allow"  # Allow extra fields

settings = Settings()