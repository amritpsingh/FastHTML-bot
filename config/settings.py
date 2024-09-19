# config/settings.py

from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Define the project root path
    PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent

    BASE_URL: str = Field("https://docs.fastht.ml/", env="BASE_URL")
    RAW_DATA_DIR: str = Field(str(PROJECT_ROOT / "data/raw-data"), env="RAW_DATA_DIR")
    PROCESSED_DATA_DIR: str = Field(str(PROJECT_ROOT / "data/processed-data"), env="PROCESSED_DATA_DIR")
    VECTOR_STORE_DIR: str = Field(str(PROJECT_ROOT / "data/docs_db"), env="VECTOR_STORE_DIR")
    CHUNK_SIZE: int = Field(500, env="CHUNK_SIZE")
    CHUNK_OVERLAP: int = Field(50, env="CHUNK_OVERLAP")
    EMBEDDING_MODEL_NAME: str = Field("thenlper/gte-base", env="EMBEDDING_MODEL_NAME")
    LLM_MODEL_NAME: str = Field("meta-llama/Meta-Llama-3.1-70B-Instruct", env="LLM_MODEL_NAME")  #  "mistralai/Mistral-7B-Instruct-v0.3"
    OPENAI_API_BASE: str = Field(..., env="OPENAI_API_BASE")
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    ANYSCALE_API_BASE: str = Field(..., env="ANYSCALE_API_BASE")
    ANYSCALE_API_KEY: str = Field(..., env="ANYSCALE_API_KEY")
    HUGGINGFACEHUB_API_TOKEN: str = Field(..., env="HUGGINGFACEHUB_API_TOKEN")
    DB_CONNECTION_STRING: str = Field(..., env="DB_CONNECTION_STRING")

    class Config:
        env_file = ".env"

settings = Settings()