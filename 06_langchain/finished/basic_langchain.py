import os
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    api_key=os.environ.get("GH_MODELS_PAT"),
    model="openai/gpt-4o-mini",
    base_url="https://models.github.ai/inference",
)

response = llm.invoke("When was Microsoft founded?")

print(response.content)

