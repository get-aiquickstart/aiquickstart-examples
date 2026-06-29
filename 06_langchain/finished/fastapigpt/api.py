import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

MODEL = "gpt-4o-mini"
SYSTEM_PROMPT = (
    "You are a tech analyst that answers questions about big tech companies."
)

llm = ChatOpenAI(
    api_key=os.environ.get("GH_MODELS_PAT", ""),
    model_name=MODEL,
    base_url="https://models.github.ai/inference",
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

chat_history: list = []


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    content: str


prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{prompt}"),
    ]
)

chain = prompt_template | llm | StrOutputParser()


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    content = chain.invoke(
        {
            "chat_history": chat_history,
            "prompt": request.prompt,
        }
    )

    chat_history.append(HumanMessage(content=request.prompt))
    chat_history.append(AIMessage(content=content))

    return ChatResponse(content=content)
