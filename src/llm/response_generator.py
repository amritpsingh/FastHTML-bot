# src/llm/response_generator.py

import openai
from typing import Union, AsyncGenerator
import logging
import asyncio
from langchain_huggingface import HuggingFaceEndpoint
from src.utils.helpers import get_client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def response_stream(chat_completion: Union[AsyncGenerator, str, openai.OpenAI, HuggingFaceEndpoint], llm: str) -> AsyncGenerator[str, None]:
    """
    Streams the response from the chat completion.

    Args:
        chat_completion (Union[AsyncGenerator, openai.OpenAI]): The chat completion object.
        llm (str): The language model identifier.

    Yields:
        AsyncGenerator[str, None]: The streamed response content.
    """
    if llm.startswith("gpt"):
        async for chunk in chat_completion:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content
    elif isinstance(chat_completion, str):
        # For non-streaming responses
        yield chat_completion
    elif isinstance(chat_completion, HuggingFaceEndpoint):
        # For HuggingFaceEndpoint, we can't stream directly, so we'll simulate streaming
        response = chat_completion(llm)
        for chunk in response.split():
            yield chunk + " "
            await asyncio.sleep(0.05)  # Simulate streaming delay
    else:
        # For other types of models (if any)
        yield chat_completion

async def prepare_response(chat_completion: Union[AsyncGenerator, str, openai.OpenAI, HuggingFaceEndpoint], stream: bool, llm: str) -> AsyncGenerator[str, None]:
    """
    Union[str, AsyncGenerator[str, None]]
    Prepares the response from the chat completion.

    Args:
        chat_completion (Union[AsyncGenerator, openai.OpenAI]): The chat completion object.
        stream (bool): Whether to stream the response.
        llm (str): The language model identifier.

    Returns:
        Union[str, AsyncGenerator[str, None]]: The prepared response.
    """
    if stream:
        async for chunk in response_stream(chat_completion, llm):
            yield chunk
    else:
        if llm.startswith("gpt"):
            yield chat_completion.choices[0].message.content
        elif isinstance(chat_completion, str):
            yield chat_completion
        elif isinstance(chat_completion, HuggingFaceEndpoint):
            yield chat_completion(llm)
        else:
            # For other types of models (if any)
            yield chat_completion


async def generate_response(
    client, llm: str, temperature: float = 0.0, stream: bool = True, 
    system_content: str = "", assistant_content: str = "", user_content: str = "", 
    max_retries: int = 1, retry_interval: int = 60
) -> Union[str, AsyncGenerator[str, None]]:
    """
    Generates a response from the language model.

    Args:
        client: The initialized client.
        llm (str): The language model identifier.
        temperature (float): The temperature for the response generation.
        stream (bool): Whether to stream the response.
        system_content (str): The system content for the prompt.
        assistant_content (str): The assistant content for the prompt.
        user_content (str): The user content for the prompt.
        max_retries (int): The maximum number of retries.
        retry_interval (int): The interval between retries.

    Returns:
        Union[str, AsyncGenerator[str, None]]: The generated response.
    """
    retry_count = 0
    
    prompt = [("system", system_content), ("assistant", assistant_content), ("user", user_content)]
    messages = [{"role": role, "content": content} for role, content in prompt if content]

    while retry_count <= max_retries:
        try:
            if llm.startswith("gpt"):
                chat_completion = await client.chat.completions.create(
                    model=llm,
                    temperature=temperature,
                    stream=stream,
                    messages=messages,
                )
            else:
                # For HuggingFaceEndpoint
                full_prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
                chat_completion = await client.ainvoke(
                    model=llm,
                    temperature=temperature,
                    streaming=stream,
                    input=full_prompt,
                )

            async for chunk in prepare_response(chat_completion, stream=stream, llm=llm):
                yield chunk
            break  # Exit the loop after yielding the complete response

        except Exception as e:
            logger.error(f'Exception: {e}')
            await asyncio.sleep(retry_interval)
            retry_count += 1
    
    yield ""  # Return empty string if all retries fail