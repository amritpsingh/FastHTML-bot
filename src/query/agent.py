# src/query/agent.py

import logging
from pydantic import BaseModel, ConfigDict
from typing import AsyncGenerator, Any, Union

from config.config import config
from config.settings import settings
from src.embedding.embedder import get_embedding_model
from src.storage.vector_store import VectorStore
from src.utils.helpers import get_num_tokens, trim, get_client
from src.llm.response_generator import generate_response

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class QueryResult(BaseModel):
    question: str
    sources: list
    context: list
    answer: Union[AsyncGenerator[str, None], str]  # Can be either an AsyncGenerator or a string
    llm: str

    model_config = ConfigDict(arbitrary_types_allowed=True)

class QueryAgent:
    def __init__(self, embedding_model_name: str = settings.EMBEDDING_MODEL_NAME,
                 llm: str = settings.LLM_MODEL_NAME, temperature: float = 0.1, 
                 max_context_length: int = config.MAX_CONTEXT_LENGTHS[settings.LLM_MODEL_NAME], 
                 system_content: str = "", assistant_content: str = ""):
        self.embedding_model = get_embedding_model(
            embedding_model_name = embedding_model_name,
            model_kwargs={"device": "cuda"},
            encode_kwargs={"device": "cuda", "batch_size": 100}
        )
        self.llm = llm
        self.temperature = temperature
        self.context_length = int(0.5 * max_context_length) - get_num_tokens(system_content + assistant_content)
        self.system_content = system_content
        self.assistant_content = assistant_content
        self.vector_store = VectorStore(embedding_model=self.embedding_model, persist_directory=settings.VECTOR_STORE_DIR)
        self.conversation_history = []  # Initialize conversation history
        self.client = get_client(llm=llm)  # Initialize the client once

    
    async def __call__(self, query: str, num_chunks: int = 5, stream: bool = True) -> QueryResult:
        context_results = await self.vector_store.similarity_search(query=query, k=num_chunks)
        context = [item["text"] for item in context_results]
        sources = [item["source"] for item in context_results]

        # Append the new user query to the conversation history
        self.conversation_history.append({"role": "user", "content": query})
        
         # Create the user content with the conversation history and context
        conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.conversation_history])
        context_text = "\n".join(context)
        
        # Construct the prompt
        prompt = f"{self.system_content}\n\n{conversation_history}\n\nContext:\n{context_text}\n\nPlease provide a concise answer without including 'Assistant:' in the response."
        
        # Ensure the prompt is trimmed properly
        trimmed_prompt = trim(prompt, self.context_length)

        response_generator  = generate_response(
            client=self.client,  # Pass the initialized client
            llm=self.llm,
            temperature=self.temperature,
            stream=stream,
            system_content=self.system_content,
            assistant_content=self.assistant_content,
            user_content=trimmed_prompt
        )

        if stream:
            answer = response_generator 
        else:
            # For non-streaming, collect the entire response
            answer = ""
            async for chunk in response_generator:
                answer += chunk
        
        # Append the assistant's response to the conversation history
        self.conversation_history.append({"role": "assistant", "content": answer})

        return QueryResult(
            question=query,
            sources=sources,
            context=context,
            answer=answer,
            llm=self.llm
        )