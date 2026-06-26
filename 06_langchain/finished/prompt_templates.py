import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI



llm = ChatOpenAI(
    api_key=os.environ.get("GH_MODELS_PAT"),
    model="openai/gpt-4o-mini",
    base_url="https://models.github.ai/inference",
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a tech analyst that answers questions about big tech companies."),
    ("user", "When was {company} founded?"),
    ],
)

prompt = prompt_template.invoke({"company": "Microsoft"})
response = llm.invoke(prompt)
print(response.content)

prompt = prompt_template.invoke({"company": "Apple"})
response = llm.invoke(prompt)
print(response.content)
