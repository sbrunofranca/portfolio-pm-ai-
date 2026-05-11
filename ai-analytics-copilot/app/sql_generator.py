from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()  # garante leitura do .env

def get_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY não encontrada. Verifique seu .env")

    return Groq(api_key=api_key)


def generate_sql(question: str, schema: str):

    client = get_client()  # <-- cria aqui, na hora de usar

    prompt = f"""
Você é um especialista em SQL.

Schema:
{schema}

Pergunta:
{question}

Gere apenas SQL válido.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content