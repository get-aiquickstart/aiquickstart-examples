import os
from openai import OpenAI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
MODEL = "gpt-4o-mini"
SYSTEM_PROMPT = (
    "You are a helpful assistant."
)

# TODO: Initialize the OpenAI client
client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=GITHUB_TOKEN
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

# TODO: Create a variable to store the chat history and inistialize it with the system prompt
chat_history: list[dict[str, str]] = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]



class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    content: str


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    # TODO: Get the user's prompt from the ChatRequest
    user_message = {"role": "user", "content": request.prompt}

    # TODO: Append the user's prompt to the chat history
    chat_history.append(user_message)

    # TODO: Call the OpenAI API with the system prompt and chat history
    response = client.chat.completions.create(
        model=MODEL,
        messages=chat_history
    )

    # TODO: Get the assistant's response from the OpenAI API response
    content = response.choices[0].message.content

    # TODO: Create a message for the assistant's response
    assistant_message = {"role": "assistant", "content": content}

    # TODO: Append the assistant's response to the chat history
    chat_history.append(assistant_message)
    
    # TODO: Return the assistant's response as a ChatResponse
    return ChatResponse(response=content)
