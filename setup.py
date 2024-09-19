# setup.py

from setuptools import setup, find_packages

setup(
    name="fasthtml-docs-bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "tenacity",
        "tqdm",
        "pydantic",
        "langchain",
        "langchain-openai",
        "langchain-huggingface",
        "langchain-chroma",
        "psutil",
        "gputil",
    ],
    entry_points={
        "console_scripts": [
            "download-docs=scripts.download_docs:main",
            "process-docs=scripts.process_docs:main",
            "create-embeddings=scripts.create_embeddings:main",
            "query-docs=scripts.query_docs:main",
        ],
    },
)
