import sys
import os
import asyncio
import uvicorn
from pydantic import BaseModel
from typing import List

from fasthtml.common import *
from fasthtml.svg import *


# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import settings
from src.query.agent import QueryAgent

# Configure logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# UI assests
svg1 = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5" /> <path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4" /></svg>'
svg2 = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>'
assistant_img = "https://user-images.githubusercontent.com/78873223/152768592-825f945e-86b4-4f51-b9e5-cd4d254003f6.png"
user_img = "https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"


# Set up the app, including daisyui and tailwind for the chat component
tlink = Script(src="https://cdn.tailwindcss.com"),
dlink = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
app = FastHTML(hdrs=(tlink, dlink, picolink), ws_hdr=True, cls="p-4 max-w-3xl mx-auto min-h-screen")


# Set up a chat model
agent = QueryAgent(
        embedding_model_name=settings.EMBEDDING_MODEL_NAME,
        llm=settings.LLM_MODEL_NAME,
        system_content="Answer the query using the context provided. Be succinct."
    )

# Chat message component (renders a chat bubble)
def ChatMessage(msg, user):
    bubble_class = "chat-bubble-accent" if user else 'chat-bubble-warning'
    chat_class = "chat-end" if user else 'chat-start'
    avatar_img = user_img if user else assistant_img
    return Div(cls=f"chat {chat_class}")(
               Div(cls="chat-image avatar")(
                   Div(cls="w-10 rounded-full")(
                       Img(src=avatar_img, alt="Avatar")
                   )
               ),
               Div('User' if user else 'Assistant', cls="chat-header"),
               Div(msg, cls=f"chat-bubble {bubble_class}"),
               Div("Delivered" if user else "Seen", cls="chat-footer opacity-50")
           )

# The input field for the user message. Also used to clear the
# input field after sending a message via an OOB swap
def ChatInput():
    return Input(name='msg', id='msg-input', placeholder="Type a message",
                 cls="input input-bordered w-full", hx_swap_oob='true')

# The main screen
@app.get
def index():
    page = Div(Label(
                Span(show(NotStr(svg1)), cls="label-text"),
                Input(type="checkbox", value="dim", cls="toggle theme-controller"),
                Span(show(NotStr(svg2)), cls="label-text"),
            cls="flex cursor-pointer gap-2"),
            Form(hx_ext="ws", ws_connect="/wscon", ws_send="")(
                Div(id="chatlist", cls="chat-box h-[73vh] overflow-y-auto  p-4 bg-white rounded-lg shadow-md"),
                    Div(cls="flex space-x-2 mt-2")(
                        Group(ChatInput(), Button("Send", cls="btn btn-primary"))
                    )
                ),
    cls="container")
    return Titled('Chatbot Demo', page)

@app.ws("/wscon")
async def websocket_endpoint(msg: str, send):
    # Send the user message to the user (updates the UI right away)
    await send(Div(ChatMessage(msg, True), hx_swap_oob='beforeend', id="chatlist"))

    # Send the clear input field command to the user
    await send(ChatInput())

    # Simulate a delay
    await asyncio.sleep(1)

    # Get response from chat model
    result = await agent(query=msg, stream=False)  # Pass only the current message to the agent
    
    # Send the assistant's response to the user
    await send(Div(ChatMessage(result.answer, False), hx_swap_oob='beforeend', id="chatlist"))

if __name__ == "__main__":
    uvicorn.run("chat_app1:app", host="0.0.0.0", port=5001, reload=True)