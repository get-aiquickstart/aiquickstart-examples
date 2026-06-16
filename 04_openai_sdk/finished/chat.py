import os 

GH_MODELS_PAT = os.getenv("GH_MODELS_PAT")

print(f"GitHub Developer Token: ****{GH_MODELS_PAT[-4:]}")

from openai import OpenAI

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=GH_MODELS_PAT
)

with open("../../03_github_models/customer_service_prompt.txt", "r") as f:
    customer_service_prompt = "".join(f.readlines())

system_message = {
    "role": "system",
    "content": customer_service_prompt
}

user_message = {
    "role": "user",
    "content": "I was charged twice for the same item. What do I do?"
}

response = client.chat.completions.create(
    messages=[system_message, user_message],
    model="openai/gpt-4.1-mini",
    temperature=0.3,
    top_p=0.7,
)

print(response.choices[0].message.content)