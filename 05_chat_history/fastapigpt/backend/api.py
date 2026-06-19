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

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

# TODO: Create a variable to store the chat history


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    content: str


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    # TODO: Get the user's prompt from the ChatRequest
    # TODO: Append the user's prompt to the chat history
    # TODO: Call the OpenAI API with the system prompt and chat history
    # TODO: Append the assistant's response to the chat history
    # TODO: Return the assistant's response as a ChatResponse
    pass
