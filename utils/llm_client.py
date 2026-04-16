import requests
from openai import OpenAI
import os
from config import MODEL_OPENAI, MODEL_OLLAMA

# OpenAI client
openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

OLLAMA_URL = "http://localhost:11434/api/generate"


def call_llm(prompt, provider):
    if provider == "openai":
        print(f"\n🧠 [LLM CALL] Provider: OpenAI | Model: {MODEL_OPENAI}")

        response = openai_client.chat.completions.create(
            model=MODEL_OPENAI,
            messages=[
                {"role": "system", "content": "You are an AI agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    elif provider == "ollama":
        print(f"\n🧠 [LLM CALL] Provider: Ollama | Model: {MODEL_OLLAMA}")

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_OLLAMA,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    else:
        raise ValueError("Invalid LLM provider selected")