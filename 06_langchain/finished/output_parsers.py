import os
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    api_key=os.environ.get("GH_MODELS_PAT"),
    model="openai/gpt-4o-mini",
    base_url="https://models.github.ai/inference",
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="You are a tech analyst that answers questions about big tech companies."
        ),
        HumanMessagePromptTemplate.from_template("When was {company} founded?"),
    ],
)

output_parser = StrOutputParser()

prompt = prompt_template.invoke({"company": "Microsoft"})
response = llm.invoke(prompt)
output_parsed = output_parser.parse(response.content)
print(output_parsed)

prompt = prompt_template.invoke({"company": "Apple"})
response = llm.invoke(prompt)
output_parsed = output_parser.parse(response.content)
print(output_parsed)
