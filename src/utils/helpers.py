# src/utils/helpers.py

import openai
from typing import Union
from langchain_huggingface import HuggingFaceEndpoint
import tiktoken
import logging
import psutil
import GPUtil

from config.settings import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def print_resource_usage() -> None:
    """
    Prints the current resource usage of the system.
    """
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    gpus = GPUtil.getGPUs()
    gpu_util = gpus[0].load * 100 if gpus else 0
    logger.info(f"CPU: {cpu_percent}%, Memory: {mem_percent}%, GPU: {gpu_util}%")

        
def get_client(llm: str) -> Union[openai.OpenAI, HuggingFaceEndpoint]:
    """
    Returns the appropriate client based on the language model identifier.

    Args:
        llm (str): The language model identifier.

    Returns:
        Union[openai.OpenAI, HuggingFaceEndpoint]: The client object.
    """
    if llm.startswith("gpt"):
        return openai.OpenAI(base_url=settings.OPENAI_API_BASE, api_key=settings.OPENAI_API_KEY)
    else:
        return HuggingFaceEndpoint(huggingfacehub_api_token=settings.HUGGINGFACEHUB_API_TOKEN, repo_id=llm)


def get_num_tokens(text: str) -> int:
    """
    Returns the number of tokens in the given text.

    Args:
        text (str): The text to tokenize.

    Returns:
        int: The number of tokens.
    """
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

def trim(text: str, max_context_length: int) -> str:
    """
    Trims the text to fit within the maximum context length.

    Args:
        text (str): The text to trim.
        max_context_length (int): The maximum context length.

    Returns:
        str: The trimmed text.
    """
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    trimmed_tokens = tokens[:max_context_length]
    trimmed_text = enc.decode(trimmed_tokens)
    
    # Ensure the trimmed text ends at a complete sentence
    if "." in trimmed_text:
        trimmed_text = trimmed_text.rsplit(".", 1)[0] + "."
    return trimmed_text