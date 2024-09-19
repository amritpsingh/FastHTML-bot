import sys
import os
import asyncio
import uvicorn
from fasthtml.common import *
from pydantic import BaseModel
from typing import List


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

nav = Div(
        Div( A('FastHTML Chatbot', cls='btn btn-ghost text-xl'), cls='flex-1'),
        Div( Label(show(NotStr(svg1)), Input(type='checkbox', value='dim', cls='toggle theme-controller'), show(NotStr(svg2)), cls='flex cursor-pointer gap-2'),
            cls='flex-none'),
        cls='navbar bg-base-300'
    )

# Set up the app, including daisyui and tailwind for the chat component
tlink = Script(src="https://cdn.tailwindcss.com"),
dlink = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
app = FastHTML(hdrs=(tlink, dlink, picolink), ws_hdr=True, cls="min-h-screen flex flex-col")


# Embedded CSS
css = """
body {
    background-color: #F0F0F0; /* Anti-Flash White */
    color: #2f4f4f; /* DarkSlateGray */
    height: 100vh; /* Ensure body covers full viewport height */
    margin: 0;
    display: flex;
    flex-direction: column;
}

.container {
    width: 80%;
    height: calc(100vh - 40px); /* Full height with margin */
    margin: 20px auto; /* Center the container with margin */
    display: flex;
    flex-direction: column;
}

header, footer {
    background-color: #b0c4de; /* LightSteelBlue */
    color: #2f4f4f; /* DarkSlateGray */
}

a {
    color: #4682b4; /* SteelBlue */
}

button {
    background-color: #f5cf89; /* Buff */
    color: #2f4f4f; /* DarkSlateGray */
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #6495ed; /* CornflowerBlue */
}

.btn-primary {
    background-color: #f5cf89; /* Buff */
    color: #2f4f4f; /* DarkSlateGray */
}

.navbar {
    background-color: #f5cf89; /* Buff */
    border-radius: 10px; /* Rounded corners */
    margin-bottom: 20px; /* Space below navbar */
    padding: 10px; /* Add padding for better appearance */
}

.chat-box {
    background-color: #FCFAF7; /* Floral White */
    flex-grow: 1; /* Allow chat-box to grow and fill available space */
    overflow-y: auto;
}

.chat-bubble-user {
    background-color: #C9E4EC; /* Columbia Blue */
    color: #2f4f4f; /* DarkSlateGray */
}

.chat-bubble-bot {
    background-color: #C0EEDE; /* Aero Blue */
    color: #2f4f4f; /* DarkSlateGray */
}

.theme-controller {
    display: flex;
    align-items: center;
}

.theme-controller input[type="checkbox"] {
    width: 40px;
    height: 20px;
    appearance: none;
    background-color: #ccc;
    border-radius: 10px;
    position: relative;
    outline: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

.theme-controller input[type="checkbox"]:checked {
    background-color: #87cefa; /* LightSkyBlue */
}

.theme-controller input[type="checkbox"]::before {
    content: '';
    position: absolute;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background-color: #fff;
    top: 1px;
    left: 1px;
    transition: transform 0.3s;
}

.theme-controller input[type="checkbox"]:checked::before {
    transform: translateX(20px);
}
"""


class Message(BaseModel):
    role: str
    content: str

messages: List[Message] = []

# Chat message component (renders a chat bubble)
def ChatMessage(msg_idx, **kwargs):
    msg = messages[msg_idx]
    bubble_class = "chat-bubble-user" if msg['role'] == 'user' else 'chat-bubble-bot'
    chat_class = "chat-end" if msg['role'] == 'user' else 'chat-start'
    avatar_img = user_img if msg['role'] == 'user' else assistant_img
    return Div(Div(cls="chat-image avatar")(
                   Div(cls="w-10 rounded-full")(
                       Img(src=avatar_img, alt="Avatar")
                   )
               ),
               #Div(msg['role'], cls="chat-header"),
               Div(msg['content'],
                   id=f"chat-content-{msg_idx}", # Target if updating the content
                     cls=f"chat-bubble {bubble_class}"),
               id=f"chat-message-{msg_idx}", # Target if replacing the whole message
               cls=f"chat {chat_class}", **kwargs)

# The input field for the user message. 
# Also used to clear the input field after sending a message via an OOB swap
def ChatInput() -> str:
    return Input(type="text", name='msg', id='msg-input', placeholder="Type a message", 
                 cls="input input-bordered w-full", hx_swap_oob='true')

# The main screen
@app.route("/")
def get():
    page = Body(Div(
                Style(css),  # Include the CSS here
                nav,
                Div(*[ChatMessage(msg_idx) for msg_idx, msg in enumerate(messages)],
                    id="chatlist", cls="chat-box flex-grow overflow-y-auto p-4 rounded-lg shadow-md"),
                Form(Group(ChatInput(), Button("Send", cls="btn btn-primary")),
                    ws_send=True, hx_ext="ws", ws_connect="/wscon",
                    cls="flex space-x-2 mt-2",
                ), 
                cls="flex flex-col container"),
            cls="flex flex-col")
    return Title('FastHTML Chatbot'), page

@app.ws("/wscon")
async def websocket_endpoint(msg:str, send):

    # Send the user message to the user (updates the UI right away)
    messages.append({"role":"user", "content":msg.rstrip()})
    await send(Div(ChatMessage(len(messages)-1), hx_swap_oob='beforeend', id="chatlist"))

    # Send the clear input field command to the user
    await send(ChatInput())

    # Simulate a delay
    #await asyncio.sleep(1)

    # Set up a chat model
    agent = QueryAgent(
        embedding_model_name=settings.EMBEDDING_MODEL_NAME,
        llm=settings.LLM_MODEL_NAME,
        system_content="Answer the query using the context provided. Be succinct."
    )
    # Get response from chat model
    result = await agent(query=msg, stream=True)  # Pass only the current message to the agent
    messages.append({"role":"assistant", "content":""})
    await send(Div(ChatMessage(len(messages)-1), hx_swap_oob='beforeend', id="chatlist"))

    # Fill in the message content
    async for chunk in result.answer:
        messages[-1]["content"] += chunk
        await send(Span(chunk, id=f"chat-content-{len(messages)-1}", hx_swap_oob='beforeend'))

if __name__ == "__main__":
    uvicorn.run("chat_app:app", host="0.0.0.0", port=5001, reload=True)