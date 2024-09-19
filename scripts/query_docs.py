# scripts/query_docs.py

import sys
import os
import asyncio
import typer
from rich.console import Console
from rich.panel import Panel

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import settings
from src.query.agent import QueryAgent
import logging

#from huggingface_hub import login
# Login to Hugging Face and save the token to git credentials helper
#login(add_to_git_credential=True)


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = typer.Typer()
console = Console()

@app.command()
def main(
    #query: str = typer.Option(..., prompt=True, help="The query to search for in the documentation"),
    stream: bool = typer.Option(True, help="Whether to stream the response or not")
):
    """
    Query the FastHTML documentation using natural language.
    """
    async def run_query():
        system_content = "Answer the query using the context provided. Be succinct."
        agent = QueryAgent(
            embedding_model_name=settings.EMBEDDING_MODEL_NAME,
            llm=settings.LLM_MODEL_NAME,
            system_content=system_content
        )

        while True:
            query = input("Query: ")
            if query.lower() in ["exit", "quit"]:
                break

            result = await agent(query=query, stream=stream)
            
            console.print(Panel("Answer:", style="bold green"))
            answer = ""

            if stream:
                async for chunk in result.answer:
                    answer += chunk
                    console.print(chunk, end="")
            else:
                async for chunk in result.answer:
                    answer += chunk
                console.print(Panel(answer, title="Answer", expand=False))
            
            console.print("\n")
            
            console.print(Panel("\n".join(result.sources), title="Sources", expand=False))

    asyncio.run(run_query())
    #async_to_sync(run_query)()

if __name__ == "__main__":
    app()